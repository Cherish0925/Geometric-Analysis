# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 44,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step44_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step44_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify, as a careful geometric analyst, the two new results in Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md (Theorem A: cover-independent perturbative coercivity of the Einstein defect P=∫|Ric°|² and of the monopole Nijenhuis energy near compact complex-hyperbolic surfaces; Proposition Π: pocket refinement of the almost-Kähler profile inequality AKΓ). The computation is in workspace/scripts/step44_perturbative_ke.py with output workspace/data/step44_perturbative_ke.json. Check specifically: (1) the Koiso Bochner identity <L_E h,h> = ||d^∇h||² + <(-λ - R̊)h,h> for TT h on Einstein manifolds (normalization of ||d^∇ h||², sign of R̊ convention: R̊h=-h on trace-free tensors of the unit sphere), and the computed spectrum R̊ = -2 (J-invariant, dim 3), +4 (J-anti, dim 6) on CH² with holomorphic sectional curvature -4 (λ=-6), giving pointwise gap 2 = |λ|/3; whether this agrees with the known infinitesimal rigidity of ball quotients and whether the gap is genuinely Γ-independent. (2) the linearized Seiberg–Witten analysis (G4): cancellation of first-order cross terms when ∇Φ₀=0 with gauge coefficient -1/2, the potential eigenvalues (1/2 on 1-forms, 2, 1, 0,0 on spinors at s=-4), and the claim that the two zero modes on Φ₀^⊥≅Λ^{0,2}≅K^{-1} are lifted by the Kodaira/Landau identity with |iΛF|=2|λ|; check whether the use of ||d^*a||²+||d^+a||² ≥ (1/2)<Δ_d a,a> loses a needed term, and whether a spectral gap of 1/2 is really cover independent. (3) the proof sketch of Theorem A: the conformal slice g=e^{2f}(g_Γ+k), the claim that P and the monopole direction depend on f only through df (exact conformal formulas), uniform Hölder inverses via lifting along the exponential map without injectivity radius bounds, the cubic remainder bounds, and the comparability 2P ≤ R ≤ C'P using Theorem N (Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md). Identify any gap that would make the constant Γ-dependent or the theorem false, and repair it if possible. (4) Proposition Π: the two-region Jensen argument, the minimum 6D² of 2x²+(3y-2x)² on y-x=D, the identities σ̄-δ̄=(ℓ/2V)(1-θ), the final bound 2/(3-2φ), and the interpretation (tiny-area Burns spheres aligned with ω save at first order iff s*>0 since R⁺(ω̂,ω̂)=s*/4); compare with AKΓ in Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md. (5) Judge the scope paragraph: whether the stated obstacles to the blow-up/localized version (bulk monopole selection, local Einstein deformations) are the real ones, and whether some stronger statement about near-minimizers on X_Γ#k CP̄² does follow. Give corrected statements where needed; do not invent literature.

## Integrated Scientific Memo

# Verification memo

## Overall verdict

The algebraic core of Step 44 is mostly correct:

- the Koiso identity and the \(\mathbb{CH}^2\) curvature-operator spectrum are correct;
- the linearized Seiberg–Witten Clifford calculation, including the gauge coefficient \(-\tfrac12\) and the listed algebraic potentials, is correct in the script’s normalization;
- Proposition \(\Pi\) and its constant \(2/(3-2\varphi)\) are correct.

However, Theorem A as stated is not proved and one assertion is false:

1. the displayed G4 coercive inequality double-counts the \(\psi_\perp\) gradient term;
2. the argument for \(\Gamma\)-uniform Hölder inverses is insufficient;
3. G4 and Theorem N use different spinor normalizations;
4. the deduction
   \[
   2P\le R
   \]
   from Theorem N is wrong, and no lower bound \(R\ge cP\) can hold in general;
5. consequently the claimed comparison \(P\asymp R\) is false. The valid perturbative relation is only
   \[
   R\le CP.
   \]

The global \(L^2\) Einstein coercivity is genuinely cover-independent. The analogous \(L^2\) gap for the gauge-fixed monopole linearization is also cover-independent. What remains unproved is a cover-uniform nonlinear branch in the stated uniformly local Hölder topology.

---

## 1. Koiso identity and the \(\mathbb{CH}^2\) tensor gap

Use
\[
(d^\nabla h)_{ijk}=\nabla_i h_{jk}-\nabla_jh_{ik},
\qquad
|d^\nabla h|^2=\frac12\sum_{ijk}(d^\nabla h)_{ijk}^2.
\]
For a TT tensor on an Einstein manifold, \(\operatorname{Ric}=\lambda g\), integration by parts and commutation of derivatives give
\[
\|d^\nabla h\|^2
=\|\nabla h\|^2-\langle\mathring Rh,h\rangle+\lambda\|h\|^2.
\]
Therefore, with
\[
L_E=\nabla^*\nabla-2\mathring R,
\]
one has exactly
\[
\boxed{\;
\langle L_Eh,h\rangle
=\|d^\nabla h\|^2+
\langle(-\lambda-\mathring R)h,h\rangle .
\;}
\]
If the full ordered-index norm \(\sum_{ijk}|d^\nabla h_{ijk}|^2\) is used instead, the first term has coefficient \(1/2\).

The curvature convention is consistent with the stated sphere test. For sectional curvature \(+1\),
\[
(\mathring Rh)_{ij}=R_{ikjl}h_{kl}
=(\operatorname{tr}h)g_{ij}-h_{ij},
\]
so \(\mathring Rh=-h\) on \(S^2_0\).

For the complex-space-form tensor in the script, direct algebra gives, on trace-free symmetric tensors,
\[
\mathring R=
\begin{cases}
-2I,&h(J\cdot,J\cdot)=h,\quad \dim_{\mathbb R}=3,\\
+4I,&h(J\cdot,J\cdot)=-h,\quad \dim_{\mathbb R}=6,
\end{cases}
\]
when the holomorphic sectional curvature is \(-4\). Since \(\lambda=-6\),
\[
-\lambda-\max\operatorname{spec}\mathring R=6-4=2=\frac{|\lambda|}{3}.
\]
After scaling to \(s=-4\), hence \(\lambda=-1\),
\[
\boxed{\;
\langle L_Eh,h\rangle\ge\frac13\|h\|^2
\qquad(h\ {\rm TT}).
\;}
\]

This agrees with infinitesimal rigidity of compact ball quotients. The potentially binding \(J\)-anti-invariant sector is precisely the sector associated with complex-structure variation, and the positive Bochner margin excludes a TT kernel. The estimate is a pointwise curvature inequality followed by integration; hence its \(L^2\) constant is independent of \(\Gamma\), including along finite covers. No quotient spectral gap is being assumed.

The stronger primitive-\((1,1)\) estimate on the \(J\)-invariant sector is also consistent:
\[
L_E\leftrightarrow\Delta_d-2\lambda
\quad\Longrightarrow\quad
\langle L_Eh,h\rangle\ge2|\lambda|\|h\|^2.
\]

Uniform \(H^2\) control of TT tensors can be obtained globally without injectivity-radius-dependent charts. Since the quotient is locally symmetric, \(\nabla\operatorname{Rm}=0\), commutation identities control \(\|\nabla^2h\|_2\) by \(\|\nabla^*\nabla h\|_2+\|\nabla h\|_2+\|h\|_2\), with model constants.

---

## 2. Linearized Seiberg–Witten operator

### 2.1 Cross-term cancellation and algebraic potentials

In the normalization of the script,
\[
c(F_{A_0}^+)=(\Phi_0\Phi_0^*)_0,
\qquad
|\Phi_0|^2=-s=4.
\]
The gauge-fixed linearization
\[
\mathcal L(a,\psi)=
\left(
d^*a-\frac12i\,\operatorname{Im}\langle\Phi_0,\psi\rangle,\,
d^+a-\sigma'_{\Phi_0}(\psi),\,
D_{A_0}\psi+\frac12a\cdot\Phi_0
\right)
\]
has exact cancellation of all first-order mixed terms for the gauge coefficient \(-\tfrac12\). The numerical \(2.2\times10^{-16}\) residual is the floating-point trace of an exact Clifford-algebra identity. Since \(\nabla_{A_0}\Phi_0=0\), differentiating the algebraic couplings produces no further first-order terms.

The listed zeroth-order eigenvalues are correct:

- \(1/2\) on the four real 1-form directions:
  \[
  \frac{\lambda}{2}+\frac{|\Phi_0|^2}{4}
  =-\frac12+1=\frac12;
  \]
- \(2\) and \(1\) on the two real directions in \(\mathbb C\Phi_0\);
- \(0,0\) on the real plane \(\Phi_0^\perp\).

For a closed four-manifold,
\[
\|d^*a\|^2+\|d^+a\|^2
=\frac12\langle\Delta_da,a\rangle+\frac12\|d^*a\|^2
\ge\frac12\langle\Delta_da,a\rangle.
\]
Thus the dropped term is exactly the nonnegative \(\tfrac12\|d^*a\|^2\); no needed term is lost. With
\[
\Delta_d=\nabla^*\nabla+\lambda
\]
and the spinor-coupling mass, this yields
\[
\frac12\|\nabla a\|^2+\frac{|\lambda|}{2}\|a\|^2.
\]

### 2.2 The two zero modes and the corrected coercive estimate

The splitting
\[
S^+=\mathbb C\Phi_0\oplus\Phi_0^\perp
\]
is parallel, and
\[
\Phi_0^\perp\cong\Lambda^{0,2}\cong K^{-1}.
\]
For the induced Chern connection,
\[
|i\Lambda F_{K^{-1}}|=2|\lambda|.
\]
The two Kähler identities
\[
\nabla^*\nabla
=2\bar\partial^*\bar\partial+i\Lambda F
=2\partial^*\partial-i\Lambda F
\]
allow the favorable sign to be chosen, giving
\[
\|\nabla\psi_\perp\|^2
\ge2|\lambda|\,\|\psi_\perp\|^2.
\]
This is again curvature-algebraic and therefore cover-independent.

The displayed estimate in G4 is nevertheless too strong:
\[
\|\mathcal L(a,\psi)\|^2
\not\ge
\frac12\|\nabla a\|^2+\|\nabla\psi\|^2
+\frac{|\lambda|}{2}\|(a,\psi)\|^2.
\]
On \(\psi_\perp\), the algebraic potential is zero. The gradient energy cannot both remain intact and also supply an additional mass term.

A valid uniform estimate is, for example,
\[
\boxed{\;
\|\mathcal L(a,\psi)\|^2
\ge
\frac12\|\nabla a\|^2
+\frac12\|\nabla\psi\|^2
+\frac{|\lambda|}{2}\|(a,\psi)\|^2 .
\;}
\]
At \(\lambda=-1\), one can retain a larger derivative coefficient on the spinor by splitting the Landau estimate more economically, but the symmetric form above suffices.

Thus the \(L^2\) spectral gap \( |\lambda|/2\) is valid and genuinely \(\Gamma\)-independent. What is not automatic from it is a \(\Gamma\)-uniform inverse on uniformly local Hölder spaces.

### 2.3 Normalization mismatch

Step 44 uses \(|\Phi_0|^2=4\) at \(s=-4\). Step 40’s Theorem N uses
\[
\rho=|\Phi|^2\in[0,2],
\]
with canonical amplitude \(\rho=2\). The fields differ by a constant factor:
\[
\Phi_{\rm Step\,40}=\frac1{\sqrt2}\Phi_{\rm Step\,44}.
\]
The direction \(n\) is unchanged, but \(\rho^2|\nabla n|^2\) changes by a factor \(4\). Therefore G4 cannot be combined literally with Theorem N without explicitly converting the quadratic map, spinor normalization, and target norms. This affects constants, though not the qualitative one-sided estimate \(R\lesssim P\).

---

## 3. Theorem A

### 3.1 Einstein-defect coercivity

Conditional on a uniformly controlled gauge representation, the expansion behind item 1 is correct.

The conformal identity is exact:
\[
\operatorname{Ric}^\circ(e^{2f}\hat g)
=\operatorname{Ric}^\circ(\hat g)
-2(\hat\nabla^2f-df\otimes df)^\circ.
\]
Hence constant shifts in \(f\) disappear, as required by scale invariance. At the Einstein host,
\[
\|(\nabla^2f)^\circ\|^2
=\frac34\|\Delta f\|^2+|\lambda|\|\nabla f\|^2.
\]
Also \(L_E\) preserves TT tensors, so
\[
\int\langle L_Ek,(\nabla^2u)^\circ\rangle=0.
\]

For \(k\) small in \(C^{2,\alpha}\),
\[
\operatorname{Ric}^\circ(g_\Gamma+k)
=\frac12L_Ek+Q(k),
\]
where schematically
\[
|Q(k)|\le C\bigl(|k||\nabla^2k|+|\nabla k|^2+|k|^2\bigr).
\]
If \(\|k\|_{C^{2,\alpha}}\le\varepsilon_0\), this is absorbable in \(L^2\). Changes of connection in the conformal Hessian contribute analogous small terms. Consequently,
\[
P(g)\ge
\kappa\bigl(\|k\|_{H^2}^2+\|df\|_{H^1}^2\bigr)
\]
with a model-dependent \(\kappa>0\), once the gauge is constructed uniformly.

A safer uniform gauge construction is:

1. take the nearby scalar-\(-4\) representative using \(6\Delta+8\), whose positive mass gives a maximum-principle inverse;
2. impose Bianchi gauge, whose vector linearization is a Laplace-type operator of the form
   \[
   \nabla^*\nabla+|\lambda|;
   \]
3. perform the TT/scalar decomposition at the \(L^2\)/Sobolev level, where the pointwise Bochner gaps supply uniform constants.

This avoids requiring a quotient-uniform Hölder inverse for \(L_E\) itself.

### 3.2 The asserted Hölder uniformity is not proved

The claim

> lifting unit balls through the exponential map, combined with an \(L^2\) gap and Agmon/Combes–Thomas decay, yields uniformly bounded Hölder inverses without injectivity-radius bounds

does not follow from the supplied argument.

Lifting gives quotient-independent interior Schauder estimates, but those estimates still require local \(C^0\) or local \(L^2\) control. A global \(L^2\) gap controls the total \(L^2\) norm, which can grow extensively with the quotient volume. To obtain a uniform \(L^\infty\) resolvent one needs either:

- a maximum-principle structure with pointwise positive potential; or
- an \(L^1\)-integrable Green kernel on the universal cover, sufficiently strong to control the periodized kernel independently of \(\Gamma\).

Neither is established for the full gauge-fixed Seiberg–Witten operator. Exponential decay alone is insufficient unless its rate is compared with the exponential orbit/volume growth.

Therefore the supported conclusions are:

- universal \(L^2\) and Sobolev coercivity for the Einstein operator;
- a universal \(L^2\) gap for the gauge-fixed monopole operator;
- existence and uniqueness of the nearby branch for each fixed compact quotient, with constants potentially depending on \(\Gamma\).

A truly cover-uniform monopole branch requires an additional resolvent theorem, for example an \(L^1\)-Green-kernel estimate for \(\mathcal L^*\mathcal L\) on \(\mathbb{CH}^2\), or a different maximum-principle formulation.

### 3.3 Conformal covariance

The qualitative conformal argument is correct, but the displayed Dirac factor is inaccurate. Under the standard conformal spinor identification,
\[
D_{e^{2f}g}(e^{-3f/2}\chi)
=e^{-5f/2}D_g\chi.
\]
Setting \(\chi=e^{f/2}\Phi\) and \(D_g\Phi=0\) yields
\[
\boxed{\;
D_{e^{2f}g}(e^{-f}\Phi)
=\frac12e^{-2f}\,df\cdot_g\Phi .
\;}
\]
Thus the residual is indeed \(O(df)\), but not with the factor \(e^{-5f/2}\) written in the note.

### 3.4 The claimed lower comparison is false

Let
\[
R=\int\rho^2|\nabla n|_{W_2}^2
\]
in the normalization of Theorem N. At \(Q=0\), Theorem N has the form
\[
-P=\frac12R-\mathcal E,
\qquad \mathcal E\ge0.
\]
Equivalently,
\[
\mathcal E=P+\frac12R.
\]
This gives no inequality \(2P\le R\). The inference in Step 44 reverses the logical role of the nonnegative remainder.

More decisively, no estimate \(R\ge cP\) can hold near the KE metric. A nearby non-Einstein Kähler metric in the same complex structure has canonical direction equal to its parallel Kähler direction, so
\[
R=0,
\qquad
P=\int|\operatorname{Ric}^\circ|^2>0.
\]
Thus Nijenhuis energy detects nonintegrable rotation, not all Einstein defects.

The corrected perturbative conclusion is
\[
\boxed{\;
P(g)\ge
\kappa\bigl(\|k\|_{H^2}^2+\|df\|_{H^1}^2\bigr),
\qquad
R(g)\le C P(g).
\;}
\]
There is no two-sided comparability \(P\asymp R\).

The common-mode exclusion uses only \(R\le CP\), so that interpretation remains valid wherever the nearby branch and its constants are available.

### 3.5 Corrected form of Theorem A

A statement supported by the current argument is:

> For each compact ball quotient \(X_\Gamma\), sufficiently close metrics admit a uniquely determined nearby canonical monopole branch in a fixed slice, and
> \[
> P(g)\ge\kappa_0\bigl(\|k\|_{H^2}^2+\|df\|_{H^1}^2\bigr),
> \qquad
> R(g)\le C_\Gamma P(g).
> \]
> The Einstein coercivity constant \(\kappa_0\) can be chosen independently of \(\Gamma\). The supplied argument does not prove that \(C_\Gamma\), the Hölder implicit-function radius, or the branch neighborhood are independent of \(\Gamma\).

If a universal uniformly local inverse for the gauge-fixed monopole operator is established separately, \(C_\Gamma\) and the branch radius can then be replaced by universal constants.

---

## 4. Proposition \(\Pi\)

Let
\[
G(\sigma,\delta)
=\frac{2\sigma^2+(3\delta-2\sigma)^2}{192\pi^2},
\qquad
\Omega_+=\{\delta\ge\sigma\},
\qquad
\varphi=\frac{\operatorname{Vol}\Omega_+}{V}.
\]
For regional means \(v_1,v_2\), write
\[
v_1=\bar v+(1-\varphi)u,\qquad
v_2=\bar v-\varphi u.
\]
Since \(G\) is a homogeneous quadratic form,
\[
\varphi G(v_1)+(1-\varphi)G(v_2)
=G(\bar v)+\varphi(1-\varphi)G(u).
\]

If \(D>0\),
\[
\min_{y-x=D}\{2x^2+(3y-2x)^2\}
=\min_x\{2x^2+(x+3D)^2\}
=6D^2,
\]
attained at \(x=-D,\ y=0\).

Blair’s identity gives
\[
2V\bar\sigma-V\bar\delta=\ell,
\qquad
V\bar\delta=\theta\ell,
\]
hence
\[
\bar\sigma=\frac{\ell}{2V}(1+\theta),\qquad
\bar\delta=\frac{\ell}{V}\theta,\qquad
\bar\sigma-\bar\delta=\frac{\ell}{2V}(1-\theta).
\]
The pocket condition implies
\[
u_\delta-u_\sigma
\ge\frac{\bar\sigma-\bar\delta}{1-\varphi}.
\]
For \(\theta\le1\), this yields
\[
C_+\ge
\frac{\ell^2}{128\pi^2V}
\left[
\Gamma(\theta)+
\frac{\varphi}{1-\varphi}(1-\theta)^2
\right],
\]
and for arbitrary \(\theta\) the positive part gives
\[
\boxed{\;
C_+\ge
\frac{\ell^2}{128\pi^2V}
\left[
\Gamma(\theta)+
\frac{\varphi}{1-\varphi}(1-\theta)_+^2
\right].
\;}
\]

For \(0\le\theta\le1\), minimization gives
\[
\theta_*=\frac1{3-2\varphi},
\qquad
\min=
\frac2{3-2\varphi}.
\]
For \(\theta\ge1\), \(\Gamma(\theta)\ge2\), so the same global lower bound follows:
\[
\boxed{\;
C_+\ge
\frac{\ell^2}{128\pi^2V}\frac2{3-2\varphi}.
\;}
\]
At \(\varphi=0\) this is \(2/3\); at \(\varphi=1/2\) it is \(1\).

The complement constraint gives a symmetric refinement:
\[
q_\varphi(\theta)=
\begin{cases}
\dfrac{\varphi}{1-\varphi}(1-\theta)^2,&\theta\le1,\\[5pt]
\dfrac{1-\varphi}{\varphi}(\theta-1)^2,&\theta\ge1,
\end{cases}
\]
but it does not change the global minimum because \(\theta_*<1\).

The curvature interpretation is correct:
\[
W^+(\hat\omega,\hat\omega)
=\frac{s}{6}+\frac{|\nabla\omega|^2}{4},
\]
so
\[
\mathbb R^+(\hat\omega,\hat\omega)
=W^+(\hat\omega,\hat\omega)+\frac{s}{12}
=\frac{s^*}{4}.
\]
Thus an aligned Burns insertion changes the first-order term favorably exactly when
\[
s^*(p)>0.
\]

A useful qualification is that the relaxed optimizer places the pocket mean at \(s^*=0\), where the first-order Burns saving itself vanishes. To price pockets with a definite threshold \(s^*\ge s_0>0\), the same calculation gives
\[
C_+\ge
\frac{\ell^2}{128\pi^2V}
\left[
\Gamma(\theta)+
\frac{\varphi}{1-\varphi}
\left(1-\theta+\frac{2Vs_0}{\ell}\right)_+^2
\right].
\]

Under \(H_L\), the optimized coefficient implies
\[
\frac{P}{8\pi^2}
\ge
k-A+\frac{2A}{3-2\varphi}
=
k-A\frac{1-2\varphi}{3-2\varphi}.
\]
This improves the \(\varphi=0\) threshold for every \(\varphi>0\), although for tiny pockets the gain is only \(O(\varphi)\). Therefore the sentence that it is informative “only for \(\varphi\) near \(1/2\)” is too strong.

The almost-Kähler pocket statement should not be identified automatically with the monopole direction of Theorem A: the given almost-Kähler form and the SW-selected direction need not coincide.

---

## 5. Localized/blow-up scope

The two obstacles listed in Step 44 are genuine for a localized monopole-coercivity theorem:

1. **Bulk field selection.** Metric closeness on a bulk region does not force a global monopole solution on the blow-up to be close there to the canonical host solution. The available Weitzenböck bounds are extensive and permit localized depletion or rotation.

2. **Collar dependence.** Interior coercivity for the Einstein equation necessarily includes boundary/collar data. Local homogeneous linearized Einstein fields prevent control of the interior deformation solely by the interior Ricci defect.

Accordingly, the statement

> every host-like region has either a monopole far from canonical or negligible Nijenhuis saving

is not yet a theorem; it is the expected conclusion of a missing localized estimate.

What does follow unconditionally from Theorem N for pure blow-ups is
\[
8\pi^2k-P
\le\frac12 R_{\rm tot},
\]
so if
\[
P\le8\pi^2ck,\qquad c<1,
\]
then
\[
\boxed{\;
R_{\rm tot}\ge16\pi^2(1-c)k.
\;}
\]
This is global and does not locate the energy. If a future estimate of the form
\[
R(\Omega)
\le C P(\Omega')+\text{collar/field-selection errors}
\]
is established, this lower bound would force the required rotation into non-host-like regions, noncanonical-field regions, or collars.

A further pointwise consequence can be extracted from Theorem W without selecting a nearby canonical branch. At an exact scalar-\(-4\) Kähler-type self-dual Weyl tensor
\[
W_*=\frac13I-\hat\omega\otimes\hat\omega,
\]
the Theorem-W saving density is nonpositive for every monopole amplitude and direction, with equality only at canonical amplitude and aligned direction:
\[
f(W_*,\rho,n)
\le-(2-\rho)^2(\rho+1)\le0.
\]
Thus exact Kähler-type curvature cannot support positive local saving, even through depletion. Perturbing \(W^+=W_*+E\) gives a linear error
\[
f(W^+,\rho,n)\le C|E|.
\]
This yields a field-independent necessary condition: substantial global saving requires substantial integrated departure of \(W^+\) from the Kähler-type orbit. It does not by itself yield a tariff, because the error is linear and extensive, and converting it to a quadratic Einstein-defect cost requires additional stationarity or gluing information.

---

## Corrected final conclusions

1. **Verified and cover-independent:**  
   \[
   \langle L_Eh,h\rangle\ge\frac13\|h\|^2
   \]
   at \(s=-4\), with \(\mathring R=-2\) on the \(3\)-dimensional \(J\)-invariant sector and \(+4\) on the \(6\)-dimensional \(J\)-anti-invariant sector.

2. **Verified after correction:** the gauge-fixed SW linearization has a cover-independent \(L^2\) gap \(1/2\), but its coercive estimate must sacrifice part of the \(\psi_\perp\) derivative term.

3. **Not established:** a \(\Gamma\)-uniform Hölder inverse and hence a universal nonlinear monopole branch radius. Lifting local balls plus an \(L^2\) gap is insufficient.

4. **False:**  
   \[
   2P\le R,\qquad P\asymp R.
   \]
   The correct perturbative relation is one-sided:
   \[
   R\le CP,
   \]
   with cover-uniformity contingent on the missing resolvent estimate.

5. **Verified:** Proposition \(\Pi\), including
   \[
   \Gamma(\theta)+\frac{\varphi}{1-\varphi}(1-\theta)_+^2
   \ge\frac2{3-2\varphi}.
   \]

6. **Blow-up consequence currently available:** subunit near-minimizers must carry total monopole \(W_2\)-energy at least \(16\pi^2(1-c)k\), but the present work does not localize that energy to or away from KE-like bulk regions.
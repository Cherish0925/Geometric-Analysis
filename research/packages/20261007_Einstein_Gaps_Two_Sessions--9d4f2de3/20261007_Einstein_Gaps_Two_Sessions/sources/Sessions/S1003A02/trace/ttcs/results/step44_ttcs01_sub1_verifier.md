# TTCS Independent Branch Record

```json
{
  "step_id": 44,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Sessions/S1003A02/workspace/scripts/step44_perturbative_ke.py",
    "Sessions/S1003A02/workspace/data/step44_perturbative_ke.json",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md"
  ]
}
```

## Task

Verify, as a careful geometric analyst, the two new results in Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md (Theorem A: cover-independent perturbative coercivity of the Einstein defect P=∫|Ric°|² and of the monopole Nijenhuis energy near compact complex-hyperbolic surfaces; Proposition Π: pocket refinement of the almost-Kähler profile inequality AKΓ). The computation is in workspace/scripts/step44_perturbative_ke.py with output workspace/data/step44_perturbative_ke.json. Check specifically: (1) the Koiso Bochner identity <L_E h,h> = ||d^∇h||² + <(-λ - R̊)h,h> for TT h on Einstein manifolds (normalization of ||d^∇ h||², sign of R̊ convention: R̊h=-h on trace-free tensors of the unit sphere), and the computed spectrum R̊ = -2 (J-invariant, dim 3), +4 (J-anti, dim 6) on CH² with holomorphic sectional curvature -4 (λ=-6), giving pointwise gap 2 = |λ|/3; whether this agrees with the known infinitesimal rigidity of ball quotients and whether the gap is genuinely Γ-independent. (2) the linearized Seiberg–Witten analysis (G4): cancellation of first-order cross terms when ∇Φ₀=0 with gauge coefficient -1/2, the potential eigenvalues (1/2 on 1-forms, 2, 1, 0,0 on spinors at s=-4), and the claim that the two zero modes on Φ₀^⊥≅Λ^{0,2}≅K^{-1} are lifted by the Kodaira/Landau identity with |iΛF|=2|λ|; check whether the use of ||d^*a||²+||d^+a||² ≥ (1/2)<Δ_d a,a> loses a needed term, and whether a spectral gap of 1/2 is really cover independent. (3) the proof sketch of Theorem A: the conformal slice g=e^{2f}(g_Γ+k), the claim that P and the monopole direction depend on f only through df (exact conformal formulas), uniform Hölder inverses via lifting along the exponential map without injectivity radius bounds, the cubic remainder bounds, and the comparability 2P ≤ R ≤ C'P using Theorem N (Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md). Identify any gap that would make the constant Γ-dependent or the theorem false, and repair it if possible. (4) Proposition Π: the two-region Jensen argument, the minimum 6D² of 2x²+(3y-2x)² on y-x=D, the identities σ̄-δ̄=(ℓ/2V)(1-θ), the final bound 2/(3-2φ), and the interpretation (tiny-area Burns spheres aligned with ω save at first order iff s*>0 since R⁺(ω̂,ω̂)=s*/4); compare with AKΓ in Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md. (5) Judge the scope paragraph: whether the stated obstacles to the blow-up/localized version (bulk monopole selection, local Einstein deformations) are the real ones, and whether some stronger statement about near-minimizers on X_Γ#k CP̄² does follow. Give corrected statements where needed; do not invent literature.

## Output

# Verification memo

## 1. Koiso identity and the \(\mathbb{CH}^{2}\) tensor gap

Let
\[
(d^\nabla h)_{ijk}=\nabla_i h_{jk}-\nabla_j h_{ik},
\qquad
|d^\nabla h|^2=\frac12\sum_{i,j,k}(d^\nabla h)_{ijk}^2.
\]
For a TT tensor on an Einstein manifold, \(\delta h=\operatorname{tr}h=0\) and \(\operatorname{Ric}=\lambda g\). Commutation of derivatives gives
\[
\int \nabla_i h_{jk}\nabla_j h_{ik}
 =\int\langle\mathring Rh,h\rangle-\lambda\int|h|^2.
\]
Consequently
\[
\|d^\nabla h\|^2
 =\|\nabla h\|^2-\langle\mathring Rh,h\rangle+\lambda\|h\|^2,
\]
and hence, for \(L_E=\nabla^*\nabla-2\mathring R\),
\[
\boxed{\;
\langle L_Eh,h\rangle
=\|d^\nabla h\|^2+\langle(-\lambda-\mathring R)h,h\rangle .
\;}
\]
This agrees with the stated sphere convention. For the unit sphere,
\[
R_{ikjl}h_{kl}=(\operatorname{tr}h)g_{ij}-h_{ij}=-h_{ij}
\]
on \(S^2_0\). If the raw ordered-index norm \(\sum_{ijk}|d^\nabla h_{ijk}|^2\) is used instead, the first term in the identity acquires a factor \(1/2\).

For the curvature tensor used in the script, direct substitution into the \(J\)-splitting
\[
S^2_0=(S^2_0)^{J,+}\oplus(S^2_0)^{J,-},
\qquad \dim_{\mathbb R}=3+6,
\]
gives
\[
\mathring R=
\begin{cases}
-2I,&(S^2_0)^{J,+},\\
4I,&(S^2_0)^{J,-}.
\end{cases}
\]
The script’s numerical matrices therefore recover exact algebraic eigenvalues, not merely sampled approximations. With holomorphic sectional curvature \(-4\),
\[
\lambda=-6,\qquad
-\lambda-\max\operatorname{spec}\mathring R=6-4=2.
\]
After scaling to \(s=-4\), so that \(\lambda=-1\), this becomes
\[
\langle L_Eh,h\rangle\ge\frac13\|h\|^2.
\]

This is fully compatible with infinitesimal rigidity of compact ball quotients. The \(J\)-anti-invariant sector is the tensor representation in which complex-structure variations would occur; the Bochner term excludes a global TT kernel. Since the estimate uses only the curvature tensor of the symmetric model, its \(L^2\) constant is independent of \(\Gamma\), including along finite-cover towers. No quotient spectral datum enters.

The sentence identifying the \(J\)-invariant Hodge gap \(2|\lambda|\) is also consistent with the standard primitive \((1,1)\)-form identification. The weaker Koiso estimate on that sector is \(8\) before rescaling, whereas the Hodge formulation gives \(12\).

---

## 2. Linearized Seiberg–Witten operator

### 2.1 Algebraic square completion

In the normalization used by `step44_perturbative_ke.py`,
\[
c(F_{A_0}^+)=(\Phi_0\Phi_0^*)_0,\qquad |\Phi_0|^2=-s=4.
\]
The Clifford calculation supports the gauge-fixed operator
\[
\mathcal L(a,\psi)=
\left(
d^*a-\frac12 i\,\operatorname{Im}\langle\Phi_0,\psi\rangle,\,
d^+a-\sigma'_{\Phi_0}(\psi),\,
D_{A_0}\psi+\frac12a\cdot\Phi_0
\right).
\]
With the stated Clifford conventions, the symbol-level mixed first-order terms cancel exactly for the gauge coefficient \(-1/2\). Because \(\nabla_{A_0}\Phi_0=0\), differentiating the algebraic maps introduces no further first-order term. Thus the numerical residual \(2.2\times10^{-16}\) records an exact Clifford identity.

The zeroth-order eigenvalues
\[
\frac12,\frac12,\frac12,\frac12,\quad 2,\quad1,\quad0,\quad0
\]
also agree with the square completion:

- the four \(1\)-form directions have
  \[
  \frac{\lambda}{2}+\frac{|\Phi_0|^2}{4}
  =-\frac12+1=\frac12;
  \]
- the two real directions in the complex line \(\mathbb C\Phi_0\) have eigenvalues \(2\) and \(1\);
- the real two-plane \(\Phi_0^\perp\) has zero algebraic potential.

For a closed four-manifold,
\[
\|d^*a\|^2+\|d^+a\|^2
=\frac12\langle\Delta_da,a\rangle+\frac12\|d^*a\|^2
\ge\frac12\langle\Delta_da,a\rangle,
\]
because \(\|d^+a\|^2=\frac12\|da\|^2\) for the exact two-form \(da\). Combining this with
\[
\Delta_d=\nabla^*\nabla+\lambda
\]
and the spinor-coupling mass \(-\lambda\) yields
\[
\frac12\|\nabla a\|^2+\frac{|\lambda|}{2}\|a\|^2.
\]
Thus no essential term is lost in the displayed Hodge estimate.

### 2.2 The \(\Phi_0^\perp\) directions

The bundle \(\Phi_0^\perp\) is the connection-invariant line
\[
\Lambda^{0,2}\cong K^{-1}
\]
under the Hermitian metric identification. At a KE metric,
\[
|i\Lambda F_{K^{-1}}|=2|\lambda|.
\]
The Kähler identities
\[
\nabla^*\nabla
=2\bar\partial^*\bar\partial+i\Lambda F
=2\partial^*\partial-i\Lambda F
\]
allow the identity with the favorable sign to be used, giving
\[
\|\nabla\psi_\perp\|^2\ge2|\lambda|\,\|\psi_\perp\|^2.
\]
This lower bound is again purely curvature-algebraic and therefore independent of \(\Gamma\).

There is, however, a mistake in the exact coercive display in G4. On \(\psi_\perp\), the square contains \(\|\nabla\psi_\perp\|^2\) with zero algebraic potential. It cannot simultaneously retain the full derivative term and add a further mass term. A valid uniform form is
\[
\boxed{\;
\|\mathcal L(a,\psi)\|^2
\ge
\frac12\|\nabla a\|^2
+\frac12\|\nabla\psi\|^2
+\frac{|\lambda|}{2}\|(a,\psi)\|^2 .
\;}
\]
For \(\psi_\perp\), half of the Landau estimate supplies the mass term; the remaining half supplies the displayed derivative term. The \(L^2\) spectral gap \(|\lambda|/2\) is therefore valid, but the coefficient \(1\) in front of \(\|\nabla\psi\|^2\) is not.

Injectivity plus the zero Fredholm index of the canonical deformation complex gives invertibility on each quotient. The index is zero because the canonical Spin\(^c\) structure satisfies \(c_1^2=2\chi+3\tau\).

### 2.3 Normalization mismatch with Theorem N

G4 and Theorem N are written in different monopole normalizations. G4 uses
\[
c(F^+)=(\Phi\Phi^*)_0,\qquad |\Phi_0|^2=4
\]
at \(s=-4\). Step 40 uses a convention in which
\[
0\le\rho=|\Phi|^2\le2
\]
and the canonical amplitude is \(\rho=2\). Thus the G4 eigenvalues and gauge square cannot be inserted literally into Theorem N without rescaling the quadratic map, the spinor, and the norm on the curvature-equation component.

The direction \(n\) is unchanged by a constant spinor rescaling, so a one-sided estimate for its derivative should survive with altered constants. Nevertheless, a consistent theorem should either:

1. rewrite G4 in the Step-40 convention and redo the square completion, possibly with a weighted norm on the equation target; or
2. rewrite Theorem N in the G4 convention.

At present the note mixes the two sets of constants.

---

## 3. Theorem A

### 3.1 Einstein-defect coercivity

Once a representation
\[
g=e^{2f}(g_\Gamma+k),\qquad \delta k=0,\quad\operatorname{tr}k=0
\]
has been obtained with a uniform small \(C^{2,\alpha}\) norm, the quadratic estimate is sound.

The conformal formula
\[
\operatorname{Ric}^\circ(e^{2f}\hat g)
=\operatorname{Ric}^\circ(\hat g)
-2(\hat\nabla^2f-df\otimes df)^\circ
\]
is exact. Constant shifts of \(f\) disappear, as required by scale invariance. On the Einstein host,
\[
\|(\nabla^2f)^\circ\|^2
=\frac34\|\Delta f\|^2+|\lambda|\,\|\nabla f\|^2.
\]
Moreover \(L_E\) preserves the TT subspace, so
\[
\int\langle L_Ek,(\nabla^2u)^\circ\rangle=0.
\]
The curvature expansion
\[
\operatorname{Ric}^\circ(g_\Gamma+k)
=\frac12L_Ek+Q_1(k)
\]
has the stated form, with
\[
|Q_1(k)|\le C\varepsilon_0
\bigl(|\nabla^2k|+|\nabla k|+|k|\bigr)
\]
when \(\|k\|_{C^{2,\alpha}}\le\varepsilon_0\). Changes from \(\nabla^{g_\Gamma+k}\) to \(\nabla^{g_\Gamma}\) in the conformal Hessian produce terms of the same absorbable type.

The homogeneous curvature and integrated Bochner formulas give quotient-independent \(H^2\) estimates for TT tensors. Thus the core estimate
\[
P(g)\ge\kappa\bigl(\|k\|_{H^2}^2+\|df\|_{H^1}^2\bigr)
\]
has a universal \(\kappa\), provided the required slice has already been constructed with uniform control.

### 3.2 Uniform Hölder inverses are not established by the present argument

For \(K<0\), \(\exp_p:T_pX_\Gamma\to X_\Gamma\) factors through the universal covering, so lifting unit balls does provide interior Schauder estimates with model constants. It does not by itself provide a global estimate
\[
\|u\|_{C^{m,\alpha}_{\mathrm{uloc}}}
\le C\|Lu\|_{C^{m-2,\alpha}_{\mathrm{uloc}}}
\]
with \(C\) uniform over all cocompact \(\Gamma\).

Likewise, an \(L^2\) spectral gap plus Agmon decay does not automatically give a quotient-independent \(L^\infty\) resolvent: the Green kernel must be summed over the orbit, and its decay must be compared with orbit growth and possible short-geodesic multiplicity. The note does not supply that estimate.

This affects:

- the nonlinear Diff\(\ltimes\)Conf slice in uniformly local Hölder norms;
- the cover-uniform implicit-function radius for the monopole branch;
- the assertion that no injectivity-radius input is needed.

What is presently justified is:

- universal \(L^2\) and integrated Sobolev coercivity for \(L_E\);
- a universal \(L^2\) gap for the gauge-fixed monopole operator, after correcting the derivative coefficient;
- a local branch for every fixed \(\Gamma\), with constants that may depend on the quotient.

A fully universal version requires a separate uniformly local resolvent theorem for the Einstein-slice, conformal-Killing, and monopole operators. The pointwise Bochner structures make such a theorem plausible, but it is not proved by the sentence about lifted balls.

### 3.3 Conformal covariance

The curvature equation is indeed preserved by the ansatz
\[
\widetilde\Phi=e^{-f}\Phi
\]
under \(\widetilde g=e^{2f}g\), in the G4 normalization. Under the standard isometric spinor identification,
\[
D_{\widetilde g}(e^{-3f/2}\chi)=e^{-5f/2}D_g\chi.
\]
Taking \(\chi=e^{f/2}\Phi\) and \(D_g\Phi=0\) gives
\[
D_{\widetilde g}(e^{-f}\Phi)
=\frac12e^{-2f}\,df\cdot\Phi.
\]
Thus the exponent \(e^{-5f/2}\) in the note is not correct in this identification. The required \(O(df)\) estimate remains valid.

The Yamabe linearization
\[
6\Delta+2|s|=6\Delta+8
\]
at \(s=-4\) has a universal mass term, so the nearby scalar-\(-4\) representative is well supported once the uniformly local inverse issue is handled.

### 3.4 The asserted two-sided comparison is false

Let
\[
R=\int\rho^2|\nabla n|_{W_2}^2.
\]
At \(Q=0\), Theorem N reads
\[
-P=\frac12R-\mathcal E,
\qquad \mathcal E\ge0,
\]
where \(\mathcal E\) is the sum of the depletion, amplitude/Lee, Weyl-alignment, and Walsh terms. Equivalently,
\[
\mathcal E=P+\frac12R.
\]
This does **not** imply \(2P\le R\); it only gives the tautology \(-P\le R/2\).

There is also a geometric counterexample to any lower estimate \(R\ge cP\). Take a nearby Kähler metric in the same complex structure that is not Einstein. Its canonical monopole direction is the Kähler direction, hence
\[
\nabla n=0,\qquad R=0,
\]
while generally
\[
P=\int|\operatorname{Ric}^\circ|^2>0.
\]
The same phenomenon reflects the fact that Nijenhuis energy detects nonintegrable rotation, not arbitrary departures from the Einstein equation.

The valid perturbative conclusion is therefore one-sided:
\[
\boxed{\;
R(g)\le C\,P(g).
\;}
\]
Together with the metric estimate, one has
\[
P(g)\asymp \|k\|_{H^2}^2+\|df\|_{H^1}^2,
\qquad
R(g)\le C P(g),
\]
but not \(P\asymp R\).

---

## 4. Proposition \(\Pi\)

The stated inequality is correct.

Let
\[
G(\sigma,\delta)
=\frac{2\sigma^2+(3\delta-2\sigma)^2}{192\pi^2},
\qquad
\Omega_+=\{\delta\ge\sigma\},
\qquad
\varphi=\frac{\operatorname{Vol}\Omega_+}{V}.
\]
Writing the two regional means as
\[
v_1=\bar v+(1-\varphi)u,\qquad
v_2=\bar v-\varphi u,
\]
quadraticity gives exactly
\[
\varphi G(v_1)+(1-\varphi)G(v_2)
=G(\bar v)+\varphi(1-\varphi)G(u).
\]

For \(D>0\),
\[
\min_{y-x=D}\left[2x^2+(3y-2x)^2\right]
=\min_x\left[2x^2+(x+3D)^2\right]
=6D^2,
\]
attained at \(x=-D,\ y=0\).

Blair’s identity gives
\[
2V\bar\sigma-V\bar\delta=\ell,
\qquad
V\bar\delta=\theta\ell,
\]
and hence
\[
\bar\sigma=\frac{\ell}{2V}(1+\theta),\qquad
\bar\delta=\frac{\ell}{V}\theta,\qquad
\bar\sigma-\bar\delta=\frac{\ell}{2V}(1-\theta).
\]
The pocket condition yields
\[
u_\delta-u_\sigma
\ge \frac{\bar\sigma-\bar\delta}{1-\varphi}.
\]
Therefore
\[
C_+\ge
\frac{\ell^2}{128\pi^2V}
\left[
\Gamma(\theta)
+\frac{\varphi}{1-\varphi}(1-\theta)_+^2
\right].
\]

For \(0\le\theta\le1\), minimization gives
\[
\theta_*=\frac1{3-2\varphi},
\qquad
\min_\theta
\left[
\Gamma(\theta)
+\frac{\varphi}{1-\varphi}(1-\theta)^2
\right]
=\frac2{3-2\varphi}.
\]
For \(\theta\ge1\), \(\Gamma(\theta)\ge2\), so the same global lower bound follows. At \(\varphi=0\) it returns \(2/3\), and at \(\varphi=1/2\) the normalized profile coefficient is \(1\). Converting that coefficient into the topological \(A\)-coefficient still requires the period hypothesis \(H_L\).

A slight strengthening follows by also using the strict complement condition \(\delta<\sigma\) on \(M\setminus\Omega_+\). For \(0<\varphi<1\),
\[
C_+\ge\frac{\ell^2}{128\pi^2V}
\bigl[\Gamma(\theta)+q_\varphi(\theta)\bigr],
\]
where
\[
q_\varphi(\theta)=
\begin{cases}
\dfrac{\varphi}{1-\varphi}(1-\theta)^2,&\theta\le1,\\[6pt]
\dfrac{1-\varphi}{\varphi}(\theta-1)^2,&\theta\ge1.
\end{cases}
\]
This refinement does not change the minimum \(2/(3-2\varphi)\), since the minimizing \(\theta_*\) lies below \(1\).

Finally,
\[
W^+(\hat\omega,\hat\omega)=\frac{s}{6}+\frac{|\nabla\omega|^2}{4},
\]
so
\[
\mathbb R^+(\hat\omega,\hat\omega)
=W^+(\hat\omega,\hat\omega)+\frac{s}{12}
=\frac{s+|\nabla\omega|^2}{4}
=\frac{s^*}{4}.
\]
Thus the first-order Burns term
\[
8\pi^2\left(1-\frac{x_0s^*(p)}4\right)
\]
is smaller than \(8\pi^2\) exactly at points with \(s^*(p)>0\). The geometric interpretation in the note is correct.

---

## 5. Blow-up and localized consequences

The two identified mechanisms are genuine:

1. A global monopole on \(X_\Gamma\#k\overline{\mathbb{CP}}^2\) need not approach the canonical host solution merely because the metric is host-like on a large region. The Step-39 integral control permits order-one depletion or rotation to be placed in selected regions.

2. An interior Einstein estimate after inserting a cutoff necessarily includes collar data. Local solutions of the homogeneous linearized Einstein equation prevent control of the interior deformation solely by the interior value of \(\operatorname{Ric}^\circ\).

The stronger sentence asserting an either/or alternative in every host-like region is not yet a theorem, because the localized monopole estimate and its collar terms have not been derived.

What does follow globally from Theorem N is concrete. For a pure blow-up,
\[
8\pi^2k-P\le\frac12R_{\mathrm{tot}},
\]
so any family with
\[
P\le8\pi^2c\,k,\qquad c<1,
\]
satisfies
\[
R_{\mathrm{tot}}\ge16\pi^2(1-c)k.
\]
If a future localized estimate gives
\[
R(\Omega)\le C\,P(\Omega')+\text{collar terms}
\]
whenever both the metric and the selected monopole are close to the canonical host branch on \(\Omega'\), then the displayed global lower bound forces the required Nijenhuis energy into non-host-like regions, noncanonical-field regions, or collars. Without that local estimate and field selection, Theorem A alone gives no corresponding statement on the blow-up.

## Final assessment

- The Koiso computation, its normalization, the \((-2,+4)\) spectrum, and the quotient-independent \(L^2\) gap are correct.
- The G4 Clifford square and potential eigenvalues are correct in the script’s normalization. The derivative coefficient in its final coercive inequality must be reduced, while the \(L^2\) gap \(1/2\) survives.
- G4 and Theorem N use incompatible spinor normalizations and need an explicit conversion.
- The perturbative estimate \(P\gtrsim\|k\|_{H^2}^2+\|df\|_{H^1}^2\) and the one-sided bound \(R\lesssim P\) are supported.
- The universal Hölder implicit-function constants are not obtained by the present lifted-ball argument.
- The relation \(2P\le R\), and hence \(P\asymp R\), is false.
- Proposition \(\Pi\) is correct and admits the symmetric refinement above for \(\theta>1\).
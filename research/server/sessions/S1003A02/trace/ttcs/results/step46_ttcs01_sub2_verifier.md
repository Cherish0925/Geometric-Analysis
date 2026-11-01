# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step46_lemmaM_elementary_and_AC.md",
    "Sessions/S1003A02/workspace/scripts/step46_lemmaM_elementary.py",
    "Sessions/S1003A02/workspace/data/step46_lemmaM_elementary.json",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Sessions/S1003A02/workspace/notes/step45_lemmaM_and_weyl_departure.md",
    "Sessions/S1003A02/trace/ttcs/results/step45_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify Step 46 of the Einstein-gap programme: `workspace/notes/step46_lemmaM_elementary_and_AC.md` (S1003A02). Work in the normalization CH^2 with holomorphic sectional curvature -4, Ric=-6g. Part 1, Lemma M by elementary means. (a) Check the block decomposition N = B_1 ⊕ (Δ0+12) ⊕ (Δ0+6) ⊕ ∇*∇ on K^{-1}, and that B_1 = dd* + ½d*d + 6 is the Hodge form of the one-form block, where the Step-44 'potential 1/2 at s=-4' is the Bochner form after dropping ½||d*a||². Then judge the strategist's worry that the coclosed sector has operator ½Δ_H + 3 with bottom 3.5 < 4 and so breaks L^1. (b) For the K^{-1} radial reduction, check the radial gauge A=6iη with η=½sinh²r σ3, V=9tanh²r, the claim that the Green kernel is radial f(r)e⊗e_o*, the Landau state cosh^{-3}r with eigenvalue 12, the zero-energy decay 2+√13, positivity, and the identity ∫tanh² G = 1/9. (c) Check formula (2.2) for B_1^{-1}, the Kato bound on 2(∇*∇+6)^{-1}, the mixed Hessian of distance on CH^2 (0, -2/sinh 2r, -1/sinh r), local cancellation, and the resulting L^∞ bound. (d) Check periodization, invertibility on quotients, derivative kernels, and the Schauder step (2.3), including surjectivity of L from index 0 plus injectivity. Part 2, Theorem A_C proof steps 1–6. Check: the Yamabe linearization 6(Δ+8); the DeTurck harmonic-map gauge with no loss of derivatives and Jacobi operator ∇*∇+6; the exact identity Ric°=Ric-λg when s=4λ; the Bianchi-gauge expansion with pointwise Q bound; and the York-decomposition coercivity argument. In that argument check the linearized scalar constraint 3Δf+24f, the relation ½(∇*∇+6)X=-df (signs and constants), that the linearized Einstein operator kills δ*X, the upgrade to H² on the locally symmetric quotient, and whether ||h||_{H²} ≤ 2||k||_{H²} really follows. Then check the canonical-branch IFT and the L² torsion bound ∫|∇n|² ≤ C||h||²_{H¹}. Identify any genuine gap, wrong constant or circularity, and state the exact corrected statement. Also check whether an absolute H^s (s≥5) neighbourhood with an injectivity-radius bound implies the C^{2,α}_b hypothesis, given that Step 44's A_H used the false H²⊂L^∞ in dimension 4. Do not infer any blow-up tariff.

## Output

# Verification memo: Step 46 (Lemma M by ODE and Kato domination, and Theorem \(A_C\))

Normalization: \(\mathbb{CH}^2\) with holomorphic sectional curvature \(-4\), \(\operatorname{Ric}=-6g\), \(s=-24\), \(|\Phi_0|^2=24\), \(\rho_0=2\).

## Summary of findings

- **Lemma M.** The elementary proof is correct. The block decomposition, \(B_1\), the radial \(K^{-1}\) reduction, the Landau state, the decay exponent, positivity, the \(1/9\) identity, formula (2.2), the mixed Hessian, the local cancellation, periodization and surjectivity all check out. The finiteness statements are rigorous; the numerical constants are not certified. A rigorous replacement for the \(K^{-1}\) constant is given in §1(b).
- **The strategist's coclosed-sector worry rests on two separate errors.** Neither threatens Lemma M.
- **Theorem \(A_C\).** The proof is correct in structure, and there is no circularity. It contains:
  - one false intermediate sentence ("the linearized operator kills \(\delta^*X\)"), which is harmless;
  - one gauge mislabel (Bianchi versus harmonic-map gauge);
  - one dropped \(-C\varepsilon\) in a constant;
  - one routine but unwritten slice step needed for "uniqueness modulo gauge".
- **\(H^s\) question.** \(H^5\)-smallness plus an injectivity-radius bound implies the \(C^{2,\alpha}_b\) hypothesis when the \(H^5\) neighbourhood is written with a single global scale. It does **not** imply it in Step 44's conformal parametrization \(g=\phi_*e^{2f}(g_\Gamma+k)\) on covers where \(f\) can drift by \(O(1)\). Reformulating \(A_C\) on the conformal class removes this and strictly strengthens the theorem.

---

## 1. Lemma M

### (a) Block structure and \(B_1\)

**Independent check of the potentials.** I used the conventions \(D_A^2=\nabla^*\nabla+\tfrac s4+\tfrac12F_A^+\) and \(\rho(\sigma(\Phi))=(\Phi\Phi^*)_0\). These force \(|\sigma(\Phi)|^2=|\Phi|^4/8\), so \(|\sigma(\Phi_0)|^2=72\). Writing \(\psi_\parallel=u\Phi_0\), so that \(|\psi_\parallel|^2=24|u|^2\):

| Component | Contributions | Operator |
|---|---|---|
| \(\operatorname{Im}u\) | gauge term \(|\tfrac12\operatorname{Im}\langle\Phi_0,\psi\rangle|^2=144(\operatorname{Im}u)^2=6|\psi|^2\) | \(\Delta_0+6\) ✓ |
| \(\operatorname{Re}u\) | \(|\sigma'(\psi)|^2=|2(\operatorname{Re}u)\sigma(\Phi_0)|^2=288(\operatorname{Re}u)^2=12|\psi|^2\); Dirac potential \(\tfrac s4+\tfrac{|\Phi_0|^2}4=0\) | \(\Delta_0+12\) ✓ |
| \(\psi_\perp\) | Dirac potential \(\tfrac s4-\tfrac{|\Phi_0|^2}4=-12\); \(|\sigma'(\psi_\perp)|^2=\tfrac12|\Phi_0|^2|\psi_\perp|^2=+12|\psi_\perp|^2\) | \(\nabla^*\nabla_{K^{-1}}\) ✓ |

- The first-order cross terms are \(\langle\partial\bar{}\,u,\bar\partial^*v\rangle\)-type and \(a\)–\(\psi\) pairings. They integrate to zero exactly because \(\nabla\Phi_0=0\) and \(\bar\partial^2=0\).
- So (1.1) holds, and it reproduces Step 44's \((2,1,0)\times6\).

**The one-form block.**
- \((d^+)^*d^+=\tfrac12d^*d\) holds pointwise, since \(d^*{*}d=\pm{*}dd=0\). Hence \(B_1=dd^*+\tfrac12d^*d+6\) is correct.
- With \(\nabla^*\nabla=\Delta_1+6\):
\[
B_1=\tfrac12\nabla^*\nabla+3+\tfrac12dd^*=\tfrac12\Delta_1+6+\tfrac12dd^*.
\]
- Step 44's potential \(\tfrac12\) at \(s=-4\) is \(\lambda/2+|\Phi_0|^2/4=-\tfrac12+1\). It is the **Bochner** constant after dropping \(\tfrac12dd^*\); at holomorphic curvature \(-4\) it becomes \(\tfrac12\nabla^*\nabla+3\).
- Textual slip: §1 of the note calls \(\tfrac12\nabla^*\nabla+3\) the "Hodge form". It is the Bochner form; the Hodge form on coclosed forms is \(\tfrac12\Delta_1+6\).

**The strategist's worry (\(\tfrac12\Delta_H+3\), bottom \(3.5<4\)).**
1. *Wrong operator.* \(\tfrac12\Delta_H+3\) comes from reading the Bochner constant \(3\) as if it accompanied \(\Delta_H\). Since \(\tfrac12\nabla^*\nabla+3=\tfrac12\Delta_H+6\), the true coclosed operator is \(\tfrac12(\Delta_H+12)\), with bottom \(6.5\).
2. *Wrong test.* For a homogeneous operator \(T\) with unit principal symbol, the radial Green kernel decays like \(e^{-(\rho_0+\sqrt{\mu_{\rm ess}})r}\), where \(\mu_{\rm ess}\) is the bottom of its continuous spectrum. It is \(L^1\) against \(e^{2\rho_0r}\) iff \(\mu_{\rm ess}>\rho_0^2\).
   - The test must be applied to \(T\), not to \(\tfrac12T\): the factor \(\tfrac12\) rescales the spectrum but doubles the kernel without changing its decay.
   - For \(\tfrac12(\Delta_H+6)\) on coexact forms, \(\mu_{\rm ess}(\Delta_H+6)=\alpha_1+6=7>4\), giving decay \(2+\sqrt7\) and \(L^1\).
   - The same rule reproduces the \(K^{-1}\) rate: \(\mu_{\rm ess}=13\), giving \(2+\sqrt{13}\), even though the \(L^2\) bottom is the discrete value \(12\).
3. *Status of the counterfactual.* \(\tfrac12(\Delta_H+6)=\tfrac12\nabla^*\nabla\) on coclosed forms has no Kato mass. The "even undercounted" statement therefore rests on Carron–Pedon's \(\alpha_1=1\), not on the elementary argument. The actual \(B_1\) needs only Kato.
4. Textual slip in §5 of the note: "\(2+\sqrt7>4-2\)" should read \(2+\sqrt7>4\) (equivalently \(\sqrt7>\rho_0\)).

### (b) The \(K^{-1}\) radial reduction

**Geometry.**
- \(d\eta=e^{03}\mp e^{12}\) is the Kähler form; the script finds the minus sign with its orientation, which is immaterial.
- \(|d\eta|^2=2\) and \(|\eta|^2=\tfrac14\tanh^2r\) are verified symbolically, as is \(\operatorname{Ric}=-6g\).

**Gauge.**
- The Chern curvature is \(\pm6i\omega\).
- \(A=\pm6i\eta\) is the radial gauge. Any other radial-gauge form differs from it by a closed one-form \(\alpha\) with \(\alpha(\partial_r)=0\) that is smooth at \(o\). Such an \(\alpha\) equals \(d\varphi\) with \(\varphi\) constant on rays, hence \(\alpha=0\).
- \(V=|A|^2=9\tanh^2r\) ✓.
- \(\eta^\sharp=\tfrac12\cosh^{-2}r\,\xi_3\), where \(\xi_3\) is the right-\(U(1)\) Killing field of the \(U(2)\)-invariant metric. Hence \(\operatorname{div}\eta^\sharp=0\) and \(\langle df,\eta\rangle=0\), so (2.1) is exact.

**Radiality of the kernel.**
- The parallel frame satisfies \(k_*e=\chi(k)\,e\circ k\) for a character \(\chi\) of the isotropy group.
- In \(G(x,o)=F(x)\,e(x)\otimes e_o^*\) the characters cancel, so \(F(kx)=F(x)\). Transitivity of the isotropy on geodesic spheres then makes \(F\) radial.

**Landau state.** For \(f=\cosh^{-3}r\),
\[
-f''-(3\coth r+\tanh r)f'+9\tanh^2r\,f=\sinh^2r\cosh^{-5}r\,(-12+3+9)+\cosh^{-3}r\,(3+9)=12f.
\]
- \(f\) is \(L^2\) with density \(\sim e^{-2r}\) ✓.
- The asymptotic exponent equation \(\mu^2-4\mu+9-E=0\) gives the radial continuous threshold \(13\), consistent with \(13-\nu_d^2=12\). The Step-45 calibration is now derived independently.

**Zero energy and positivity.**
- \(\mu_+=2+\sqrt{13}\) ✓.
- Positivity: \(Jf'\to0\) at infinity because \(\mu_+>4\). Then \(Jf'(r)=-\int_r^\infty JVf<0\), so \(f\) is positive and decreasing on \((0,\infty)\) ✓.
- Pole: \(f\sim(4\pi^2r^2)^{-1}\) ✓.

**The \(1/9\) identity.** On \(\{r>\varepsilon\}\), \(\int VG=-2\pi^2Jf'(\varepsilon)\to1\). Hence \(9\int\tanh^2r\,G=1\) ✓, and \(\|G\|_1\ge1/9\).

**Rigorous upper bound (new).**
- Comparison step: let \(w=G_{\Delta_0}-G\). Then \(-(Jw')'=JVG\ge0\) and \(Jw'(0^+)=0\), so \(w\) is decreasing and tends to \(0\). Hence \(0<G\le G_{\Delta_0}\).
- The scalar kernel is explicit:
\[
G_{\Delta_0}(r)=\frac1{4\pi^2}\Bigl(\sinh^{-2}r-2\log\coth r\Bigr).
\]
- With \(Y=\sinh^21\), one gets
\[
\int_{r<1}G_{\Delta_0}=\tfrac12\Bigl[\tfrac Y2-\tfrac12\Phi(Y)\Bigr]=0.1512,\qquad
\Phi(y)=\tfrac12(y^2-1)\log(1+y)+\tfrac y2-\tfrac12y^2\log y .
\]
- On \(r\ge1\), \(V\ge9\tanh^21\), so \(\int_{r\ge1}G\le1/(9\tanh^21)=0.1916\).
- Therefore
\[
\tfrac19\le\|G_{K^{-1}}\|_{L^1}\le0.343,
\]
a certified \(L^\infty\) inverse bound for the \(\psi_\perp\) block. The numerical value \(0.2149\) lies inside this interval.

**Gradient.** The reported \(1.452\) is \(\int|f'|\) only. The full kernel gradient is \(|\nabla G|=\sqrt{f'^2+9\tanh^2r\,f^2}\). Its \(L^1\) norm is therefore at most \(1.452+3(0.215)\approx2.10\), still finite.

### (c) The one-form inverse

**Formula (2.2).** On an exact mode, \(\tfrac2{x+12}-\tfrac{x}{(x+6)(x+12)}=\tfrac1{x+6}\). On coexact modes the multiplier is \(\tfrac2{x+12}\); on harmonic forms it is \(\tfrac16\) ✓. Note \(\nabla^*\nabla+6=\Delta_1+12\).

**Kato term.** \(\|2(\nabla^*\nabla+6)^{-1}\|_{\infty\to\infty}\le\tfrac13\) ✓.

**Mixed Hessian.**
- The kernel of \(d\varphi(\Delta_0)d^*\) is \(d_xd_y\varphi(r)=\varphi''\,dr_x\otimes dr_y+\varphi'\,\nabla_x\nabla_yr\).
- Along \(\gamma\), the curvature operator \(R(\cdot,\gamma')\gamma'\) has parallel eigenspaces \(\gamma'\) (value \(0\)), \(J\gamma'\) (\(-4\)) and the orthogonal plane (\(-1\)). The mixed Hessian is therefore diagonal with entries \(0,\ -2/\sinh2r,\ -1/\sinh r\) ✓.
- Since \(2/\sinh2r\le1/\sinh r\), the operator norm is \(\max(|h''|,|h'|/\sinh r)\) ✓.

**Local cancellation.**
- In four dimensions \(G_\mu=\tfrac1{4\pi^2r^2}-\tfrac{\mu+c_0}{8\pi^2}\log\tfrac1r+\dots\). The difference gives \(rh'\to-6/8\pi^2=-0.07599\), matching the script.
- So the kernel is \(O(r^{-2})\), locally \(L^1\), with far decay \(2+\sqrt{10}\).

**Resulting bound.** \(\|B_1^{-1}\|_{\infty\to\infty}\le\tfrac13+\tfrac{I_{dd}}6\).
- Finiteness is proved.
- The value \(0.679\) is uncertified quadrature. A radial comparison for \(h,h',h''\), as for \(G_{K^{-1}}\) above, would certify it; no step of \(A_C\) needs the numerical value.

### (d) Quotients

- **Periodization.** The sum converges absolutely, and the sup-row bound is \(\le\|K\|_{L^1(\mathbb{CH}^2)}\) ✓.
- **Identification with the inverse.** Translates of the singular kernel are summed with locally uniform convergence of derivatives away from the diagonal, so \(NK_\Gamma=\delta\). Uniqueness follows from \(L^2\) invertibility.
- **Invertibility.** From the exact block form, \(N\ge\min(6,12,6,12)=6\) in \(L^2\), which is cleaner than Step 44's bound. On compact quotients \(\nabla^*\nabla_{K^{-1}}\) attains \(12\) on the \(p_g\) conjugate holomorphic 2-forms; this is harmless.
- **Surjectivity of \(\mathcal L\).**
  - \(\operatorname{ind}\mathcal L=(c_1^2-\sigma)/4+b_1-1-b^+\). Using \(\chi+\sigma=2-2b_1+2b^+\), this equals \((c_1^2-2\chi-3\sigma)/4\), which is \(0\) since \(K^2=2\chi+3\sigma\).
  - Injectivity plus index zero gives surjectivity, and \(\mathcal L^{-1}=N^{-1}\mathcal L^*\) has an \(L^1\) first-derivative kernel (\(O(r^{-3})\) at the pole).
- **Schauder step (2.3).** The \(L^\infty\) bound plus interior Schauder estimates on universal-cover unit balls give (2.3) ✓.

---

## 2. Theorem \(A_C\), steps 1–6

### Step 1 (Yamabe normalization)

- \(s_{u^2g}=u^{-3}(6\Delta u+s_gu)\), so the linearization at \(u=1\) is \(6\Delta v-24v+72v=6(\Delta_0+8)v\) ✓.
- Cross-check: this agrees with \(s'(2vg)=3\Delta(2v)+24(2v)\) from Step 4.
- \(P(g)\ge P(\hat g)\) holds. Gauss–Bonnet gives \(\tfrac12\int|\operatorname{Ric}^\circ|^2=\int|W|^2+\tfrac1{24}\int s^2-8\pi^2\chi\). The Weyl term is conformally invariant, and for \(Y([g])<0\) the constant-scalar-curvature metric minimizes \(\int s^2\,d\mu\) in the conformal class.
- Uniqueness of the constant-scalar-curvature metric at \(s=-24\) uses \(Y<0\), which holds near \(g_\Gamma\).

### Step 2 (DeTurck gauge)

- The tension \(\tau_{\hat g}(\Psi)\) involves only \(\hat g\) and \(\partial\hat g\), so the map \(C^{2,\alpha}\to C^{0,\alpha}\) is \(C^1\) with no derivative loss ✓.
- The Jacobi operator at the identity is \(\nabla^*\nabla-\operatorname{Ric}=\nabla^*\nabla+6\) ✓.
- Parametrize \(\Psi\) by \(\tilde\Psi(x)=\exp_xV(x)\) with \(V\) a \(\Gamma\)-equivariant field on the universal cover. Then no injectivity radius enters, consistent with the note.
- \(g'=(\Psi^{-1})^*\hat g\) is only \(C^{1,\alpha}\) a priori. The Ricci–DeTurck equation restores \(C^{2,\alpha}\) ✓.
- **Mislabel.** The resulting condition is the nonlinear harmonic-map gauge \(W_{g_\Gamma}(g')=g'^{ij}(\Gamma'-\Gamma)^k_{ij}=0\), not \(\beta_{g_\Gamma}(h)=0\). One has \(\beta_{g_\Gamma}(h)=O(|h||\nabla h|)\) pointwise.

### Step 3 (exact trace-free identity and expansion)

- \(s(g')=-24=4\lambda\), so \(\operatorname{Ric}^\circ(g')=\operatorname{Ric}(g')+6g'\) exactly ✓.
- In DeTurck gauge, \(\operatorname{Ric}(g')-\lambda g'=\tfrac12(\nabla^*\nabla-2\mathring R)h+Q(h)\). This follows from Besse's \(\operatorname{Ric}'(h)=\tfrac12\Delta_Lh-\delta^*\beta(h)\) and \(\Delta_L=\nabla^*\nabla+2\lambda-2\mathring R\).
- \(Q\) is quadratic, of the form \(h*\nabla^2h+\nabla h*\nabla h+\mathrm{Rm}*h*h\), so the pointwise bound holds ✓.

### Step 4 (York coercivity)

**Linearized scalar constraint.** With \(\Delta\ge0\), Besse's \(s'(h)=\Delta\operatorname{tr}h+\delta\delta h-\langle\operatorname{Ric},h\rangle\) gives:
- \(s'(k)=0\) for \(k\) TT;
- \(s'(\delta^*X)=\tfrac12\mathcal L_Xs=0\);
- \(s'(fg)=4\Delta f-\Delta f+24f=3\Delta f+24f\) ✓.

Hence \(\|f\|_{H^2}\le C\varepsilon\|h\|_{H^2}\) ✓.

**Bianchi relation.**
- \(\beta(\mathcal L_Xg)=\nabla^*\nabla X-\operatorname{Ric}X\), so \(\beta(\delta^*X)=\tfrac12(\nabla^*\nabla+6)X\).
- \(\beta(fg)=-df+2df=df\), and \(\beta(k)=0\).
- So \(\tfrac12(\nabla^*\nabla+6)X=-df+O(|h||\nabla h|)\): signs and constants are correct.
- The gauge error has \(H^1\) norm \(\le C\varepsilon\|h\|_{H^2}\), so \(\|X\|_{H^3}\le C\varepsilon\|h\|_{H^2}\) still holds.

**False sentence.** "The linearized operator kills \(\delta^*X\)" is false for the gauge-fixed operator. Diffeomorphism invariance kills \(\delta^*X\) under \(D(\operatorname{Ric}-\lambda g)\), and therefore
\[
\tfrac12(\nabla^*\nabla-2\mathring R)\delta^*X=\delta^*\beta(\delta^*X)=-\nabla^2f+O(\varepsilon\cdot),
\]
which is nonzero. It is harmless: \(\|\tfrac12(\nabla^*\nabla-2\mathring R)\delta^*X\|\le C\|X\|_{H^3}\le C\varepsilon\|h\|_{H^2}\).

**The \(H^2\) upgrade on the quotient.**
- Cauchy–Schwarz gives \(\|L_Ek\|\ge2\|k\|\).
- Then \(\|\nabla k\|^2\le\|L_Ek\|\|k\|+8\|k\|^2\), using \(|\mathring R|\le4\).
- \(\|\nabla^2k\|^2\) follows by commuting derivatives with \(\nabla\mathrm{Rm}=0\).

So \(\kappa\) is a model constant ✓.

**Does \(\|h\|_{H^2}\le2\|k\|_{H^2}\) follow?** Yes:
\[
\|h\|_{H^2}\le\|k\|_{H^2}+C\|X\|_{H^3}+C\|f\|_{H^2}\le\|k\|_{H^2}+C\varepsilon\|h\|_{H^2}.
\]

**Constant.** The final chain gives \(P(\hat g)^{1/2}\ge(\kappa/4-C\varepsilon)\|h\|_{H^2}\ge(\kappa/8)\|h\|_{H^2}\). The note's \(\kappa/4\) drops the \(-C\varepsilon\).

**Global versus pointwise input.** Only pointwise smallness (from \(C^{2,\alpha}_b\)) and global \(L^2\)/\(H^2\) identities are used. No Sobolev embedding enters, which is exactly what repairs \(A_H\).

### Step 5 (canonical branch)

- After the Bourguignon–Gauduchon identification, \(F(0)=O(|h|+|\nabla h|)\), using \(\nabla\Phi_0=0\) for the Dirac term ✓.
- \(\|DF(0)-\mathcal L\|\le C\varepsilon\) ✓.
- The nonlinearity \(q\) is zeroth-order bilinear, so the contraction closes in \(C^{1,\alpha}_b\) ✓.
- **Unwritten slice step.** "Unique modulo gauge" needs a uniformly local Coulomb slice: every solution \(C^{1,\alpha}_b\)-close to \((A_0,\Phi_0)\) is gauge-equivalent, by a gauge transformation near \(1\), to one satisfying the slice equation. The relevant operator is the positive-mass scalar gauge block (\(\Delta_0+6\)), which is Kato-invertible, so this is routine.
- Gauge transformations in other components of \(\operatorname{Map}(X,S^1)\) move \(\Phi_0\) by \(O(|\Phi_0|)\) pointwise and do not enter the ball.
- Since \(\phi\) is arbitrary, the branch lives in \(\phi^*\mathfrak s_K\). That class is \(\pm K\), and conjugation identifies the two.

### Step 6 (torsion bound)

- \(\|(DF(0)-\mathcal L)v\|\le C\varepsilon\|v\|_{H^1}\) and \(\|q(v)\|\le C\|v\|_\infty\|v\|_2\), so \(\|v\|_{H^1}\le C\|h\|_{H^1}\) ✓.
- \(n=\sigma(\Phi)/|\sigma(\Phi)|\) is gauge invariant. Since \(\nabla^{g'}_{A_0}\Phi_0=O(|\nabla h|)\) and \(|\Phi|\ge\tfrac12|\Phi_0|\), one gets \(|\nabla n|\le C(|\nabla v|+|v|+|\nabla h|)\) ✓.
- Hence \(\int|\nabla n|^2\le C\|h\|^2_{H^1}\le CP(\hat g)\) ✓.
- \(R_{\rm can}\) and \(\int|\nabla n|^2\) are not scale invariant as raw integrals. They are evaluated at the fixed scalar normalization, so the passage \(s=-24\to-4\) is a fixed factor absorbed into \(C'\).

---

## 3. The \(H^s\) neighbourhood

**Embedding.** In dimension four, \(H^s\subset C^{2,\alpha}\) requires \(s>4+\alpha\). So \(s=5\) works for every \(\alpha<1\), and \(s=4\) gives only \(C^{1,\alpha}\).

**Single-scale form.** With \(\operatorname{inj}\ge i_0\), balls of radius \(i_0\) in \(X_\Gamma\) are isometric to model balls. Hence
\[
\|c\phi^*g-g_\Gamma\|_{H^5(X_\Gamma)}\le\varepsilon\ \Longrightarrow\ \|c\phi^*g-g_\Gamma\|_{C^{2,\alpha}_b}\le C(i_0)\varepsilon .
\]
Along cover towers \(i_0\) does not decrease. In this form "\(A_H\) survives" is correct.

**Step 44's parametrization does not give this.** For \(g=\phi_*e^{2f}(g_\Gamma+k)\) with \(\|k\|_{H^5}+\|df\|_{H^4}\le\varepsilon\), the implication does not hold.
- Example: on cyclic covers of degree \(n\) of a ball quotient with \(b_1>0\), take \(f\) of unit oscillation and gradient \(\sim1/n\).
- Then \(\|df\|^2_{H^4}\sim V/n^2\sim1/n\to0\), yet \(e^{2f}\) is not uniformly close to any single constant \(c\).

**Conformal-class formulation.** Step 1 uses only the conformal class, and \(P(g)\ge P(\hat g)\) holds for every \(g\in[\hat g]\). The theorem therefore holds under the strictly weaker hypothesis:
\[
\exists\,\tilde g\in[g]:\ \|c\phi^*\tilde g-g_\Gamma\|_{C^{2,\alpha}_b}\le\varepsilon_0 .
\]
This version contains the \(H^5\) form of \(A_H\) in Step 44's parametrization, conformal drift included.

**Original \(A_H\).** The absolute-\(H^2\) statement remains unproved, because \(h*\nabla^2h\) needs \(L^\infty\) control.

---

## 4. Corrected statements

**Lemma M.** All four blocks of \(N\) are invertible on every compact \(X_\Gamma\), with \(\Gamma\)-independent \(L^\infty\), \(C^{2,\alpha}_b\) and divergence-form \(C^{1,\alpha}_b\) inverse bounds. Certified constants:

| Block | \(\infty\to\infty\) bound |
|---|---|
| \(\Delta_0+12\) | \(\tfrac1{12}\) |
| \(\Delta_0+6\) | \(\tfrac16\) |
| \(\nabla^*\nabla_{K^{-1}}\) | \(\in[\tfrac19,\,0.343]\) |
| \(B_1\) | \(\tfrac13+\tfrac16I_{dd}\), with \(I_{dd}<\infty\) (numerically \(2.074\)) |

**Theorem \(A_C\).** Assume some metric conformal to \(g\) satisfies \(\|c\phi^*\tilde g-g_\Gamma\|_{C^{2,\alpha}_b}\le\varepsilon_0\). Then:
1. The Yamabe representative \(\hat g\) admits a harmonic-map gauge \(g'=g_\Gamma+h\) with \(\|h\|_{C^{2,\alpha}_b}\le C\varepsilon_0\) and \(P(g)\ge P(\hat g)\ge(\kappa/8)^2\|h\|^2_{H^2}\).
2. There is a solution of the canonical class within \(C\varepsilon_0\) of \((A_0,\Phi_0)\), unique modulo identity-component gauge among solutions within a fixed model distance. Uniqueness is subject to the uniformly local Coulomb slice lemma.
3. That solution satisfies \(\int|\nabla n|^2\le C\|h\|^2_{H^1}\le C'P(g)\), with all constants depending only on \(\mathbb{CH}^2\).

**Unaffected material.** None of the above concerns branch selection for other solutions, localization over blow-ups, or any tariff. The note's §3 list of what \(A_C\) does not establish stands.
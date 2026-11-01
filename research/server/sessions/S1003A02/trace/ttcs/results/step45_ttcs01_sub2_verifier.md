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

# Verification memo: Step 45, Lemma M and Theorem K

## Verdict

**Lemma M.** The line-sector and one-form-sector statements are correct as written, in the normalization the note uses. I confirmed the calibration \(H_{K^{-1}}(\nu)=13-\nu^2\) by three routes that do not depend on one another. One gap needs filling: the script hard-codes \(12+1=13\), so it does not test this calibration itself. Periodization does give a \(\Gamma\)-independent \(L^\infty\) inverse. The extensive form \(A_C\) of Theorem A, on closed ball quotients and their finite covers, now has every linear input it needs. The few remaining nonlinear items, listed in §3, use the same mechanism and need no new idea.

**Theorem K.** (K0), (K1) and the integrated inequality (K3) are exact. The constant \(4\sqrt6/3\) is sharp even when \(E\) is restricted to normal directions of the orbit. Sharpness on the box follows from the short analytic argument in §5, so it no longer rests on differential evolution. The printed numerical consequence should read \(0.104855\ldots\), not "\(\ge 0.10486\ldots\)".

Neither result says anything about \(X_\Gamma\#k\overline{\mathbb{CP}}^2\).

---

## 1. Lemma M, line sector

### Identification of \(K^{-1}\) with \(|l|=3\)

In Will's convention \(\chi_l(\operatorname{diag}(A,y))=y^l\) with \(\det A\cdot y=1\). The isotropy acts on \(T^{1,0}_0\cong\mathbb C^n\) by \(z\mapsto Azy^{-1}\), coming from \((Az+B)(Cz+D)^{-1}\). Its determinant is \(\det A\,y^{-n}=y^{-(n+1)}\). Hence:

- \(K\) has character \(y^{\pm(n+1)}\), and \(K^{-1}\) has the opposite sign.
- For \(n=2\), \(|l|=3\).
- Will's results (poles, discrete series, decay) depend only on \(|l|\). Also, \(K^{-1}\cong\overline K\) as Hermitian line bundles with connection, so the spectral data of \(\nabla^*\nabla\) coincide for the two bundles.

### Metric normalization

Will uses \(B(H_0,H_0)=1\) and the density \(\delta(t)=\sinh^{2(n-1)}t\,\sinh 2t\). The \(\sinh t\) factors correspond to curvature \(-1\) directions and \(\sinh 2t\) to the \(J\)-direction of curvature \(-4\). So \(t\) is geodesic distance at holomorphic sectional curvature \(-4\), and the volume grows as \(e^{2nt}=e^{4t}\). This agrees with Carron–Pedon (\(\rho=n\), curvature in \([-4,-1]\)) and with Askour et al., where \(-\Delta_{v=0}\) has bottom \(n^2\).

### Affine dependence on \(-\nu^2\)

By Kuga and Carron–Pedon (2.20), \(\nabla^*\nabla=-\Omega_{\mathfrak p}=-\Omega_{\mathfrak g}-\Omega_{\mathfrak k}\), and \(\Omega_{\mathfrak k}\) is a scalar on \(\tau_l\). Will gives \(\chi(\nu,l)=\nu^2-\rho^2+\text{const}\). Therefore \(\nabla^*\nabla=A-\nu^2\) on the \(\nu\)-spherical type.

The spectrum then has two parts:

- **Continuous:** \(\nu\in i\mathbb R\), giving \([A,\infty)\).
- **Discrete:** Will's \(L^2\) parameters \(\nu^+_{k,l}=|l|-n-2k\ge0\). For \(|l|=3\), \(n=2\) only \(\nu=1\) occurs, giving the single eigenvalue \(A-1\).

### Three independent checks that \(A-1=12\), i.e. \(A=13\)

**(a) Kodaira identity and Bergman space.** On \(K\) (equivalently \(K^{-1}\) by conjugation), \(\nabla^*\nabla=2\bar\partial^*\bar\partial+n|\lambda|\), and \(n|\lambda|=2\cdot6=12\). Equality holds exactly on \(L^2\) holomorphic sections. These form the Bergman space with weight \((1-|z|^2)^{v-n-1}\), \(v=3\), which is nonzero because \(v>n\). So 12 is an eigenvalue, it is the bottom, and it is the discrete state.

**(b) Askour–Bouaouid–Elhadouni.** For \(\Delta_v\) on \(L^2((1-|z|^2)^{v-n-1}dm)\):

- The point spectrum of \(-\Delta_v\) is \(4l(v-n-l)\), with ground state \(0\) on holomorphic functions.
- The continuous threshold is \((v-n)^2\).

Holomorphic \(L^2\) sections with this weight are sections of the bundle with fiber metric \((1-|z|^2)^v\), which is \(K^{v/(n+1)}\). So \(v=n+1=3\) is \(K\), and the gap from ground state to threshold is \((v-n)^2=1=(|l|-n)^2\). This matches Will.

**(c) Hodge Weitzenböck on \(\Lambda^{2,0}\subset\Lambda^+\otimes\mathbb C\).** We have \(\Delta=\nabla^*\nabla-2W^++s/3\), and the Kähler \(W^+\) equals \(-s/12\) on \(K\oplus\bar K\). Hence \(\Delta|_{\Lambda^{2,0}}=\nabla^*\nabla+s/2=\nabla^*\nabla-12\).

- The Hodge spectrum in middle degree is \(\{0\}\cup[\alpha_2,\infty)\) with \(\alpha_2=1\) (Carron–Pedon Thm 2.4, \(p=n\)).
- So \(\nabla^*\nabla\) has \(12\) as a discrete eigenvalue, and its continuous part starts at or above 13.

The same three-way check in complex dimension one passes. On the disc with curvature \(-4\), \(\nabla^*\nabla_K=\Delta_1+4\) has spectrum \(\{4\}\cup[5,\infty)\). This equals \(n|\lambda|=4\) plus a gap of 1.

### Zero energy, decay and \(L^1\)

- Zero energy means \(13-\nu^2=0\), so \(\nu=\sqrt{13}\). This exceeds \(\rho=2\), inside Will's half-plane \(\operatorname{Re}\nu>\rho\). There, Theorem 3.4(e) says the kernel \(-Q_{\nu,l}/(2\nu c(\nu,l))\) is the resolvent, and 3.4(c) gives \(Q\in L^1(G)\) directly.
- **Normalizing constant.** At \(\nu=\sqrt{13}\), \(c(\nu,\pm3)\) involves \(\Gamma((\sqrt{13}+5)/2)\) and \(\Gamma((\sqrt{13}-1)/2)\), both finite. So \(2\nu c\neq0\), and the remark about poles is consistent but not needed.
- **Decay.** \(Q_{\nu,l}(a_t)=u^{-l}\tilde Q\sim e^{-lt}e^{-(\nu+n-l)t}=e^{-(\nu+\rho)t}\), independent of \(l\). Against volume \(e^{4t}\) the margin is \(\sqrt{13}-2\).
- **Local singularity.** It is \(t^{-2(n-1)}=t^{-2}\), which is integrable in dimension 4.

A second derivation of the line-sector bound uses only Carron–Pedon. Write \(\nabla^*\nabla=\Delta_2+12\) on the parallel subbundle \(\Lambda^{2,0}\). Then \((\Delta_2+12)^{-1}=(\Delta_2-\alpha_2+s^2)^{-1}\) with \(s=\sqrt{13}\), and Theorem 3.6 gives decay \(e^{-(\rho+\sqrt{13})t}\). The middle-degree pole sits at \(s=\sqrt{\alpha_2}=1\), not at \(\sqrt{13}\). This route does not need the exact threshold of the \(\Lambda^{2,0}\) K-type.

---

## 2. Lemma M, one-form block

### Operator

Two facts give the operator:

- The identity \((d^+)^*d^+=\tfrac12 d^*d\) holds as an operator identity, because \(d^*{*}d=-{*}dd=0\).
- The Clifford mass is \(|\Phi_0|^2/4=6\) when \(|\Phi_0|^2=-s=24\).

So \(B_1=dd^*+\tfrac12d^*d+6\). This is the same as Step 44's "potential ½" at \(s=-4\), which is written in Bochner form: \(\tfrac12\mathrm{Ric}+|\Phi|^2/4=-\tfrac12+1\).

### Inverse identity

On closed manifolds and on \(\mathbb{CH}^2\) (no \(L^2\) harmonic 1-forms, since \(\alpha_1=1>0\)), \(L^2\) splits into closures of exact and coexact forms.

- **Exact forms \(a=df\):** \(d^*a=\Delta_0f\) and \((\Delta_1+12)^{-1}df=d(\Delta_0+12)^{-1}f\). The formula then gives
  \[
  d(\Delta_0+12)^{-1}(\Delta_0+6)^{-1}\bigl[2(\Delta_0+6)-\Delta_0\bigr]f=d(\Delta_0+6)^{-1}f=(\Delta_1+6)^{-1}df .
  \]
- **Coexact forms:** only \(2(\Delta_1+12)^{-1}=(\tfrac12(\Delta_1+12))^{-1}\) survives.

Both agree with the script's zero residuals.

### Thresholds

In Carron–Pedon normalization, \(\alpha_0=\rho^2=4\) and \(\alpha_1=(n-1)^2=1\). The exact sector carries the scalar spectrum \([4,\infty)\).

### A cleaner local argument

Partial fractions remove the convolution the note invokes:
\[
(\Delta_0+6)^{-1}(\Delta_0+12)^{-1}=\tfrac16\bigl[(\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}\bigr],
\]
with \(s^2=10\) and \(s^2=16\).

- **Local behaviour.** The leading \(r^{-2}\) singularities cancel and leave a \(\log r\) term. So \(d_xd_y\) of this kernel is \(O(r^{-2})\). This is homogeneous of degree \(-2>-4\): integrable, with no principal-value issue.
- **Decay.** The rates are \(e^{-(2+\sqrt{10})r}\) and \(e^{-6r}\). Derivatives keep these rates, because the Fuchsian expansion \(e^{-t\sqrt{E+s^2}}\sum a_le^{-lt}\) (Carron–Pedon Prop. 3.3) converges for \(t>1\) and can be differentiated term by term.
- **Smallest margin.** \(\sqrt{10}-2=1.1623\).

---

## 3. Periodization and the status of \(A_C\)

### Periodization

The unfolding estimate is correct. To identify \(G_\Gamma f\) with \(B^{-1}f\) on \(X_\Gamma\) three facts are needed:

1. **\(BG=I\) on bounded inputs.** Approximate by \(\chi_R\tilde f\) and use \(L^1\) convergence plus local elliptic regularity.
2. **Convergence of the lattice sum.** It needs rate \(>\delta(\Gamma)=4\), which is the same condition as \(L^1\).
3. **Uniqueness on \(X_\Gamma\).** \(B_1\ge6\) for every \(\Gamma\), whatever \(b_1\) is, and \(\nabla^*\nabla_{K^{-1}}\ge12\).

### Strengthening

Run the interior Schauder estimates on the universal cover, applied to lifted periodic functions. The Hölder constants then depend only on \(\mathbb{CH}^2\); no injectivity-radius bound \(i_0\) enters \(A_C\), unlike \(A_H\).

### Remaining nonlinear items

The IFT in uniformly local \(C^{k,\alpha}\) spaces needs the following. Each is either Laplace-type with positive mass, or reduces by the same exact/coexact mechanism.

- **First-order inverse.** \(L\) is square (rank \(8\to8\)), and \(L^{-1}=(L^*L)^{-1}L^*\) has kernel \(L^*_yG\). Its singularity is \(r^{-3}\) and its exponential rate is unchanged, so it is \(L^1\). This gives the uniform \(C^{0,\alpha}\to C^{1,\alpha}\) inverse the SW IFT actually uses. The note does not state this step.
- **Metric slice.** In Bianchi gauge the operators are \(\nabla^*\nabla+|\lambda|\) and \(6\Delta+8\), handled by Kato domination. If the TT/York form \(g=\phi_*e^{2f}(g_\Gamma+k)\) is kept in Hölder norms, the conformal Killing normal operator is not Laplace-type. From (G3) it equals \(2\nabla^*\nabla+dd^*+2|\lambda|=2\Delta_1+dd^*+24\). This splits as:
  - exact sector \(3(\Delta_1+8)\), with \(s=\sqrt{12}\);
  - coexact sector \(2(\Delta_1+12)\), with \(s=\sqrt{13}\);
  - margins \(\sqrt{12}-2\) and \(\sqrt{13}-2\), so it also passes.
- **Coulomb slice for SW.** A scalar Laplacian plus a mass proportional to \(|\Phi_0|^2\), handled by Kato domination.
- **Block decomposition.** The decomposition of \(L^*L\) into \(B_1\), the \(\psi_\parallel\) blocks and \(\nabla^*\nabla_{K^{-1}}\) is inherited from Step 44's symbol computation. That computation has the vanishing \(a\)–\(\psi\) cross terms and the listed zeroth-order potentials. Step 45 does not recheck it.
- **Item 2.** Combine the uniform \(L^\infty\) smallness of the branch \(v\) (to absorb quadratic terms) with the \(\Gamma\)-independent \(L^2\)/\(H^1\) gap of Step 44. This gives \(\|v\|_{H^1}\le C(\|k\|_{H^1}+\|df\|)\). In the extensive neighborhood \(f\) is uniformly close to a constant because \(c\) is a single constant.

With these, \(A_C\) holds on closed \(X_\Gamma\). Its uniqueness is local: it holds among solutions uniformly \(C^{1,\alpha}\)-close to the canonical one. The phrase "excludes the diffuse common mode within that extensive neighborhood" carries content only after localization to the blow-up bulk, which the note correctly leaves open. That localization needs bulk field selection and control of the collar term \(\int_{\Omega'\setminus\Omega}|k|^2\).

---

## 4. Theorem K: factorization and expansion

Write \(a=r^2/4\) and \(M_*=\tfrac{1-a}{3}I-\hat\omega\hat\omega+a\,nn\). Then:

- \(x_*=\tfrac{1-a}3-q+a\)
- \(|M_*|^2=1+a^2-2aq-\tfrac{(1-a)^2}3\)
- \(r^2x_*-4|M_*|^2=r^2q-\tfrac{r^2}3-\tfrac83\)
- \(p(r)=-r^3+\tfrac73r^2-\tfrac43\)

Summing gives \(f_*=r^2q+2r^2-r^3-4=-(2-r)^2(r+1)-r^2(1-q)\), which is (K0). Equality holds only at \(r=2\), \(q=1\). At \(r=0\), \(f=-4|W^+|^2-4/3<0\), so the undefined \(n\) on \(\{\rho=0\}\) does no harm.

The expansion is \(f=f_*+\langle r^2(nn)_0-8M_*,E\rangle-4|E|^2\). From \(|(nn)_0|^2=\tfrac23\), \(\langle(nn)_0,M_*\rangle=x_*\), and the formula for \(|M_*|^2\), we get
\[
|G|^2=\tfrac23r^4+\tfrac{128}3-16r^2\bigl(q-\tfrac13\bigr),
\]
which is (K1).

---

## 5. Theorem K: the sharp constant

### Reduction to a two-variable function

For fixed \((r,q)\), \(\sup_{t>0}(f_*+|G|t-4t^2)/t=|G|-4\sqrt{-f_*}\). This is the script's `c_eff`.

Put \(u=1-q\), \(A=(2-r)^2(r+1)\) and \(B=\sqrt{2/3}\,(8-r^2)\). Then \(|G|^2=B^2+16r^2u\) and \(-f_*=A+r^2u\). Differentiating,
\[
\partial_u c\le0\iff 16A\le B^2 .
\]

### Analytic proof that \(C_{\mathcal K}=4\sqrt6/3\) is the maximum

**Region \(16A\le B^2\).** Here \(c\le c(r,q=1)=B-4(2-r)\sqrt{r+1}\), and
\[
c(2,1)-c(r,1)=(2-r)\bigl[4\sqrt{r+1}-\sqrt{2/3}\,(r+2)\bigr]\ge(2-r)(4-3.266)\ge0 .
\]

**Region \(16A>B^2\).** Here \(c\le c(r,0)\le\sqrt{2/3}\sqrt{112}-4\sqrt{\min(r^3-2r^2+4)}\le8.641-6.711<1.94\).

So the maximum over \([0,2]\times[0,1]\) is \(c(2,1)=\sqrt{32/3}=4\sqrt6/3\). The script's \(q=0\) edge maximum, 0.9004, agrees with this. Its \(r=2\) edge value 3.2650 falls slightly short only because of bounded-optimizer tolerance: on \(r=2\), \(c=\sqrt{32/3+64u}-8\sqrt u\) is strictly decreasing.

### Sharpness with the closest-point constraint

Choosing the closest \(W_*\) forces \(E\perp T_{W_*}\mathcal K=\{[A,W_*]\}\).

- At \((r,n)=(2,\hat\omega)\), \(M_*=0\) and \(G=-4W_*\), which is radial.
- \(\langle[A,W_*],W_*\rangle=0\), so \(G\) is normal to the orbit.
- \(E=-\varepsilon W_*\) is admissible, with \(\operatorname{dist}=\varepsilon|W_*|\), because \(\mathcal K\) lies on the sphere \(|W|^2=2/3\).

So the constant is sharp in the restricted sense too. The extremal departure is a contraction of \(|W^+|\) at fixed Kähler spectral shape. That is the same direction as the \(4\mathcal W_+\) term in the closed identity \(P=4\mathcal W_++\tfrac43V-8\pi^2(A-k)\). Any quadratic improvement must come from an integrated identity tying \(\int\operatorname{dist}\) to \(\int|W^+|^2\). The pointwise formula \(f=4E(\hat\omega,\hat\omega)-4|E|^2\) at the equality state is correct and uses admissible normal \(E\).

---

## 6. Integration over the sign family and the numerical consequence

### Integrated inequality (K3)

The steps are:

1. Theorem W gives \(\mathfrak S\le\mathbb E_\epsilon\int f(W^+,\rho_\epsilon,n_\epsilon)\) after dropping \(-4\|\zeta\|^2-\mathcal W\).
2. \(\operatorname{dist}(W^+,\mathcal K)\) does not depend on \(\epsilon\), so averaging is immediate.
3. \(P(g)\ge P(\hat g)\) follows from Gauss–Bonnet, \(P=2\int(|W|^2+s^2/24)-16\pi^2\chi\), together with \(\int s^2\ge Y^2\) when \(Y<0\).
4. For pure blow-ups \(Q=k\).

(K3) and (K4) follow, with \(\sqrt6\pi^2=24.175495\).

### Numerical consequence

With \(1-c\in[0.0043372672289,\,0.0043372672468]\), the bound is \(\int\operatorname{dist}\ge0.1048556\,k\). The printed "\(\ge0.10486\ldots\)" overstates the fifth digit.

For comparison, \(16\pi^2(1-c)=0.684913\) reproduces Theorem N's Nijenhuis bound. Both are asymptotic in \(k\) for the closed replica, with the \(o(k)\) correction retained at finite \(k\).

---

## 7. Textual defects that affect use

- **Corrupted LaTeX.** In the note, `\frac` was mangled into "rac" (a form-feed escape) and "	frac" (a tab) in the definition of \(f\) and in (K1). The two central displays of §3 do not render.
- **Wrong metric in §4's measurement list.** The list puts \(\int\operatorname{dist}(W^+,\mathcal K)\) on the smooth metric \(g\). (K3) concerns the scalar-\(-4\) Yamabe representative \(\hat g\), which is smooth and conformal to \(g\). The number must be computed for \(\hat g\) unless \(s_g\equiv-4\).
- **Calibration not tested by the script.** The script enters \(13\) as \(12+\nu_d^2\) rather than computing it. A short radial computation would confirm the calibration independently:
  - solve Will's \(\tau_3\)-radial ODE for \(n=2\), or
  - evaluate \(\nabla^*\nabla\) on the Bergman ground state \((1-|z|^2)^0\) of \(A^2_3\), or
  - compute the \(\Lambda^{2,0}\) threshold from Pedon's K-type data.
- **Convolution step.** The note's "convolution of the two shifted scalar resolvents" is correct but needs no convolution estimate. Partial fractions give it directly with explicit local cancellation.

## 8. Unresolved

On \(X_\Gamma\#k\overline{\mathbb{CP}}^2\), neither Lemma M/\(A_C\) nor Theorem K prices a subunit saving. Three inputs would be needed:

- a bulk-selection theorem placing actual blow-up monopoles near the canonical branch;
- collar control of \(\int_{\Omega'\setminus\Omega}|k|^2\);
- an integrated identity that turns the linear Weyl departure in (K3) into a quadratic cost. The natural candidates are Bach stationarity, or pairing \(\int\operatorname{dist}\) against \(\int|W^+|^2\) through the closed identity.
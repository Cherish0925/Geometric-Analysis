# Step 46 — An elementary proof of Lemma M, the extensive perturbative theorem \(A_C\), and the three regimes

Session S1003A02, Agent2. Script/data: `workspace/scripts/step46_lemmaM_elementary.py` →
`workspace/data/step46_lemmaM_elementary.json`. Inherits Step 44
(`step44_perturbative_ke_coercivity_and_pocket_price.md`), Step 45
(`step45_lemmaM_and_weyl_departure.md`) and the TTCS verification
`trace/ttcs/results/step45_ttcs01_verifier1_integration.md`.

Normalization in §§1–3: \(\mathbb{CH}^2\) with holomorphic sectional curvature \(-4\), \(\operatorname{Ric}=\lambda g\),
\(\lambda=-6\), \(s=-24\), half volume-growth exponent \(\rho_0=2\) (shells grow like \(e^{4r}\)). Theorem N/W
quantities use \(s=-4\); the conversion is the homothety \(g\mapsto 6g\) (Laplace eigenvalues divide by 6;
\(P\), \(R\) are scale invariant).

Step 45 settled the homogeneous kernels by reading Will's line-bundle resolvent and Carron–Pedon's
form spectrum, with the \(K^{-1}\) calibration \(13\) entered by hand. This note (i) replaces that input by
a self-contained ODE/Kato proof with explicit inverse norms, (ii) answers the question whether the
connection (one-form) sector could break Lemma M, and (iii) writes the uniformly local nonlinear
argument, so that \(A_C\) becomes a theorem for the canonical branch. It closes the perturbative regime of
the diffuse-rotation problem and nothing more: it is not a blow-up tariff.

---

## 1. The normal operator at the canonical solution, block by block

Let \((A_0,\Phi_0)\) be the canonical Kähler solution on a compact ball quotient \(X_\Gamma\), with
\(\nabla_{A_0}\Phi_0=0\), \(|\Phi_0|^2=-s=24\), and \(\mathcal L\) the gauge-fixed linearization of Step 44 (G4),
gauge coefficient \(-\tfrac12\). Step 44 verified in a Clifford model that all first-order cross terms of
\(\|\mathcal L(a,\psi)\|^2\) cancel when \(\nabla\Phi_0=0\) and that the zeroth-order potential is diagonal. Hence
\(N:=\mathcal L^*\mathcal L\) splits exactly as
\[
N= B_1\ \oplus\ (\Delta_0+12)\ \oplus\ (\Delta_0+6)\ \oplus\ \nabla^*\nabla_{K^{-1}},
\tag{1.1}
\]
acting on \(a\in\Omega^1\), \(\operatorname{Re}\psi_\parallel\), \(\operatorname{Im}\psi_\parallel\) (the gauge direction), and
\(\psi_\perp\in\Phi_0^\perp\cong\Lambda^{0,2}\cong K^{-1}\). The constants are the Step-44 potentials
\((2,1,0)\) at \(s=-4\) multiplied by \(6\).

**The one-form block.** Exactly,
\[
\|d^*a\|^2+\|d^+a\|^2+\|\tfrac12a\cdot\Phi_0\|^2=\langle(dd^*+\tfrac12d^*d+6)a,a\rangle,
\]
because \((d^+)^*d^+=\tfrac12d^*d\) on one-forms (\(d^*{*}da=\pm{*}dda=0\)) and
\(|\tfrac12a\cdot\Phi_0|^2=\tfrac14|a|^2|\Phi_0|^2=6|a|^2\). So
\[
B_1=dd^*+\tfrac12d^*d+6 .
\]
The Step-44 statement "potential \(\tfrac12\) on 1-forms" at \(s=-4\) refers to the Bochner form
\(\tfrac12\nabla^*\nabla+\tfrac12\) obtained after **dropping** \(\tfrac12\|d^*a\|^2\) and using
\(\Delta_1=\nabla^*\nabla+\operatorname{Ric}\); in that Bochner form at hol. \(-4\) it is \(\tfrac12\nabla^*\nabla+3\), and exactly \(B_1=\tfrac12\nabla^*\nabla+3+\tfrac12dd^*\). Writing
\(\tfrac12d^*d+dd^*+3\) mixes the two forms and undercounts the mass by \(3\).

*The connection-sector worry.* On coclosed forms \(B_1=\tfrac12\Delta_1+6=\tfrac12(\Delta_1+12)\), with
\(\Delta_1\ge\alpha_1=1\) on coexact forms; on exact forms \(B_1=\Delta_1+6\ge10\). The relevant comparison for
\(L^1\) is not "bottom of \(B_1\) versus \(\rho_0^2\)": the Green kernel of \(\tfrac12(\Delta_1+12)\) is twice that of
\(\Delta_1+12\), and it is the shift \(12\) (with the form threshold \(\alpha_1\)) that sets the decay
\(e^{-(\rho_0+\sqrt{\alpha_1+12})r}\). Even the undercounted operator \(\tfrac12\Delta_1+3=\tfrac12(\Delta_1+6)\) would give
decay \(e^{-(2+\sqrt7)r}\), still \(L^1\) against \(e^{4r}\). The connection sector is safe; §2.3 proves this without
Carron–Pedon.

---

## 2. Lemma M by ODE and Kato domination

**Lemma M.** On every compact quotient \(X_\Gamma=\Gamma\backslash\mathbb{CH}^2\), \(N\) is invertible and
\[
\|N^{-1}f\|_{L^\infty}\le C_0\|f\|_{L^\infty},
\qquad
\|\nabla N^{-1}f\|_{L^\infty}+\|N^{-1}\nabla^*F\|_{L^\infty}\le C_1(\|f\|_{L^\infty}+\|F\|_{L^\infty}),
\]
with \(C_0,C_1\) depending only on \(\mathbb{CH}^2\). Explicitly, per block (hol. \(-4\) units),
\[
\|B_1^{-1}\|_{\infty\to\infty}\le \tfrac13+\tfrac16 I_{dd}=0.6790,\quad
\|(\Delta_0+12)^{-1}\|=\tfrac1{12},\quad \|(\Delta_0+6)^{-1}\|=\tfrac16,\quad
\|(\nabla^*\nabla_{K^{-1}})^{-1}\|\le\|G_{K^{-1}}\|_{L^1}=0.21490,
\]
where \(I_{dd}\approx2.0738\) is computed in §2.3. Rigorous content: finiteness of every norm, the exact values \(1/12,1/6\),
\(\|B_1^{-1}\|\le\tfrac13+\tfrac16I_{dd}\), and \(\|G_{K^{-1}}\|_{L^1}\ge1/9\). The decimals \(0.6790\), \(0.2149\), \(2.0738\) are floating-point
ODE/quadrature estimates (finite truncation radius), not certified upper bounds.

### 2.1 Positive-mass blocks

For \(\nabla^*\nabla+\mu\) on a metric bundle with \(\mu>0\) constant (or \(\ge\mu\) pointwise), Kato's semigroup
domination \(|e^{-t\nabla^*\nabla}u|\le e^{-t\Delta_0}|u|\) gives \(|(\nabla^*\nabla+\mu)^{-1}u|\le(\Delta_0+\mu)^{-1}|u|\)
pointwise, and \((\Delta_0+\mu)^{-1}1=1/\mu\). This holds directly on \(X_\Gamma\). It covers the two
\(\psi_\parallel\) blocks, the Yamabe linearization \(6(\Delta_0+8)\), and the DeTurck/Bianchi operator
\(\nabla^*\nabla+6\) on vector fields used in §3. The script checks \(\|G_\mu\|_{L^1}=1/\mu\) for \(\mu=6,12\) to
\(10^{-7}\) relative accuracy.

### 2.2 The \(K^{-1}\) block (magnetic, no pointwise mass)

Write \(g=dr^2+\sinh^2r(\sigma_1^2+\sigma_2^2)+\sinh^2r\cosh^2r\,\sigma_3^2\) with unit-\(S^3\) left-invariant forms. The
script verifies symbolically: \(\operatorname{Ric}=-6g\) (residual \(4\times10^{-12}\) at sample points),
\(\omega=d\eta=e^0\wedge e^3-e^1\wedge e^2\) (orientation of the script's frame) with \(\eta=\tfrac12\sinh^2r\,\sigma_3\) and \(|\omega|^2=2\), and \(|\eta|^2=\tfrac14\tanh^2r\).

1. *Radial gauge.* The Chern connection of \(K^{-1}\) has curvature \(\pm i\rho_{\rm Ric}=\mp6i\omega\); in radial
   gauge (\(A(\partial_r)=0\), smooth at the origin) \(A=\pm6i\eta\). Parallel transport from the origin along
   geodesics defines a frame \(e\) equivariant under the isotropy \(U(2)\), so the Green kernel
   \(G(\cdot,o)\) is \(f(r)\,e\otimes e_o^*\) with \(f\) radial. Since \(\eta^\sharp\) is a radial function times a
   Killing field, \(\operatorname{div}\eta^\sharp=0\) and \(\langle df,\eta\rangle=0\); hence
   \[
   \nabla^*\nabla(fe)=\Bigl(-f''-(3\coth r+\tanh r)f'+V f\Bigr)e,\qquad V=|A|^2=9\tanh^2r .
   \tag{2.1}
   \]
2. *Landau state (independent calibration).* \(f=\cosh^{-3}r\) satisfies (2.1) with eigenvalue exactly \(12\)
   (symbolic), and is \(L^2\) since \(\cosh^{-6}r\cdot\sinh^3r\cosh r\sim e^{-2r}\). This is the bottom \(2|\lambda|\), and its decay
   \(e^{-3r}=e^{-(\rho_0+\nu_d)r}\) with \(\nu_d=1\) reproduces Will's lowest discrete parameter. Thus the
   calibration \(H(\nu)=13-\nu^2\) of Step 45 is now derived, not assumed: \(V\to9\) gives the continuous
   threshold \(\rho_0^2+9=13\).
3. *Zero energy.* Since \(V=9-9\,\mathrm{sech}^2r\) with integrable correction, Levinson's theorem gives
   solutions \(\sim e^{-\mu_\pm r}\), \(\mu^2-4\mu-9=0\), i.e. \(\mu_+=2+\sqrt{13}\). The decaying solution is positive and
   decreasing (\(Jf'(r)=-\int_r^\infty9J\tanh^2s\,f\,ds<0\) once \(f>0\); Sturm uniqueness), has the four-dimensional singularity \((4\pi^2r^2)^{-1}\) at
   \(0\) (checked: \(4\pi^2r^2G=0.99999\) at \(r=10^{-3}\)), and
   \[
   |G_{K^{-1}}|\,d\mathrm{vol}=O\bigl(e^{-(\sqrt{13}-2)r}\bigr)dr .
   \]
   Integrating (2.1) against the flux normalization gives the exact identity
   \(\int\tanh^2r\,G_{K^{-1}}=1/9\) (numerically \(0.1111111110\)), so \(\|G_{K^{-1}}\|_{L^1}\ge1/9\); numerically
   \(\|G_{K^{-1}}\|_{L^1}=0.21490\).
4. *Gradient.* Away from the pole, interior estimates for the homogeneous equation bound
   \(|\nabla G|\) by \(\sup_{B(x,1/2)}|G|\); near the pole \(|\nabla G|\sim r^{-3}\). Hence \(\nabla G\in L^1\)
   (radial part \(\int|f'|\approx1.452\); the covariant derivative satisfies \(|\nabla(fe)|\le|f'|+3\tanh r\,f\)).

### 2.3 The one-form block (not Laplace type)

From \(B_1=\Delta_1+6\) on exact and \(\tfrac12(\Delta_1+12)\) on coexact forms, and
\(\Delta_1+12=\nabla^*\nabla+6\) (Bochner, \(\operatorname{Ric}=-6\)),
\[
B_1^{-1}=2(\nabla^*\nabla+6)^{-1}-\tfrac16\,d\bigl[(\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}\bigr]d^* .
\tag{2.2}
\]
(Check on an exact mode of eigenvalue \(x\): \(\tfrac2{x+12}-\tfrac{x}{(x+6)(x+12)}=\tfrac1{x+6}\); harmonic one-forms on a
compact quotient get \(\tfrac16\), consistent with \(B_1=6\) there.) The first term is Kato-dominated by
\(2G_6\), norm \(\le\tfrac13\). The second term has kernel \(\tfrac16 d_xd_y h(r(x,y))\), \(h=G_6-G_{12}\), and
\[
d_xd_yh=h''\,dr_x\otimes dr_y+h'\,\nabla_x\nabla_yr,
\]
where the mixed Hessian of the distance on \(\mathbb{CH}^2\) is \(0\) along the geodesic, \(-2/\sinh2r\) in the
\(J\gamma'\) direction and \(-1/\sinh r\) on the orthogonal 2-plane (Jacobi fields of curvature \(-4\), \(-1\)).
Its operator norm is \(\max(|h''|,|h'|/\sinh r)\). Locally the \(r^{-2}\) singularities cancel:
\(h'\sim(6-12)/(8\pi^2r)\), checked numerically (\(rh'=-0.07599\) vs \(-6/8\pi^2=-0.075991\)); so the kernel is
\(O(r^{-2})\), integrable in dimension four. At infinity it decays like \(e^{-(2+\sqrt{10})r}\). Numerically
\[
I_{dd}=\int\max(|h''|,|h'|/\sinh r)\,d\mathrm{vol}=2.0738,\qquad
\|B_1^{-1}\|_{\infty\to\infty}\le\tfrac13+\tfrac{2.0738}6=0.6790 .
\]
The exponents agree with Carron–Pedon (exact \(s_e=\sqrt{10}\), coexact \(s_c=\sqrt{13}\)), but the bound above uses
only Kato domination and scalar radial ODEs.

### 2.4 Quotients

The universal kernels are \(L^1\), so periodization converges absolutely and
\(\sup_x\int_{X_\Gamma}|K_\Gamma(x,y)|dy\le\|K\|_{L^1(\mathbb{CH}^2)}\). On compact \(X_\Gamma\), \(N\ge c>0\) in \(L^2\)
(Step 44 (G4); \(\nabla^*\nabla_{K^{-1}}\ge12\) by the integrated Kodaira identity), so the periodized kernel is the
inverse. Derivative kernels are handled by §2.2(4) and the same interior estimate applied to each block.
Interior Schauder estimates on unit balls of the universal cover then give
\[
\|u\|_{C^{2,\alpha}_b}\le C\|Nu\|_{C^{0,\alpha}_b},\qquad
\|v\|_{C^{1,\alpha}_b}\le C\|\mathcal Lv\|_{C^{0,\alpha}_b},
\tag{2.3}
\]
where \(\|T\|_{C^{k,\alpha}_b}:=\sup_{\tilde x}\|\pi^*T\|_{C^{k,\alpha}(B(\tilde x,1))}\) is measured on the universal cover (no injectivity
radius enters). For the second estimate, \(\mathcal L\) is elliptic of index zero (expected dimension of the
canonical class is \(0\)) and injective, hence surjective, and \(\mathcal L^{-1}=N^{-1}\mathcal L^*\) has an \(L^1\)
derivative kernel. ∎

---

## 3. Theorem \(A_C\)

**Theorem \(A_C\) (extensive perturbative torsion quotient).** There are \(\varepsilon_0,C>0\) depending only on
\(\mathbb{CH}^2\) such that the following holds on every compact ball quotient \(X_\Gamma\), in particular along every
tower of finite covers. Let \(g\) be a metric on \(X_\Gamma\) with
\[
\|c\,\phi^*g-g_\Gamma\|_{C^{2,\alpha}_b}\le\varepsilon\le\varepsilon_0
\]
for some diffeomorphism \(\phi\) and constant \(c>0\). Let \(\hat g\) be its scalar-normalized Yamabe representative.
Then the Seiberg–Witten equations of the canonical class for \(\hat g\) have a unique solution, modulo
gauge, within \(C^{1,\alpha}_b\)-distance \(C\varepsilon_0\) of \((A_0,\Phi_0)\) (the *canonical branch*). Its direction \(n\)
satisfies
\[
\int|\nabla n|^2\le C\,P(\hat g)\le C\,P(g),\qquad\text{hence}\qquad R_{\rm can}(\hat g)\le C'P(g),
\]
with \(R_{\rm can}=\int\rho^2|\nabla n|^2_{W_2}\) in the Theorem-N normalization. The hypothesis may be imposed on any metric conformal to
\(g\). Absolute \(H^s\)-smallness, \(s\ge5\), of \(c\phi^*g-g_\Gamma\) for one global scale \(c\), together with an injectivity-radius bound, implies it
(\(H^5\subset C^{2,\alpha}\) in dimension four). Smallness only of \(\|k\|+\|df\|\) in a conformal parametrization does not imply it, because slow
conformal drift can have small \(df\) and order-one oscillation on large covers. Step 44's \(H^2\) version is withdrawn
(\(H^2\not\subset L^\infty\) in dimension four).

*Proof.* Rescale so that \(c=1\) and replace \(g\) by \(\phi^*g\); \(P\) and \(R\) are invariant.

1. *Yamabe normalization.* \(\hat g=u^2g\), \(6\Delta_gu+s_gu+24u^3=0\). At \(g_\Gamma,u=1\) the linearization is
   \(6(\Delta_0+8)\), Kato-invertible with \(\|\cdot\|_{\infty\to\infty}\le1/48\). The implicit function theorem in
   \(C^{2,\alpha}_b\), with the map \(C^1\) in \((g,u)\) and constants from (2.3), gives \(\|u-1\|_{C^{2,\alpha}_b}\le C\varepsilon\). By
   uniqueness of constant-scalar-curvature metrics in a conformal class of negative Yamabe invariant this is
   the Yamabe representative, and \(P(g)\ge P(\hat g)\).
2. *DeTurck gauge.* Solve for a harmonic map \(\Psi:(X_\Gamma,\hat g)\to(X_\Gamma,g_\Gamma)\) near the identity. Its tension
   field depends on \(\hat g\) through \(\partial\hat g\) only, so it is a \(C^1\) map \(C^{2,\alpha}_b\to C^{0,\alpha}_b\) without
   loss of derivatives, and its linearization at the identity is the Jacobi operator
   \(\nabla^*\nabla-\operatorname{Ric}=\nabla^*\nabla+6\), Kato-invertible. Hence \(\|\Psi-\mathrm{id}\|_{C^{2,\alpha}_b}\le C\varepsilon\), and
   \(g':=(\Psi^{-1})^*\hat g=g_\Gamma+h\) satisfies the nonlinear DeTurck gauge \(g'^{ij}(\Gamma(g')-\Gamma(g_\Gamma))^k_{ij}=0\), i.e.
   \(\beta_{g_\Gamma}(h)=O(h\nabla h)\) (not exact linear Bianchi gauge), with
   \(\|h\|_{C^{1,\alpha}_b}\le C\varepsilon\). The DeTurck–Ricci equation is elliptic in \(h\) with right side
   \((\Psi^{-1})^*(\operatorname{Ric}(\hat g)+6\hat g)\), small in \(C^{0,\alpha}_b\); Schauder gives \(\|h\|_{C^{2,\alpha}_b}\le C\varepsilon\).
3. *Exact trace-free identity.* Since \(s(g')=-24=4\lambda\), \(\operatorname{tr}_{g'}(\operatorname{Ric}-\lambda g')=0\), so
   \(\operatorname{Ric}^\circ(g')=\operatorname{Ric}(g')-\lambda g'\) **exactly**. In DeTurck gauge (the \(\delta^*\beta h\) term is quadratic and is absorbed into \(Q\))
   \[
   \operatorname{Ric}(g')-\lambda g'=\tfrac12(\nabla^*\nabla-2\mathring R)h+Q(h),\qquad
   |Q(h)|\le C(|h||\nabla^2h|+|\nabla h|^2+|h|^2)\le C\varepsilon(|h|+|\nabla h|+|\nabla^2h|)
   \]
   pointwise.
4. *\(L^2\) coercivity (quotient-independent).* Decompose \(h=k+\delta^*X+fg_\Gamma\) in \(L^2\) (York; \(k\) TT). The scalar constraint
   \(s(g')=-24\) linearizes to \(3\Delta f+24f=O(\varepsilon(|h|+|\nabla h|+|\nabla^2h|))\), so
   \(\|f\|_{H^2}\le C\varepsilon\|h\|_{H^2}\); the gauge condition gives \(\tfrac12(\nabla^*\nabla+6)X=-df+O(h\nabla h)\), so
   \(\|X\|_{H^3}\le C\varepsilon\|h\|_{H^2}\). Hence \(\|h-k\|_{H^2}\le C\varepsilon\|h\|_{H^2}\) and \(\|h\|_{H^2}\le2\|k\|_{H^2}\) for small \(\varepsilon\) (no use of \(P\);
   noncircular). \(L_E=\nabla^*\nabla-2\mathring R\) does **not** annihilate \(\delta^*X\) (diffeomorphism invariance concerns the ungauged
   linearization \(\tfrac12L_E-\delta^*\beta\)); one uses instead \(\|L_E(h-k)\|\le C\|h-k\|_{H^2}\le C\varepsilon\|h\|_{H^2}\). The Koiso Bochner
   identity of Step 44 (G1) gives \(\langle(\nabla^*\nabla-2\mathring R)k,k\rangle\ge2\|k\|^2\) on TT tensors, and integration by parts on
   the locally symmetric quotient upgrades this to \(\|(\nabla^*\nabla-2\mathring R)k\|\ge\kappa\|k\|_{H^2}\). Therefore
   \[
   P(\hat g)^{1/2}=\|\operatorname{Ric}(g')-\lambda g'\|_{L^2}\ge\tfrac\kappa2\|k\|_{H^2}-C\varepsilon\|h\|_{H^2}\ge(\tfrac\kappa4-C\varepsilon)\|h\|_{H^2}\ge\tfrac\kappa8\|h\|_{H^2}
   \]
   All constants are pointwise/model constants. (Step 44's conformal channel (G2) is not needed: for the
   scalar-normalized representative the conformal part of \(h\) is quadratically small.)
5. *Canonical branch.* Identify spinor bundles of \(g'\) and \(g_\Gamma\) (Bourguignon–Gauduchon), and solve
   \(F(v)=0\), \(v=(a,\psi)\), \(F(v)=\bigl(\text{gauge},\ F^+_{g'}(A_0+a)-\sigma_{g'}(\Phi_0+\psi),\ D_{g',A_0+a}(\Phi_0+\psi)\bigr)\).
   Then \(F(0)=O(|h|+|\nabla h|)\) pointwise, \(\|DF(0)-\mathcal L\|_{C^{1,\alpha}\to C^{0,\alpha}}\le C\varepsilon\), and the nonlinearity
   \((-\sigma(\psi,\psi),\tfrac12a\cdot\psi)\) is bilinear. With (2.3), the contraction mapping principle in
   \(C^{1,\alpha}_b\) gives the unique branch with \(\|v\|_{C^{1,\alpha}_b}\le C\varepsilon\). Uniqueness modulo gauge uses the uniformly local
   Coulomb slice, whose scalar operator is the positive block \(\Delta_0+6\) (Kato-invertible), so it is quotient-uniform.
6. *Torsion bound.* In \(L^2\), \(\mathcal Lv=-F(0)-(DF(0)-\mathcal L)v-q(v)\), and Step 44's quotient-independent gap
   \(\|\mathcal Lv\|^2\ge\tfrac12\|\nabla v\|^2+\tfrac{|\lambda|}2\|v\|^2\) gives \(\|v\|_{H^1}\le C\|h\|_{H^1}+C\varepsilon\|v\|_{H^1}\), i.e.
   \(\|v\|_{H^1}\le C\|h\|_{H^1}\). Since \(n\) is parallel at \(g_\Gamma\) and \(|\Phi|\ge\tfrac12|\Phi_0|\),
   \(|\nabla^{g'}n|\le C(|\nabla v|+|v|+|\nabla h|)\) pointwise. So
   \(\int|\nabla n|^2\le C\|h\|_{H^1}^2\le C\|h\|_{H^2}^2\le C P(\hat g)\). ∎

**What \(A_C\) establishes.** In the extensive neighbourhood — uniformly local \(C^{2,\alpha}\)-closeness to a
complex-hyperbolic metric, with no smallness of total size — the canonical monopole branch cannot carry
Nijenhuis rotation cheaper than \(P/C'\), uniformly along every cover tower. The formal common mode needs
\(R\sim\sqrt{PA}\) with \(P\ll A\) (Step 43); it is therefore excluded from this neighbourhood **for the canonical
branch**. This repairs the phrase of message #809: "far from every KE metric in most of the volume" is now
proved in the uniformly local sense for the canonical branch, and only for it.

**What it does not establish.** (a) Branch selection: on large covers a metric \(\varepsilon_0\)-close to \(g_\Gamma\) may
carry other solutions of the canonical class with localized depletion; compactness of the SW moduli
space is not uniform in the cover. Theorem N applies to every solution; \(A_C\) only to the canonical one.
On \(X_\Gamma\#k\overline{\mathbb{CP}}^2\) the sign-family solutions are not the canonical branch on the host bulk unless proved.
(b) Localization: on a blow-up no metric is globally in the neighbourhood; a local version carries the
outer-layer term \(\int_{\Omega'\setminus\Omega}|h|^2\) (local Einstein deformations of \(\mathbb{CH}^2\) exist) and the
core/collar action. (c) It is not a tariff.

---

## 4. Theorem K, and the three-regime statement with exact status

Theorem K (Step 45, exact constant proved by the TTCS integration): under the all-metric sign-family hypotheses
of Theorems N/W, for the scalar-\(-4\) Yamabe representative \(\hat g\),
\[
8\pi^2k-P(g)\le8\pi^2k-P(\hat g)\le\tfrac{4\sqrt6}{3}\int\operatorname{dist}(W^+_{\hat g},\mathcal K)\,d\mu_{\hat g},
\]
so \(P(g)\le8\pi^2ck\) forces \(\int\operatorname{dist}(W^+_{\hat g},\mathcal K)\ge\sqrt6\pi^2(1-c)k\), which is
\(\ge0.10485\,k\) for the certified cell coefficient (exact range \(0.1048555811\)–\(0.1048555815\)).

**Proposition 46.T (three regimes; status of each).** Let \(g_j\) be metrics on \(X\#k_j\overline{\mathbb{CP}}^2\) with
\(P(g_j)\le8\pi^2ck_j\), \(c<1\), under the sign-family hypotheses. Then the sign-averaged Nijenhuis energy satisfies
\(R\ge16\pi^2(1-c)k\) (Theorem N) and the Weyl departure satisfies Theorem K. The saving must be carried by one or
more of the following, and the current mathematics prices each as stated:

1. *Diffuse rotation of the canonical branch in a uniformly CH region.* Priced: \(R\le C'P\) on any closed
   quotient in the \(\varepsilon_0\)-neighbourhood (Theorem \(A_C\), proved). On a blow-up the local form is open
   (outer layer, collar).
2. *Concentrated almost-Kähler torsion, \(s^*=s+|\nabla\omega|^2\ge0\).* Priced per unit volume by Proposition \(\Pi\)
   through AK\(\Gamma\) (proved), but pockets may shrink; Theorem F's aligned Burns saving is \(O(x_0)\) per sphere, so
   only nonperturbative aligned cells could lower \(c\) substantially. This is a construction target, not a
   prediction.
3. *Intermediate torsion \(|\nabla\omega|^2\sim|s|\), noncanonical fields (depletion/vortices), or harmonic-form zero
   sets and collars.* Not priced. Kirchberg's identity retains the Cotton pairing, and the quadratic law
   \(P\gtrsim R^2/A\) is conditional on noncircular control of \(E=W^+-W_0\) and \(\nabla a\). Every subunit family must
   place its \(\sqrt6\pi^2(1-c)k\) of Weyl departure and its \(16\pi^2(1-c)k\) of rotation somewhere in regimes
   2–3 or in the cores; the certified cells do so in cores whose closed form vanishes on the bolt.

This is a classification of where the saving may sit, with one regime closed, one priced but escapable by
shrinking, and one open; it is not an exhaustive theorem about arbitrary monopoles, because the regimes are
defined through the metric and an almost-Kähler representative while Theorems N/K concern the actual
fields.

---

## 5. What changed

- Lemma M is proved without the hand-entered calibration: the Landau ground state \(\cosh^{-3}r\) is explicit,
  the potential \(9\tanh^2r\) fixes the threshold \(13\), and all four blocks have explicit
  \(L^\infty\) inverse norms (\(0.679,\ 1/12,\ 1/6,\ 0.215\) in hol. \(-4\) units).
- The connection sector does not break Lemma M; its operator is \(dd^*+\tfrac12d^*d+6\), and even a halved mass
  would leave decay \(2+\sqrt7>4\).
- \(A_C\) is proved for the canonical branch by a uniformly local IFT whose only non-pointwise input is
  Lemma M. Scalar normalization removes the conformal channel from the coercivity proof.
- The open perturbative problems are now precisely branch selection and localization on blow-ups;
  the open nonperturbative problem is regime 3.

---

## 6. The almost-Kähler representative is the wrong conformal gauge (A01 #812)

A01 (#812, `Sessions/S1003A01/workspace/notes/step40_harmonic_class_compatibility_and_period_stiffness.md`)
rotates the certified cell's bolt circle and obtains strictly subthreshold cells whose canonical SD harmonic form \(\Omega\) is
nowhere zero, with small exceptional period \(t\ne0\) and cost \(J_*+O(\psi^2)\). Glued into ball-quotient hosts, these give
pure blow-ups with closed metrics \(g\) conformal to smooth almost-Kähler metrics \(\hat g_{AK}=u^2g\), \(u^2=|\Omega|_g/\sqrt2\).
Lemma T is then satisfied and imposes nothing.

**Proposition 46.V.** Model near the bolt \(E\) by \(|\Omega|=a|t|+b\rho^2\), where \(\rho\) is the transverse distance (this follows from A01's
SD bolt exponents \((0,2,2)\)). Then, as \(t\to0\),
\[
\int\hat s_{AK}^2\,d\mu_{AK}=\int\Bigl(6\frac{\Delta u}{u}+s\Bigr)^2d\mu\ \sim\ 84\pi\,\frac{b}{a}\,\frac{\operatorname{Area}(E)}{|t|},
\]
because \(\Delta_{\mathbb R^2}u/u=(\rho^2+2t')/(\rho^2+t')^2\) with \(t'=a|t|/b\) and \(\int_0(\Delta u/u)^2\rho\,d\rho=7/(6t')+O(1)\) (symbolic check).
By contrast \(\int\hat s\,d\mu_{AK}=\int(6|\nabla u|^2+su^2)d\mu\), \(\hat V\), \(\ell\) and \(\int|\nabla\omega|^2d\mu_{AK}\) (of order \(t^{-2}\cdot t^3\)) stay bounded.
In the AK\(\Gamma\) identity on \(\hat g_{AK}\) the divergence therefore sits entirely in the Cauchy–Schwarz (variance) defect of
\(\hat s\); \(\theta\) and \(\ell\) stay bounded. Since the Yamabe representative minimizes \(\int s^2d\mu\) in a negative conformal class,
\[
P(\hat g_{AK})-P(g_Y)=\tfrac1{12}\Bigl(\int\hat s_{AK}^2d\mu_{AK}-Y^2\Bigr)\sim\frac{C\,\operatorname{Area}(E)}{|t|}.
\]
The almost-Kähler representative pays an unbounded scalar tariff that the actual metric never pays. Its \(s^*\)-pocket has
volume \(O(t^3)\), which is exactly the shrinking-pocket escape of Proposition Π.

*Consequence.* No lower bound computed on an almost-Kähler representative (AK\(\Gamma\), Π, Armstrong-type Goldberg estimates)
transfers to \(P\) of the metric itself. It does so only if the conformal factor is controlled, and that factor is precisely what
degenerates as exceptional periods close. Coercive statements must be formulated on the Yamabe representative with the
actual monopole fields (Theorems N, W, K, B), or must be conformally invariant. This settles the role of the AK category in
the global problem: it records period information (Lemma T) but sits in a conformal gauge that can be made arbitrarily
expensive at no cost to \(P\).


---

## Step-47 correction to §6 (A01 Steps 41 / messages #814–#815)

The qualitative conclusion of §6 is unchanged, but its local model and divergence exponent are superseded.  In a smooth orthonormal bolt frame,
\[
f_p^2=|\Omega_p|^2/2=a^2p^2+\kappa^2r^2+O(p^2r^2+r^4),
\qquad \widehat g_{AK}=f_pg,
\]
because the zero-period form has an orthonormal component of order \(r\), not \(r^2\).  With \(v=\sqrt{f_p}\),
\[
\frac{\Delta v}{v}
=\frac{\kappa^2(4a^2p^2+\kappa^2r^2)}{4(a^2p^2+\kappa^2r^2)^2}+O(1),
\qquad
\int_0^\infty(\Delta v/v)^2r\,dr=\frac{7\kappa^2}{32a^2p^2}.
\]
Thus \(\int\widehat s^2d\mu_{AK}=C_Ep^{-2}+O(|\log|p||)\), not \(C/|p|\).  For the certified profile A01 obtains \(C_E=1.75135145\), with resolved values converging to it.  The earlier model \(|\Omega|=a|p|+br^2\), the \(7/(6p)\) calculation, and the \(p^{-1}\) rate in this note are withdrawn.  The retained conclusion is stronger: the almost-Kähler conformal representative develops a \(p^{-2}\) scalar-variance layer while the original smooth subthreshold metrics converge to the certified metric, so AK-gauge lower estimates do not transfer to the original \(P\) without the exact conformal conversion.

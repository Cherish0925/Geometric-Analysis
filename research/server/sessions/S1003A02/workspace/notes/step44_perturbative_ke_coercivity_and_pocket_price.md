# Step 44 — Cover-independent coercivity at complex-hyperbolic hosts, and the price of \(s^*>0\) pockets

Session S1003A02, Agent2. Data/script: `workspace/scripts/step44_perturbative_ke.py` →
`workspace/data/step44_perturbative_ke.json`. Normalization unless stated: scalar curvature
\(s=-4\), \(\operatorname{Ric}=\lambda g\) with \(\lambda=-1\) at the Kähler–Einstein (KE) host;
\(P=\int|\operatorname{Ric}^\circ|^2\) (scale invariant in dimension four).

The Step-43 handoff asked for (i) the perturbative negative-KE torsion theorem with an explicit
statement of whether its constant is cover-independent, and (ii) a pricing of the "tiny positive
exceptional area" branch of Lemma T. Both are answered below. The nonperturbative quadratic
Cotton law and the second-jet estimate are untouched and remain open.

---

## 1. Four pointwise gaps at a complex-hyperbolic surface

Let \(X_\Gamma=B^4/\Gamma\) be any compact quotient of the complex-hyperbolic ball (\(\Gamma\subset PU(2,1)\)
torsion free, cocompact), with its KE metric \(g_\Gamma\). Each operator entering the linearization
of \(P\) and of the canonical monopole has a Weitzenböck form \(\nabla^*\nabla+\mathcal V\) (or a
sum of such) whose potential is a fixed algebraic function of the curvature of \(\mathbb{CH}^2\).
Hence every lower bound below holds with the same constant on every \(X_\Gamma\), in particular
uniformly along every tower of finite covers. A Γ-dependent spectral gap never enters.

**(G1) Einstein operator on TT tensors (Koiso, computed).** For TT \(h\) on an Einstein manifold,
\(L_E h=\nabla^*\nabla h-2\mathring R h\) and the \(d^\nabla\) Bochner identity gives
\[
\langle L_Eh,h\rangle=\|d^\nabla h\|^2+\langle(-\lambda-\mathring R)h,h\rangle\ \ge\ (-\lambda-a)\|h\|^2,
\qquad a=\max\operatorname{spec}\mathring R|_{S^2_0}.
\]
Exact computation on \(\mathbb{CH}^2\) with holomorphic sectional curvature \(-4\) (\(\lambda=-6\),
sectional curvatures in \([-4,-1]\)): \(\mathring R=-2\) on the 3-dimensional \(J\)-invariant
trace-free tensors and \(\mathring R=+4\) on the 6-dimensional \(J\)-anti-invariant ones. Thus
\(a=4\) and the pointwise Koiso gap is \(-\lambda-a=2=|\lambda|/3\). (Control: real hyperbolic
\(K=-1\), \(n=4\): \(\mathring R\equiv1\), gap \(2\), the known rigid case.) On the \(J\)-invariant
sector the Hodge identification \(L_E\leftrightarrow\Delta_d-2\lambda\) on primitive (1,1)-forms
gives the larger gap \(2|\lambda|\). In the \(s=-4\) normalization:
\[
\langle L_Eh,h\rangle\ \ge\ \tfrac13\|h\|^2\qquad(h\ \text{TT}).
\]
So the infinitesimal Einstein rigidity of ball quotients (Calabi–Vesentini/Koiso) is, in real
dimension four, a pointwise Bochner statement; the \(J\)-anti-invariant sector, which carries
complex-structure deformations, is the binding one with margin \(|\lambda|/3\).

**(G2) Conformal channel.** \(\operatorname{Ric}^\circ(e^{2f}\hat g)=\operatorname{Ric}^\circ(\hat g)
-2(\hat\nabla^2f-df\otimes df)^\circ\), and on an Einstein background with \(\lambda<0\)
\[
\|(\nabla^2f)^\circ\|^2=\tfrac34\|\Delta f\|^2+|\lambda|\,\|\nabla f\|^2 ,
\]
which controls \(\|df\|_{H^1}^2\) (not \(\|f-\bar f\|^2\), which is not needed: \(P\) and the monopole
direction depend on \(f\) only through \(df\), see §2).

**(G3) Gauge.** The conformal Killing operator satisfies
\(\|(L_Xg)^\circ\|^2=2\|\nabla X\|^2+2(1-\tfrac2n)\|\operatorname{div}X\|^2+2|\lambda|\|X\|^2\ge2|\lambda|\|X\|^2\),
so the York decomposition \(h=h_{TT}+L_Xg+fg\) and the Ebin slice have uniformly bounded inverses.

**(G4) Linearized Seiberg–Witten operator at the canonical Kähler solution.** At a KE surface
the canonical solution \((A_0,\Phi_0)\) of the class \(K\) has \(\nabla_{A_0}\Phi_0=0\),
\(|\Phi_0|^2=-s\), \(c(F^+_{A_0})=(\Phi_0\Phi_0^*)_0\). With the gauge-fixed linearization
\[
\mathcal L(a,\psi)=\Bigl(d^*a-\tfrac12\,i\operatorname{Im}\langle\Phi_0,\psi\rangle,\ d^+a-\sigma'(\psi),\ D_{A_0}\psi+\tfrac12a\cdot\Phi_0\Bigr),
\]
the Clifford-model computation verifies: (i) all first-order cross terms in \(\|\mathcal L(a,\psi)\|^2\)
cancel identically at the symbol level (mismatch \(2\times10^{-16}\); every other sign/gauge
coefficient tested fails), so they vanish exactly when \(\nabla\Phi_0=0\); (ii) the zeroth-order
potential at \(s=-4\) has eigenvalues \(\tfrac12\) (four, on \(a\): \(\lambda/2+|\Phi_0|^2/4\)),
\(2\) (real part of \(\psi\parallel\Phi_0\)), \(1\) (gauge direction), and \(0,0\) on
\(\psi_\perp\in\Phi_0^\perp\cong\Lambda^{0,2}\cong K^{-1}\). The two zero eigenvalues are lifted
by the Kodaira/Landau identity \(\nabla^*\nabla=2\bar\partial^*\bar\partial+i\Lambda F=2\partial^*\partial-i\Lambda F\)
on the parallel line subbundle \(\Phi_0^\perp\), whose curvature \(\mp i\lambda\omega\) has constant
\(|i\Lambda F|=2|\lambda|\). Therefore
\[
\|\mathcal L(a,\psi)\|^2\ \ge\ \tfrac12\|\nabla a\|^2+\tfrac12\|\nabla\psi\|^2+\tfrac{|\lambda|}2\|(a,\psi)\|^2 ,
\]
a cover-independent \(L^2\) gap \(|\lambda|/2\). Half of the \(\psi_\perp\) gradient is spent on the Landau
mass; the first draft kept the full \(\|\nabla\psi\|^2\), which double-counts (TTCS correction). The 1-form
part uses \(\|d^*a\|^2+\|d^+a\|^2=\tfrac12\langle\Delta_da,a\rangle+\tfrac12\|d^*a\|^2\); only a nonnegative term is
dropped. *Normalization.* Here \(|\Phi_0|^2=4\) at \(s=-4\); Theorem N uses \(\rho=|\Phi|^2/2\in[0,2]\). The direction
\(n\) is the same, but constants in \(\rho^2|\nabla n|^2\) must be converted by the factor \(4\).

*Which topology is cover-uniform.* (G1)–(G4) are \(L^2\) gaps. Since \(X_\Gamma\) is locally symmetric
(\(\nabla\mathrm{Rm}=0\)), global \(H^2\) bounds follow from them by integration by parts, with model constants.
The local Sobolev embedding \(\|v\|_{L^\infty}\le C(i_0)\|v\|_{H^2}\) depends only on a lower bound \(i_0\) for the
injectivity radius, and \(i_0\) is inherited by every finite cover. Hence an implicit-function
argument in **global** Sobolev spaces has constants depending only on \(\mathbb{CH}^2\) and \(i_0\).
An \(L^2\) gap does **not** by itself give \(\Gamma\)-uniform \(L^\infty\)/Hölder inverses; the first draft's
appeal to lifting plus Agmon decay was insufficient. For sectors whose operator is
\(\nabla^*\nabla+\mathcal V\) with \(\mathcal V\ge\mu>0\) pointwise, Kato domination by \((\Delta+\mu)^{-1}\) gives
\(\|\cdot\|_{L^\infty\to L^\infty}\le1/\mu\) on every quotient. The \(\psi_\perp\) sector is \(\nabla^*\nabla\) on \(K^{-1}\), whose
gap is magnetic (Landau), not pointwise, and the 1-form sector is \(dd^*+\tfrac12d^*d+\text{mass}\), which is not
Laplace type. For these sectors a uniform \(L^\infty\) resolvent is the open **Lemma M**: the Green
kernels of these \(SU(2,1)\)-homogeneous operators on \(\mathbb{CH}^2\) at energy \(0\) are in \(L^1\). By
homogeneity this is a computable spherical-function question; the heuristic decay rate exceeds
the volume growth \(e^{4r}\) (holomorphic curvature \(-4\)) when the spectral bottom exceeds \(\rho_0^2=4\),
and the \(K^{-1}\) bottom is \(12\) there.

## 2. Theorem A (perturbative torsion quotient, cover independent)

> **Step-46 correction.** The global-Sobolev form below uses \(\|v\|_{L^\infty}\le C(i_0)\|v\|_{H^2}\), which is false in
> real dimension four (A01, #811). The nonlinear neighbourhood is therefore not established as stated. The
> correct theorem is the uniformly local form \(A_C\), proved in `step46_lemmaM_elementary_and_AC.md` §3
> (hypothesis \(\|c\phi^*g-g_\Gamma\|_{C^{2,\alpha}_b}\le\varepsilon_0\)). An absolute \(H^s\) neighbourhood with \(s\ge5\) plus an
> injectivity-radius bound implies that hypothesis, so \(A_H\) survives in that form. The linear gaps of §1 stand.

**Theorem A (global-Sobolev form \(A_H\)).** There are constants \(\varepsilon_0,\kappa,C>0\), depending only on
the geometry of \(\mathbb{CH}^2\) and a lower bound \(i_0\) for the injectivity radius (hence uniform along every
tower of finite covers of a fixed \(X\)), such that for every compact ball quotient \(X_\Gamma\) with
\(\operatorname{inj}\ge i_0\) and every metric \(g=\phi_*e^{2f}(g_\Gamma+k)\) (\(k\) TT) with
\(\|k\|_{H^2}+\|df\|_{H^1}\le\varepsilon_0\) (absolute, not per unit volume):

1. (quadratic Einstein gap) writing, after a diffeomorphism and scaling, \(g=e^{2f}(g_\Gamma+k)\)
   with \(k\) transverse-traceless,
   \[
   P(g)\ \ge\ \kappa\bigl(\|k\|_{H^2}^2+\|df\|_{H^1}^2\bigr);
   \]
2. (unique canonical branch) the Seiberg–Witten equations of the class \(K\) for \(g\) have a
   unique solution within \(C\varepsilon_0\) of the canonical Kähler solution (in the slice), and
   its almost-complex structure \(n_g\) satisfies
   \[
   \int|\nabla n_g|^2\ \le\ C\bigl(\|k\|_{H^1}^2+\|df\|_{L^2}^2\bigr)\ \le\ \tfrac C\kappa\,P(g);
   \]
3. hence for the Nijenhuis energy \(R(g)=\int\rho^2|\nabla n_g|^2_{W_2}\) of that branch (Theorem-N
   normalization, after the factor-4 conversion), \(R(g)\le C' P(g)\). The same holds for the scalar
   \(-4\) Yamabe representative \(\hat g\), which is \(C\varepsilon_0\)-close because \(6\Delta+8\) is uniformly invertible.
   This inequality is one-sided only (see the correction below).

*Proof.* (a) Slice. The Diff ⋉ Conf slice at \(g_\Gamma\) is constructed in global Sobolev spaces with
uniform constants by (G2)–(G3): the scalar \(-4\) normalization uses \(6\Delta+8\), Bianchi gauge uses
\(\nabla^*\nabla+|\lambda|\). (b) Expansion. \(\operatorname{Ric}^\circ(g_\Gamma+k)=\tfrac12L_Ek+Q_1(k)\) with
\(\|Q_1\|_{L^2}\le C\|k\|_{L^\infty\cap W^{1,4}}\|k\|_{H^2}\le C(i_0)\varepsilon_0\|k\|_{H^2}\); the conformal formula of (G2) is exact and
contains only \(df,\nabla^2f\). The \(TT\) and Hessian channels are \(L^2\)-orthogonal
(\(\int\langle L_Ek,\nabla^2u\rangle=\int\langle k,\nabla^2(\Delta-2\lambda)u\rangle=0\)). Hence
\(P\ge(1-\eta)\bigl(\tfrac14\|L_Ek\|^2+4\|(\nabla^2f)^\circ\|^2\bigr)-C_\eta\varepsilon_0^2(\|k\|^2_{H^2}+\|df\|^2_{H^1})\),
and (G1), (G2) with elliptic regularity give item 1 for \(\varepsilon_0\) small. (c) Monopole. Scale
covariance is exact: for constant \(c\), \(\Phi\mapsto e^{-c}\Phi\) maps solutions of \(g\) to those of
\(e^{2c}g\) and fixes \(n\). For \(\tilde g=e^{2f}\hat g\), the ansatz \(\tilde\Phi=e^{-f}\Phi_{\hat g}\)
solves the curvature equation exactly (\(F^+\) and \(\sigma\) are both conformally natural as
2-forms) and the Dirac equation up to \(\tfrac12 e^{-2f}df\cdot\Phi\). By (G4) and the implicit
function theorem in global \(H^2\) (quadratic terms controlled by \(\|v\|_{L^\infty}\le C(i_0)\|v\|_{H^2}\)), the true branch solution differs from the ansatz by \(O(\|df\|)\) and
from the Kähler solution by \(O(\|k\|_{H^1})\) through the \(k\)-dependence of the Levi-Civita and
spin connections. Since \(\nabla n=0\) at \(g_\Gamma\), \(\nabla n_g\) is bounded by these
differences, giving item 2. Item 3 follows. ∎

**Correction (TTCS).** The first draft also claimed \(2P\le R\) from Theorem N, and hence \(P\asymp R\). This is
false. At \(Q=0\), Theorem N reads \(-P=\tfrac12R-\mathcal E\) with \(\mathcal E\ge0\); this gives no lower bound for \(R\).
Near-KE cscK metrics in nearby Kähler classes (LeBrun–Simanca) have \(R=0<P\). Only the one-sided
\(R\le C'P\) holds: Nijenhuis energy detects nonintegrable rotation, not every Einstein defect.

**Hölder form \(A_C\) (conditional).** If Lemma M holds, the same conclusions hold for every \(g\) with
\(\inf\|\phi^*g-cg_\Gamma\|_{C^{2,\alpha}(\text{unit balls})}\le\varepsilon_0\), which is the extensive neighbourhood relevant to
diffuse modes. Without Lemma M, item 1 is still expected in that neighbourhood with a universal
\(\kappa\). In Bianchi gauge the slice uses only \(\nabla^*\nabla+|\lambda|\) and \(6\Delta+8\), both with pointwise-positive
potentials and hence uniform \(L^\infty\) inverses by Kato domination, and the rest needs only \(L^2\) gaps and
pointwise-small cubic terms. Item 2 then holds with \(\Gamma\)-dependent constants.

**What Theorem A establishes and what it does not.** It is the perturbative Goldberg statement
with constants uniform along cover towers: diffuse almost-complex rotation costs linearly in \(P\)
near every compact complex-hyperbolic host. In global Sobolev form this is proved; in the
extensive Hölder form it is conditional on Lemma M. The formal common mode needs \(R\sim\sqrt{PA}\)
(Step 43), while Theorem A forces \(R\le C'P\); hence a common mode with \(P\ll A\) cannot sit in the relevant
neighbourhood of a KE host. The binding coercivity input is the pointwise \(J\)-anti-invariant Koiso
margin \(|\lambda|/3\).

It is not the tariff. On \(M=X_\Gamma\#k\overline{\mathbb{CP}}^2\) no metric is globally
\(C^2\)-close to the host. The localized version, "if \(g\) is \(\varepsilon_0\)-close to \(g_\Gamma\) on a
bulk domain \(\Omega\), then the bulk Nijenhuis energy is \(\le C\,P\) on a slightly larger domain,"
needs two further inputs that are **not** proved:

- *Bulk selection.* An actual solution on \(M\) for each sign class must be close to the canonical
  solution on \(\Omega\). The \(L^2\) bound \(\int(|\Phi|^2+s)^2\le\int s^2-32\pi^2c_1^2\) coming from
  the Weitzenböck formula is extensive. It allows localized depletion of unit size anywhere in a
  large bulk, which is exactly what the Step-39 depletion law requires of a subunit
  near-minimizer. So bulk-closeness of the field is not implied by bulk-closeness of the metric.
- *Lower-order outer layer.* Locally, Einstein deformations of \(\mathbb{CH}^2\) exist, so a local
  coercive estimate always carries a term \(\int_{\Omega'\setminus\Omega}|k|^2\). It is not controlled
  by \(P\) without global input.

The correct structural reading is therefore: *every subunit near-minimizer has, in each region
where it is \(C^{2,\alpha}\)-close to a complex-hyperbolic metric, either a monopole far from the
canonical one there (depletion/vortex) or negligible Nijenhuis saving there.* The saving must be
financed either away from KE geometry or by field depletion, which is the Step-39 channel.

## 3. Proposition Π (price of \(s^*\ge0\) pockets in the almost-Kähler profile)

In an almost-Kähler 4-manifold, \(W^+(\hat\omega,\hat\omega)=s/6+|\nabla\omega|^2/4\), so
\(\mathbb R^+(\hat\omega,\hat\omega)=W^+(\hat\omega,\hat\omega)+s/12=s^*/4\) with
\(s^*=s+|\nabla\omega|^2\). By Theorem F, a Burns insertion of parameter \(x_0\) whose exceptional
sphere is aligned with \(\omega\) (small *positive* symplectic area) changes \(P\) by
\(8\pi^2(1-x_0s^*(p)/4)+O(x_0^{6/5})\). It saves at first order exactly where \(s^*>0\), i.e. where
the torsion density \(\delta=|\nabla\omega|^2\) exceeds \(\sigma=-s\).

**Proposition Π.** Let \((M,g,\omega)\) be a closed almost-Kähler 4-manifold, \(V\) its volume,
\(\ell=8\pi K_\omega\cdot[\omega]>0\), \(\theta=\int|\nabla\omega|^2/\ell\), and
\(\varphi=\operatorname{Vol}\{s^*\ge0\}/V\in[0,1)\). Then
\[
C_+\ \ge\ \frac{\ell^2}{128\pi^2V}\Bigl[\Gamma(\theta)+\frac{\varphi}{1-\varphi}(1-\theta)_+^2\Bigr]
\ \ge\ \frac{\ell^2}{128\pi^2V}\cdot\frac{2}{3-2\varphi},
\]
the last minimum attained at \(\theta=1/(3-2\varphi)\). At \(\varphi=0\) this is AKΓ (minimum \(2/3\));
\(\varphi=1/2\) already forces the Kähler constant \(1\).

*Proof.* AKΓ's pointwise step gives \(C_+\ge\int G(\sigma,\delta)\) with the convex quadratic
\(G=[2\sigma^2+(3\delta-2\sigma)^2]/192\pi^2\). Split \(M\) into the pocket \(\Omega_+=\{\delta\ge\sigma\}\) and
its complement. Jensen within each region reduces to constants \(v_1\in\{\delta\ge\sigma\}\), \(v_2\)
with \(\varphi v_1+(1-\varphi)v_2=\bar v\). Writing \(v_1=\bar v+(1-\varphi)u\), \(v_2=\bar v-\varphi u\), the
mixed terms cancel and \(\varphi G(v_1)+(1-\varphi)G(v_2)=G(\bar v)+\varphi(1-\varphi)G(u)\). The
constraint is \(u_\delta-u_\sigma\ge(\bar\sigma-\bar\delta)/(1-\varphi)\). The minimum of
\(2x^2+(3y-2x)^2\) on \(y-x=D\) is \(6D^2\) (symbolic). Blair fixes \(\ell=V(2\bar\sigma-\bar\delta)\), so
\(\bar\sigma-\bar\delta=\tfrac{\ell}{2V}(1-\theta)\), and \(VG(\bar v)=\ell^2\Gamma(\theta)/(128\pi^2V)\) (Step 42). The
optimization in \(\theta\) is elementary. A brute-force two-region search reproduces the formula
(e.g. \(38.684\) sampled vs \(38.667\) exact at \(\varphi=.1\)). ∎

**Consequences for the tiny-area branch of Lemma T.**
(a) Uniform \(s^*>0\) is prohibitively expensive (\(\theta\ge1\), \(\Gamma\ge2\)). First-order savings
must be localized in pockets.
(b) Per sphere, the Theorem-F saving is linear in \(x_0\), while a pocket of radius \(r\gg\sqrt{x_0}\)
costs \(O(r^4)\) in the convex profile. So convexity does **not** exclude the pocket route at small
\(x_0\). What limits it is the perturbative range of Theorem F, which delivers only \(c=1-O(x_0)\).
Driving \(c\) far below one through aligned tiny-area spheres needs nonperturbative cells, which
is the regime of the certified perpendicular cell, but with the opposite (aligned) orientation.
(c) Theorem A makes pockets incompatible with KE-closeness: \(\delta\ge\sigma=4\) on a pocket forces
\(\int|\nabla n|^2\ge4\operatorname{Vol}(\Omega_+)\), while near a host \(\int|\nabla n|^2\le CP\). In the
regime \(P\ll\operatorname{Vol}\) the pockets therefore live in regions far from KE geometry.
(d) Scope. Π is an almost-Kähler (\(\ell\)-form) statement. Converting \(\ell\) to \(A\) needs the
Lorentzian hypothesis \(H_L\). Under \(H_L\) (with \(\eta+\alpha\ge1\)) it gives \(P/8\pi^2\ge k-A(1-2\varphi)/(3-2\varphi)\). This
improves LeBrun's threshold linearly, by \(\tfrac49A\varphi+O(\varphi^2)\), for every \(\varphi>0\). Π does not see the monopole field, and the given
almost-Kähler form need not coincide with the monopole direction of Theorem A.
(e) Threshold pockets. The relaxed optimizer places the pocket mean at \(s^*=0\), where the Burns
saving vanishes. For pockets with \(s^*\ge s_0>0\) the same calculation gives
\(C_+\ge\frac{\ell^2}{128\pi^2V}\bigl[\Gamma(\theta)+\frac{\varphi}{1-\varphi}\bigl(1-\theta+\frac{2Vs_0}{\ell}\bigr)_+^2\bigr]\).

## 4. Updated global picture

- **Perturbative regime: settled in global Sobolev form, open in Hölder form.** The defect is
  quadratically coercive modulo Diff ⋉ scaling with a universal constant, which comes from the
  pointwise Koiso margin \(|\lambda|/3\) of the \(J\)-anti-invariant sector. Diffuse rotation is priced linearly,
  \(R\le C'P\), with constants uniform along cover towers in the absolute \(H^2\) neighbourhood. In the
  extensive Hölder neighbourhood the same holds once Lemma M is proved. There is no reverse inequality.
- **Unconditional global input (Theorem N).** A subunit sequence \(P\le8\pi^2ck\) on a pure blow-up has
  total \(W_2\)-energy \(R_{\rm tot}\ge16\pi^2(1-c)k\). Theorem A says that this rotation cannot sit in absolute-\(H^2\)-near-KE
  geometry. A localized estimate would push it into non-host-like regions, noncanonical-field
  regions, or collars.
- **TTCS-proposed pointwise lemma (to verify).** At exactly Kähler-type scalar \(-4\) self-dual Weyl
  \(W_*=\tfrac13I-\hat\omega\otimes\hat\omega\), the Theorem-W saving density would be \(\le-(2-\rho)^2(\rho+1)\) for every amplitude
  and direction, with linear error \(C|E|\) off the orbit. If this holds, substantial saving needs substantial
  integrated departure of \(W^+\) from the Kähler orbit, independently of any field selection. This
  has not yet been checked against the Theorem-W formula in `step40_nijenhuis_form_and_pointwise_exhaustion.md`.
- **Nonperturbative regime: open.** It is still governed by the conditional quadratic law
  \(P\gtrsim R^2/A\) (Step 43), whose missing inputs are the second-jet/Cotton estimate and the
  noncircular control of \(E=W^+-W_0\) and \(\nabla a\). Theorem A supplies the linear
  complement: the two regimes join only if one proves that a near-minimizer which is far from KE
  everywhere still pays (a quantitative non-Kähler–Einstein bulk statement). That is the true
  remaining global question for diffuse modes.
- **Construction side (for A01).** Any \(c\to0\) family must be, in most of its volume, outside the
  \(\varepsilon_0\)-neighbourhood of every KE metric (Theorem A), or have bulk monopoles away from
  canonical (depletion). Aligned tiny-area exceptional spheres need \(s^*>0\) pockets priced by Π;
  the perpendicular/null-period alternative needs the closed form to vanish on the spheres (Lemma T).

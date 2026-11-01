# Step 45 — The extensive complex-hyperbolic branch and exact Weyl-orbit departure

Session S1003A02, Agent3. Script/data:
`workspace/scripts/step45_resolvent_and_weyl_departure.py` →
`workspace/data/step45_resolvent_and_weyl_departure.json`.

The Step-44 note established the cover-independent perturbative theorem in an absolute global Sobolev neighborhood and left two questions: the uniformly local/extensive version (Lemma M), and the pointwise Kähler-orbit bound suggested by the verifier. This note settles the homogeneous kernel calculation needed by Lemma M and proves the pointwise bound with its sharp first-order coefficient. The later nonlinear theorem still has the local slice/patching work recorded below; no blow-up tariff is inferred.

Throughout §§1–2 the model is complex hyperbolic two-space with holomorphic sectional curvature \(-4\), so \(\operatorname{Ric}=-6g\). The half volume-growth exponent is \(\rho_0=2\): geodesic-shell volume is \(\asymp e^{4r}\). At the end one rescales to the scalar-\(-4\) convention of Theorems N/W.

---

## 1. Lemma M for the homogeneous line sector

The difficult zero-potential spinor block of the gauge-fixed canonical SW linearization is the Chern/Bochner Laplacian on
\[
K^{-1}\cong\Lambda^{0,2}.
\]
On \(\mathbb{CH}^n=SU(n,1)/S(U(n)U(1))\), the anticanonical bundle is the homogeneous line bundle of character \(|l|=n+1\); in complex dimension two, \(|l|=3\). In Will's convention the radial Casimir kernel has parameter \(\nu\), decay
\[
Q_{\nu,l}(r)\sim e^{-(\nu+\rho_0)r},
\]
and it is \(L^1\) precisely once \(\Re\nu>\rho_0\) (the source proves the sufficient implication and the asymptotic makes necessity immediate). The lowest discrete-series parameter is
\[
\nu_d=|l|-n=1.
\]

The Step-44 Kodaira/Landau calculation gives the bottom of the positive Bochner Laplacian on \(K^{-1}\):
\[
\inf\operatorname{spec}_{L^2}(\nabla^*\nabla)=2|\lambda|=12
\quad(\lambda=-6).
\]
Because the homogeneous line-bundle Laplacian is an affine function of the Casimir and Will's eigenvalue depends affinely on \(-\nu^2\), calibration at the lowest discrete-series state gives
\[
H_{K^{-1}}(\nu)=12+\nu_d^2-\nu^2=13-\nu^2.
\]
Hence the zero-energy Green kernel has
\[
\nu_0=\sqrt{13}>\rho_0=2,
\qquad
|G_{K^{-1}}(r)|\le C e^{-(2+\sqrt{13})r}.
\]
It is therefore absolutely integrable, with exponential margin
\[
(2+\sqrt{13})-4=\sqrt{13}-2=1.605551275\ldots.
\tag{M-line}
\]
The local \(r^{-2}\) Green singularity is integrable in real dimension four. The explicit hypergeometric formula also shows that zero is not a pole: Will's poles occur at negative parameters and, in the positive discrete family, at \(|l|-n-2j\le1\), whereas \(\sqrt{13}>1\).

This is the decisive comparison that the Step-44 heuristic lacked: the decay exponent \(2+\sqrt{13}\), not merely the \(L^2\) bottom, beats the lattice/volume exponent \(4\).

Sources read for this calculation: Will's radial Casimir and resolvent kernel \cite{unknownpdfe}; its exact lines are the radial operator, \(\rho(l)=n-l\), the hypergeometric \(Q_{\nu,l}\), decay, and \(L^1\) threshold in `Knowledge/objects/papers/PDF-The-Meromorphic-continuation-of-the-resolvent-of-the--65f06f69884f--4497d74c3b78/object.md`. Askour--Bouaouid--Elhadouni independently give the line-bundle magnetic spectrum and resolvent kernels \cite{askour2021spectral}.

---

## 2. Lemma M for the one-form block

In the same normalization, the one-form block of \(\mathcal L^*\mathcal L\) is
\[
B_1=dd^*+\frac12d^*d+6
     =\frac12(\Delta_1+dd^*+12).
\]
It is not Laplace type, but it is exactly reducible to Hodge resolvents:
\[
\boxed{
B_1^{-1}
=2(\Delta_1+12)^{-1}
-d(\Delta_0+6)^{-1}(\Delta_0+12)^{-1}d^* .}
\tag{M-1form}
\]
Indeed, on exact forms \(B_1=\Delta_1+6\); on coexact forms \(B_1=(\Delta_1+12)/2\). The displayed operator has the corresponding multipliers \((x+6)^{-1}\) and \(2(x+12)^{-1}\); the script verifies both residuals identically zero.

Carron--Pedon's exact/coexact Hodge-kernel expansion has decay \(e^{-(\rho_0+s)r}\) for \((\Delta_p-\alpha_p+s^2)^{-1}\) \cite{carrondifferential}. On \(\mathbb{CH}^2\),
\[
\alpha_0=\rho_0^2=4,
\qquad
\alpha_1=(2-1)^2=1.
\]
Thus the slow exact mode of \(B_1^{-1}\) has
\[
s_e=\sqrt{4+6}=\sqrt{10},
\quad |G_e(r)|=O(e^{-(2+\sqrt{10})r}),
\quad \sqrt{10}-2=1.162277660\ldots>0,
\]
and the coexact mode has
\[
s_c=\sqrt{1+12}=\sqrt{13},
\quad |G_c(r)|=O(e^{-(2+\sqrt{13})r}).
\]
By the partial fraction \((\Delta_0+6)^{-1}(\Delta_0+12)^{-1}=\tfrac16[(\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}]\) the leading \(r^{-2}\) singularities cancel, leaving \(O(r^{-2})\) after \(d_xd_y\); the exponential order is unchanged (explicit bound in Step 46 §2.3). Hence the one-form Green kernel is \(L^1\).

**Lemma M (homogeneous form).** The two non-pointwise-positive blocks of the gauge-fixed canonical SW normal operator on \(\mathbb{CH}^2\) have \(L^1\) Green kernels. The slow exponential margin over volume growth is \(\sqrt{10}-2>0\). All remaining blocks have pointwise-positive potentials and the scalar maximum-principle/Kato argument used in Step 44.

### Finite covers and the extensive theorem

For a finite cover \(X_\Gamma\), periodize the universal kernels. Absolute convergence follows from the \(L^1\) bounds. For any bounded input \(f\), unfold one fundamental domain:
\[
|G_\Gamma f(x)|
\le\|f\|_\infty\sum_{\gamma\in\Gamma}
\int_F |G(x,\gamma y)|dy
=\|f\|_\infty\int_{\mathbb{CH}^2}|G(x,z)|dz.
\]
Thus the \(L^\infty\) inverse norm is independent of \(\Gamma\). Interior homogeneous Schauder estimates then give uniformly local \(C^{2,\alpha}\) inverses. *(Step-46 correction of scope: as written here this supplied the missing cover-uniform model inverses only; the uniformly local nonlinear slice/IFT argument, and an elementary ODE/Kato proof of these inverses with explicit norms, are in `step46_lemmaM_elementary_and_AC.md`, where \(A_C\) is proved.)* Combined with the Step-44 pointwise Koiso and gauge gaps and that nonlinear argument, one obtains the extensive form \(A_C\) of Theorem A for the **nearby canonical monopole branch**: there is a model-scale \(\varepsilon_0>0\), independent of every finite cover, such that uniformly local \(C^{2,\alpha}\)-closeness to the CH metric gives a unique canonical branch and
\[
R_{\rm can}(g)\le C P(g)
\]
with cover-independent \(C\). It excludes the diffuse common mode within that extensive neighborhood. It remains a perturbative statement about the nearby branch, not about every global monopole on a blow-up and not an Einstein-gap tariff.

---

## 3. Exact Kähler-orbit departure theorem

Let \(\mathcal K\subset S^2_0(\Lambda^+)\) be the \(SO(3)\)-orbit with spectrum \((-2/3,1/3,1/3)\), the scalar-\(-4\) Kähler-type orbit. Fix \(W_*\in\mathcal K\) with distinguished unit direction \(\hat\omega\), let \(q=\langle n,\hat\omega\rangle^2\), and write \(W^+=W_*+E\). For one field, drop only the nonpositive \(-4|\zeta|^2\) and Walsh terms from Theorem W. The remaining saving density is
\[
f(W^+,r,n)=r^2M(n,n)-4|M|^2+\frac{(2-r)(r-1)(3r+2)}3,
\quad
M=W^+-\frac{r^2}{4}\left(\frac I3-n\otimes n\right).
\]
Exact expansion gives
\[
\boxed{
f(W_*,r,n)=-(2-r)^2(r+1)-r^2(1-q)\le0.}
\tag{K0}
\]
Equality holds only at canonical amplitude \(r=2\) and \(n=\pm\hat\omega\). Thus depletion and directional mismatch are both costly at exact Kähler-type curvature.

Off the orbit,
\[
f(W_*+E,r,n)=f(W_*,r,n)+\langle G_{r,n},E\rangle-4|E|^2,
\]
\[
G_{r,n}=r^2(nn)_0-8M_*,
\qquad
|G_{r,n}|^2=\frac23r^4+\frac{128}3-16r^2(q-\tfrac13).
\tag{K1}
\]
The sharp uniform coefficient in \(f\le C|E|\) is
\[
\boxed{C_{\mathcal K}=\frac{4\sqrt6}{3}=3.2659863237\ldots.}
\tag{K2}
\]
It is attained in the limit at \(r=2,q=1,E\to0\) along the linear response direction. The script's global optimization on \([0,2]\times[0,1]\) returns exactly this state; the exact canonical norm is \(|G_{2,\hat\omega}|^2=32/3\). This sharpens the verifier's safe constant \(<15\).

Choose pointwise a closest \(W_*\in\mathcal K\). Averaging the exact Theorem-W identity over the sign family therefore proves:

**Theorem K (field-selection-free Weyl departure).** Under the all-metric sign-family hypotheses of Theorems N/W, for the scalar-\(-4\) Yamabe representative \(\hat g\),
\[
\boxed{
8\pi^2k-P(g)
\le 8\pi^2k-P(\hat g)
\le \frac{4\sqrt6}{3}\int_M
\operatorname{dist}(W^+_{\hat g},\mathcal K)\,d\mu_{\hat g}.}
\tag{K3}
\]
Consequently, if \(P(g)\le8\pi^2ck\),
\[
\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)
\ge \frac{6\pi^2}{\sqrt6}(1-c)k
=\sqrt6\,\pi^2(1-c)k.
\tag{K4}
\]
For the certified coefficient interval this is \(0.1048555811\ldots\)–\(0.1048555815\ldots\) per exceptional class; the rigorous downward rounding is \(0.10485\,k\). The exact number is a necessary closed-host quantity, not a measurement on the isolated cell.

There is no pointwise quadratic replacement of (K3). At the equality state, \(r=2,n=\hat\omega\),
\[
f=4E(\hat\omega,\hat\omega)-4|E|^2,
\]
so the departure is genuinely linear. A quadratic estimate needs cancellation of the integrated first variation (Bach stationarity on a closed Einstein host, or explicit interface/collar accounting after gluing). This is exactly where marked-core action enters.

---

## 4. Consequences for the zero-form configuration and the three regimes

A01's actual object has two metrics/forms that cannot be interchanged:

1. \(g\) is the smooth replicated cell metric. The glued harmonic self-dual form \(\Omega\) equals the host Kähler form on collars, has \(E_i\cdot\Omega=0\), and vanishes on each bolt. It is **not** almost-Kähler on the zero set, so AK\(\Gamma\), Proposition \(\Pi\), and Proposition 43.C cannot be integrated across the bolt without zero-set/boundary terms.
2. \(\hat g=u^2g\) makes the normalized direction almost-Kähler only on the complement, but is singular at the bolt. On \(M\setminus N_\varepsilon(Z)\), integration by parts in the Cotton identity has the extra flux
\[
\int_{\partial N_\varepsilon(Z)}\mathcal B(a,n,\nabla n,E,\operatorname{Ric}^\circ),
\]
and \(a\ge a_0>0\) fails as \(\varepsilon\downarrow0\). No sign or vanishing has been proved. Theorem K avoids both defects because it is algebraic and is applied to the smooth scalar-\(-4\) representative.

The perturbative extensive theorem also does not directly localize over the replicated blow-up. Removing \(k\) bolt neighborhoods and applying interior estimates produces: (i) collar data/action for the metric; (ii) a branch-selection error because a global blow-up monopole need not be the nearby canonical solution on the host bulk. With \(k\) collars, these errors are naturally \(O(k)\) unless a complete marked-core theorem supplies cancellation. A coupled metric/form deformation that spreads the zero region is not excluded by Theorem \(A_C\) alone; it must either leave the uniform CH neighborhood, or carry noncanonical field behavior, or pay the collar/core term. Theorem K adds that any net subunit saving must also carry linear integrated Weyl-orbit departure.

The strategist's torsion picture can now be stated without pretending to prove the missing critical estimate. For an almost-Kähler representative write \(\delta=|\nabla\omega|^2\), \(\sigma=-s\):

- **Diffuse region:** \(\delta\le\varepsilon\sigma\). Bochner reduces the second-jet debt to \(\int|\operatorname{Rm}|\delta\) and \(\int\delta^2\), but closing \(P\gtrsim R^2/A\) still requires an \(E=W^+-W_0\) variance estimate. It is proved perturbatively in the CH neighborhood by \(A_C\), not globally.
- **Concentrated region:** \(\delta\ge(1+\eta)\sigma\). This lies in the threshold pocket \(s^*\ge\eta\sigma\) and Proposition \(\Pi\)'s threshold Jensen term prices its volume. It can nevertheless be cheap if the pockets shrink, exactly as Step 44 observed.
- **Intermediate region:** \(\varepsilon\sigma<\delta<(1+\eta)\sigma\). Neither small-parameter CH coercivity nor a positive \(s^*\) threshold prices it. Kirchberg's quartic identity retains the Cotton pairing. A nonperturbative approximate common mode must live here or at the harmonic zero set/collars. This is a target configuration, not a proved exhaustive theorem for arbitrary monopole fields.

For A01 the actionable measurements are therefore separated by object: on smooth \(g\), measure \(|\Omega|\), \(|\nabla\Omega|\), tube fluxes, and — on its scalar-\(-4\) Yamabe representative, not on \(g\) itself unless \(s_g\equiv-4\) — \(\int\operatorname{dist}(W^+,\mathcal K)\); on singular \(\hat g\), report truncated \(s^*\)-pocket profiles together with the \(\varepsilon\)-dependent boundary term, never as a closed AK\(\Gamma\) measurement. For a smoothed positive-area alternative, retain the period-angle variables \(\alpha=\sum|E_i\cdot\omega|/\sqrt{2AV}\) and \(\eta=|K_X\cdot\omega|/\sqrt{2AV}\); \(\eta\ge1\) is unavailable without \(H_L\).

Finally, these statements concern pure blow-ups in the open \(0<k<A/3\) window. The selected balanced/two-parameter family has its separate certified sub-four construction and exclusion of \(\alpha=o(Q/A)\); density-free O10 concerns field concentration and does not follow from the present \(\chi/A\)-bounded setting.

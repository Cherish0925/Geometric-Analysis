# Einstein gaps on four-manifolds: dependence-ordered theorem package (v1)

This file is a research map for the Discovery loop. It records the mathematical objects, proved results, certified computations, numerical structures, and open implications in dependency order. It is not a paper and does not turn construction-level information into a theorem about the unrestricted infimum.

## 1. Functionals, scale, and distinct questions

Let \(M\) be a closed oriented smooth four-manifold. The direct Einstein defect \(\mathcal E\), its trace-free Ricci component
\[
P(g)=\int_M |\operatorname{Ric}^{\circ}_g|^2\,d\mu_g,
\]
and the field-alignment functionals \(\kappa_\beta\) are distinct. The invariant of interest is \(\alpha(M)=\inf_g\mathscr D(g)\), with the precise normalization and admissible class inherited from the geometric-analysis corpus. Any passage among \(\mathcal E\), \(P\), and \(\kappa_\beta\) must use its stated scalar/Yamabe normalization and same-metric identities.

Research status vocabulary used below:

- **Proved:** analytic argument with its hypotheses recorded.
- **Certified:** a fixed explicit metric or flow is enclosed by interval arithmetic, with exact input data.
- **Numerical structure:** reproducible computation that guides a theorem but is not itself a general theorem.
- **Open:** an implication needed for the unrestricted \(\alpha\)-problem has not been established.

## 2. Actual fields control the regular bulk

### 2.1 Bounded-form interface and linear coercivity — Proved

The inherited bounded-form theorem has the form \((1+B_\psi)d_\psi\ge c(K)\). The I40/I41 estimates retain differential information from an actual field; schematically,
\[
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\}.
\]
Formal Chern--Weil and monopole-number budgets do not imply this estimate. Hence a localization theorem for near-minimizers must carry the actual field, or an equivalent differential object, through regular regions and concentration regions.

Primary paths: `Skills/geometric-analysis/research/supplements/20261004_classical_and_quantitative_gaps.tex`; `Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex`; `workspace/notes/step1_field_compatibility_and_route_portfolio.md`.

### 2.2 Density-free finite-\(\beta\) alignment theorem — Proved

Assume metric-wise conformal monopole supply with \(p\ge A>0\), \(a^2\ge T_+\), and \(T_+\le\theta A\) for \(\theta<3/4\). Then every finite \(\beta\ge2\) has a uniform positive lower bound for \(\kappa_\beta\). The algebra is governed by
\[
a(\theta,\beta)=
\frac{(\frac34-\theta)\beta^2+(\frac12-\frac{11}{4}\theta)\beta+6-\theta}
{\beta(9\beta-\theta+6)},
\]
whose numerator has discriminant
\[
\frac{57}{16}\left(\theta-\frac23\right)
\left(\theta+\frac{142}{19}\right).
\]
At \(\theta=2/3\) it is \((\beta-8)^2/12\). This explains the thresholds \(2/3\), \(\beta=8\), and \(3/4\). The verified Kähler application is restricted to the recorded minimal general-type, \(p_g\ge1\), blow-up setting. This is an alignment theorem and does not imply a positive direct Einstein gap.

Primary paths: `workspace/notes/step4_O10_localization_and_orbifold_test.md`; `workspace/scripts/o10_localization.py`; Step-5 records.

### 2.3 Charged concentration tangents — Proved model calculation

One- and multi-centre Gibbons--Hawking spaces carry genuine solutions of the leading coupled tangent equations, with
\[
\int|\nabla v|^2=8\pi^2m_*k\ell^2,
\qquad
\int|d|v|^2|^2=\frac{16\pi^2}{3}m_*^2k\ell^2.
\]
The \(k\)-centre topology has \(b_2=k-1\) and boundary \(L(k,1)\). These tangents rule out a leading-order density-free Liouville argument; they do not by themselves produce closed-manifold escape sequences.

Primary paths: `workspace/scripts/verify_gh_tangent.py`; `workspace/scripts/gh_multicentre_energy.py`.

## 3. Zero gap, attainment, exact Einstein existence, and entropy-supplied nonexistence

### 3.1 Canonical-model resolutions — Proved construction

For the stated minimal Kähler surfaces of general type, resolving canonical negative Kähler--Einstein orbifolds with shrinking Ricci-flat ALE pieces gives smooth metrics with \(\mathcal E\to0\), hence \(\alpha=0\). The core contribution vanishes because its volume tends to zero even though \(|\operatorname{Ric}+g|^2=4\) there. In this zero-gap class, attainment is equivalent to existence of a smooth non-Ricci-flat Einstein metric on the underlying smooth manifold. Ampleness supplies the canonical Kähler--Einstein case; nef/nonample does not exclude all other complex or non-Kähler Einstein metrics.

### 3.2 Rational-blowdown examples — Proved construction with source attribution

Şuvaina-type generalized rational blowdowns provide further zero-gap manifolds, including simply connected minimal symplectic non-Kähler examples. Exact Einstein exterior, scaled Ricci-flat filler, bounded-curvature shrinking collar, and vanishing filler volume yield \(\alpha=0\). The source establishes non-Kählerness, not absence of every complex structure.

Primary paths: `workspace/notes/step6_theorems_and_O11_rotation.md`; `Knowledge/objects/papers/The-Yamabe-invariant-of-a-class-of-symplectic-4-manifolds--93fc75a3247d--f4170b4b9bdb/object.md`.

### 3.3 Real-hyperbolic blow-ups: exact Einstein nonexistence from entropy — Proved

Let \(Y\) be a closed oriented real-hyperbolic four-manifold and \(X=Y\#k\overline{\mathbb{CP}}^{\,2}\). The pinch map \(X\to Y\) has degree one, while
\[
\chi(X)=\chi(Y)+k,\qquad \sigma(X)=-k.
\]
Kotschick's entropy-strengthened Einstein inequality and its Sambusetti/BCG degree corollary require every Einstein \(X\) mapping with degree \(d\ne0\) to \(Y\) to satisfy
\[
\chi(X)\ge\frac32|\sigma(X)|+|d|\chi(Y).
\]
For the pinch map this would give \(k\ge3k/2\), impossible for every \(k\ge1\). Hence no real-hyperbolic blow-up carries an Einstein metric. This is a new actual supplier beyond monopole classes: the input is homological minimal-volume entropy. It is an exact existence obstruction, not by itself a positive critical-\(L^2\) Einstein-gap theorem for the low-blow-up range. The source does not compute the Yamabe invariant of these blow-ups.

Primary paths: `workspace/notes/step21_entropy_hyperbolic_cells_and_offbolt_weyl.md`; `Knowledge/objects/papers/ENTROPIES-VOLUMES-AND-EINSTEIN-METRICS--0ee1eb110f9d--94203f883336/object.md`; `trace/ttcs/results/step21_ttcs01_verifier1_integration.md`.

### 3.4 Real-hyperbolic blow-ups: the gap is the Yamabe problem — Proved identity; sharp value conditional on one Yamabe identity (Step 23)

For every metric on \(X_k=Y\#k\overline{\mathbb{CP}}^2\), with \(Y_{\rm hyp}^2/12=16\pi^2\chi(Y)\),
\[
P=8\pi^2k+4\int|W^+|^2+\frac{Y[g]^2-Y_{\rm hyp}^2}{12}+3\int(\Delta u/u)^2+24\int|\nabla u|^2\quad(Y[g]<0),
\]
where \(u^2g\) is the \(\hat s=-24\) Yamabe metric (exact form of LeBrun's \(\int s^2\ge Y[g]^2\)). **Theorem H:** if \(\mathcal Y(X_k)=Y_{\rm hyp}\) (Schoen's conjecture plus blow-up invariance), then \(P>8\pi^2k\) for every metric, \(\inf P=8\pi^2k\) (Burns concentration, Theorem F with \(\mathbf R^+=-2I\)), not attained (equality would make \(g\) a Yamabe-invariant-attaining metric, hence Einstein; LeBrun 1996), and \(\alpha(X_k)=\inf\mathcal E=\inf\mathcal J=4k/(k+6\chi(Y))\) for \(1\le k\le2\chi(Y)\), not attained for \(k<2\chi(Y)\). At \(k=2\chi(Y)\) the infimum is unconditionally \(1\) and its attainment is equivalent to an anti-self-dual (for \(\mathcal E\): anti-self-dual constant-scalar) metric, not excluded here. Arbitrary minimizing sequences are globally asymptotically half-conformally-flat and Yamabe-extremal; the allocation of \(8\pi^2\) to each exceptional class is proved only for Burns sequences. Unconditionally, with \(y_k=\mathcal Y(X_k)^2/Y_{\rm hyp}^2\): \(P\ge8\pi^2k-(1-y_k)16\pi^2\chi(Y)\), and \(\alpha(X_k)>0\) whenever \(y_k>1-k/(2\chi(Y))\); \(y_k=1\) is sufficient, not proved necessary, for \(\inf P=8\pi^2k\). For \(k>2\chi(Y)\), \(\mathcal E\ge\mathcal J>1\) pointwise but \(\inf\mathcal J=1\) by conformal inflation and \(\inf\mathcal E\in[1,4k/(k+6\chi(Y))]\) is undetermined. The conformal identity is already implicit in LeBrun's 1996 Lemma 1. Theorem H\(_\varepsilon\) is the pointwise-Ricci shadow. Path: `workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md` §3.
### 3.5 Kähler blow-up tariff and paired actual fields — Proved restricted theorem; global paired coercivity open (Step 38)

For a fixed blow-up complex structure \(M=X\#k\overline{\mathbb{CP}}^2\), \(A=K_X^2\), every Kähler metric in the complex orientation satisfies
\[
 C_+=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2
 =\frac1{32\pi^2}\int s^2\ge A,
 \qquad P\ge8\pi^2k.
\]
Writing \(K_M=K_0+\sum E_i\), \(\Omega=[\omega]\), and \(e_i=\Omega\cdot E_i>0\), the Hodge-index proof is
\[
 C_+=\frac{(K_M\cdot\Omega)^2}{\Omega^2}+\frac1{32\pi^2}\int(s-\bar s)^2,
 \qquad K_0\cdot\Omega\ge\sqrt{A\Omega^2}.
\]
Hence the inequalities are strict when \(k>0\). Equality of the Kähler infimum with \(8\pi^2k\) additionally needs a Kähler recovery family; Theorem F alone is Riemannian and does not supply that input.

For sign-family monopoles \(a_\epsilon=c+\sum\epsilon_iE_i\), the paired inner product is a section of the relative twisting line with
\[
 c_1(u_{\epsilon\epsilon'})=\frac{a_\epsilon-a_{\epsilon'}}2;
\]
a single sign flip therefore gives \(c_1(u)=\pm E_i\), not \(\pm2E_i\). Its zero may be an amplitude vortex or pointwise spinor orthogonality. In scalar \(-4\) normalization, simultaneous actual solutions give the exact nonnegative amplitude form and in particular
\[
 P\ge8\pi^2Q-4\,\mathbb E_\epsilon\int(2-|\Phi_\epsilon|^2).
\]
The paired field recovers individual exceptional topology lost by convex projection, but it is exactly the singleton Walsh sector rather than an additional positive sector. For one sign flip, with relative curvature \(h=(f-f')/2\),
\[
 |h^+|^2=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2},\qquad
 \|h^-\|_2^2-\|h^+\|_2^2=4\pi^2.
\]
The fixed negative-square charge lies in the field-undetermined anti-self-dual relative curvature. Moreover the combined bilinear \((u,w)\) lies in a rank-two bundle of \(c_2=0\); its normalized value is \(S^3\)-valued where both spinors are nonzero, so the \(u\)-phase vortex can unwind through \(w\). No metric-uniform vortex/relative-rotation excess follows without extra projection/noncollapse and kinetic-compensation input. The cheap perpendicular cell has zero compatible almost-Kähler period on \(E\), showing that this rotation channel is geometrically real.

The SU(2)-invariant isolated-cell monopole ODE is exact, but the Step-37/38 numerical attempts imposed incorrect finite-end or cutoff conditions and produced no monopole profile. Exact finite-radius matching to the complete canonical CH monopole is impossible in a charged invariant sector by backward uniqueness; asymptotic convergence requires matching the two-dimensional CH stable manifold. Closed-host monopoles need not induce that isolated invariant boundary problem.

For a topology-preserving ramification neighbourhood with the same controlled boundary germ as its Kähler--Einstein model, relative signature and the relative \(P\) identity give exactly
\[
 \Delta B=\frac14P_N-\frac1{48}\Delta S;
\]
in scalar \(-4\) normalization, \(\Delta B=P_N/4-\Delta V/3\). Hence characteristic flux alone has no anti-self-dual retention sign: retention is precisely a relative-volume upper problem, and depletion occurs when \(\Delta V>3P_N/4\).

Primary path: `workspace/notes/step38_kahler_and_paired_field_scope.md`; independent verification: `trace/ttcs/results/step38_ttcs01_verifier1_integration.md`, `step38_ttcs01_verifier2_integration.md`.

### 3.6 The monopole family on arbitrary metrics: amplitude, Nijenhuis and Weyl forms; affine exhaustion at LeBrun's threshold; the common mode — Proved identities; tariff open (Steps 39–40)

*Quantifiers.* Fixed Spin\(^c\) structures \(a_\epsilon=c+\sum\epsilon_iE_i\); for \(b^+\ge2\), chamber-independent nonzero invariants give unperturbed solutions for every metric (LeBrun's limiting argument); if \(A-k>0\) all solutions are irreducible; apply to the scalar \(-4\) Yamabe representative (\(P(g)\ge P(\hat g)\)); benchmark \(8\pi^2Q\) uses simple type; handles need the higher-type supplier. Saving \(\mathfrak S=8\pi^2Q-P\), Walsh part \(\mathcal W\ge0\), \(M=W^+-W_0\), \(x=M(n,n)\).

*Amplitude form (Step 39).* \(\mathfrak S=\mathbb E\int m(\rho)-8\mathbb E\|\zeta\|^2-4\mathbb E\|M\|^2-\mathcal W\), \(m=(2-\rho)(-\rho^3+10\rho^2-2\rho-4)/6\); positive only on \(0.7758<\rho<2\), \(m_{\max}=1.01555\). Hence \(P/(8\pi^2k)\to c<1\) forces \(\mathbb E\int(2-\rho)\ge2\pi^2(1-c)k-o(k)\).

*Lemma 1 (Step 40).* The Dirac equation fixes the Lee (\(\mathcal W_4\)) component of the rotation of the monopole almost-complex structure, \(\rho|v_4|^2=\frac12|a+J'b|^2\) (\(a=d\sqrt\rho\), \(b=\sqrt\rho\beta\)), and does not see the Nijenhuis (\(\mathcal W_2\)) component (\(\ker\) Clifford contraction \(=\mathcal W_2\), \(cc^*=2\)).

*Theorem N (exact).* \(\mathfrak S=\frac12\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}-\mathbb E\int\frac{(2-\rho)^2(2+2\rho-\rho^2)}6-\mathbb E\int\rho(|a|^2+5|b|^2-2\langle a,J'b\rangle)-4\mathbb E\|M\|^2-\mathcal W\). Corollaries: Hermitian tariff \(P\ge8\pi^2Q\) for scalar \(-4\) metrics admitting a simultaneous integrable choice; near-minimizers with ratio \(c<1\) have \(\liminf k^{-1}\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}\ge16\pi^2(1-c)\) (\(\ge0.684914\) per class for a closed replica of the certified cell).

*Theorem W (exact).* \(\mathfrak S=\mathbb E\int[\rho^2x-4|M|^2]+\mathbb E\int\frac{(2-\rho)(\rho-1)(3\rho+2)}3-4\mathbb E\|\zeta\|^2-\mathcal W\), using \(|d\psi|^2=2|\operatorname{Im}\zeta|^2\). Saving is Weyl-type (rise of \(W^+(n,n)\) above \(-\rho^2/6\)) plus volume-type shallow depletion.

*Theorem E (affine pointwise exhaustion).* Constant affine combinations of these forms with \(P=4W_++4V/3-8\pi^2(A-k)\), \(|W^+|^2=\rho^4/24-\rho^2x/2+|M|^2\), \(|M|^2\ge\frac32x^2\) give \(P\ge8\pi^2[k-(1-t)A]+\mathbb E\int g_{t,\lambda}\) with \(g_{2/3,2/3}=-\frac2{243}(2\rho-3)^2(\rho^2-24\rho-18)\ge0\) (LeBrun's \(C_+\ge2A/3\)) and \(\max_\lambda g_{t,\lambda}(3/2)=-\frac34(3t-2)\): nothing beyond LeBrun; contact at \(\rho=3/2\), not at KE.

*Formal common mode.* Constant \(\rho=r\), \(\zeta=0\), \(d\psi=0\) (almost-Kähler, all \(E_i\) ASD-harmonic, null periods) gives \(P/(8\pi^2)=k-A\beta(r)\), \(\beta=16/r-5-12/r^2\); \(r=2-k/A\) gives \(P=o(k)\) with uniform torsion \(|\nabla J|^2\approx2k/A\). Thus the exact identities are consistent with \(c\to0\). **Step-42 correction:** the exact mode is topologically excluded for \(b^+\ge2\) (Lemma T of §3.7: a nowhere-zero self-dual harmonic form has positive period on every exceptional class); it is the \(\alpha=0\) equality case of Theorem AKΓ, with \(\beta(r)=2\theta-3\theta^2\), \(\theta=h/(2-h)\). Approximate modes (tiny positive exceptional areas, or thin zero sets of the harmonic part) are not excluded, so the obstruction must still be a linear coercivity of diffuse torsion (§3.7, Proposition G).

Paths: `workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md`; `workspace/scripts/step40_nijenhuis_tariff_check.py`; `workspace/data/step40_nijenhuis_tariff_check.json`; verification `trace/ttcs/results/step40_ttcs01_verifier1_integration.md`; mechanisms `trace/ttcs/results/step40_ttcs01_generator1_integration.md`; Step 39: `workspace/scripts/step39_amplitude_band_and_curvature_channels.py`, `trace/ttcs/results/step39_ttcs01_verifier{1,2}_integration.md`.

### 3.7 Blindness theorem, Taubes period lemma, almost-Kähler torsion profile, and the Goldberg reduction — Proved (Step 42); coercive estimate open

*Setting.* \(M=X\#k\overline{\mathbb{CP}}^2\), \(X\) minimal, \(b^+(X)\ge2\), basic classes exactly \(\pm K_X\) modulo torsion (hypothesis), \(A=K_X^2\), \(0<k<A/3\). In this range with \(b^+\ge2\) simple type, nonzero invariants plus \(A-k>0\) give irreducible unperturbed solutions of every sign class for every metric; \(b^+=1\) keeps its chamber input.

*Theorem B (blindness of the self-dual sign-family data; Step 38).* For one sign flip at \(E_i\), the relative curvature \(h=(f_\epsilon-f_{\epsilon^i})/2\) satisfies \(\|h^-\|^2-\|h^+\|^2=4\pi^2\); every self-dual quantity of the family (amplitudes, \(\psi_\epsilon\), Walsh self-dual energy) sees only \(h^+\), which may vanish, and the forced zero of \(u\) unwinds through \(w\) (\(S^3\)-valued pair, \(\pi_1(S^3)=0\)). Consequently no estimate built only from monopole amplitudes and self-dual curvature of the sign family yields a \(k\)-dependent excess; together with Theorem E this closes the Seiberg–Witten-identity route as a source of the tariff.

*Lemma T (Taubes period lemma).* For any symplectic \(\omega\) on \(M\) (e.g. a nowhere-zero self-dual harmonic form of any metric), \(K_\omega\cdot\omega=|K_X\cdot\omega|+\sum_i|E_i\cdot\omega|\) with every \(|E_i\cdot\omega|>0\) (Taubes SW⇒Gr plus the blow-up formula). Corollary: a self-dual harmonic form with a null exceptional period vanishes somewhere. The symmetric perpendicular cell's canonical closed form has null period and vanishes along the bolt (A01 profile: \(|\omega|_g=\sqrt2u^2\), \(u=0.0072\) at the first bolt sample); it is not an almost-Kähler structure. Lemma T packages a standard argument (LeBrun 2001, Prop. 3.2); new is its use against the common mode.

*Theorem AKΓ.* For every almost-Kähler \((g,\omega)\) on \(M\), with \(\ell=8\pi K_\omega\cdot[\omega]\), \(\theta=\ell^{-1}\int|\nabla\omega|^2\), \(\alpha=\sum|E_i\cdot\omega|/\sqrt{2AV}>0\), \(\eta=|K_X\cdot\omega|/\sqrt{2AV}\):
\[
C_+\ge\frac{\ell^2}{128\pi^2V}(3\theta^2-2\theta+1)=A(\eta+\alpha)^2(3\theta^2-2\theta+1).
\]
(Pointwise \(|W^+|^2\ge\frac32W^+(u,u)^2\), \(W^+(u,u)=s/6+|\nabla\omega|^2/4\); Blair's \(\int(s+s^*)=-8\pi K_\omega\cdot\omega\) fixes the means; Jensen; Lemma T.) \(\eta\ge1\) is **not** automatic for \(b^+\ge2\) (verified counter-mechanism \(\omega_0+t\operatorname{Re}\Omega\)); it holds under the Lorentzian hypothesis (H\(_L\)), e.g. in the Kähler case, where then \(P/(8\pi^2)>k-A(2\theta-3\theta^2)\). \(\theta=0\): Kähler tariff strengthened by areas. \(\min\Gamma=2/3\) at \(\theta=1/3\) (\(s^*=s/2\)): LeBrun's constant. Equality iff \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) along ω and \(s,s^*\) separately constant (ω lowest only for \(\theta<1/2\)); the Step-40 common mode is the formal \(\eta=1,\alpha=0\) member. Under (H\(_L\)) the saving is \(\le2A\theta\): linear in torsion.

*Proposition G (reduction).* Under (H\(_L\)) (or directly assuming \(p\ge k-2A\theta\)), if \(P\ge8\pi^2\kappa A\theta\) on a class of almost-Kähler metrics, then \(P\ge8\pi^2k\,\kappa/(\kappa+2)\) there. Monopole form (unconditional beyond §3.6 hypotheses): if \(P\ge\kappa\mathcal N\), \(\mathcal N=\frac12\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}\), then \(P\ge8\pi^2k\,\kappa/(1+\kappa)\); conversely \(P/(8\pi^2k)\to c\) forces \(\mathcal N/P\ge(1-c)/c\) (one-way). The tariff in the open range is thus implied by a linear negative-scalar Goldberg estimate. Its \(P=0\) endpoint on the eigenvector class is Armstrong's theorem; the correctly posed coercive target is a near-saturated quantitative Armstrong estimate \(P/(8\pi^2)+C\mathfrak d_{AK}\ge cA\theta\) with period-loss control, or the quartic variant \(\int|\mathrm{Ric}^\circ|^2\ge c\int|\nabla\omega|^4\) on \(W^+(\omega)^\perp=0\).

*Superseded.* The Step-39/41 co-rotation dichotomy: co-rotation is automatic in almost-Kähler geometry; misalignment is quadratic in torsion and the saving linear.

Paths: `workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md`; `workspace/scripts/step42_ak_torsion_profile.py`; `workspace/data/step42_ak_torsion_profile.json`; verification `trace/ttcs/results/step42_ttcs01_verifier1_integration.md`.

### 3.8 The corrected \(W_0\), divergence symbol, Cotton pairing and quadratic-law reduction — exact local identities; global estimate open (Steps 41–43)

For one monopole field, \(W_0=aK_n\), \(a=\rho^2/4\), \(K_n=I/3-n\otimes n\). Hence
\[
\operatorname{spec}(W_0)=(-\rho^2/6,\rho^2/12,\rho^2/12),\qquad |W_0|^2=\rho^4/24.
\]
For unit \(n,m\), \(|aK_n-aK_m|^2=2a^2(1-\langle n,m\rangle^2)=\rho^4\sin^2\theta/8\), and
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\frac{a^2}{2}(1-c^2)(1+3c^2),&c^2\ge1/3,\\
\frac{2a^2}{3},&c^2\le1/3,
\end{cases}\quad c=\langle n,m\rangle.
\]
Thus Kähler-type co-rotation is forced quantitatively only where \(\rho\) is bounded below. AAD's proper three-symmetric almost-Kähler model proves that this algebraic structure does not force integrability; the differential slack is the Cotton source \(\delta W^+=C^+=\nabla\operatorname{Ric}^\circ\).

**Proposition 43.B (exact divergence symbol).** For a smooth unit \(n\in\Lambda^+\),
\[
\delta W_0=\mathcal A(da)+a\mathcal T(\nabla n).
\]
If \(d(\sqrt2n)=0\) (the almost-Kähler first-jet condition), then in the standard induced tensor norm
\[
|\delta W_0|^2=\frac13|da|^2+\frac{a^2}{2}|\nabla n|^2,
\]
and the amplitude and torsion images are orthogonal. The torsion map has squared singular value \(1/2\), singular value \(1/\sqrt2\). For a general monopole direction the Dirac-controlled Lee component adds \(dn\) and amplitude--Lee cross terms; the restricted formula cannot be applied to the full jet without Theorem N's \(\zeta\) control.

**Proposition 43.C (exact Cotton pairing).** On a closed constant-scalar almost-Kähler four-manifold, write \(\omega=\sqrt2n\), assume \(a\ge a_0>0\), put \(E=W^+-W_0\), \(U=\mathcal T(\nabla n)\). Then
\[
\frac12\int a|\nabla n|^2=\int\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle-\int\langle E,\delta^*U\rangle,
\]
so
\[
\frac{a_0}{2}\int|\nabla n|^2\le\sqrt P\,\|\mathcal C^*U\|_2+\|E\|_2\,\|\delta^*U\|_2.
\]
No estimate of the adjoint norms by \(C\|\operatorname{Rm}\|_2\) is currently proved: they contain \(\nabla^2n\) and \((\nabla n)^2\). A localized monopole version additionally needs zero-set/band cutoffs, Lee torsion, amplitude-gradient products and control of \(E\). Hence the hoped-for quadratic transport law is conditional, not a theorem.

**Conditional optimization.** With total sign-averaged \(W_2\) energy \(R=\mathbb E\int|\nabla n|_{W_2}^2\), Theorem N gives exactly \(P\ge8\pi^2k-2R\). If an independent theorem gives \(P\ge R^2/(\Lambda A)\), then
\[
P\ge\bigl(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\bigr)^2
=\frac{16\pi^4k^2}{\Lambda A}+O(k^3/A^2).
\]
This would give a positive fixed-topology gap of order \(k^2/A\) without a uniform per-class tariff, but it is conditional on the missing transport/error estimate. Perturbative linear coercivity near a negative Kähler--Einstein host remains a separate spectral theorem; cover-uniformity is open.

**Kirchberg--Sekigawa resisting term.** In Kirchberg's norms, for scalar \(S=-4\),
\[
Q(J)+\int\bigl(|\widetilde R|^2+4|\operatorname{Ric}_\star^-|^2-2|\nabla J|^2+|\nabla J|^4\bigr)=0,
\]
with \(Q(J)=2\int\langle\varphi,\psi\rangle\) an explicit torsion--\(\nabla\operatorname{Ric}\) (Cotton) pairing. The adverse \(-2|\nabla J|^2\) and uncontrolled \(Q(J)\) are exactly why the negative-scalar formula does not give nonperturbative linear Goldberg coercivity from \(P\). AAD's proper three-symmetric local test has \(s=-3/4\), \(\kappa=3/4\), \(|\nabla\Omega|^2=1\), \(|\operatorname{Ric}^\circ|^2=9/64\); it allows Kähler-type algebraic curvature with nonzero torsion and caps any pointwise quartic constant at \(9/64\) in those conventions, but is noncompact/local.

Paths: `workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md`; `workspace/scripts/step43_w0_divergence_symbol.py`; `workspace/data/step43_w0_divergence_symbol.json`; `workspace/scripts/step43_proper3symmetric_test.py`; `workspace/data/step43_proper3symmetric_test.json`; verification `trace/ttcs/results/step43_ttcs01_verifier1_integration.md`.

## 4. Curvature-sensitive marked blow-up cells

For an exact-complex-hyperbolic-collar marked cell,
\[
P_{\rm cell}-8\pi^2=4\Delta W_++\frac1{12}\Delta S.
\]
This same-metric identity is the reason a Weyl-energy improvement alone does not control the direct defect.

### 4.1 First-order response for a general bulk — Proved (Theorem F, Step 20) as an upper construction

The aligned Kähler seed obeys
\[
\frac{P_K}{8\pi^2}=1+6\kappa x_0+9(\kappa^2+X^{-2})x_0^2+O_X(x_0^3).
\]
**Theorem F.** Let \((M,g)\) be closed and oriented, \(p\in M\), and \(\zeta\in\Lambda^+_p\) a unit form. Glue the Burns metric \(\delta+x_0h\), whose exceptional curve has area \(\pi x_0\), into \(g\)-normal coordinates with cutoff radius \(x_0^{1/5}\). This gives metrics on \(M\#\overline{\mathbb{CP}}^2\) with
\[
P(\hat g_{x_0})=P(g)+8\pi^2\big(1-x_0\mathbf R^+_p(\zeta,\zeta)\big)+O(x_0^{6/5}),
\]
and the same law holds for \(J\) when \(g\) is Einstein. The proof rests on two facts: the Burns tail is pointwise linearly self-dual-flat and scalar-flat, and its exact cut-annulus transgression is \(\Phi^{++}=\pi^2\,\hat\zeta\hat\zeta^T\), \(\Phi^{--}=\frac{\pi^2}3I\), \(\Phi^{+-}=0\) (exact sympy on \(S^3\)). The scalar flux \(4\pi^2x_0=4\pi\,\mathrm{area}(E)\) reproduces the Kähler identity \(\int s=4\pi c_1\cdot[\omega]\). Theorem F recovers the signed complex-space-form slopes \(+6,0,-6\). At a negative Kähler–Einstein point, \(\ker\mathbf R^+=\omega^\perp\) is first-order free and coincides with the directions allowed by the first \(A_1\) desingularization obstruction \(\mathbf R^+\zeta=0\). On real hyperbolic bulk \(\mathbf R^+=\frac s{12}I<0\), so every direction costs at first order. The matching lower bound for the cell infimum is open.

Primary paths: `workspace/notes/step20_burns_response_and_neck_quantization.md`; `workspace/scripts/burns_transgression_flux.py`; `workspace/data/burns_transgression_flux.json`; `workspace/scripts/o11_general_bulk_cell.py`.

**CR pinning (Lemma P, Step 25; independently verified in Step 26) — Proved.** For every diagonal metric, the Rossi variable \(\widetilde\Phi=q+\frac14(y_g-y_h)-\zeta\sinh q\) obeys exactly \(\widetilde\Phi'=F-\frac14(\mathrm{Ric}^\circ_{gg}-\mathrm{Ric}^\circ_{hh})\), hence \(|\Delta\widetilde\Phi-\int F|\le(\widehat P/2)^{1/2}(\int dt/W)^{1/2}\). In an ACH block, and only with that scope, \(F=\zeta^2G\) with bounded \(G\). Changing the Rossi squashing at radius \(T\) costs at least \(\frac12e^{4T}(\Delta\log\rho)^2\) (units \(8\pi^2\)), and the constant \(\frac12\) is the exact linearized optimum; the null-line value function and Lemma P measure the same charge and are not additive.

**Standard-CR truncation (Theorem T, Step 26) — Proved for diagonal scalar-\(-24\) ends in one small ACH block.** The CH linear rates are \(2,0,-2,-4,-6,-8\). The \(-2\) mode is exactly radial phase, while the physical Einstein modes begin at \(-4\); the \(-8\) mode is a forced constraint response for non-Einstein scalar-normalized ends. After matching radial phase, finite \(P\) and \(\widetilde\Phi\to0\) give transverse deviation \(o(e^{-2t})\), enough to splice on a unit annulus with added squared Einstein residual tending to zero. Hence a complete standard-CR diagonal Einstein ACH filling implies \(p^{\rm diag}_{1,0}=0\), while the converse needs attainment/compactness.

**Euler-flux collapse separation (Step 26) — Proved for diagonal annuli.** For \(\mathfrak b=W(\sum_i y_iK^{(3)}_{jk}-y_1y_2y_3)\), exact Cartan computation gives \(\widehat P(C)=\Delta\mathfrak b+\int|W|^2/(4\pi^2)+\int s^2/(96\pi^2)\). On CH, \(\mathfrak b=2-6\sinh^4t\). Arb evaluation on all 40 validated Theorem-E endpoint boxes gives \(\mathfrak b\in[-64533.462,-64275.416]\) once \(\widetilde\Phi\approx0.7845\). Product and ALF Berger necks have \(\mathfrak b\to0\), so a post-developed-Rossi connector to such a neck costs far above the certified cell value. High-shear scale-invariant connectors and resets before the developed ACH regime remain open.

Theorem E is therefore not a bounded-cost limit of exact-CH diagonal cells whose correction remains in the ACH block, nor can it first develop to the validated orbit and then pass through an ordinary product/ALF neck. The conditional structure Theorem D now has a proved truncation direction; its remaining inputs are compactness, high-shear/interior-collapse and large-bolt control, and validated no-return dynamics. Paths: `workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md`; `workspace/notes/step26_truncation_flux_and_branch_completeness.md`; `workspace/scripts/cr_pinning_check.py`; `workspace/scripts/squash_escape_cost.py`; `workspace/scripts/verify_euler_flux_identity.py`; `workspace/scripts/ach_euler_flux.py`.

**Chiral transgressions (Theorem X, Step 27) — Proved for diagonal annuli (exact symbolic).** There is an explicit signature transgression \(\mathfrak s\) with \(\mathfrak s'=\frac12W(B_+-B_-)\). With \(\mathfrak b_\pm=\mathfrak b\mp\mathfrak s\),
\(\widehat P(C)=\Delta\mathfrak b_\pm+\frac1{2\pi^2}\int_C|W^\pm|^2+\frac1{96\pi^2}\int_Cs^2\).

The charges \((\mathfrak b_+,\mathfrak b_-)\) are:
- smooth centre: \((2,2)\);
- \(O(-1)\) bolt in the blow-up orientation: \((1,7)\);
- biaxial or controlled near-biaxial Hopf-collapsed Berger orbit in the Taub–NUT/blow-up chirality: \((-2,2)\), since the Euler flux vanishes on collapse while \(\mathfrak s\) keeps an adiabatic charge; the opposite four-dimensional orientation gives \((2,-2)\), and unrestricted anisotropic collapsed jets have additional shear terms;
- CH orbit: \((2-9\sinh^4t,\ 2-3\sinh^4t)\).

Consequences:
- \(\widehat P[0,t]\ge\mathfrak b_+(t)-1\). This is the sharp, Burns-extremal replacement of Lemma Q′: Burns has \(W^+=s=0\) and \(\widehat P=2-1\).
- A cell with \(\widehat P<1\) has no orbit close to round.
- Decollapse from a collapsed neck to a CH-like orbit of radius \(\tau\) costs at least \(4-9\sinh^4\tau\).
- Taub-bolt is a regular zero-cost core in the blow-up orientation, with \(\frac1{2\pi^2}\int|W^\pm|^2=3,5\).

Step 28 independently verified the formula, signs, orientation and model balances. The normalized transgression is \(\mathfrak s=S_0-6\); raw `chiral_flux.json` fields use \(S_0\), so its `bA,bB` require shifts \(+6,-6\). The Hitchin–Thorpe prefactor is \(4\pi^2(2\chi\pm3\tau)\).

Files: `notes/step27_chiral_transgression_and_small_bolt.md`, `scripts/chiral_flux_identity.py`, `scripts/chiral_flux_models.py`; independent reading `trace/ttcs/results/step28_ttcs01_verifier1_integration.md`.

**Small-bolt Einstein structure (Step 27) — Matched-asymptotic mechanism, numerically confirmed.** As \(b\to0\) the perpendicular ACH separatrix is a Taub-bolt core followed by a collapsed \(\Lambda\)-Taub-NUT neck with circle \(\simeq4n\cosh\sqrt2t\), \(n=b/(2\sqrt3)\), and then saturation at scale one. The triaxial mode grows at rate \(4/\varepsilon\) in the neck, which predicts \(\log(1/d_*)\sim\pi\sqrt{3/2}/b=3.8476/b\); the fit gives \(3.854\). The Rossi parameter behaves as \(\rho\simeq0.8/b\to\infty\). A rigorous matching proof remains open.

**Scale-free saturation problem (Step 28) — Exact reduction; value open.** With \(a_f=re^{2\beta/3}\), \(a_g=re^{-\beta/3+q/2}\), \(a_h=re^{-\beta/3-q/2}\), \(d\tau=dt/r\), and \((\bar H,\bar E,\bar D)=r^2(H,E,D)\), the full diagonal dynamics and action become independent of the bolt scale:
\[
\widehat P=\int\left(3\bar H^2/16+\bar E^2/6+\bar D^2/8\right)d\tau.
\]
The collapsed branch is the control value from the Taub-bolt/\(\Lambda\)-Taub-NUT entry ray to the standard-CR end. All three controls are essential. Path: `notes/step28_saturation_control_and_revised_diagonal_structure.md`.

**Collapsed saturation value (Step 29) — Terminal reduction proved; value \(=4\) numerically.**

*Terminal reduction (Lemma S).* An exact-CH terminal jet followed by the homothetic exact CH collar is a legitimate exact-collar competitor. Two facts make this work: \(\widehat P\) is scale invariant, and zero-control flow is Einstein by the contracted Bianchi identity. By Theorem T this terminal has the same infimum as the standard-CR stable set, so no stable-manifold parameterization is needed. Step 28's rejection of these endpoints came from its checker, which forced the compact section \(\zeta=1/(a_ga_h)=10^{-2}\) and thereby rescaled CH jets.

*Numerical value.* The minimal action rises monotonically along the entry ray:

| \(\varepsilon\) | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 |
|---|---|---|---|---|---|---|---|---|
| minimal action | 2.33 | 3.38 | 3.75 | 3.89 | 3.95 | 3.976 | 3.988 | 3.994 |

Independent actual-metric evaluations of the same runs give 2.52, 3.48, 3.82, 3.93, 3.98 at \(\varepsilon=1/2\) to \(1/32\), 3.98841 at \(1/128\), and 3.9963 at \(1/256\). The values track the chiral gap \(2-\mathfrak b_+(\text{entry})\to4\).

*Structure of the minimizer.* For small \(\varepsilon\) the minimizer rises with \(W^+\approx0\) and \(s\approx0\), an ASD scalar-flat decollapse, to an exactly round orbit with \(\mathfrak b_+=2\). It then follows a CH ball at zero cost. The collapsed branch is therefore an ALF analogue of the Burns bubble. Burns pays \(2-1=1\); the collapsed route pays \(2-(-2)=4\).

*Opening radius.* Opening late is priced at least exponentially, roughly like \(e^{4\tau}\) (Lemma P): at \(\varepsilon=1/16\), windows starting at \(\tau=2.5,3,3.5,4\) cost about 4.1, 7.9, 34, 207.

*What remains.* The diagonal transgression itself now proves the first branch estimate in a precise finite-charge normalized-jet class. If a collapsed normalized first-jet family obeys
\[
x=Xz^3+o(z^3),\qquad p=Pz+o(z),\qquad \chi=Cz+o(z),\qquad \eta=Nz+o(z),
\]
then exact symbolic evaluation gives
\[
\mathfrak b_+^{\rm end}=-2-(C+4X)^2,
\]
so every annulus joining it to a round orbit satisfies the **Q″ inequality**
\[
\liminf\widehat P\ge2-\mathfrak b_+^{\rm end}=4+(C+4X)^2.
\]
Thus anisotropy in this finite-charge normalized-jet class cannot lower the Berger-to-round payment. The opposite charge is \(\mathfrak b_-^{\rm end}=2+(C-4X)^2\); \(P,N\) cancel from both limits. This class is not automatically bounded-curvature geometry: fixed-base-scale bounded orbit/mixed curvature imposes stronger decay, such as \(x=O(z^6)\), \(\chi=O(z^4)\), and radial second-derivative control, which force \(X,C\to0\). Burns and Taub-bolt/ALF decollapse are priced by the same rule: round charge minus bubble-end charge, respectively \(2-1=1\) and \(2-(-2)=4\). What remains for small-bolt matching is to prove that regular bolt trajectories enter a finite-charge or bounded-geometry class, or charge the production of an uncontrolled high-shear first jet.

**Fibre/base pinning (Step 30) — Proved identity.** Put \(v=y_f-(y_g+y_h)/2\) and
\[
\widetilde B=\log\frac{\kappa}{\sqrt{1+\zeta}}+\frac14(v-\kappa^{-1}).
\]
This vanishes on every CH orbit and obeys exactly
\[
\widetilde B'=F_\beta-\frac14\left(\operatorname{Ric}_{ff}-\frac{\operatorname{Ric}_{gg}+\operatorname{Ric}_{hh}}2\right),
\]
hence
\[
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le\sqrt{\frac{3\widehat P}{8}}\left(\int\frac{dt}{W}\right)^{1/2}.
\]
On an exact CH tail, \(\int_T^\infty W^{-1}dt=\frac1{2\sinh^2T}-\frac12\log(1+\sinh^{-2}T)\), giving an exponential late-opening payment once the effective mismatch is known. For a general connector this CH denominator requires a separate comparison with its actual \(\int W_g^{-1}dt\). With the CH denominator, overlap with the early-opening bound at \(T=.70\) needs mismatch at least \(0.370125\ldots\); volume comparison and free-drift control on the saturation region remain missing.

An enlarged-entry numerical test confirms why first-jet control matters. At \(\varepsilon=1/16\), imposing a fixed raw \(\Delta\eta=-8\) produces an explicit collocation path of cost \(0.5454\) and independently reconstructed metric cost \(0.5745\), below the certified cell; but this violates the finite-charge scaling above and at \(\varepsilon=1/32\) the same raw perturbation costs \(2.9425\). It is not a regular bolt construction. Its entry charge is already \(1.45194\), so the omitted bolt-to-entry prefix costs at least \(0.45194\); prefix plus reconstructed connector is at least \(1.0264\). It identifies uncontrolled contact-slot shear as the remaining high-shear escape mechanism rather than refuting Q″. Paths: `notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md`, `scripts/collapse_chiral_charge_limit.py`, `scripts/beta_pinning_identity.py`, `scripts/saturation_anisotropic_scan.py`, `data/saturation_control/step30_anisotropic_summary.json`.

**Theorem D (frozen statement, Step 29).**

*Setting.* Let \(p^{\rm diag}_{1,0}\) be the infimum of \(\widehat P\) over diagonal Bianchi-IX metrics on \(O(-1)\) with an exact CH collar. By Theorem C and the Yamabe solution, this equals the scalar-\(-24\) standard-CR value.

*(i) Einstein \(\Rightarrow\) zero — proved, unconditional.* If a complete diagonal Einstein ACH metric on \(O(-1)\) with standard CR infinity exists, then \(p^{\rm diag}_{1,0}=0\). This is Theorem T.

*(ii) Compactness — conditional on four branch inequalities.* Let \(g_j\) be a minimizing sequence. On bounded-shape, bounded-\(W\) regions the chiral identities bound the weighted curvature, and the state equations are affine in the Ricci controls. Hence a subsequence converges to a complete minimizer with standard CR infinity, unless one of four mechanisms occurs. In each case it suffices to show that the mechanism costs more than \(\min(p^{\rm diag}_{1,0}+\delta,\ 0.99585)\).

1. *Small-bolt collapse/saturation.* Finite-charge normalized entries are now priced rigorously by Q″ at \(4+(C+4X)^2\), while genuinely bounded-geometry Berger entries have \(X,C\to0\) and price \(4-o(1)\). The remaining work is the matched-entry theorem showing regular small-bolt sequences satisfy one of these asymptotic regimes; if they do not, the escaping first-jet shear joins mechanism 3.
2. *Large-bolt escape.* Status: open.
3. *Interior high-shear/volume-bounce connector.* The exact formula \(\mathfrak b_+^{\rm end}=-2-(C+4X)^2\) handles the finite-charge normalized-jet class, and bounded-geometry Berger collapse is a stronger subcase. Uncontrolled raw contact shear \(\eta\) can sharply lower finite-scale connector cost and is the remaining escape mechanism; it must either be excluded by regular bolt/interior matching or charged before the selected section.
4. *Conformal-infinity face escape.* Status: the face flow from \(E(q)\) has been computed and shows no return (Step 25, floating); a validated no-return proof is open.

Scale-separated ALE concentration (\(\mathfrak b_+\)), large-volume nonstandard-CR escape (Lemma P) and post-Rossi product/ALF collapse (Euler flux) are already excluded.

*Step-31 revision of (ii) — three inputs.* The chiral identities hold pointwise in \(t\), which yields the charge-variation bound Lemma V:
\[
\widehat P\ge\int\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt,
\qquad
\widehat P\ge\sup_t\max\{\mathfrak b_+(t)-1,\ \mathfrak b_-(t)-7\}.
\]
Here \(\mathfrak b_-=\sum w_i^2-\prod w_i-2\) with \(w_i=a_i'+\gamma_i\), and the bolt charges are \((1,7)\). Two consequences follow. Any round passage costs at least \(1-o(1)\). The raw \(\Delta\eta=-8\) entry has \(\mathfrak b_-=8.5496\), so its bolt prefix alone costs at least \(1.5496\).

Mechanisms 1 and 3 therefore reduce to **(N) non-round late opening**: after a collapsed section, \(\mathfrak b_+\) must stay below \(-1\) until CH shape is reached at \(\tau>0.70\). Constrained collocation (`SAT_BPMAX`) gives non-round values \(6.48\) (cap \(-1\), \(\varepsilon=1/16\), two warm starts; \(N=80\): \(6.44\)), \(5.37\), \(6.55\) and \(6.62\) at \(\varepsilon=1/4,1/32,1/64\), and \(4.03,4.81,5.50,7.89,11.87\) for caps \(1,0,-.5,-1.5,-2.5\). These costs are paid mainly in the \(D\) channel and not by charges.

Lemma N (independently verified, Step 32, and by S1003A01) shows that in the scalar-normalized class \(s\equiv-24\) the \(H\) channel is the Hamiltonian-constraint residual \(\mathcal C=\sigma_2(y)-6-R^{(3)}/2\), with \(\widehat P\supset\int W\mathcal C^2/3\). The normalization is not a literal preservation of the exact CH collar: the exact-ended diagonal infimum equals the scalar-\(-24\) infimum over metrics asymptotic to the marked standard CH end at rate \(>4\), followed by Theorem-T truncation; the bolt radius becomes \(u(0)b\). Lemma N also gives \(\mathcal C'=-2S\mathcal C-\sum(S-y_i)e_i\) and \(S'=18-S^2+R^{(3)}+\mathcal C\). Lemma W (last-crossing proof, repaired Step 33) uses these identities to supply the \(\int W^{-1}\) volume comparison wherever \(R^{(3)}\ge-\rho_0\), \(\rho_0<18\). The constrained collocation values above are feasible paths returned by a local optimizer, not lower estimates.

*Steps 33–34 additions.* Lemma V is exhausted as a static tool for (N): in scale-free jet coordinates \(\mathfrak b_+=2-|u|^2-\prod u\) depends on \(u=a'-\gamma\) only, an explicit path from the collapsed jet \((1,1,-2)\) to the CH jet \((3\sinh^2\tau,0,0)\) makes \(\mathfrak b_+\) monotone, and joint minimization finds triaxial never-round paths with \(\int\max(0,d\mathfrak b_+,d\mathfrak b_-)\approx0.02\) (Lemma Z). The exact control minimization goes further: for \(V=\mathfrak b_++\phi(q,\eta)\), SymPy gives \(\sup_{\bar H,\bar E,\bar D}(\dot{\mathfrak b}_+-L)\equiv0\), so the HJ condition is \(\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le0\). A sampled convex search on the cap-\(-1\) swap trajectories gives zero gain for every quadratic \(\phi(q,\eta)\); \(K\) changes sign from about \(-3.34\) to \(4.46\). Thus decorating the already exact chiral calibration by \((q,\eta)\) does not expose the missing cost. The stronger next structure is S1003A01's exact canonical almost-Kähler identity
\[
\widehat P-1=12H+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N+\Sigma,
\]
whose only negative term is Nijenhuis energy and whose transport/Hardy estimate makes the far zone nonnegative. An independent check confirms the coefficients but also shows that the certified subunit cells realize a genuine negative compact middle-zone mode; this route should determine a sharp subunit lower value and near-extremal mode (or a unit bound only under additional coercive hypotheses), not contradict the certified metrics. The unresolved inequality is the lowest coupled compact action for the forced bolt Nijenhuis charge, conformal factor, and \(W_3^+\) transport. Paths: `notes/step34_characteristic_constraint_calculus_and_N_probe.md`, `scripts/hj_symbolic_reduction.py`, `data/saturation_control/hj_qeta_probe.json`, and `Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md`.

*Step-35 addition (calibration and leaves).* Since \(\dot{\mathfrak b}_+\) is affine in the controls and \(\sup_c(\dot{\mathfrak b}_+-L)\equiv0\), one has exactly \(L(c)-\dot{\mathfrak b}_+=L(c-c^*)\), so \(\widehat P=\Delta\mathfrak b_++\int L(c-c^*)\) with positive-definite weight (no kernel defect); calibrated curves are the ASD scalar-flat diagonal metrics (Burns yes; Taub-bolt and CH no). Calibrated leaves from the collapsed entry converge to the Euclidean round fixed point (transverse eigenvalues \(-2,-4\)); backward leaves from all CH jets stay in the invariant biaxial set \(\Sigma=\{q=\eta=0\}\) and blow up without approaching the collapsed set. The endpoints are therefore leaf-separated in the antisymmetric pair \((q,\eta)\), reachable only through \(\bar D\) — the structural origin of the \(D\)-dominance. The exact transverse block on \(\Sigma\) is attracting on 38% and saddle on 62% of sampled \(\Sigma\cap\{\mathfrak b_+\le-1\}\), so no frozen argument excludes a cheap connector: (N) lacks path weight, not kernel or separation. It is recorded as a numerical-margin input. The proposed route is to match the \(\mathfrak b_+\) calibration on the swap band with S1003A01's CH-renormalized \(B\) (\(B_{\rm bolt}=1,B_{\rm CH}=2\)) on the tail. Paths: `notes/step35_calibration_theorem_and_branch_classification.md`, `scripts/calibrated_flow_leaves.py`, `scripts/transverse_block.py`.

**(L) large bolt:** the Einstein separatrix has an exact face limit, with \(d/b\to0.90535\), \(\rho\sim1.345b\), and the Rossi offset \(\log b\) produced at \(W\asymp b^2\). Shadowing together with Lemma P therefore predicts cost \(\gtrsim b^2(\log b)^2\). **(F)** conformal-face escape is analysed on the same \(\zeta=0\) face. Path: `notes/step31_charge_variation_constraint_pinning_nonround_opening.md`.

*(iii) Zero \(\Rightarrow\) Einstein.* Under (ii), \(p^{\rm diag}_{1,0}\) is attained. If \(p^{\rm diag}_{1,0}=0\), the minimizer is an Einstein metric of this type. Hence
\[
p^{\rm diag}_{1,0}>0\iff \text{no standard-CR diagonal Einstein filling of } O(-1).
\]

*(iv) Expected route to positivity.* Positivity would follow from \(\rho\neq1\) along all Einstein separatrices. Floating fate maps give \(\rho\ge2.19\) on ACH1 and its mirror \(\rho\le1/2.19\) on ACH2 at the sampled \(b\in\{.14,.2,.35,.8,2,20\}\) (minimum near \(b=.8\)), with \(\rho\sim0.8/b\) as \(b\to0\). This requires interval fate enclosure and large/small-\(b\) asymptotics.

### 4.2 Kernel-direction neck response — Exact reduced calculation; general remainder open

The calibrated neck density is
\[
x_0^2\left[\frac{(v_s+2v-3)^2}{4}-6v\right],
\]
with minimum \(-18x_0^2\) at \(v=9/2\). The exact constant-mode expansion gives the common minimizer \((C_1,C_2,C_3)=(9/4,3/4,1/2)\) for \(P\) and \(J\), predicting
\[
\frac{P}{8\pi^2},\frac{J}{8\pi^2}
=1-9x_0^2\log(1/x_0)+O(x_0^2).
\]
The coefficient and cancellations are exact in the reduced family; a uniform error estimate for general bulk metrics remains open.

Primary paths: `workspace/scripts/o11_neck_density_sympy.py`; `workspace/scripts/o11_perp_logneck.py`; `workspace/data/o11logneck/`.

### 4.3 Explicit subthreshold cells — Certified

The exact-dyadic \(x_0=0.01, X=8\) cell satisfies
\[
P/(8\pi^2)=0.999108702733592648\ldots,
\qquad
J_6/(8\pi^2)=0.999116243135324311\ldots
\]
with pure-Arb enclosures and exact bolt/collar matching data. The stronger area-selected \(x_0=3/100, X=64\) cell satisfies
\[
P/(8\pi^2)\in[0.9958484075845568,0.9958484075911518],
\]
\[
J_6/(8\pi^2)\in[0.9958546908532724,0.9958546908569237].
\]
The authoritative Step-33 extension to \(X=128\), degree 20, has the sharpened exact-dyadic Arb enclosure
\[
P/(8\pi^2)\in[0.995662732753254329\ldots,0.995662732771114200\ldots],
\]
\[
J_6/(8\pi^2)\in[0.995670030344086466\ldots,0.995670030355130639\ldots].
\]
Thus the isolated blow-up cost can be strictly below \(8\pi^2\) in negative Kähler--Einstein bulk. The area/collar sweeps suggest a finite-radius preferred scale, but do not prove existence or uniqueness of a complete-cell minimizer.

Primary paths: `workspace/data/o11_strict_arb_x001_X8_256.json`; `workspace/notes/step11_subthreshold_perpendicular_cell.md`; `Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X64_d16.json`; `Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_{P,J,S}_exact.json`.

## 5. Cell infima, handles, and balanced upper bounds

Let \(\mathfrak P_{k,\ell}\) and \(\mathfrak J_{k,\ell}\) denote infima over smooth marked cells of topology \(D\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)\), exact CH on an outer collar, with radius allowed to vary.

### 5.1 Subadditivity and balanced specific energy — Proved at construction level

Disjoint placement gives subadditivity and therefore
\[
\gamma_{\rm bal}=
\lim_{n\to\infty}\frac{\mathfrak P_{8n,7n}}{72\pi^2n}
=\inf_n\frac{\mathfrak P_{8n,7n}}{72\pi^2n}.
\]
This does not identify \(\gamma_{\rm bal}\) with the unrestricted closed-manifold \(\alpha\)-coefficient.

### 5.2 Pure handles — Proved sharp infimum

\[
\mathfrak P_{0,\ell}=\mathfrak J_{0,\ell}=32\pi^2\ell.
\]
For \(\ell>0\), the value is approached by shrinking cores and is not attained by a fixed smooth cell. Mixed-cell nonadditivity remains open.

### 5.3 Balanced sequence — Proved existential upper construction

Residual-finite covers provide disjoint placements, exact-collar smoothing has arbitrarily small loss, and the certified \(x_0=3/100, X=128\) blow-up cell together with the pure-handle construction yields a suitably selected balanced family with
\[
\limsup \alpha(M_j)/h_j<3.9961512+\varepsilon.
\]
This is not a statement for every prescribed cover sequence and does not determine the sharp coefficient. The separated bookkeeping is \(28/9+(8/9)p_{1,0}\), not \(4p_{1,0}\).

## 6. A complete nonstandard-boundary Einstein filling (Theorem E)

### 6.1 Theorem — Proved by analytic local construction and validated flow

There exists a complete real-analytic diagonal Bianchi--IX metric on the total space of \(\mathcal O(-1)\to\mathbb{CP}^1\) satisfying \(\operatorname{Ric}=-6g\). It is ACH with fibre slot 1 and convergence rate at least \(O(e^{-1.99t})\). Its conformal infinity is a nonstandard Rossi sphere with
\[
\rho_\infty\in[2.19013,2.19242].
\]
The bolt has \(b=4/5\), while the free fourth-order anisotropy lies in the validated interval used by the Fuchsian/CAPD passage.

Proof components: analytic Fuchsian solution in \(s=t^2\); exact constraint propagation; source-level equivalence of the compact CAPD vector field and the Einstein system; interval transport of a tiled bolt family to a verified cusp block; opposite unstable-face crossings; Ważewski continuation; and quadratic drift control of
\[
\widetilde\Phi=q+\frac{y_g-y_h}{4}-\zeta\sinh q.
\]

Primary paths: `workspace/notes/step15_ach_projected_theory.md`; `workspace/scripts/ach_bolt_fuchs.py`; `workspace/data/ach_capd/fuchs_boxes_N6_complex.json`; `workspace/scripts/ach_capd_field_check.py`; `workspace/data/ach_capd/wazewski_T2.75.json`; `workspace/scripts/ach_block_verify.py`; `workspace/scripts/ach_phi_drift.py`; `workspace/data/ach_capd/rossi_enclosure_b0.8.json`.

### 6.2 Exact bolt geometry — Proved

At \(b=4/5\), the scalar curvature is \(-24\). The earlier values \(\operatorname{diag}(-139/16,57/16,41/8)\) and \(\operatorname{diag}(-385/16,203/16,91/8)\) were produced by a symbol-collision bug in the peer script (peer message 771) and are withdrawn. The repaired exact computation, which agrees with the independent coordinate limit (operator norms \(39.3985\), \(194.083\)), gives the unordered chiral curvature-operator Weyl blocks
\[
\operatorname{diag}(-41/16,-41/16,41/8),
\qquad
\operatorname{diag}(-91/16,-91/16,91/8),
\]
   Neither bolt block has the Kähler--Einstein spectrum. More strongly, the CAPD off-bolt calculation now transports all forty outward-rounded analytic Fuchsian boxes to \(t=.5\) and proves that both chiral Weyl blocks have simple spectrum there. The weakest pairwise gap lower bounds are \(0.9669947784\) and \(0.003926698448\), and the discriminant lower bounds are \(66.1883\) and \(0.0006333125\). A point-box comparison with the independent coordinate/JAX curvature calculation agrees within \(5.6\times10^{-15}\). Thus the metric is not conformally Kähler on any nonempty open set in either orientation; analyticity excludes an open conformally Kähler region after the discriminant is nonzero at the certified orbit.

Primary paths: `Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_exact.py`; `workspace/scripts/ach_bolt_weyl_series_check.py`; `workspace/scripts/ach_weyl_interval.cpp`; `workspace/scripts/ach_weyl_interval_run.py`; `workspace/data/ach_capd/weyl_discriminant_t0.5.json`.

### 6.3 Relation to the marked-cell problem

Theorem E changes the boundary CR structure and therefore is not an exact-CH-collar zero-cost cell. The certified cheap cells also do not shadow this Einstein trajectory: their positive action is concentrated near a Burns-like core and their collar returns rapidly to CH. The theorem supplies a possible compactness endpoint and an existence result, not a proof that \(p_{1,0}=0\).

The Biquard--Herzlich identity places the convergent combined curvature integral against \(\chi-3\tau+\nu\). For the blown-up ball \(\chi-3\tau=5\); the standard sphere value leaves slack, so topology does not exclude a standard-boundary filling. Numerical branch-wide nonexistence at \(\rho=1\) remains open and would be dynamical even in the diagonal class. The off-bolt conformal-Kähler question is now closed by the interval theorem in §6.2.

## 7. Common mechanism and its present mathematical scope

The proved pieces support the following schema. Actual metric-wise fields and their differential prolongations control regular bulk geometry. A topology change is realized by a complete marked cell whose leading response depends on the ambient self-dual curvature, not solely on the topology. Kernel directions can evade the linear payment and exploit a negative quadratic interaction. Volume entropy supplies a separate field-free obstruction to exact Einstein metrics on real-hyperbolic blow-ups. Pure handles retain the exact \(32\pi^2\) cost, while blow-ups admit certified costs below \(8\pi^2\) in CH bulk. Exact Einstein filling can occur after moving the CR boundary away from the standard CH value. The unrestricted \(\alpha\)-problem requires a compactness/localization theorem linking global near-minimizers to these bulk and cell objects.

The general-bulk first-order law is now proved as an upper construction (Theorem F). Still open: the full \(-9\) remainder, positivity of \(p_{1,0}\), equality of global and cell asymptotics, standard-CR diagonal nonexistence, and a universal degeneration theorem. Two rigid inputs constrain degeneration. First, an almost-Euclidean neck enclosing a blow-up class carries \(P\ge8\pi^2-C\varepsilon\), and a scalar-flat ALE bubble with \(\Gamma=1\) carries \(P\ge8\pi^2(k+4\ell)\). Second, no nontrivial exact-CH-collar cell is Einstein: the locally symmetric developing-map argument removes the temporary \(\ell=2k\) exception. Hence \(\mathfrak P_{1,0}<8\pi^2\) forbids almost-flat concentration of the class, and \(\mathfrak P_{k,\ell}=0\) for any \((k,\ell)\ne(0,0)\) requires escape of the collar, collapse, or concentration through curved necks.

The real-hyperbolic contrast now has two theorems beyond the numerical scan. On closed \(Y\#k\overline{\mathbb{CP}}^2\) with \(s=-12\), a Ricci floor \(\operatorname{Ric}\ge-3(1+\varepsilon)g\) gives
\[
P\ge8\pi^2k-12\operatorname{Vol}(Y)[1-(1+\varepsilon)^{-2}]
\]
by BCG entropy and Bishop comparison. For a complete exact-\(H^4\)-exterior cell, the scalar floor \(s\ge-24\) forces the manifold to be hyperbolic by the non-spin Chruściel--Delay positive-energy theorem in dimension four. Details and sources are in `workspace/notes/step22_hyperbolic_volume_mass_and_weyl_certificate.md`.

**Two-channel cell identity (Theorem C, Steps 23–24).** For a complete cell of marked topology \((k,\ell)\), exactly equal to the model outside a compact set for a fixed end marking, with Yamabe representative \(\hat g=u^2g\), \(\hat s=-24\), \(u\to1\) (derivative decay faster than inverse volume growth),
\[
P_{\rm cell}-8\pi^2(k+4\ell)=4\Delta W_++48\,\mathrm{RV}(\hat g)+3\int(\Delta u/u)^2+24\int|\nabla u|^2,
\]
where \(\mathrm{RV}\) is the matched relative volume: matched truncations of cell and model plus the whole-cell integral \(\int(u^4-1)d\mu_g\). For exact-CH ends \(u\) exists uniquely for **every** smooth cell (S1003A01 weak-barrier theorem, no sign condition on \(s\)), so the exact-ended \(J_6\) infimum equals the \(P\) infimum over complete scalar \(-24\) metrics asymptotic to the marked CH end at rate \(>4\). The H\(^4\) cell bound \(P\ge8\pi^2\) is reduced to \(\mathrm{RV}(\hat g)\ge0\). Numerically (11 diagonal cells, both bulks, \(x_0\le1\)) \(\mathrm{RV}(\hat g)>0\) always; \(48\mathrm{RV}\approx-x_0s_p/12\) and \(4\Delta W_+\approx-x_0W^+_p(\zeta,\zeta)\) to first order: the two halves of \(\mathbf R^+\) in Theorem F are the volume and Weyl channels. The certified CH witness pays \(+0.0706\) in volume and saves \(-0.0747\) in Weyl (units \(8\pi^2\)). The scalar floor does not separate the two bulks (both families of competitors dip below the background scalar); the Weyl channel does. Relative signature for the one-blow-up CH cell gives \(\Delta W_+-\int|W^-|^2=-12\pi^2\); at \(P=0\) Theorem C then reproduces the relative Biquard–Herzlich identity, \(\mathrm{RV}=5\pi^2/6-\int|W^-|^2/12\), so these identities alone give no obstruction to a standard-CR Einstein filling.

**Monopole estimates give no per-blow-up cell payment (Step 24).** For minimal general type \(X\), LeBrun's convex invariant satisfies \(\beta^2(X\#k\overline{\mathbb{CP}}^2)=c_1^2(X)\), independent of \(k\): averaging the monopole classes \(\pm c_1(X)\pm E_1\pm\cdots\pm E_k\) puts \(c_1(X)\) in the convex hull, and scalar-recovery metrics give the reverse inequality (`Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md`). Thus \(\int s^2\) and \(\int(s-\sqrt6|W_+|)^2\) see only the minimal model; the \(k\)-dependence of \(8\pi^2(k-A/3)\) enters only through \(\chi,\tau\) in Chern–Weil. Positivity of \(p_{1,0}\) must come from intrinsic Weyl–volume geometry, not from localizing a Seiberg–Witten estimate.

## 8. The missing global passage

**Steps 33–34: characteristic–constraint link calculus (proved identities and corrected consequences).** For every compact \(\Omega\subset M\) with smooth boundary,
\[
\widehat P(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2+\frac1{96\pi^2}\int_\Omega s^2-(2\chi\pm3\tau)(\Omega)+\mathcal Q_\pm(\partial\Omega),\qquad\mathcal Q_\pm=2\mathcal E\mp3\mathcal H,
\]
with \(\mathcal E\) Chern's boundary term and \(\mathcal H=\eta+\int T_{p_1}\) the APS boundary term (Theorem G). Verified model charges are: round flat-conical link \((2,2)\); flat-conical/ALE \(S^3/\Gamma\) limit \((2/|\Gamma|\mp3\eta_\Gamma)\), recovering Lemma Q; a fixed-smooth-metric thin tube around a surface of self-intersection \(n\), \((2\chi(\Sigma)\pm3\operatorname{sgn}n)\), giving the bolt \((1,7)\); the controlled Taub–NUT-chirality Hopf-adiabatic link \((-2,2)\), with the opposite chirality \((2,-2)\); and the CH sphere \((2-9\sinh^4\tau,2-3\sinh^4\tau)\). The radial collar jet is part of every charge. For \(D\cong(\#k_D\overline{\mathbb{CP}}^2\#\ell_D S^1\times S^3)\setminus B^4\),
\[
P(g)\ge8\pi^2[k_D+4\ell_D-(2-\mathcal Q_+(\partial D))].
\]
Disjoint regions add. For one blow-up with \(\widehat P<1-\varepsilon\), a standard negative-definite blow-up region has \(\mathcal Q_+\le1+\widehat P<2-\varepsilon\); therefore an exceptional subtree cannot be separated from the bulk by a \(C^2\)-Euclidean-round \(S^3\) germ. This does not exclude orbifold necks, Taub–NUT-chirality collapse, curved/sheared links, bulk bubbling, or regions containing positive intersection form.

The complementary symmetry-free foliation identity is
\[
|\operatorname{Ric}^\circ|^2=\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2,
\quad
\mathcal C=\tfrac12(\Theta^2-|K|^2-R_h)+s/4,
\quad
\mathcal J=\operatorname{div}K-d\Theta,
\]
where \(\mathcal S\) is the trace-free tangential evolution residual. Lemma N is the diagonal Hamiltonian component; Lemma P and fibre/base pinning use the two diagonal tangential-evolution projections, not the Codazzi component. Exact transport identities tested against \((\mathcal C,\mathcal J,\mathcal S)\) give weighted Cauchy–Schwarz lower bounds. Thus characteristic transgressions price topology and boundary-germ changes, while Gauss–Codazzi/evolution residuals price drift-corrected shape changes. Their bounds are generally combined by a maximum unless regions or orthogonal components are separated. **Link regularity** is control/convergence of the intrinsic link geometry, second fundamental form, characteristic and Dai spectral transgressions, and the field boundary data actually used on the bulk. Critical \(L^2\) defect alone does not establish it. Details: `notes/step33_link_charges_global_decomposition_static_channel.md`, `notes/step34_characteristic_constraint_calculus_and_N_probe.md`, and the Step-34 TTCS integrations.

The classical handle-free lower interval is
\[
8\pi^2\max\{0,k-A/3\}\le\inf P\le8\pi^2k,
\]
so present lower information vanishes for \(0<k<A/3\). A successful global passage must do more than extract an ideal limit: it must preserve family-uniform scale control, distinguish collapse from noncollapsed convergence, identify the CH bulk through actual-field coercivity, assign topological charge to complete bubbles or cells, and compare asymptotically CH cells with exact-collar infima by truncation.

On the scalar-minus-four class, put
\[
R_1(g)=\int_M|\nabla\operatorname{Rm}_g|^2\,d\mu_g.
\]
If \(P(g_0)\le p+\delta\), \(0<R_1(g_0)<\infty\), \(\varepsilon=\delta/R_1(g_0)\), and \(g\) is a \(\delta\)-near-minimizer of \(P+\varepsilon R_1\), then the elementary comparison proves
\[
P(g)-p\le3\delta,\qquad R_1(g)\le3R_1(g_0).
\]
This selection lemma is valid and needs neither an attained minimum nor a gauge. It does not yet give a uniform compactness theorem: the comparison \(g_0=g_0(\delta)\) may have \(R_1(g_0)\to\infty\), the certified upper construction is not known to be \(\delta\)-close to the unknown infimum for arbitrarily small \(\delta\), and an intrinsic derivative-curvature bound gives a uniform \(L^4\) bound only after a uniform Sobolev or harmonic-radius input. Across the balanced family, even an extensive bound \(R_1=O(A)\) permits scales of order \(A^{-1/2}\) and is not local equiintegrability. The corrected statement and the independent reading of Theorem E are in `workspace/notes/step19_theorem_package_and_selection_lemma.md`.

## 9. Highest-return next theorems

1. Prove positivity of the absolute cell channel \(\inf\{8\pi^2+4\Delta W_++48\mathrm{RV}(\hat g)\}>0\) over complete scalar \(-24\) metrics asymptotic to the standard marked CH end on \(O(-1)\). (The earlier linear trade-off \(4\Delta W_+\ge-\Lambda48\mathrm{RV}-\eta\), \(\Lambda\in[1.03,1.06]\), is withdrawn: \(\Lambda\to1\) is forced by Theorem F in the kernel direction and \(\Lambda>1\) gives no absolute bound.) The first complete form of this is the diagonal compactness/trichotomy theorem of `workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md`.
2. Real-hyperbolic: prove \(\mathrm{RV}(\hat g)\ge0\) for \(\hat s\equiv-24\) AH metrics on \(D\#k\overline{\mathbb{CP}}^2\) conformal to exact-collar metrics (local topological Schoen problem), and on the closed side the identity \(\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}\), which is now the only input missing from the sharp theorem H.
3. Study the regularity profile \(\mathcal R_*(\delta)=\inf\{R_1(g):P(g)\le p+\delta,\ s_g=-4\}\), and either bound it uniformly or derive a local Sobolev/harmonic-radius estimate from the penalized equation with constants that survive \(\varepsilon\to0\).
4. Use actual-field coercivity to identify a noncollapsed bulk and localize topological charge; separately analyze collapse and the entropy/Ricci critical-exponent obstruction.
5. Prove truncation equivalence between asymptotically CH complete cells and exact-collar cell infima; determine whether \(p_{1,0}>0\) and whether global near-minimizers decompose into cells at that cost.
6. Analyze the exact-standard-CR endpoint in and beyond the diagonal class. Theorem E now has certified non-conformal-Kählerness, but its Rossi boundary remains nonstandard.

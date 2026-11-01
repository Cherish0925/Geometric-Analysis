# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/codex_loop/work/proved_vs_open.md",
    "Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md",
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Review the monopole-amplitude/eigenline transfer needed after selecting bounded-curvature exponential pullback charts in the fixed critical Ishida-LeBrun sequence. Use the exact quantitative deficit decomposition in the Codex report. Suppose at an evolved time one has global Q=∫|Ric+g|²→0 and hence the scalar-Weyl completion-square profile, and suppose bounded sectional curvature plus derivative estimates hold on a positive-volume buffered set P. Identify a single nonnegative density or finite family of densities whose small global integrals and exponential-chart averaging would guarantee on one pullback chart: (i) a quantitatively nonzero limiting harmonic self-dual form, (ii) lowest-W+ eigenvalue saturation, and (iii) enough compactness to pass these to a local Einstein limit. Carefully distinguish harmonic representative H_a, spinor quadratic form ψ/φ, the fact the selected sign class may depend on metric/time, and any equations not preserved by cutoff flow. Decide whether the existing identities actually make such joint chart selection possible, or expose an exact missing estimate. Do not use unique continuation as a substitute for quantitative local amplitude.

## Output

## Verifier memo — chart transfer of the monopole amplitude/eigenline data on the exact critical Ishida–LeBrun family

### 1. What the deficit family actually delivers, and in what norm

The quantitative decomposition in `quantitative_deficit_analysis.md` is a family of **global** integral inequalities for a **fixed metric** \(g\). Taking the optimal weight \(f=\sqrt q\), \(q=\sqrt6 w-s\), the controlling quantity is
\[
\Delta_a=\int_M(s-\sqrt6 w)^2-72\pi^2p,\qquad p=(a^+)^2 .
\]
I re-derived the algebraic backbone and it is correct: identity (18),
\(27(\tfrac{s^2}{24}+2w^2)-(s-\sqrt6w)^2=\tfrac18(s+8\sqrt6w)^2\), checks exactly, and the near‑saturation profile it forces (\(s\to-4\), \(w\to 1/(2\sqrt6)\), \(K\to A\), \(\mathrm{Vol}\to 32\pi^2A/9\), \(c_0=3/(4\sqrt2\pi)\) with \(c_0^2=9/(32\pi^2)=A/(32\pi^2A/9)\)) is internally consistent. The consequences you would use on a chart are all **integrals over \(M\)**:
\[
\|iF_A^+-2\pi H_a\|_2^2\le\tfrac{\Delta_a}{18},\quad
\int_M\!\big[W_+(\psi,\psi)+\sqrt{\tfrac23}w|\psi|^2\big]\le\tfrac{2\Delta_a}{27},\quad
\big\||2\pi H_a|-\tfrac{q}{3\sqrt2}\big\|_2\le 2\sqrt{\tfrac{\Delta_a}{18}} .
\]
With \(Q=\int|\mathrm{Ric}+g|^2\to0\) at the evolved time one has \(R=(8\pi^2)^{-1}\int|\mathrm{Ric}^\circ|^2\to0\), hence \(\Delta_a\le108\pi^2R\to0\), so every one of these integrals tends to \(0\). This is genuine and unconditional given \(Q\to0\).

The decisive point for chart transfer is that these are **integrals, not densities, and not scale‑invariant**. On the exact critical manifold the unit‑ball volume tends to \(0\) everywhere (this is exactly the content of Step 6’s (10)); a positive‑volume set carrying bounded curvature only becomes definitely noncollapsed after CFG unwrapping to a local cover, and the pullback multiplies a downstairs integral by the sheet number \(N_i=\mathrm{Vol}_{\text{cover}}/\mathrm{Vol}_{\text{down}}\to\infty\). A global integral \(\int_M(|H_a|-c_0)^2\le C\Delta_a\) pulled back to a unit‑volume cover ball becomes \(N_i\cdot\int_{B}(\dots)\), an \(\infty\cdot0\) quantity. So the raw integral statements do **not** survive the pullback; only **local means (densities)** do.

### 2. The transfer the existing identities do support

The transfer can be organized entirely through local means at a fixed radius \(r\), and this part works:

- **Averaging.** \(\mathrm{Ric}\ge -3\) gives Bishop–Gromov volume doubling up to scale \(\sim1\) with a dimensional constant. The uncentered maximal function is therefore weak‑\((1,1)\) with a uniform constant, so for the density \(a_{\mathrm{amp}}=(|H_a|-c_0)^2\) (which satisfies \(\int_M a_{\mathrm{amp}}=O(\Delta_a)\) after combining (17) with \(\|q-9/2\|_2=O(\delta\sqrt A)\) from (37)),
\[
\mathrm{Vol}\{x:\ \textstyle\fint_{B_r(x)}a_{\mathrm{amp}}>\eta\}\le \frac{C\Delta_a}{\eta}.
\]
Since \(\mathrm{Vol}(M)\) is fixed \(\approx 32\pi^2A/9\), the set of centers with small **local mean** at scale \(r\) has volume fraction \(\to1\), so it meets the positive‑volume set \(P\).

- **Isometric unwrapping preserves means.** CFG/Fukaya unwrapping of a collapsed bounded‑curvature ball is a local isometry, so \(|\pi^*H_a|(\tilde x)=|H_a|(\pi\tilde x)\) and \(\fint_{\tilde B_r}(|\pi^*H_a|-c_0)^2=\fint_{B_r}(|H_a|-c_0)^2\le\eta\). \(\pi^*H_a\) is again closed, coclosed and self‑dual for the pulled‑back metric.

- **Local‑mean → pointwise.** On the noncollapsed cover ball, a uniform Hölder bound \([\pi^*H_a]_{C^\alpha}\le L\) turns a small mean square deviation into a pointwise lower bound: a point with \(|\pi^*H_a|<c_0/2\) would force \(\fint_{B_r}(\dots)^2\ge (c_0^2/16)v(\rho/r)^4\) with \(\rho=(c_0/4L)^{1/\alpha}\), contradicting \(\eta\to0\). This is exactly the mechanism of statement (40) in §5, but run at the cover’s **preserved mean** rather than the raw global integral.

So (i) — a quantitatively nonzero limiting harmonic self‑dual form — is obtainable **provided** the noncollapse and Hölder inputs hold on the cover at the same radius \(r\) at which the mean is small.

### 3. A single density does not exist; the usable finite family does

There is **no** pointwise nonnegative density whose integral equals \(\Delta_a\). The monopole term \(72\pi^2p\) is a cohomological \(L^2\)-norm of \(H_a\), a global number; and in the exact decomposition (9)/(12) the two Hölder gaps \(H_1,H_2\) and the conformal value gap \(D_{\mathrm{conf}}\) are themselves **global** functionals with no pointwise integrand. Those objects therefore cannot be localized to a chart at all. Fortunately they are not needed for (i)–(iii).

The transfer instead reduces to a **finite family of genuine densities**, each with global integral \(\le C\Delta_a\), whose small local means at scale \(r\) give the three conclusions:
\[
a_{\mathrm{amp}}=(|H_a|-c_0)^2,\quad
a_{\mathrm{proj}}=|iF_A^+-2\pi H_a|^2,\quad
a_{\mathrm{eig}}=W_+(\psi,\psi)+\sqrt{\tfrac23}w|\psi|^2,\quad
a_{\mathrm{Ein}}=|\mathrm{Ric}+g|^2,
\]
(optionally \(a_{\mathrm{grad}}=|d\psi|^2+|d\rho|^2\) for regularity). Because each has full‑volume‑fraction good set (via §2), a **single** center in \(P\) with all four means small exists for \(\delta\) small — provided the geometric inputs below are met. This is the honest form of the density family the task asks for: a finite family of local‑mean densities, not one pointwise scalar.

### 4. \(H_a\) versus \(\psi/\varphi\), and where (ii) is genuinely weaker

Conclusion (i) uses only \(a_{\mathrm{amp}}\), built from the **canonical** \(g(t)\)-harmonic representative \(H_a\); it inherits metric continuity and elliptic regularity directly. Conclusion (ii) is structurally different: \(D_{\mathrm{eig}}\) controls the **spinor** quadratic form \(\psi=2\sqrt2\,\sigma(\Phi)\), not \(H_a\). The passage to \(H_a\) is a two‑step chain: \(a_{\mathrm{eig}}\) puts \(\sigma(\Phi)\) (hence \(-iF_A^+=f\sigma(\Phi)\) up to the weight) in the lowest \(W_+\)-eigenline, and \(a_{\mathrm{proj}}\) (\(J_A\to0\)) identifies \(iF_A^+\) with \(2\pi H_a\). Two things attach to this chain and must be flagged:

- The report itself states that the optimal weight \(f=\sqrt q\) is only Lipschitz at the zero set of \(W_+\), so there is **no canonical monopole**; (13)–(17) hold only along a **regularized sequence** \(f_k\to\sqrt q\) with a different \((\Phi_k,A_k)\) for each \(k\), and “they do not assert convergence of a canonical sequence.” Hence \(a_{\mathrm{proj}},a_{\mathrm{eig}}\) are \(k\)-dependent, and the good chart center from §2 is a priori \(k\)-dependent. A single center good for the \(k\to\infty\) limit needs a diagonal/uniform estimate that is asserted (§6, Step 6 “choose diagonally”) but not quantitatively supplied.

- \(a_{\mathrm{eig}}\) contains \(W_+(\psi,\psi)\); transferring its mean to the cover and reading off the two‑eigenvalue spectrum needs \(W_+\) to converge on the cover, i.e. the same cover regularity as in (i).

So (ii) rests on (i)’s geometric inputs **plus** regularization uniformity. This distinction is real and the notes blur it when they treat the eigenline conclusion as coming “from the L² chain” — the L² Weyl‑modulus estimate (Step 15 Th. 1(d), constant \(7/24\), which I confirm arithmetically) fixes only \(|W_+|\); the extremal determinant \(\det W_+=-|W_+|^3/(3\sqrt6)\) needed for the germ comes precisely from the monopole \(a_{\mathrm{eig}}/a_{\mathrm{proj}}\) alignment, i.e. from the spinor, not from \(|W_+|\).

### 5. The exact missing estimate

Given §2–§4, joint chart selection reduces to inputs the current notes do **not** establish quantitatively:

**(G‑scale) A single radius \(r\), uniform in \(i\), at which the cover is definitely noncollapsed with a definite \(C^{1,\alpha}\) harmonic radius.** The maximal‑function selection produces small local means at a **fixed** scale \(r\); the Hölder‑to‑pointwise step needs, on the cover ball of that same radius \(r\), (a) \(\mathrm{Vol}\,\tilde B_r\ge v r^4\) and (b) a uniform elliptic (harmonic‑radius) bound for the Hodge Laplacian so that \([\pi^*H_a]_{C^\alpha}\le L\) and \(W_+\) converges. CFG bounded curvature gives noncollapse on the cover but **not** a lower harmonic‑radius bound tied to \(r\); nothing in the notes prevents the plateau/bounded‑curvature scale and the collapse scale from pinching together as \(\delta_i\to0\), in which case no fixed \(r\) survives and the mean‑preservation argument has no cover ball to land on. This is the precise estimate to isolate: *a scale‑matched cover noncollapse with uniform \(C^{1,\alpha}\) harmonic radius \(r_h^{\text{cover}}\ge r_0>0\) at a radius \(r\) where \(\fint_{B_r}\{a_{\mathrm{amp}},a_{\mathrm{proj}},a_{\mathrm{eig}}\}=o(1)\).* Equivalently in raw terms, the transfer needs \(N_i\,\Delta_a\to0\) (collapse depth × deficit) at the working scale; no bound relating collapse depth to \(\delta_i\) is present.

**(G‑reg) Uniformity across the weight regularization** for the two spinor densities \(a_{\mathrm{proj}},a_{\mathrm{eig}}\) (§4).

These two are the load‑bearing missing pieces. Everything else (doubling, mean preservation, Hölder upgrade) is in hand.

### 6. Conclusion (iii) does not come from \(Q\)

The Einstein‑limit compactness is not delivered by \(Q\to0\): \(a_{\mathrm{Ein}}=|\mathrm{Ric}+g|^2\) is again only a global integral, and on collapsed balls its density is not controlled by \(\int_M a_{\mathrm{Ein}}\) without the same doubling/scale argument. What actually gives (iii) is the **pointwise** plateau estimate \(\sup_P|\mathrm{Ric}+g|\le C_\theta\delta\) (Li Cor 3.5, the load‑bearing conditional of Step 15 §7 Demand C). Since the task hypothesis supplies “bounded curvature + derivative estimates on \(P\)” together with that pointwise plateau defect, (iii) is available on \(P\); but it must be sourced from the pointwise estimate, not from the \(L^2\) profile. If one leans only on \(Q\), (iii) inherits the same collapse‑depth obstruction as (i)–(ii).

### 7. Cutoff‑flow / snapshot and sign‑class remarks

- The Seiberg–Witten equations \(D_A\Phi=0,\ -iF_A^+=f\sigma(\Phi)\) and the deficit identities (5),(9),(12)–(17) are **snapshot** statements: they are algebraic/integral consequences of SW + Weitzenböck for whatever metric is present, so they hold at the evolved \(g(t)\) — but \(H_a(t)\), \(\Phi,A\), and \(W_+\) must be **recomputed** at \(g(t)\); one cannot transport the \(t=0\) monopole through the flow. Off the plateau the cutoff flow \(\partial_t g=-2\chi^2E\) is not Ricci flow and carries no Weitzenböck monotonicity, so there is **no** propagation of \(a_{\mathrm{proj}},a_{\mathrm{eig}},a_{\mathrm{amp}}\) in time; all of (i)–(iii) must come from the single snapshot at the evolved time. This is consistent with the notes but should be stated: the profile (5)–(7) and \(K\ge A\) are Chern–Gauss–Bonnet/monopole‑invariant facts, hence snapshot‑valid, so the reliance on the snapshot is legitimate.
- **Sign class.** On the fixed critical manifold the sign cube is finite and fixed; the average deficit (31) \(\to0\) forces every individual fixed vertex deficit \(\to0\). So one may fix any single class \(a\) and drop the time‑dependence of the maximizing choice — there is no genuine per‑time selection problem here. (If \(A_i\to\infty\), only the average is controlled and a sparse set of vertices may not saturate; that regime is not the present one, and the notes correctly restrict the “every vertex saturates” statement to fixed topology in §9.)

### 8. Unique continuation is not a substitute

Step 15 §6(4) uses unique continuation to assert \(\omega_a\neq0\) a.e. This is purely qualitative: it forbids vanishing on an open set but gives **no** lower bound and **no** control of how small \(|H_a|\) can be on the chosen chart. In the phase‑separation scenario the topological mass of \(H_a\) is carried on a thin transition region and \(|H_a|\) on a given cover ball can be arbitrarily close to \(0\); unique continuation is silent about this. The quantitatively nonzero limit in (i) can come **only** from the \(a_{\mathrm{amp}}\) local‑mean transfer + cover noncollapse + Hölder (§2, §5), i.e. from (G‑scale). Any argument that reaches the germ contradiction by invoking unique continuation in place of a local amplitude density is not carrying the quantitative content, and the note’s summary tables should not mark “harmonic form nonvanishing — ESTABLISHED” on that basis.

### 9. Verdict

The exact deficit decomposition **does** make joint chart selection possible in principle, through a mechanism the identities already support: doubling‑based maximal‑function selection of a center with small local means of the finite family \(\{a_{\mathrm{amp}},a_{\mathrm{proj}},a_{\mathrm{eig}},a_{\mathrm{Ein}}\}\), mean preservation under isometric CFG unwrapping, and Hölder upgrade to pointwise amplitude and eigenline saturation. What is **not** in the notes, and is the exact estimate to isolate, is:

1. a scale‑matched cover noncollapse with a uniform \(C^{1,\alpha}\) harmonic radius at the same fixed radius \(r\) where the local means are \(o(1)\) — equivalently a collapse‑depth‑versus‑deficit bound \(N_i\Delta_a\to0\) at the working scale (this is what replaces the raw global integrals, which do not survive pullback); and
2. uniformity across the non‑canonical weight regularization for the spinor densities \(a_{\mathrm{proj}},a_{\mathrm{eig}}\).

With these, the calibrated germ contradiction closes — I verified its endpoint arithmetic independently: at \(s=-4\), \(\operatorname{Spec}W_+=(-\tfrac16,\tfrac1{12},\tfrac1{12})\), \(|W_+|^2=\tfrac1{24}\), \(\det W_+=-\tfrac1{864}\), the scalar identity gives \(|\nabla W_+|^2=\tfrac1{16}\), against \(\nabla W_+=0\) from the constant‑spectrum lemma. The germ step is sound; the unresolved substance is entirely the scale‑matched cover regularity/amplitude estimate above, and the Einstein‑limit input (iii) must be drawn from the pointwise plateau defect rather than from \(Q\).
# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A01/workspace/notes/step11_chart_accessibility_and_energy.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md"
  ]
}
```

## Task

Verify the Pontryagin localization mechanism for the four-dimensional negative-branch Yau 26 program.

1. VERIFY THE PONTRYAGIN DENSITY FORMULA: For a 4-manifold with curvature decomposition Rm = W⁺ + W⁻ + E + s, what is p₁(Λ²₊) as an integrand? Specifically, verify that on a region of regular fibered collapse (fiber dim d ≥ 1, base dim ≤ 3) where the self-dual forms are 'basic' (pulled back from the base), the contribution to ∫p₁(Λ²₊) = 8π²(2χ+3τ)/? vanishes or is constrained.

2. CHECK THE COUNTERMODEL: For the Taub-NUT-AdS metric with NUT parameter ν→0, verify:
   (a) The claim that the ψ-circle at distance 1/2 from the NUT is contractible in B₁.
   (b) The claim that the curvature |Rm|² remains bounded as ν→0 at fixed distance from the NUT.
   (c) Whether the maximal function bound ∫_{B_r}|Rm|² ≤ K₀·Vol(B_r) holds.

3. VERIFY THE WEITZENBÖCK COMPUTATION: For Einstein Ric=-g with calibrated W⁺ spectrum (-1/6,1/12,1/12), check that the Weitzenböck formula gives ∫|∇H|²/∫|H|² = 1 for the simple eigenform and 3/2 for the double eigenspace. Distinguish between the curvature-operator arrangement and the Weitzenböck R̃ arrangement.

4. CHECK THE DEFINITE-PAIR EXCLUSION: A03 claims flat rank ≥ 2 collapse is excluded. Verify the argument: two independent near-harmonic SD forms with locally nondegenerate Gram matrix, closedness, and constant amplitude → ∇ → 0, contradicting the Weitzenböck gradient energy. Is 'locally nondegenerate Gram matrix' automatic or an additional hypothesis?

5. ASSESS: Is the Pontryagin charge 4π²(A-k) correctly computed? Does basic collapse really contribute zero to this charge?

## Output

# Verification Memo: Pontryagin Localization, Taub–NUT–AdS Countermodel, Weitzenböck Energies

Prepared for the four-dimensional negative-branch program (S0910A03 step9, S0910A01 step8/step11). I checked the five requested items by re-deriving the underlying identities and cross-checking against the calibrated Einstein profile the program uses. Overall the numerical content is correct; two structural statements are stated more strongly than the mathematics supports, one interpretive sentence about the Weitzenböck endomorphism is inaccurate (with no effect on the numbers), and one physical assertion about the countermodel rests on an uncomputed uniform curvature bound. I also found a sharpening of the localization mechanism that the notes do not yet exploit.

---

## 1. Pontryagin density formula

**The identity is correct with the following normalization.** For an oriented Riemannian 4-manifold, the standard pointwise Chern–Weil representatives are

- Euler (Pfaffian): $e = \frac{1}{8\pi^2}\big(|W^+|^2+|W^-|^2+\tfrac{s^2}{24}-\tfrac12|E|^2\big)\,d\mu$, $\int e=\chi$;
- Signature (first Pontryagin of $TM$): $p_1(TM)=\frac{1}{4\pi^2}(|W^+|^2-|W^-|^2)\,d\mu$, $\int p_1(TM)=3\tau$.

Combining,
$$
\int p_1(\Lambda^2_+) = 2\chi+3\tau = \frac{1}{4\pi^2}\int_M\Big(2|W^+|^2+\tfrac{s^2}{24}-\tfrac12|E|^2\Big)\,d\mu .
$$
So the geometric integral $\int(2|W^+|^2+\tfrac{s^2}{24}-\tfrac12|E|^2)\,d\mu = 4\pi^2(2\chi+3\tau)$. There is no $8\pi^2$ in the placeholder $\int p_1=8\pi^2(2\chi+3\tau)/?$; the $8\pi^2$ belongs to $\chi$, and the dimensionless topological number is exactly $2\chi+3\tau$. Please replace the placeholder by the two forms above so the "$\int p_1=2A/3$" (dimensionless) and "$4\pi^2(A-k)$" (curvature integral) normalizations in step9 are not conflated.

**Basic-collapse vanishing is valid, and it is a pullback statement, not a metric statement.** If the induced connection on $\Lambda^2_+$ is genuinely pulled back from a base $B$ of dimension $\le 3$, its curvature 2-form $F^+$ is a pullback $\pi^*\beta$. Then $F^+\wedge F^+=\pi^*(\beta\wedge\beta)$ is a pullback of a degree-4 form on $B$, which is identically zero because $\dim B\le 3$. Hence $\operatorname{tr}(F^+\wedge F^+)=0$ pointwise and the local Chern–Weil density vanishes. This is the standard vanishing of characteristic forms above the base dimension and is correct.

The essential qualification the notes make correctly: this holds only when the $\Lambda^2_+$ connection is *basic*. A generic collapsing $S^1$- or $T^k$-fibration carries vertical connection curvature (the O'Neill/field-strength tensor) that is not basic. Taub–NUT is precisely the non-basic case: the Hopf connection $d\psi+\cos\theta\,d\phi$ has curvature $-\sin\theta\,d\theta\wedge d\phi\neq0$. So the vanishing is a genuine structural dichotomy — basic (density zero) versus twisted (density can be nonzero) — not a property of collapse per se. This is what makes the localization statement nontrivial rather than automatic.

---

## 2. Taub–NUT–AdS countermodel

I verified the NUT smoothing algebraically. Near $r=\nu$, $F_\nu(r)\approx \frac{r-\nu}{2\nu}$; with $r=\nu+\rho^2/(8\nu)$ one gets $dr^2/F_\nu\to d\rho^2$, and both $(r^2-\nu^2)$ and $4\nu^2F_\nu$ tend to $\rho^2/4$, giving
$$
d\rho^2+\tfrac{\rho^2}{4}\big[d\theta^2+\sin^2\theta\,d\phi^2+(d\psi+\cos\theta\,d\phi)^2\big]=d\rho^2+\rho^2 g_{S^3},
$$
the flat $\mathbb R^4$ metric with $\psi$-period $4\pi$. **The flat-$\mathbb R^4$ NUT structure is confirmed.**

**(a) Contractibility — correct.** Near the NUT the space is $\mathbb R^4$ and the $\psi$-fiber is the Hopf circle at a small radius, which bounds a disk. Sweeping the fiber radially from the basepoint (distance $1/2$) to the NUT gives a nullhomotopy whose image stays within distance $\le 1/2$ of $p_\nu$, hence inside $B_1(p_\nu)$. Consequently the local universal cover of $B_1$ does not unwrap this loop, so the cover remains collapsed. This is sound.

**(b) Uniform curvature bound — asserted, not computed in the supplied files.** The metric is Einstein $\operatorname{Ric}=-g$ (with $\ell^2=3$, so $-3/\ell^2=-1$), so $E=0$, $s=-4$, and $|\mathrm{Rm}|^2=|W^+|^2+|W^-|^2+s^2/24$. The Weyl part is the piece that must stay bounded uniformly in $\nu$ at fixed distance from the NUT. Physically this is Berger-sphere/Hopf collapse with the NUT-localized Weyl contribution scaling with $\nu$, so at fixed distance the density should tend to the AdS background value as $\nu\to0$, giving a $\nu$-independent bound $K_0$. This is plausible and consistent with the known bounded-curvature collapse of shrinking Hopf circles, **but the provided material does not contain the computation.** The referenced `verify_weitzenbock_clean.py` addresses the eigenform energies, not the Taub–NUT curvature. Two cheap symbolic computations would make this decisive:
  1. Confirm $\operatorname{Ric}_{g_\nu}=-g_\nu$ exactly for the stated $F_\nu$ (the metric-function tuning that makes the NUT regular and Einstein at $\ell^2=3$ should be verified symbolically, since the exact form of $F_\nu$ determines whether it is a genuine regular AdS–Taub–NUT).
  2. Tabulate $|W^\pm|^2(r;\nu)$ on the band $r\in[\nu+\tfrac16,\nu+\tfrac56]$ for a range $\nu\downarrow0$ and read off the uniform bound $K_0$.

**(c) Maximal-function bound — immediate given (b).** If $\sup_{\text{band}}|\mathrm{Rm}|^2\le K_0$, then $\fint_{B_r}|\mathrm{Rm}|^2\le K_0$ trivially. So (c) reduces entirely to (b).

**Standing of the countermodel.** As a refutation of the *general local* statement "controlled maximal $\fint|\mathrm{Rm}|^2$ at all scales $+\operatorname{Ric}\ge-3g\Rightarrow$ noncollapse of the local universal cover," the construction is credible (modulo the (b) computation): $\operatorname{Ric}=-g\ge-3g$, curvature energy density bounded, volume $O(\nu)\to0$, and the collapsing circle contractible so the cover stays collapsed. The notes are right that this does *not* touch the closed-manifold problem: the space is noncompact, $\int|\mathrm{Rm}|^2=\infty$, and there is no monopole/topology constraint. The distinction between "local regularity is not automatic" and "the closed Ishida–LeBrun problem" is handled accurately.

---

## 3. Weitzenböck computation

**The numbers are correct; I confirm them from the standard self-dual Weitzenböck formula independently of the $\widetilde R$ bookkeeping.** For $\omega\in\Lambda^2_+$ on an Einstein 4-manifold,
$$
\Delta_d\omega=\nabla^*\nabla\omega+\tfrac{s}{3}\omega-2W^+(\omega).
$$
For harmonic $\omega$ in the $\mu_{W^+}$-eigenspace,
$$
\frac{\int|\nabla\omega|^2}{\int|\omega|^2}=2\mu_{W^+}-\tfrac{s}{3}.
$$
With $s=-4$ ($\lambda=-1$) and $\operatorname{Spec}(W^+)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$:
- simple ($\mu_{W^+}=-1/6$): $2(-\tfrac16)+\tfrac43=1$ ✓
- double ($\mu_{W^+}=1/12$): $2(\tfrac1{12})+\tfrac43=\tfrac32$ ✓

The three consistency checks also hold: KE $\lambda=-1$ has the Kähler form with $\mu_{W^+}=s/6=-2/3$, giving $2(-2/3)+4/3=0$ (parallel) ✓; K3 gives $0$ ✓; $S^4$ ($s=12$) gives $2\cdot0-4=-4<0$, hence no harmonic self-dual forms, matching $b^+_2(S^4)=0$ ✓. So **the conclusion — every harmonic self-dual form at the calibrated spectrum has gradient energy of the same order as its amplitude, hence is not nearly parallel — is correct and well-supported.**

**One interpretive sentence in step9 is inaccurate.** The note states the $\widetilde R$-arrangement eigenvalues are "not the usual $W^++s/12$." In fact the computed values $\mu_{\widetilde R}=(-\tfrac12,-\tfrac14,-\tfrac14)$ are *exactly* $W^++\tfrac{s}{12}$:
$$
-\tfrac16+\tfrac{-4}{12}=-\tfrac12,\qquad \tfrac1{12}+\tfrac{-4}{12}=-\tfrac14 .
$$
These are precisely the eigenvalues of the curvature operator $\mathcal R|_{\Lambda^2_+}=W^++\tfrac{s}{12}\,\mathrm{Id}$. The identity $q(R)=2\lambda-2\widetilde R$ then reproduces $2\mu_{\widetilde R}-2\lambda=2W^++\tfrac{s}{6}-\tfrac{s}{2}=2W^+-\tfrac{s}{3}$, agreeing with the standard formula. So the two routes are the same computation; the sentence asserting a difference from $W^++s/12$ should be corrected (it does not propagate to any wrong number). The genuine subtlety worth keeping is only that the raw contraction $R_{ikjl}\omega^{kl}$ does not manifestly preserve $\Lambda^2_+$; after the self-dual projection it reduces to $W^++s/12$.

---

## 4. Definite-pair exclusion

**Local nondegeneracy of the Gram matrix is an additional hypothesis, not automatic.** This is the pivotal point of Question 4, and the answer is unambiguous.

Global linear independence of harmonic self-dual forms (independence as $L^2$ sections / cohomology classes) does not imply pointwise linear independence. A harmonic self-dual 2-form can have zeros, and two globally independent harmonic forms $H_1,H_2$ can have $\det\langle H_a,H_b\rangle$ vanish or degenerate on a subset. Precisely in the collapsing regions — where the program needs the exclusion — the pointwise Gram matrix is exactly where degeneration is expected. The step9 note flags this correctly for flat rank 3 ("requires *local* nondegeneracy, not just global independence") but the boxed rank-$\ge2$ statement omits the qualification. The two should carry the same wording: **flat rank $\ge2$ is excluded only on the set where the Gram matrix stays uniformly nondegenerate.**

There is also an internal tension in the phrasing "closedness and constant amplitude force $\nabla H\to0$." Read literally against the step9 Weitzenböck result, constant amplitude does *not* force $\nabla H\to0$ — the same section proves $\int|\nabla H|^2=(1+o(1))\int|H|^2>0$. The intended logic is a reductio: the *flat rank-2 collapse model* would make the spanning forms nearly parallel ($\nabla H\to0$), and Weitzenböck contradicts that, excluding the model. Written that way it is valid, but only where (i) two forms actually span a rank-2 subbundle with nondegenerate Gram matrix and (ii) the flat-fiber structure genuinely forces near-parallelism. Both are hypotheses on the geometry, not consequences of the form algebra. The rank-1 and nil-twisted cases remaining open (as the note states) is consistent with this.

---

## 5. Assessment of the Pontryagin charge and a sharpening

**The charge is correctly computed.** For a minimal general-type surface, $c_1^2(X)=2\chi(X)+3\tau(X)=A$; under $M=X\#k\overline{\mathbb{CP}}^2$, $\chi(M)=\chi(X)+k$, $\tau(M)=\tau(X)-k$, so
$$
2\chi(M)+3\tau(M)=A-k=c_1^2(M),\qquad \frac{A-k}{A}\to\frac23 .
$$
Hence $\int p_1(\Lambda^2_+)=A-k\to 2A/3$ (dimensionless), equivalently $\int(2|W^+|^2+\tfrac{s^2}{24}-\tfrac12|E|^2)\,d\mu=4\pi^2(A-k)$. Both numbers in the notes are consistent. Basic collapse contributes zero, as verified in item 1.

**A sharpening the notes do not use, and which strengthens the mechanism.** On the calibrated near-saturation, $E=O(\delta)\to0$, $s\to-4$, and $|W^+|^2\to1/24$, so the Pontryagin density becomes essentially nonnegative and, more strongly, *uniformly bounded below*:
$$
2|W^+|^2+\tfrac{s^2}{24}-\tfrac12|E|^2 \;\to\; 2\cdot\tfrac1{24}+\tfrac{16}{24}=\tfrac{3}{4}>0
$$
on the good set (where the calibrated deficit $F_i$ is small). I checked this integrates correctly: $\tfrac34\cdot\mathrm{Vol}\approx\tfrac34\cdot\tfrac{32}{9}\pi^2 A=\tfrac{8}{3}\pi^2 A=4\pi^2\cdot\tfrac{2A}{3}=4\pi^2(A-k)$ ✓.

The consequence is stronger than "the charge localizes to a small bad set." Because a basic $\Lambda^2_+$ connection forces the density to vanish pointwise, while the calibration forces the density to equal $\approx 3/4$ on the bulk (most of the volume), **the collapse cannot be basic anywhere on the good set** — it must be twisted (non-basic vertical curvature) across the whole bulk, not merely on a small exceptional stratum. The topological charge is carried as a uniform positive density over the good set. This is exactly the Taub–NUT-type twisted collapse: its Hopf connection has nonzero field strength, so it is a non-basic collapse that can and does support Pontryagin density. So the countermodel of item 2 and the localization mechanism of item 5 are the same geometric object seen from two sides.

Two quantitative points to make this a working tool rather than a heuristic:
- The density $2|W^+|^2+\tfrac{s^2}{24}-\tfrac12|E|^2$ is sign-indefinite in general (the $-\tfrac12|E|^2$ term), so the "positive topological energy in twisted regions" argument needs the near-Einstein control $|E|^2=O(\delta^2)$ to make it effectively nonnegative. Near saturation this is available; away from saturation it is not, and any use of the density as a lower energy bound should carry the $E$-control explicitly.
- To turn "charge lives in twisted regions" into "$\int_{\text{twisted}}|\mathrm{Rm}|^2\ge c(A-k)$," one needs $|p_1\text{-density}|\le C|\mathrm{Rm}|^2$ (immediate by Cauchy–Schwarz) together with the density lower bound above. The notes sketch this but do not state the coupling constant; it is worth writing down because it is what connects the fixed topological charge to the curvature-energy budget that the rest of the program manipulates.

---

## What remains unresolved (substance needed)

1. The uniform-in-$\nu$ curvature bound (2b) and the exact Einstein property of $F_\nu$ are asserted; a short symbolic computation of $\operatorname{Ric}_{g_\nu}$ and $|W^\pm|^2(r;\nu)$ on the band would settle both and pin $K_0$.
2. The rank-$\ge2$ definite-pair exclusion holds only where the Gram matrix is uniformly nondegenerate; the open cases (rank-1 weighted harmonic forms on the 3D base, nil-twisted Heisenberg models) are exactly the ones the twisted-collapse picture predicts, and they are where the Pontryagin charge must sit. The unresolved question is whether the twisted regions carrying the charge $4\pi^2(A-k)$ can be simultaneously (i) volume-collapsed, (ii) curvature-energy-bounded in the $\int|\mathrm{Rm}|^2\le E_0(A)$ budget, and (iii) non-basic enough to hold the full charge. The uniform density $3/4$ result above makes (ii)–(iii) a sharp arithmetic question rather than an open-ended search: the total curvature energy $\int|\mathrm{Rm}|^2$ and the fixed charge $4\pi^2(A-k)$ must both be accommodated by the same twisted geometry, and comparing the two integrals ($\overline{|\mathcal R|^2}\le12$ from step11 versus the density $\ge3/4$ forced by calibration) is the concrete computation that would decide whether the twisted collapse is possible.
3. The interpretive sentence in item 3 and the missing qualification in item 4 are corrections of wording; neither changes a computed value, but both matter for anyone reading the notes as a source of established statements.
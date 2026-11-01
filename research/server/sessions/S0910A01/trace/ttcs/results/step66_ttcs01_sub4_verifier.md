# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step66_route_reorientation_after_IL_bridge.md",
    "Sessions/S0910A01/workspace/notes/step65_per_datum_existence_theorem.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Read the Step 66 route reorientation note and related context. Check the mathematical logic and scope: the correction to Step65's family-uniform C^k wording; exclusion of #5CP2 by tight-pinching Hitchin--Thorpe; asymmetric interpretation of A02's Green-operator desingularization computation; and the claimed flow-transfer principle from sign-general cutoff flow plus calibration density to a branch gap. Identify any overstatement, missing assumption, or stronger route suggested by the same evidence. Keep the answer scientific and concrete.

## Output

# Verification memo on Step 66 (route reorientation after the restricted IL bridge)

Session S0910A01 material read: `step66_route_reorientation_after_IL_bridge.md`, `step65_per_datum_existence_theorem.md`, `step55_joint_bootstrap_background_continuation_repair.md`, `step8_derdzinski_measure_local_theorem.md`, dossier `20260910.tex` (§2, §4.2, §4.3, §6, §9).

---

## 1. Algebra I recomputed independently, and what it confirms

Before discussing the four items, I recomputed the arithmetic on which Step 66's judgements rest, because several of the route decisions depend on it.

**(a) Step 8's completion identity is exact.** With $f=\tfrac23 s-2\alpha u$, $\alpha=\sqrt{2/3}$, $u=|W^+|$:
$\tfrac1{12}f^2=\tfrac1{27}s^2-\tfrac{2\sqrt6}{27}su+\tfrac29u^2$, $\tfrac1{216}(s+8\sqrt6u)^2=\tfrac1{216}s^2+\tfrac{2\sqrt6}{27}su+\tfrac{16}9u^2$; the $su$ terms cancel, $\tfrac1{27}+\tfrac1{216}=\tfrac1{24}$, $\tfrac29+\tfrac{16}9=2$. So $\tfrac{s^2}{24}+2u^2=\tfrac1{12}f^2+\tfrac1{216}(s+8\sqrt6u)^2$ holds identically.

**(b) The calibrated point is exactly the second square's zero.** At $s=-4$, $u=1/(2\sqrt6)$: $f=-8/3-1/3=-3$ and $s+8\sqrt6u=-4+4=0$. $\mathcal G=f^2-(a_-)^2=9-(3-2\xi)^2=4\xi(3-\xi)$, so $\mathcal G=0\iff\xi=0\iff w=-1/6$, and trace-free plus $|W^+|^2=1/24$ forces $(-1/6,1/12,1/12)$ (solve $\lambda_2+\lambda_3=1/6$, $\lambda_2^2+\lambda_3^2=1/72$: double root $1/12$). The sharp enclosure is $\xi\in[0,1/12]$, not $[0,1/6]$ as written in Step 8 §2; the weaker enclosure suffices for the argument, but the sharp one is worth recording since it quantifies how far the eigenvalues can sit from the calibrated triple at given $\mathcal G$.

**(c) The Einstein–Weyl identity's normalization passes an exact test.** On the Kähler–Einstein model $\operatorname{spec}W^+=(-2/3,1/3,1/3)$, $s=-4$, $\nabla W^+=0$: $2|\nabla W^+|^2+s|W^+|^2-36\det W^+=0-\tfrac83+36\cdot\tfrac2{27}=0$. So the coefficients $2$, $1$, $-36$ in $\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$ are mutually consistent, and at the calibrated spectrum they give $|\nabla W^+|^2=\tfrac12(\tfrac16-\tfrac1{24})=\tfrac1{16}$, matching Step 8.

**(d) Step 8's two constants $864\pi^2D$ and $48\pi^2D$ are reproducible from the recorded LeBrun estimate plus Chern–Weil.** This computation also yields the structural point of §5 below, so I give it there.

These checks are worth having on record: the local germ contradiction at the core of the $\sigma=-1$ route is arithmetically sound and internally cross-validated on an exact solution.

---

## 2. The Step 65 §8 wording correction

**What the correction gets right.** The splice is legitimate. The geometric equation $\partial_tg=-2\chi^2(\operatorname{Ric}_g-\sigma g)$ with fixed $\chi$ is autonomous in $g$, so every time derivative at a splice time $T$ is a universal expression $\partial_t^kg=P_k(g,\partial g,\dots,\partial^{2k}g;\chi)$ evaluated at $g(T)$. Left and right one-sided jets therefore agree automatically, and the concatenated $g$ is smooth in $t$ without any gauge matching. Step 65 §7's re-initialization $\varphi_{T+s}=\varphi_T\circ\psi_s$ is then only bookkeeping. Dropping the assertion of family-uniform $C^k$ bounds on slabs is correct: nothing in Step 65 produces constants independent of the datum.

**Where the corrected statement is still stronger than the recorded material.** Step 66 §0 states that the per-datum theorem "removes the last named analytic hypothesis" in the restricted route. Two concrete obstacles remain in the notes themselves.

*(i) Restart times can accumulate.* $T_0$ in Step 65 (4.7) depends on the full datum, including $\|g_0\|_{H^{s_0}}$ with $s_0=\lfloor n/2\rfloor+5$ (in $n=4$: $H^7$) and the positivity constant $\lambda_0$. Iterating restarts gives times $T_0^{(1)},T_0^{(2)},\dots$, and reaching a *prescribed* observation time $\theta r^2$ requires $\sum_kT_0^{(k)}\ge\theta r^2$, i.e. a lower bound on $T_0$ along the flow. The $(\Gamma,V)$ bootstrap of Step 55 does supply the positivity half: (1.6) gives $e^{-2V}g(0)\le g(t)\le e^{2V}g(0)$ with $V\le V_*$, so $\lambda$ does not degenerate. It does **not** supply a time-uniform $H^{s_0}$ bound: Step 55 controls the weighted energy $H$, the weighted $\|aF_T\|_\infty$, and $\|aE\|_\infty$, none of which bound $\|g(t)\|_{H^7}$. Step 55 §4 item 2 says exactly this ("the current-pair hierarchy must be completed to every finite order needed for restart"). So the continuation to $\theta r^2$ is not yet a consequence of Step 65 plus Step 55; one all-order (or at least $s_0$-order, time-uniform) estimate is still open.

*(ii) A cheaper substitute exists and should be considered instead.* If the terminal argument is run on exponential pullback balls (Step 55 §3), then smooth compactness is not needed. On a pullback ball with $|\operatorname{Rm}|\le K$ (terminal plateau estimate (1.19)) Rauch gives two-sided volume control, so Cheeger–Naber's harmonic radius lower bound applies, and Step 8 §5's finite-$W^{2,p}$ passage yields a $W^{2,p}$ limit that is Einstein weakly, hence smooth by elliptic regularity. This needs only $|\operatorname{Rm}|$ plus volume on pullbacks — not the derivative bounds Step 55 §3 says are required "only after the finite restart/continuation estimates are available". The two notes are inconsistent about which regularity input the germ argument consumes, and the weaker input suffices. Resolving this in favour of the weaker input would shrink the remaining analytic work substantially, but note that it does not remove obstacle (i), which is about reaching $\theta r^2$ at all.

**Document defects in Step 65 that affect readability of the very step being corrected.** §4.5 breaks off after "Grönwall gives" and the text resumes at §5.1; equation (4.9), cited in (5.1), does not appear. The label (4.7) is used twice (for $T_0$ and next to (4.7a)). §4.4 asserts existence on $[0,T_0)$ *and* closure of the interval by "restarting once more", which is the same accumulation issue in miniature and should be written as a statement about $\mathcal E_{s_0}$ staying bounded up to $T_0$.

---

## 3. Exclusion of $\#_5\mathbb{CP}^2$ by tight pinching

**Arithmetic verified.** $\chi(\#_m\mathbb{CP}^2)=m+2$, $\tau=m$, $2\chi-3\tau=4-m$, $2\chi+3\tau=5m+4$. Dossier Proposition 4.2 needs $\varepsilon<1/(1+\sqrt3)$: indeed $\tfrac23(1-\varepsilon)^2>2\varepsilon^2\iff 1-\varepsilon>\sqrt3\varepsilon$. Its proof uses $|s|\ge4(1-\varepsilon)$ and $|E|^2=\sum(e_i-\bar e)^2\le\sum e_i^2\le4\varepsilon^2$, both correct, and drops $|W^\pm|^2\ge0$ for both signs. So $2\chi>3|\tau|$ under either normalization. $m=5$ is excluded.

**Three refinements the same computation gives.**

*(a) $m=4$ is excluded too.* $2\chi-3\tau=0$ violates the *strict* inequality, so $\#_4\mathbb{CP}^2$ also cannot carry $\varepsilon<1/(1+\sqrt3)$ pinching of either sign. Step 66 §2.1 says "$\#_5$ and all stronger violators"; the equality case belongs in the excluded set. (Independently, equality with Einstein forces $s=0$, $W^+=0$, which $\#_4\mathbb{CP}^2$ cannot realize.) The live $\#_m\mathbb{CP}^2$ range for a $\sigma=+1$ counterexample search is therefore $m\le3$ only.

*(b) A volume estimate falls out, not just a topological one.* Keeping the discarded terms,
$$2\chi\pm3\tau\;=\;\frac1{4\pi^2}\!\int\!\Big(2|W^\pm|^2+\frac{s^2}{24}-\frac{|E|^2}2\Big)\;\ge\;\frac{1}{2\pi^2}\!\int\!|W^\pm|^2+\frac{\kappa(\varepsilon)\operatorname{Vol}}{4\pi^2},\qquad \kappa(\varepsilon)=\tfrac23(1-\varepsilon)^2-2\varepsilon^2,$$
hence for any closed oriented $M^4$ and any $g$ with $\delta_\sigma(g)\le\varepsilon<1/(1+\sqrt3)$:
$$\operatorname{Vol}(M,g)\le\frac{4\pi^2\bigl(2\chi-3|\tau|\bigr)}{\kappa(\varepsilon)},\qquad \int|W^\pm|^2\le2\pi^2(2\chi\pm3\tau)-\tfrac12\kappa(\varepsilon)\operatorname{Vol}.$$
With $\varepsilon\to0$: $\operatorname{Vol}\le6\pi^2(2\chi-3|\tau|)$. This is a *dimension-only-threshold, topology-only-constant* a priori estimate for the entire pinched class in dimension four, both signs. It is consistent with, and explains, the bookkeeping $\operatorname{Vol}/A\asymp1$ assumed in Step 8 §4.

*(c) Bounded $L^2$ curvature energy follows.* Using $|\operatorname{Rm}|^2=|W|^2+2|E|^2+s^2/6$ in dimension four (this coefficient should be re-derived under the Step 64 canonical convention before quotation) and $\int|W|^2\le8\pi^2\chi-\kappa\operatorname{Vol}$ from adding the two Chern–Weil identities,
$$\int|\operatorname{Rm}|^2\le 8\pi^2\chi+C(\varepsilon)\operatorname{Vol}\le 8\pi^2\chi+16\pi^2\bigl(2\chi-3|\tau|\bigr)+O(\varepsilon).$$
So the whole pinched class in dimension four has two-sided Ricci bounds, bounded volume, and bounded $\int|\operatorname{Rm}|^2$, all with constants from $(\chi,\tau)$ alone. Jiang–Naber and Cheeger–Naber then apply wherever a unit-ball volume lower bound is available. This says something the notes have not used: in dimension four, the *only* regime not already inside standard bounded-Ricci compactness theory is collapse — the same conclusion Step 8 §6–§7 reached for the IL family, but now for arbitrary four-dimensional topology and both signs.

*(d) Non-orientable case.* $\tau$ is undefined there, but pinching lifts to the orientation double cover $\tilde M$, where $\tau(\tilde M)=0$, so the exclusion reads $\chi(M)>0$. Note the direction of the lifting argument: an Einstein metric on $M$ lifts to $\tilde M$, so nonexistence on $\tilde M$ gives nonexistence on $M$, but existence on $\tilde M$ does not descend. The non-orientable case therefore inherits the exclusion but not the positive statement.

---

## 4. The asymmetric reading of the Green-operator computation

The asymmetry stated in Step 66 §2.2 is correct in direction, but both halves need adjustment.

**The "success" half is stated too strongly.** A Green-operator/pattern computation on a mixed Eguchi–Hanson configuration over $(S^2\times S^2)/\mathbb Z_2$ decides whether the *leading* desingularization obstruction vanishes. Biquard's obstruction (dossier ref. [30]) and Ozuch's higher-order obstructions (refs. [34], [35]) together say that vanishing at leading order does not close the nonlinear gluing: further obstructions can appear at higher order, and the fixed-point step needs an inverse bound for the linearized operator on the glued configuration, which the pattern computation does not supply. So a favourable computation upgrades the configuration to "not obstructed at this order", not to "Einstein metrics constructed". Which smooth type would result (its $\chi,\tau$, hence whether it lies in the strict-$2\chi>3|\tau|$ range) should be recorded together with the numbers, since by §3 above that determines whether the type was ever a pinching candidate.

**The "obstruction only local" half understates what is available.** Step 66 says a global compactness/rigidity theorem forcing all Einstein metrics into the studied degeneration is "missing". Item 3(c) shows a large part of it is elementary: for an Einstein metric on a fixed closed oriented $M^4$ with normalized $|\lambda|=1$, $\int|\operatorname{Rm}|^2=8\pi^2\chi+\tfrac{s^2}8\operatorname{Vol}$ and $\operatorname{Vol}\le96\pi^2(2\chi-3|\tau|)/s^2$, so $\int|\operatorname{Rm}|^2\le8\pi^2\chi+12(2\chi-3|\tau|)$ — bounded by topology alone, uniformly over the whole Einstein moduli set. With a volume (equivalently unit-ball volume) lower bound, Anderson/Bando–Kasue–Nakajima/Cheeger–Naber orbifold compactness then confines *all* such Einstein metrics to a compact set of orbifold degenerations. The genuinely absent ingredient is thus a volume lower bound for Einstein metrics on the candidate type, not a new compactness theory. For $\lambda<0$ a candidate source is Gromov's comparison $\|M\|\le C(n)\operatorname{Vol}$ under $\operatorname{Ric}\ge-(n-1)g$ (to be read from its source before use), which paired with the upper bound in 3(b) yields a purely topological compatibility condition $\|M\|/C(4)\le6\pi^2(2\chi-3|\tau|)$ for pinched $\sigma=-1$ metrics. That is a concrete, cheap test worth computing on any candidate family.

---

## 5. The flow-transfer principle: one ingredient is an identity, one is genuinely open

Step 66 §3 lists (1) a global curvature/defect budget from topology, (2) a selected-support construction with proportional volume and small local mean **terminal** density, (3) a branch density $\Phi_\sigma$ whose zero set forbids the germ.

**Ingredient (1) is stronger than stated: it is an exact identity valid for every metric.** From Chern–Weil,
$$\frac1{4\pi^2}\int\Bigl(\frac{s^2}{24}+2|W^+|^2\Bigr)d\mu_g=(2\chi+3\tau)+\frac1{8\pi^2}\int|E|^2d\mu_g,$$
so with $A=(a^+)^2$ the Step 8 deficit is
$$\boxed{\;D(g)=(2\chi+3\tau)-\tfrac23A+\frac1{8\pi^2}\int|E|_g^2\,d\mu_g\;}$$
— a topological number plus the pinching defect energy. Consequences:

* Combining with LeBrun's estimate $\int(a)_-^2\ge32\pi^2A$ and $(a)_-^2\le f^2$ reproduces Step 8's constants exactly: $\tfrac1{18}\int(s+8\sqrt6|W^+|)^2\le 864\pi^2D$ and $0\le\int\mathcal G\le48\pi^2D$. Both are now derived rather than script-checked.
* For the IL blow-ups $M_i=X_i\#k_i\overline{\mathbb{CP}}^2$ with $2\chi+3\tau=A_i-k_i$, the identity gives $D_i=\bigl(\tfrac{A_i}3-k_i\bigr)+\tfrac1{8\pi^2}\int|E_i|^2$. So the geography hypothesis "$D_i/A_i\to0$" is *not* an independent analytic assumption: it is the arithmetic condition $k_i/A_i\to1/3$ together with $\|E_i\|_\infty\to0$ and the volume bound of §3(b). This both explains Step 8 §8's $k_i/A_i\to1/3$ and shows the hypothesis is easy to arrange (choose $k_i=\lfloor A_i/3\rfloor$).
* No monotonicity along the flow is needed for the budget: the identity holds for $g(t)$ verbatim, with the only time-dependent term $\int|E(t)|^2$.

**Ingredient (2) contains the actual open link, and it is not the one Step 66 names.** The word "terminal" is doing heavy work. The budget above is quantitatively useful at $t=0$, where $\|E(0)\|_\infty\le\delta$ globally and $\int|E(0)|^2\le4\delta^2\operatorname{Vol}$. At $t=\theta r^2$ two things must hold that are not yet established:

* *Global $E$-energy at terminal time.* Step 55 (1.18) controls only $\|aE(t)\|_\infty$ with $a=\chi^2$. On $\{\chi=0\}$ the flow is stationary so $E(t)=E(0)$ is small; on $\{a\ge a_0\}$ one gets $|E|\le C\delta a_0^{-1}(r^2/t)^{1/3}$; on the cutoff transition set $\{0<a<a_0\}$ nothing prevents $|E(t)|$ from being large, and $\int_{\{0<a<a_0\}}|E(t)|^2$ is not controlled. So $D(g(\theta r^2))$ is not yet bounded.
* *Transport of the mixed density.* Alternatively one keeps the budget at $t=0$ and transports the small local mean of $\Phi=|E|^2+(s+8\sqrt6|W^+|)^2+\mathcal G$ from $t=0$ to $t=\theta r^2$. The Step 55 machinery bounds the weighted curvature *energy* $H(t)\le H(0)e^{C\theta+C_VV}$ and the weighted defect $\|aE\|_\infty$; neither implies that a small local mean of $(s+8\sqrt6|W^+|)^2$ stays small, since the flow can create $W^+$ while $H$ merely stays bounded. This is the same object in a different guise.

So the flow-transfer principle should be written with ingredient (2) split into (2a) budget at the initial time, (2b) a transport estimate for the branch density across $[0,\theta r^2]$, or an equivalent terminal-time budget with cutoff-transition control. Candidate routes: (i) an $L^1$-in-space, $L^1$-in-time estimate $\int_0^{\theta r^2}\!\!\int a|\partial_t\Phi|$ using the curvature variation of Step 63 with the weighted $H$-energy and $\|aE\|_\infty$; (ii) a plateau-localized Chern–Weil identity with transgression terms on the edge of $\{a=1\}$, where at terminal time $|\operatorname{Rm}|\le K$ makes the transgression integral estimable — this would give a *local* budget and avoid transport entirely, at the cost of controlling the edge terms; (iii) choosing the cutoff so that the transition set has volume proportion $o(1)$ relative to the selected support, and re-deriving the terminal budget with that set's contribution absorbed. Route (ii) looks the most structurally interesting and is not in the notes.

**Ingredient (3) is verified for $\sigma=-1$** by §1 above, on pullback balls as well as on the base, since Derdziński Proposition 5, the projector lemma $\nabla\omega=0$, and the Einstein–Weyl identity are local and $\exp_p$ is an immersion for $\rho<\pi/\sqrt K$, so the pullback is locally isometric and Einstein-ness passes.

**One more mechanism in Step 55 §3 that deserves to be recorded as a proved lemma.** The Liouville step is exact, not heuristic: writing $d\mu_{\tilde g_p}=J\,dt\,dv$ with $J\le J_K(t)$ by Rauch, and using invariance of the Liouville measure under geodesic flow,
$$\int_M\!\int_{S_pM}\!\int_0^\rho \Phi(\exp_p(tv))\,dt\,dv\,d\mu(p)=\int_0^\rho\Bigl[\int_{SM}\Phi(\pi\xi)\,d\xi\Bigr]dt=\rho\,\omega_{n-1}\int_M\Phi\,d\mu .$$
With the Rauch two-sided bound on $\operatorname{Vol}(\mathcal B_\rho(p))$, this gives $\int_M A_\rho\Phi\,d\mu\le C(K,\rho,n)\int_M\Phi\,d\mu$ with **no** injectivity or volume assumption on the base. This is the collapse-tolerant part of the architecture, and it is stronger than Step 8's Bishop–Gromov averaging lemma, which needs the doubling constant. Step 66 §4 Front A therefore has a plausible route through the collapsed regime, which Step 8 §7 treated as an open unwrapping problem — but the route runs through the terminal-density issue just described, and Front A's asserted uniform $\varepsilon_{IL}$ is not delivered by the recorded material until that item and item 2(i) are settled. As currently supported, the IL output remains the volume-proportion statement of Step 8 §6 plus the local germ contradiction.

---

## 6. A structural reason the $\sigma=+1$ branch looks different from how Step 66 frames it

Step 66 §3 says no positive analogue of the monopole calibration is *known*. The evidence in hand gives a sharper statement: under $\delta_+(g)\le\varepsilon<1$ one has $s\ge4(1-\varepsilon)>0$, so Witten's vanishing applies and all Seiberg–Witten invariants of $M$ vanish. Every LeBrun-type Einstein-nonexistence theorem in the recorded sources needs a nonzero monopole class. Hence for $\sigma=+1$ the monopole route is not merely undeveloped — it is incompatible with the input, exactly as dossier §4.3 warns. The remaining recorded Einstein-nonexistence mechanism compatible with positive scalar curvature is Hitchin–Thorpe, and §3 above shows tight pinching already forces strict $2\chi>3|\tau|$.

Two consequences for how the same evidence can be used:

* Within the recorded obstruction inventory there is **no** four-dimensional mechanism that can both exclude all Einstein metrics and coexist with tight $\sigma=+1$ pinching. A $\sigma=+1$ counterexample requires a new nonexistence invariant surviving positive scalar curvature. By dossier Proposition 2.5 ($Q_n\iff P_n^+\vee P_n^-$), proving $P_4^+$ alone settles $Q_4$. This makes the $\sigma=+1$ *existence* direction, not the obstruction search, the higher-yield four-dimensional target — the opposite emphasis to Step 66 §4 Front B.
* What such a proof would need is now concrete: by §3, $\delta_+(g)\le\varepsilon$ gives $\operatorname{diam}\le\pi\sqrt{3/(1-\varepsilon)}$ (Myers), $\operatorname{Vol}\le6\pi^2(2\chi-3|\tau|)+O(\varepsilon)$, $\int|\operatorname{Rm}|^2\le C(\chi,\tau)$, and $2\chi>3|\tau|$. So the class is precompact in the bounded-Ricci orbifold sense away from collapse. The two live questions are then: (A) can $\delta_+\to0$ occur with unit-ball volume $\to0$ in dimension four, or does the two-sided pinching plus Myers exclude collapse (the three-dimensional lens-space family shows collapse is possible under exact positive Einstein conditions, so the four-dimensional analogue must be examined rather than assumed either way); (B) in the non-collapsed case the limit is an Einstein *orbifold*, and passing from that to a smooth Einstein metric on $M$ is precisely the desingularization problem with Biquard/Ozuch obstructions — so non-collapsed does not automatically give a positive answer, and this is where the obstruction computations of §4 acquire real weight for the $\sigma=+1$ branch.

For $n\ge5$ (Front D) the situation differs in one identifiable way: there is no analogue of §3(c), i.e. pinching gives no bound on $\int|\operatorname{Rm}|^{n/2}$, which is exactly the hypothesis appearing in Yao's Theorem 1.2 (dossier ref. [36]). Any transfer of the four-dimensional architecture to higher $n$ therefore needs a substitute for the Chern–Weil energy bound, not just a substitute for the monopole budget.

---

## 7. Items left unresolved, with the substance needed

1. **Reaching $\theta r^2$ per datum.** Needed: a time-uniform $H^{s_0}$ bound (or the $s_0$-order part of Step 55 §4 item 2) along the flow, so that restart times do not accumulate. The $(\Gamma,V)$ pair gives positivity and bilipschitz control but not this.
2. **Terminal branch density.** Needed: either (2b) transport of $|E|^2+(s+8\sqrt6|W^+|)^2+\mathcal G$ across $[0,\theta r^2]$, or a plateau-localized Chern–Weil budget with controlled transgression on the edge of $\{\chi=1\}$, or control of $\int|E(t)|^2$ on the cutoff transition set. Without one of these, Front A's uniform $\varepsilon_{IL}$ is not yet a theorem, and the supported IL output remains Step 8 §6.
3. **Which regularity the germ argument consumes.** Step 55 §3 and Step 8 §5 disagree; the weaker input ($|\operatorname{Rm}|$ + Rauch volume on pullbacks $\Rightarrow$ harmonic radius $\Rightarrow$ $W^{2,p}$ limit $\Rightarrow$ smooth by elliptic regularity for the limit Einstein equation) appears sufficient and should be written once.
4. **Source items before further investment.** (a) The dimension-four identity $|\operatorname{Rm}|^2=|W|^2+2|E|^2+s^2/6$ under the Step 64 convention. (b) LeBrun's mixed estimate and the constant $32\pi^2$ in the normalization $a=\tfrac23s+2w$, read from `dg-ga/9511015` / `math/0404359`. (c) Whether any all-metric lower bound for $\int(s^2/24+2|W^+|^2)$ exists when $b_-=0$ (relevant to $\#_m\mathbb{CP}^2$, $m\le3$); the monopole ones are removed by Witten vanishing. (d) Gromov's $\|M\|\le C(n)\operatorname{Vol}$ under $\operatorname{Ric}\ge-(n-1)g$, for the pinched $\sigma=-1$ compatibility test in §4.
5. **Step 65 text repair.** §4.5 truncation, the missing (4.9), duplicated (4.7).

Nothing in Step 66's three corrections is mathematically wrong in direction; the two places where it reads stronger than the recorded material are the "last named analytic hypothesis" sentence in §0 and the Front A theorem statement in §4. The two places where the same evidence supports a stronger route are the exact deficit identity $D(g)=(2\chi+3\tau)-\tfrac23A+\tfrac1{8\pi^2}\int|E|^2$ (which turns ingredient (1) into arithmetic and reduces the IL geography hypothesis to $k_i/A_i\to1/3$), and the topology-only bounds $\operatorname{Vol}\le6\pi^2(2\chi-3|\tau|)$, $\int|\operatorname{Rm}|^2\le C(\chi,\tau)$ for the entire pinched class in dimension four, which put the whole four-dimensional problem inside bounded-Ricci compactness theory except for collapse, in both sign branches at once.
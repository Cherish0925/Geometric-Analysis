# TTCS Independent Branch Record

```json
{
  "step_id": 69,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step68_restricted_IL_canonical_assembly.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step69.md",
    "Sessions/S0910A01/workspace/notes/step24_buffered_support_energy_test.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step62_defect_moser_general_p_proof.md",
    "Sessions/S0910A01/workspace/notes/step68_global_yau26_landscape.md"
  ]
}
```

## Task

Read the patched Step 68 restricted Ishida--LeBrun assembly together with the Step 69 repair note and source support/Moser notes. Verify the two specific repaired interfaces, not the entire Yau26 problem: (1) selected-support input should use the full-curvature mean budget on outer buffers, maximal-function radius at least the auxiliary support radius, and collapse-cancelling product S_alpha H_{2,alpha}^{1/2}, with no initial sectional-curvature or noncollapsing Sobolev assumption; (2) the defect Moser endpoint should distinguish the integrated q=2 curvature-energy estimate valid from time zero from the positive-time S^2Y <= C gamma^3/t coefficient on nested Moser slabs. Also verify the Step 69 global-landscape correction that delta_- -> 0 plus all-sign Einstein nonexistence defeats only the negative branch, not the full sign-unrestricted Yau26 proposition. Give a concise scientific reading of whether these repairs are mathematically coherent and what exact remaining proof expansions are still most load-bearing.

## Output

# Verification memo: Step 68/69 two-interface repairs and landscape correction

Session S0910A01. Independent reading of the two repaired interfaces and the negative-branch landscape correction. I verified the algebra and structural logic that I could reconstruct from the provided files, and I mark what is cited to modules not reproduced here.

## 1. Selected-support input (Interface 1): coherent

The repaired mechanism in §4.1–4.5 and route note §2 is internally consistent, and the specific correction over the pre-repair text is genuinely necessary.

**The collapse cancellation is exact.** With the local Croke-type relative Sobolev constant $\mathcal S_\alpha(0)\le Cr^2\operatorname{Vol}(U_\alpha)^{-1/2}$ and the good-support energy $H_{2,\alpha}(0)\le C(1+\widetilde\gamma^2/r^4)\operatorname{Vol}(U_\alpha)$, the product is
$$
\gamma_\alpha(0)=\mathcal S_\alpha(0)H_{2,\alpha}(0)^{1/2}
=Cr^2(1+\widetilde\gamma^2/r^4)^{1/2}=C(r^4+\widetilde\gamma^2)^{1/2}\le C(r^2+\widetilde\gamma),
$$
and $\operatorname{Vol}(U_\alpha)$ cancels identically, for every value of the volume including the collapse regime $\operatorname{Vol}\to0$. This confirms (4.5). The pre-repair statement that "the Sobolev constant does not grow under collapse" was indeed false: as $\operatorname{Vol}(U_\alpha)\to0$ one has $\mathcal S_\alpha=r^2\operatorname{Vol}^{-1/2}\to\infty$, so only the product, not the two factors, is sequence-uniform. The repair states this correctly.

**The Ricci lower bound needed for the maximal-function machinery is free from the pinching hypothesis.** Along a hypothetical sequence with $\|E_i\|_\infty=\delta_i\to0$, one has $\operatorname{Ric}_{g_i}=-g_i+E_i\ge-(1+\delta_i)g_i\ge-2g_i$ for large $i$. So Bishop–Gromov doubling holds up to scale $R_0=10r$ with a sequence-uniform constant $C(R_0)$ (close to the Euclidean $2^4$ for small $r$), and the weak-type volume estimate (4.1e) and the good-set lower volume (4.1f) are legitimate at time zero. Crucially, this Ricci control does **not** bound $|\operatorname{Rm}|$ pointwise: the Weyl part is only in the $L^2$ budget $\int F_T^2\le C_0A_i$. The repair correctly separates the available integral curvature input from an unavailable pointwise sectional input, which is exactly why the smoothing flow is required.

**The $R_0\ge7r$ requirement is load-bearing and correctly identified.** The energy $H_{2,\alpha}(0)$ is computed on $U_\alpha=B_{7r}(x_\alpha)$, so the good-point condition must control $\fint_{B_{7r}}|\operatorname{Rm}|^2$; a maximal supremum over radii $\le r$ would only control $\fint_{B_r}$. The condition $7r\le R_0$ delivers (4.3a). Correct.

**What remains most load-bearing here.** The support algebra does not by itself give the flow. The exact index-level tensor energy inequalities are still premises, not consequences: (3.1)/(6.4) for $H_2$, (6.1) for the $q=3$ moment, (7.2) for the unweighted defect $Q$, each requiring the metric-norm and volume-form variations written out with the derivative-structure bound $|\nabla B|\le CF|\nabla\operatorname{Rm}|$ (step34 §2, eq. 2.10; still listed open in step34 §7 and step62 §8 item 3). The per-datum degenerate cutoff-flow existence (step65, the doubly-regularized transported DeTurck system) is cited to a named parabolic theorem not reproduced; step62 §9 correctly records it as the one fully-conditional analytic input feeding §5. These two are the substantive expansions the repaired Interface 1 still rests on.

## 2. Defect Moser chronology (Interface 2): coherent

The distinction between the time-zero integrated $q=2$ input and the positive-time slab coefficient is correct and is exactly what the ladder needs.

**Integrated bound, valid from zero.** From (3.5) $\sup_{[0,t]}K_2^\eta+\int_0^tD_2^\eta\le CK_2^\eta(0)$ and (3.6) $\int_0^tY\le C\gamma K_2^\eta(0)$, using $\mathcal S(s)\le2\mathcal S(0)$,
$$
\int_0^t\mathcal S^2Y\le 4\mathcal S(0)^2\cdot C\gamma K_2^\eta(0)=C\gamma\cdot\mathcal S(0)^2K_2^\eta(0)=C\gamma^3,
$$
since $\gamma^2=\mathcal S(0)^2K_2^\eta(0)$. Confirms (3.7).

**Positive-time coefficient, not integrated from zero.** The good slice $\tau\in[t/4,t/2]$ with $Y(\tau)\le C\gamma K_2^\eta(0)/t$, forward-propagated through $Y'\le C(r^{-2}+1+\mathcal S^2Y)Y$ with Grönwall exponent $\int_\tau^t(r^{-2}+1)+\int_\tau^t\mathcal S^2Y\le C\theta+C\gamma^3=O(1)$, gives $Y(t)\le C\gamma K_2^\eta(0)/t$ and $\mathcal S(t)^2Y(t)\le C\gamma^3/t$. Confirms (4.4). On each Moser slab $[\tau_k,t]$ with $\tau_k\ge t/2$, either $\int_{\tau_k}^t\mathcal S^2Y\le\int_0^t\mathcal S^2Y\le C\gamma^3$ or $\sup_{[\tau_k,t]}\mathcal S^2Y\le C\gamma^3/\tau_k$ times slab length gives the same $C\gamma^3$: bounded, $p$-independent. Confirms (6.8a)/(4.7)–(4.8). The $t^{-1}$ blow-up as $t\to0$ is harmless because the slabs live at $\tau_k\ge t/2>0$ while the seed uses the finite time-integral. This chronology is stated correctly and is the right resolution.

**No circularity.** The $Y$-input is controlled by the curvature $q=2$ seed and Sobolev interpolation alone (§3), independent of the defect Moser output; the three-factor route (step62 §4) uses $\mathcal S^2Y$ only as an externally supplied integrable coefficient. This is consistent.

**Endpoint volume cancellation verified in all regimes.** With the repaired time-integrated seed $I_0=\int_{t/2}^tJ_6\le CtJ_6(0)\le Ct\delta^6V$ (no Sobolev factor) and (5.8) $\|aE(t)\|_\infty\le C\mathcal S^{1/3}t^{-1/2}I_0^{1/6}$:
$$
C\mathcal S^{1/3}t^{-1/2}(Ct\delta^6V)^{1/6}
=C\delta\,\mathcal S^{1/3}V^{1/6}t^{-1/3}
=C\delta\,(r^2V^{-1/2})^{1/3}V^{1/6}t^{-1/3}
=C\delta(r^2/t)^{1/3}.
$$
$V$ cancels for all $\mathcal S$, confirming (5.9)–(5.10). The two endpoint forms (5.4) with $t^{-1/3}$ and (5.8) with $t^{-1/2}$ are mutually consistent because $I_0\approx t\Lambda_0$ converts $t^{-1/2}I_0^{1/6}$ into $t^{-1/3}\Lambda_0^{1/6}$. The step62 finding that the general-$p$ two-factor absorption needs $\gamma_t\le c/p$ (Prop. 3.2, from $\|\nabla z_p\|_2^2\le Cp^2(Q_p+r^{-2}J_p)$ and reaction $Cp\cdot P_p\le Cp^3\gamma_tQ_p$ against $c_2p^2Q_p$) is algebraically correct, and the switch to the three-factor $\mathcal S^2Y$-coefficient route for the ladder is the right structural move.

**What remains most load-bearing here.** (i) The index-level curvature variation (step34 eq. 2.14) with $|\nabla B|\le CF|\nabla\operatorname{Rm}|$, which underlies the $Y$-input the whole defect ladder consumes — still open. (ii) Kato regularization $s_\varepsilon=|E|^2+\varepsilon$ for the non-integer ladder exponents $p_k=6(3/2)^k$ and the endpoint limit $J_p^{1/p}\to\|aE\|_\infty$ near $a=0$ (cleaner via $z_p^{2/p}\to a|E|$). (iii) The uniformity $\mathcal S(t)\le2\mathcal S(0)$, $K_2^\eta(t)\le CK_2^\eta(0)$ is not a standalone fact: it is delivered by the coupled $(\Gamma,V)$ first-exit closure (step55 eq. 6.11), where the curvature endpoint feeds $\Gamma$ and this defect endpoint feeds the $V$-improvement (6.10). Interface 2's coherence therefore hinges on both endpoints closing simultaneously, not on the defect endpoint alone; that mutual closure is the right thing to write out explicitly.

## 3. Landscape correction: logically correct

The statement that "$\delta_-\to0$ plus all-sign Einstein nonexistence defeats only the negative branch" is sound, and the underlying reason is a scaling argument worth making explicit.

The pinching $c_ng\le\operatorname{Ric}_g\le C_ng$ transforms under $g\mapsto\lambda g$ into $\lambda c_ng\le\operatorname{Ric}_g\le\lambda C_ng$ (Ricci is $0$-homogeneous). So rescaling slides an admissible interval but preserves the sign-type of the cone it cuts out. A manifold carrying metrics with $\operatorname{Ric}\approx-g$ (negative-definite Ricci) can be rescaled to satisfy intervals with $C_n<0$ only; it can never satisfy an interval with $c_n\ge0$, which demands positive Ricci. A refutation of the displayed proposition must exhibit, for **every** admissible $[c_n,C_n]$, a manifold with a pinched metric and no Einstein metric. A single-sign near-Einstein family with an Einstein obstruction therefore reaches only the sub-family of intervals of that sign; the positive-forcing intervals (and any near-flat mixed intervals) need an independent construction. The correction is correct.

Two refinements for the write-up:

- The reduction to "two forcing signs in the same dimension" captures the essential extremes (the narrowest intervals near $\operatorname{Ric}\approx\pm g$, where pinching is strongest and refutation hardest), but a fully rigorous refutation still ranges over the two-parameter family $(c_n,C_n)$; wide intervals are easier to defeat (more metrics qualify), narrow ones harder. Stating the interval-uniformity across the family, not only the two endpoints, is the precise form.
- As step68_global_yau26_landscape itself records, current candidates achieve **neither** branch cleanly: $E_D$ has $\delta_-\to0$ but negative Einstein existence is open (equivalently, full-curvature-energy attainment $\int|\operatorname{Rm}|^2=8V_*$ is undecided), while extended graph four-manifolds have Di Cerbo Einstein nonexistence but no $\delta\to0$ family. So even the negative branch is not yet defeated by a single manifold carrying both properties. The correction's caution is appropriate and consistent with the assembled IL theorem, which points the other way — it is a near-negative-Einstein **obstruction** on the $q\ge0$ IL geography (no metric with $\|E\|<\varepsilon_{\rm IL}$), i.e., evidence for the negative branch on those topologies rather than a refutation ingredient.

## 4. Adjacent load-bearing item feeding both interfaces

The two verified interfaces feed a contradiction whose driving inequality is the terminal calibration (§3, cited to step67). I confirmed the exact square identity (3.6):
$$
\tfrac{s^2}{24}+2\nu^2=\tfrac1{12}f^2+\tfrac1{216}(s+8\sqrt6\,\nu)^2,\quad f=\tfrac23s-2\sqrt{2/3}\,\nu,
$$
by expansion: the $s^2$ coefficients sum to $\tfrac1{27}+\tfrac1{216}=\tfrac1{24}$, the $\nu^2$ coefficients to $\tfrac29+\tfrac{16}9=2$, and the $s\nu$ cross terms cancel ($-\tfrac29\sqrt{2/3}+\tfrac{2\sqrt6}{27}=0$ using $\sqrt{2/3}=\sqrt6/3$). The density $s+8\sqrt6\nu$ vanishes at the forbidden germ profile $s=-4,\ \nu=1/(2\sqrt6)$, consistent with it measuring deviation from the Kähler–Einstein configuration.

However, the passage from (3.6) with the mixed SW averaging (3.3) and Chern–Weil deficit (3.4) to (3.7) — $\int(s+8\sqrt6|W^+|)^2\le108Q$ and $\int\mathcal G\le6Q$, hence $\int\Phi\le119Q$ — is **not reconstructible from the provided text**. The issue is precise: $4\pi^2I=\tfrac1{12}\int f^2+\tfrac1{216}\int(s+8\sqrt6\nu)^2$ and $I=J+\tfrac{2A}{3}-q$ carry an $A$-proportional term, so bounding $\int(s+8\sqrt6\nu)^2$ by $Q$ (which is $O(\delta_i^2A_i)=o(A_i)$) rather than by $O(A_i)$ requires the $\tfrac{2A}{3}$ to cancel through the SW lower bound (3.3) and the $a_*=\tfrac23s+2w$ negative-part structure in (3.5). This cancellation — turning $\int\Phi$ from $O(A_i)$ into $o(A_i)$ — is the entire engine of the §9 contradiction (it must beat the forbidden-germ lower bound $\int\Phi\gtrsim A_i$ from the proportional plateau volume). It is the single most valuable thing to display explicitly, because both verified interfaces are only useful insofar as they deliver a smooth terminal metric on which this $o(A_i)$ calibration holds. I could confirm the exact identity but not the coefficient $108$ nor the $A$-cancellation from what is here.

## Summary

Both repaired interfaces are mathematically coherent as stated, and the specific corrections over the pre-repair Step 68 text (Sobolev-constant collapse growth; time-zero integrated versus positive-time slab curvature coefficient; time-integrated seed for volume cancellation) are genuinely required and correctly executed. The scaling logic behind the negative-branch landscape correction is sound. The remaining most load-bearing expansions, in order of how much they carry: (1) the index-level tensor energy inequalities for the cutoff flow including $|\nabla B|\le CF|\nabla\operatorname{Rm}|$ — shared premise of both interfaces; (2) the per-datum degenerate DeTurck existence theorem; (3) the simultaneous $(\Gamma,V)$ first-exit closure that supplies the Sobolev/energy uniformity both endpoints assume; (4) the explicit $A$-cancellation in the terminal calibration (3.7), which converts the whole assembly into an $o(A_i)$ contradiction and is not visible in the supplied files.
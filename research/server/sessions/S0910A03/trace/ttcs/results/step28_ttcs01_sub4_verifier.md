# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step21_corrections_from_ttcs_and_peers.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md"
  ]
}
```

## Task

Independently check the downstream geometric passage from the terminal cutoff-flow metrics to the forbidden calibrated Einstein germ. Focus on whether the good-support/Vitali construction truly supplies a positive-volume set with a fixed terminal-metric geodesic buffer; whether the exponential-pullback averaging inequality supplies a noncollapsed smooth chart despite collapse and sheet multiplicity; whether global terminal L2 defect can be converted, after rebuilding the Seiberg-Witten objects for that same terminal metric, into one joint nonnegative density whose pullback limit has nonzero harmonic self-dual form in the lowest W+ eigenspace; and whether the Step 6 projector/Einstein-Weyl contradiction then follows. Distinguish fixed topology from varying topology. Identify every load-bearing statement still asserted rather than proved, and formulate the shortest rigorous bridge that would close it if possible.

## Output

# Verification memo: terminal cutoff-metric → forbidden calibrated Einstein germ

## 1. Where the passage actually stands

I traced the chain A→F: (A) good-support/Vitali plateau, (B) exponential-pullback averaging, (C) smooth chart convergence, (D) rebuilding Seiberg–Witten data on the terminal metric and assembling one nonnegative density, (E) the chart-limit self-dual form in the lowest $W^+$ eigenline, (F) the projector/Einstein–Weyl contradiction.

The result of the check is sharp and, I think, useful: **on the fixed critical Ishida–LeBrun manifold, every algebraic and geometric-measure piece I can verify independently is correct, and the whole chain collapses onto one unproved parabolic input** — the transition-inclusive cutoff-flow smoothing theorem that simultaneously delivers metric comparability, relative-Sobolev persistence, energy persistence, a weighted curvature $L^\infty$ bound, and an integrable weighted defect $L^\infty$ bound, with constants that do not degenerate under collapse. Everything downstream of that theorem is either verified below or reduces to standard Shi/elliptic theory applied on the plateau it would produce. This single input is exactly what Step 16 §5, Step 23 §7, and the hypothesis (1.2) of Step 27 leave open, and what the absent "Step 26" (eq. (8.1)) asserts.

I set out the verified parts first, then isolate the input, then the two-topology distinction and the shortest closing bridge.

## 2. Step F (projector + Weyl–Weitzenböck) — arithmetic verified

The Derdziński-type lemma and the Einstein Weitzenböck arithmetic are internally consistent and force a genuine contradiction.

- Lemma: $\delta W^+=0$ with $W^+=\mu I+(\lambda-\mu)P_\omega$, $\lambda\neq\mu$ constant, gives, after contracting the divergence with $\omega^{cd}$ (constant $|\omega|^2$ kills the $\nabla|\omega|^2$ term), first $\nabla^a\omega_{ab}=0$, then $\omega_{ab}\nabla^a\omega_{cd}=0$; nondegeneracy $\omega_a{}^c\omega_c{}^b=-\delta_a^b$ then yields $\nabla\omega=0$, hence $\nabla W^+=0$. This matches Derdziński 1983 Prop. 5. The first term in eq. (1) is correctly retained.
- Weitzenböck values: with $s=-4$, $|W^+|^2=1/24$, $\det W^+=-1/864$, the note's scalar identity $\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$ at constant modulus gives $2|\nabla W^+|^2=-s|W^+|^2+36\det W^+=\tfrac16-\tfrac1{24}=\tfrac18$, i.e. $|\nabla W^+|^2=1/16$. I recomputed the sign bookkeeping both ways; the value $1/16$ is the one consistent with $|\nabla W^+|^2>0$, and it is nonzero. This contradicts $\nabla W^+=0$.
- The lemma applies because the chart limit is Einstein ($\delta W^+=0$ automatically) and has two distinct constant eigenvalues $(-1/6;\,1/12,1/12)$, with $-1/6$ simple.

I also confirmed the spectrum is forced pointwise on the whole open chart, not just at the center: $\mathscr A_\infty H_\infty\equiv 0$ with $|H_\infty|\equiv 3/(4\sqrt2\pi)>0$ makes the lowest eigenvalue $-\sqrt{2/3}\,|W^+|=-1/6$ everywhere; combined with $\mathrm{tr}=0$ and $|W^+|^2=1/24$ this gives $(1/12,1/12)$ for the other two at every point. So constancy on an open set — which the projector lemma requires — is genuinely produced, not assumed.

**Step F is sound conditional only on the chart limit being smooth Einstein with that constant calibrated spectrum and a nonzero lowest-eigenline harmonic form.**

## 3. Steps D–E (terminal deficit → joint density → limit form) — verified on fixed topology, one important simplification

The most consequential thing I checked is that **the terminal metric need not be pointwise near-Einstein**; the entire deficit chain is driven by the single scalar $Q(T_0)=\int|E|^2$.

- $\mathrm{Ric}^\circ = E - \tfrac14(\mathrm{tr}E)g$, so $|\mathrm{Ric}^\circ|^2=|E|^2-\tfrac14(\mathrm{tr}E)^2\le|E|^2$ and $R=\frac1{8\pi^2}\int|\mathrm{Ric}^\circ|^2\le Q/(8\pi^2)$. This uses no pointwise $\delta$ at terminal time.
- The selected-sign bound (30) $\Delta_\epsilon\le 108\pi^2 R$ uses only: the exact topological identity $I-R=2A/3$ (Gauss–Bonnet + signature, which I re-derived), the pointwise algebra $K\le\frac32 I$ from identity (18) (verified: $27(\tfrac{s^2}{24}+2w^2)-(s-\sqrt6 w)^2=\tfrac18(s+8\sqrt6 w)^2\ge0$), and a sign with $p_\epsilon\ge A$ from sign-averaging. Hence $\Delta_\epsilon\le 108\pi^2 R\le 13.5\,Q(T_0)\to 0$.

Because the flow persistence gives $Q(T_0)\le e^{C\theta}Q(0)$ and $Q(0)\le\delta_i^2\,\mathrm{Vol}\to 0$ on fixed topology, all monopole near-saturation quantities on $g_i(T_0)$ tend to zero: (17)+(37) give $\||H_i|-\tfrac{3}{4\sqrt2\pi}\|_2^2\le CQ$, the Weyl term $(q^+-\tfrac92)$ tends to zero in $L^2$, and the eigenline term $\int_{P_i}\langle\mathscr A_iH_i,H_i\rangle\le C(K)Q$ with $\mathscr A_i=W_i^++\sqrt{2/3}|W_i^+|I\ge0$ pointwise. So the joint density $\mathcal D_i$ is genuinely nonnegative and $\int_{P_i}\mathcal D_i\to0$.

Two points I verified that matter for correctness:
- The transported object in $\mathcal D_i$ is the **Hodge-harmonic representative $H_i$** (smooth, metric-canonical), not a monopole; the "no canonical monopole sequence" remark about the non-smooth optimal weight $f=\sqrt q$ therefore does not obstruct the chart limit. The regularized diagonal choice $f_{k(i)}$ only proves the deficit bounds on $H_i$.
- The positive-part repair $r_i=q_i^+$ is necessary because $q_i$ need only approach $9/2$ in $L^2$; the extra term $N_f\ge0$ keeps the deficit decomposition nonnegative. This is algebra-checked by `verify_positive_part_monopole_algebra.py`.

Given smooth chart convergence (Step C), $\int\mathcal D_i\circ\exp\to0$ forces $E_\infty\equiv0$, $q_\infty^+\equiv9/2$, $|W_\infty^+|\equiv 1/(2\sqrt6)$, $|H_\infty|\equiv 3/(4\sqrt2\pi)>0$, $\mathscr A_\infty H_\infty\equiv0$. **Steps D–E are sound on fixed topology, conditional on Step A/C.**

## 4. Step B (exponential-pullback averaging) — fully verified, and genuinely collapse/sheet-robust

I checked the lemma line by line and it is correct.

- Denominator: $\mathrm{Vol}_{h_p}B_r(0)\ge\omega_{n-1}\int_0^r s_K^{n-1}$ (Rauch lower Jacobian). Numerator: $\int_{B_r(0)}F\circ\exp_p\,d\mu_{h_p}\le\int_0^r s_{-K}^{n-1}\!\int_{S_pM}F(\gamma_{p,\theta}(t))\,d\theta\,dt$ (Rauch upper Jacobian, $F\ge0$).
- The Liouville step is exactly right: for $G=F\circ\pi$ on $SM$, $\int_{SM}G(\phi_t z)\,dL=\int_{SM}G\,dL=\omega_{n-1}\int_M F\,d\mu_g$. Enlarging $SM|_P\to SM$ (valid since $F\ge0$) and dividing gives $C(n,K,r)=\int_0^r s_{-K}^{n-1}/\int_0^r s_K^{n-1}$.

Two features I want to affirm because they carry the argument against collapse:
1. **The pullback chart is noncollapsed by construction.** Its $h_p$-volume is $\ge\omega_{n-1}\int_0^r s_K^{n-1}$, a fixed positive number depending only on $(n,K,r)$, even where $B_r(p)\subset M$ is arbitrarily collapsed. Multiple exponential sheets are folded back by the measure-preserving geodesic flow; no injectivity-radius or sheet count enters. With $K\sim C/r^2$ and averaging radius a fixed small multiple of $r$, $C(n,K,\cdot)$ is a fixed constant, uniform under collapse.
2. **Injectivity radius at the chart center is $\ge$ the averaging radius.** In $(B_r(0),h_p)$ geodesics from $0$ are the straight rays $t\theta$; conjugate points along them occur at distance $\ge\pi/\sqrt K$, and $r<\pi/(2\sqrt K)$, so $\mathrm{inj}_{h_p}(0)\ge$ averaging radius. This is what lets the later Cheeger–Gromov–Hamilton compactness produce a limit centered at $0$.

So the averaging lemma does exactly what is asked: from a positive-volume bounded-$\sec$ set with small $\int\mathcal D_i$, it selects $p_i$ with a fixed-radius, fixed-volume, unit-injectivity-radius pullback chart on which $\int\mathcal D_i\circ\exp\to0$. **This step is unconditional given a positive-volume bounded-$\sec$ plateau.** Its input requirement — that radius-$r$ geodesics from good points stay in $\{|\sec|\le K\}$ with $r<\pi/(2\sqrt K)$ — is a geometric consequence of Step A.

## 5. Step C (smooth convergence) — reduces to Shi estimates on the plateau

Bounded $\sec$ alone is not enough for $C^\infty$ chart convergence; the material states this correctly. Smooth convergence needs uniform $|\nabla^m\mathrm{Rm}_{h_{p_i}}|$, i.e. uniform $|\nabla^m\mathrm{Rm}_{g_i}(T_0)|$ on the buffered plateau. These are exactly the interior Shi estimates for the smoothing flow that ran on $B_{4r}(p_j)$ (where $a=1$) for time $T_0=\theta r^2$: $|\mathrm{Rm}|\le K$ there gives $|\nabla^m\mathrm{Rm}(T_0)|\le C_m K/r^m$ on $B_{2r}$. With the noncollapsed chart from Step B and these bounds, Cheeger–Gromov–Hamilton gives the smooth Einstein limit $g_\infty$ ($\mathrm{Ric}=-g_\infty$ from $E_i\to0$ in pullback + smooth convergence), and interior Hodge/elliptic estimates give the smooth self-dual harmonic $H_\infty$ with $|H_\infty|=c_0>0$ (the pullback amplitude $\to c_0$ in $L^2$, upgraded to $C^0$ by ellipticity). **Step C has no gap of its own; it inherits the plateau curvature and its derivatives from Step A.**

## 6. Step A and the single load-bearing input (★)

This is where the passage is not yet a proof. The good-support/Vitali construction supplies a positive-volume, fixed-geodesic-buffer, bounded-$\sec$ terminal-metric plateau **if and only if** the cutoff flow can be run to $t=\theta r^2$ with the plateau estimates. Concretely, the construction needs, with constants independent of collapse:

- **(★) A transition-inclusive normalized cutoff-flow existence/continuation theorem** for $\partial_t g=-2a(\mathrm{Ric}+g)$, $a=\sum_j\chi_j^2$, on $[0,\theta r^2]$, jointly delivering
  - (F1) metric comparability $\tfrac12 g_0\le g(t)\le 2g_0$ on the active support;
  - (F2) relative-Sobolev persistence with a fixed multiple of the initial coefficient;
  - (F3) local curvature-energy and defect-energy persistence ($H_{2,j}$, $J_{6,j}$, global $Q$);
  - (F4) the weighted curvature $L^\infty$ bound $|a\,\mathrm{Rm}(t)|\le C\gamma/t$;
  - (F5) the integrable weighted defect $L^\infty$ bound $|aE(t)|\le C\delta(r^2/t)^{\gamma}$, $\gamma<1$.

What is genuinely established in the provided material, and what is asserted:

- **Established (on the provisional comparability/Sobolev interval):** the integrated $q=2,3$ curvature inequality (2.7) with the cutoff Hessian removed by one integration by parts and the identity $|da|^2/a=4|d\chi|^2$; component $H_2$ persistence (3.5), spacetime $H_3$ (3.6), the fixed-$q=3$ terminal estimate (4.4); global $Q$ amplification (5.3) with no curvature-only source; fixed $J_6$ persistence (5.6) keeping the $\delta^6$ factor. The disjoint-support simplification (Step 23 §1) correctly removes the earlier inner/outer neighbor-dissipation obstruction and the neighbor-graph. The exact-model and homothetic sign checks (§6) are consistent. Step 27 rigorously converts hypothesis (F4) into smooth continuation, per sequence member, via the shifted curvature $T=\mathrm{Rm}+G$; I find its architecture credible (the highest cutoff term $\chi\nabla^{m+2}\chi*U$ is lowered one order by (3.5)–(3.6), and $G$-terms are bounded linear).

- **Asserted, not derived here:**
  1. The passage from the integral hierarchy (4.4) to the pointwise (F4) $\|a\mathrm{Rm}\|_\infty\le C\gamma/t$ — the whole-support $L^2\!\to\!L^\infty$ Moser iteration — is deferred to the absent "Step 26" (eq. (8.1)). This is the hypothesis Step 27 requires; the continuation theorem cannot run without it.
  2. The weighted-defect (F5) $|aE|\le C\delta(r^2/t)^{2/p}$, $p>2$ — the Deane–Yang/Moser estimate for $aE$ on the whole active support including cutoff terms and finite-neighbor summation — is identified (Step 16 §7) but explicitly not supplied by Wang's source and not derived. Wang Prop. 4.9 / Thm 6.3 obtain their propagation only under a global Sobolev inequality and a global full-support $L^{n/2}$ curvature threshold, stronger than the collapsed relative-ball hypotheses.
  3. The **noncircular closure** of (F1)+(F2) via (F5): metric comparability needs integrable $|aE|$ drift, which needs (F5), which is proved on the comparability/Sobolev interval — a first-exit/continuity structure (Step 21 §9.2) whose strict self-improvement is asserted but not carried out.
  4. Subsidiary geometric-measure statements: disjoint good macro-supports $U_j$ with inner-ball union of fixed positive volume proportion on a collapsed manifold (Step 23 §1); the relative-Sobolev inequality on collapsed balls with coefficient $\mathsf S_j\lesssim r^2\mathrm{Vol}(U_j)^{-1/2}$ and the volume-cancellation $\beta=A_0^2\|\mathrm{Rm}\|_{L^2(B_{r_*})}=Cr_*^2\sqrt{K_0}=C\sqrt{\varepsilon_{\mathrm{Li}}}$ small (Step 21 §9.4, referenced to "Step 19"); $\mathrm{Vol}(P_i)\ge c\,\mathrm{Vol}(M,g_i)$ (Step 21 §9.5). These are plausible and dimensionally consistent (the drift bookkeeping $\int_0^{\theta r^2}\!\!(r^2/t)^{1/3}dt=C\theta^{2/3}r^2$ is finite precisely because the exponent is $<1$), but they rest on the same relative-geometry inputs and on (★).

The verification scripts (`verify_step23_component_wang_bridge.py`, `verify_step27_shifted_curvature_algebra.py`, `verify_deficit_constants.py`) confirm symbolic identities and scalings and exit 0; they do not touch the PDE existence/continuation content of (★).

**Consequently: the fixed-topology Ricci-pinching contradiction rests entirely on (★).** Note also that the *unit-scale* deployment of the same germ contradiction (Step 6, regular-patch transfer via Cheeger–Naber Thm 1.13) is self-contained on fixed topology and appears rigorous; it proves $\sup_p\mathrm{Vol}_{g_i}B_1(p)\to0$, i.e. everywhere-collapse with $\mathrm{Vol}\to32\pi^2A/9$ and diameter diverging. That is a strong structural statement but not itself a contradiction — collapse with bounded volume and unbounded diameter is realizable. The Li-scale deployment (A–F), and hence (★), is what is needed to exclude the collapsed alternative and reach a contradiction.

## 7. Fixed topology vs varying topology

The distinction is handled correctly throughout and is decisive.

- **Fixed critical $M$ ($A$ fixed):** all monopole deficits are absolute $O(A\delta_i^2)$, and at terminal time $O(Q(T_0))\to0$; $R\le Q/(8\pi^2)$; the selected sign is constant on a subsequence; $K_0\le C(M)$ so $r_*>0$ and $\gamma_*\sim r_*^2\sqrt{K_0}$ are uniform; $\mathrm{Vol}\to32\pi^2A/9$ bounds $Q(0)$; the plateau carries a fixed volume fraction. Every piece except (★) closes.
- **Varying topology ($A_i\to\infty$):** deficits are only $o(A_i)$, not absolute $o(1)$; Walsh averaging (31) controls the mean deficit while a sparse set of saturating signs can persist, and a small noncollapsed island can absorb nonvanishing defect. $K_0$ is uniform only on the Noether subclass $\chi/A\le 65/6$; otherwise $r_*\to0$ and the Li/Shi scale degenerates. The material's insistence that "every fixed sign vertex saturates" is a fixed-cube statement only, and that unnormalized volume may diverge, is correct. **The varying-topology case is not covered even granting (★),** and every step correctly restricts its conclusion to the fixed critical four-manifold $\mathrm{Ric}=-g$ branch. The positive normalized branch, $n\ge5$, and the dimension-only interval quantifiers of Yau 26 are untouched.

## 8. Shortest rigorous bridge

Since A–F reduce to (★), the minimal closing content on fixed topology is two Moser-type $L^\infty$ estimates with collapse-uniform constants, plus the first-exit closure that Step 27 then continues:

1. **Weighted curvature ultracontractivity (gives F4).** De Giorgi–Nash–Moser $L^2\!\to\!L^\infty$ for $aF$ on the disjoint good supports, cubic reaction absorbed by the small product $\beta=C\sqrt{\varepsilon_{\mathrm{Li}}}$. Output $\|a\mathrm{Rm}(t)\|_\infty\le C\gamma/t$. The Nash-form reformulation on the conformal measure $d\nu=a^{-2}d\mu$ (Step 21 §9.6) is the most compact route: one $L^2\!\to\!L^\infty$ bound replaces the infinite Moser ladder, provided the non-autonomous Dirichlet form is uniformly closed, the $da$-terms are sector-bounded, and the curvature potential is a small form-perturbation ($\gamma<1$). Developing this is the cleanest single target.

2. **Weighted defect Moser (gives F5).** A Deane–Yang-type inequality $\|aE(t)\|_\infty\le C_p\,\delta(r^2/t)^{2/p}$, $p>2$, on the whole active support with cutoff terms and finite-neighbor summation, yielding $\int_0^{\theta r^2}\|aE\|_\infty\,dt\le C\delta\,\theta^{1-2/p}r^2$ and hence metric comparability and Sobolev persistence (F1,F2). The scale-check $A_0^{4/p}\|E(0)\|_p\lesssim\delta r^{4/p}$ shows the collapse factor cancels; the time singularity is integrable exactly because $p>2$.

3. **First-exit closure.** Define $\tau$ as the first time any of (F1)–(F5) reaches twice its threshold; use 1–2 to show each strictly improves on $[0,\tau)$, so $\tau=\theta r^2$; then Step 27 continues each sequence member and the maximality contradiction (8.1)→§8 closes.

If 1–3 are established with constants independent of collapse (the $\beta$-cancellation mechanism is the crux), then Steps A–C produce the noncollapsed smooth Einstein chart, Steps D–E give the nonzero lowest-eigenline harmonic form and the constant calibrated spectrum, and Step F closes the contradiction — on the fixed critical Ishida–LeBrun $\mathrm{Ric}=-g$ family. The remaining pieces of Yau 26 (positive branch, all topologies, $n\ge5$, dimension-only constants, Lean formalization) are separate and not addressed by this line.

## 9. Load-bearing statements still asserted rather than proved

1. (★-a) Whole-support weighted-curvature $L^\infty$ bound (8.1) — deferred to absent Step 26; it is the hypothesis of the Step 27 continuation theorem.
2. (★-b) Weighted-defect $L^\infty$ bound $(M_p)$ — identified, not derived; not available from the cited Wang theorems under collapsed relative-ball hypotheses.
3. (★-c) Noncircular joint closure of metric comparability and Sobolev persistence via $(M_p)$ (the first-exit self-improvement).
4. Step 27's verbatim transfer of Wang's Section 4 staggered-exponent induction "with only coefficients changed," including harmlessness of the $G$-terms and the normalized lower-order term.
5. The collapsed relative-Sobolev inequality with coefficient $\sim r^2\mathrm{Vol}^{-1/2}$ and the volume-cancellation $\beta=C\sqrt{\varepsilon_{\mathrm{Li}}}$ (referenced to Step 19, not provided).
6. The disjoint-support covering with inner-ball union of fixed positive volume proportion, and $\mathrm{Vol}(P_i)\ge c\,\mathrm{Vol}(M,g_i)$, on a collapsed manifold.
7. The eigenline constant $C(K)$ in (L) as a function of plateau curvature (its dependence on $K$ is stated but the Weitzenböck route to it is not shown in the provided files).

Items 1–3 are the essential ones; 4–7 are supporting geometric-analytic inputs that would be verified alongside (★). Everything I could check independently — the averaging lemma, the $R\le Q/(8\pi^2)$ reduction and the deficit-to-$Q$ chain, the monopole near-saturation bounds, the amplitude/eigenline forcing of the spectrum, and the projector/Weyl arithmetic — holds.
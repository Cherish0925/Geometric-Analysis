# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Read the corrected Step 25 single-support argument as a PDE/geometric compactness expert. Determine exactly which parts of the simultaneous first-exit are now established and whether the whole-support bounds for a Rm and aE genuinely restore metric/Sobolev/cutoff control before plateau regularity. Then analyze the remaining normalized Yang-Wang existence/continuation adaptation: does bounded |a Rm| together with the derived metric comparison suffice after adding -2ag, or are additional uniform quantities missing? Finally verify that the only justified terminal local obstruction is the Step 6 projector plus Einstein-Weyl identity, not local-symmetry classification. Produce a precise scientific memo that distinguishes proved implications from remaining derivations without reducing the original Yau 26 goal.

## Output

# Verification memo: Step 25 normalized cutoff-flow argument on the critical Ishida–LeBrun four-manifold

I read Step 25 together with the A01 tensor-energy derivation it depends on, the Step 23 single-support bridge, the Step 6 projector note, and the two source papers (Wang's pseudolocality paper and Yang's local-Ricci-flow paper). I re-derived the arithmetic wherever a numerical constant or exponent identity is asserted. Below I separate implications that are actually proved (given the existence input) from the derivations still owed, and I locate each precisely.

## 1. The tensor and energy layer is arithmetically sound

**Scale-neutrality in dimension four (§2).** I confirm the computation. Under the homothetic part $\partial_t g=-2ag$ with $a$ spatially constant, the mixed tensor $R^\ell{}_{ijk}$ is unchanged, so $\partial_t R_{ijkl}=-2aR_{ijkl}$; two curvature factors give $-4ax$, four inverse metrics give $+8ax$, hence $\partial_t x=4ax$ for $x=|\operatorname{Rm}|^2$. With $\partial_t d\mu=-4a\,d\mu$ in $n=4$, $\partial_t(x\,d\mu)=0$. The density identity (2.4), $\partial_t(F^pd\mu)|_{-2ag}=2a[(p-2)F^p-pF^{p-2}]d\mu$, follows from $\partial_tF=2ax/F$ and $x=F^2-1$; at $p=2$ it reduces to $-4a\,d\mu$. The consequence is correct and consequential: the homothety supplies no curvature-proportional sink, only a bounded lower-order measure term. This removes a coercive $-4aF^2$ term that a naive normalized-flow energy estimate could wrongly assume, and it forces the coarse scale-consistent inequality (2.5). This self-correction is genuine and matters.

A conceptual point worth stating: the reason a normalized flow with fixed point $\operatorname{Ric}=-g$ remains compatible with Yang's $L^{n/2}=L^2$ critical-energy machinery is exactly this dimension-four scale-invariance. The homothety term is energy-neutral only in $n=4$. Any attempt to move this program to other dimensions loses this compatibility at §2, which is consistent with the note restricting itself to $n=4$.

**Weak energy inequalities (3.1)/A01 (1.3).** The three inequalities cross-check against A01's index-level derivation. The essential structural fact — that the mixed-index curvature variation (A01 2.2–2.10) produces $\partial_t\operatorname{Rm}=a\Delta\operatorname{Rm}+a\mathcal A(\operatorname{Rm})+(da)*\nabla E+(\nabla^2a)*E$ with **no bare $(\nabla^2a)*g$ source** — is correct: a constant variation $-2g$ does not move the Levi-Civita connection, so the only trace of normalization in $\partial_t\operatorname{Rm}$ is the algebraic $-2aE_{\ell p}R^p{}_{kij}$ of size $\le CaF^2$, the same order as the existing quadratic reaction. Because every Hessian-$a$ term therefore carries a factor $E$ (or $\operatorname{Rm}$), the single integration by parts producing $|da|^2/a=4|d\chi|^2$ is legitimate, and the strict buffer $\operatorname{supp}d\eta\subset\{a=0\}^\circ$ kills all $d\eta$ terms. The defect identity A01 (6.4) correctly carries **no** linear $-4a|E|^2$ damping (it cancels against the $\Delta_L$ Ricci terms after $\operatorname{Ric}=E-g$); the note does not assume any exponential contraction of $|E|^2$, which is the right stance.

**Weighted power inequality (4.2)–(4.7).** I verified the exponent bookkeeping. The factorization (4.4) has $a$-power $\tfrac13+\tfrac23(3p/2-2)=p-1$, $F$-power $1$, $\Phi$-power $p$; the interpolation $K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}$ is Cauchy–Schwarz on $a^{3p/2-2}\Phi^{3p/2}$; and $Z_p^2=\eta^2a^{p-1}\Phi^p$ carries exactly the extra factor $a$ demanded by the degenerate diffusion $a\Delta$. The Young step producing $Cp^3(r^{-2}+\mathsf S^2H_3)K_p$ is correct, and the reduction $\mathsf S^2H_3\le C\beta_*^3/s$ (using $H_3^{1/3}\le C\beta_*\mathsf S^{-2/3}s^{-1/3}$) matches (4.7). The polynomial $p^3$ growth is harmless; only the fixed exponents $2,3$ use current-time smallness.

**Exact match with Yang's fixed-cutoff moments (§5).** For $n=4$, $v=1+2/n=3/2$, so Yang's $p_k=p_0(3/2)^k$ and $p'_{k+1}=\tfrac32p'_k+1$ reproduce (5.1). With $p'_0=p_0-2=p_0-n/2$, induction gives $p'_j=p_j-2$, hence Yang's moment $\chi^{2p'_j}\Phi^{p_j}=a^{p_j-2}\Phi^{p_j}=K_{p_j}$ and endpoint $a\Phi$. The potential exponent $q=6$ gives $\int\chi^{q-4}F^{q/2}=\int aF^3=H_3$. The exponent sums $\sum1/p_j=3/p_0$ and $\sum(j+\log p_j)/p_j<\infty$ are correct, so (5.10) is a legitimate Moser endpoint. This is not a loose analogy: in $n=4$ the present weights and Yang's Appendix-A moments coincide identically.

## 2. The whole-support outputs are correctly computed and play complementary roles

Curvature ($\Phi=F$, $p_0=3$): $K_3[F]=H_3$, $\mathcal M_{3,0}=\int_{t/2}^tH_3\le C\beta_*^3/\mathsf S^2$, and (5.10) gives $\|aF\|_\infty\le C\beta_*(t^{-1}+r^{-2})\approx C\beta_*/t$ for $0<t\le r^2$. Verified.

Defect ($\Phi=|E|$, $p_0=6$): $K_6[|E|]=J_6$, $\mathcal M_{6,0}\le Ct\delta^6V$, $\mathsf S\le Cr^2V^{-1/2}$, and (5.10) gives $\|aE\|_\infty\le C\delta r^{2/3}t^{-1/3}=C\delta(r^2/t)^{1/3}$. The volume powers cancel ($V^{-1/6}\cdot V^{1/6}$), so the defect bound is independent of collapsed volume. The time integral $\int_0^{\theta r^2}\|aE\|ds\le\tfrac32C\delta\theta^{2/3}r^2$ is correct because $s^{-1/3}$ integrates near $0$.

These two bounds are genuinely on the **whole active support** $\operatorname{supp}\chi$ including the transition collar, since the Sobolev test functions $Z_p=\eta a^{(p-1)/2}\Phi^{p/2}$ live wherever $a>0$ and the endpoint is $\|a\Phi\|_{L^\infty(\operatorname{supp}\chi)}$. This does supply what plateau-only estimates could not. The two bounds are not redundant, and their complementarity is the actual engine:

- The **defect** bound $\|aE\|\sim(r^2/t)^{1/3}$ is time-integrable to $t=0$, so through A01 (8.2), $g(t)=e^{\pm2\int\|aE\|ds}g_0$ with exponent $\le C\delta\theta^{2/3}r^2$, giving metric equivalence relative to $g_0$ **all the way to $t=0$**. Because $E$ enters the velocity only through the weight $a$, this is exactly the object needed on the collar, where $a\to0$ and the metric barely moves; one does not need $E$ itself bounded there.
- The **curvature** bound $\|a\operatorname{Rm}\|\sim1/t$ diverges at $t=0$ and therefore cannot by itself close metric equivalence near the initial time; it is the positive-time interior-regularity input on the $a=1$ plateau.

This division of labor is correctly identified and is the substantive advance of Step 25 over Step 23.

## 3. The simultaneous first-exit: what closes and what is presupposed

The continuity/first-exit method here follows Yang's Theorem 9.2 structure (maximal interval on which bilipschitz, Sobolev, and small-curvature-energy hold; show strict improvement; contradict maximality). Given the whole-support outputs, I confirm the four package quantities improve consistently on a fixed interval $[0,\theta r^2]$:

1. **Bilipschitz constant.** Exponent $2\int\|aE\|ds\le C\delta\theta^{2/3}r^2$; with $r\le1$, $\theta\le1$, this is $\lesssim\delta$, strictly below any preset margin for small $\delta$. (The dimension works out because $r^2$ here is the flow-time span, bounded by $1$; A01 §8.7's $r\le1$ convention is what makes the exponent small rather than large.)
2. **Sobolev constant.** Follows from bilipschitz metric+measure comparison; on $U_j\setminus\operatorname{supp}\chi$ the metric is stationary ($a=0$), so persistence there is exact, and on $\operatorname{supp}\chi$ it is controlled by (1). Improves with the bilipschitz constant.
3. **$|d\chi|_{g(t)}$.** Fixed $\chi$; $|d\chi|_{g(t)}^2\le\Lambda|d\chi|_{g_0}^2$, improves with $\Lambda$.
4. **$\beta(t)=\mathsf S\|F\|_{L^2(\operatorname{supp}\chi)}$.** Here the wording "self-improves" is slightly optimistic. The $q=2$ estimate gives $H_2(t)\le e^{Ct/r^2}H_2(0)$, which **grows**, so $\beta$ does not decrease; it **persists below threshold with a multiplicative margin $e^{C\theta}$**. The first-exit closes because the initial margin $\beta(0)\le Cr^2\sqrt{1+K_0}$ (collapse-independent, achievable by choosing the Li scale $r$ small) absorbs $e^{C\theta}$. This is correct provided the threshold is set with that margin; it should be stated as controlled persistence rather than monotone improvement.

The terminal estimate (3.2)/(4.4) is obtained the right way: the spacetime cubic bound $\int_0^tH_3\,ds$ selects a good slice $s\in[t/4,t/2]$, and the **separate** $q=3$ differential inequality $H_3'\le Cr^{-2}H_3$ propagates that slice to time $t$, excluding terminal spikes. This correctly avoids inferring a pointwise-in-time bound from a time integral alone (the error the notes attribute to Step 22).

**Therefore the a priori side of the first-exit closes** — conditional on two things that Step 25 does not itself derive:

**(A) Existence/smooth continuation of the degenerate normalized flow** (treated in §5 below).

**(B) The relative Sobolev inequality (1.1)/(3.1) on the selected supports with scaling $\mathsf S\le Cr^2V^{-1/2}$.** This is explicitly assumed ("On a provisional smooth bilipschitz interval assume the relative four-dimensional Sobolev inequality"). Its geometric validity in the collapsed setting is not established here. Yang's route to such a volume-normalized inequality (Theorem 6.2/7.4) uses a volume lower bound $\operatorname{Vol}B(x,\tau r)\ge w(n)(\eta\tau r)^n$ — precisely the condition that **fails under the unit-scale collapse that Step 6 (10) establishes**. The final outputs are collapse-independent because $\mathsf S^{2/p_0}$ and $\mathcal M^{1/p_0}$ carry canceling powers of $V$, but the inequality must still hold as an inequality with finite $\mathsf S$ for the iteration to run. Whether a relative Sobolev/Poincaré inequality of this form holds on a genuinely collapsed macro-support is exactly the "collapsed-ball unwrapping to noncollapsed harmonic charts" question that Step 6's closing section flags as open. This is the most load-bearing unproved geometric input, and it links directly to (B) in Step 6.

A related presupposition is the **good-macro-support construction** (Vitali selection giving disjoint $U_j$ of fixed volume proportion with $\fint_{U_j}F(0)^2\le CK_0$). Step 23 §1 constructs it; I take it as given, but note it feeds both the relative-Sobolev assumption and the initial-data placement $J_6(0)\le\delta^6V$.

## 4. Normalized Yang–Wang continuation: structural adaptation and what is genuinely owed

**Short-time existence for the normalized degenerate flow is essentially free.** Yang's Theorem 8.2 (DeTurck symmetry-breaking, or the $\varepsilon^2+\chi^2$ strictly-parabolic regularization) applies to $\partial_t g=-2\chi^2\operatorname{Ric}$; adding $-2\chi^2g$ is a smooth zeroth-order (in metric derivatives) reaction, so the DeTurck-modified system stays strictly parabolic and the same fixed-point/energy argument gives short-time existence. The note's assertion here is correct and is not an unfilled step.

**Bounded $|a\operatorname{Rm}|$ plus the derived metric comparison is structurally the right pair, but the continuation induction must be written.** Wang's Theorem 4.1 extends $\partial_t g=-2\chi^2\operatorname{Ric}$ past $T$ given uniform $|\chi^2\operatorname{Rm}|_\infty$, via the coupled induction on $|\nabla^m(\chi^2\operatorname{Rm})|_p$, unweighted $|\nabla^m\operatorname{Rm}|_p$, and $|\nabla^m\chi|_p$ (his Lemmas 4.4–4.6, 4.10–4.11, Props 4.13–4.14). For the normalized flow, splitting $-2aE=-2a\operatorname{Ric}-2ag$:

- In $\partial_t\operatorname{Rm}$ the added term contributes only the algebraic $CaF^2$ piece (same order as Wang's existing quadratic reaction) — no new principal or derivative structure.
- In Wang's cutoff-velocity Lemma 4.6, $\chi^2E=\chi^2\operatorname{Ric}+\chi^2g$ with $\nabla^k(\chi^2g)=(\nabla^k\chi^2)g$ (since $g$ is parallel). The extra terms are **pure cutoff derivatives $\nabla^k a\cdot g$ with no curvature**, which feed Wang's $|\nabla^m\chi|_p$ hierarchy without introducing a new curvature-order unknown. Wang's order-counting chain (his Remark 4.2) is not disrupted, because the new terms sit entirely in the cutoff-derivative slot.

So no additional uniform **curvature-order** quantity beyond the derivative hierarchy Wang already controls is needed. What is genuinely owed is the term-by-term rewriting confirming that:

1. the $\nabla^k a\cdot g$ contributions close in Wang's Lemma 4.6 and Props 4.13–4.14 (this is very likely, since they are lower order, but it is not yet on paper);
2. the $|\nabla^2\chi|_p\leftrightarrow|\nabla(aE)|_p$ interplay (Wang's Lemma 4.11, his stated reason for bounding $|\nabla^2\chi|_p$ first) still closes with $E$ in place of $\operatorname{Ric}$;
3. the near-$t=0$ metric equivalence — where Wang's Prop 4.9 route via bounded $|\chi^2\operatorname{Rm}|$ is unavailable because $|a\operatorname{Rm}|\sim1/t$ diverges — is instead supplied by the **time-integrable defect** (6.5)/(6.6). This substitution is the correct one and is the second reason the defect bound is indispensable; it should be made explicit in the written continuation, since $\int_0^t|a\operatorname{Rm}|\,ds\sim\log(t/t_0)$ alone would give metric equivalence only on positive-time subintervals with growing constants.

In short: the continuation is not blocked by a missing quantity; it is blocked only by an unwritten but structurally routine adaptation, with the one non-routine ingredient (metric equivalence to $t=0$) already produced by (6.5).

## 5. The terminal local obstruction is the projector lemma plus the Einstein–Weyl identity, and nothing more

I verified Step 6's terminal contradiction independently.

**Projector lemma.** With $W^+=\mu I+(\lambda-\mu)P_\omega$, $\omega$ a constant-norm eigenform ($|\omega|^2=2$), $\delta W^+=0$ gives $(\nabla^a\omega_{ab})\omega_{cd}+\omega_{ab}\nabla^a\omega_{cd}=0$. Contracting with $\omega^{cd}$ and using $\nabla|\omega|^2=0$ kills the second term, so $\nabla^a\omega_{ab}=0$; back-substitution gives $\omega_{ab}\nabla^a\omega_{cd}=0$, and since a nonzero self-dual two-form is invertible ($\omega_a{}^c\omega_c{}^b=-\delta_a^b$), $\nabla\omega=0$, hence $\nabla W^+=0$. The argument uses only $\lambda\ne\mu$, not the sign of either eigenvalue, and matches Derdziński 1983 Prop 5 (primary text cited by line range). The "$\nabla^a\omega_{ab}$ must not be omitted" remark is the correct repair of the Step 5 incompleteness.

**Einstein–Weyl scalar identity.** For the calibrated spectrum $(-1/6,1/12,1/12)$: $|W^+|^2=\tfrac1{36}+\tfrac1{144}+\tfrac1{144}=\tfrac1{24}$ and $\det W^+=-\tfrac1{864}$. With $\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$, $s=-4$, and $|W^+|^2$ constant (so $\Delta|W^+|^2=0$): $0=2|\nabla W^+|^2-\tfrac16+\tfrac1{24}$, giving $|\nabla W^+|^2=\tfrac1{16}$. This contradicts $\nabla W^+=0$ from the lemma. Arithmetic verified.

**No local-symmetry classification is used.** The contradiction lives entirely at the level of $W^+$ and its first covariant derivative: the lemma forces $\nabla W^+=0$, the Weitzenböck scalar identity forces $|\nabla W^+|^2=1/16$. The note is right that parallel $W^+$ does not imply the full curvature is parallel, and it does not invoke any classification of parallel-$W^+$ manifolds. The double-eigenvalue structure the lemma requires (simple $-1/6$, double $1/12$, distinct) is exactly what the trace-free $3\times3$ equality case in the regular-patch transfer produces (Step 6 (9)), and the constant calibrated spectrum is forced by the absolutely-convergent-to-zero eigenvalue/monopole defects at fixed $A$. This is the LeBrun completion-of-square rigidity; I did not re-derive the Seiberg–Witten amplitude $|H_\infty|=3/(4\sqrt2\pi)$ or the monopole eigenline placement, which are inherited inputs, but the logical assembly and the two decisive identities are correct.

## 6. Relation to the full Yau 26 statement

Both notes state, correctly, that this addresses only the critical four-dimensional Ishida–LeBrun family with $\lambda<0$, not the dimension-by-dimension statement. Two facts should be kept in view without shrinking the target:

- The pinching actually processed is the almost-Einstein defect $\delta_i=\|g_i^{-1}(\operatorname{Ric}+g_i)\|_\infty\to0$ (i.e. $\operatorname{Ric}\approx-g$), which is far stronger than the two-sided $c_ng\le\operatorname{Ric}\le C_ng$ of Yau 26. The strategic bridge from a two-sided Ricci window on an Einstein-obstructed four-manifold to this near-Einstein regime is not contained in these files and would have to be supplied separately.
- The $n=4$ scale-invariance at §2 is what makes the normalized flow compatible with the $L^{n/2}$-critical machinery; the whole apparatus is intrinsically four-dimensional. The general $n\ge2$ statement — including the existence of dimension-only constants $c_n<C_n$ — is untouched by this program and would require different structure.

The original goal (all $n\ge2$, all closed connected smooth manifolds, quadratic-form pinching, either a full proof or a rigorous refutation, with Lean formalization) therefore remains fully open; what is being built is machinery on one four-dimensional testing family.

## 7. Consolidated ledger

**Established (given existence input and the two assumed geometric inputs):** §2 scale-neutrality; the three weak energy inequalities with no $(\nabla^2a)*g$ source; the weighted power inequality and its Young absorption; the exact identity with Yang's fixed-cutoff moments; the Moser endpoint; the whole-support bounds $\|a\operatorname{Rm}\|\le C\beta_*/t$ and $\|aE\|\le C\delta(r^2/t)^{1/3}$ with the integrable-in-time consequence; the internal self-consistency of the first-exit improvements for bilipschitz, Sobolev, $|d\chi|$, and (as controlled persistence) $\beta$.

**Presupposed, not derived here:** (A) smooth existence/continuation of the degenerate normalized flow on $[0,\theta r^2]$ — short-time existence is immediate, but the uniform higher-derivative normalized Wang induction is unwritten (items 1–3 of §4), with the near-$t=0$ metric equivalence correctly delegated to the defect bound; (B) the relative Sobolev inequality $\mathsf S\le Cr^2V^{-1/2}$ on the selected supports in the collapsed geometry, whose usual derivation route rests on a volume lower bound that collapse removes — this is coupled to Step 6's open unwrapping question; and the good-macro-support construction that feeds both.

**Terminal obstruction:** verified as the projector lemma plus the Einstein–Weyl scalar identity, self-contained at the $W^+$/$\nabla W^+$ level, without local-symmetry classification.

The single most decisive unproved element, in order of leverage on the argument's correctness, is the relative Sobolev inequality in collapse (it is the hypothesis under which every energy absorption in Steps 23 and 25 runs), followed by the written normalized continuation induction (structurally routine, one non-routine ingredient already supplied), followed by the strategic connection of the near-Einstein four-dimensional family to the two-sided pinching statement of Yau 26.
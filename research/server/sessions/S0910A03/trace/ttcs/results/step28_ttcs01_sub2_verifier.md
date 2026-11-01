# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md"
  ]
}
```

## Task

Independently check the complete analytic chain for the normalized cutoff flow on the selected disjoint supports. Read the actual derivations, not their status labels. Determine whether the q=2 and q=3 estimates, global Q and J6 propagation, general-p tensor inequality, three-factor/time-slab Moser iteration, first-exit closure, and shifted-curvature continuation form a logically closed proof with volume-independent constants for a fixed critical four-manifold. Attack the most consequential non-routine transitions: active-region versus collar energy, use of the unweighted F factor, relative Sobolev domains, polynomial p dependence, terminal H3 propagation, the t=0 splice, and the current-order Wang derivative induction. State any precise missing lemma or false inference, with equations and a concrete repair if available. Do not infer validity from scripts or prior summaries.

## Output

# Verification Memo: Analytic Chain for the Normalized Cutoff Flow (4D Negative Ishida–LeBrun Branch)

I read the derivations directly and reconstructed the load-bearing algebra. Below is what holds, what I verified by independent computation, the one place where an earlier formulation was incorrect and later repaired, and the precise statements that are still asserted rather than derived. I ignored exit-code lines and status labels.

## 1. Overall assessment

For a **fixed** critical four-manifold at **fixed** pinching parameter δ, the parabolic portion of the chain — good-support selection, relative Sobolev, q=2/q=3 energy, terminal H₃, global Q and J₆, the general-p inequality, the three-factor/time-slab Moser iteration, first-exit self-improvement, and the shifted-curvature continuation — is **structurally coherent and its constants are genuinely independent of the collapsed local volume**. The volume cancellation is real, not a bookkeeping artifact; I confirmed it below. Two things are not yet derived at the level the notes sometimes suggest: (i) the general-p tensor inequality is proved for representative terms only, with its uniform dissipation constant and its polynomial p-power asserted; (ii) the downstream geometric terminal (calibrated W⁺ spectrum, δW⁺=0 ⇒ ∇W⁺=0, the Einstein limit, and the δ→0 passage that actually produces the contradiction) lives entirely outside these notes. The material is explicit that this treats only the 4D negative Ishida–LeBrun family, not the dimension-indexed interval statement, the positive branch, or a Lean development.

## 2. Active-region versus collar energy: an earlier error, correctly repaired

This is the place where reading the derivation rather than the label matters. In Step 23 §3 the absorption variable is
$$\gamma_j(t)=\mathsf S_j\|F(t)\|_{L^2(U_j)},$$
taken over the **auxiliary** support $U_j$. But $U_j$ contains the collar $\{a=0\}$ where the velocity $-2aE$ vanishes, so $\|F\|_{L^2(U_j)}^2$ carries a **time-frozen** contribution $C_{\mathrm{col}}=\int_{U_j\setminus\operatorname{supp}\chi}\eta^2F_0^2$. The persistence estimate only controls the active part $\int_{\operatorname{supp}\chi}F^2$, so the "self-improvement of $\gamma_j$" in Step 23 §3 is not justified as written.

Step 26 §2 repairs this exactly. It defines
$$\widehat H_2=\int_{\operatorname{supp}\chi}F^2=H_2-C_{\mathrm{col}},\qquad \bar\beta=\mathsf S\,\widehat H_2^{1/2},$$
and observes that every remainder term in the energy identity carries $a$, $da$, or $|da|^2/a=4|d\chi|^2$, all supported in $\{a>0\}\subset\operatorname{supp}\chi$. Hence the active-region inequality
$$\widehat H_2'+cD_2\le C\!\int\eta^2aF^3+Cr^{-2}\widehat H_2$$
has **no additive collar constant**, and the Hölder–Sobolev absorption $\int\eta^2aF^3=\int F(\chi F)^2\le\|F\|_{L^2(\operatorname{supp}\chi)}\|\chi F\|_4^2$ uses the active $L^2$ norm only. I verified that $\bar\beta$ is the correct self-improving variable and that $C_{\mathrm{col}}$ is truly time-independent (on $\operatorname{supp}\eta\setminus\operatorname{supp}\chi$ one has $\chi=0$, so $a=0$ and the velocity vanishes). One cosmetic slip: (2.5) writes $\widehat H_2(t)\le e^{Ct/r^2}(\widehat H_2(0)+C_{\mathrm{col}})$, but the collar-free differential inequality gives the stronger $\widehat H_2(t)\le e^{Ct/r^2}\widehat H_2(0)$; harmless. **The active/collar separation is now correct**, and any downstream use of $\gamma_j$ over $U_j$ should be read as $\bar\beta$ over $\operatorname{supp}\chi$.

## 3. Unweighted $F$ factor and the volume-independence of $\bar\beta(0)$

The absorption keeps $F=(1+|\mathrm{Rm}|^2)^{1/2}$ to the **first power** as the Hölder factor, then applies Sobolev to $\chi F$. I checked the initial value:
$$\mathsf S\sim r^2 V^{-1/2},\qquad \|F(0)\|_{L^2(\operatorname{supp}\chi)}\lesssim\sqrt{(1+K_0)V}\ \Rightarrow\ \bar\beta(0)\lesssim r^2\sqrt{1+K_0},$$
with the local volume $V$ cancelling exactly. This is the crux of collapse-independence and it is correct.

Two things this rests on that are not shown in these notes:
- The centered maximal-function bound $\fint F(0)^2\le C(1+K_0)$ needs $\fint|\mathrm{Rm}|^2\le K_0$ at good centers, i.e. a finite $L^2$ curvature energy for a Ricci-pinched metric. In 4D this follows from Gauss–Bonnet/signature: $\int|W|^2=8\pi^2\chi(M)+\tfrac12\int|\mathring{Ric}|^2-\tfrac1{24}\int s^2$, and $|Ric|\le C$ bounds $\int|\mathring{Ric}|^2,\int s^2$ by $C\,\mathrm{Vol}(M)$ with $\chi(M)$ a fixed topological number. This is standard for the fixed family but is a genuine input that should be stated as a lemma; the notes use $K_0$ without deriving it.
- $\bar\beta(0)\lesssim r^2\sqrt{1+K_0}$ is small only for **small $r$**, since $K_0$ is order one. The absorption threshold therefore forces working at a scale $r\ll r_*$. I checked this is compatible: the maximal set $\{M(|\mathrm{Rm}|^2)\le K_0\}$ has fixed positive measure independent of $r$ (weak-type/Chebyshev on the fixed function $|\mathrm{Rm}|^2$), and a Vitali packing at scale $r$ yields a fixed positive volume fraction of disjoint inner balls at any $r$. So small $r$ does not shrink the good fraction; it only shrinks the flow window $\theta r^2$, and the terminal plateau curvature bound $\sim\sqrt{K_0}/\theta$ (from $\|aF\|\le C\bar\beta/t$ at $t\sim\theta r^2$) is $r$-independent. Consistent.

## 4. Relative Sobolev domains (Step 26 §1) — verified

The Maheux–Saloff-Coste inequality needs only $\mathrm{Ric}\ge kg$ (Bishop–Gromov doubling + Buser Poincaré + Hajłasz–Koskela), and I reproduced the exponent arithmetic for $n=4$, $p=2$, $p^*=4$:
$$\|\phi-\phi_B\|_4\le C r V^{-1/4}\|\nabla\phi\|_2,\quad |u_B|\le V^{-1/2}\|u\|_2\Rightarrow \|u\|_4^2\le C r^2 V^{-1/2}(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2).$$
So $\mathsf S=C(n,Kr^2)r^2V^{-1/2}$, uniform in the sequence because $Kr^2$ is bounded ($k=-(1+\delta)$, $r$ bounded). This legitimately removes any noncollapse hypothesis for the local Sobolev constant. Transfer to $g(t)$ via $C^0$ comparability multiplies $\mathsf S$ by $e^{CI}$; the smallness of $I$ comes from the defect bound, so this is a bootstrap link, closed by first-exit. No error.

## 5. Three-factor absorption and polynomial $p$-dependence — mechanism verified, uniform constants asserted

The device that makes the iteration work is the exact Hölder factorization (Step 27 §3):
$$a^{p-1}F\Phi^p=(aF^3)^{1/3}\,(a^{p-2}\Phi^p)^{1/3}\,(z_p^{4/3}),\quad z_p=a^{(p-1)/2}\Phi^{p/2},$$
which I checked has correct $a$-powers ($\tfrac13+\tfrac{p-2}3+\tfrac{2(p-1)}3=p-1$) and $F$/$\Phi$-powers. Hölder $(3,3,3)$ then Sobolev on $z_p$ and Young $(3,\tfrac32)$ give
$$R_p\le \varepsilon(D_p+r^{-2}H_p)+C p^2\mathsf S^2 Y H_p,$$
so the curvature potential $Y=\int aF^3$ enters **linearly as a coefficient**, not as a per-exponent smallness threshold. This is the genuine improvement over the two-factor form (which needed $\bar\beta<c/p$). I confirm the resulting Gronwall coefficient is $\sim p^N(r^{-2}+\bar\beta^3/t)$ and that $\sum_k(\log L_k)/p_k<\infty$ with $L_k=Cp_k^N4^k(\cdot)$ and $p_k$ geometric, so the Moser product converges. The architecture is sound.

What is **not** yet an exhaustive proof is the underlying inequality (Step 26 (3.1))
$$K_p'+c\|\nabla Z_p\|_2^2\le Cp^2r^{-2}K_p+Cp\int\eta^2a^{p-1}F\Phi^p .$$
Its §3.2 derivation treats a representative Bochner term, a representative Hessian-$a$ term, and the measure term, then asserts uniform $c>0$ and power $p^2$. Step 27 §9 itself lists as remaining "full index-level formulas including moving-norm, moving-volume, Lichnerowicz reaction, Hessian IBP, Kato regularization, and exact constant tracking." So the two sessions are not in agreement on whether (3.1) is complete. I did the sign/coefficient check for the load-bearing point: the Laplacian yields dissipation $\ge p(p-1)\int a^{p-1}F^{p-2}|\nabla F|^2$ (using $|\nabla F|\le|\nabla\mathrm{Rm}|$ and the $-p(p-2)$ Kato term), while $\|\nabla Z_p\|_2^2$ needs $\sim(p^2/4)\int a^{p-1}F^{p-2}|\nabla F|^2$; since $p(p-1)\ge p^2/4$ for $p\ge 4/3$, a uniform $c\gtrsim 1$ is plausible for $p\ge3$. This is encouraging but is exactly the computation that must be written in full, tracking every factor of $p$ (from $\partial_tF^p$, from $a^{p-2}$ in the IBP, from the $p(p-2)$ Kato term, from Young). **Concrete missing lemma:** the general-$p$ inequality with (a) a stated $c(p)\ge c_0>0$ for all $p\ge3$ and (b) a fixed polynomial power $p^N$, both proved by an exhaustive index-level expansion, for $\Phi=F$ and for the regularized $\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}$ with the $\varepsilon\to0$ passage. If the true $p$-dependence were super-polynomial the Moser product diverges; the whole endpoint hinges on this being polynomial.

I did verify the defect structural point that makes the $\delta^6$-preservation possible: the $|E|^2$ equation (4.3) has reaction $4a\,\mathrm{Rm}(E,E)$, so testing gives $\int a^{p-1}F|E|^p$ (one power of $F$), never $\int a^{p-1}F^2|E|^{p-1}$ or a curvature-only source. This is forced by $E=0$ being a fixed point of $\partial_tg=-2aE$, and it is what keeps the defect reaction controlled by $\bar\beta$ rather than by a $\delta$-independent quantity.

The noninteger-power remark (§3.4) is a real technical point handled adequately by Lipschitz weights and $|da|^2/a=4|d\chi|^2$; only first derivatives of the weight enter the energy, so $W^{1,\infty}$ suffices.

## 6. Terminal $H_3$ propagation and the $t=0$ splice — verified

**Terminal $H_3$ (Step 23 §4):** the spacetime bound $\int_0^tH_3\le C\bar\beta_* \widehat H_2(0)$ comes from the $q=2$ dissipation, and the pointwise-in-time bound $H_3(t)\le C\bar\beta_*\widehat H_2(0)/t$ follows by picking a good slice $s\in[t/4,t/2]$ with $H_3(s)\le\tfrac4t\int_0^{t/2}H_3$ and propagating forward by the **separate** $q=3$ inequality $H_3'\le Cr^{-2}H_3$, with $r^{-2}(t-s)\le\theta$. This is a legitimate mean-slice + forward-propagation argument, not a mean-value assertion; I confirmed the $v_3=aF^{3/2}$ gradient estimate $\|\nabla v_3\|_2^2\le CD_3+Cr^{-2}H_3$ that the $q=3$ absorption needs (using $|\nabla a|^2=4a|\nabla\chi|^2$ and $a^2F|\nabla F|^2\le D_3$ integrand).

**$t=0$ splice:** the two endpoint bounds have opposite integrability. $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ is integrable: $\int_0^{\theta r^2}\lesssim\delta\theta^{2/3}r^2\to0$, giving small metric drift; and $J_6(t)\le e^{C\theta}J_6(0)\le C\delta^6V$ is a persistence from $t=0$, so nothing about the defect blows up at $0$. The non-integrable $\|aF\|\le C\bar\beta/t$ is **never integrated from zero** — it is only used at positive $t$ for continuation, and the spacetime $\int_0^t H_3$ that seeds the curvature Moser comes from the $q=2$ dissipation, not from the pointwise $t^{-1}$ bound. Short-time DeTurck existence covers $[0,t_0]$ with bounded $a\mathrm{Rm}$, so $\|a\mathrm{Rm}\|$ is bounded on all of $[0,T_{\max})$ (short-time on $[0,t_0]$, Moser $\le C\bar\beta/t_0$ on $[t_0,T_{\max})$). The splice is coherent.

## 7. Shifted-curvature continuation — the algebra checks out

This is the strongest self-contained piece. I verified the central identities directly:
- $\mathrm{Ric}(G)=g$ for $G=\tfrac1{2(n-1)}g\owedge g$ (computed $g^{ik}G_{ijkl}=\tfrac{n-1}{n-1}g_{jl}$).
- $E=\mathrm{Ric}(\widetilde R)$, $aE=\mathrm{Ric}(U)$, hence $\partial_tg=-2\,\mathrm{Ric}(U)$ — so the normalization does **not** appear as a separate $ag$ term in the connection evolution.
- $\partial_tG=\tfrac1{n-1}h\owedge g=-\tfrac{2a}{n-1}E\owedge g$ (from $\partial_t(g\owedge g)=2h\owedge g$).

The decisive structural fact is that in $(\partial_t-a\Delta)\widetilde R$ the potentially dangerous $(\nabla^2a)*E$ term equals $(\nabla^2a)*\mathrm{Ric}(\widetilde R)$, a contraction with $\widetilde R$; the "$+g$" of $E=\mathrm{Ric}+g$ is itself $\mathrm{Ric}(G)$ and is absorbed into $\widetilde R=\mathrm{Rm}+G$. Thus **there is no curvature-independent $(\nabla^2a)*g$ source**, and every term carries $\widetilde R$ or a derivative of it — confirmed by the consistency check $\widetilde R=0\Leftrightarrow\mathrm{Ric}=-g\Leftrightarrow$ stationary. This is precisely why Wang's Section-4 induction transfers: the normalized velocity has the same $\mathrm{Ric}(U)$ contraction structure as the unnormalized case.

I also checked the current-order induction triangle $A_{m-1}\to C_m\to B_{m-1}\to A_m$. The raw $\nabla^mU$ equation genuinely contains $\chi\nabla^{m+2}\chi*U$ and $\nabla^{m+1}U$; these are removed, not assumed:
- The one IBP of $\int|W|^{p-2}\langle W,\chi\nabla^{m+2}\chi*U\rangle$ lowers the cutoff order to $m+1$, and the resulting $\nabla W$ term pairs with the diffusion because the factor $\chi$ in front of $\nabla^{m+2}\chi$ supplies exactly the $\sqrt a$ matching the weight $a=\chi^2$: $\chi|\nabla W|\le\varepsilon^{1/2}(a|\nabla W|^2)^{1/2}$, giving $\varepsilon\int a|\nabla W|^2|W|^{p-2}+C_\varepsilon\int|U|^2|\nabla^{m+1}\chi|^2|W|^{p-2}$. I confirmed this weight-matching is the mechanism, and it is why $U=\chi^2\widetilde R$ (not $\widetilde R$) must be the evolved object.
- $\nabla^{m+1}\chi$ then closes with $\nabla^mU$ through the cutoff evolution $\partial_t\nabla^{m+1}\chi$, which contains only the current $|\nabla^mU||\nabla\chi|$ at top order, giving a coupled Volterra/Gronwall system $Y_m'\le C(1+Y_m+\int_0^tY_m)$ — Wang's Lemma 4.11 pairing.
- The new $G$-monomials ($\mathcal N_m$, (7.9), (7.13)–(7.14)) carry no top derivative because $\nabla G=0$ and $aG$ is a bounded coefficient; I checked they add only $C(1+\|V\|_p^p)$.

Constants here depend on the individual $(g_0,\chi,T)$ and on the single bound $\sup|a\mathrm{Rm}|$, not on sequence-uniform higher cutoff jets — which is all the first-exit continuation needs, since it only requires extending across a **positive** $T_{\max}<\theta r^2$. The interface (§8) is coherent: $\|a\mathrm{Rm}\|$ is bounded on $[T_{\max}/2,T_{\max})$ by the Moser estimate under the first-exit conditions, and short-time existence handles $[0,t_0]$, so the continuation theorem contradicts maximality. I did not find an error in this transfer; the shift is a real and correct idea.

## 8. Moser endpoint and the "four-dimensional coincidence" — verified

I checked the endpoint exponents and the volume cancellation are internally exact, not fitted:
- $\sum_k1/p_k=3/p_0$, net Sobolev power $\tfrac1\kappa\sum1/p_k=2/p_0=n/(2p_0)$, time power $(1+n/2)/p_0=3/p_0$, with $\kappa=1+2/n=3/2$.
- Curvature ($p_0=3$): $\mathsf S^{2/3}\cdot t^{-1}\cdot(\bar\beta^3/\mathsf S^2)^{1/3}=C\bar\beta/t$ — $\mathsf S$ cancels.
- Defect ($p_0=6$): $\mathsf S^{1/3}\cdot t^{-1/2}\cdot(\delta^6V t)^{1/6}$ with $\mathsf S^{1/3}V^{1/6}=r^{2/3}$ — volume cancels, giving $C\delta(r^2/t)^{1/3}$.

The cancellation is genuine: the seed's volume factor ($V^{-1/3},V^{-1/6}$ inside $\mathsf S^{n/(2p_0)}$ against $V^{1/3},V^{1/6}$ in the $L^{p_0}$ seed) is matched by the 4D relation $n/(2p_0)\in\{2/3,1/3\}$. The dropping of $(t^{-1}+r^{-2})^{3/p_0}$ to $t^{-3/p_0}$ uses $t\le\theta r^2\le r^2$ so $t^{-1}\ge r^{-2}$; valid.

## 9. What remains open or is outside the material examined

Grounded, these are the statements not established here:

1. **The full index-level general-$p$ inequality** (Section 5 above). This is the single most consequential parabolic item not yet exhaustively proved: the uniform lower bound on the dissipation constant $c(p)$ and the polynomial power $p^N$ are asserted from representative-term work. Suggested resolution: an explicit expansion tracking each $p$-factor, plus the $\varepsilon\to0$ passage for $\Phi_\varepsilon$, for both $\Phi=F$ and $\Phi=|E|$.

2. **The $L^2$ curvature seed** $\fint|\mathrm{Rm}|^2\le K_0$ from Ricci pinching, via 4D Gauss–Bonnet with fixed $\chi(M)$. Standard for the fixed family but used as a black box.

3. **The geometric terminal (Step 6), entirely outside these notes.** In particular the implication "$\mathrm{Spec}(W^+)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$, $\delta W^+=0\ \Rightarrow\ \nabla W^+=0$" against $|\nabla W^+|^2=\tfrac1{16}$ is the actual contradiction, and harmonic $W^+$ with a fixed non-generic spectrum does **not** obviously force $\nabla W^+=0$ (harmonic $\neq$ parallel in general). This is the geometric hinge on which the whole negative-branch program turns and it is not verified in the provided files. The traceless check $-\tfrac16+\tfrac1{12}+\tfrac1{12}=0$ is consistent, but that is all one can confirm from the material.

4. **The $\delta\to0$ uniformity** that converts the fixed-$\delta$ estimates into an Einstein germ carrying the calibrated spectrum. The per-$\delta$ chain is collapse-independent, but the passage to the limit metric (smooth compactness in harmonic charts, preservation of the calibrated Weyl datum) is asserted, not derived.

5. **Coverage.** By the notes' own statements this is only the 4D negative Ishida–LeBrun branch; the dimension-indexed interval $c_n g\le\mathrm{Ric}\le C_n g$, the positive branch, arbitrary topology, $n\ge5$, and the Lean development are untouched.

## 10. Summary of the one incorrect inference and its repair

The only outright incorrect step I found is Step 23's use of $\gamma_j=\mathsf S_j\|F\|_{L^2(U_j)}$ over the auxiliary support, which conflates the frozen collar energy with the active energy and cannot self-improve. It is correctly repaired in Step 26 by $\bar\beta=\mathsf S\,\widehat H_2^{1/2}$ over $\operatorname{supp}\chi$, with the collar-free active-region inequality. Any later note still written in terms of $\gamma_j$ over $U_j$ should be read through this replacement. Everything else I checked (the MSC exponents, the three-factor Hölder, the terminal $H_3$ slice+propagation, the Moser volume cancellation, the shift identities $\mathrm{Ric}(G)=g$ and the absence of a $(\nabla^2a)*G$ source, and the $\sqrt a$-matched cutoff IBP in the Wang triangle) is internally consistent; the remaining substance is the full general-$p$ derivation and the geometric terminal, both identified above with the specific object each requires.
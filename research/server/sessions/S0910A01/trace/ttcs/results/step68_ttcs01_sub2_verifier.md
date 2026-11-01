# TTCS Independent Branch Record

```json
{
  "step_id": 68,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step68_restricted_IL_canonical_assembly.md",
    "Sessions/S0910A01/workspace/notes/step67_terminal_recalibration_recovery.md",
    "Sessions/S0910A01/workspace/notes/step62_defect_moser_general_p_proof.md",
    "Sessions/S0910A01/workspace/notes/step64_convention_consistency_sweep.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md"
  ]
}
```

## Task

Verify the mathematical consistency of this assembled restricted Ishida-LeBrun negative-gap theorem. Check specifically:

1. INTERFACE CONSISTENCY: Does the terminal calibration (§3) correctly interface with the flow output (§7)? Is the passage from Q(T)/A_i→0 through the Liouville averaging (§9) to the forbidden-germ contradiction logically complete? Are there any missing hypotheses at any interface?

2. CONVENTION CORRECTNESS: Under T=Rm-G with G=(g⊙g)/(2(n-1)) and Ric(G)=-g, does the pure-scaling correction ∂_tT=-2aT+2aG add a term that is genuinely absorbed by CaF_T^3? Does this break any energy inequality or Moser iteration?

3. UNIFORMITY SEPARATION: Is the distinction between sequence-uniform (first-exit curvature/defect/Q) and datum-dependent (all-order continuation) correctly maintained? Could a datum-dependent quantity leak into the terminal contradiction?

4. DEFECT MOSER ENDPOINT: Is the three-factor route (§6.5) genuinely p-independent? Does S²Y ≤ Cγ³/t come from the curvature branch without circularity? Is the nested Moser product convergence rigorous?

5. FORBIDDEN GERM: Does Φ=0 actually force the specific W+ spectrum (-1/6, 1/12, 1/12)? Is the passage from G_gap=0 to two-eigenvalue W+ correct? Does Derdziński's proposition apply to this exact setting (Einstein, two W+ eigenvalues, dimension 4)?

## Output

# Verification Memo: Restricted Ishida–LeBrun No-Near-Einstein Assembly (Step 68)

I reproduced the load-bearing computations independently where they are self-contained and traced the module interfaces where they are not. The strongest module (§3 terminal calibration) checks out exactly; the flow modules (§§4–8) rest on three elements that the module notes themselves mark unresolved, which the assembly's status tables present more confidently than the notes support. Details below, organized by your five questions plus the structural items they surface.

---

## 1. Terminal calibration (§3) — independently confirmed exact

I recomputed the entire chain. Every constant is correct.

- **Completion identity (3.6)** $\frac{s^2}{24}+2\nu^2=\frac1{12}f^2+\frac1{216}(s+8\sqrt6\nu)^2$ with $f=\tfrac23 s-2\sqrt{2/3}\,\nu$: I expanded both sides. The $s^2$ coefficients give $\tfrac1{27}+\tfrac1{216}=\tfrac{9}{216}=\tfrac1{24}$; the $\nu^2$ coefficients give $\tfrac29+\tfrac{16}9=2$; the cross $s\nu$ terms cancel ($-\tfrac{2\sqrt6}{27}+\tfrac{2\sqrt6}{27}=0$). Exact.
- **Deficit bounds (3.4)**: $I-J=2\chi+3\tau=\tfrac{2A}3-q$ (standard Gauss–Bonnet/signature combination), $D_{\rm av}=J-q-\tfrac23\sum|e_\ell^+|^2$, with $0\le D_{\rm av}\le J\le Q/8\pi^2$ using $q\ge0$ and $\sum|e_\ell^+|^2\ge0$. The passage $J\le Q/8\pi^2$ from $|E|^2=|E^\circ|^2+\tfrac{(s+4)^2}4$ is correct, as is $\int(s+4)^2\le4Q$.
- **(1.11)** $4\pi^2 D_{\rm av}\ge\tfrac1{12}\int\mathcal G+\tfrac1{216}\int(s+8\sqrt6\nu)^2$: follows by combining $4\pi^2 I=\int[f^2/12+(s+8\sqrt6\nu)^2/216]$ with the averaged lower-part inequality $\int a_{*,-}^2\ge32\pi^2(A+\sum)$ rewritten as $\tfrac23(A+\sum)\le\int a_{*,-}^2/48\pi^2$. Then $D_{\rm av}\le Q/8\pi^2$ yields $\int(s+8\sqrt6|W^+|)^2\le108Q$ and $\int\mathcal G\le6Q$. So $\int\Phi\le(1+4+108+6)Q=119Q$. Confirmed.

Two structural facts here are correct and important:

- The **sign-free density $\mathcal G=f^2-a_{*,-}^2$** (with $a_{*,-}=\min(a_*,0)$) is nonnegative without assuming $s<0$, because $w+\sqrt{2/3}|W^+|\ge0$ always (the most-negative eigenvalue of a trace-free symmetric operator on $\Lambda^+$ satisfies $w\ge-\sqrt{2/3}|W^+|$; I verified the extremal $(-2t,t,t)$ realizes $-\sqrt{2/3}$). The note correctly flags that the `20260912.tex` lines 285–327 $u=-s$ decomposition assumes $s<0$ and must not be substituted here.
- The **recalibration works with no transport of the Weyl profile through the flow**: the mixed Seiberg–Witten inequality and Chern–Weil identity are reapplied directly to the terminal metric $g_i(T)$ on the same smooth manifold. Since SW curvature integral lower bounds hold for *every* metric on $M$ (they are topological), this is legitimate. This correctly dissolves the Step 66 worry that terminal $\Phi$ needed a new transport theorem. §3 is the cleanest and most reliable module in the assembly.

**Interface into §7.** $\int\Phi(g_i(T))\le119Q(T)$ and $Q(T)/A_i\to0$ (from $Q(0)=O(\delta_i^2 A_i)$ and the sequence-uniform propagation constant in (7.2)) give $\int\Phi(g_i(T))=o(A_i)$. Logically clean; the only hidden requirement is that (7.2)'s exponent $e^{C(1+r^{-2})T+C_VV(T)}$ is genuinely metric-independent, which it is (all inputs are sequence-uniform).

---

## 2. Convention correction — genuinely absorbed, breaks nothing

Under $T=\operatorname{Rm}-G$, $G=(g\owedge g)/2(n-1)$: I verified the pure-scaling behavior. As a $(0,4)$-tensor, $\operatorname{Rm}$ scales by $\lambda$ under $g\mapsto\lambda g$, while $G$ (two factors of $g$) scales by $\lambda^2$. Hence $T$ is **not** scale-homogeneous, and along $g(t)=e^{-2t}g_0$ one gets $\partial_t\operatorname{Rm}=-2\operatorname{Rm}$, $\partial_tG=-4G$, so $\partial_tT=-2\operatorname{Rm}+4G=-2T+2G$. This confirms Step 63's old homogeneous line $\partial_tT=-2T$ was wrong and the corrected form $\partial_tT=-2aT+2aG+(\text{gradient terms})$ is right.

The extra $2aG$ term is zero-order and algebraically bounded: $|2aG|\le 2a|G|=2a\sqrt{2/3}\le Ca$ (constant $|G|$ in $n=4$). Its contribution to $\tfrac{d}{dt}H_2$ is $\int\eta^2\,2\langle T,2aG\rangle\le C\int\eta^2 a|T|\le C\int\eta^2 aF_T\le CH_2$. So it is in fact bounded by $C\int\eta^2 aF_T$ — one power of $F_T$ below the cubic potential $Y=\int\eta^2 aF_T^3$ that carries the Sobolev absorption. The note's stated bound $CaF_T^2\le CaF_T^3$ is valid but not tight; either way the term absorbs into the linear $C_H(1+r^{-2})H_2$ reaction and does not touch the $\gamma$-absorption structure. In the curvature Moser ladder it contributes $\sim p\,a F_T^p$, a standard $p$-linear reaction that leaves the iteration exponent unchanged. The defect equation $E=\operatorname{Ric}+g$ contains no $G$, so §6.5 is untouched. **The correction does not break any energy inequality or Moser step.**

The legacy reconciliation $G_{\rm old}=-G\Rightarrow T_{\rm old}=T$ (step64 §2) is correct *given* that $G_{\rm old}$ was the universal $g\owedge g$ multiple; step64 correctly notes this does not follow from $\operatorname{Ric}(T)=E,\ \nabla T=\nabla\operatorname{Rm}$ alone (a parallel Ricci-free Weyl piece could be added). Since the old notes used the constant-curvature reference, the identification holds.

---

## 3. Uniformity separation — logically maintained; one wording point to watch

The separation is correct in substance. The terminal contradiction consumes only: $\int\Phi\le119Q(T)$ (sequence-uniform $Q$), $Q(T)/A_i\to0$, $\operatorname{Vol}(P_i)\ge\alpha_0A_i/2$, plateau curvature $|\operatorname{Rm}(T)|\le K(\gamma_*,\theta,r)$, the Liouville constant $C(K,\rho)$, and forbidden-germ constants $K_0,\rho_0,\eta$ — all sequence-uniform. The datum-dependent all-order continuation (§8, $m\ge2$) is used only to carry each solution to the common time $\theta r^2$; its bounds do not enter §9.

One place where a datum-dependent quantity *appears* to threaten leakage but does not: §9.5 says the pullback balls "converge in $C^\infty$" by Cheeger–Gromov. A genuine $C^\infty$ subconvergence would need bounds on all $\nabla^m\operatorname{Rm}$, which are datum-dependent. The correct justification — supplied in step8 §5 but not in the §68 wording — is that a $C^0$ curvature bound plus noncollapse gives only $C^{1,\alpha}$/$W^{2,p}$ harmonic-coordinate subconvergence, and the *limit* is Einstein ($\Phi\to0\Rightarrow E_\infty=0$), so the limit bootstraps to smooth by elliptic regularity for $\operatorname{Ric}=-g$. Passing $s$, $W^+$, and $\Phi$ requires only $W^{2,p}$ ($p>2$) convergence of $g$, hence $L^p$ convergence of curvature. So no derivative bound on the approximants is needed and there is no actual leak — but the §68 phrase "$C^\infty$ Cheeger–Gromov" overstates and should be read as step8's finite-$W^{2,p}$-then-Einstein-bootstrap. I recommend aligning the wording so the separation is visibly airtight.

---

## 4. Defect Moser endpoint — three-factor route is genuinely $p$-independent

I checked the algebra end to end.

- **Three-factor identity (4.1)** $\eta^2a^{p-1}Fs^{p/2}=(aF^3)^{1/3}(\eta^2a^{p-2}s^{p/2})^{1/3}z_p^{4/3}$ with $z_p=\eta a^{(p-1)/2}s^{p/4}$: I summed the exponents. $a$: $\tfrac13+\tfrac{p-2}3+\tfrac{2(p-1)}3=p-1$; $s$: $\tfrac p6+\tfrac p3=\tfrac p2$; $\eta$: $\tfrac23+\tfrac43=2$; $F$: $1$. All match. Correct.
- **Hölder$(3,3,3)$ + Sobolev + Young**: $P_p\le Y^{1/3}J_p^{1/3}\|z_p\|_4^{4/3}$, then $\|z_p\|_4^2\le Cp^2\mathcal S(Q_p+r^{-2}J_p)$ (the $p^2$ from differentiating $s^{p/4}$, and $\|z_p\|_2^2\le J_p$ since $a^{p-1}\le a^{p-2}$). Young splitting $(Q_p)^{2/3}$ against the remainder gives coefficient $\mathcal S^2 Y$ with $N=4$: I tracked $[\mathcal S^{2/3}Y^{1/3}J_p^{1/3}p^{4/3}]^3=\mathcal S^2 Y J_p p^4$. Multiplying by the chain-rule $Cp$ gives $\varepsilon pQ_p+C_\varepsilon p^{N+1}\mathcal S^2Y J_p$, and $\varepsilon pQ_p$ absorbs into $c_2p^2Q_p$ for every $p\ge2$ (needs $\varepsilon\le c_2 p/2$, true) — **no smallness on $\gamma$**. This is exactly why the two-factor route does not close (its condition $\gamma_t\le c/p$ is $p$-dependent, Prop 3.2, which I confirmed: reaction $\sim p^3\gamma_t Q_p$ against dissipation $p^2Q_p$).
- **$\mathcal S^2Y\le C\gamma^3/t$ without circularity**: $Y=\int\eta^2 aF_T^3\le\|aF_T\|_\infty H_2\le(C\Gamma/t)H_2$ from the *curvature* endpoint (6.6); with $\gamma=\mathcal S H_2^{1/2}$ this gives $\mathcal S^2 Y\le \mathcal S^2\cdot C\Gamma H_2/t\sim\gamma^3/t$. The curvature endpoint is produced by the curvature branch alone, so the defect endpoint takes $Y$ as an already-established input — no circularity between the two branches.
- **Moser product**: $\Lambda_k\le C_k\Lambda_{k-1}^{3/2}$, $p_k=6(3/2)^k$, root exponent $(3/2)^k/p_k=1/6$; the product converges via $\sum(2/3)^j=2$ and $\sum j(2/3)^j=6$ absorbing the $p_k^N4^k$ factors. Volume cancellation (5.9): with $\mathcal S\simeq r^2V^{-1/2}$, $I_0\le Ct\delta^6V$, I recomputed $\mathcal S^{1/3}t^{-1/2}I_0^{1/6}=Cr^{2/3}\delta V^{-1/6+1/6}t^{-1/2+1/6}=C\delta(r^2/t)^{1/3}$. Exact cancellation, including the collapse regime $\mathcal S\to\infty$. Endpoint $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ confirmed, integrable at $t=0$, giving $V(T)\le C\delta\theta^{2/3}r^2$.

So the defect endpoint is correct **given** the curvature endpoint (6.6). That dependency is the pivot to item below.

---

## 5. Forbidden germ — algebra and Derdziński application both correct

I verified independently that $\Phi\equiv0$ forces the exact spectrum.
- $|E|^2=0\Rightarrow\operatorname{Ric}=-g$; $(s+4)^2=0\Rightarrow s=-4$; $(s+8\sqrt6|W^+|)^2=0\Rightarrow|W^+|=\tfrac1{2\sqrt6}$, i.e. $|W^+|^2=\tfrac1{24}$.
- With $s=-4,\ \nu=\tfrac1{2\sqrt6}$: $f=\tfrac23(-4)-2\sqrt{2/3}\cdot\tfrac1{2\sqrt6}=-\tfrac83-\tfrac13=-3$, so $f^2=9$. $\mathcal G=0\Rightarrow a_{*,-}^2=9\Rightarrow a_*=-3\Rightarrow w=-\tfrac16$. With lowest eigenvalue $-\tfrac16$, trace-free ($\lambda_2+\lambda_3=\tfrac16$) and $\lambda_2^2+\lambda_3^2=\tfrac1{24}-\tfrac1{36}=\tfrac1{72}$: the quadratic $x^2-\tfrac16 x+\tfrac1{144}$ has discriminant $\tfrac1{36}-\tfrac1{36}=0$, so $\lambda_2=\lambda_3=\tfrac1{12}$. Spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$ is forced. Correct.
- **Derdziński applies to this exact setting**: Einstein $\Rightarrow\delta W^+=0$ (standard Bianchi consequence); two distinct $W^+$ eigenvalues; dimension 4. Proposition 5 then makes $\hat g=(24|W^+|^2)^{1/3}g$ locally Kähler; here $24|W^+|^2=1$ so $g$ itself is locally Kähler. A Kähler–Einstein 4-germ with $\operatorname{Ric}=-g$ ($s=-4$) has $W^+$ spectrum $(s/6,-s/12,-s/12)=(-\tfrac23,\tfrac13,\tfrac13)$, so $|W^+|^2=\tfrac23=s^2/24\neq\tfrac1{24}$. Contradiction. The independent tensor route ($\delta W^+=0$ + two constant eigenvalues $\Rightarrow\nabla W^+=0$, versus the Einstein–Weyl identity forcing $|\nabla W^+|^2=\tfrac1{16}$; I confirmed $-36\det W^+=\tfrac1{24}$ gives $|\nabla W^+|^2=\tfrac1{16}$) corroborates. Solid.

---

## Load-bearing elements that remain open inside the restricted claim

The five checks above confirm the *algebraic spine* (§3 calibration, forbidden germ, convention arithmetic, defect endpoint arithmetic). The *analytic flow modules* that connect a wild near-Einstein $g_i$ to a bounded-curvature terminal metric rest on three elements the module notes mark unresolved, and the §68 status tables run ahead of that:

1. **Per-datum existence of the exact degenerate cutoff flow (§5).** step64 §5 and step62 §8–9 state that only the doubly-regularized $(\varepsilon,\nu)$ transported-DeTurck system is standard parabolic; the real content is the regularization-uniform estimate package letting $\varepsilon,\nu\to0$ to the exact degenerate $\partial_t g=-2\chi^2(\operatorname{Ric}-\sigma g)$. This underlies the entire flow argument and is not established in the supplied notes.

2. **Curvature Moser endpoint (6.6) rests on an open index-level tensor identity.** step62 §9 and step64 §5 record that the curvature branch needs $|\nabla B|\le CF|\nabla\operatorname{Rm}|$ (Step 34 §7 item 1), listed as unproven. Because $Y$ — and thus $\mathcal S^2Y$ in item 4, and the plateau curvature bound $K$ in item 3 — flow from (6.6), the whole terminal geometry is contingent on this identity. The defect branch's non-circularity is real, but both branches sit on top of this one unproven curvature estimate.

3. **The $A_i$-proportional inner-plateau volume (4.7).** The passage from maximal-function selection (centers with $\mathcal M(x_\alpha)\le\Lambda_0$ capturing $c\cdot\operatorname{Vol}(M_i)$) to $\operatorname{Vol}(P_i)\ge\alpha_0A_i$ on the *inner* balls $B_r$ with sequence-uniform $\alpha_0$ is asserted and cited to Steps 34/43/45, not derived in the assembly. This volume is exactly what carries the cancellation in (9.6)–(9.7), so it is load-bearing and is the least substantiated interface in §§4, 8.

A fourth, smaller interface point: the assembly asserts the pullback $\rho$-ball stays inside the curvature-controlled plateau and inherits noncollapse via Rauch, but does not explicitly reconcile the universal forbidden-germ radius/curvature $(\rho_0,K_0)$ with the plateau radius/curvature $(r,K(\gamma_*,\theta,r))$. Both are universal, so $\rho_0\le c\,r$ and $K\le K_0$ are presumably arrangeable, but the matching is not carried out in text; without it, a geodesic $\rho_0$-ball from $p\in\bigcup B_r$ could exit $B_{5r}$ where curvature control lapses.

The §68 status framing ("proved," "gap closed") reflects the algebraic modules accurately but not elements 1–3, which step67 §4, step64 §5, step62 §8–9, and step8 §9 all list as unresolved. Read together, the result is a **conditional theorem for the $\operatorname{Ric}\approx-g$, $q\ge0$ Ishida–LeBrun geography in dimension 4**, modulo (1)–(3).

---

## Reach relative to Yau 26 — an absent logical bridge worth naming

Beyond §13's honest enumeration (positive sign case, general 4-topology, $n\ge5$, Lean), there is a conceptual distance in the direction of the statement that the shifted-defect notation $E=\operatorname{Ric}+g$ can obscure:

- Yau 26 asks that a **wide pinch** $c_ng\le\operatorname{Ric}_g\le C_ng$ *force existence* of some Einstein $h$ (any $\lambda$).
- This assembly shows **non-existence** of metrics with $\|g^{-1}(\operatorname{Ric}_g+g)\|<\varepsilon_{\rm IL}$ — a small neighborhood of the single Einstein value $\lambda=-1$ — on special manifolds.

These bear on Yau 26 only through the contrapositive "manifolds with no Einstein metric admit no pinched metric," and the present result excludes only metrics *very close to* $\operatorname{Ric}=-g$, not metrics with $\operatorname{Ric}$ anywhere in a wide band $[c_n,C_n]$ that need not approach any $\lambda g$. A pinched metric on an IL manifold could have $\operatorname{Ric}$ in a wide interval and never be $\varepsilon_{\rm IL}$-near-Einstein, in which case this theorem says nothing about it. So the result neither exhibits an IL manifold as a counterexample nor removes it as one. Connecting "no $\varepsilon_{\rm IL}$-near-$(-g)$ metric" to "no metric in the pinch interval" requires an additional argument (interval rescaling to $\lambda=-1$, or a separate rigidity spanning the whole band) that is not present in the notes. Stating this bridge explicitly would clarify what the restricted result can and cannot contribute even after (1)–(3) are closed.

---

## Summary for use

The algebraic core is reliable: §3 calibration ($\int\Phi\le119Q$) is exact and I recommend treating it as a finished, transportable lemma; the forbidden-germ spectrum and Derdziński application are correct; the convention correction is harmless; the three-factor defect endpoint is genuinely $p$-independent and non-circular. The analytic flow that connects these — per-datum existence, the curvature endpoint's index-level tensor identity, and the $A_i$-proportional plateau volume — remains the substance to establish, and the terminal constant-matching $(\rho_0,K_0)$ vs $(r,K)$ deserves an explicit line. What would most change the value of this line is (a) the regularization-uniform estimate closing element 1, (b) the tensor identity closing element 2, and (c) a stated bridge from near-$(-g)$ non-existence to the wide pinch interval, since without (c) the restricted result, even fully closed, does not yet speak to the existence direction Yau 26 asks about.
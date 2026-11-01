# TTCS Independent Branch Record

```json
{
  "step_id": 29,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step29_simultaneous_support_theorem.md",
    "Sessions/S0910A03/workspace/notes/step29_consolidated_conditional_theorem.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Verify the complete conditional chain for the four-dimensional negative-branch Yau Problem 26 argument on the Ishida-LeBrun no-Einstein family. The chain has three layers: (1) TOPOLOGICAL: For above-critical manifolds (sigma = D - A/3 > 0), CGB + Hirzebruch + SW monopole inequality give R >= sigma >= delta^2 Vol/(2pi^2), hence delta >= c sqrt(sigma/A) with no PDE. (2) ANALYTIC: For the critical boundary (sigma = 0), a buffered cutoff flow partial_t g = -2 chi^2(Ric+g) on selected maximal-function good supports produces: H_2 persistence -> S^2Y <= C beta^3/t -> ||aF||_inf <= C beta/t (three-factor Moser) -> J_6 persistence -> ||aE||_inf <= C delta(r^2/t)^{1/3} -> integrable velocity V(T) <= C delta theta^{2/3} r^2 -> metric comparison closes bootstrap. The shifted curvature T = Rm + G, U = aT gives continuation via Wang's theorem. (3) GEOMETRIC DOWNSTREAM: terminal recalibration gives int mathfrak_D <= 119 Q(T) = o(A); exponential pullback on fixed-volume plateau selects centers with vanishing pulled-back defect; Rauch tangent-space noncollapse; harmonic-coordinate compactness; smooth Einstein limit with calibrated Weyl spectrum (-1/6, 1/12, 1/12); Derdzinski contradiction (locally conformally Kahler but |W+|^2 = 1/24 != 2/3). KEY CLAIM: K_0 = Vol^{-1} int |Rm|^2 is uniformly bounded by 9 + O(1/A) + O(delta^2) across the IL family, making the critical product beta = S * H_2^{1/2} = C r^2 K_0^{1/2} a universal constant, hence the gap delta_0 is universal. Check: (a) Is the above-critical algebraic gap correct? (b) Is the bootstrap dependency graph non-circular? (c) Does the volume cancellation in beta hold exactly? (d) Is the Moser time exponent (1+n/2)/p_0 correct for the parabolic iteration? (e) Is the Derdzinski contradiction valid at the calibrated spectrum? (f) Are there any hidden gaps in the conditional chain?

## Output

# Verifier Memo: Four-Dimensional λ = −1 Ricci-Pinching Gap Chain on the Ishida–LeBrun Family

Session S0910A01/A03, Steps 27–29. I checked the six requested items by re-deriving the algebra where possible and testing the internal consistency of the estimate hierarchy. The topological layer and the two "cancellation" identities check out exactly. The Moser exponent and the Derdziński contradiction are sound. The single decisive matter that is asserted but not established is a numerical inequality among fixed order-one geometric constants; it is forced into view precisely by the KEY assertion that β is a universal constant. I treat this as the headline finding and place the other checks around it.

---

## (a) Above-critical algebraic gap — correct, given the monopole input

The chain (1.1)→(1.7) verifies term by term.

- **Topological identity.** With $D=A/3+\sigma$, $A-D=2A/3-\sigma$, so $I-R=A-D$ gives $R=I-2A/3+\sigma$. The monopole inequality $I\ge 2A/3$ yields $R\ge\sigma$. Correct.
- **Pinching bound.** $\|g^{-1}(\mathrm{Ric}+g)\|_\infty\le\delta$ means the eigenvalues $\mu_i$ of $g^{-1}(\mathrm{Ric}+g)$ lie in $[-\delta,\delta]$, and $|\mathrm{Ric}_0|^2=\sum(\mu_i-\bar\mu)^2\le\sum\mu_i^2\le 4\delta^2$ in dimension 4. Hence $R\le\frac{\delta^2}{2\pi^2}\mathrm{Vol}$. Correct.
- **Volume control.** I reconstructed (1.5) independently: from $s\le-4(1-\delta)$ one gets $\mathrm{Vol}\le\frac{1}{16(1-\delta)^2}\int s^2$, and from $\int\frac{s^2}{24}\le 4\pi^2 I=4\pi^2(R+A-D)$ one gets $\int s^2\le 96\pi^2(R+A-D)$. Combining with $R\le\frac{\delta^2}{2\pi^2}\mathrm{Vol}$ closes the self-referential volume estimate for small $\delta$, giving $\mathrm{Vol}\le C(1-3\delta^2/(1-\delta)^2)^{-1}(A-D)=O(A)$. So $\mathrm{Vol}/A=O(1)$, and $\delta\ge\sqrt{2\pi^2\sigma/\mathrm{Vol}}\ge c\sqrt{\sigma/A}$. Correct.

**One genuine external input.** The inequality $I\ge 2A/3$ is the refined LeBrun/Ishida–LeBrun monopole estimate for the selected sign class, with $A=\sum c_1^2(X_j)$ carried through the connected-sum construction. This is not derived in these notes; it is cited (Ishida–LeBrun Thm 7). The whole above-critical layer rests on this holding with the stated constant and the stated definition of $A$ under blow-up/connected-sum. That reliance is real but is standard four-dimensional Seiberg–Witten material; I record it as an input rather than a defect.

The completed-square tightening (1.8), the $J\le Q/(8\pi^2)$ relation (1.2), and the combined constant $119$ in (1.7) all reproduce: $1\cdot Q+4Q+108Q+6Q=119Q$ with $108=864\pi^2\cdot(8\pi^2)^{-1}$ and $6=48\pi^2\cdot(8\pi^2)^{-1}$. Internally consistent.

---

## (b) Bootstrap dependency graph — non-circular as a first-exit structure, but closure is not free

The graph A→B→C→D→E→F→G is a standard continuity/first-exit argument: assume (B1–B4) with doubled constants on $[0,T^*)$, derive strictly better estimates, contradict maximality of $T^*$. Read as a directed acyclic dependency it is non-circular: each step consumes only earlier outputs plus the assumed doubled-constant hypothesis, and Step F regenerates (B1) and Sobolev persistence. No backward edge in the estimate flow.

However, the structure closes **only if** the absorption conditions inside the steps hold with the actual value of the critical parameter. Step A absorbs the cubic reaction under $C\beta_a<c/4$, with the bootstrap supplying $\beta_a\le 4\beta_0$; the whole theorem is stated under $C_*\beta_0<\Lambda$. This is a smallness condition on $\beta_0$. The question of whether it can be met is *not* internal to the graph — it is decided by the value of $\beta_0$ produced by the geometry, which is settled in (c) and is the crux discussed below.

So: the graph has no logical circularity; the open matter is not topology of the dependency but the numerical admissibility of the entrance condition $C_*\beta_0<\Lambda$.

---

## (c) Volume cancellation in β — exact, and it pins β at order one

The cancellation is correct and I verified it dimensionally and algebraically.

- Local Sobolev constant $S=Cr^2/\mathrm{Vol}(B_r)^{1/2}$ has dimension $L^2/\mathrm{Vol}^{1/2}$; with $L^4$ the Sobolev conjugate exponent in $n=4$ this is the correct Maheux–Saloff-Coste form under a Ricci lower bound and bounded $\kappa r^2$.
- $\beta=S\|F\|_{L^2(\Omega)}$: with $\int_\Omega F^2\le(1+4K_0)\mathrm{Vol}(\Omega)$ from the maximal-function support bound, $\|F\|_2\le\sqrt{(1+4K_0)V}$, so $\beta\le\frac{Cr^2}{V^{1/2}}\sqrt{(1+4K_0)V}=Cr^2\sqrt{1+4K_0}$. The $V^{1/2}$ cancels exactly. $\beta$ is dimensionless, as a critical scale-invariant quantity must be. Collapse-independence holds.
- The two downstream cancellations are likewise exact: curvature $S^{2/3}\cdot(\beta^3/S^2)^{1/3}=\beta$, and defect $S^{1/3}V^{1/6}=(r^2/V^{1/2})^{1/3}V^{1/6}=r^{2/3}$.

**Consequence that the KEY assertion makes unavoidable.** At the natural scale $r_*\sim K_0^{-1/4}$ one gets $\beta\le CK_0^{-1/2}\sqrt{1+4K_0}=O(1)$, and with the uniform bound $K_0\le 9+O(1/A)+O(\delta^2)$ the value is a fixed order-one constant, not a small one. The uniform-$K_0$ computation (6.1)–(6.2) is correct and reproduces $\beta\sim C_{\mathrm{Sob}}$. This is exactly what makes $\delta_0$ candidate-uniform — and exactly what removes the freedom to make $\beta_0$ small.

---

## The crux: β = O(1), the fixed-scale germ, and the unverified numerical thresholds

This is the central matter across layers 2 and 3, and it is created by the KEY assertion itself.

A01 Step 29 §1 says "$r$ is chosen so that $C_*\beta_0$ is below the absorption threshold," using $\beta_0\le C(L_\eta)r^2\sqrt M\to0$ as $r\to0$. A03 §6 instead pins $r_*\sim K_0^{-1/4}$ and reports $\beta\sim C_{\mathrm{Sob}}=O(1)$. These two statements are in tension, and the resolution is forced:

1. **The downstream contradiction requires a fixed-size germ with nonzero Einstein constant and nonzero Weyl.** Derdziński needs $g_\infty$ Einstein with $\mathrm{Ric}=-g_\infty$ and $|W^+|^2=1/24\ne0$ on an open set. The tangent-ball pullback lives on $B_\rho(0)$ with $\rho\lesssim r/4$. Cheeger–Gromov/harmonic-coordinate compactness produces a nondegenerate limit only when $\rho$ is bounded below along the sequence. If one shrinks $r\to0$ to make $\beta_0$ small, then $\rho\to0$; rescaling to unit size sends the curvature and the Einstein constant to zero, and the limit is flat $\mathbb R^4$ — the Weyl calibration $|W^+|^2=1/24$ collapses and there is nothing to contradict. Therefore $r$ must stay at $r_*=O(1)$ (indeed $r_*\sim K_0^{-1/4}=O(1)$ since $K_0=O(1)$).

2. **At $r=r_*=O(1)$, $\beta_0=O(1)$**, by (c). The entrance condition $C_*\beta_0<\Lambda$ becomes a numerical inequality between two fixed geometric constants ($C_*C_{\mathrm{Sob}}$ versus a threshold $\Lambda$ set by support ratios and cutoff smoothness). Nothing in Steps 24–29 or the passing scripts tracks these constants; the scripts verify Hölder-exponent algebra and Moser bookkeeping, not this inequality.

3. **A second numerical matching appears in the buffer condition.** The tangent-ball diffeomorphism requires $K\rho^2<\pi^2/4$ with $K=K_{\mathrm{pl}}=C\beta/(\theta r_*^2)=O(1/\theta)$ and $\rho=O(r_*)$, giving $K\rho^2\sim C\beta/(16\theta)$. Meanwhile the bootstrap Gronwall needs $C_1\theta<\ln 2$. Both hold simultaneously only if $C\beta/40<\ln2/C_1$ — again a numerical relation among fixed order-one constants, asserted satisfiable but not shown. (Shrinking $\rho\sim\sqrt\theta\,r_*$ keeps $\rho=O(1)$ only while $\theta=O(1)$, so this does not evade item 2.)

The upshot: the KEY assertion "β universal ⟹ $\delta_0$ universal" is correct about volume-independence and order-one size of $\beta$, and this is *necessary* for uniformity. It does **not** by itself deliver bootstrap closure, because closure needs $\beta$ (and $\theta$) below fixed thresholds, and the program provides no constant-level verification that the actual order-one values sit on the admissible side. Resolving this needs explicit tracking of $c$, $C$, $C_*$, $C_{\mathrm{Sob}}$, $\Lambda$, and $\theta$ through Steps 24–27 for the first few Moser exponents, sufficient to exhibit $C_*C_{\mathrm{Sob}}<\Lambda$ and $C\beta/(16\theta)<\pi^2/4$ with $C_1\theta<\ln2$ jointly. This is the calculation that would convert the chain from "consistent structure" to "closed argument."

---

## (d) Moser time exponent (1+n/2)/p₀ — correct

I verified this three ways.

- **Both applications land on the physically expected rates.** Curvature $p_0=3$: exponent $(1+2)/3=1$, giving $\|aF\|_\infty\le C\beta/t$ (the pseudolocality $|Rm|\le C/t$ form). Defect $p_0=6$: exponent $3/6=1/2$, combining with the seed $t$-power to give $\|aE\|_\infty\le C\delta(r^2/t)^{1/3}$. Both reproduce.
- **Parabolic scaling in $n=4$.** Under $x\to\lambda x$, $t\to\lambda^2t$, I computed the total dimension of the right side $S^{n/(2p_0)}\,t^{-(1+n/2)/p_0}(\int_{t/2}^t H_{p_0})^{1/p_0}$ and obtained the net length exponent $\frac{1}{p_0}(n-n^2/4)-2$. For $n=4$ this equals $-2$ exactly, matching $\|aF\|_\infty\sim L^{-2}$ (curvature dimension), independent of $p_0$. The vanishing of $n-n^2/4$ at $n=4$ is the same four-dimensional coincidence used for the volume cancellation.
- **Bookkeeping identity.** With $\kappa=1+2/n$, $\sum_{k}1/p_k=\frac{n+2}{2p_0}$ and net Sobolev power $\frac1\kappa\sum 1/p_k=\frac{n}{2p_0}$. The time exponent $(1+n/2)/p_0=(n+2)/(2p_0)$ equals $\sum 1/p_k$, i.e. the accumulated $1/t$ time-cutoff loss over all iterations. Internally consistent, and the Step 28 correction (distinguishing $\sum 1/p_k$ from the Sobolev power) is right.

The convergence of the Moser product under polynomial $p$-growth ($\sum(\log L_k)/p_k<\infty$ with $p_k$ geometric, $\log L_k\sim k+\log p_k$) is also correct.

---

## (e) Derdziński contradiction — valid via the conformal-Kähler route

The calibrated data check out: $s_\infty=-4$ and $s+8\sqrt6|W^+|=0$ give $|W^+|=1/(2\sqrt6)$, $|W^+|^2=1/24$. The spectrum $(-1/6,1/12,1/12)$ is trace-free ($\sum=0$) with $\sum\lambda_i^2=6/144=1/24$, matching, and it is the extremal type-D configuration $(-2,1,1)\times\tfrac{1}{12}$ forced by the lowest eigenvalue saturating $w=-\sqrt{2/3}\,|W^+|=-1/6$ (the $\mathcal G_\infty=0$ equality case).

The contradiction is clean via conformal-Kähler:
- Einstein 4-metric with $W^+$ of type D (double eigenvalue) and $W^+\ne0$ is locally conformally Kähler by the factor $(24|W^+|^2)^{1/3}$ (Derdziński).
- Here $24|W^+|^2=1$, so the factor is $1$ and $g_\infty$ itself is Kähler on the open set, hence Kähler–Einstein.
- Kähler–Einstein in dimension 4 forces $|W^+|^2=s^2/24=16/24=2/3$, contradicting $1/24$.

Valid, provided the limit germ genuinely carries constant $|W^+|^2=1/24$, the type-D spectrum, and smooth Einstein structure on an open set — all of which follow from $A_\rho\mathfrak D(p_i)\to0$ and smooth subsequential convergence (the fixed-scale germ of the crux above).

**One phrasing to drop.** A01 §3 and part of Step 28 route the contradiction through "$\nabla W^+=0$ forced, but $|\nabla W^+|^2=1/16\ne0$." Constant eigenvalues do not by themselves force $\nabla W^+=0$ (eigenframes may rotate), so that assertion is not justified. The computed value is right — via the Einstein Weitzenböck identity $\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$ with constant $|W^+|^2$, using $\det W^+=(-1/6)(1/12)^2=-1/864$, one gets $2|\nabla W^+|^2=1/6-1/24=1/8$, so $|\nabla W^+|^2=1/16$. But $|\nabla W^+|^2=1/16\ne0$ is *consistent with* a locally Kähler(–Einstein) germ and is not itself a contradiction; the actual contradiction is the modulus clash $1/24\ne2/3$. The conformal-Kähler route is the reliable one and does not need the parallel-Weyl assertion.

---

## (f) Remaining gaps in the conditional chain

Beyond the crux (numerical threshold matching), the following are open substance, most acknowledged in the notes:

1. **Smooth existence and continuation of the degenerate flow $\partial_t g=-2\chi^2(\mathrm{Ric}+g)$.** Where $\chi=0$ the metric is frozen and the principal part degenerates; this is not a uniformly parabolic system, so the standard DeTurck short-time existence "from Yang §8" and the remark that the zeroth-order $-2\chi^2 g$ "does not change the principal symbol" do not address the degeneracy of the leading operator itself across the transition annulus. The continuation via the shifted curvature $U=a(\mathrm{Rm}+G)$ and "Wang Theorem 4.1 derivative induction / Proposition 4.14 grouped IBP" is explicitly marked schematic and not expanded to the tensor level. This is a genuine unfilled analytic core, not a formality.

2. **The power-energy inequality (2.3)/(4.2) with polynomial $p$-dependence** is derived schematically for both $f=F$ and $f=|E|$. The full index-level derivation (moving norm and volume, Lichnerowicz reaction, Hessian integration by parts, Kato regularization of $|E|$ at its zeros, and explicit constant tracking for the first several $p_k$) is not carried out. The passing scripts verify the Hölder factorization and exponent sums, not this inequality.

3. **Simultaneous multi-support closure.** The number of active supports is $N_i=O(A_i)$ at scale $r_*=O(1)$. The argument treats supports as exactly disjoint with stationary collars so that $Q_{\mathrm{global}}(T)\le e^{C\theta}Q_{\mathrm{global}}(0)$; the metric comparison and Sobolev persistence must hold uniformly across all supports at the same terminal time. Since supports are disjoint and self-contained this is plausible, but the uniformity of constants over a growing family should be stated at the term level rather than asserted.

4. **Relation to the original Yau Problem 26 proposition.** Even with every conditional piece completed, this establishes a lower Ricci-pinching gap $\delta\ge\delta_0$ on the Ishida–LeBrun family under the $\lambda=-1$ normalization. Logically this *removes* that family as a candidate counterexample to Yau 26 in the window $\delta<\delta_0$; it does not prove the proposition (which asks whether pinching forces an Einstein metric for all $M^n$, all $n\ge2$, both signs of $\lambda$), nor does it refute it. The $\lambda>0$ branch, dimensions $n\ge5$ (where the notes themselves record that Kaluza–Klein positive-Einstein collapse defeats collapse-exclusion), arbitrary four-manifold topologies, dimension-only constants $c_n<C_n$, and the Lean formalization all remain untouched. The result is evidence narrowing one four-dimensional candidate family under one sign, not a resolution of Problem 26.

---

## Summary

Layer 1 (topological gap) is correct as algebra, resting on the cited monopole inequality. The two cancellation identities in β and in the Moser outputs are exact, the parabolic time exponent $(1+n/2)/p_0$ is correct and scaling-consistent in $n=4$, and the Derdziński contradiction is valid through the conformal-Kähler route (the alternative parallel-Weyl phrasing should be dropped). The dependency graph is non-circular.

The one matter on which the analytic-plus-geometric layers actually turn is quantitative: the same fact that makes β collapse-independent and universal ($\beta=O(1)$, verified) also forbids shrinking β, while the fixed-size nonzero-curvature Einstein germ needed for Derdziński forbids shrinking the scale — so bootstrap closure and the tangent-ball diffeomorphism reduce to numerical inequalities among fixed order-one constants ($C_*C_{\mathrm{Sob}}<\Lambda$; $C\beta/(16\theta)<\pi^2/4$ jointly with $C_1\theta<\ln2$) that are asserted admissible but nowhere tracked. Plus the degenerate-parabolic existence/continuation and the index-level power-energy inequality remain schematic. These are the concrete pieces whose completion would decide whether the chain is a consistent architecture or a closed proof of the family-restricted statement.
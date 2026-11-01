# TTCS Independent Branch Record

```json
{
  "step_id": 29,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step29_consolidated_conditional_theorem.md",
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Verify the following claims from the consolidated conditional theorem for the Ishida-LeBrun no-Einstein family, checking each step against the supplied mathematical evidence:

1. ABOVE-CRITICAL TOPOLOGICAL GAP: For sigma = D - A/3 > 0, the Chern-Gauss-Bonnet identity I - R = 2A/3 - sigma combined with the monopole inequality I >= 2A/3 forces R >= sigma. Since |Ric_0|^2 <= 4*delta^2 pointwise under Ricci pinching, R <= delta^2*Vol/(2pi^2). Combined with Vol bounded by topology, this gives delta >= c*sqrt(sigma/A). Verify that this chain has no gap and that the volume bound is justified.

2. UNIFORM K_0: For the IL family, int|Rm|^2 = 32pi^2*chi + 6*int|Ric_0|^2 from the decomposition |Rm|^2 = |W|^2 + 2|Ric_0|^2 + s^2/6 and CGB. With chi(M) ~ A + O(1) and Vol ~ 32pi^2A/9, K_0 ~ 9 + O(1/A). Check whether |Rm|^2 = |W|^2 + 2|Ric_0|^2 + s^2/6 is the correct decomposition in dimension 4, and whether the CGB identity used is accurate.

3. VOLUME CANCELLATION: beta = S*H_2^{1/2} = C*r^2*K_0^{1/2} is volume-independent. Check: S = C*r^2*Vol(B_r)^{-1/2} (Maheux-Saloff-Coste), H_2 ~ K_0*Vol(B_r), so S*H_2^{1/2} = C*r^2*K_0^{1/2}. With r = c*K_0^{-1/4}, beta = C*K_0^0 = C.

4. The defect identity D_a = R - sigma - (2/3)((a+)^2 - A) implies D_a <= R - sigma <= R, so the calibration tightens with sigma. Check this chain.

5. The general-p Moser iteration coefficient: the dissipation p*D_p controls |nabla Z_p|^2 with coefficient O(1/p), giving an extra factor p in the loss L_j. The Moser product converges because sum(log(p_j^4))/p_j < infinity. Verify.

## Output

# Verification Memo: Consolidated Conditional Theorem, Ishida–LeBrun Family

Prepared for the core research agent. I checked each of the five items against the supplied notes (Step 29, Step 3, Step 26, S0910A01 Step 28), reconstructing the algebra independently where the notes compress it. Four items hold as stated. One (Item 2) contains a numerical coefficient slip that does not disturb its stated conclusion, plus a hidden topological input worth pinning down. Details below, with the concrete objects involved.

---

## Item 1 — Above-critical topological gap: holds, and I can supply the missing volume step explicitly

The algebraic core is clean. Using $\sigma = D - A/3$, so $D = A/3 + \sigma$:

- Eq. (1.1) $I - R = (2\chi+3\tau)(M) = A - D = 2A/3 - \sigma$ is the standard LeBrun identity
$$(2\chi+3\tau)(M) = \frac{1}{4\pi^2}\int_M\Big(\frac{s^2}{24} + 2|W^+|^2 - \frac{|\operatorname{Ric}_0|^2}{2}\Big)\,d\mu,$$
with $I = \frac{1}{4\pi^2}\int(\frac{s^2}{24}+2|W^+|^2)$ and $R = \frac{1}{4\pi^2}\int\frac{|\operatorname{Ric}_0|^2}{2}$. Correct.
- Monopole input $I \ge 2A/3$ (Seiberg–Witten, selected sign, $(a^+)^2\ge A$): literature input for the family, accepted.
- Hence $R = I - 2A/3 + \sigma \ge \sigma$. Correct.
- Pointwise $|\operatorname{Ric}_0|^2 \le 4\delta^2$: eigenvalues $\mu_\alpha$ of $g^{-1}(\operatorname{Ric}+g)$ lie in $[-\delta,\delta]$; $|\operatorname{Ric}_0|^2 = \sum(\mu_\alpha-\bar\mu)^2$ is maximized (four values, two at $+\delta$, two at $-\delta$) at $4\delta^2$. Correct.
- Therefore $R \le \frac{\delta^2}{2\pi^2}\operatorname{Vol}$ (Eq. 1.4), and $\delta \ge \sqrt{2\pi^2\sigma/\operatorname{Vol}}$ (Eq. 1.6). Correct.

**The volume bound (Eq. 1.5) is the one nontrivial input, and the note states it only sketchily. It is genuinely justified, by this chain**, which I recommend inserting explicitly:

The upper Ricci bound $\operatorname{Ric}\le -(1-\delta)g$ forces $s \le -4(1-\delta)$, so $\int s^2 \ge 16(1-\delta)^2\operatorname{Vol}$. From $4\pi^2 I \ge \int s^2/24$ and $I = R + 2A/3 - \sigma$,
$$\int s^2 \le 96\pi^2\big(R + \tfrac{2A}{3} - \sigma\big).$$
Combining with $R \le \frac{\delta^2}{2\pi^2}\operatorname{Vol}$:
$$\big(16(1-\delta)^2 - 48\delta^2\big)\operatorname{Vol} \le 96\pi^2\big(\tfrac{2A}{3}-\sigma\big).$$
For small $\delta$ the bracket is $\approx 16 > 0$, giving $\operatorname{Vol} \lesssim 4\pi^2 A$. This is consistent with the calibration limit $\operatorname{Vol}\to 32\pi^2A/9\approx 3.56\pi^2A$ (the bound sits just above the limiting value, as it must). Feeding back:
$$\delta \ge \sqrt{\frac{2\pi^2\sigma}{4\pi^2 A}} = \tfrac{1}{\sqrt2}\sqrt{\sigma/A},$$
matching Eq. (1.7) with an explicit constant. 

The Proposition (a positive $\delta_*(M)$ for each fixed $M$ with $\sigma>0$) is therefore correct and rests only on Chern–Gauss–Bonnet, the signature identity, the monopole inequality, and the pointwise trace-free bound. No flow or collapse analysis enters. This is the most solid piece in the file, and the argument I reconstructed above closes the one place where the note gestured ("$\operatorname{Vol}\le C(1+R)$") without showing the mechanism.

One presentational inconsistency: Eq. (1.5)'s remark "$\operatorname{Vol}\to 32\pi^2A/9$ as $\delta\to0$ regardless of $\sigma$" is vacuous when $\sigma>0$, since the same section proves $\delta\ge c\sqrt{\sigma/A}>0$ prevents $\delta\to0$. That limit statement belongs only to the $\sigma=0$ case. Harmless to the conclusion.

---

## Item 2 — Uniform $K_0$: decomposition correct; CGB coefficient stated wrongly (6 vs 4); leading value 9 depends on an unstated topological input

**Decomposition.** In dimension 4, $|\operatorname{Rm}|^2 = |W|^2 + \frac{4}{n-2}|\operatorname{Ric}_0|^2 + \frac{2}{n(n-1)}s^2 = |W|^2 + 2|\operatorname{Ric}_0|^2 + \frac{s^2}{6}$ (full (0,4)-tensor norm). Correct.

**CGB coefficient is wrong.** The note (Step 29 §6.1) writes
$$\int|\operatorname{Rm}|^2 = 32\pi^2\chi(M) + 6\int|\operatorname{Ric}_0|^2.$$
Using the unambiguous tensor-norm Gauss–Bonnet $\chi = \frac{1}{32\pi^2}\int(|\operatorname{Rm}|^2 - 4|\operatorname{Ric}|^2 + s^2)$ with $|\operatorname{Ric}|^2 = |\operatorname{Ric}_0|^2 + s^2/4$:
$$32\pi^2\chi = \int(|\operatorname{Rm}|^2 - 4|\operatorname{Ric}_0|^2)\ \Longrightarrow\ \int|\operatorname{Rm}|^2 = 32\pi^2\chi + 4\int|\operatorname{Ric}_0|^2.$$
The correct coefficient is **4, not 6**. The value 6 comes from mixing the operator-norm Weyl convention (where the Weyl form of CGB carries coefficient $1$ on $|W|^2$) with the tensor-norm decomposition (where it carries $1/4$); the two are internally inconsistent and produce the spurious 6. I verified consistency: the tensor-norm Weyl form is $8\pi^2\chi = \int(\frac14|W|^2 - \frac12|\operatorname{Ric}_0|^2 + \frac{s^2}{24})$, which combined with the decomposition reproduces coefficient 4.

**Effect on the conclusion.** The erroneous term multiplies $\int|\operatorname{Ric}_0|^2 \le 4\delta^2\operatorname{Vol}$, contributing $24\delta^2$ (note) versus the correct $16\delta^2$. This is a subleading $O(\delta^2)$ term. The leading term is unaffected:
$$K_0 = \frac{32\pi^2\chi}{\operatorname{Vol}} + O(\delta^2), \qquad \text{with }\operatorname{Vol}\to \frac{32\pi^2A}{9}\ \Rightarrow\ K_0 \to \frac{9\chi}{A}.$$
So the value $K_0\to 9$ holds **if and only if $\chi(M)\sim A$.** This is asserted ("$\chi(M)\sim A + O(1)$") but not derived. It is not an automatic consequence of the family construction: for the symplectic summands, Noether's relation gives $\chi = 12\chi_h - c_1^2$, and $c_1^2 = 2\chi+3\tau$, so $\chi$ depends on the holomorphic Euler characteristics $\chi_h(X_j)$, not on $A=\sum c_1^2(X_j)$ alone. The constraint the family actually carries is $2\chi+3\tau = 2A/3$ at $D=A/3$, which fixes a combination of $\chi$ and $\tau$, not $\chi$ itself.

What the downstream argument truly needs is only that $K_0$ is **uniformly bounded above and below**, i.e. $\chi(M)\asymp A$ (so that $r_* = cK_0^{-1/4}$ stays bounded away from $0$ and $\infty$ across the family). The upper bound $\chi\lesssim A$ is the load-bearing part. I recommend deriving $\chi(M)\asymp A$ from the explicit summand data of the Ishida–LeBrun family (the $\chi_h(X_j)$ and $\chi(N)$), rather than asserting $\chi\sim A$. Until that is done, "uniform $K_0$" across the family is supported in structure but not established in fact.

---

## Item 3 — Volume cancellation in $\beta$: algebraically correct

$\mathsf S = C r^2\operatorname{Vol}(B_r)^{-1/2}$ is the Maheux–Saloff-Coste output (Step 26 §1.3, Eq. 1.3), and I checked its derivation: doubling + Buser–Poincaré (both requiring only $\operatorname{Ric}\ge kg$) give Sobolev with the constant depending on $n$ and $Kr^2$ only, not on $\operatorname{Vol}(B_r)$. The volume factor $\operatorname{Vol}(B_r)^{-1/2}$ is explicit and correct for the $L^2\to L^4$ embedding in $n=4$.

With $\widehat H_2 = \int_{\operatorname{supp}\chi}F^2 \lesssim K_0\operatorname{Vol}(B_r)$ (from the maximal-function selection $\mathcal M_r|\operatorname{Rm}|^2\le 4K_0$, giving $F^2 = 1+|\operatorname{Rm}|^2 \lesssim K_0$ on average over the good support):
$$\beta = \mathsf S\,\widehat H_2^{1/2} \le C r^2 \operatorname{Vol}(B_r)^{-1/2}\cdot K_0^{1/2}\operatorname{Vol}(B_r)^{1/2} = C r^2 K_0^{1/2}.$$
The volume cancels exactly. With $r_* = c K_0^{-1/4}$, $r_*^2 = c^2 K_0^{-1/2}$ and $\beta = Cc^2 K_0^0 = Cc^2$, volume- and collapse-independent, depending only on $n$ and $K_0$. Verified.

Two points on the underlying content (not defects in the item as stated): (i) only the upper bound $\widehat H_2\lesssim K_0\operatorname{Vol}(B_r)$ is needed for the cancellation, and the maximal-function selection supplies it. (ii) The constant $\beta=Cc^2$ is fixed, not automatically small; the smallness $\bar\beta\le\bar\beta_*\ll1$ required by the critical absorption is obtained by choosing $c$ small, which shrinks $r_*$ and the flow interval $\theta r_*^2$ while the plateau volume $\operatorname{Vol}(P)\ge\alpha A$ must be retained. That interlock is exactly what Assumptions (A1)–(A3) carry; the volume-cancellation statement itself is correct independently of it.

---

## Item 4 — Defect identity $D_a = R-\sigma-\frac23((a^+)^2-A)$, giving $D_a\le R-\sigma\le R$: holds

From S0910A01 Step 28 Eq. (1.3), with the notation match $J = R$ (normalized trace-free Ricci energy) and $q = \sigma = D - A/3 \ge 0$:
$$D_a = R - \sigma - \tfrac23\big((a^+)^2 - A\big), \qquad (a^+)^2 \ge A\ \text{(selected sign)}.$$
Since $(a^+)^2 - A \ge 0$, the subtracted term is nonnegative, so $D_a \le R - \sigma$; since $\sigma\ge0$, $R-\sigma\le R$. The nonnegativity $D_a\ge0$ is the completion-of-squares statement (Step 3's identity $27\int(\frac{s^2}{24}+2|W^+|^2) - \int(s-\sqrt6|W^+|)^2 = \frac18\int(s+8\sqrt6|W^+|)^2$, all summands squares). Chain correct.

The tightening interpretation follows: $\int(s+8\sqrt6|W^+|)^2 = 864\pi^2 D_a \le 864\pi^2(R-\sigma)$, so larger $\sigma$ lowers the deficit ceiling. Logically sound given the identity. I did not re-derive the constant $864\pi^2$ from first principles (it is a completion-of-squares constant checked by the associated script); the structural relation asked for is what matters and it is correct.

---

## Item 5 — General-$p$ Moser coefficient and product convergence: holds

The gradient relation is correct: with $Z_p = \eta a^{(p-1)/2}F^{p/2}$, the dominant term of $\nabla Z_p$ is $\frac{p}{2}\eta a^{(p-1)/2}F^{p/2-1}\nabla F$, so
$$|\nabla Z_p|^2 \lesssim \tfrac{p^2}{4}a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2 + (\text{cutoff terms}),$$
matching Eq. (4.1). Inverting (Eq. 4.2), controlling $\|\nabla Z_p\|_2^2$ through the available dissipation $pD_p$ costs a factor $\sim p$, so the total per-step loss carries $p^4$ (the pre-existing $p^3$ times the extra $p$), Eq. (4.3): $L_j = Cp_j^4\,4^j(t^{-1}+r^{-2})$.

Convergence: with $p_j = p_0(3/2)^j$, $\log L_j = 4\log p_j + j\log 4 + O(1) = O(j)$ while $p_j$ grows geometrically, so
$$\sum_j \frac{\log L_j}{p_j} \lesssim \sum_j \frac{j}{(3/2)^j} < \infty.$$
Any polynomial-in-$p_j$ deterioration is absorbed. Correct. I also checked the auxiliary sums: $\sum_j \frac{2}{3p_j} = \frac{2}{3p_0}\cdot 3 = \frac{2}{p_0}$ (Eq. 4.5), giving net Sobolev power $\mathsf S^{2/p_0}$ ($\mathsf S^{2/3}$ for $p_0=3$, $\mathsf S^{1/3}$ for $p_0=6$); and $\sum 1/p_j = 3/p_0$, consistent with Step 28's $(n+2)/(2p_0)=6/(2p_0)=3/p_0$ and net power $n/(2p_0)=2/p_0$. The two notes agree. Verified.

---

## Summary of what is established and what remains open in these five items

- **Items 1, 3, 4, 5 hold** as stated, with correct algebra. Item 1 in particular is a self-contained result for each fixed $\sigma>0$ manifold, resting only on topology + Seiberg–Witten + Chern–Gauss–Bonnet + the pointwise pinch; I supplied the explicit volume-bound derivation the note left implicit, with constant $\delta\ge\frac{1}{\sqrt2}\sqrt{\sigma/A}$.
- **Item 2 needs two corrections.** The coefficient in $\int|\operatorname{Rm}|^2 = 32\pi^2\chi + c\int|\operatorname{Ric}_0|^2$ is $c=4$, not $6$ (a mixed-convention slip); this only affects a subleading $O(\delta^2)$ term, so the qualitative conclusion "$K_0$ bounded" survives. But the numerical value $K_0\to9$ and, more importantly, the *uniform two-sided* bound on $K_0$ across the family require $\chi(M)\asymp A$, which is asserted, not derived, and does not follow from $A=\sum c_1^2(X_j)$ alone (via Noether, $\chi$ depends on the $\chi_h(X_j)$). Deriving $\chi(M)\asymp A$ from the explicit summand data would convert "uniform $K_0$" from structurally-plausible to established, and this feeds directly into the uniform-$\delta_0$ statement of §6 and the uniform $r_*$ that Item 3 relies on.

All five items live entirely inside the conditional framework (A1)–(A4) and address only the $\lambda<0$ normalization on the critical/above-critical Ishida–LeBrun family in dimension 4; that positioning is stated plainly in Step 29 §7 and Step 28 §4 and I found no drift on it in the material checked.
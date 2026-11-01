# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A03/workspace/scripts/verify_step25_normalization_and_moser_exponents.py",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Sessions/S0910A01/workspace/codex_loop/work/verify_tensor_energy_ledger.py",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the Step 25 mathematical repair for the four-dimensional normalized cutoff flow. Check (i) the combined fully covariant tensor, inverse-metric, and measure contributions under the homothetic piece -2ag, including the formula for the pure-normalization variation of F^p dmu; (ii) the general weighted weak power inequality for K_p=int eta^2 a^(p-2) Phi^p with Phi=F or |E|; (iii) the H3-potential interpolation and Young exponents; and (iv) the exact match p'_j=p_j-2 with Yang's fixed-cutoff Moser iteration in n=4, including whether p0=3 gives |a Rm|<=C beta/t and p0=6 gives |aE|<=C delta(r^2/t)^(1/3) on the whole active support. Identify any hidden cutoff, measure, tensor-regularization, or exponent error. Give corrected formulas if needed; do not infer a pinching gap unless the supplied proof actually closes.

## Output

## Verification Memo — Step 25 normalized cutoff-flow algebra (n=4)

I independently reworked every exponent, weight, contraction, and scaling identity in the Step 25 note and its two companion scripts, and cross-checked against Yang (1992), Appendix A. The algebraic content is correct throughout; I reproduce each identity below. The genuinely unresolved mathematical substance lies outside the algebra, and both notes state it explicitly. I separate the two.

---

### (i) Homothetic bookkeeping and the F^p dμ variation — correct

For spatially constant $a$ and $\partial_t g=-2ag$ the metric evolves as $g(t)=e^{-2at}g(0)$, i.e. a pure homothety $c=e^{-2at}$, $\dot c=-2ac$.

- Mixed $R^\ell{}_{ijk}$ is scale-invariant, so $\partial_t R^\ell{}_{ijk}=0$; lowering one index gives $\partial_t R_{ijkl}=-2aR_{ijkl}$ (2.1). ✓
- $x=|\mathrm{Rm}|^2\sim c^{-2}$ (curvature dimension $L^{-2}$): two lowered tensors give $-4ax$, four inverse metrics give $+8ax$, hence $\partial_t x=4ax$ (2.2). ✓
- $\partial_t d\mu=\tfrac12\mathrm{tr}_g(-2ag)\,d\mu=-4a\,d\mu$ in $n=4$; therefore $\partial_t(x\,d\mu)=0$ (2.3): the $\int|\mathrm{Rm}|^2$ energy is scale-invariant in four dimensions. ✓

For $F=(1+x)^{1/2}$: $\partial_t F=2axF^{-1}$, so $\partial_t F^p=2ap(F^2-1)F^{p-2}=2ap(F^p-F^{p-2})$, and with the measure,
$$\partial_t(F^p d\mu)=2a\big[(p-2)F^p-pF^{p-2}\big]d\mu,$$
matching (2.4). At $p=2$ this is exactly $-4a\,d\mu$ (only the additive constant in $F^2$ survives). The script's `Fp_density` reduction is faithful.

The scientifically important reading: for $p>2$ the surviving term is $\approx+2a(p-2)F^p>0$. There is **no** homothety-induced damping $-4aF^2$; the normalized flow does not gain a coercive curvature term. Framing (2.5) as a scale-consistent inequality whose reaction is absorbed by smallness of $\beta$ (Sobolev $\times$ local $L^2$ curvature), rather than by normalization damping, is the correct mechanism and coincides with Yang's original absorption. Removing the earlier reliance on a damping term is a legitimate correction that does not break the chain.

### (ii) Weighted weak power inequality — weights consistent

With $K_p=\int\eta^2 a^{p-2}\Phi^p$ and $Z_p=\eta a^{(p-1)/2}\Phi^{p/2}$, note $Z_p^2=\eta^2a^{p-1}\Phi^p$ (one extra power of $a$ over $K_p$, the diffusion weight). The reaction $\int\eta^2a^{p-1}F\Phi^p$ reproduces every explicitly derived case:

- $\Phi=F$, $p=2$: $a^{1}F\cdot F^2=aF^3$ — the $H_2$ reaction. ✓
- $\Phi=F$, $p=3$: $a^{2}F\cdot F^3=a^2F^4$ — the weighted $q=3$ reaction. ✓
- $\Phi=|E|$, $p=2$: $aF|E|^2$ — the triangular defect potential. ✓

These three are the cases the A01 memo derives in full (with the ledger script confirming the contractions), so (4.2) is a structurally sound generalization at the weight level. Two points worth recording, neither of which affects the endpoint:

1. The intermediate powers $3\le p\le 6$ (and beyond) are asserted by analogy; the Hessian-$a$ integration-by-parts and the sign of the diffusion coefficient are verified in closed form only at $p=2,3$ (curvature) and $p=6$ (defect). The diffusion terms in (3.3) carry coefficients $-q$ and $-q(q-2)$, both dissipative for all $q\ge2$, so uniform positivity of the dissipation is not in doubt.
2. Relating $\|\nabla Z_p\|_2^2$ (chain rule on $\Phi^{p/2}$ produces $p^2/4$) to the raw equation dissipation ($\sim p$) can cost a factor of $p$. This only changes the polynomial power of $p$ in $L_j$; see (iv), where the Moser product is insensitive to that power.

### (iii) H₃ interpolation and Young exponents — correct

Weight identity (4.4): $(aF^3)^{1/3}(a^{3p/2-2}\Phi^{3p/2})^{2/3}=a^{1/3+p-4/3}F\Phi^p=a^{p-1}F\Phi^p$. ✓ (the two `sympy` exponent asserts encode exactly the $a$-power $p-1$ and the $F/\Phi$-power $p+1$.)

Cauchy–Schwarz $K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}$: splitting $\eta^2a^{3p/2-2}\Phi^{3p/2}$ into $(\eta^2a^{p-2}\Phi^p)^{1/2}(\eta^2a^{2p-2}\Phi^{2p})^{1/2}$ is exact. ✓

$K_{2p}^{1/2}=\|Z_p\|_4^2$: here the harmless point is $Z_p^4=\eta^4a^{2p-2}\Phi^{2p}$ but $\eta=1$ wherever $a>0$, so $\eta^4$ collapses to $\eta^2$ on the integrand's support; and $\|Z_p\|_2^2=\int\eta^2a^{p-1}\Phi^p\le K_p$ using $a=\chi^2\le1$. ✓

Chaining Hölder $(3,\tfrac32)$ + interpolation + relative Sobolev + Young gives
$$Cp\!\int\!\eta^2a^{p-1}F\Phi^p\le\tfrac c2\|\nabla Z_p\|_2^2+Cp^3(r^{-2}+\mathsf S^2H_3)K_p,$$
matching (4.6): the outer $Cp$ cubed to $p^3$ under Young against a $2/3$-power. With $\mathsf S^2H_3\le C\beta_*^3/t$ from (3.2), (4.7) follows. ✓

I confirm the $\mathsf S^2H_3(t)\le C\beta_*^3/t$ input is not a mere time-integral: the spacetime bound $\int_{t/2}^t H_3\lesssim\beta_a H_2(0)=\mathsf S\|F\|_2^3=\beta_*^3/\mathsf S^2$ (using $\int D_2\lesssim H_2(0)$ from the $q=2$ estimate) combined with forward propagation $H_3(t)\le e^{C(t-s)/r^2}H_3(s)$ from the separate $q=3$ equation and the mean-value trick yields $H_3(t)\lesssim t^{-1}\int_{t/2}^tH_3$. The note's insistence that both equations are needed is accurate.

### (iv) Exact match with Yang and the two endpoint scalings — correct

In $n=4$, $v=1+2/n=3/2$, $n/2=2$. Yang's Appendix A recursion is $p_k=p_0v^k$, $p'_k=(p_0-2)v^k+\sum_{j=0}^{k-1}v^j$. Since $\sum_{j=0}^{k-1}(3/2)^j=2(v^k-1)$,
$$p'_k=(p_0-2)v^k+2v^k-2=p_0v^k-2=p_k-2.$$
This holds for **every** $p_0$ and is a clean consequence of $n/2=2$ in dimension four. The recursion $p'_{k+1}=\tfrac32p'_k+1$ is consistent with it. Hence Yang's moment $\chi^{2p'_k}\Phi^{p_k}=a^{p_k-2}\Phi^{p_k}=K_{p_k}[\Phi]$, and the endpoint $\chi^{2p'_k/p_k}\Phi\to\chi^2\Phi=a\Phi$ ($p'_k/p_k\to1$). ✓ The `pprime_source` loop verifies both the identity and the recursion for $p_0\in\{3,6\}$, $k\le11$.

Potential exponent $q=6>4$: $\int\chi^{q-n}u^{q/2}=\int\chi^2F^3=H_3$ ($u\sim|\mathrm{Rm}|\sim F$ is the potential multiplying $f=|\mathrm{Rm}|$). ✓ Dimensionless combination: $\mu=t^{1/3}H_3^{1/3}\le C\beta_*\mathsf S^{-2/3}$, so $\mathsf S^{2/3}\mu=C\beta_*$ and $(\mu\mathsf S^{n/q})^{q/(q-n)}=(C\beta_*)^3$, entering as $C\beta_*^3/t$, exactly the coefficient in (4.7). The identification with the fixed-cutoff powers is genuine, not merely analogous.

Product convergence: $\sum 1/p_k=3/p_0$, $\sum(k+\log p_k)/p_k<\infty$, both insensitive to the polynomial-in-$p$ power in $L_j$; the endpoint $\mathsf S$-exponent $2/p_0$ and time exponent $3/p_0$ in (5.10) follow. ✓

**Curvature, $p_0=3$:** $\mathcal M_{3,0}=\int_{t/2}^tH_3\le C\beta_*^3/\mathsf S^2$; substituting into (5.10):
$$\|aF(t)\|_\infty\le C\mathsf S^{2/3}(t^{-1}+r^{-2})(\beta_*^3/\mathsf S^2)^{1/3}=C\beta_*(t^{-1}+r^{-2})\xrightarrow{t\le r^2}C\beta_*/t.$$
✓ matches (6.2) and the script's `curv` reduction.

**Defect, $p_0=6$:** $K_6[|E|]=\int\eta^2a^4|E|^6=J_6$, and $\mathcal M_{6,0}\le Ct\,\delta^6V$ (with $J_6(0)\le C\delta^6V$, $e^{Cs/r^2}=O(1)$ for $s\le r^2$). Then
$$\|a|E|(t)\|_\infty\le C\mathsf S^{1/3}(t^{-1}+r^{-2})^{1/2}(t\delta^6V)^{1/6}\xrightarrow{t\le r^2}C\mathsf S^{1/3}\delta V^{1/6}t^{-1/3},$$
and with $\mathsf S\le Cr^2V^{-1/2}$ this collapses to $C\delta(r^2/t)^{1/3}$, matching (6.5) and `defect_scaled`. ✓ The integral (6.6) $\int_0^{\theta r^2}\|aE\|_\infty ds=\tfrac32C\delta\theta^{2/3}r^2$ is correct and finite because $s^{-1/3}$ is integrable at $0$.

Both endpoint quantities are genuinely whole-support (weighted by $a=\chi^2$ across the transition collar, not only on the $\chi=1$ plateau), which is what feeds the metric-comparison integral (8.2).

**No hidden cutoff/measure/tensor-regularization error found.** The buffer (1.1) legitimately annihilates all $a\,d\eta$ and $da\,d\eta$ terms; $|da|^2/a=4|d\chi|^2$ (3.6) extends smoothly; the defect regularization ($|E|^2$ heat identity (4.3), Moser on $(|E|^2)^{p/2}$) is standard. The ledger script's degree check confirms the integrated Hessian-$a$ contribution to the defect energy is $\ge$ quadratic in $E$ — i.e. there is **no** $E$-independent or $E$-linear $(\nabla^2a)*g$ source, so the defect estimate is truly triangular and self-improving. This structural fact is the load-bearing one and it holds.

---

### What the supplied material does not yet establish

The task asks not to infer a pinching gap unless the proof closes; the supplied text does not close it, and says so. The unresolved substance:

1. **Continuation of the degenerate normalized flow.** The slice-wise inequalities (4.3),(5.4),(7.3) presuppose an already-smooth solution. Step 25 §7 and A01 §8(1) state that the Wang-type extension induction (bounded $|\chi^2\mathrm{Rm}|$ extends the flow) has been written only for the *unnormalized* local Ricci flow; the adaptation carrying the extra $-2ag$ term is described but not written. This is the principal missing analytic object.

2. **Simultaneous first-exit closure.** A01 §8(2)–(5) is explicit that the three energy inequalities alone do not imply the metric equivalence (8.2) with a uniform constant, nor Sobolev persistence, nor propagation of $\beta_a(t)$. The intended closure is: (6.6) improves the provisional bilipschitz bound for small $\delta$, which then improves $\mathsf S$, $|d\chi|_{g(t)}$, and $\beta$ together. The pieces are consistent, but whether the improved constants strictly dominate the provisional ones uniformly — the actual continuity/first-exit step — is asserted, contingent on item 1.

3. **Asserted inputs.** The relative Sobolev scaling $\mathsf S\le Cr^2V^{-1/2}$ (6.4) and the good-support initial smallness $\beta(0)\le Cr^2\sqrt{1+K_0}$ are stated from the volume-comparison / Croke isoperimetric machinery (Yang §7, Thm 7.4) but not derived in the supplied files. The exponent verification is independent of their exact constants; the closure of item 2 is not. These should be traced to an explicit statement.

4. **The value-carrying terminal step is not in the supplied files.** The conclusion the whole branch exists to reach is the geometric contradiction: $\mathrm{Spec}(W^+)=(-1/6,1/12,1/12)$, $\delta W^+=0\Rightarrow\nabla W^+=0$, against the Einstein–Weyl scalar identity $|\nabla W^+|^2=1/16$. None of the three constants, nor the implication $\delta W^+=0\Rightarrow\nabla W^+=0$ under the stated spectrum, can be checked from what is provided; the Step 6 computation is referenced only. This is the single most consequential item to verify independently, and it is currently external.

5. **Range of applicability.** Even with items 1–4 settled, Step 25 §7 states this advances only the critical four-dimensional Ishida–LeBrun family (target $\lambda<0$) and does not touch the dimension-dependent interval statement of the full problem. The construction is one obstruction argument on one family in one dimension, not the general dichotomy.

**Summary.** Every quantity you asked me to check — the combined homothetic tensor/inverse-metric/measure bookkeeping and the $F^p d\mu$ formula (i), the weighted power inequality's weights (ii), the $H_3$ interpolation and Young exponents (iii), the exact $p'_j=p_j-2$ Yang identification and the two endpoints $|a\mathrm{Rm}|\le C\beta_*/t$, $|aE|\le C\delta(r^2/t)^{1/3}$ on the whole active support (iv) — is algebraically correct and internally consistent, and the scripts genuinely verify it. The exponent machinery is sound. The unfinished mathematics is the normalized-flow continuation theorem, the quantitative first-exit closure that turns the weighted bounds into a uniform interval, the two asserted geometric-analytic inputs (6.4) and the initial smallness, and independent confirmation of the terminal Weyl-curvature contradiction and its three constants.
# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step3_mixed_bound_analysis.md",
    "Sessions/S0910A01/workspace/scripts/mixed_sw_bound_analysis.py",
    "Knowledge/objects/papers/Spin-Manifolds-Einstein-Metrics-and-Differential-Topology--1a2235341441--f19aa00d70c8/object.md"
  ]
}
```

## Task

Verify the following argument for a uniform Ricci-pinching lower bound on LeBrun manifolds using the mixed Seiberg-Witten estimate. The claim is: for M = X#k CP̄² (X a minimal surface of general type, A = c₁²(X)), any metric g with δ_-(g) = δ (Ricci eigenvalues in (-(1+δ), -(1+δ))) satisfies δ/(1-δ) ≥ √((k/A - 1/3)/2) whenever k > A/3. The argument uses: (1) Proposition 4 from Ishida-LeBrun with the sign-trick optimization giving (a⁺)² ≥ A; (2) CGB formula giving ∫|r̊|²/2 ≥ 4π²(k-A/3); (3) pointwise bound |r̊|² ≤ 4δ²; (4) volume upper bound from CGB V ≤ 4π²(A-k)/(2(1-δ)²/3 - 2δ²). Check each step, especially: (a) Is the sign trick valid for a single factor X (not just X#Y as in the Ishida-LeBrun proof)? (b) Is the pointwise bound |r̊|² ≤ 4δ² correct (given |Ric - σg|_op ≤ δ)? (c) Does the volume bound follow correctly from CGB? (d) Is the final inequality tight? (e) Does the argument correctly imply that the no-Einstein range extends from k > 2A/3 (scalar-only) to k > A/3 (mixed)?

## Output

## Verification Memo: Uniform Ricci-Pinching Floor on LeBrun Manifolds via the Mixed SW Estimate

### Overall

The four-step derivation is mathematically correct, and the end result

$$\frac{\delta}{1-\delta}\ \ge\ \sqrt{\frac{p-1/3}{2}}\,,\qquad p=k/A,$$

holds for LeBrun manifolds $M=X\#k\overline{\mathbb{CP}}{}^2$ with $X$ minimal of general type, in the regime $1/3<p<1$. I reproduced every step symbolically and the algebra closes exactly. The genuinely new content is the quantitative pinching floor depending only on $p$; the Einstein non-existence statement it contains (step e) is the already-known optimal LeBrun result. Below I check each step and mark two places where the written argument omits substance needed for it to be complete, plus one point about what "tight" does and does not establish.

A preliminary textual matter: the stated interval "Ric eigenvalues in $(-(1+\delta),-(1+\delta))$" is degenerate as written (both endpoints equal). The derivation uses, and only makes sense with, $\operatorname{Ric}$ eigenvalues in $[-(1+\delta),-(1-\delta)]$, i.e. $|\operatorname{Ric}+g|_{\mathrm{op}}\le\delta$ after normalizing the center to $-1$. This same typo is carried in the script comments. All checks below use the sensible reading.

### (a) The sign trick for a single factor $X$

**The optimization itself is valid for a single factor.** Write $a=\alpha+\sum_j \hat E_j$ with $\alpha=c_1(X)$, choosing $\hat E_j=\pm E_j$ so that $\hat E_j\cdot\alpha^+\ge0$. Then

$$(a^+)^2=(\alpha^+)^2+2\sum_j\alpha^+\!\cdot\hat E_j^+ + \Big(\sum_j\hat E_j^+\Big)^2.$$

For harmonic representatives $\alpha^+\!\cdot\hat E_j^+=\alpha^+\!\cdot\hat E_j\ge0$ (the anti-self-dual part of $\hat E_j$ is orthogonal to $\alpha^+$ under the intersection form), and $(\sum\hat E_j^+)^2\ge0$ because the form is positive on $\mathcal H_g^+$. Hence $(a^+)^2\ge(\alpha^+)^2$, and $(\alpha^+)^2=\alpha^2-(\alpha^-)^2\ge\alpha^2=A$ since $(\alpha^-)^2\le0$. So $(a^+)^2\ge A$. This computation uses only the $E_j$ and $\alpha$; it does not depend on $X$ being itself a connected sum, so it transfers verbatim from the $X\#Y$ setting to $X\#k\overline{\mathbb{CP}}{}^2$.

**The one thing that does not transfer is the source of the monopole class.** Ishida–LeBrun Theorem 7 obtains monopole classes on $X\#Y\#k\overline{\mathbb{CP}}{}^2$ through the Bauer–Furuta cohomotopy invariant precisely because the ordinary Seiberg–Witten invariant vanishes on a connected sum of two pieces each with $b_+\ge1$; that machinery genuinely needs at least two symplectic summands. For a single $X\#k\overline{\mathbb{CP}}{}^2$ the ordinary SW invariant is nonzero: $X\#k\overline{\mathbb{CP}}{}^2$ is symplectic (blow-up of a symplectic manifold), Taubes' theorem gives nonzero SW for the canonical $\mathrm{spin}^c$ structure, and the blow-up formula produces the classes $\alpha+\sum\pm E_j$. This is exactly LeBrun's own construction in "Four-manifolds without Einstein metrics" and "Ricci curvature, minimal volumes, and SW theory," not the Bauer–Furuta route. The note cites Ishida–LeBrun's Proposition 4 (the curvature estimate — fine, it is general) but leans on the Theorem-7 monopole mechanism, which is the wrong grounding for a single factor. The correct citation is LeBrun's earlier two papers. Two conditions must be recorded for the single-factor grounding: $b_+(X)=1+2p_g(X)\ge2$ so that Definition 1 applies (a minimal general-type surface with $p_g=0$, e.g. a Barlow surface, sits at $b_+=1$ and needs the separate $b_+=1$ treatment with its wall-crossing subtlety); this is satisfied automatically once $p_g(X)\ge1$.

### (b) The pointwise bound $|\mathring r|^2\le4\delta^2$

**Correct.** With $E=\operatorname{Ric}+g$, eigenvalues $e_i=\rho_i+1\in[-\delta,\delta]$. One has $s=\operatorname{tr}\operatorname{Ric}=\operatorname{tr}E-4$ and

$$\mathring r=\operatorname{Ric}-\tfrac{s}{4}g=E-\tfrac{\operatorname{tr}E}{4}g=E_0,$$

the trace-free part of $E$. Therefore $|\mathring r|^2=|E|^2-\tfrac{(\operatorname{tr}E)^2}{4}\le|E|^2=\sum e_i^2\le4\delta^2$ (dimension $4$). The step is exactly as the note writes it. The value $4\delta^2$ is the sharp pointwise maximum (attained at $e=(\delta,\delta,-\delta,-\delta)$).

### (c) The volume upper bound

**Correct, with a positivity condition and $k<A$ that the note passes over.** From CGB on the $2\chi+3\tau$ side,

$$A-k=\frac1{4\pi^2}\int\Big(\tfrac{s^2}{24}+2|W_+|^2-\tfrac{|\mathring r|^2}{2}\Big),$$

and pointwise $s^2\ge16(1-\delta)^2$ (since $|s|\ge4(1-\delta)$), $|\mathring r|^2/2\le2\delta^2$, $2|W_+|^2\ge0$, giving integrand $\ge \tfrac{2}{3}(1-\delta)^2-2\delta^2$, hence

$$V\le\frac{4\pi^2(A-k)}{\tfrac23(1-\delta)^2-2\delta^2}.$$

Two things are silently required. First, the denominator must be positive, i.e. $\delta<\tfrac1{1+\sqrt3}\approx0.366$. Second, $A-k>0$, i.e. $k<A$. Neither is automatic, and $X\#k\overline{\mathbb{CP}}{}^2$ with $k\ge A$ is a real regime (repeated blow-ups). The conclusion nevertheless survives a clean two-case argument that the note should state explicitly:

- If the metric already has $\delta\ge\tfrac1{1+\sqrt3}$, then since the target floor satisfies $\delta_{\text{floor}}(p)=t/(1+t)$ with $t=\sqrt{(p-1/3)/2}<1/\sqrt3$ for $p<1$, one has $\delta\ge\delta_{\text{floor}}(p)$ trivially.
- If $\delta<\tfrac1{1+\sqrt3}$, the denominator is positive, the volume bound applies, and the derivation gives $\delta\ge\delta_{\text{floor}}(p)$.

So the result is valid for all $1/3<p<1$ once this case split is added. For $p\ge1$ the volume-bound route breaks down (CGB right side $\le0$), but in that regime $A-k\le0$ forces the $|\mathring r|^2$ term to dominate, so a positive floor $\delta\ge1/(1+\sqrt3)$ is even more forced; the closed formula $\sqrt{(p-1/3)/2}$ at $p=1$ lands exactly on this threshold, which is a good internal consistency signal but is not covered by the written derivation and should be handled by the separate remark.

### (d) Combination and what "tight" means

The final combination is exact. With $q'=k-A/3$, $B=A-k$, $q'+B=2A/3$:

$$q'\Big(\tfrac23(1-\delta)^2-2\delta^2\Big)\le2B\delta^2 \;\Longrightarrow\; q'(1-\delta)^2\le2A\delta^2 \;\Longrightarrow\; \frac{\delta^2}{(1-\delta)^2}\ge\frac{p-1/3}{2}.$$

This reproduces the stated inequality, and the symbolic "boundary is tight" in the script means only that the last implication is an equivalence for $\delta\in(0,1)$ — i.e. the algebra is exact. It does **not** establish that any metric attains $\delta=\delta_{\text{floor}}(p)$. The bound was built from three separate estimates (dropping $2|W_+|^2\ge0$; $|\mathring r|^2\le4\delta^2$; $s^2\ge16(1-\delta)^2$), and these cannot hold as pointwise/integral equalities together over the whole manifold with $W_+\equiv0$. Consequently the true infimum of $\delta$ over admissible metrics is plausibly strictly larger than $\delta_{\text{floor}}(p)$, and this matters for the research reading below: the $p\to1/3$ transition is analyzed with a bound that is not shown to be sharp there, so the actual pinching floor near $p=1/3$ could still be positive.

### (e) Extension of Einstein non-existence from $k>2A/3$ to $k>A/3$

**Correct, and it is the known optimal LeBrun statement, not a new result.** Setting $\mathring r=0$ (Einstein) in the $\int|\mathring r|^2/2\ge4\pi^2(k-A/3)$ line forces $k\le A/3$; equivalently, CGB with the full mixed left side $\ge(2/3)(a^+)^2\ge 2A/3$ gives $A-k\ge2A/3$. The scalar-only version keeps $2|W_+|^2$ on the CGB side but bounds only $\tfrac1{4\pi^2}\int s^2/24\ge A/3$, yielding $A-k\ge A/3$, i.e. $k\le2A/3$. The factor-two comes exactly from carrying $|W_+|^2$ into the a priori estimate rather than discarding it, and for a single factor there is no $-4$ correction (that term in Ishida–LeBrun Theorem 7 is the cost of the extra $X\#Y$ connected sum; here $2\chi+3\tau=A-k$ with no constant). This matches LeBrun's Invent. Math. 2001 bound $k>c_1^2(X)/3$. So step (e) is sound but the non-existence range is not itself new; the quantitative floor of (a)–(d) is the contribution.

### What the floor does and does not settle for Yau 26

The floor is a one-directional statement: **any** admissible metric on the fixed manifold has $\delta\ge\delta_{\text{floor}}(p)$. It is an obstruction working against constructing a $\sigma=-1$-branch counterexample, and it does correctly remove the "vary the manifold with $A\to\infty$ at fixed $p>1/3$" route, since $\delta_{\text{floor}}$ depends on $p$ only. Two substantive unknowns remain that the note should not let the "kills the route" language obscure:

1. **Existence is untouched.** The floor says nothing about whether $X\#k\overline{\mathbb{CP}}{}^2$ admits *any* metric with $\operatorname{Ric}$ pinched near $-g$. The base $X$ carries an Aubin–Yau Kähler–Einstein metric with $\operatorname{Ric}=-g$ ($\delta=0$), but the blow-up is a different smooth manifold and the existence of even one negatively-pinched metric on it is open. A counterexample needs a *construction*; the floor only bounds it from one side.

2. **The $p\to1/3$ transition is analyzed with an unsharp bound.** Because (d) is not shown to be geometrically attained, the possibility "$\delta\to0$ as $p\to1/3^+$" is not established — it is only *not excluded* by this particular estimate. A sharp pinching floor near $p=1/3$ (or an independent obstruction there) is exactly the piece of scientific substance that would decide whether the $\sigma=-1$ branch of the LeBrun family can approach Einstein-like pinching at all. This is the natural next quantitative target.

### Minor items, confirmed

- Topology correction $2\chi-3|\tau|=4-m$ for $\#_m\mathbb{CP}^2$ is right ($\chi=m+2$, $\tau=m$), so $m=3$ satisfies strict HT and $m\ge5$ violates it. The earlier "$2-m$" was wrong.
- Numerical table is internally consistent: $p=2/3\Rightarrow\delta\ge1/(1+\sqrt6)\approx0.290$; $p=0.4\Rightarrow0.154$; $p=0.5\Rightarrow0.224$; $p=0.9\Rightarrow0.347$ all match $t/(1+t)$ with $t=\sqrt{(p-1/3)/2}$.
- Proposition 4's strictness clause (needing $a$ not the canonical class of a symplectic structure) is irrelevant here, since only the non-strict $\ge(2/3)(a^+)^2$ is used.

### Net

Steps (a)–(e) are correct as mathematics. The two additions needed to make the written argument complete are: (i) grounding monopole-class existence on Taubes plus the blow-up formula (with $b_+(X)\ge2$), rather than on the Bauer–Furuta connected-sum mechanism, and (ii) the explicit two-case handling of the volume-bound denominator so the conclusion is valid across $1/3<p<1$ and, by a separate remark, for $p\ge1$. The one interpretive point to carry forward is that "tight" here is algebraic, not geometric, so the floor is a valid necessary bound but not a sharp one; the sharp floor near $p=1/3$ and the existence of any negatively-pinched metric on the blow-ups are the two open quantities on which the $\sigma=-1$-branch question actually turns.
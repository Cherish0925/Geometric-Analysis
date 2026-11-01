# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step22_inverse_square_correction_and_two_stage_architecture.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A03/workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md",
    "Sessions/S0910A03/workspace/notes/step21_corrections_from_ttcs_and_peers.md",
    "Sessions/S0910A03/workspace/scripts/verify_step22_inverse_square_and_subcritical.py"
  ]
}
```

## Task

Verify the following claims about the normalized cutoff flow in 4 dimensions:

1. INVERSE-SQUARE COUNTEREXAMPLE: The Hardy potential V = κ/|x|² on R⁴ with 0 < κ < 1 satisfies the form bound ∫Vφ² ≤ κ∫|∇φ|² (small form perturbation), but the heat semigroup e^{t(Δ+V)} does NOT have a uniform L²→L∞ bound. Verify that σ = 1-√(1-κ) > 0 gives the singular ground state r^{-σ} ∈ L² \ L∞.

2. SUBCRITICAL UPGRADE: In 4D, n/2 = 2 is the critical Sobolev exponent. A potential in L² gives only a form bound (critical, possibly non-ultracontractive). A potential in L³ gives form-relative bound zero (subcritical), allowing standard Moser iteration with convergent constants. Verify that the Wang hierarchy H₃(t) ≤ Cγ³/t provides exactly this subcritical upgrade at positive time.

3. SOBOLEV VARIABLE: For v = ηχF with a=χ², check that |∇v|² = η²a|∇F|² + |∇χ|²F² + a F²|∇η|² + cross terms, and that |∇a|²/a = 4|∇χ|² is bounded. Verify that this means the gradient of the Sobolev variable is controlled by the dissipation D₂ = ∫η²a|∇F|² plus lower-order terms.

4. CAUCHY-SCHWARZ FACTORING: H₃ = ∫η²aF³ ≤ H₂^{1/2} · (∫η²a²F⁴)^{1/2}. The second factor requires an OUTER cutoff. Verify that the finite-neighbor graph system handles this, and that the critical Sobolev product β = A₀²||F||₂ = C√ε_Li controls the absorption.

5. TRANSCRIPTION: The correct quadratic form is ε_t[φ] = ∫|∇(a^{-1/2}φ)|²dμ, NOT ∫|∇(a⁻¹φ)|²dμ. The former has leading weight a⁻¹ near the gradient, the latter a⁻². Verify that the a⁻¹/² version matches the conformal Sobolev substitution u = a^{-1/2}φ.

## Output

## Verification memo: five analytic statements for the normalized cutoff flow in 4D

I reproduced each computation independently. The essential content of all five is sound. Two places carry genuine transcription slips inside the correction notes themselves, and one place needs an explicit convention statement to prevent conflating two distinct $a$-weight scales. I give the arithmetic and the two corrections below, then state what remains open in the surrounding program.

---

### Item 1 — Inverse-square counterexample. Confirmed.

Radial static solutions $u=r^{-\alpha}$ of $-\Delta u-\kappa r^{-2}u=0$ on $\mathbb R^n$: using $\Delta u=\alpha(\alpha+2-n)r^{-\alpha-2}$ gives $\alpha^2-(n-2)\alpha+\kappa=0$, matching the script's characteristic equation. For $n=4$, $\alpha=1\pm\sqrt{1-\kappa}$, so $\sigma=\alpha_-=1-\sqrt{1-\kappa}$. For $0<\kappa<1$ this is in $(0,1)$, hence positive; $\sigma(1/2)=0.2929$, $\sigma(9/10)=0.6838$, and $\sigma\approx\kappa/2$ for small $\kappa$ — all as printed.

Integrability near $0$ in $\mathbb R^4$: $\int_0 r^{-2\sigma}r^3\,dr$ converges iff $\sigma<2$, so $r^{-\sigma}\in L^2_{\rm loc}$; and $r^{-\sigma}\to\infty$ since $\sigma>0$, so $r^{-\sigma}\notin L^\infty$. Correct.

Form bound: the sharp Hardy constant in $\mathbb R^4$ is $(n-2)^2/4=1$, so $\int\kappa|x|^{-2}\phi^2\le\kappa\int|\nabla\phi|^2$ for $\kappa<1$. This is exactly relation (1) with $\gamma=\kappa$. Correct.

The decisive step — form-smallness does **not** give $L^2\to L^\infty$ — is right. The Milman–Semenov/Moschini–Tesei heat-kernel estimate for $-\Delta-\kappa|x|^{-2}$ has on-diagonal behavior $p_t(x,x)\asymp t^{-2}(1\wedge\sqrt t/|x|)^{2\sigma}$ with the same $\sigma=1-\sqrt{1-\kappa}$. As $x\to0$ this diverges, so $\|e^{-tH}\|_{L^1\to L^\infty}=\infty$; by self-adjointness $\|e^{-tH}\|_{2\to\infty}=\|e^{-tH}\|_{1\to2}$ and $\|e^{-tH}\|_{1\to\infty}\le\|e^{-tH/2}\|_{2\to\infty}^2$, so $L^2\to L^\infty$ unboundedness follows. The note's assertion $\|e^{-tH}f\|_\infty=\infty$ holds for $f\ge0$ nonzero near $0$ (the projection coefficient is then positive); for sign-changing $f$ it holds generically. The striking point is correct and worth keeping: **arbitrarily small $\kappa$ still gives $\sigma>0$**, so no amount of form-smallness rescues ultracontractivity.

One wording point: $r^{-\sigma}$ is the less-singular homogeneous static solution governing the near-origin kernel, not an $L^2$ eigenfunction (the operator on $\mathbb R^4$ has purely continuous spectrum). The script's docstring word "ground-state" is imprecise; the object and its role are correct.

Logical use is right: the counterexample refutes the general implication "small form bound $\Rightarrow$ ultracontractivity," which is what the Step 21 abstract Nash lemma asserted. It does not by itself say the cutoff-flow setting must fail; it says the shortcut is unavailable and the $H_2\to H_3$ work is unavoidable. The note states exactly this.

---

### Item 2 — Subcritical upgrade. Correct as a conditional statement.

In 4D the critical exponent for a potential in the Schrödinger/Moser theory is $n/2=2$. The standard dichotomy (Serrin/Aronson–Serrin; Kato-class): $V\in L^p_{\rm loc}$ with $p>n/2$ gives form-relative bound zero and local $L^2\to L^\infty$ boundedness with convergent constants; $p=n/2$ is the borderline where this can fail, the Hardy potential being the model. I verified the form-relative-bound-zero mechanism: $\int V\phi^2\le\|V\|_p\|\phi\|_{2p'}^2$, and $2p'<2^*=4$ exactly when $p>2$, so $\|\phi\|_{2p'}$ interpolates between $L^2$ and $L^4$ with an $\varepsilon$-small $L^4$ weight. At $p=2$, $2p'=2^*$ and the room disappears. This is the precise sense in which $L^3$ is subcritical and $L^2$ is critical in 4D.

The Wang bound $H_3(t)\le C\gamma^3/t$ gives $\|\mathcal K\|_{L^3(\nu)}\lesssim\gamma\,t^{-1/3}$ at positive time, i.e. the potential is $L^3(\nu)$, hence subcritical since $3>2$. So the upgrade is exactly what is stated — **as a conditional statement**. Two dependencies must stay visible:

- The $H_3(t)\le C\gamma^3/t$ input is the output of Stage 1 (the $H_2\to H_3$ energy inequality (2.1)–(2.3)/(11.1)), which the notes themselves mark as the genuine unproven core (T1, T2, U1). The counterexample of Item 1 is precisely why this cannot be sidestepped. So Item 2's value is that it correctly localizes the whole difficulty into Stage 1.
- The subcritical closure runs the iteration in a space where a uniform 4D Sobolev/Nash inequality holds. That is exactly the degenerate cusped conformal geometry near $\{a=0\}$ where the Hardy phenomenon lives. Form-relative-bound-zero for $L^3$ potentials is standard **given** the uniform Sobolev inequality (this is condition (F2)); the uniformity of that inequality across the cusped region and the finite-neighbor assembly (Item 4) are program items, not settled facts.

---

### Item 3 — Sobolev variable gradient. Confirmed.

With $v=\eta\chi F$ and $a=\chi^2$:
$$
\nabla v=(\nabla\eta)\chi F+\eta(\nabla\chi)F+\eta\chi\nabla F,
$$
$$
|\nabla v|^2=\underbrace{\eta^2\chi^2|\nabla F|^2}_{\eta^2 a|\nabla F|^2}+\eta^2|\nabla\chi|^2F^2+\chi^2|\nabla\eta|^2F^2+\text{cross},
$$
i.e. $\eta^2 a|\nabla F|^2+\eta^2|\nabla\chi|^2F^2+a|\nabla\eta|^2F^2+\text{cross}$, matching the task expression. (One small item: the middle term carries $\eta^2$; the task line dropped it. Since $\eta\le1$ this only strengthens the stated inequality, so it does not affect the conclusion, but the clean identity has $\eta^2|\nabla\chi|^2F^2$.)

The regular identity is exact: $\nabla a=2\chi\nabla\chi$, so $|\nabla a|^2=4\chi^2|\nabla\chi|^2=4a|\nabla\chi|^2$, hence $|\nabla a|^2/a=4|\nabla\chi|^2\le C/r^2$, bounded — no $1/a$ blow-up. The dominant cross term $2\eta^2\chi F\langle\nabla\chi,\nabla F\rangle$ is Young-absorbed into $\varepsilon\,\eta^2 a|\nabla F|^2+\varepsilon^{-1}\eta^2|\nabla\chi|^2F^2$, i.e. into the dissipation $D_2=\int\eta^2 a|\nabla F|^2$ plus the bounded-weight $F^2$ terms. So $|\nabla v|^2$ is controlled by $D_2$ plus $r^{-2}$-weighted $F^2$ mass. Correct.

Also consistent with the degenerate structure: even though the energy $H_2=\int F^2\,d\mu$ carries weight $a^0$, its time derivative under $\partial_t g=-2aE$ (with $\partial_t\mathrm{Rm}=a\Delta\mathrm{Rm}+\cdots$) produces dissipation $\int a|\nabla F|^2$ at weight $a^1$, because the Laplacian carries the $a$ factor. The weight bookkeeping in Item 3 and this energy identity fit together.

---

### Item 4 — Cauchy–Schwarz factoring. Correct under one convention that must be stated explicitly.

The factoring $H_3\le H_2^{1/2}\,\big(\int\eta^2 a^2F^4\big)^{1/2}$ is correct **only** with the convention
$$
H_q=\int\eta^2\,\mathcal K^q\,d\nu=\int\eta^2\,a^{\,q-2}F^q\,d\mu,\qquad \mathcal K=aF,\ d\nu=a^{-2}d\mu,
$$
under which $H_2=\int\eta^2F^2$ (weight $a^0$), $H_3=\int\eta^2 aF^3$ (weight $a^1$), $H_4=\int\eta^2a^2F^4$ (weight $a^2$). Then the factoring is just Cauchy–Schwarz in $L^2(\nu)$: the geometric mean of the $H_2$ and $H_4$ densities is $\sqrt{\eta^4a^2F^6}=\eta^2aF^3=$ the $H_3$ density. Confirmed exactly.

This must be flagged because a second, distinct $a$-weight scale is present: the Sobolev variable $v_2=\eta a^{1/2}F$ has $\|v_2\|_2^2=\int\eta^2 aF^2$ (weight $a^1$), which is **not** $H_2=\int\eta^2F^2$ (weight $a^0$). The two differ by a factor of $a$. Because $0\le a\le1$, $\int\eta^2 aF^2\le\int\eta^2F^2$, so replacing $\|v_2\|_2^2$ by $H_2$ in "$H_3\le C\gamma(\|\nabla v_2\|^2+r^{-2}H_2)$" is direction-consistent (it enlarges the bound). But near $a=0$ this is exactly where a $a^1\leftrightarrow a^0$ substitution is delicate, so any writeup should state the convention $H_q=\int a^{q-2}F^q$ once and keep $\|v_2\|_2^2$ separate. Conflating them silently is the kind of slip that has already happened once in this program (Item 5 below).

The absorption chain is correct: Sobolev gives $\|v_2\|_4^2=\big(\int\eta^4a^2F^4\big)^{1/2}\le A_0^2(\|\nabla v_2\|_2^2+r^{-2}\|v_2\|_2^2)$, and $H_3\le H_2^{1/2}\|v_2\|_4^2\le\beta\,D_2+\beta r^{-2}H_2$ with $\beta=A_0^2\|F\|_2=A_0^2 H_2^{1/2}=C\sqrt{\varepsilon_{\rm Li}}$; for $\beta\ll1$ the $\beta D_2$ term is absorbed by the dissipation. The volume-independence of $\beta$ (product of a large $A_0^2$ on a collapsed ball with a small $\|\mathrm{Rm}\|_{L^2}$) is the load-bearing point and is internally consistent with §9.4.

What is **not** completed here: the "outer cutoff" needed for the $H_4$ factor. Sobolev applied to $v_2$ produces $|\nabla\eta|^2$ terms supported on a slightly larger set than $\eta_k$, so the reaction on level $k$ is bounded by dissipation/energy on the enlarged support — the finite-neighbor graph system $S_\alpha'\le Cr^{-2}\sum_{\beta\sim\alpha}(A_\alpha/A_\beta)^4 S_\beta$. The notes assert this structure (T1, U1) but do not close it. So "the finite-neighbor graph system handles this" is a program statement, not a finished derivation. The algebra of the single factoring step is correct; the assembly across nested supports and infinitely many exponents is the substantive remaining work.

---

### Item 5 — Transcription $a^{-1/2}$ vs $a^{-1}$. Headline correct; the inline expansion in the correction note carries its own slip.

The substitution is forced by the $L^4$ matching: requiring $\int u^4 d\mu=\int\phi^4 d\nu$ with $d\nu=a^{-2}d\mu$ gives $u^4=a^{-2}\phi^4$, hence $u=a^{-1/2}\phi$. This is dimension-4 specific: $2^*=2n/(n-2)=4$ and $a^{-2}=(a^{-1/2})^{4}$. So $a^{-1/2}$ is the correct exponent and the conformal Sobolev substitution matches. The comparison "$a^{-1}$ gives two powers of $a^{-1}$ in the leading gradient term" is right at the level of the leading term:
$$
|\nabla(a^{-1/2}\phi)|^2\text{ has leading }a^{-1}|\nabla\phi|^2,\qquad
|\nabla(a^{-1}\phi)|^2\text{ has leading }a^{-2}|\nabla\phi|^2 .
$$
So the headline correction (use $a^{-1/2}$) is sound and important.

However, the **potential (pure $\phi^2$) term** in the correct form is more singular than the note states. Writing $w=a^{-1/2}\phi=\chi^{-1}\phi$:
$$
|\nabla w|^2=\underbrace{a^{-2}|\nabla\chi|^2\phi^2}_{\text{weight }a^{-2}}-2a^{-3/2}\phi\langle\nabla\chi,\nabla\phi\rangle+\underbrace{a^{-1}|\nabla\phi|^2}_{\text{weight }a^{-1}} .
$$
The exact potential coefficient is $\tfrac14 a^{-3}|\nabla a|^2=a^{-2}|\nabla\chi|^2$, i.e. **weight $a^{-2}$**. The note wrote this term as "$O(a^{-2}|da|^2\phi^2)$"; with $|da|^2=4a|\nabla\chi|^2$ that literal expression equals $4a^{-1}|\nabla\chi|^2\phi^2$, weight $a^{-1}$ — off by one power of $a$. Notice the note's $s=1$ line "$a^{-4}|da|^2\phi^2$" is the raw ($a^{-3}$-family) form, so the two lines are written in inconsistent conventions and the $s=1/2$ line specifically understates the exponent. The correct raw coefficient is $a^{-3}|da|^2$, equivalently $a^{-2}|\nabla\chi|^2$.

This is not merely bookkeeping. That $a^{-2}|\nabla\chi|^2\phi^2=\chi^{-4}|\nabla\chi|^2\phi^2$ term is exactly the inverse-square (Hardy) potential in the conformal coordinate — the same structure the counterexample of Item 1 is about. It sits inside $\mathfrak e_t[\phi]$ as part of the free conformal energy (so the Sobolev inequality $\|\phi\|_{L^4(\nu)}^2\le A_0^2\mathfrak e_t[\phi]$ still holds, being a literal rewriting of the original inequality). The phrase "the correct form (2) does not have a hidden singularity in the cross terms" is defensible only for the linear cross term (which Young-absorbs into the $a^{-1}$ gradient plus the $a^{-2}$ potential and introduces nothing worse). It should not be read as saying the form is benign near $a=0$: the genuine $a^{-2}$ conformal-Hardy potential is present, and it is exactly why the curvature potential's critical/subcritical status — not the form's smallness — decides ultracontractivity. Making this explicit removes an internal tension between §2 ("no hidden singularity") and §1/§3 (the Hardy obstruction).

---

### Net assessment and what remains open

The five items are mutually consistent and their essential mathematics is correct. Two concrete fixes: (i) state the moment convention $H_q=\int a^{q-2}F^q$ explicitly wherever the $H_2^{1/2}H_4^{1/2}$ factoring or the Sobolev variable $v_2$ appears, and keep $\|v_2\|_2^2=\int aF^2$ distinct from $H_2=\int F^2$; (ii) correct the $s=1/2$ inline expansion so the potential term reads $a^{-2}|\nabla\chi|^2\phi^2$ (weight $a^{-2}$), and rephrase "no hidden singularity" to acknowledge that this term is the conformal Hardy potential rather than an artifact.

The structural conclusion these items support is the useful one: the abstract-Nash shortcut is genuinely unavailable (Item 1), so the entire difficulty is the single critical step producing $H_3(t)\le C\gamma^3/t$ (Items 2, 4), after which the subcritical $L^3$ iteration is standard given a uniform 4D Sobolev inequality on the cusped domain. What is not yet derived, and remains the load-bearing work, is: the exact localized energy inequality (2.1)/(11.1) for the degenerate normalized flow with the evolving measure and $\nabla^2 a$ terms integrated by parts; the finite-neighbor outer-cutoff assembly behind the $H_4$ factor (T1/U1); the time integration to $H_3(t)\le C\gamma^3/t$; and the uniformity of the Sobolev/Nash inequality across $\{a\to0\}$ that the subcritical closure consumes. The counterexample sharpens why these cannot be replaced by a form-smallness argument, but it does not supply them.
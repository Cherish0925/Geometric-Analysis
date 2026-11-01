# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step28_bochner_center_bound_and_abelian_forcing.md",
    "Sessions/S0910A02/workspace/data/step28_bochner_killing_center_bound.json",
    "Sessions/S0910A02/workspace/data/step28_almost_killing_correction.json",
    "Sessions/S0910A02/workspace/notes/step27_preceptor_h3_positive_monotonicity_review.md",
    "Sessions/S0910A02/workspace/notes/step26_nilpotent_abelian_forcing_audit.md"
  ]
}
```

## Task

Verify the Bochner center bound theorem package for the positive-collapse route of Yau Problem 26. The key claims to check:

1. THEOREM A (Bochner center bound): For Z Killing on closed (M,g) with Ric ≤ (Λ+δ)g, the standard Bochner identity ∫|∇Z|² = ∫Ric(Z,Z) combined with the fiber gradient lower bound |∇Z|² ≥ (b²/2)|Z|² (for Heisenberg center bracket b) gives ⟨b²⟩ ≤ 2(Λ+δ). Check that the fiber gradient lower bound is correct for a general submersion with possibly nonzero T and A tensors (not just the totally geodesic case). The claim is that T and A terms add non-negatively to |∇Z|².

2. THEOREM B: For Λ+δ < 0 on a closed manifold, the Bochner identity implies Z=0. Check sign conventions.

3. ALMOST-KILLING CORRECTION: The exact Weitzenböck formula gives ∫|∇Z|² = ∫Ric(Z,Z) + (1/2)∫|σ|² - (1/4)∫(tr σ)² where σ = L_Z g. Check that the 2-form norm convention (|dω|² = 2|A|² vs 4|A|²) is consistent with the derivation. Also check the collapse-scale analysis: for fiber scale ε, average |Z|² ~ ε², and τ = ||L_Z g||, the correction is τ²Vol/∫|Z|². When does this give abelian forcing?

4. INDUCTION ARCHITECTURE: Bound center bracket, quotient by central circle, apply Kaluza-Klein relation to get two-sided Ricci control on quotient, repeat. Check whether the constant degradation is O(2^k Λ) and whether the central quotient preserves the manifold structure needed for the next Bochner step.

5. The H3 model verification: |∇Z|² = c²(2k₃² + b²/2) where Z=c·e₃, verified by explicit Koszul formula. The Bochner identity integrand c²(3k₃² + 2k₁k₃ + k₃') vanishes after IBP. Check this.

Be precise about sign/convention issues, especially in the Weitzenböck formula. Flag any gaps in the induction architecture.

## Output

## Verifier memo — Bochner center bound package (Step 28)

I checked each mathematical object against the stated derivations, the JSON data, and independent recomputation. The core inequalities (Theorems A, B) and the exact Weitzenböck correction are correct. The induction architecture contains one decisive unresolved point at the quotient step, and a second at the global-symmetry hypothesis. Details below, item by item.

### 1. Theorem A and the fiber gradient lower bound — correct, with one sign typo in the stated operator equation

The conclusion $\int_M|\nabla Z|^2 = \int_M\operatorname{Ric}(Z,Z)\le(\Lambda+\delta)\int_M|Z|^2$ is right. But the proof line "the Bochner formula gives $\nabla^*\nabla Z + \operatorname{Ric}(Z)=0$" is wrong as an equation. For a Killing field the correct identity is
$$\nabla^*\nabla Z = \operatorname{Ric}(Z)\qquad(\text{equivalently }\Delta Z=-\operatorname{Ric}(Z),\ \Delta=\operatorname{tr}\nabla^2).$$
The written form $\nabla^*\nabla Z+\operatorname{Ric}(Z)=0$ asserts $\Delta_H Z^\flat=0$, i.e. that $Z^\flat$ is harmonic, which is false for a general Killing field (Killing fields are co-closed but not closed). The final integrated identity is unaffected because the integral of $\tfrac12\Delta|Z|^2$ vanishes on a closed manifold; still, the governing equation as printed should be corrected, since Section 6 later re-derives everything correctly via Hodge and the two versions must not disagree in the same document.

The load-bearing geometric claim — $|\nabla Z|^2\ge|\nabla^F Z|^2=(b^2/2)|Z|^2$ for a general submersion with nonzero $T,A$ — is correct. I verified the mechanism explicitly. Split an ambient orthonormal frame into vertical $\{U_i\}$ and horizontal $\{X_a\}$. For vertical $U_i$, O'Neill gives $\nabla_{U_i}Z = \nabla^F_{U_i}Z + T(U_i,Z)$ with the first term vertical, the second horizontal, hence orthogonal:
$$|\nabla_{U_i}Z|^2 = |\nabla^F_{U_i}Z|^2 + |T(U_i,Z)|^2 \ge |\nabla^F_{U_i}Z|^2.$$
For horizontal $X_a$, $\nabla_{X_a}Z$ has horizontal part $A_{X_a}Z$, so $|\nabla_{X_a}Z|^2\ge|A_{X_a}Z|^2\ge0$. Summing, $|\nabla Z|^2\ge\sum_i|\nabla^F_{U_i}Z|^2 = |\nabla^F Z|^2$. So both $T$ and $A$ enter with non-negative sign and the bound needs no control of either. The value $|\nabla^F Z|^2=(b^2/2)|Z|^2$ I recomputed from Koszul on $H_3$ with $[E_1,E_2]=bE_3$: $\nabla^F_{E_1}E_3=-\tfrac b2 E_2$, $\nabla^F_{E_2}E_3=+\tfrac b2 E_1$, $\nabla^F_{E_3}E_3=0$, giving $|\nabla^F E_3|^2=b^2/2$. Correct. The twist-immunity conclusion holds.

One point to state plainly for use: $b$ is *defined* by $b^2:=2|\nabla^F Z|^2/|Z|^2$ through a fiber structure. Corollary A1 therefore needs a genuine free isometric nilpotent action with Heisenberg-type fibers; the bound is meaningless for a Killing field without such structure.

### 2. Theorem B ($\Lambda+\delta<0$) — correct

$\int|\nabla Z|^2=\int\operatorname{Ric}(Z,Z)\le(\Lambda+\delta)\int|Z|^2\le0$ forces $\int|\nabla Z|^2=0$ and, since the coefficient is nonzero, $\int|Z|^2=0$, so $Z\equiv0$. This is classical Bochner and the sign flow is right. The CH² consistency check is also right: $|\nabla Z|^2/|Z|^2=2k_3^2+b^2/2=5/2$, $\operatorname{Ric}_{33}=b^2/2-Hk_3=1/2-(-2)(-1)=-3/2$, residual $5/2-(-3/2)=4>0$; a strictly positive pointwise integrand cannot integrate to zero on a closed manifold, consistent with CH² being non-compact. This is a calibration, not an ingredient of any theorem, and is labelled as such.

### 3. Almost-Killing Weitzenböck correction — derivation and convention consistent

I re-derived the formula and it is internally consistent with the 2-form convention used. With $\nabla Z=A+S$, $A$ skew, $S=\sigma/2$, $\sigma=\mathcal L_Z g$:
- $|\nabla Z|^2=|A|^2+|\sigma|^2/4$ (Frobenius $|A|^2=\sum_{ij}A_{ij}^2$);
- $(d\omega)_{ij}=2A_{ij}$, and with $|d\omega|^2=\sum_{i<j}(d\omega)_{ij}^2$ this gives $|d\omega|^2=2|A|^2$ — matching the note;
- $\delta\omega=-\tfrac12\operatorname{tr}\sigma$, $|\delta\omega|^2=\tfrac14(\operatorname{tr}\sigma)^2$.

Integrated Weitzenböck $\int(|d\omega|^2+|\delta\omega|^2)=\int(|\nabla Z|^2+\operatorname{Ric}(Z,Z))$ yields $\int|A|^2=\int(\operatorname{Ric}(Z,Z)+\tfrac14|\sigma|^2-\tfrac14(\operatorname{tr}\sigma)^2)$, and adding $\tfrac14\int|\sigma|^2$ gives exactly
$$\int|\nabla Z|^2=\int\operatorname{Ric}(Z,Z)+\tfrac12\int|\sigma|^2-\tfrac14\int(\operatorname{tr}\sigma)^2.$$
The 2-form convention $|d\omega|^2=2|A|^2$ (not $4|A|^2$) is the one that makes this close; the note is consistent throughout. Dropping the non-positive $-\tfrac14\int(\operatorname{tr}\sigma)^2$ for the upper estimate is the correct direction. Good.

Collapse-scale arithmetic: from $\int(b^2/2)|Z|^2\le\int|\nabla Z|^2\le(\Lambda+\delta)\int|Z|^2+\tfrac12\int|\sigma|^2$ and $|\sigma|\le\tau$,
$$\langle b^2\rangle_{|Z|^2}\le 2(\Lambda+\delta)+\frac{\tau^2\operatorname{Vol}(M)}{\int|Z|^2}.$$
With $\int|Z|^2\sim\varepsilon^2\operatorname{Vol}$, the correction is $\sim\tau^2/\varepsilon^2$. This is right.

One substantive refinement of the threshold: the note requires $\tau=o(|Z|)$ (its "regime 2") for the abelian conclusion, but that is stronger than the qualitative statement needs. For the normalized bracket $\tilde b^2=\varepsilon^2 b^2$ to vanish it suffices that the ambient $\langle b^2\rangle$ stay $O(1)$, i.e. the correction stay $O(1)$, i.e. $\tau=O(|Z|)\sim\varepsilon$ ("regime 1"). Regime 1 already gives $\tilde b^2\le\varepsilon^2\cdot O(1)\to0$. Regime 2 is only needed for the sharper $\langle b^2\rangle\to2\Lambda$. Stating the weaker threshold enlarges the set of local structures the bridge is allowed to have, which matters for whether the bridge can be built at all.

### 4. Averaged versus pointwise — the abelian conclusion is $L^2$-weighted only

The bound is a $|Z|^2$-weighted average, $\langle b^2\rangle_{|Z|^2}\le 2(\Lambda+\delta)$. It permits $b^2$ to be large on sets of small measure or small $|Z|^2$. The Step-27 model shows precisely this: large bracket concentrates in a *thin high-curvature shell* of thickness $\le 2/(\sqrt5 B)$ with $|\operatorname{Rm}|\ge 3b^2/4$. Such a shell is fully compatible with a bounded $|Z|^2$-average. So "asymptotically abelian" here is an integral statement, not a uniform one; the integral Bochner bound does not by itself exclude localized nonabelian shells. This is not an error — the hierarchy table correctly places pointwise structure at Level 2 — but the prose "the collapse is asymptotically abelian" should be read in the averaged sense, and any later use that needs uniform near-flatness of the fiber must draw on the pointwise model input, not on Theorem A.

### 5. Induction architecture — one decisive unresolved point at the quotient

Step 1 (center Killing field $Z_k$, Bochner bound) is sound. The problem is Step 2. To iterate Bochner on the quotient $B$ one needs an *upper* two-sided Ricci bound on $B$. The Kaluza–Klein/O'Neill relation for the central circle reads
$$\operatorname{Ric}_B = \operatorname{Ric}_M^{H} + \tfrac12\,\phi\circ\phi,\qquad \phi\circ\phi\ge0,$$
so the base Ricci is the total-space horizontal Ricci *plus* a non-negative twist term. An upper Ricci bound on $M$ therefore descends to an upper bound on $B$ only if $|\phi|^2$ is bounded above. The note supplies this via "$|\phi_k|^2=2\Lambda$ from Step-24 type equations" — but that identity is an *exact* Einstein constraint. Under the pinching hypothesis (the left-hand class this package is about), the metric is not Einstein, and $|\phi|^2$ is not pinned. Crucially, the Bochner center bound controls the *vertical fiber bracket* $b$ (the nilpotency of the fiber), whereas $\phi=A$ is the *horizontal connection curvature* of the bundle $M\to B$ — a different O'Neill tensor. Theorem A gives no bound on $|\phi|$. Hence the upper Ricci control does not descend to $B$, and the "$O(2^k\Lambda)$ constant degradation" is valid only along the exact-Einstein descent, not for the pinched class. This is the point that currently prevents the induction from running on the objects it is meant to run on. Resolving it needs an independent bound on the horizontal twist $|\phi|=|A|$ under two-sided Ricci pinching — a genuinely separate ingredient.

A second unresolved point, already flagged in the note but worth stating with its full weight: Step 2 also needs the central quotient to be a manifold carrying a global central Killing field at the next level. This holds for a smooth free isometric action, but generic pinched metrics carry *no* continuous isometry at all; the collapse geometry of Cheeger–Fukaya–Gromov / Kapovitch–Wilking produces only *local, approximate* N-structures. So Theorem A in its exact-Killing form applies directly only to the thin sub-class of pinched metrics that happen to have global symmetry. Everything general rests on the almost-Killing bridge of Section 6, whose input — that tight positive pinching forces the local nilpotent generators to satisfy $\|\mathcal L_Z g\|=O(|Z|)$ at collapse scale — is not established here. The lower Ricci bound (via Kapovitch–Wilking/Naber–Zhang) supplies the nilpotent structure; the quantitative Lie-derivative control that must come from the *upper* bound is the open link. The note identifies this correctly as the load-bearing question.

### 6. H₃ model verification — fully reproduced

Independent recomputation:
- $Z=ce_3$, $|Z|^2=c^2$. With $\nabla_{e_0}Z=c'e_3=ck_3e_3$, $\nabla_{e_1}Z=-\tfrac{c^2}{2a^2}e_2=-\tfrac{cb}{2}e_2$, $\nabla_{e_2}Z=+\tfrac{cb}{2}e_1$, $\nabla_{e_3}Z=-ck_3e_0$, I get $|\nabla Z|^2=c^2(2k_3^2+b^2/2)$. Matches.
- Integrand $|\nabla Z|^2-\operatorname{Ric}(Z,Z)=c^2[2k_3^2+b^2/2-(b^2/2-k_3'-(2k_1+k_3)k_3)]=c^2(3k_3^2+2k_1k_3+k_3')$. Matches.
- IBP with total weight $c^2 w=a^2c^3$, $\tfrac{d}{dt}\log(a^2c^3)=2k_1+3k_3$: $\int k_3' a^2c^3\,dt=-\int k_3(2k_1+3k_3)a^2c^3\,dt$, so the integrand integrates to $\int(3k_3^2+2k_1k_3-2k_1k_3-3k_3^2)a^2c^3\,dt=0$. Matches, and the volume weight $a^2c$ times the explicit $c^2$ factor is the correct measure. The alternative divergence form $\operatorname{Ric}_{33}=b^2/2-(wk_3)'/w$ with $w=a^2c$ also checks: $(wk_3)'/w=k_3'+k_3(2k_1+k_3)$, giving $\langle b^2\rangle_w=2\Lambda$ for exact Einstein — a distinct, $w$-weighted statement, correctly labelled as consistent-but-different from the $|Z|^2$-weighted Bochner bound.

### Bottom line for use

The four elementary results are solid and reusable: the Killing Bochner bound (Theorem A), the vanishing at $\Lambda+\delta<0$ (Theorem B), the exact almost-Killing Weitzenböck formula, and the H₃ model verification. They correctly establish that any *genuinely isometric* nilpotent collapse under upper Ricci control has $|Z|^2$-averaged bracket $\le 2(\Lambda+\delta)$, with twist entering only favorably.

What the package does not yet deliver toward the containment question, and what would make the positive-collapse route land:
- an upper bound on the horizontal twist $|\phi|=|A|$ under two-sided Ricci pinching, without which the quotient Ricci is not two-sided-controlled and the induction cannot descend for non-Einstein pinched metrics;
- the almost-Killing bridge: a quantitative $\|\mathcal L_Z g\|=O(|Z|)$ (the weaker threshold suffices) for the local N-structure generators forced by tight positive pinching, converting the exact-Killing statement into one about actual collapse geometry;
- pointwise (not merely $L^2$-averaged) bracket control if a uniform near-abelian fiber statement is wanted, since the integral bound is compatible with the thin nonabelian shells the Step-27 model exhibits.

The document's own framing — a structural result about the pinched left-hand class, proving no branch of the containment statement and formalizing only the algebraic kernels — matches what the mathematics supports.
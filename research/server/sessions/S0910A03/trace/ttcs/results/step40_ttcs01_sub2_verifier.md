# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently verify the proposed m=2 coupled continuation mechanism in step40_m2_coupled_continuation_mechanism.md for the normalized cutoff flow. Focus on the exact hard residual: V=∇²U, Z=∇³χ, W=∇U, Θ=∇²χ, and I=∫χ Z*W*|V|^{p-2}V. Check whether integrating once more off Z really yields only (i) a signed χΘ*V*P(V) term amenable to the Step 38 Hessian lemma, (ii) a weighted-dissipation term with coefficient ΘW controlled from the m=1 base pair at finite exponents, and (iii) lower products—without hidden current-level Z at 2p or W in L∞. Check tensor/covariant-derivative commutators and whether the Γ1, Γ2, Γ3 coefficients/contractions can be grouped this way rather than merely schematically. Also verify the Z evolution derivative count and same-p closure. Identify precisely any remaining term that invalidates the displayed m=2 Grönwall inequality. Treat the note as a mathematical proposal, not as established.

## Output

## Verification memo — the m=2 coupled continuation mechanism

**Summary judgment.** Treating `step40` as a proposal, the central residual mechanism is arithmetically sound. The second integration by parts on $I_{ZW}=\int\chi\,Z*W*P(V)$ genuinely eliminates the current cutoff jet $Z=\nabla^3\chi$ and replaces it by $\Theta=\nabla^2\chi$; the three resulting pieces are exactly (i) a signed $\chi\Theta*V*P(V)$ Hessian term, (ii) a weighted-diffusion term with coefficient $\Theta W$, and (iii) products in base-pair norms — with no hidden $\|Z\|_{2p}$ and no $\|W\|_\infty$. The $Z$-evolution derivative count is correct and closes at the same exponent $p$. No term inside the stated hypotheses invalidates the displayed Grönwall inequality (4.3)+(5.4). The mechanism is a valid **conditional** m=2 lemma. Its load-bearing external input is the unweighted first-derivative estimate (1.1) $\nabla T\in L^q$, which is not written in this note; and one attribution in (3.9) is incomplete. Details follow.

---

### 1. The residual integration $I_{ZW}$ (§3) is correct

Write $Z=\nabla\Theta$. Moving the single covariant derivative $\nabla_k$ off $Z$ inside $\int\chi(\nabla_k\Theta)*W*P(V)$ gives, with the divergence integral vanishing on the closed manifold,
$$
I_{ZW}=-\int d\chi*\Theta*W*P(V)-\int\chi\,\Theta*(\nabla W)*P(V)-\int\chi\,\Theta*W*\nabla P(V),
$$
exactly (3.2). Three points I checked:

- **No commutator enters.** The identity $\int(\nabla_k A)B^k=-\int A\,\nabla_k B^k$ on a closed manifold introduces no curvature; commutators would appear only from reordering covariant derivatives, which is not done here. The derivative $\nabla_k$ lands on $\chi$, $W$, or $P(V)$ only.

- **$\nabla W=V$ is exact.** $\nabla_kW_i=\nabla_k\nabla_iU=V_{ki}$ is literally the second covariant derivative defining $V$; there is no lower-order remainder. Hence the middle term is $\int\chi\,\Theta*V*P(V)$, size $\chi|\Theta||V|^p$.

- **Middle term is a genuine signed Hessian.** With $\Theta_{ij}=\nabla_i\nabla_j\chi$ (symmetric) and $B^{ij}(V)=(V*P(V))^{ij}$, one has $|B|\le|V|\cdot|V|^{p-1}=|V|^p$ and $|\nabla B|\le|\nabla V||V|^{p-1}+|V|\,(p-1)|V|^{p-2}|\nabla V|=C_p|V|^{p-1}|\nabla V|$. These match Step 38 (1.2) precisely, so the Step 38 lemma yields $\le\varepsilon D_{2,p}+C_{p,\varepsilon}r^{-2}\|V\|_p^p$. I re-derived the Step 38 lemma itself (its (1.3)–(1.4) IBP and Young step $|\chi||d\chi||V|^{p-1}|\nabla V|=(\chi|\nabla V||V|^{(p-2)/2})(|d\chi||V|^{p/2})$); it is valid for any tensor $B$ with those two pointwise bounds.

- **First and third pieces, exponents verified.**
  First: $\int|d\chi||\Theta||W||V|^{p-1}$, Hölder $\tfrac1{2p}+\tfrac1{2p}+\tfrac{p-1}{p}=1$ gives $Cr^{-1}\|\Theta\|_{2p}\|W\|_{2p}\|V\|_p^{p-1}$, matching (3.5). Third: $|\nabla P(V)|\le C_p|V|^{p-2}|\nabla V|$, Young against $D_{2,p}$ leaves $\int|\Theta|^2|W|^2|V|^{p-2}$; the four-factor Hölder $\tfrac1{2p}+\tfrac1{2p}+\tfrac{p-2}{p}+\tfrac1p=1$ (the last exponent being the "unused finite-volume factor" $\|1\|_p=\mathrm{Vol}^{1/p}$) gives $C(M,g)\|\Theta\|_{4p}^2\|W\|_{4p}^2\|V\|_p^{p-2}$, matching (3.7).

All of these use $W,\Theta$ only at finite exponents $L^{2p},L^{4p}$ and never $L^\infty$. So (3.8) $|I_{ZW}|\le\varepsilon D_{2,p}+C(1+\|V\|_p^p)$ holds, given $W,\Theta,\nabla T\in L^q$ and metric equivalence.

### 2. The $\Gamma_1$ three-descendant split (§2) is exact, not schematic

$\Gamma_1=\chi\nabla^4\chi*U=\chi(\nabla Z)*U$. One IBP off $\nabla Z$ gives precisely
$-\int\nabla P(V)*\chi Z*U-\int P(V)*d\chi*Z*U-\int P(V)*\chi Z*W$, i.e. (2.3). The first two are current-exponent $Z$-couplings: $\int|\nabla P(V)|\chi|Z||U|\le\varepsilon D_{2,p}+C_KK^2\int|Z|^2|V|^{p-2}\le\varepsilon D_{2,p}+C(\|Z\|_p^p+\|V\|_p^p)$ (2.4) using $\tfrac2p+\tfrac{p-2}p=1$; and $\int|P(V)||d\chi||Z||U|\le C(\|Z\|_p^p+\|V\|_p^p)$ (2.5) using $\tfrac1p+\tfrac{p-1}p=1$. The third descendant is the $\chi ZW$ residual dispatched in §1. I confirmed $\Gamma_1,\dots,\Gamma_4$ are the $(\alpha,\beta,\gamma)=(0,4,0),(1,3,0),(0,3,1),(0,1,3)$ allocations of the high-cutoff sum in the derived equation (shifted memo (4.1)); this is a real term inventory traceable to the exact variation (3.1)–(3.6), not a labeling convenience. $\Gamma_4=\chi d\chi*\nabla V$ absorbs directly into diffusion (2.2).

### 3. One incomplete attribution in (3.9)

The high-cutoff sum of the m=2 $U$-equation contains, beyond $\Gamma_1$–$\Gamma_4$, four more allocations with cutoff order $\le 2$: $(2,0,2)=\chi\Theta*V$, $(2,2,0)=\Theta*\Theta*U$, $(2,1,1)=\Theta*d\chi*W$, $(1,1,2)=|d\chi|^2*V$. The statement (3.9) that "all high-cutoff terms ... satisfy [the bound]" then sums only the four top-jet allocations. This is an incomplete attribution: the intrinsic $\chi\Theta*V$ is a signed Hessian handled separately in Step 38 §2 ($\le\varepsilon D_{2,p}+Cr^{-2}\|V\|_p^p$), and $\Theta^2U$, $\Theta d\chi W$, $|d\chi|^2V$ are base-pair/$r^{-2}$ terms ($\le C(1+\|V\|_p^p)$). All are controlled, so the assembled (4.3) is correct, but (3.9) as written does not by itself exhaust the high-cutoff line. The passage becomes rigorous only when the Step 38 signed term and the three benign terms are added. This is a presentation gap, not an analytic hole.

### 4. The $Z$-evolution count (§5) and same-$p$ closure — verified

I recomputed the cutoff evolution directly. Since $\chi$ is time-fixed, $\partial_t\nabla^3\chi$ arises from the time-varying connection: $\partial_t\nabla^3\chi\sim\nabla(\partial_t\Gamma)*d\chi+\partial_t\Gamma*\Theta+(\text{norm/metric variation})$, with $\partial_t\Gamma=g^{-1}*\nabla\mathrm{Ric}(U)\sim\nabla U=W$ (order one, since $\mathrm{Ric}(U)$ is algebraic in $U$). Therefore
$$
\partial_t Z\sim \underbrace{\nabla W}_{=V}*d\chi+W*\Theta+\underbrace{U*Z}_{\text{norm variation}},
$$
whose **highest $U$-derivative is $V=\nabla^2U$, not $\nabla^3U$.** This is the crucial point: $\nabla^3\chi$ carries at most $\nabla^1\Gamma$, so $\partial_t$ produces at most $\nabla^1(\partial_t\Gamma)=\nabla W=V$. Testing against $|Z|^{p-2}Z$:
$$
\tfrac{d}{dt}\|Z\|_p^p\le C\Big(K\|Z\|_p^p+\|W\|_{2p}\|\Theta\|_{2p}\|Z\|_p^{p-1}+r^{-1}\|V\|_p\|Z\|_p^{p-1}\Big)\le C(1+\|V\|_p^p+\|Z\|_p^p),
$$
matching (5.3). The pair $Y_{2,p}=\|V\|_p^p+\|Z\|_p^p$ then obeys $Y'\le C(1+Y)$ and Grönwall gives finiteness on $[\tau,T)$. There is no $\nabla^4\chi$ and no $\|Z\|_{2p}$ entering the $Z$-equation; the closure is genuinely at exponent $p$.

### 5. The load-bearing unproved input: (1.1) $\nabla T\in L^q$

The $V$-energy closes only through the mixed $T$-products of §4. The derived reaction sum caps the $\widetilde R=T$-derivative at $k\le m-1=1$ (shifted memo (4.1), $k\le m-1$), plus the separate $U*\nabla^2U=U*V$ term with coefficient $K$. So **no $\nabla^2T$ appears** — good — but (4.2) and the $k=1$ products ($a*W*\nabla T$, $\nabla a*U*\nabla T$) require $\nabla T\in L^{2p}$, i.e. (1.1). The note states (1.1) but does not prove it here, and correctly rejects the "insert a missing $\chi$ into $\nabla^2a$" route (its (1.2) $\nabla^2a=2\chi\Theta+2d\chi\otimes d\chi$ shows the $d\chi\otimes d\chi$ part carries no $\chi$).

I checked the dependency chain is acyclic and reachable:
- **$T\in L^q$** (the $k=0$ inputs, and $a|T|=|U|\le K$ closing $a*V*T$): proved in shifted memo §6 (6.5)–(6.6), via one IBP on $\int\nabla^2a*\widetilde R*\widetilde R|\widetilde R|^{p-2}$ and $|\nabla a|^2/a=4|\nabla\chi|^2$. I re-verified this IBP and Young step; it stands.
- **$W,\Theta\in L^q$** (base pair): Step 37 as repaired by Step 38's signed lemma, given $T\in L^q$.
- **$\nabla T\in L^q$** (1.1): obtainable by the *same* residual mechanism. The top cutoff term of the $\nabla T$-equation is $\chi\nabla^3\chi*T=\chi Z*T$; testing against $P(\nabla T)$ and integrating off $Z$ gives $d\chi\Theta T P(\nabla T)$ (base-pair), $\chi\Theta\,\nabla T\,P(\nabla T)$ (signed Hessian in $\nabla T$, paid by the $\nabla T$-equation's own diffusion $\int a|\nabla^2T|^2|\nabla T|^{p-2}$), and $\chi\Theta T\,\nabla P(\nabla T)$ (Young). This needs only $\Theta,T\in L^q$ and does not require $\nabla T$ of itself — no circularity. So (1.1) is provable from $T,\Theta\in L^q$ by the identical device, but it is not written in this note.

Hence the m=2 lemma reduces to (c) $T\in L^q$ [established in §6], (d) $W,\Theta\in L^q$ [Step 37/38], and (e) $\nabla T\in L^q$ [reducible to (c)+(d), not yet written]. Under these, nothing invalidates (4.3)/(5.4).

### 6. What would invalidate the Grönwall inequality — and what does not

Within the three hypotheses above I found no term forcing $\|Z\|_{2p}$, $\|W\|_\infty$, $\nabla^2T$, or $\nabla^4\chi$ at the current level. The specific worry that the $Z$-equation might carry $\nabla^3U$ is resolved by the derivative count in §4 above: it carries only $V$. The one exposure is external: if the unweighted $\nabla T\in L^q$ estimate (1.1) cannot be secured, then (4.2) and the §4 $k=1$ products have no finite coefficient and (4.3) does not close. That is the single mathematical substance on which the m=2 conclusion presently rests and which is deferred.

### 7. Remaining substance to make this an unconditional lemma

1. **Write (1.1)** explicitly by the signed-IBP mechanism above (top term $\chi Z*T$ against $P(\nabla T)$, using the $\nabla T$-equation's own diffusion), confirming it needs only $T,\Theta\in L^q$.
2. **Confirm the Step 37/38 base pair** is complete, since (d) is itself conditional on (c) and on the signed-Hessian repair of $I_{1c},I_3$.
3. **Complete (3.9)** by explicitly adjoining the intrinsic $\chi\Theta*V$ (Step 38) and the benign $\Theta^2U,\Theta d\chi W,|d\chi|^2V$ terms, so that the high-cutoff line of the $U$-energy is fully accounted rather than represented by the top-jet subset.

The note's own statement that this is a finite-exponent m=2 lemma and not the all-order continuation is accurate; the all-order pattern (arbitrary distribution of a top cutoff jet against differentiated lower-order curvature, plus the transported-coefficient short-time existence and the terminal restart) is genuinely additional and is not reached by the m=2 calculation.
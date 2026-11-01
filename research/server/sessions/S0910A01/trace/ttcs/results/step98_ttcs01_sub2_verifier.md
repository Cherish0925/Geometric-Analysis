# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step98_trace_obstruction_theorem.md",
    "Sessions/S0910A01/workspace/notes/step97_ab_physical_cone_interpretation.md",
    "Sessions/S0910A01/workspace/scripts/step98_full_chirality_tensor_maps.py",
    "Sessions/S0910A01/workspace/notes/step96_source_compatible_kernel_map.md"
  ]
}
```

## Task

Verify the mathematical content and logical soundness of the Step 98 trace obstruction theorem for the product-orbifold Ozuch desingularization. The key claims to verify are:

1. SAME-CHIRALITY VANISHING: B_{++} = B_{--} = 0 for all spectral sectors and pairs. The argument is that B_ee = -B_oo exactly (verified computationally) and cross-parity blocks vanish by K-symmetry. Is this a structural identity or a numerical coincidence? Is there a representation-theoretic reason that same-chirality pairs should give zero response?

2. TRACE OBSTRUCTION: The AB sector gives cross-chirality trace c0 = 4a ≈ 0.1258 for adjacent pairs. For the mixed pattern, this sums to 0.503 t^2 at equal scales. The argument that this is a genuine obstruction relies on: (a) self-terms are pattern-independent, (b) all-same has zero inter-node trace (by B_same=0), (c) KE existence implies self-trace is solvable independently. Does this argument work? Are there loopholes?

3. TRACE VS P/Q: The claim that the trace channel is independent of the P/Q (traceless) channel and that the trace obstruction alone suffices. Is this correct in the Ozuch framework?

4. The P/Q channel structure: NN←NS has pure Q (anti-holomorphic from AA tensor on factor A), while NN←SN has pure P (holomorphic from BB tensor on factor B). Is this consistent with the product structure and chirality conventions?

## Output

## Verification memo — Step 98 inter-node trace obstruction

### Summary judgment

Three of the four items hold up as internally coherent computations, and the linear-algebra correction to A02 is correct. The one place where the reasoning does not yet close is the passage from "the assembled inter-node trace is strictly positive" to "this is a genuine barrier to desingularization." The decisive object needed to close it — the self-interaction (and background-deformation) trace as a function of the bubble scales — is asserted to be pattern-independent but is never computed, and the trace direction is never shown to lie in the cokernel of the full adjustment space. I also find an unreconciled normalization between Step 97 and Step 98 (power of $t$ and a prefactor) that bears directly on the eventual comparison with the construction remainder.

---

### Claim 1 — same-chirality vanishing $B_{++}=B_{--}=0$

**The stated derivation is circular, though the underlying numerics may still be sound.** Unpack the algebra actually in the script. The even/odd combinations are a $2\times2$ transform on (receiver chirality, source chirality):
$$
B_{ee}=\tfrac14(K_{++}+K_{+-}+K_{-+}+K_{--}),\qquad B_{oo}=\tfrac14(K_{++}-K_{+-}-K_{-+}+K_{--}).
$$
Given the two symmetries attributed to Step 90, $K_{++}=K_{--}$ and $K_{+-}=K_{-+}$, one gets identically
$$
B_{ee}+B_{oo}=\tfrac12(K_{++}+K_{--})=K_{++}.
$$
So the "structural identity $B_{ee}=-B_{oo}$" is *literally the same statement* as $B_{++}=0$, not an independent reason for it. Likewise the "cross-parity vanishing $B_{eo}=B_{oe}=0$" is algebraically equivalent to the pair $K_{++}=K_{--}$, $K_{+-}=K_{-+}$ and carries no extra content. The note therefore does not supply a representation-theoretic mechanism; it restates a numerical output.

**What is actually established:** $K_{++}\approx 0$ to machine precision at the rungs run (tensor sectors only at the coarsest rung $\tau=0.08,L_{\max}=80$; AB at finer rungs). That is meaningful evidence but not a proof, and the tensor-sector zero is checked at a single, fairly strongly regularized rung.

**What would make it structural:** an argument that a same-chirality source projects trivially onto a same-chirality receiver through the projected Green operator — e.g. that the self-dual $H^4$ obstruction source of an $\varepsilon=+$ Eguchi–Hanson bubble and the $\varepsilon=+$ linearized-curvature receiver sit in Green-orthogonal chirality classes. If such a symmetry exists it would upgrade $K_{++}=0$ from numerics to identity and would simultaneously determine whether it survives to all spectral orders (currently it is a leading-order statement only). This is worth isolating because the entire obstruction rests on same-chirality pairs contributing nothing.

---

### Claim 2 — is the trace a genuine barrier? (the central gap)

The chain is: (a) self-terms pattern-independent; (b) all-same has zero inter-node trace via $B_{\rm same}=0$; (c) KE existence on $\mathrm{Bl}_5\mathbb P^2$ makes all-same solvable; (d) subtract to expose $+0.503\,t^2$ that cannot be removed.

**Where it is strong.** The angular part is genuinely closed. On the physical cone $M_j=t_j^2u_ju_j^T$ one has $\operatorname{tr}M_j=t_j^2>0$ and the AB response is $-a\,(\operatorname{tr}M_j)I_K$, angle-independent. So neither the source angles $\theta_j$ nor the receiver angle can touch the trace component, and the trace enters as a sum of $t_j^2\ge0$ terms — sign-definite positive for the checkerboard sign pattern. That much is solid: within the *angular* freedom there is no escape, and the intersection of the traceless subspace with the cone is only the zero insertion (Step 97 §4).

**Where it does not yet close.** The only remaining adjustment freedoms are the scales $t_j$ and the background/deformation modes, and the argument handles them by a "difference with all-same" that implicitly holds the scale profile fixed. Concretely, write the trace equation at receiver $i$ as
$$
\operatorname{tr}\mathcal A_i(t,\varepsilon)=\underbrace{\operatorname{tr}\,\mathrm{self}_i(t_i)}_{\text{function of }t_i}+\operatorname{tr}\,\mathrm{inter}_i(t;\varepsilon)+\underbrace{\operatorname{tr}\,\mathrm{deform}_i}_{?}=0.
$$
For all-same, $\operatorname{tr}\,\mathrm{inter}=0$, so KE existence forces $\operatorname{tr}\,\mathrm{self}_i(t_i^\ast)+\operatorname{tr}\,\mathrm{deform}_i=0$ *at the all-same solution scale* $t^\ast$. For mixed the extra term is $+0.503\,t^2>0$. This obstructs mixed **only if** the self+deformation trace cannot be driven negative at some *other* admissible scale. The note never rules this out; it compares the two patterns at one common scale.

There is a clean way the loop *would* close, and it is precisely the missing computation: if the self+deformation trace is not merely pattern-independent but **identically zero at this order** (the same kind of vanishing as $B_{\rm same}=0$), then it can never equal $-0.503\,t^2$, and the mixed trace equation has no solution for any scales. KE existence already forces this quantity to *vanish at $t^\ast$* for all-same (since inter-node is zero there); the open question is whether it vanishes as a *function of $t$* or only at a point. Distinguishing these two is the single computation that determines whether Step 98 is a theorem or a suggestive coincidence.

Two further items feed the same question:
- **Pattern-independence of the deformation trace is the delicate one.** The background-correction field is exactly the object that tries to cancel the assembled source; its value is determined by that source and is therefore a priori pattern-dependent. "Pattern-independent by product symmetry" is defensible for the *self-interaction of a single bubble* (mirror symmetry in $\varepsilon_i$), but is not obviously true for the deformation response. What is needed is the statement that the trace direction in $\operatorname{Sym}^2(K_i)$ is not in the range of the deformation/gluing operator — i.e. that trace is a genuine cokernel direction — after all adjustment modes are included.
- **Remainder comparison is explicitly unfinished.** Both notes state the Ozuch/Biquard cubic-vs-remainder asymptotic has not been carried out. Since the barrier lives at a fixed power of $t$ and must dominate the construction error as $t\to0$, and since the all-same solution scale must also lie in the valid small-$t$ window, "leading-order barrier" is not yet supported by an error bound.

None of this contradicts the computation; it identifies that "strictly positive relative trace" and "unremovable obstruction" are not yet the same statement.

---

### Claim 3 — trace independent of P/Q

**The representation theory is correct.** For a 2-plane $K$, $\operatorname{Sym}^2(K)$ splits under $SO(2)$ frame rotation as trace (invariant, 1-dim) $\oplus$ traceless (spin-2 / double-angle, 2-dim). The trace component is a basis-free scalar, so it is genuinely independent of the P/Q (traceless) block and unaffected by receiver-frame rotation. The computed blocks respect this: AB is pure trace→trace, tensor sectors pure traceless. So "trace and traceless are independent equations" is right.

**"Trace alone suffices" inherits the Claim 2 gap.** Independence of the channels is a fact; sufficiency of the trace as an obstruction requires the trace to be an unremovable cokernel direction, which is exactly what Claim 2 has not established. So Claim 3 is correct as an algebraic statement and only as strong as Claim 2 as an existence statement.

---

### Claim 4 — P/Q vs product structure

**Internally consistent, with the holomorphy assignment resting on unverified conventions.** The pattern is coherent: a tensor harmonic on factor A couples only when the pair shares the A-pole (NN←NS), on factor B only when it shares the B-pole (NN←SN), and the opposite corner SS (sharing no pole) carries only the scalar×scalar AB trace. That "shared pole ⇒ nonzero tensor overlap" is the expected support structure. The A↔B / P↔Q exchange symmetry between NN←NS and NN←SN is a good self-consistency signal, matching the two factors entering the self-dual/anti-self-dual decomposition with opposite roles. What is *not* checked in the material is the absolute assignment "AA→Q, BB→P" versus the reverse; that depends on the orientation and complex-structure convention on each $S^2$ and on how $\varepsilon$ is tied to $R^\pm$. Since the trace barrier is driven by AB and declared independent of the P/Q values, this does not affect the headline, but the P/Q signs are convention-fixed rather than derived here.

---

### The A02 linear-algebra correction (Step 98 §7)

**Correct.** For the real-linear map $\xi\mapsto P\xi+Q\bar\xi$ on $\mathbb C$, the real determinant is $|P|^2-|Q|^2$, so a nontrivial kernel exists iff $|P|=|Q|$; $|Q|>|P|$ gives $\det<0$, an invertible (orientation-reversing) real map with no kernel. A02's "$|Q|>|P|\Rightarrow$ kernel $\Rightarrow$ solvable" is indeed mistaken. The "eigenvalues of opposite sign" remark is loose but harmless (a $2\times2$ real map with negative determinant has real eigenvalues of opposite sign). The separation of the trace channel from P/Q reinforced here is the same $SO(2)$ decomposition noted in Claim 3.

---

### Consistency issue to reconcile: power of $t$ and prefactor

Step 97 §5 gives the AB radial piece as $4a\,t^3=0.12577\,t^3$, carrying an explicit receiver scale $t_i$ (so $t_it_j^2\sim t^3$). Step 98 §5 assembles $\operatorname{tr}=2(0.12577+0.12577)\,t^2=0.503\,t^2$, i.e. $16a\,t^2$, with only the source scale ($t_j^2$). These differ both in the power of $t$ (whether the receiver scale enters) and in the numerical prefactor (radial-to-trace is a factor 2; $8a\,t^3$ vs $16a\,t^2$). This is very likely a difference of normalization convention rather than an arithmetic error, but it is unreconciled in the notes. It matters concretely because the *power of $t$* is exactly what must be compared against the (still-unquantified) construction remainder to justify "leading-order," and because a consistent exponent is needed before "dominates as $t\to0$" can be asserted.

---

### What would make the obstruction airtight

1. A symmetry/representation argument for $K_{++}=0$ (not the equivalent restatement), which would also settle whether it is a leading-order or all-order fact; plus a finer-rung confirmation of the tensor-sector zero beyond $\tau=0.08,L_{\max}=80$.
2. The self-interaction trace and the background-deformation trace computed **as functions of the scales**, to decide whether the self+deformation trace vanishes identically at this order (which closes the argument) or can absorb $-0.503\,t^2$ at some scale (which reopens it).
3. An explicit statement that the trace direction in $\operatorname{Sym}^2(K_i)$ is a cokernel direction of the full linearized gluing/deformation operator, so that it cannot be removed by any adjustment mode.
4. Reconciliation of the Step 97 / Step 98 normalization, followed by the Ozuch/Biquard remainder estimate at the reconciled power of $t$.

The notes' own delimiting remark (Step 98 §6, Step 97 §6) that this concerns one orbifold, filling, and desingularization method, and does not by itself settle Einstein existence on the smooth resolution or the all-dimensional pinching proposition, is consistent with the material and should be kept in view when relating this branch to the original problem.
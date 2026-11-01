# TTCS Independent Branch Record

```json
{
  "step_id": 27,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/notes/step26_wang_continuation_specification.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the shifted-curvature continuation mechanism for the normalized fixed-cutoff flow ∂_t g=-2a(Ric+g), a=χ². Read the Step 27 note, Wang's actual Section 4 proof, Yang's DeTurck construction, and the full-velocity tensor derivation. Check the convention G=(g∧g)/(2(n−1)), Ric(G)=g, ∇G=0, ∂_tG algebraic; derive the schematic evolutions of T=Rm+G and U=aT with all highest cutoff derivatives visible. Then assess whether Wang Lemmas 4.10, 4.11, 4.13, 4.14 transfer without an uncancelled highest-order term. Focus especially on χ∇^{m+2}χ*U, the integration by parts, the cutoff derivative equation driven by Ric(U), and any error in the proposed dependency triangle. Give explicit repairs or a precise obstruction; do not merely call terms lower order.

## Output

# Verification memo: shifted-curvature continuation for ∂ₜg = −2a(Ric+g), a=χ²

## Summary judgment

The shifted-tensor mechanism is internally correct as a *transfer scheme* from Wang's unnormalized Local Ricci Flow (LRF) extension theorem to the normalized fixed-cutoff flow. I find no uncancelled highest-order term. The one essential analytic fact that makes the transfer work is correctly identified and I confirm it below. What remains is genuine estimate-writing plus one convention sign that must be pinned. I also record where the surrounding narrative is honest about what these energy identities do *not* by themselves supply. Below, equation numbers refer to the Step 27 note, the A01 tensor-energy memo, and Wang §4.

---

## 1. The shift-tensor conventions are correct

With Kulkarni–Nomizu $(g\owedge g)_{ijkl}=2(g_{ik}g_{jl}-g_{il}g_{jk})$ and $G=\frac{1}{2(n-1)}g\owedge g$, I verify the contraction in the first–third slots:
$$
g^{ik}G_{ijkl}=\frac{1}{n-1}\bigl(n\,g_{jl}-g_{jl}\bigr)=g_{jl},
$$
so $\operatorname{Ric}(G)=g$ and $\operatorname{Ric}(\widetilde R)=\operatorname{Ric}+g=E$ (1.2) hold. Since $G$ is a constant multiple of $g\owedge g$ built from the parallel metric, $\nabla G=0$, hence $\nabla^k\widetilde R=\nabla^k\operatorname{Rm}$ for $k\ge1$ (1.3): the shift moves only zero-order curvature. The time variation $\partial_tG=\frac{1}{n-1}(h_{ik}g_{jl}+\cdots)$ with $h=-2aE$ carries no derivative of $a$ or $E$ (1.5); this algebraic character is genuine and is the only structural payoff of the shift. Also $|a\widetilde R|\le|a\operatorname{Rm}|+C_n$ (1.4) is immediate from $0\le a\le1$ and dimension-controlled $|G|$, so the extension hypothesis $\sup|a\operatorname{Rm}|<\infty$ is equivalent to $\sup|a\widetilde R|<\infty$. All of §1 checks out.

## 2. The shift does not remove ∇^{m+2}χ — correctly stated

Section 2 states plainly, and I confirm, that substituting $E=\operatorname{Ric}(\widetilde R)$ leaves the true highest cutoff term $\chi\nabla^{m+2}\chi*\widetilde R$ in place (2.4). Because $\nabla G=0$, the $G$-terms in (2.3) either drop a curvature factor or become pure cutoff terms at an order already present; they cannot cancel $\nabla^{m+2}\chi$. This is the honest reading. Any presentation that "hides" the top cutoff derivative before integration by parts would be wrong, and the note explicitly forbids that (§5, last sentence). Good.

## 3. The one load-bearing fact, verified

The reason the normalization is harmless is **not** the shift as such — it is the identity
$$
\nabla E=\nabla\operatorname{Ric},\qquad aE=\operatorname{Ric}(a\widetilde R)=\operatorname{Ric}(U).
$$
I verify both. From $E=\operatorname{Ric}+g$ and $\nabla g=0$, every *differentiated* occurrence of $E$ is a curvature derivative: the added $+g$ survives only in undifferentiated slots. And since contraction is with the parallel metric, $\nabla^k\operatorname{Ric}(U)=\operatorname{Ric}(\nabla^kU)$ exactly, so the flow velocity $aE$ is literally the Ricci contraction of $U=a\widetilde R$. This is what the A01 memo means (§2.1, boxed (2.10)): before commuting derivatives the whole right side is the linearization applied to $aE$, so there is no bare $(\nabla^2a)*g$ *source*. The correct reading is that $(\nabla^2a)*E=(\nabla^2a)*\operatorname{Ric}+(\nabla^2a)*g$ **does** contain a curvature-free $(\nabla^2a)*g$ piece; the point is that it must be kept as one factor $(\nabla^2a)*\operatorname{Ric}(\widetilde R)$ occupying Wang's exact slot, and that its differentiated descendants are $\nabla\operatorname{Ric}=\nabla\operatorname{Rm}$. This is right and it is the crux.

## 4. Term-by-term transfer of Wang 4.10, 4.11, 4.13, 4.14

The mechanism transfers because, at **every** place where Wang carries a factor $\chi^2\operatorname{Ric}$ or $\operatorname{Rm}$, the normalized flow carries the same factor plus a curvature-free companion of the form $(\nabla^k a)\,g$. I trace where each companion lands and confirm each is pointwise milder than a term Wang already controls:

- **Lemma 4.10 (base $L^p$ curvature).** Testing (2.1) against $|\widetilde R|^{p-2}\widetilde R$, the $(\nabla^2a)*E$ term integrates by parts once. When the derivative lands on the $g$-part of $E$ it produces nothing new ($\nabla g=0$); when it lands on $\widetilde R$ it is $|da||\nabla\widetilde R|$, absorbed by the weighted diffusion exactly as in Wang. The algebraic $G$-terms add at most $C(1+\|\widetilde R\|_p^p)$. Inequality (4.2) is the correct analogue of Wang Lemma 4.10.

- **Lemma 4.11 (the $|\nabla^2\chi|$ / $|\nabla U|$ interplay).** The genuinely coupled base case. In Wang, $I_1$ produces $C|\nabla^2\chi|_p^2|\nabla(\chi^2\operatorname{Rm})|_p^{p-2}$. In the normalized version the same $I_1$ with $\chi^2\operatorname{Ric}\to aE=\operatorname{Ric}(U)$ carries an extra piece $\int|\nabla U|^{p-2}\langle\nabla U,\chi\nabla^3\chi*ag\rangle$; integration by parts (Wang's own move) and Young against $\frac1{16}\int\chi^2|\nabla^2U|^2|\nabla U|^{p-2}$ leave $C|\nabla^2\chi|_p^2|\nabla U|_p^{p-2}$ — **structurally identical** to Wang, and in fact milder because $|ag|\le C_n$ replaces the possibly large $|\chi^2\operatorname{Ric}|$. The forcing of $|\nabla^2\chi|_p$ picks up $|\nabla(ag)|=|(\nabla a)g|\le 2\chi|\nabla\chi|$, a bounded additive constant inside $\int_0^t$, harmless under Lemma 4.8 (which already carries a "+1").

- **Prop 4.13 ($|\nabla^m\operatorname{Rm}|_p$).** The dangerous term $\chi\nabla^{m+2}\chi*\widetilde R$. Its $G$-summand $\chi\nabla^{m+2}\chi*aG\sim\chi\nabla^{m+2}\chi*ag$, after the same integration by parts, sends the derivative onto $\nabla^m U$ (diffusion) or onto $ag$ giving $\chi\nabla^{m+1}\chi*(\nabla a)g$ — cutoff order $m+1$ times a bounded order-1 factor. The branch where a derivative would fall on curvature is *absent* for the $G$-summand, so it is strictly milder than Wang's $\chi\nabla^{m+2}\chi*\operatorname{Rm}$.

- **Prop 4.14 ($|\nabla^m(\chi^2\operatorname{Rm})|_\infty$).** Same picture in $\Gamma_1,\Gamma_2,\Gamma_3$; the sole leftover Wang flags, $\nabla^2\chi*\nabla^m\chi*\chi^2\operatorname{Rm}$, becomes $\nabla^2\chi*\nabla^m\chi*\operatorname{Ric}(U)$ plus a curvature-free $\nabla^2\chi*\nabla^m\chi*ag$; both need only $|\nabla^2\chi|_q$ and $|\nabla^m\chi|_q$, which are the same quantities Wang already assumes uniformly bounded.

Conclusion: no companion term exceeds, in derivative order or in cutoff-derivative content, a term Wang bounds. There is no uncancelled highest-order term.

## 5. The dependency cycle — verified, with one correction to a Wang remark

The Step 27 cycle (§3, list 1–3) is the correct precise version of Wang's Remark 4.2, and it closes by the same $\int_0^t$ mechanism, **not** by strict spatial descent:
$$
\nabla^mU\ \xrightarrow[\text{top IBP}]{}\ \nabla^{m+1}\chi\ \xrightarrow[\text{Lemma 4.6}]{}\ \nabla^m\operatorname{Ric}(U)\sim\nabla^mU .
$$
This is a *self-referential* top order closed by Lemma 4.8 ($y'\le a\int_0^t y+by+1$), which is precisely why Wang needs the time-integral Gronwall rather than the pointwise one. I note that Wang's Remark 4.2(2) ("$|\nabla^{m-1}\operatorname{Rm}|$ depends on $|\nabla^m\chi|$") is loose: Lemma 4.4 at level $m-1$ gives the top cutoff term $\chi\nabla^{m+1}\chi*\operatorname{Rm}$, i.e. order $m+1$, exactly as the Step 27 list states ("$\nabla^{m-1}\widetilde R$ depends on $\nabla^{m+1}\chi$"). The note is more accurate than the source remark here.

The one genuinely new ingredient in the cycle is the curvature-free summand $(\nabla^m a)g$ inside $\nabla^m\operatorname{Ric}(U)$. Its top piece is $2\chi\nabla^m\chi$, so the forcing it injects into $\partial_t|\nabla^{m+1}\chi|$ is $\sim\chi|\nabla^m\chi||\nabla\chi|$: linear in $|\nabla^m\chi|$ (already bounded at induction level $m$), and — importantly — it does **not** reintroduce $\nabla^{m+1}\chi$ on its own right side. So it is a bounded forcing that Lemma 4.8's closure absorbs. The cycle survives.

## 6. Convention sign that must be fixed (a genuine bookkeeping item, not an obstruction)

The A01 memo uses $(\nabla_i\nabla_j-\nabla_j\nabla_i)X^\ell=R^\ell{}_{kij}X^k$; the shift note uses Kulkarni–Nomizu with first–third contraction giving $\operatorname{Ric}(G)=+g$. Merging these with Wang's explicit $\partial_tR_{ijkl}$ (which fixes both the diffusion sign $+\chi^2\Delta$ and the sign of the quadratic reaction) requires that the Ricci contraction of $\operatorname{Rm}$ in the chosen convention be $+\operatorname{Ric}$, so that $\widetilde R=\operatorname{Rm}+G$ (rather than $\operatorname{Rm}-G$) yields $\operatorname{Ric}(\widetilde R)=+E$. The note itself flags (2.1) as "a schematic equality of universal contractions rather than an assertion that each displayed coefficient is one," which is acceptable for the mechanism, but a complete proof must pin this so that $+a\Delta\widetilde R$ and the reaction have consistent signs. Concrete repair: fix once and for all $g^{ik}R_{ikjl}=R_{jl}$ (or its negation), then choose $\widetilde R=\operatorname{Rm}\pm G$ accordingly; every downstream sign is then determined and the energy inequalities (4.2)–(4.3), (5.4), (7.3) are sign-independent as the memos note.

## 7. One asserted cancellation that is not verified here and is not load-bearing

A01 §6 asserts that in $(\partial_t-a\Delta)|E|^2$ the bare $-4a|E|^2$ cancels against the Ricci terms of $\Delta_L$ (via $\operatorname{Ric}=E-g$) together with the inverse-metric variation, leaving (6.4) with only $-2a|\nabla E|^2+4aR_{ikjl}E_{ij}E_{kl}+2\langle E,\mathcal C_a(E)\rangle$. I did not reproduce this cancellation term by term. It is not needed for the continuation mechanism: the defect estimate (7.3), $Q'+cX\le Cr^{-2}Q+C\int\eta^2aF|E|^2$, absorbs any $|E|^2$ potential regardless of the sign of that coefficient. The cancellation matters only for a separate strict-damping statement, which is not used in the extension argument. If a strict-damping statement is later wanted, this identity should be recomputed explicitly, including the $\partial_t g^{-1}=+2aE$ contraction on both $E$-indices.

## 8. What these identities and the mechanism do not, by themselves, deliver

This is stated correctly in A01 §8 and Step 27 §§6–7, and I confirm the substance:

- **Existence.** The three energy inequalities and the shifted-curvature evolution are slice-wise for an *already smooth* solution. Short-time existence is carried by the transported-coefficient DeTurck construction (6.1)–(6.2): the added $-2\widehat a\,\widehat g$ is zeroth order in $\widehat g$ and does not change the principal symbol $-2\widehat a\Delta$, so Yang's fixed-point/Nash–Moser argument applies and $\varphi_t^*$ returns (0.1). This part is sound. But the *terminal* extension under only $\sup|a\operatorname{Rm}|<\infty$ is exactly what the induction is meant to supply, and it is that induction that still needs to be written in full (the note's §5 is explicit).

- **Metric comparison, Sobolev persistence, first-exit closure.** The bilipschitz bound (8.2) needs an integrable weighted pointwise defect bound or an independent local-existence estimate; a time-zero Ricci or Sobolev bound does not propagate on its own. The critical absorptions (4.6),(5.7),(7.4) use current-time $A(t)^2\|F\|_{L^2(\operatorname{supp}\chi,g(t))}\ll1$, which must live inside a simultaneous bootstrap. None of this is produced by the tensor algebra.

- **Geometry.** Even a complete extension theorem feeds only the Step 6 projector/Einstein–Weyl argument on a critical four-dimensional Ishida–LeBrun family. The positive branch, arbitrary topology, dimensions $\ge5$, and the Lean formalization are untouched. This is stated accurately.

## 9. Concrete items to make the mechanism a theorem

1. Fix the curvature/contraction sign so $\widetilde R=\operatorname{Rm}\pm G$ gives $\operatorname{Ric}(\widetilde R)=+E$ with $+a\Delta$ diffusion (§6 above).
2. Write $\mathcal L_{G,m}$ explicitly through Wang 4.11, 4.13, 4.14, showing every $(\nabla^k a)g$ companion lands in one of the three families and is dominated by the corresponding curvature term (the pattern of §4 above, one term at a time), and verify the Lemma 4.8 closure survives the extra bounded forcing of §5.
3. Keep $\chi\nabla^{m+2}\chi*U$ intact until the integration by parts; never split $-2aE$ into $-2a\operatorname{Ric}-2ag$ inside a high-derivative estimate.
4. Supply the existence/first-exit package (metric equivalence, Sobolev persistence, small $\beta_a$) separately; the energy identities presuppose it.

Net: the shifted-curvature continuation is a valid and cleanly organized transfer of Wang §4 to the normalized fixed-cutoff flow, with no uncancelled highest-order term and no hidden $(\nabla^2a)*g$ source. Its correctness rests entirely on $\nabla E=\nabla\operatorname{Ric}$ and $aE=\operatorname{Ric}(U)$, both verified. The remaining work is explicit estimate-writing and one sign convention, together with the independent existence/bootstrap inputs that these identities do not contain.
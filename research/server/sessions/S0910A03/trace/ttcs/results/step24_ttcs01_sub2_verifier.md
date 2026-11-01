# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/scripts/verify_step24_exact_curvature_variation.py",
    "Sessions/S0910A03/workspace/scripts/verify_step24_downstream_chain.py",
    "Sessions/S0910A03/workspace/notes/step22_inverse_square_correction_and_two_stage_architecture.md"
  ]
}
```

## Task

Verify the following two claims for the 4D normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed Riemannian 4-manifold.

CLAIM 1 (Normalization reaction): Under h = -2a·g with a = χ², the linearized Riemann curvature variation has ZERO lower-order R·h contribution. The conformal piece contributes only the Kulkarni-Nomizu Hessian source -(∇²a ∧ g) to ∂_t R_{ijkl}. Consequently, the full flow h = -2a(Ric+g) has curvature evolution ∂_t Rm = a·ΔRm + a·(Rm*Rm) + (∇a)*(∇Ric) + (∇²a ∧ E), where the quadratic reaction is EXACTLY the same as Wang's unnormalized local Ricci flow, and the normalization produces no linear Rm reaction.

CLAIM 2 (Subcritical downstream chain): Conditional on the q=2,3 integrated energy inequalities holding for the normalized cutoff flow, the complete chain from H₃(t) ≤ Cγ³/t to the gap theorem on critical Ishida-LeBrun 4-manifolds is logically sound:
(a) The subcritical Moser iteration from L³ to L^∞ converges because 3 > n/2 = 2 in 4D. The exponent sequence q_k = 3·(3/2)^k and the per-step constant product converge.
(b) The defect iteration from J₆ to |aE| ≤ Cδ(r²/t)^{1/3} uses the same subcritical potential.
(c) The metric drift ∫₀^{θr²} |aE| dt is integrable (proportional to δ), hence self-improving.
(d) All five first-exit conditions (Sobolev, energy, curvature, defect, metric) are self-improving.

Please verify these using the general linearized curvature variation formula (Chow-Lu-Ni Lemma 2.27) and the standard subcritical Moser theory. Identify any errors, missing hypotheses, or gaps in the chain.

## Output

# Verification Memo: normalization reaction and the subcritical downstream chain

I checked Statement 1 against the invariant conformal-change computation and against the two supplied scripts, and Statement 2 against the parabolic De Giorgi–Nash–Moser theory it invokes. There is a genuine sign/term error in Statement 1 that is also an internal contradiction between the two scripts, and Statement 2 rests on one central analytic step that the scripts state but do not derive (the passage from volume-weighted integral energies to volume-independent pointwise bounds). Details below.

---

## Statement 1: the conformal normalization DOES produce a linear Rm reaction

**The invariant check contradicts the "zero linear reaction" wording.** Take the finite conformal change $\bar g=e^{2f}g$. The (4,0) Riemann tensor obeys the exact identity
$$
\bar R_{ijkl}=e^{2f}\big[R_{ijkl}-(g\owedge B)_{ijkl}\big],\qquad
B_{ij}=\nabla_i\nabla_j f-\nabla_i f\nabla_j f+\tfrac12|\nabla f|^2 g_{ij}.
$$
Linearizing with $\partial_\epsilon\bar g|_0=\phi g$ (so $f=\tfrac12\phi\epsilon$) gives
$$
\partial_\epsilon\bar R_{ijkl}\big|_0=\phi\,R_{ijkl}-\tfrac12(g\owedge\nabla^2\phi)_{ijkl}.
$$
The (4,0) variation carries the algebraic scaling term $\phi R_{ijkl}$; it is **not** zero. What is genuinely free of an algebraic curvature term is the **(1,3)** tensor: $\delta R^l{}_{ijk}$ for conformal $h$ contains only derivatives of $\phi$. The Part-1 cancellation in `verify_step24_downstream_chain.py` (two pairs summing to $\phi R-\phi R=0$) is describing the (1,3)-level algebraic structure, and then the printed conclusion transfers it to the (4,0) evolution used in the energy estimates. That transfer drops the scaling term.

**Consequence for the quantity actually estimated.** The energy hierarchy works with $F=(1+|{\rm Rm}|^2)^{1/2}$, so the object that matters is $\partial_t|{\rm Rm}|^2$, in which both $R_{ijkl}$ and the four inverse-metric slots vary. For pure conformal velocity $\partial_t g=\phi g$ the two contributions are
$$
2\langle\phi R,R\rangle+R_{ijkl}R_{abcd}\,\partial_t(g^{ia}\cdots g^{ld})
=2\phi|{\rm Rm}|^2-4\phi|{\rm Rm}|^2=-2\phi|{\rm Rm}|^2 .
$$
This is confirmed independently by the homothety $g(t)=c(t)g_0$: $|{\rm Rm}|^2_{cg_0}=c^{-2}|{\rm Rm}|^2_{g_0}$, hence $\tfrac{d}{dt}\log|{\rm Rm}|^2=-2\phi$. With the normalization piece $\phi=-2a$ this is a linear reaction $+4a|{\rm Rm}|^2$.

**Which files are right.** Step 23 eq. (2.2) and `verify_step24_exact_curvature_variation.py` both keep the linear term $a\cdot{\rm Rm}$ and are correct. Step 23 §6 even reproduces the exact homothetic rate $\tfrac{d}{dt}\log|{\rm Rm}|^2=4(1+3k_0/c)$, whose Einstein value $k_0=-\tfrac13,c=1$ vanishes — this rate contains the normalization contribution. The Part-1 conclusion in `verify_step24_downstream_chain.py` ("normalization $-2ag$ produces NO linear Rm reaction") therefore contradicts both Step 23 and its sibling script. It also contradicts its **own** homothetic block a few lines later: that block prints $\tfrac{d}{dt}\log|{\rm Rm}|^2=4\varepsilon$ with $\varepsilon=(n-1)k+1$, and the "$+1$" inside $\varepsilon$ is precisely the normalization's linear contribution. So Statement 1 is inconsistent with the numerics printed under it.

**Is the dropped term load-bearing?** No, provided the physical radius stays bounded. The reaction feeds $H_{q,j}=\int\eta^2 a^{q-2}F^q$ as
$$
\int\eta^2 a^{q-2}\cdot 2q\,aF^q\le 2q\,H_{q,j},
$$
an additive $+CH_{q,j}$ with an $O(1)$ coefficient (in the flow's time units), not an $r^{-2}$-scaled one. On $t\le\theta r^2$ this multiplies the persistence estimate by $e^{2q\theta r^2}$. Because $r$ is chosen small (the absorption threshold forces $\gamma_j(0)\lesssim r^2\sqrt{K_0}$ below a fixed constant), $r^2$ is small and this factor is harmless. The correct statement is: **the quadratic reaction equals Wang's; there is an additional linear reaction $-2\phi|{\rm Rm}|^2$ from the conformal $-2ag$ piece, of lower order, absorbed together with the $r^{-2}H_{q,j}$ term for small $r$.** Eq. (2.2), (2.7), and the two scripts should be brought into agreement by carrying this term explicitly rather than deleting it.

**One further point about the stationarity confirmation.** `verify_step24_exact_curvature_variation.py` §5 substitutes $E=0$ into the proxy $h=-2aE$ and finds $h=0\Rightarrow\partial_t{\rm Rm}=0$. That is true but trivial: with $E\equiv0$ the whole velocity vanishes by construction. It does **not** confirm the term-by-term decomposition (2.2), because at an Einstein metric ${\rm Rm}\neq0$, so the individual pieces $a\Delta{\rm Rm}+a({\rm Rm}*{\rm Rm})+a\,{\rm Rm}$ must cancel among themselves. That cancellation (the $-2a\,{\rm Ric}$ part and the $-2ag$ part being opposite conformal velocities at ${\rm Ric}=-g$) is the nontrivial consistency, and it is exactly the balance the missing linear term participates in. As written, dropping $a\,{\rm Rm}$ breaks this balance; restoring it repairs it.

---

## Statement 2: the subcritical chain — principle sound, one crux not derived

### (a) The subcritical Moser upgrade

The spatial heuristic "$3>n/2=2$" is not by itself the right threshold for a parabolic operator; the parabolic threshold is $(n+2)/2=3$, which $L^3_x$ meets only borderline. The chain is nevertheless subcritical for the correct reason: on any interval $[t_0,2t_0]$ bounded away from $0$, the bound $H_3(t)\le C\gamma^3/t$ gives $F\in L^\infty_t L^3_x$, and the parabolic scaling number is
$$
\frac2q+\frac np=\frac2\infty+\frac43=\frac43<2,
$$
which is strictly subcritical. The abstract product also converges: with $q_k=3(3/2)^k$ and per-step constants growing at most polynomially in $q_k$, $\sum_k q_k^{-1}\log q_k<\infty$ because $q_k$ grows geometrically. Both are correct as stated.

**What is not established is the volume-independence of the resulting pointwise bound.** Subcriticality makes the iteration *converge*; it does not by itself make the final constant free of the Sobolev constant $A_0$ (equivalently, free of collapse). The standard parabolic $L^\infty$ estimate $\|u\|_{L^\infty(Q_{1/2})}\le C\|u\|_{L^2(Q_1)}$ has $C$ depending on the domain's Sobolev constant, which diverges under collapse. To reach a collapse-independent $|a{\rm Rm}|\le C\gamma/t$ one must carry the $A_0$-normalized energies ($A_0^4H_3\le C\gamma^3/t$) through **every** iteration step so that only the volume-free combination $\gamma=A_0^2\|F\|_2$ survives. Part 2 of `verify_step24_downstream_chain.py` attempts exactly this and does not close: it produces in succession $C\gamma/(A^{4/3}t^{1/3})$, then $CH_2(0)^{1/2}/r^2$, then $C\gamma V^{1/3}/(r^{8/3}t^{1/3})$ (with a residual $V^{1/3}$ that would be fatal for a collapsing sequence), before writing "I think the correct scaling is $|{\rm Rm}|\le C/t$… this follows from the FULL Wang argument, not just the mean-value" and asserting the volume factor cancels. The comment block is a record of unresolved bookkeeping, not a derivation. Both the exact $t$-power ($t^{-1}$ vs $t^{-1/3}$ vs $t^{-2/3}$ appear) and the cancellation of $A_0$/$V$ remain open. This is the load-bearing step of the whole downstream chain.

The initial-time cancellation that the argument needs *does* work and is worth isolating as the reliable piece: at $t=0$,
$$
\gamma_j(0)=\mathsf S_j\|F(0)\|_{L^2(U_j)}\lesssim \big(r^2 V_j^{-1/2}\big)\big(\sqrt{K_0 V_j}\big)=r^2\sqrt{K_0},
$$
volume-free, which is what lets $r$ be fixed small below the absorption threshold with $K_0$ bounded by Chern–Weil. The one input inside this that is used but not proven is the relative Sobolev behavior $\mathsf S_j\lesssim r^2 V_j^{-1/2}$ **under collapse**; the $L^4$ Sobolev constant on a collapsed ball is a genuine analytic fact (volume-weighted Sobolev of Croke/Gallot type) that the notes assert. It is plausible but should be pinned down, since the entire collapse-independence rests on this exponent.

### (b) The defect iteration $J_6\to|aE|$

The exponent count is comfortable: $m=6$ exceeds every candidate threshold ($n/2=2$, $(n+2)/2=3$), so subcriticality of the defect is not in doubt (the "$2n/2$" wording in the comment is dimensionally garbled but the conclusion is safe). The persistence $J_6(t)\le e^{C\theta}J_6(0)$ with $J_6(0)\le\delta^6 V_j$ preserves the $\delta^6$ factor, and the $t^{-1/3}$ pointwise bound is integrable in time — the essential feature that separates the defect from the non-integrable $t^{-1}$ curvature bound, correctly emphasized in Step 23 §5.2.

Two items to nail down. First, `verify_step24_downstream_chain.py` Part 3 states $|aE|\le C\delta(r^2/t)^{1/3}$ with no derivation; it inherits exactly the volume-independence question of (a), since $J_6(0)$ carries $V_j$ and the target is volume-free. Second, Step 23 §5.2 asserts the $|E|^2$ evolution "contains the curvature potential but no cubic defect source." The reaction from $\partial_t{\rm Ric}\sim{\rm Rm}*h={\rm Rm}*aE$ contracted with $E$ is indeed $\sim aF|E|^2$ (the curvature-potential term, which is kept) and there is no $|E|^3$ term — that part is correct. But the conformal $-2aE$ velocity and the trace terms produce an $a|E|^2$ reaction with an $O(1)$ coefficient (again not $r^{-2}$-scaled), the exact analogue of the Statement-1 linear term. It should be carried explicitly in (5.4); like the curvature case it is absorbed for small $r$, but it is presently invisible in the boxed inequality.

### (c) Metric drift

Given (b), the arithmetic is right: $\int_0^{\theta r^2}(r^2/t)^{1/3}dt=\tfrac32\theta^{2/3}r^2$ (sympy confirms $\int_0^t s^{-1/3}ds=\tfrac32 t^{2/3}$), so the total drift is $\le\tfrac32 C\delta\theta^{2/3}r^2$, proportional to $\delta$. In the normalization units ($\lambda=-1$, so $r$ is a dimensionless ratio and $r\lesssim1$) this is a legitimate small dimensionless bilipschitz displacement, and the $t^{-1/3}$ integrand is integrable at $t=0$. This step is sound conditional on (b)'s pointwise defect bound.

### (d) The five self-improving conditions

The continuity/first-exit logic can close, but the phrasing in Part 4 is imprecise in a way that matters. It writes "entry hypothesis: bilipschitz factor $1+\epsilon$" and "exit guarantee: … factor 2." Going from $1+\epsilon$ to $2$ is a *weakening*, not a self-improvement. The correct structure is: define the first-exit time $\tau$ as the first moment the bilipschitz factor reaches (say) $2$; derive the drift bound $\le\tfrac32C\delta\theta^{2/3}r^2$ using *only* the factor-$\le2$ hypothesis (so the perturbed Sobolev/energy constants stay within their factor-2 versions); and observe that for small $\delta$ this bound is $<\log2$, so the factor never actually reaches $2$ before $\theta r^2$, giving $\tau\ge\theta r^2$. That closes, but it requires (F3),(F4) to be established with the factor-$\le2$-perturbed constants — i.e., it depends entirely on (a) and (b). Conditions (F1),(F2) are the routine ones (Sobolev stable to factor $\le2$ under bilipschitz; $H_2$ persistence from the absorbed $q=2$ inequality) and are fine. Conditions (F3),(F4),(F5) reduce to the same crux as (a),(b),(c).

---

## Net reading and the strategic target

Statement 1's quadratic reaction structure and heat coefficient are correct; the specific wording "no linear Rm reaction" is wrong, contradicts Step 23, the sibling script, and its own homothetic numerics, and should be replaced by "quadratic reaction = Wang's, plus a lower-order linear reaction $-2\phi|{\rm Rm}|^2$ absorbed for small $r$." Statement 2's subcriticality reasoning is valid in the correct parabolic form ($L^\infty_tL^3_x$, scaling $4/3<2$), the abstract product converges, and the drift arithmetic and first-exit logic close *conditionally*. The single unfinished mathematical object on which (a)–(d) all depend is the collapse-independent (volume-free) pointwise curvature and defect bound obtained by carrying the $A_0$-normalized energies through the entire Moser iteration; Part 2 of the script exhibits this as unresolved, with residual $V^{1/3}$ factors, and settles it only by assertion. Resolving it requires: (i) the exact $t$-power and $A_0$-power of the $L^\infty$ estimate for the degenerate operator $\partial_t=a\Delta+\text{potential}$ on the $A_0$-normalized cylinder, (ii) the collapse behavior $\mathsf S_j\lesssim r^2 V_j^{-1/2}$ of the relative $L^4$ Sobolev constant, and (iii) the explicit inclusion of the $O(1)$ linear reactions (curvature and defect) that are presently omitted from the boxed inequalities (2.7) and (5.4).

Finally, a framing point relevant to how this material feeds the top-line problem: the conditional endpoint here is a gap statement $\inf_g\|{\rm Ric}_g+g\|_\infty\ge\varepsilon_0(M)>0$ on critical Ishida–LeBrun 4-manifolds. Such manifolds carry no Einstein metric of that sign for Seiberg–Witten reasons, so a completed chain would contribute to a **disproof** of the Yau-26 statement in $n=4$ (a manifold satisfying the Ricci-pinching hypothesis yet admitting no $\lambda h={\rm Ric}_h$ metric), not to its proof, and only for this specific 4-dimensional family. Step 23 §7 states this directly ("a result for the critical four-dimensional … laboratory, not the full dimension-by-dimension Yau 26 statement"). Any assembly of Statement 2 should keep that target explicit, and the $n\ge5$ positive-collapse observation in Step 22 §9 (Kaluza–Klein circle-bundle Einstein models exist, so no collapse obstruction there) indicates the mechanism does not transport to higher dimensions as-is.
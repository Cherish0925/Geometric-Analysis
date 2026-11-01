# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step41_continuation_criterion_and_first_exit_assembly.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md"
  ]
}
```

## Task

Verify the continuation criterion (Theorem 3.1) and its application to the first-exit bootstrap, as stated in the Step 41 note. The key claims are:

1. Given a smooth solution of dt g = -2a(Ric+g) on [0,T*) with |U| = |a(Rm+G)| ≤ K and T* < ∞, the solution extends smoothly past T*. The proof uses: (a) metric equivalence from bounded velocity, (b) the Step 40 staggered L^p induction giving all derivative bounds, (c) Sobolev + Kato for pointwise bounds, (d) Arzelà-Ascoli for terminal convergence, (e) restart from the Step 37 DeTurck existence.

2. The first-exit bootstrap closes on the actual maximal interval. The curvature Moser gives |U(t)| ≤ Cγ/t + C for t > 0, which combined with the smooth initial data gives sup_{[0,T*)} |U| < ∞ when T* < ∞, hence T_max = ∞ by the continuation criterion.

Check carefully: (i) Is the argument from L^p bounds to pointwise bounds (Step C) correct for all m? Does the Kato inequality handle tensor norms properly? (ii) Is the terminal convergence (Step E) correct for this degenerate equation where the diffusion degenerates at χ=0? (iii) In the first-exit closure, the curvature endpoint |aF(t)| ≤ Cγ/t gives |U(t)| bounded only for t > 0 — does the argument properly handle the initial time t=0? (iv) Is there a gap between the per-datum continuation (which uses constants depending on the specific smooth solution) and the sequence-uniform estimates needed for the gap theorem?

## Output

## Verification memo — Step 41 continuation statement (Theorem 3.1) and first-exit assembly

### Overall reading

The logical skeleton is sound and the pieces fit together in the intended way: bounded $|U|=|a(\mathrm{Rm}+G)|$ on a finite interval $\Rightarrow$ all covariant derivatives of the velocity $\partial_t g=-2\mathrm{Ric}(U)$ are bounded $\Rightarrow$ a smooth positive-definite terminal metric $\Rightarrow$ restart. Theorem 3.1 is dimension-general (stated for closed $M^n$), which is a genuine strength; only the first-exit assembly §5 specializes to $n=4$. The substantive content is not created in this note — it is inherited from Step 40 (derivative-energy induction) and Step 37 (degenerate short-time existence), and the honesty about what §5 does not settle (Layer E, sequence-uniformity, positive branch, $n\ge5$, Lean) is appropriate. My checks below concern whether the inherited machinery actually delivers what Step 41 consumes, and locate one specific unaddressed regime and one structural distance to the per-manifold statement.

### (i) $L^p\to$ pointwise (Step C): the mechanism is correct; the input is only partly established

The Step C reasoning is valid for each fixed $m$. Kato's inequality $|\nabla|U_m||\le|\nabla U_m|=|U_{m+1}|$ holds for a section of any tensor bundle with a metric connection — it is rank- and dimension-independent — so applying it to the scalar $|U_m|$ and then Sobolev $W^{1,q}\hookrightarrow L^\infty$ ($q>n$) with the uniformly bounded Sobolev constant of Lemma 2.1 gives $\|U_m\|_\infty\le C(\|U_m\|_q+\|U_{m+1}\|_q)$. Tensor norms are handled properly. There is no error in Step C's own logic.

What Step C rests on is the delivery of $\|U_m\|_{L^q}<\infty$ for **all** $m$ and $q$, uniformly on $[\tau,T_*)$, by the Step 40 staggered induction. Here I flag an internal tension the core agent should reconcile: the companion note `step40_m2_coupled_continuation_mechanism.md` states in §6 that "the all-order pattern has not yet been written for arbitrary distributions" and lists the arbitrary-$m$ integration and the arbitrary-order unweighted $\nabla^jT$ module as still-needed, whereas `step40_staggered_all_order_continuation_candidate.md` presents the arbitrary-order induction as done. Step 41 §3 consumes the latter. Only $m\le 2$ is written in full detail; the general-$m$ term enumeration is asserted schematically (with a stated independent cross-check).

I independently verified the load-bearing leading-cutoff-order classification of equation (1.4), and it is correct: the unique term carrying $C_{m+2}$ is $\chi C_{m+2}*U$ (forces $\alpha=m+2,\beta=\gamma=0$), and the two terms carrying the current jet $C_{m+1}$ are $\chi C_{m+1}*U_1$ (the one removed by the extra integration (2.6)) and $C_{m+1}*C_1*U$ (a same-exponent product). So the specific error that invalidated Step 39 — using $C_{m+1}$ at exponent $2p$ — is genuinely absent at leading order, and the extra integration by parts is the correct repair. The general-$m$ closure is therefore credible, but the exhaustive term-by-term enumeration at arbitrary $m$ (and the finite-exponent schedule §4 applied to every distribution) exists in detail only for $m\le2$.

One point worth making explicit because it initially looks troubling and then resolves: the pointwise bound $|U|\le K$ does **not** control $\mathrm{Rm}=T-G$ pointwise near $\{\chi=0\}$ (it only bounds $\chi^2\mathrm{Rm}$, and $\chi^{-2q}$ is not integrable against a smooth cutoff vanishing at finite order). So the intermediate "$T_m\in L^q$" cannot come from the sup bound. It comes instead from the $\chi^2$-weighted energy $D^T_{m,p}=\int\chi^2|\nabla X|^2|X|^{p-2}$ seeded by the finite smooth norms at time $\tau$, propagated by Grönwall. This only closes because every term needing absorption into the degenerate dissipation is engineered to carry a matching $\chi$ factor (the discipline of expanding $\nabla^2a=2\chi\Theta+2\,d\chi\otimes d\chi$ and $\nabla^{m+2}a$ explicitly, and never inserting a phantom $\chi$). The m2 note's own warning — that a blind integration of $\nabla(\nabla^2a)$ would leave a $d\chi\otimes d\chi*T*\nabla P(X)$ term with no $\chi$ for the degenerate dissipation — shows the authors are tracking exactly the right hazard. This part is consistent. For the metric convergence itself, note that only the $U$-quantities matter: $|\nabla^m\partial_t g|=2|\mathrm{Ric}(U_m)|\le C|U_m|$, so the velocity and all its derivatives are controlled by $\|U_m\|_\infty$, and $T_m$ is purely an internal variable. Where $\chi=0$ the metric is frozen ($\partial_t g=-2aE=0$). So the degeneracy is invisible to the terminal-metric argument.

### (ii) Terminal convergence (Step E): correct, degeneracy does not obstruct it

The degeneracy at $\{\chi=0\}$ is not an obstacle to the terminal limit. On $\{\chi=0\}$ the metric does not move; on $\{\chi>0\}$ the velocity derivatives $|\nabla^m\partial_t g|\le C|U_m|$ are uniformly bounded on $[0,T_*)$ by (i). Converting these covariant bounds to bounds on coordinate components $\partial^\alpha\partial_t g_{ij}$ in fixed coordinates requires the standard connection-difference induction (control $\partial_t\Gamma$ and its derivatives from $|\nabla^m\partial_t g|$ plus the bilipschitz control of Lemma 2.1), which the note names but does not write; this is routine (Shi/Hamilton-type). Positive definiteness of $g_*$ follows from the exponential bilipschitz bound. The Cauchy-in-$C^k$ estimate is fine (the stated "$C_kT_*$" prefactor is unnecessary; $|g(t)-g(s)|_{C^k}\le\sup|\partial_\sigma g|_{C^k}\,|t-s|$ suffices). The delicate object is the **restart** from $g_*$ (Step 37, degenerate short-time existence), not the limit; that is separately consumed. One item there deserving independent scrutiny is Step 37 §3's assertion that $\delta\hat a$ retains a $\chi^2$ weight "since $\chi$ vanishes to order matching $a$" — this is precisely the transition-region weight structure and is stated rather than derived. Uniqueness on the overlap (Step F) for a degenerate-parabolic flow is also cited to Yang rather than shown.

Also on Lemma 2.1: the additive estimate "$|g(t)-g(0)|\le CKT_*$" is coordinate/background-dependent; the rigorous form is the multiplicative one, $e^{-CnKt}g(0)\le g(t)\le e^{CnKt}g(0)$, from $|\partial_t g|_{g(t)}\le CnK$ by ODE comparison. The stated conclusion (bilipschitz with constant depending on $n,K,T_*$) is correct via the exponential version.

### (iii) The initial time $t=0$ in the first-exit closure — a real, located issue

The Moser endpoint $\|aF(t)\|_\infty\le C\gamma_0/t$ gives $|U(t)|\le C\gamma_0/t+C$ (5.6), singular as $t\to0^+$. This singularity is harmless for Theorem 3.1's hypothesis: verifying $\sup_{[0,T_*)}|U|<\infty$ when $T_*<\infty$ uses the smooth solution on $[0,\tau]$ and (5.6) on $[\tau,T_*)$ where $C\gamma_0/\tau+C<\infty$. That deduction is correct.

The problem is inside the first-exit self-improvement, and it is specific to (H2). The other three hypotheses improve through time-integrable quantities:

- (H1) improves via metric drift (5.10), which integrates the **defect** Moser bound $|aE|\le C\delta(r^2/s)^{1/3}$; since $\int_0^t s^{-1/3}ds=\tfrac32 t^{2/3}$ is finite, the drift is $O(\delta t^{2/3}r^{2/3})$ and closes cleanly including at $t=0$. (This integrability is exactly why the defect Moser exponent $1/3<1$ is load-bearing, and it is a nice internal consistency.)
- (H3),(H4) improve to $(1+O(\delta))$ factors from the energy seeds, again finite at $t=0$.

But (H2) is a **time-uniform** bound $\sup_M|U|\le K_*$, and its only offered improvement (5.6) is $C\gamma_0/t+C$, which exceeds $K_*/2$ for $t< \sim 2C\gamma_0/K_*$. So the "strict improvement of (H1)–(H4)" asserted in §5.2 does not hold for (H2) near $t=0$. The open–closed argument at $t=T_{\rm ex}$ needs strict improvement of every hypothesis at $T_{\rm ex}$; for (H2) this requires $K_*>C\gamma_0/T_{\rm ex}+C$, i.e. a lower bound on $T_{\rm ex}$, which is not supplied. Near $t=0$ one must instead keep (H2) by continuity from the smooth short-time solution — but this needs an explicit initial-layer estimate on $[0,t_0]$ with margin, and none is written. Compounding this: $|U(0)|=|a(\mathrm{Rm}+G)|$ at $t=0$ is **not** controlled by $\delta_i=\|\mathrm{Ric}+g\|_\infty$ (large Weyl curvature can coexist with small $\mathrm{Ric}+g$), so $K_*$ cannot be taken small.

Concretely, the cure is one of: (a) reformulate (H2) as a parabolically weighted quantity, e.g. $\sup_M t\,\|aF(t)\|_\infty\le 2C\gamma_0$ (plus an additive constant absorbing $|aG|$), which (5.5) improves directly and which is finite at $t=0$; or (b) prove an explicit $[0,t_0]$ layer from Step 37's smooth solution keeping (H2)–(H4) with margin, with $t_0$ chosen so the Moser regime $t\ge t_0$ takes over. The final "$T_{\max}=\infty$" conclusion is very likely correct once this is done, but as written the first-exit closure does not treat the one non-time-integrable hypothesis at small $t$.

### (iv) Per-datum continuation vs. sequence-uniform bootstrap — the distance is substantive

The estimates of §6 are explicitly per-datum, with $c_4,C$ and the required initial smallness depending on $K_2^{(0)}$, $\mathcal S_0$, and the support geometry of the individual $(g_0,\chi)$. The note flags topology-uniformity as a separate matter (§8.2). But there is a step needed even for the **per-manifold** Conditional Theorem 7.1 that its proof sketch passes over: the sketch takes a sequence $g_i$ with $\delta_i=\|\mathrm{Ric}_{g_i}+g_i\|_\infty\to0$ and states the bootstrap hypotheses hold "for $i$ large." The bootstrap requires $\gamma_0=\mathcal S K_2(0)^{1/2}\le c_4$ with $K_2^{(0)}=\int\eta^2a^0F^2$, $F=(1+|\mathrm{Rm}|^2)^{1/2}$ — i.e. **small local full-curvature energy** and a controlled Sobolev constant. Neither is implied by $\delta_i\to0$:

- $\|\mathrm{Rm}\|$ (Weyl part) is uncontrolled by $\mathrm{Ric}+g$; a near-Einstein sequence can concentrate curvature.
- The Sobolev constant $\mathcal S_0$ degenerates under collapse.

The maximal-net cutoff (Step 30) is presumably meant to select a component of small local energy by pigeonhole, but that requires (a) the **total** curvature energy $\int|\mathrm{Rm}|^2$ bounded along the sequence and (b) non-collapse so that a net ball has definite volume and controlled Sobolev constant. Item (a) is plausibly reachable in $n=4$ from Gauss–Bonnet, $8\pi^2\chi_{\mathrm{top}}=\int(|W|^2+\tfrac{s^2}{24}-\tfrac12|\mathring{\mathrm{Ric}}|^2)$: under $\mathrm{Ric}\approx-g$ one has $\mathring{\mathrm{Ric}}\approx0$, $s\approx-4$, so $\int|W|^2\approx8\pi^2\chi_{\mathrm{top}}-\tfrac{2}{3}\mathrm{Vol}$ — but this still needs the **volume** of the near-Einstein sequence bounded, and among approximate $\mathrm{Ric}=-g$ metrics the volume is not a priori pinned. Item (b) (non-collapse / uniform Sobolev) is not addressed at all. So the passage from per-datum estimates to the per-manifold constant $\delta_0(M)$ of Theorem 7.1 requires exactly a uniform curvature-energy-plus-injectivity control along $\delta_i\to0$ sequences, which the note assumes rather than establishes. This is a distinct missing piece from the also-open Layer E terminal passage, and it is where near-Einstein sequences (collapse, curvature concentration) can genuinely obstruct.

### Independent checks that came out clean

- Remark 3.2: $|G|_g=C(n)$ is a fixed constant, so bounded $|U|\Leftrightarrow$ bounded $|a\mathrm{Rm}|$ up to an additive $C(n)$ — correct, and it matches the Wang Theorem 4.1 quantity $|\chi^2\mathrm{Rm}|_\infty$.
- Cutoff-jet evolution (2.10)/(5.1): from $\partial_t\Gamma\sim g^{-1}\nabla\mathrm{Ric}(U)$, one gets $\partial_t C_{m+1}\sim\sum_{j\ge1}U_j*C_{m+1-j}$ with top term $U_m*C_1=V*d\chi$ (bounded coefficient $\times$ current $V$); the schematic $U_0*C_{m+1}$ is the metric/volume-form variation in the $L^p$ energy, bounded by $K$. This is correctly typed.
- Coupled $(U_m,C_{m+1})$ Grönwall (adding (2.9)+(2.11)) is standard once both RHS depend only on $\|V\|_p^p+\|Z\|_p^p$ and previous levels.
- The Grönwall constants at each stage depend only on $K$, the uniform metric-equivalence/Sobolev/$|d\chi|$ constants (Lemma 2.1), and previously bounded norms — none blows up as $t\to T_*$ — which is precisely why $|U|\le K$ forces continuation.

### What would make the assembled result convincing

1. Reconcile the two Step 40 notes: state which document is current, and write the arbitrary-$m$ term enumeration and finite-exponent schedule with the same completeness as the $m=2$ case (or verify the schematic classification exhaustively), since Step 41 §3B consumes the all-order version.
2. Reformulate (H2) as a parabolically weighted quantity finite at $t=0$, or supply the explicit initial-layer estimate reconciling the smooth short-time solution with the $C\gamma_0/t$ Moser regime; note that $|U(0)|$ is not small under $\delta_i\to0$.
3. For Conditional Theorem 7.1, supply the sequence-uniform control of $K_2^{(0)}$ and $\mathcal S_0$ (bounded total curvature energy and non-collapse along $\delta_i\to0$), including the volume control needed to close the Gauss–Bonnet estimate of $\int|W|^2$.
4. The two consumed foundations — Step 37 degenerate short-time existence with the transition-region weight $\delta\hat a\sim\chi^2(\cdots)$, and uniqueness of the degenerate flow on the restart overlap — remain the analytic pieces most worth an independent re-derivation, since the entire continuation rests on the restart being genuine at $\{\chi=0\}$.

Nothing I checked contradicts Theorem 3.1 as a per-datum statement conditional on the Step 40 derivative-energy induction and the Step 37 restart; the mechanism handling the degeneracy (weighted dissipation with a strict $\chi$-weight discipline, and reliance on $U$-quantities alone for the metric limit) is coherent. The two places where the written argument does not yet close are the small-$t$ regime of (H2) in the first-exit assembly and the sequence-uniform inputs behind Theorem 7.1; both are located precisely and appear repairable rather than structural, but neither is presently established.
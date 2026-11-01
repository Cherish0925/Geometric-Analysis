# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Develop or refute a derivative-free first-exit theorem for the normalized cutoff flow based solely on weak weighted moments. Use H_q=∫eta²a^(q-2)F^q to obtain H_3 and then |aRm|, J_m=∫eta²a^(m-2)|E|^m to obtain |aE|, and triangular local Q energies. Ask whether one can choose the provisional quantities so no evolving Hess(a) or connection norm is ever assumed: only metric equivalence, local Sobolev, local energy, cutoff-gradient bounds, fixed-domain containment, and weighted pointwise curvature/velocity. If possible, formulate the exact first-exit closure and identify what remains to prove (especially smooth continuation for dg/dt=-2a(Ric+g)); if impossible, exhibit the precise term that cannot be controlled weakly. Include finite-neighbor and buffered-good-ball dependencies and preserve the distinction between local averages and support-global averages.

## Output

## 1. The bootstrap set can be chosen with only zeroth‑order and integral primitives

The Step 19 architecture carried a pointwise Hessian‑drift bound and a companion gradient bound `(D_p): |χ∇U| ≤ Cδ t^{-1/2}(r²/t)^{2/p}` as if metric equivalence and Sobolev persistence required them. They do not. The provisional quantities that actually need to be reproduced at a first‑exit time `T_*` are

- **C⁰ metric equivalence** `e^{-Λ}g(0) ≤ g(t) ≤ e^{Λ}g(0)`;
- **relative Sobolev persistence** on each buffered ball;
- **small local critical curvature energy** `R_α(t)=∫_{U_α}F² ≤ 2ε_*`;
- **weighted pointwise curvature** `|aRm| ≤ C/t`;
- **weighted pointwise velocity** `|aE| ≤ Cδ(1+r²/t)^{1/3}`;
- **support‑global unweighted defect** `Q_support(t) ≤ e^{Cθ}Q_support(0)`.

Each of these closes without ever naming `∇²a` or `∇U` pointwise, for two structural reasons already visible in your Step 20 and in Wang:

**(i) Metric equivalence and Sobolev are C⁰ facts.** The log metric ratio is `≤ 2∫_0^t |aE|_∞ ds`, controlled by the *velocity* bound alone with `p=6>2`; no derivative of the metric enters. Sobolev/isoperimetric persistence is then Wang Prop 3.6/4.9: it depends on tensor‑Lipschitz distance (C⁰ closeness), not on a time‑`t` Ricci lower bound. The Ricci lower bound is used only at `t=0` to *install* the initial relative Sobolev constant (Yang Thm 6.2 / Bishop–Gromov); afterward it propagates by `d_TL`. This removes the hidden worry that `Ric_{g(t)}` must be re‑controlled where `a` is small — it need not be.

**(ii) Every `a`‑derivative is paired with dissipation through the regular identity `|∇a|²/a = 4|∇χ|²`.** In all of your power inequalities the Hessian‑cutoff term `(∇²a)*E`, `(∇²a)*Rm` is integrated by parts once, producing `∇a·∇(test)` and `∇a·∇E`, which Young‑absorb into the curvature/defect gradient dissipation because `|∇a| = 2χ|∇χ| ≤ C√a/r`. The residue is always a *first‑order* cutoff potential `(|∇a|²/a + a)F^q = (4|∇χ|²+a)F^q`. Thus `∇²a` is a computed object inside a weak identity, never a provisional quantity.

The conclusion is affirmative and sharp: **a derivative‑free bootstrap set exists**, and the two "new PDE targets" of Step 19 collapse to fewer objects (see §2). The gradient estimate `(D_p)` is an artifact of trying to bound the Hessian drift directly.

## 2. The single genuinely nonlinear input: strictly‑supercritical weighted curvature integrability

The cleanest reformulation of your `H_q → |aRm|` and `J_m → |aE|` ladders is to recognize what the linear parabolic theory actually consumes. The velocity tensor solves

$$
\partial_t E = a\Delta_L E - 2aE + (\nabla a)*\nabla E + (\nabla^2 a)*E + a\,\mathrm{Rm}*E + a\,E*E,
$$

which in weak (tested) form is a **linear** parabolic system for `E` with:

- bounded effective drift, coefficient `∇a/√a = 2∇χ ∈ L^∞`;
- Hessian‑cutoff term removed by one integration by parts (bounded coefficient `∇a`);
- potential `V = a\,\mathrm{Rm}` (the `aE*E` piece is a self‑consistent potential `a|E|`, even smaller).

For De Giorgi–Nash–Moser local boundedness of `∂_t u = a\Delta u + (\text{bdd drift})\cdot\nabla u + Vu` in dimension `n=4`, the requirement on the potential is the parabolic Serrin condition `V ∈ L^{s}_{t,x}` with `s > (n+2)/2 = 3`. Your energy identity gives exactly the *borderline* `∫_0^{θr²} H_3 ≤ Cγ H_2(0)`, i.e. `aRm ∈ L^3_{t,x}` and no more. Therefore:

> The one nonlinear input the whole derivative‑free architecture needs is
> $$\boxed{\;a\,\mathrm{Rm}\in L^{3+\sigma}_{t,x}\ \text{on buffered cylinders, }\sigma>0,\ \text{volume‑independent}\;}$$
> created at positive time from small critical local `L²` energy.

Everything downstream is then *linear parabolic theory*, not a new nonlinear estimate:

1. `aRm ∈ L^{3+σ}` + Moser ⟹ `|aRm|_∞ ≤ Cβ/t` (the localized ε‑regularity output; this is exactly Wang Thm 6.3 in its localized, normalized form).
2. With `V=aRm ∈ L^{3+σ}` fixed, the velocity equation is linear in `E`; local boundedness gives `|aE|_∞`, and the δ‑linear rate `|aE| ≤ Cδ(1+r²/t)^{1/3}` follows because the *initial data* of the velocity moment is `J_6(0)^{1/6} ≤ δ V^{1/6}` while the curvature moment is `O(1)`. In other words, the curvature bound and the velocity bound are **the same linear De Giorgi theorem applied to two initial data**: `O(1)` produces the `1/t` curvature scaling, `O(δ)` produces the δ‑linear velocity scaling. No separate `J_m` machinery beyond this is needed once the potential is supercritical.
3. `|aRm|_∞ ≤ C/t` on `[t_0,T_*)` feeds the continuation lemma of §3.

This reduction is the most valuable structural point: **the Step 19 pair (ε‑regularity + weighted Bernstein) becomes one localized ε‑regularity statement**, because the linear theory delivers `L^∞` (and even Hölder) directly from a supercritical potential, with no gradient hypothesis. The dangerous differentiated‑curvature term `χa\nabla\mathrm{Rm}*U` — the term you flagged in Step 20 §6 as uncontrolled — appears *only* in the equation for `∇U`, which the derivative‑free route never forms. That is the precise term that "does not close weakly," and the architecture is arranged so it is never needed.

**Distinguishing check for whether `L^3` suffices or `L^{3+σ}` is essential.** Test the model scalar `∂_t u = a\Delta u + (a|\mathrm{Rm}|)u` on a Whitney cylinder with `a|\mathrm{Rm}|(x,t)=λ/(a_0 t)` (the borderline profile). After the Whitney rescaling `τ=a_0t`, `ℓ=cr χ_0`, this is `∂_τ u = \Delta u + (λ/τ)u`, whose Moser iteration closes iff `λ` is below the parabolic‑Serrin constant — i.e. the borderline is crossed precisely by the ε‑smallness `β = C\sqrt{ε_{Li}} < 1/(2n²)`. A short computation (backward average on `[τ/2,τ]`, tracking the constant in `\|u\|_{L^\infty(τ)} ≤ C\,τ^{-2}\|u\|_{L^2([τ/2,τ])}` with the `λ/τ` potential) shows the iteration constant is `exp(Cλ)`, finite for all `λ`, but the *rate* degenerates as `λ→` the critical value. This is worth doing numerically: it tells you whether you must manufacture `σ>0` or can run at `s=3` with the ε‑small constant. My reading of Wang/Li is that ε‑smallness lets you run *at* the borderline via the backward‑average trick, so the honest target is: localized `H_{q}` for a **fixed** `q_0` slightly above `3` (equivalently `aRm ∈ L^{3+σ}`), created at positive time exactly as Li creates an `L^3` potential from local `L²` persistence before a linear Moser step.

## 3. Normalized‑flow continuation is a Wang‑Theorem‑4.1 analog with derivative‑free hypotheses

Smooth continuation past `T_*` is a *separate logical layer* from the bootstrap, and its hypotheses are derivative‑free. Wang Thm 4.1 states: `|χ²Rm|_∞` and `|∇χ|_∞` uniformly bounded, plus bounded Sobolev, imply all `|∇^m(χ²Rm)|_∞` bounded and hence smooth extension. The higher χ‑derivative `L^p` bounds (`|∇²χ|_p`, `|∇(χ²Rm)|_p`, …) are **derived inside** the lemma by the triangular Gronwall interplay of Prop 4.9–4.14 — they are consequences of the two `L^∞` inputs, not additional assumptions. So the continuation consumes exactly the object your bootstrap already produces: `|aRm|_∞ ≤ C/t` (bounded on any `[t_0,T_*)`, `t_0>0`) and `|∇χ|_∞` (fixed function, C⁰‑stable).

What must be proven is the **normalized** analog, because your flow is `∂_t g = -2a(\mathrm{Ric}+g)`, not Wang's `-2χ²\mathrm{Ric}`. The extra `-2ag` term and the resulting curvature source `(\nabla^2 a)*g + a\,\mathrm{Rm}` do not disturb Wang's induction, for a concrete reason: `∇g ≡ 0`, so every derivative that lands on `χ²g` produces `∇^k(χ²)*g = ∇^k(a)*g`, i.e. a pure cutoff‑derivative term times the bounded fixed tensor `g`. These slot into Wang's first sum `∑∇^iχ*∇^jχ*∇^k(\cdot)` with an extra bounded factor, and the linear `a\,\mathrm{Rm}` term slots into the lower‑order reaction sum. Consequently the triangular system `{|∇^mχ|_p} ↔ {|∇^m(aRm)|_p}` retains Wang's Lemma 4.8 structure and closes by the same Gronwall argument. The identities `E=\mathrm{contr}(\mathrm{Rm})+g`, `∇E=\mathrm{contr}(∇\mathrm{Rm})` make `E` interchangeable with `\mathrm{Ric}` up to the benign `g`. **This is a bounded, checkable extension of Wang §4 to the normalized velocity, and it is the honest home of "smooth continuation for `dg/dt=-2a(\mathrm{Ric}+g)`."** Formalizing it is more tractable than the abandoned Bernstein target because it is a term‑by‑term inheritance rather than a new degenerate estimate.

## 4. Exact first‑exit closure and what remains

Let `T_*` be the supremum of times on which the smooth normalized cutoff flow exists (short‑time from Yang/Wang) and all provisional quantities hold. On `[t_0,T_*)`:

- **(P1)** `d_{TL}(g(t),g(0)) ≤ Λ_0` from `2∫|aE|_\infty`, using **(P5)** with `p=6`.
- **(P2)** relative Sobolev on each `U_α` from **(P1)** via Prop 3.6, with constant `2A_α`.
- **(P3)** `R_α(t) ≤ 2ε_*` from the weighted curvature‑power identity (your (5.1)/(2.1)), with the reaction `∫η²aF³` absorbed because `β = A_α^2\|F\|_{L^2(\widetilde U_α)} ≤ C_S^2 C_V^{1/2}\sqrt{ε_{Li}} < 1/(2n²)`; Hessian‑cutoff integrated by parts, `|∇a|²/a=4|∇χ|²`.
- **(P4)** `aRm ∈ L^{3+σ}(\text{buffered cylinder})` created from **(P3)** at positive time; hence `|aRm| ≤ Cβ/t` by localized Moser.
- **(P5)** `|aE| ≤ Cδ(1+r²/t)^{1/3}` by the linear velocity estimate with potential from **(P4)** and initial datum `J_6(0)^{1/6} ≤ δV^{1/6}`.
- **(P6)** `Q_support(T) ≤ e^{Cθ}Q_support(0)` by the triangular finite‑neighbor system (your (4.1)/(7.4)), curvature reaction absorbed by full‑support small `β`.

If **(P1)–(P6)** are each *strictly* interior at `T_*`, then `|aRm|_\infty ≤ C/t_0 < ∞`, so the §3 continuation lemma extends the smooth flow past `T_*` with all six quantities still interior — contradicting maximality. Hence `T_* ≥ θr²`, and metric drift `≤ Cδθ^{2/3}r²` gives the fixed‑topology negative pinching gap on the critical Ishida–LeBrun laboratory.

**What remains to prove, precisely:**

1. **Localized supercritical creation (the one hard theorem):** from `R_α(t) ≤ 2ε_*` on the buffered finite‑neighbor family under the normalized flow, obtain `aRm ∈ L^{3+σ}` on positive‑time Whitney cylinders with constants depending only on `(n=4, N, C_V, C_S, |∇χ|_\infty, ε_{Li}, θ)` and independent of collapsed volume. This is the honest content of your `H_q` hierarchy pushed one exponent above the borderline; the backward‑average on `[t/2,t]` and the ε‑small `β` are the mechanism.
2. **Normalized continuation lemma (§3):** the term‑by‑term Wang §4 inheritance, formalized.
3. **Triangular defect closure (P6):** the bounded‑overlap summation of *unnormalized* local energies with the finite‑neighbor coupling constant `C(c,L,N)r^{-2}`.

Items 2–3 are structurally routine given Wang; item 1 is the crux and is a *single* localized parabolic ε‑regularity statement — the derivative/Bernstein target is eliminated.

## 5. Finite‑neighbor, buffered‑ball, and average bookkeeping to carry

The reformulation stands or falls on three distinctions your notes already flagged; keep them explicit in any statement.

- **Unnormalized local integrals vs normalized averages.** `R_α = ∫_{U_α}F²` and `Q_β = ∫η_β^2|E|²` are unnormalized and sum with bounded overlap: `∑_{β∼α}Q_β ≲ N\int_{\text{buffer}}|E|²`. Normalized averages `\fint F²` do **not** sum this way. The Whitney‑ball smallness needed for local ε‑regularity is a *centered* budget `∫_{B_{10r}(y)}F² ≤ K_0\mathrm{Vol}(B_{10r}(y))`, not a consequence of one global energy bound on the disconnected support union. Bishop–Gromov then gives `ℓ^4\fint_{B_ℓ(y)}F² ≤ CK_0 r^4` uniformly in `χ_0`.
- **Volume‑independent `β` through the buffer.** `A_α^2\|F\|_{L^2(\widetilde U_α)} ≤ C_S^2 C_V^{1/2} r_*^2\sqrt{K_0}` with the neighbor count `N` and doubling ratio `C_V` absorbed; the regularized norm `F=(1+|\mathrm{Rm}|^2)^{1/2}` contributes only `O(r^2)` from the constant part. This is what lets the borderline `s=3` be crossed with a fixed small constant.
- **Buffered containment for integration by parts.** All cutoff‑gradient terms `∇η_α` must be supported inside `\widetilde U_α`, where the neighboring curvature energy is `≤ N·2ε_*`; otherwise the "removed" Hessian terms reappear as uncontrolled reaction. The single physical interval `t ≤ θr²`, `θ<c²`, is compatible with every Whitney level after the rescaling `τ=a_0 t`, `ℓ=crχ_0`, `τ/ℓ² = t/(c²r²)` — this uniformity in `χ_0` (including arbitrarily small `χ_0>0`) is what makes the linear operator uniformly parabolic on each cylinder and is the reason the cutoff level cancels exactly in the potential `a|\mathrm{Rm}| ~ λ/(a_0t)`.

## 6. A cross‑check worth running before committing

Before formalizing, verify the linear‑theory reduction on the exact tensor equation, not the scalar model: test `∂_t E = a\Delta_L E + \dots` by `η²|E|^{m-2}E`, and confirm that after (a) Kato `|∇|E|| ≤ |∇E|`, (b) integrating `(∇²a)*E` by parts, (c) treating `aE*E` as the self‑consistent potential `a|E|`, the only potential surviving in supercritical form is `a\mathrm{Rm}`, with every `∇a`‑term Young‑absorbed via `|∇a|²/a=4|∇χ|²`. If a Lichnerowicz cross term or the `\Delta_L` zeroth‑order Weyl action leaves a residual potential *not* of the form `a\mathrm{Rm}` or `a|E|`, that residual is the honest place where weak control would need one more idea; my expectation from `∇E=\mathrm{contr}(∇\mathrm{Rm})` and `|E|≤CF` is that it does not, and that `aRm ∈ L^{3+σ}` is the complete potential input. Confirming this on the index‑level equation is the highest‑value calculation for locking the derivative‑free closure.
# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step30_weighted_moser_and_family_repair.md",
    "Sessions/S0910A01/workspace/scripts/step30_weighted_moser_family_repair.py",
    "Sessions/S0910A01/workspace/notes/step29_simultaneous_support_theorem.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/notes/step29_terminal_density_bridge_lemma.md"
  ]
}
```

## Task

Verify the Step 30 repair of the four-dimensional negative Ishida--LeBrun selected-support route. Focus on four concrete issues, not the old dependency diagram: (1) whether the mixed Hölder--Sobolev estimate H_{3p/2} <= H_p^{1/2} ||z_p||_4^2 correctly repairs the half-power gap in the weighted Moser hierarchy with z_p=a^{(p-1)/2} f^{p/2}, including time cutoffs and polynomial p-losses; (2) whether ordinary unweighted Moser on U=a(Rm+G) is indeed unjustified as a first bound because the operator remains a Delta and the quadratic term becomes U*U, while U remains useful for continuation; (3) whether the Ishida--LeBrun family bookkeeping should use an O(A) Euler bound plus Vol/A lower bound rather than chi(M)=A+O(1) or K0->9, and whether sigma_i/A_i->0 (not exact sigma=0) is the full analytic regime; (4) whether the macro-disjoint support/plateau/eigenline zero-extension refinements are the right hypotheses for the terminal pullback chain. Please identify any remaining hidden mathematical gaps precisely.

## Output

# Verification Memo: Step 30 repair of the four-dimensional Ishida–LeBrun selected-support route

Session S0910A01. Independent checking of the four requested points, with the algebra re-derived from the notes and the residual mathematical substance stated explicitly.

---

## Issue 1 — Mixed Hölder–Sobolev estimate for the weighted hierarchy

**The bridge is correct.** With `z_p = η a^{(p-1)/2} f^{p/2}`, the pointwise identity

$$
\eta^2 a^{3p/2-2} f^{3p/2} \;=\; (a^{p-2}f^p)^{1/2}\cdot z_p^2
$$

holds exactly: the `a`-exponent on the left is `(3p-4)/2`, and on the right `(p-2)/2 + (p-1) = (3p-4)/2`. Cauchy–Schwarz with factors `(a^{p-2}f^p)^{1/2}` and `z_p^2` then gives

$$
H_{3p/2} \le \Big(\int a^{p-2}f^p\Big)^{1/2}\,\|z_p\|_4^2 = H_p^{1/2}\,\|z_p\|_4^2 .
$$

The identification `∫ a^{p-2}f^p = H_p` is valid precisely because `p>2` forces `a^{p-2}` to vanish off `supp a ⊆ {η=1}`; every iterate `p_k ≥ p_0 ∈ {3,6}` satisfies this, so the auxiliary-cutoff subtlety the note raises is real but harmless in the actual iteration. The earlier `‖z_p‖_3^3` route indeed sits on the wrong side: its integrand carries an extra `a^{1/2}`, and since `a≤1` one gets `‖z_p‖_3^3 ≤ H_{3p/2}`, so Sobolev on `z_p` cannot majorize `H_{3p/2}`. The half-power mismatch diagnosis and its repair are both sound.

**Sobolev, gradient, and recurrence check out.** `∇z_p` splits into a `∇η` piece (killed because `a=0` where `∇η≠0`), a `∇a` piece bounded via `|∇a|^2/a = 4|∇χ|^2 ≤ Cr^{-2}` yielding `Cp^2 r^{-2}H_p`, and a `∇f` piece yielding `Cp^2 D_p`; together `‖∇z_p‖_2^2 ≤ Cp^2(D_p + r^{-2}H_p)` and `‖z_p‖_2^2 ≤ H_p`. The passage (1.3)→(2.5)→(2.6) is arithmetically exact: raising `∫H_{p_{k+1}} ≤ Cp_k^N S(L_k∫H_{p_k})^{3/2}` to the power `1/(κp_k)` and using `(3/2)/(κp_k)=1/p_k` reproduces `m_{k+1} ≤ (CS)^{1/(κp_k)}L_k^{1/p_k}m_k`. The reciprocal sums `Σ1/p_k = 3/p_0 = (n+2)/(2p_0)` and `Σ1/(κp_k)=2/p_0=n/(2p_0)` are correct for `n=4`, giving time power `t^{-3/p_0}` and Sobolev power `S^{2/p_0}`, hence `β/t` for `p_0=3` and `δ(r^2/t)^{1/3}` for `p_0=6`, with the `S` and volume factors cancelling against the seeds exactly as displayed.

**The exponent `κ=3/2` is the correct parabolic gain.** In `n=4` the space–time Sobolev exponent is `(n+2)/n = 3/2`, so the mixed estimate is the correct Ladyzhenskaya-type parabolic interpolation, not the elliptic gain `n/(n-2)=2`. This is internally consistent and reassuring.

**What Issue 1 does not settle (precise).** The mixed estimate is a *correct bridge that consumes two un-derived inputs*:

1. The tensor-level power-energy inequality (2.1)/(2.3), `H_p' + c\,p^{-m}D_p ≤ Cp^N(r^{-2}+S^2Y)H_p + \text{source}_p`, with a *finite, `k`-independent* polynomial `N` and a *finite* dissipation-weakening `m`, for both `f=F` and `f=|E|`. The note asserts existence of finite `N`; the Moser product then converges for *any* fixed finite `N` because `p_k` grows geometrically (`Σ(\log p_k)/p_k<∞`, `Σk/p_k<∞`). This robustness is genuine and worth keeping. But the derivation that `N,m` are finite and uniform — through the moving metric, moving volume measure `∂_t dμ = -σ dμ`, the Lichnerowicz reaction, Hessian integration by parts, and the Kato regularization for `|E|` — is not carried out. If the Kato limit or the moving-norm terms hid a factor growing faster than polynomially in `p`, the product would not converge. This is the single most important unfinished analytic object.

2. The positive-time potential `S^2Y(t) ≤ Cβ^3/t`, feeding the coefficient in (2.1). It rests on the `q=2` and `q=3` energy estimates, which the step29 status table marks "schematically derived" — not complete tensor-index proofs.

The note's own phrasing ("(2.8) is a repaired analytic route, not a completed theorem") matches this reading.

---

## Issue 2 — Unweighted Moser on `U=a(Rm+G)` is not a first-bound tool

**Correct, for the stated reasons.** From (3.6), `(∂_t-a\Delta)\widetilde R = a(\widetilde R*\widetilde R + G*\widetilde R)+(\nabla a)*\nabla\widetilde R+(\nabla^2 a)*\widetilde R`. Multiplying by `a`: the quadratic reaction becomes `a\cdot(a\widetilde R*\widetilde R)=a^2\widetilde R*\widetilde R=(a\widetilde R)*(a\widetilde R)=U*U` — no spare factor of `a`. Testing `|U|^{p-2}U` against `(∂_t-a\Delta)U` produces only the degenerate dissipation `∫a|\nabla(|U|^{p/2})|^2`, because the principal operator remains `a\Delta`; on the collar `a=χ^2` vanishes, so this is not the uniformly parabolic dissipation an ordinary Moser scheme requires. Both obstacles the note names are real, and withdrawing the Step 29 unweighted-`U` shortcut is the right correction.

**`U` retained for continuation is consistent.** The identities `\operatorname{Ric}(U)=aE`, `∂_t g=-2\operatorname{Ric}(U)`, `\nabla G=0` and the triangular derivative induction of `shifted_curvature_continuation.md` §§4–7 genuinely require only a *first* bound `\sup|a\operatorname{Rm}|<∞` as input, which the weighted Moser of Issue 1 is meant to supply. The division of labor — weighted mixed Moser produces the first pointwise bound, `U` organizes higher derivatives and the smooth restart — is coherent.

**One reconciliation the note omits.** The continuation theorem's hypothesis (1.2) is `\sup_{[0,T)}|a\operatorname{Rm}|<∞`, but the weighted Moser output `‖aF(t)‖_∞ ≤ Cβ/t` diverges as `t→0`. The finite supremum on `[0,T)` is recoverable — near `t=0` from smoothness of the initial metric and short-time existence, on `[t_0,T)` from the Moser bound — but this splicing is not written down. It should be stated, because the continuation induction is invoked as if (1.2) were directly available.

**A stale statement to repair.** The Step 30 repair notice withdraws unweighted Moser "on `U=a(Rm+G)` *or* `|aE|`," and step27 §6 correctly runs the defect through the weighted hierarchy `H_p(|E|)` with seed `p_0=6`. Yet step29 Step E still reads "Standard parabolic Moser on `|aE|` (unweighted `L^p`)." The defect operator is also `a\Delta` (the `U=aE` equation (3) in step18), so the same degeneracy applies and the defect bound must use the weighted mixed route, not an unweighted one. The exponents happen to coincide (`n=4`, `p_0=6` gives `t^{-1/2}`, `S^{1/3}`, and the volume cancels to `δ(r^2/t)^{1/3}` either way), so the endpoint is unaffected, but the *mechanism* in step29 Step E is the withdrawn one and should be rewritten to the weighted mixed derivation. This also means the defect route needs its *own* tensor power-energy inequality for `f=|E|` with Kato regularization — the same un-derived object as in Issue 1, at a different seed.

---

## Issue 3 — `O(A)` Euler bound with `Vol/A` two-sided control, and `σ_i/A_i→0`

**The `O(A)` bookkeeping is correct and `χ(M)=A+O(1)` was wrong.** Re-deriving: `c_2(X_j)≤5c_1^2(X_j)+36`, `χ(M)=Σc_2(X_j)+χ(N)-2m`, and with `b_+(N)=0`, `D=A/3+σ` giving `χ(N)≤A/3+σ+6-4m`, yields

$$
χ(M) \le 5A+34m+χ(N) \le \tfrac{16}{3}A+σ+30m+6 .
$$

The slope is `16/3`, not `1`, and a `σ` term is present, so neither `χ(M)` nor `(2χ+3τ)(M)=\tfrac{2A}{3}-σ` is `A+O(1)`. At `σ=0` this recovers `χ/A≤65/6` (`m=2`, using `A≥12`) and `≤28/3` (`m=3`, `A≥24`), matching step18. The correction is sound.

**`K_0→9` is indeed unnecessary.** Chern–Gauss–Bonnet plus the pinching `|Ric+g|≤δ` gives `∫|Rm|^2 ≤ C_1χ(M)+C_2\operatorname{Vol}+C_3δ^2\operatorname{Vol}` structurally (in `4`d, `∫|Rm|^2` is a fixed combination of `χ`, `∫s^2`, `∫|Ric^\circ|^2`, and `s≈-4`, `|Ric^\circ|≤Cδ` under pinching). With `χ/\operatorname{Vol} = (χ/A)(A/\operatorname{Vol})` bounded, `K_0 = \operatorname{Vol}^{-1}∫|Rm|^2 ≤ C`. Only the existence of universal constants is used; the specific value `9` plays no role. Correct.

**`σ_i/A_i→0` is the right regime, and this is a substantive point.** The chain `σ≤R≤\tfrac{δ^2}{2π^2}\operatorname{Vol}` with `\operatorname{Vol}/A≤v_+` gives `σ/A≤Cδ^2`. Hence *every* pinching sequence with `δ_i→0` has `σ_i/A_i→0`, including sequences with all `σ_i>0`. Restricting to exact `σ=0` would miss the generic near-critical sequence. Insisting the smoothing cover the whole `σ_i/A_i→0` band is correct and materially strengthens the argument.

**Load-bearing inputs that live outside these notes (precise).**
- `R≥σ` (5.1) is the exact Ishida–LeBrun mixed Seiberg–Witten + CGB deficit inequality. Its sign and normalization conventions are not re-derived here; the whole `σ/A→0` conclusion and the terminal recalibration `D_a≤R-σ≤R` rest on it. Independent confirmation with explicit conventions is needed.
- `0<v_-≤\operatorname{Vol}/A≤v_+<∞` (4.7) is attributed to a "Step 4 volume estimate" not present. The lower bound (LeBrun-type `∫s^2≥32π^2(a^+)^2`, so `\operatorname{Vol}\gtrsim A`) is standard; the *upper* bound `\operatorname{Vol}/A≤v_+` is more delicate and is used twice (for `σ/A≤Cδ^2` and for `K_0≤C`). Both bounds should be exhibited, since the plateau-mass estimate (4.9) `\operatorname{Vol}(P_i)≥θv_-A_i` depends on the lower one and (5.3) on the upper one.

---

## Issue 4 — Macro-disjoint support / plateau / eigenline zero-extension

**These are the correct hypotheses for the terminal density bridge.** The A03 density-bridge lemma requires exactly (i) `\operatorname{Vol}_g(P)≥αA` and (ii) `|\sec_g|≤K` on `B_ρ(p)` with `Kρ^2<π^2/4`, plus `Q/A→0`. The refinements produce precisely these:
- The `r`-separated net of maximal-function good centers, bounded-degree interaction graph, coloring, and retention of a maximal-volume color class give *pairwise-disjoint* enlarged buffers, which is what makes `Q_{\rm global}=Σ_j Q_j+\text{frozen}` an exact sum with no double counting.
- The plateau (`a=1` on `B_{4r}`) with `|Rm|≤C/θ_0=K_{\rm pl}` supplies (ii); coloring with a retained volume fraction plus the lower `\operatorname{Vol}/A` bound supplies (i) with `A`-proportional mass.
- Zero-extension of the terminal eigenline/harmonic-form densities is consistent in direction: the density `\mathfrak D` is nonnegative and one seeks an *upper* bound on its pullback average, so zero-extending off the bounded-curvature region only decreases `∫_M\mathfrak D`, and the selected good point lies in `P` where the extension equals the true density. The inequality direction is preserved.

**These hypotheses are outputs of the still-conditional flow theorem.** The metric comparison `e^{-1/10}g_0≤g(T)≤e^{1/10}g_0` (needed to transfer volume fractions from initial to terminal time) is the bootstrap conclusion (B1), which depends on the entire unproved analytic chain (power-energy inequality, `q=3` potential, continuation). So Issue 4 correctly identifies the *target* hypotheses, but their realization is downstream of Issues 1–2.

**A cross-session inconsistency to reconcile.** A03 step29 Step 2 sets the positive-part monopole regularization `ε_Q=Q`, while A01 step30 §6.5 prescribes `ε=Q/\operatorname{Vol}` with final densities normalized by `A`. The harmonic-amplitude estimate `\||2πH|-r/(3\sqrt2)\|_2^2≤CQ` and the normalization `β=72π^2(a^+)^2` should be checked to hold under whichever scaling is adopted; the two notes presently disagree on the scaling.

**The terminal contradiction itself is arithmetically sound.** For the calibrated limit `\operatorname{Spec}(W^+)=(-1/6,1/12,1/12)`: trace `=0`, `|W^+|^2=1/36+2/144=1/24`, `\det W^+=-1/864`. The Weitzenböck `\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+` with `s=-4`, constant `|W^+|^2` gives `0=2|\nabla W^+|^2-1/6+1/24=2|\nabla W^+|^2-1/8`, forcing `|\nabla W^+|^2=1/16`, which contradicts the parallel structure the projector identity forces. The exclusion mechanism is internally correct.

---

## Remaining hidden mathematical substance (consolidated)

1. **Tensor power-energy inequality with finite polynomial `p`-loss**, for both `f=F` (curvature) and `f=|E|` (defect), including moving metric/volume, Lichnerowicz reaction, Hessian IBP, and Kato regularization. This is the analytic core; everything downstream is conditional on it. The Moser product tolerates any finite fixed `N`, but finiteness of `N` (and of the dissipation-weakening `m`) at tensor-index level is asserted, not shown.

2. **Positive-time `q=3` potential** `S^2Y≤Cβ^3/t`, resting on the `q=2` and `q=3` energy estimates, which are schematic.

3. **Continuation input reconciliation**: the `t→0` divergence of `‖aF(t)‖_∞≤Cβ/t` versus the continuation hypothesis `\sup_{[0,T)}|a\operatorname{Rm}|<∞` should be spliced explicitly (initial smoothness plus interior Moser).

4. **Wang Proposition 4.14 grouped IBP** transferred verbatim from `χ^2\operatorname{Rm}` to `U`: the residual top-cutoff distribution (7.11) and the new `G`-terms `\mathcal N_m` are estimated, but the assertion that all other distributions have cutoff order `≤m` and `U`-order `≤m` needs the term-by-term expansion rather than a structural transfer.

5. **`R≥σ` and `v_±`** (the Ishida–LeBrun deficit inequality and the two-sided `\operatorname{Vol}/A` bounds) are cited from primary sources / an unshown Step 4 and are load-bearing for `σ/A→0` and plateau mass.

6. **Cross-session regularization scaling** (`ε_Q=Q` vs `ε=Q/\operatorname{Vol}`) to reconcile.

7. **Connection to the interval proposition.** Even a complete version of this route excludes only sequences on the Ishida–LeBrun family with `δ_i→0` (near-critical, `σ_i/A_i→0`). The original problem asks for fixed dimension-dependent constants `c_n<C_n` in a *fixed* pinching interval, which corresponds to a *fixed* positive defect `δ`, not `δ→0`. A uniform floor `δ_0>0` for one family in the vanishing-defect regime does not by itself resolve the fixed-interval existence/non-existence question — nor does it cover arbitrary four-manifolds, the `σ=+1` side, `n≥5`, or the formal verification. Also, the assertion that the mixed Seiberg–Witten estimate "forces `k/A→1/3` for any candidate countersequence" (step29 §7), which is needed to close even the family-restricted statement, is not derived in the supplied files. The notes flag this reach honestly; it remains the dominant conceptual distance between the present route and the stated research target.

**Overall:** the four Step 30 repairs are individually correct — the mixed Cauchy–Schwarz bridge, the withdrawal of the unweighted-`U` (and `|aE|`) shortcut, the `O(A)` topology with two-sided `\operatorname{Vol}/A`, and the `σ_i/A_i→0` regime with the macro-disjoint/zero-extension hypotheses. The route is an internally consistent conditional architecture whose weight now rests almost entirely on the un-derived tensor power-energy inequality (items 1–2), on the primary-source inequalities (item 5), and on the still-open link to the fixed-interval proposition (item 7).
# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/notes/step29_consolidated_conditional_theorem.md",
    "Sessions/S0910A03/workspace/notes/step29_terminal_density_bridge_lemma.md",
    "Sessions/S0910A03/trace/ttcs/results/step16_ttcs02_sub1_generator.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Adversarially verify and strengthen the proposed common-union first-exit route for varying Ishida–LeBrun manifolds. Use the Step 23/26/A01 Moser files and the Step 29 terminal lemma. Focus on: (i) a quantitatively correct disjoint macro-support selection in collapsed Ricci-lower-bound geometry retaining a fixed total volume fraction; (ii) one common cutoff flow a=Σχ_j² with componentwise H2/H3/J6 and global Q closing noncircularly; (iii) strict center set P versus a larger bounded-curvature plateau containing every chart geodesic; (iv) terminal errors normalized by A or volume for σ/A→0, with positive-weight regularization ε chosen correctly when Q itself need not tend to zero; and (v) eigenline density restricted to the bounded-curvature region and extended by zero. Identify any remaining mathematical obstruction, especially any false use of maximal-function constants, Sobolev domains, or flow existence.

## Output

# Verification Memo: common-union first-exit route for varying Ishida–LeBrun manifolds

## Orientation

The route has two genuinely distinct halves. The σ>0 half (Step 29 §1) is a clean topological estimate: Chern–Gauss–Bonnet + signature + the LeBrun monopole inequality give a metric-independent lower bound on the pinching, with no analysis. The σ=0 half is the analytic engine: disjoint-support cutoff flow, weighted energy hierarchy, Moser iteration to `‖aRm‖_∞≤Cβ/t` and `‖aE‖_∞≤Cδ(r²/t)^{1/3}`, first-exit closure, then terminal recalibration + exponential-pullback selection into a forbidden calibrated Einstein germ. Everything downstream of the flow (Step 28/Step 29 terminal lemma) is well-organized and the two most attractive structural ideas — (a) the volume cancellation `S·‖F‖_{L²}~r²√K₀` making β collapse-independent, and (b) the Rauch pullback-Jacobian lower bound giving tangent-ball noncollapse regardless of base collapse — are algebraically and geometrically sound. The load-bearing unresolved substance is concentrated in the flow half, and there is one item there that currently blocks the pointwise bounds on which the entire σ=0 half depends.

I address the five requested items, then the flow-existence link and the distance to the stated goal.

---

## (i) Disjoint macro-support selection in collapsed Ric-lower-bound geometry

Two concrete defects, both repairable, one currently making the construction internally inconsistent.

**Doubling/maximal-function constant (Step 29 §3.1).** The passage sets the good set at threshold `4K₀` and concludes `Vol(G)≥(1−C_D/4)Vol≥Vol/2 for C_D≤2`. In dimension four the doubling constant at the Li scale, `C_D(4,Kr_*²)` with `Kr_*²` bounded, is a fixed number well above `2` (near `2⁴=16` as `r_*→0`, since `V(B_{2r})/V(B_r)→2ⁿ`). So `C_D≤2` is false. The weak-(1,1) bound for the centered maximal operator carries the doubling constant, giving `Vol({M_{r_*}|Rm|²>λK₀})≤(C_D/λ)Vol`. To retain a fixed fraction one must take `λ=2C_D~32`, not `4`. Consequence: the good-support initial energy becomes `⨏_{U_j}F(0)²≤(2C_D)K₀` rather than `4K₀`; this enlarges the numerical value of `β` but is absorbed by choosing the constant `c` in `r_*=cK₀^{-1/4}` smaller. Not fatal, but the stated inequality is wrong and should be replaced by the `λ=2C_D` version.

**Disjointness vs. covering (Step 29 §3.2–3.3).** The centers `{p_α}` are chosen `r_*/5`-separated, so only `B_{r_*/10}(p_α)` are disjoint; but the cutoff supports are `supp χ_α⊂B_{2r_*/3}(p_α)`, and `2·(2r_*/3)=4r_*/3≫r_*/5`. The supports overlap heavily. Then `a=Σχ_α²` is bounded by the packing number `C_pack`, not by `1`, and every downstream use of "`a≤1`" (Step 26 §4 `‖Z₆‖₂²≤J₆`, Step 27 §3.3 `‖z_p‖₂²≤H_p`, Step 23's single-support geometry) is invalidated in the overlap region. Step 23 §1's assertion of "disjoint good macro-supports" is therefore not delivered by the §3.2 selection at these radii.

The repair is standard and preserves the fixed volume fraction. Choose a maximal `2ρ_out`-separated subset of `G` where `ρ_out=2r_*/3` is the outer support radius. Then `B_{ρ_out}(p_α)` are genuinely disjoint, `B_{2ρ_out}(p_α)` cover `G` by maximality, and Bishop–Gromov (the volume-comparison direction that is legitimately available under `Ric≥-(1+δ)g`) gives
`Σ_α Vol(B_{ρ_out/?}) ≥ c_{BG} Vol(∪B_{2ρ_out}) ≥ c_{BG}Vol(G) ≥ (c_{BG}/2)Vol(M)`.
This yields genuinely disjoint supports **and** a fixed fraction of `Vol(M)~A`, so `a≤1` holds everywhere and the componentwise flow decouples exactly. I recommend adopting this in place of the `r_*/5`-separation. With disjoint supports the "common union flow" is literally a family of independent single-support flows, coupled only through the global `Q` integral and the (topological) terminal recalibration.

---

## (ii) One common flow with componentwise `H₂/H₃/J₆` and global `Q` — and the weighted Moser gap

**Noncircularity of the chain is structurally correct**, conditional on flow existence: the first-exit hypotheses (F1)–(F4) are assumed on `[0,T)`, the energy inequalities (Step 23 (2.7),(3.4),(3.5),(3.6),(4.2)–(4.4), (5.3),(5.6)) improve them strictly, and the metric drift `I(T)≤(3/2)Cδθ^{2/3}r_*²` (Step 27 (6.6)) improves (F1). The global `Q` closes componentwise on disjoint supports: (5.1)→(5.2)→(5.3) absorbs the curvature×defect term `∫a|Rm||E|²` using `γ_j=β` small and the componentwise Sobolev/dissipation. Because the flow freezes the metric off `∪U_j`, `Q(T)=`(evolved on-support)+(frozen off-support)`≤e^{Cθ}Q(0)`, and `Q(0)≤Cδ²Vol≤Cδ²A` gives `Q(T)/A≲δ²→0`. This part is coherent.

**The one item that currently blocks the pointwise bounds.** The weighted Moser iteration used to produce `‖aRm‖_∞≤Cβ/t` (Step 26 §5, Step 29 §4) does not close in the weighted variables `H_p=∫a^{p-2}f^p`, `z_p=a^{(p-1)/2}f^{p/2}`. The parabolic embedding in `n=4` places `z_p` in `L³_{x,t}`, and
`∫∫z_p³=∫∫a^{3(p-1)/2}f^{3p/2}` has `a`-exponent `3p/2−3/2`, whereas the next-level energy `M_{3p/2}=∫∫a^{3p/2−2}f^{3p/2}` has `a`-exponent `3p/2−2`. Since `3p/2−3/2>3p/2−2` and `a≤1`, one gets `∫∫z_p³≤M_{3p/2}` — an inequality in the wrong direction. The Sobolev step controls `∫∫z_p³` but does **not** bound `M_{3p/2}` from above, so the recurrence `M_{p_{k+1}}≤CS(L_kM_{p_k})^{3/2}` (Step 29 (4.4)) is unsupported by the displayed estimates. This exact half-power `a`-mismatch is stated in the S0910A01 Step 27 header and is arithmetically correct.

The unweighted variable resolves it cleanly. With `U=aF`, `w_p=U^{p/2}=a^{p/2}F^{p/2}`, one has `∫∫w_p³=∫∫a^{3p/2}F^{3p/2}=M[U]_{3p/2}` exactly — no exponent gap — and `‖w_p‖₄⁴=∫U^{2p}` matches the doubling gain. The seed transfers (`∫a³F³≤∫aF³` by `a≤1`) and the `L^∞` target `‖aF‖_∞` is unchanged. So the repair proposed by S0910A01 (iterate `U=a(Rm+G)` or `aE`, not `H_p`) is the right move.

Two things follow that the consolidation has not yet absorbed:

1. **Cross-session inconsistency.** S0910A01 Step 27 declares the weighted iteration defective and mandates the unweighted variable; S0910A03 Step 29 §4 still carries the weighted `K_p` recurrence and asserts product convergence. The consolidated Step 29 therefore rests on a step a parallel session has shown does not close. The unweighted energy inequality for `U=aF` (its dissipation structure, the `∇a`-remainders, and the `−2ag` reaction) is not derived in any supplied file; Step 27's header points to `step29_simultaneous_support_theorem.md §3` which is not present here.

2. **The volume cancellations must be re-verified after the rewrite.** The elegant outputs `‖aF‖_∞≤Cβ/t` (Step 27 (5.3)) and `‖aE‖_∞≤Cδ(r²/t)^{1/3}` (6.5) come from `S^{n/2p₀}·`seed with `S^{2/3}·V^{-1/3}=1` and `S^{1/3}·V^{1/6}=r^{2/3}`. These identities are algebraically correct **as stated for the weighted iteration**. In the unweighted variable the `a`-exponents and hence the Sobolev-power/volume bookkeeping change, so the "four-dimensional coincidence" `n/(2p₀)∈{2/3,1/3}` matching `V`-exponents must be recomputed. Until the unweighted energy inequality and its endpoint formula are written, `‖aRm‖_∞≤Cβ/t` — which feeds both Wang continuation and the terminal plateau curvature bound — is not established.

Because `‖aRm‖_∞≤Cβ/t` is the single quantity that (a) drives continuation (A4) and (b) supplies the plateau curvature `K` in (iii), this is the pivot of the whole σ=0 half.

**Minor point on the linearized curvature evolution (Step 23 (2.2)).** As printed, the reaction term `a(Rm*Rm+Rm)` carries no explicit `E`, which appears to contradict the stationarity check in §6 (`E=0⇒∂_tRm=0`). It is consistent only if `Rm*Rm` is read as `Rm*Ric⊂Rm*E` and `Rm` as `Rm*g⊂Rm*E`, i.e. the whole reaction is `a·Rm*E` and vanishes at `E=0`. The §6 stationarity argument depends on this reading. A full write-up should display the reaction as `a·Rm*E` explicitly, since the exact-Einstein cancellation used to justify the energy identities hinges on it.

---

## (iii) Strict center set `P` versus a larger bounded-curvature plateau

Here the note's specific radii are inconsistent with the only curvature control the flow provides. The pointwise bound is `‖aF‖_∞≤Cβ/t`; on the collar `{0<a<1}` this gives `F≤Cβ/(at)`, which is **not** a bound on `|Rm|` — it permits `F→∞` as `a→0`. A genuine sectional-curvature bound `|Rm|≤K` holds only on `{a=1}=∪P_α`.

The exponential-pullback construction requires every length-`ρ` geodesic from every center `p∈P` to remain in `{|sec|≤K}` with `Kρ²<π²/4` (needed for Rauch's Jacobian lower bound and absence of conjugate points, Step 28 §2–3). But Step 29 §3.3–3.4 places centers in `P_α=B_{r_*/3}` and takes `ρ≥r_*/4`. Then geodesics reach `B_{r_*/3+r_*/4}=B_{7r_*/12}⊂B_{2r_*/3}=supp χ`, i.e. into the collar where curvature is uncontrolled. The `K` used in `Kρ²<π²/4` is a curvature bound that does not hold on that annulus.

Repair, with a quantitative constraint that must be stated. Restrict centers to an inner ball (e.g. `B_{r_*/6}`) and take `ρ=εr_*` with `ε<1/6` so that all `ρ`-geodesics stay inside `{a=1}=P_α`, where `|Rm|≤K=Cβ/T=Cβ/(θr_*²)`. Then
`Kρ²=(Cβ/(θr_*²))·ε²r_*²=Cβε²/θ<π²/4`
forces `ε²<π²θ/(4Cβ)`. Since `β~C_Sob` is a fixed constant and `θ` is chosen small (for energy preservation), `ε` must be a genuinely small fixed fraction of `r_*` — it cannot be `~r_*/4`. This is achievable (any `ε` below the threshold), and the center set `B_{r_*/6−ρ}` still retains a fixed fraction of `Vol(P_α)`, hence `Vol(center set)≥α'A`. But the interplay `ε²≲θ/β` should be written explicitly, since it ties the pullback radius to the (small) flow time and the (fixed) critical parameter. The current `ρ≥r_*/4` value cannot be used.

---

## (iv) Terminal normalization for σ/A→0 and the positive-weight `ε`

**The `ε=Q` choice is dimensionally wrong for varying `A`.** Step 16 §3 and Step 29 terminal-lemma Step 2 set `ε=Q`. `Q~δ²A` is an **extensive** quantity. The weight-error terms in the exact regularization (Step 16 (7), (25)) are `ε²V` and `εI` with `I=∫q^+~(9/2)V~A`:
- `εI~εA` must be `O(Q)=O(δ²A)`, forcing `ε=O(δ²)`;
- `ε²V~ε²A` must be `o(Q)`, again `ε=o(δ)`.

With `ε=Q~δ²A` one gets `εI~δ²A²` and `ε²V~δ⁴A³`, both of which dwarf `Q` as `A→∞`, destroying the `O(Q)` calibration errors `∫a²=β+O(Q)`, `Z=β+O(Q)` that feed the harmonic-amplitude estimate (28)–(29). The correct choice is the **intensive** scaling `ε~Q/V~δ²`, i.e. `ε=cδ²`. Then `εI~δ²A~Q` (order `Q`) and `ε²V~δ⁴A=o(Q)`, and Step 16's own stated sufficient conditions `ε²V→0`, `ε√(VE⁺)→0` (with `E⁺~β~A`, `ε√(VE⁺)~ε A`) become `δ²→0` and `δ²A? `— which still needs care: `ε√(VE⁺)~δ²A` does **not** tend to zero at fixed `δ` with `A→∞`.

The resolution is to normalize the entire terminal argument by `A` (or `V`) from the outset. The pullback selection needs only `A^{-1}∫_M𝔇→0`, and
`A^{-1}∫𝔇≤C·A^{-1}(Q+ε²V)=C(δ²+ε²·(V/A))=C(δ²+O(ε²))`,
which `→0` for `ε→0` and `δ→0`. In the contradiction sequence (negation of a uniform gap = pinching `δ_i→0`) this holds along **any** `A_i→∞`, because `Q_i/A_i~δ_i²→0` even when `Q_i=δ_i²A_i` itself need not tend to zero. So the correct statement is: use the intensive weight `ε_i~δ_i²`, keep every terminal density and every calibration error normalized by `A_i`, and the pullback density at the selected center is bounded by `C·(Q_i/A_i)~Cδ_i²→0`. The `ε=Q` prescription and the extensive auxiliary conditions in Step 16 §3 are incorrect for the `A→∞` regime and should be replaced accordingly. This is precisely the point the task flagged (`ε` correct when `Q` need not vanish): `Q` may stay `O(1)` while `Q/A→0`, and only the intensive normalization survives.

**A numerical inconsistency in the σ>0 gap.** Step 29 (1.4)–(1.5) use `Vol→32π²A/9`, giving from `σ≤R≤(δ²/2π²)Vol` the bound `δ²≥2π²σ/Vol=9σ/(16A)`, i.e. `δ≥(3/4)√(σ/A)`. But the boxed (1.7) states `δ≥√(3σ/16A)=(√3/4)√(σ/A)`. These differ by a factor `√3` (constant `9` vs `3` under the root). The §10 correction lists `√(3σ/16A)` as intentional, so either the `Vol~32π²A/9` asymptotic or the gap constant carries a factor-3 error; they cannot both be right. (Relatedly, §10 already corrected the Chern–Gauss–Bonnet coefficient `6→4` in `∫|Rm|²=32π²χ+4∫|Ric₀|²`; the `Vol` asymptotic and the gap constant should be re-derived from a single consistent identity.) The direction of the σ>0 result is unaffected, but the explicit constant is not currently pinned down.

---

## (v) Eigenline density restricted to the bounded-curvature region

Step 16 (35) controls `∫_{U_i}⟨𝒜_iH_i,H_i⟩≤C(K)Q` **only on** the bounded-curvature plateau `U_i`, via `sup_{U_i}f_i²≤C(K)+1` (eq (22)). Off `U_i`, where curvature is large and `f` can be large, this density is uncontrolled. Yet Step 29 terminal-lemma (5) writes `∫_M𝔇≤119Q+CQ+C(K)Q` as an integral over all of `M` with the eigenline term included globally. As written this over-integrates: the eigenline contribution to an `M`-integral is not bounded by `C(K)Q`.

The correct object is the eigenline density multiplied by the indicator of `{a=1}` (or a plateau cutoff) and extended by zero. Then `∫_M𝔇` splits into the plateau part (full `𝔇`, bounded by `C(K)Q`) and the off-plateau part (without the eigenline term). This is harmless for the contradiction **iff** the pullback selection is confined to the plateau and every `ρ`-geodesic from a selected center stays in `{a=1}` — exactly the (iii) requirement. So (v) is consistent, but only after (iii) is corrected to keep geodesics inside `{a=1}` with the small `ρ=εr_*`; and Step 29 (5) should be rewritten with the eigenline term explicitly restricted-and-zero-extended, rather than integrated over `M`.

---

## The genuinely open analytic link: normalized cutoff-flow continuation (A4)

Every branch of the σ=0 argument funnels into one unresolved statement: smooth continuation of the degenerate normalized flow `∂_tg=−2χ²(Ric+g)` to `t=θr_*²`, given `‖aRm(t)‖_∞≤Cβ/t<∞` for `t>0`. Step 26 §8 and Step 27/28 argue via the shifted quantity `U=a(Rm+G)` that Wang's pseudolocality continuation (bounded `|χ²Rm|` extends unnormalized local Ricci flow) adapts, with `−2ag` "lower order." The files themselves state this is the "single open analytic task" (Step 26 §0) and label (A4) conditional (Step 29 §5.3). What is present is a structural sketch, not a proof: the DeTurck gauge for the fixed spatial cutoff, the degenerate parabolicity on the collar `{0<a<1}` where `Rm` (as opposed to `aRm`) is uncontrolled, and the induction coupling `∇^m(aRm)`, `∇^mχ`, `∇^{m-k}Rm` are asserted to close but not derived. This link, together with the unweighted Moser rewrite (ii), is what stands between the current material and a complete σ=0 statement. Both are internally identified; neither is executed in the supplied files.

---

## Distance to the stated research problem

The route, even with all five items repaired and (A4) proven, would exclude near-Einstein sequences (pinching `δ→0`) on the σ≥0 Ishida–LeBrun family in dimension four with `Ric_h=−h`. It does not produce dimension-only constants `c_n<C_n`, does not address the `λ≥0` target, does not treat four-manifolds outside this family or `n≥5` (where the notes correctly recall Kaluza–Klein positive-Einstein collapse blocks collapse-exclusion), and contains no Lean formalization. The consolidated conditional theorem (Step 29 §5) is honest about this. As a reusable mechanism — converting topological/gauge near-saturation into a forbidden local Einstein germ despite arbitrary base collapse, via Rauch tangent-ball noncollapse — it is a real structural contribution; its correctness now rests on (a) the unweighted-variable Moser inequality actually producing `‖aRm‖_∞≤Cβ/t` with the volume cancellation rechecked, and (b) the normalized continuation theorem. Those two, plus the intensive-`ε` normalization (iv) and the small-`ρ` plateau containment (iii), are the substance whose resolution would turn the conditional chain into an unconditional σ=0 result for this family.
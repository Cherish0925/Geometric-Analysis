# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md",
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260927_covering_geometry_and_sharp_subfamilies.md",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py"
  ]
}
```

## Task

Independently verify the geometric and global deduction from the frozen C² cell to a smooth exact-CH-collar blow-up cell and then to a balanced sequence with coefficient below four. Check bolt smoothness with dσ_i=2σ_j∧σ_k and ∫σ123=2π², topology/orientation of collapsing σ1 versus the aligned blow-up, the O(δ³) exact-collar smoothing, constant rescaling Ric=-6g to Ric=-g, I54 transfer arithmetic, and residual-finite fixed-ball supply. Also analyze the consequence of the inherited exact handle-only formula α=4h/(1+h): prove or refute that every pure-handle exact-CH cell must have J≥32π²ℓ, and formulate the distinct mixed-cell interaction question without conflating it with isolated handle improvement.

## Output

# Verification memo: from the frozen C² perpendicular cell to a balanced sequence below four, and what the handle-only identity forces

## Summary

**Verified:**
- the bolt regularity;
- the oriented topology of the σ₁-collapsing cell;
- the O(δ³) smoothing to a smooth exact-CH cell;
- the change of normalization from Ric = −6g to Ric = −g;
- the I54 transfer arithmetic;
- the residual-finiteness supply of large balls.

Two of these can be stated more strongly than the notes do:
- One diagonal sequence already gives lim sup α/h ≤ 4 − 8η/9. The "for every ε" form is not needed.
- On any cofinal tower of normal subgroups, the large-ball condition holds automatically.

**Proved:** every pure-handle exact-CH cell satisfies J > 32π²ℓ (strict for ℓ ≥ 1), through an exact relative identity. This settles the open item "can S¹×S³ cells be improved below 32π²" in Step 10 §6: in isolation they cannot.

The same identity, J − 8π²q = (S_C − 16d)/12 + L_C/4 − 4(2d/3 − W_C), holds for every cell. It shows that a cell goes below threshold only through a deficit in self-dual Weyl energy, and that signature funds this deficit only through the blowups. The mixed-cell question is then whether handle regions can share in a blowup-funded deficit more cheaply. That is distinct from improving a handle in isolation.

---

## 1. Bolt regularity with dσ_i = 2σ_j∧σ_k and ∫σ₁₂₃ = 2π²

**Lie algebra and fibre period.** Let e_a be the dual fields. From dσ₁(e₂,e₃) = −σ₁([e₂,e₃]) we get [e₂,e₃] = −2e₁ (cyclic). This is realised by X_a = −(i,j,k) in the unit quaternions. Then exp(θX₁) = cos θ − i sin θ, so:
- the e₁-flow is free right multiplication by a unit complex number;
- it has period exactly 2π.

**Volume normalization.** Σσ_a² is the unit round S³, so ∫σ₁₂₃ = 2π². This gives dV = π²√(h₁h₂h₃/G) dx, as in Step 10. The closed-form Ricci used there also checks against this normalization:
- for a₁ = a₂ = a₃ = a, the formula gives 2/a², the round S³ value;
- for a₁ = a₂ = a, a₃ = b, it reproduces λ_A = 4/a² − 2b²/a⁴ of I54 (5.1).

**Slice weights.** The isotropy circle at the bolt acts:
- on the normal disk with weight 1, because the fibre period is 2π;
- on span(e₂,e₃) with weight 2, since ad_{X₁} rotates the (X₂,X₃) plane at rate 2.

For a diagonal metric dt² + Σa_a²σ_a², the complete smoothness conditions are therefore:
1. a₁ is odd in t with a₁′(0) = 1, i.e. a₁² = t²φ(t²) with φ(0) = 1;
2. a₂² + a₃² is smooth in t² and positive (weight 0);
3. a₂² − a₃² = t⁴ψ(t²) (the weight-4 part of S² of a weight-2 representation).

The cross terms in a₁²σ₁² = a₁²(dθ + A)² are smooth because a₁² = O(t²).

**The profile meets all three.**
- G = yĜ(y) with Ĝ analytic and Ĝ(0) = e^{q_G(0)} > 0, so t = y^{1/2}·(analytic in y). Hence y = Ĝ(0)t² + O(t⁴) is analytic in t².
- F = yF̂ with F̂(0) = e^{q_F(0)}, because x₀S/y = O(y²). So a₁² = F̂(0)Ĝ(0)t² + O(t⁴), and F̂(0)Ĝ(0) = e^{q_F(0)+q_G(0)} = 1.
- The shift z̃₈ does give q_F(0) + q_G(0) = Σ(−1)^k z_k + Σ(−1)^k z_{8+k} − Σ(−1)^k(z_k + z_{8+k}) = 0, since T_k(−1) = (−1)^k. The independent script implements the same shift (`cG0.at[0].add(shift)`).
- The Step-9 jets confirm this: f₁g₁ = 0.96886036 × 1.03214048 = 0.99999999.
- w = log(1+x)S + u²(1−u)³C_w = O(y²), because S = O(u³) and u = ℓ⁻¹log(1+y/x₀) is analytic with u = O(y). So a₂² − a₃² = −xwφ(w) = O(y²) = O(t⁴), with an even smooth cofactor.

**Pointwise corroboration.** At a smooth bolt the weight-2 and weight-4 components of any invariant symmetric tensor must vanish on the bolt. That forces R₀₀ = R₁₁ and R₂₂ = R₃₃, which is exactly the recorded pattern (−206.29, −206.29, 193.57, 193.57).

## 2. Topology and orientation of the σ₁ collapse

Both e₁ and e₃ are left-invariant and generate right translations. Choose h ∈ SU(2) with Ad_h X₃ = X₁. Then φ(p) = p h⁻¹ satisfies φ(p·exp θX₃) = φ(p)·exp θX₁, so φ carries the aligned mapping cylinder onto the perpendicular one equivariantly.

To make the map the identity on the outer collar, take a path k(x) in SU(2) with k = h⁻¹ near x₀ and k = 1 near X, and set Φ(x,p) = (x, p·k(x)). This descends over the bolt because it is equivariant there. It preserves orientation, since right translation is isotopic to the identity on S³ and x is untouched.

Hence the perpendicular cell is oriented-diffeomorphic, rel the outer collar, to the aligned blow-up D#CP̄². Here σ₃ is the complex Hopf direction of the CH collar, whose x(1+x) coefficient is the sinh²ρ cosh²ρ term. The intersection form is (−1), so the I54 indices are k = 1, ℓ = 0, q = 1.

What would change the topology is collapsing a right-invariant circle, which generates left translations. The profile does not do this.

Φ is not an isometry of the collar: only U(1)_right preserves CH. So the perpendicular cell is the same manifold with genuinely different geometry. This matters for the inherited exclusions:
- I54 §6.1 says it covers "every smooth diagonal triaxial cell with this bolt". "This bolt" is the σ₃ (aligned) bolt, where b = t.
- The perpendicular cell is diagonal and triaxial with a radial CH collar, but has the σ₁ bolt.
- The aligned-bolt hypothesis in §6.1 is therefore essential, not removable, and nothing in §§3–6 contradicts J₁ < 8π².

**A topological check computable from the frozen profile.** The relative signature identity (1.1) predicts

  B_C − W_C = 12π² − 2d/3, where W = ∫|W⁺|², B = ∫|W⁻|².

This holds exactly for the complex-orientation blow-up and would change sign structure for the opposite one. The diagonal Bianchi IX Weyl components are algebraic in the same jets already used for Ricci. Evaluating them on the frozen record would test the orientation conclusion independently of the energy code.

## 3. O(δ³) smoothing

**Third-order contact at x = X.**
- 1 − S = (1−u)³(1+3u+6u²).
- e^{q}−1 = O((1−u)³).
- So d_F, d_G, d_w = O((X−x)³), and the decompositions of d_F, d_G, d_w in Step 10 §3 are algebraically correct.

**Derivative bounds.** By Leibniz, |(χ_δd)^{(k)}| ≤ C Σ_i δ^{−i} δ^{3−k+i} = Cδ^{3−k} for k ≤ 2. So the 2-jets of both g and g_δ lie within O(δ) of the CH 2-jet on B_δ.

**Curvature and energy.** Ric + 6g is a smooth function of (F, F′, F″, G, G′, w, w′, w″, x) on the region where F, G, x > 0, and it vanishes at the CH jet. Therefore:
- |Ric + 6g| ≤ C″δ on B_δ;
- Vol(B_δ) = O(δ);
- |J(g_δ) − J(g)| = O(δ³).

**Exact-CH region.** g_δ is smooth and equals CH for x ≥ X − δ/2. So the smoothed cell lies inside the CH ball of radius arsinh√X. No buffer beyond X is needed for the embedding.

**Sign of the change.** The sign of J(g_δ) − J(g) is unknown, but J(g_δ) → J(g). The constants v(g_δ) and t(g_δ) = ∫(s+4) in (2.1) are uniformly bounded in δ.

**Consequence for the corollary.** Step 10 states a separate sequence for each smoothing width. Instead, take a single diagonal sequence with δ_j → 0. Formula (2.1) is exact for each cell, and its limit uses only bounded J, v, t. That one sequence gives

  lim sup α(M_j)/h_j ≤ 28/9 + J(g)/(9π²) ≤ 4 − 8η/9,

with no ε.

## 4. Normalization Ric = −6g → Ric = −g

**CH collar normalization.** The collar is dx²/(4x(1+x)) + x(σ₁²+σ₂²) + x(1+x)σ₃². With x = sinh²ρ this becomes dρ² + sinh²ρ(σ₁²+σ₂²) + sinh²ρ cosh²ρ σ₃². That is CH² with holomorphic curvature −4, so Ric = −6g.

**Rescaling.** For g̃ = 6g:
- Ric_g̃ = Ric_g = −g̃, and Ric_g̃ + g̃ = Ric_g + 6g;
- |T|²_g̃ = 6⁻²|T|²_g and dV_g̃ = 6² dV_g.

So J₁(g̃) = J₆(g) exactly. The scale-invariant quantities ∫s², ∫|W^±|² and the reference values 16d and (2/3)d are unchanged.

**Radius and ball volume.** The radius is r₋₁ = √6·arsinh√8 = 2.449 × 1.7627 = 4.32. The ball D has Vol₋₆ = π²∫₀^X x dx = 32π² at X = 8, so d = 1152π² in −1 units. This d is huge compared with 8π². Consequently the d-dependent bounds (7.1)–(7.3) of I54 carry no information about this cell.

## 5. I54 transfer arithmetic

To first order, (2.1) gives ℰ_j ≈ ΣJ_i/v_j with v_j ≈ 2π²A_j and h_j = Q_j/A_j. So

  ℰ_j/h_j → (k_j J₁ + 32π²ℓ_j)/(2π²Q_j) = (2/9)·J₁/(2π²) + (7/36)·16 = 28/9 + J₁/(9π²).

Evaluations:
- J₁ = 8π²(1−ε) gives 4 − 8ε/9.
- J₁ ≤ 8π²(1−η/2) gives 4 − 4η/9.
- With η₁₆ = 1.0970563×10⁻³, 4 − 8η₁₆/9 = 3.99902484.

α(M_j) ≤ ℰ(g_j) because ℰ = 4 − I²/(VR) is the functional whose infimum defines α. The arithmetic is correct. It inherits two things from I54: the asymptotic handle cost of 32π² per handle and the o(Q_j) error bookkeeping.

## 6. Residual-finite fixed-ball supply

**The construction.** Γ acts properly, so only finitely many γ ≠ 1 satisfy d(p, γp) ≤ 2r. Γ is finitely generated and linear, hence residually finite (Mal'cev). Intersecting the finitely many separating finite-index normal subgroups gives a finite-index Γ_* that avoids all of them, so inj(p) > r in X_* = Γ_*\CH².

**Lifts.** For Γ′ ≤ Γ_* of finite index, the ball B(p,r) is contractible, so its preimage is [Γ_*:Γ′] disjoint isometric copies. That number is proportional to A′ = c₁²(X′). The balanced family uses only k_j = (2/9)h_jA_j = o(A_j) cells. Further covers increase χ_hol = A/9, so b⁺ > 1 is also available. Each step is correct.

**Strengthening.** If the inherited tower is cofinal and normal (Γ_j ⊲ Γ, ∩Γ_j = {1}), then the injectivity radius tends to infinity uniformly. The displacement condition only needs checking for x in a compact fundamental domain of Γ, which involves a finite set of γ, and normality makes it conjugation-invariant. For such towers the transfer holds on every sufficiently deep stage, not just on a specially selected tower.

The existential wording is needed only if the inherited family lives on a non-normal tower whose short loops persist. One example is a cyclic cover along Γ → ℤ/n where a short loop lies in the kernel.

## 7. Theorem: pure-handle exact-CH cells cost more than 32π²ℓ

**Theorem H.** Let D be a geodesic ball in CH² with Ric = −g, and d = Vol D. Let C = D#ℓ(S¹×S³), ℓ ≥ 1, carry any smooth metric agreeing with CH on a full outer collar. Then

  J(C) − 32π²ℓ = (S_C − 16d)/12 + 4B_C + ¼∫_C(s+4)², and J(C) > 32π²ℓ.

**Proof.**

*Step 1 (exact identity).* Pointwise, |Ric+g|² = |Ric°|² + (s+4)²/4 and |Ric|² = |Ric°|² + s²/4, so J = R − S/4 + L/4. A handle changes 2χ+3τ by −4 and τ by 0. Relative Chern–Gauss–Bonnet and signature, I54 (1.1) with k = 0 and q = 4ℓ, give:
- R = 32π²ℓ + S/3 + 4W − 4d;
- B = W − 2d/3.

Substituting gives the displayed identity exactly.

*Step 2 (scalar inequality).* By §6, embed D in a closed CH surface X* with b⁺ > 1, and glue C in. On M = X*#ℓ(S¹×S³), S_M = 32π²A* − 16d + S_C. The inherited metricwise estimate S_M ≥ 32π²A*, used in Proposition 3 of I44 §5, gives S_C ≥ 16d. All three terms of the identity are then ≥ 0.

*Step 3 (strictness).* Equality would force S_C = 16d, B_C = 0 and s ≡ −4 on C. The glued metric would then satisfy S = S₀, B = 0 and L_s = 0. The inherited equality argument of I44 Corollary 4 produces a parallel positive spinor. This contradicts c₂(S⁺)[M] = ℓ > 0. ∎

**A second route, giving the non-strict bound only.** Insert a single cell (n_j = 1) into covers X_j. Then (2.1) gives ℰ_j/h_j → J/(32π²ℓ), while (5.3) with θ = h gives ℰ_j/h_j ≥ 4/(1+h_j) → 4.

**What the theorem does not use.** No symmetry, collar radius or smallness is assumed.

**Consequences for Step 10 §6.**
- The open item "can S¹×S³ cells be improved below 32π²" is resolved: not in isolation.
- κ(0,ℓ) := inf J/(8π²) = 4ℓ is the exact infimum. Shrinking handles approach it; it is never attained.

## 8. The common identity for all cells: a self-dual Weyl deficit

For C = D#kCP̄²#ℓ(S¹×S³), put:
- δW = 2d/3 − W_C, the self-dual Weyl deficit relative to the CH ball;
- σ = (S_C − 16d)/12 + L_C/4, the scalar excess.

The same substitution as in Step 1 gives

  J − 8π²q = σ − 4δW, with δW = 12π²k − B_C ≤ 12π²k.

LeBrun's estimate holds on blow-ups and handle sums alike, so σ ≥ 0 for every cell. This single identity explains two facts at once:
- **Handles alone:** k = 0 forces δW = −B_C ≤ 0, so J ≥ 8π²q. This is Theorem H.
- **Blowups:** they are the only topological source of a positive deficit, with budget 12π² each.

**Numbers for the Step-10 cell.** With J − 8π² = −0.069779 and L/4 = 5.954×10⁻⁴:

  δW = 0.017594 + (S_C − 16d)/48 ≥ 0.0176, and B_C ≤ 12π² − 0.0176 ≈ 118.42.

So the cell uses a tiny fraction of its signature budget. The binding constraint is the geometric cost σ, not topology. The perpendicular bolt works by lowering |W⁺| (the ω^⊥ mode of R⁺) more than it raises the scalar and volume terms.

**Two available consistency checks** on the frozen record, each through an integrand distinct from |Ric + g|²:
- the signature relation of §2, B_C − W_C = 12π² − 2d/3;
- the inequality S_C ≥ 16d.

## 9. The mixed-cell interaction question, kept separate from isolated-handle improvement

**Setup.** Let κ(k,ℓ) = inf J/(8π²) over smooth exact-CH cells of topology (k,ℓ), taken over all radii. By residual finiteness, every cell embeds in some cover. Known properties:
- κ is subadditive, since cells with exact collars can be placed in disjoint sub-balls.
- κ is nonincreasing in the ball radius, simply by inclusion. Step-8 monotonicity is not needed for this.
- κ(0,ℓ) = 4ℓ (Theorem H).
- κ(1,0) ≤ 1 − η₁₆ (Step 10).

**Coefficient decomposition.** Applying (2.3) to (8m,7m) cells, and Fekete's lemma, the best cell-built balanced coefficient is

  c_cell = lim_m 4κ(8m,7m)/(36m) = 28/9 + (8/9)κ_∞ + Δ_∞/9,

where:
- κ_∞ = lim κ(k,0)/k ≤ κ(1,0);
- Δ_∞ = lim Δ_m/m, with Δ_m = κ(8m,7m) − κ(8m,0) − 28m ≤ 0.

**Four distinct questions:**
1. **Isolated handle improvement.** Impossible (Theorem H). Any construction that splits into separate pure-blowup and pure-handle exact-CH cells therefore has coefficient ≥ 28/9 + (8/9)κ_∞ ≥ 28/9. Within the separated single-blowup route the range is [28/9, 3.99903].
2. **Multi-blowup interaction.** Is κ_∞ < κ(1,0)?
3. **Blowup–handle interaction.** Is Δ_∞ < 0? By §8, handles add 32π² each to the topological base 8π²q, but add nothing to the deficit budget 12π²k. So Δ < 0 needs a cell that does not split along any exact-CH collar into handle and blowup parts. In such a cell, handle regions host part of a blowup-funded deficit δW, or lower σ for the blowup cores. A concrete mechanism to test is a neck with nearly conformally flat geometry, where W⁺ ≈ 0 locally. Its Ric° and scalar cost enter σ and P directly.
4. **Non-cell metrics.** c_* ≤ c_cell; the all-metric coefficient could lie below any cell construction.

The lower side is untouched by all of this. Feeding δW ≤ 12π²k into the identity only gives 4 − 24k/Q = −4/3 at the balanced ratio, which carries no information. A positive lower constant still comes only from the inherited actual-field c_inh.

## 10. Not re-examined here

- **The Arb enclosure itself.** Only its structural consistency was checked: the regular desingularized forms (the (h₂−h₃)² identity was re-derived) and the bolt Ricci symmetry.
- **Inherited inputs.** These are taken as given: LeBrun's metricwise scalar estimate on X#kCP̄²#ℓ(S¹×S³), its equality case, and the 32π² asymptotic handle cost in I54. Strictness in Theorem H rests on the inherited equality argument. The non-strict bound J ≥ 32π²ℓ needs only the inequality.
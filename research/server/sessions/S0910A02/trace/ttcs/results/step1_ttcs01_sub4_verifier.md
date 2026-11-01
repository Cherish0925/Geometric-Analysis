# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A02/workspace/notes/step1_initial_resolution_and_routes.md",
    "Skills/qiushi-yau26/references/research/20260910.tex",
    "Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md"
  ]
}
```

## Task

Adversarially verify the Step 1 package for Yau Problem 26. Check the quantifier reduction Q_n <=> P_n^+ or P_n^-, the refutation burden, the corrected Min-Oo scope, and especially the Calabi/orbifold scaling claim: Morteza--Viaclovsky remainder O(t^2 rho^2) can become small in g_t-operator norm but the nonzero t*lambda*o obstruction term is order one, so current nonexistence examples do not directly yield delta_sigma->0. Identify any mathematical errors, hidden target changes, source overclaims, or missing assumptions that could materially alter the next research route. Suggest the sharpest next checks that would settle the most important uncertainties.

## Output

## Verification memo: Step 1 package for Yau Problem 26

Verdict up front: on the four mathematical items you asked me to stress-test, the Step 1 reasoning holds. I reproduced the arguments independently against the supplied sources and found no computational error. Below I give the checks, three places where the wording is stronger than the mathematics licenses (each fixable), one strengthening you should add, and the checks that would actually move the research judgment.

---

### 1. The reduction Q_n ⟺ P_n^+ ∨ P_n^−

Independently reproduced and correct, in both directions, per fixed dimension inside the stated manifold class.

- Forward (P_n^σ ⟹ Q_n): with threshold ε, set a=σ−ε, b=σ+ε. The ordering ag≤Ric_g≤bg is exactly "eigenvalues of A_g=g^{-1}Ric_g lie in [a,b]" because A_g is g-self-adjoint; this gives ‖A_g−σId‖_op≤ε pointwise, hence δ_σ(g)≤ε. For σ=+1, a=1−ε>0 since ε<1; for σ=−1, a<b holds. Fine.
- Reverse (Q_n ⟹ P_n^+ ∨ P_n^−): I checked the three quantities. Any nondegenerate [a,b] contains a same-sign closed subinterval [u,v] (uv>0); with μ=(u+v)/2, σ=sign μ, ε=(v−u)/|u+v|, one gets ε∈(0,1) — I verified ε<1 reduces to u>0 (both positive) or v<0 (both negative), both true under uv>0. Then A_{h/|μ|}=|μ|A_h sends eigenvalues in [σ−ε,σ+ε] to exactly [u,v] because |μ|(σ±ε) computes to v and u. So Q_n applies. This actually yields P_n^σ for the single σ tied to the witnessing interval, i.e. slightly more than the disjunction.

The associated statement that a zero-interior interval is not an independent third case is a consequence, not an extra assumption: the same-sign subinterval always exists. This is genuinely settled mathematics, and the scaling identity Ric_{cg}=Ric_g, A_{cg}=c^{-1}A_g that it rests on is correct.

### 2. The refutation burden

Correct. ¬Q_n ⟺ ¬P_n^+ ∧ ¬P_n^−, in the *same* n. Refuting the full target ∀n≥2 Q_n therefore requires one fixed dimension in which *both* sign branches are contradicted, with the two witnessing families allowed on different smooth manifolds. Given the n=2 (uniformization) and n=3 (Hamilton for sign +1; the 3D eigenframe identity K_{ij}=(r_i+r_j−r_k)/2 with ε<1/3 forcing all sec<0, then geometrization) baselines, any refutation lives at n≥4. I re-derived the ε<1/3 threshold and the fact that all sectional curvatures (not just eigenplanes) are <0, since the 3D curvature operator is diagonalized in the Ricci eigenframe and K(π)=⟨R ω,ω⟩ is bounded by the largest eigenvalue. Sound.

### 3. Corrected Min-Oo reading

The correction is right and now matches the retrieved source verbatim. The class 𝒥⁻(n,Λ) is defined by (i) average scalar r<0 and (ii) **d² max|K| < Λ²** with d the diameter — the earlier "r^{-2}max|K|" reading is discarded correctly. The theorem needs n>3 (i.e. n≥4) and gives an Einstein metric of sign −1 *near* the input once the normalized deviation max_{SM}|n p/r − 1| < ε(n,Λ).

Two points I confirmed:
- δ_−(g) small does drive max|n p/r −1| small (Ricci eigenvalues in [−1−δ,−1+δ] give p and r both ≈ −1, ratio → 1 with error O(δ)), so Min-Oo *is* triggerable by sign −1 pinching provided the geometric quantity d²max|K| stays under a fixed Λ.
- Hence the evasion statement is exact: a sign −1 family with δ_−(g_j)→0 that carries no Einstein metric must have d(g_j)²max|K_{g_j}| → ∞, otherwise Min-Oo produces the Einstein metric for large j. Since d²max|K| is not controlled by two-sided Ricci pinching, Min-Oo does not deliver P_n^−. Correct, and the mechanism (Moser iteration needing only diameter + Ricci-lower-bound-controlled isoperimetric/Sobolev constant, not injectivity radius) is faithfully summarized.

### 4. The Calabi/orbifold scaling statement — the load-bearing item

I redid the norm conversion from Morteza–Viaclovsky Lemma 4.2 and it is correct.

Write the defect D = Ric_{g_t} − Λ g_t. Lemma 4.2 gives, in g_cal norm on X^t,
D = t λ χ_t(ρ) o + O(t² ρ²).
The pinching quantity is ‖A_{g_t} − Λ Id‖_op = ‖g_t^{-1} D‖_op, and for a (0,2) tensor D on the core where g_t = t g_cal,
‖g_t^{-1}D‖_{op} = t^{-1} ‖g_cal^{-1}D‖_{op,g_cal},
because raising an index with t g_cal carries the factor t^{-1} (equivalently |D|_{g_t}=t^{-1}|D|_{g_cal}). Applying this term by term:

- Remainder: t^{-1}·O(t²ρ²)=O(tρ²); with ρ≲1 in the core and ρ≲t^{-1/4} in the transition, this is O(t) and O(t^{1/2}) respectively → 0. Matches the note.
- Obstruction: t^{-1}·(tλχ_t)‖o‖ = λχ_t‖o‖ = O(1) in the core (χ_t=1 there). Matches the note.

So when the first obstruction λ≠0, δ_σ(g_t) does **not** tend to 0. Confirmed.

**Strengthening you should record (currently only an upper bound is spelled out).** The order-one conclusion also has a genuine lower bound, not merely a non-vanishing upper estimate. The generator o is a fixed nonzero traceless symmetric 2-tensor with ‖o‖_{op,g_cal} bounded below by a positive constant on a set of positive measure near the exceptional ℙ^{n−1}. Since the remainder is o(1) in g_t-operator norm, for small t
δ_σ(g_t) ≥ c|λ| − o(1) > 0,
uniformly in t. This upgrades "does not tend to zero" to "bounded below by a fixed positive constant," which is what actually excludes these families as pinched inputs. Worth stating because it removes any worry about cancellation between the obstruction and remainder terms.

**Two wording items in this route that outrun the mathematics:**

(a) The conclusion is about the *specific* naïve/refined family g_t, not the smooth resolution manifold. MV Theorem 1.1 excludes Einstein metrics *near g_t* when λ≠0; it says nothing about other metrics on the same smooth manifold. Near-Einstein metrics on a fixed manifold form a large space, so the order-one obstruction of g_t is not evidence that δ_σ cannot be made small on that manifold by a different construction. The note's phrasing "does not provide a Yau26 pinched input" is right if read as "this construction does not," but should not be read as "this manifold is disqualified."

(b) The concrete estimate used is even real dimension m=2n with singularity group Γ_n⊂SU(n) and the Calabi (Ricci-flat Kähler ALE) bubble. Ozuch I is real dimension 4; Biquard is n=4 with ℝ⁴/ℤ₂. The λ-formula λ ∝ ((2−n)/2)Λ − (1/8)⟨R(ω),ω⟩ (MV Prop 3.5) is Kähler-model-specific. Transporting the "order-one defect" conclusion to odd real dimensions or non-SU singularities needs the corresponding bubble estimates; the general-dimension version leans on Yichen Yao's assumptions, which are not the same. This is a range-of-validity note, not an error.

**The decision-relevant addition the package should carry.** The λ=0 escape route the note proposes has a structural tension that the supplied sources already expose:

- λ≠0 ⟹ δ_σ = Θ(1): not pinched (verified above).
- λ=0 ⟹ the naïve metric *is* genuinely C⁰-pinched: with λ=0 the defect is O(t²ρ²) everywhere (and identically Einstein in the orbifold bulk), so δ_σ(g_t)→0 across the whole manifold. But λ=0 is exactly the regime where Einstein metrics tend to *exist*: MV Theorem 1.2 gives an actual Einstein metric on the conformally-compact desingularization when λ=0 and the model is nondegenerate, and the flat Kummer/T⁶/ℤ₃ model (MV Example 1.2, λ=0 automatically) resolves to a Calabi–Yau Einstein metric.

So the orbifold-resolution refutation program is squeezed: the sign of δ_σ→0 forces λ=0, and λ=0 is where the known constructions produce Einstein metrics rather than obstruct them. A refutation via this mechanism must exhibit a compact orbifold with λ=0 at every singular point whose smooth resolution provably carries *no* Einstein metric of any sign — which runs directly against the constructive evidence. This is a sharper statement of "route 2 has two hard missing pieces," and it is the part most likely to redirect effort.

---

### Independent cross-checks I ran (both consistent with the package)

- The 4D Chern–Gauss–Bonnet inequality (dossier Prop "gap"): I verified δ_σ≤ε<1/(1+√3) ⟹ 2χ>3|τ|. Pointwise |s|≥4(1−ε), |E|²≤4ε², dropping 2|W^±|²≥0 gives integrand ≥ (2/3)(1−ε)² − 2ε² > 0 ⟺ (1−ε)²>3ε² ⟺ ε<1/(1+√3). Correct. Consequence for the research: any 4-dimensional pinched candidate for *either* sign must satisfy 2χ>3|τ|, so Hitchin–Thorpe-saturating or -violating manifolds are removed from the candidate pool for both branches — this constrains the orbifold-resolution and the sign −1 routes simultaneously.
- Ozuch Example 1 (Ric(g_i)≥3g_i, ‖Ric−3g_i‖_{L^p}→0, GH-limit S⁴/ℤ₂, no Einstein sequence with that limit): this is an L^p one-sided statement, and "no Einstein sequence sharing the GH limit" is not "no Einstein metric on the smooth manifold." The package uses it correctly to separate L^p-small from C⁰-small and local-nonexistence from global-nonexistence.

### What is still unpinned and materially affects the next route

1. **Classical hypotheses.** Anderson 1989 Corollary B(4) and Ye 1993 were not retrieved in theorem form. Their exact hypotheses (whether they need a volume lower bound, injectivity-radius bound, or a ‖∇Ric‖ bound in addition to pinching) decide whether P_n^σ is already essentially known under supplementary geometric data or genuinely open under Ricci pinching alone. Until these are read, the frontier "n≥4, pure Ricci pinching" cannot be located precisely.
2. **The damage-zone conversion factor.** The core (t^{-1}) and orbifold-bulk (factor 1) conversions are clean, but the interpolating region has a position-dependent factor between t^{-1} and 1. A fully written region-by-region unweighted computation of δ_σ(g_t) — using MV's weight w (∼t^{1/2} core, ∼|z| bulk, ∼r t^{1/2} transition) converted to operator norm — is still to be produced. The leading O(1) core term is robust to this, so the qualitative conclusion stands, but any quantitative statement about the transition should wait for that computation.

### Sharpest next checks (ordered by how much they would change the judgment)

1. **Resolve the λ=0 dichotomy concretely.** Determine whether there exists a compact Einstein orbifold with Λ≠0 satisfying n⟨R(ω),ω⟩+2(n−2)R=0 at every singular point (first obstruction vanishing) whose smooth resolution carries no Einstein metric of any sign. If every such λ=0 model admits an Einstein resolution (as Kummer/Calabi–Yau and MV Thm 1.2 suggest), the orbifold-resolution refutation mechanism is exhausted and effort should move. This is the single most informative computation.
2. **Recover Anderson B(4) and Ye 1993 verbatim** and record whether their thresholds depend on anything beyond n. This fixes whether the sign +1 branch in n≥4 is open under pure pinching.
3. **Sign −1 branch beyond Min-Oo.** Test whether a fixed no-Einstein 4-manifold can carry a family with δ_−(g_j)→0 and d²max|K|→∞ simultaneously. Note the 4D inequality already forces 2χ>3|τ| on any such family, so the candidate must be a no-Einstein manifold that nonetheless satisfies 2χ>3|τ| (needing a Seiberg–Witten/LeBrun-type obstruction rather than Hitchin–Thorpe), and must additionally collapse curvature-wise (d²max|K|→∞). Enumerate whether any known no-Einstein 4-manifold meets all three at once; if none can, the sign −1 orbifold/collapse route is heavily constrained.
4. **Convert "GH-limit is an Einstein orbifold" into "no Einstein on M."** Check, via Anderson–BKN plus Cheeger–Naber codimension-4, whether δ_σ→0 on a noncollapsed sequence forces subconvergence to an Einstein orbifold, and whether the target smooth topology can be arranged incompatible with carrying any Einstein metric. This is the actual gap between the degeneration theory and a Yau26 refutation, and it is where a genuinely new global obstruction would have to enter.

Net: the four items are correct, the one substantive addition is the explicit uniform lower bound δ_σ(g_t)≥c|λ|−o(1)>0, and the most consequential open question is the λ=0 dichotomy, which currently points against the orbifold-resolution refutation and toward existence.
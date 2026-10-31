# Step 7: Local vs Global Rigidity and the Conformal-Kähler Obstruction

## Summary

This note develops three analytical tools and one structural obstruction for the
negative-branch four-dimensional Yau 26 analysis.

### Tools developed
1. **Bochner formula verification** on Einstein 4-manifolds: the calibrated
   two-eigenvalue W⁺ profile with constant |W⁺| = 1/(2√6) is consistent with
   the Bochner identity and gives |∇W⁺|² = 1/24 > 0 (not parallel).

2. **Noncollapsed convergence chain**: harmonic radius → W²,p → smooth Einstein
   limit → constant |W⁺| → two-eigenvalue profile.

3. **Volume-random basepoint argument**: eliminates spatial escape for noncollapsed
   regions with vanishing normalized deficit.

### Structural obstruction found
**The local Derdziński conformal-Kähler route does NOT yield a contradiction on
noncompact smooth Einstein limits.** The conformal factor f satisfying Δf = −f/2
can be nonconstant on noncompact manifolds. On compact manifolds, the Stokes
theorem forces f = const → Kähler → |W⁺|² = 2/3, contradiction. The negative-
branch argument is inherently global.

---

## 1. Bochner formula for |W⁺|² on Einstein 4-manifolds

On a 4-dimensional Einstein manifold (∇·W⁺ = 0), the scalar Bochner formula is:
$$
\frac12 \Delta|W^+|^2 = |\nabla W^+|^2 + \frac{s}{3}|W^+|^2 - 4\,\mathrm{tr}(W^+)^3.
$$

For trace-free W⁺ with eigenvalues α ≥ β ≥ γ (α + β + γ = 0):
$$
\mathrm{tr}(W^+)^3 = \alpha^3 + \beta^3 + \gamma^3 = 3\alpha\beta\gamma.
$$

**Verification on ℂℍ²** (s = −4, Kähler-Einstein with eigenvalues (1/3, 1/3, −2/3)):
- |W⁺|² = 2/3, tr(W⁺)³ = −2/9
- (s/3)|W⁺|² − 4·tr(W⁺)³ = (−4/3)(2/3) − 4(−2/9) = −8/9 + 8/9 = 0 ✓ (W⁺ parallel)

**At the calibrated target** (s = −4, eigenvalues (1/12, 1/12, −1/6)):
- |W⁺|² = 1/24, tr(W⁺)³ = −1/288
- |∇W⁺|² = −(s/3)|W⁺|² + 4·tr(W⁺)³ = (4/3)(1/24) + 4(−1/288) = 1/18 − 1/72 = **1/24 > 0**

This means: the calibrated two-eigenvalue profile with constant norm is **consistent**
with the Bochner formula but W⁺ is **not parallel**. The metric is not locally
symmetric. An Einstein 4-manifold with this exact Weyl profile can exist.

**General eigenvalue family**: Parametrize α = a+ε, β = a−ε, γ = −2a with
6a² + 2ε² = 1/24. Then:
$$
|\nabla W^+|^2(a) = -96a^3 + \frac{a}{2} + \frac{1}{18}.
$$
At a = 1/12 (two-eigenvalue): |∇W⁺|² = 1/24. At a = 0: |∇W⁺|² = 1/18.
No real root with ε² ≥ 0 gives |∇W⁺|² = 0 except W⁺ = 0.

---

## 2. Conformal-Kähler analysis and the compact/noncompact distinction

### Derdziński's theorem (modern form)
On an Einstein 4-manifold, if W⁺ is nonzero and has at most two distinct eigenvalues
at every point of an open set U, then the metric is locally conformally Kähler on U.
That is, there exists f > 0 with f²g Kähler.

### Conformal weight and eigenvalue matching
For g̃ = f²g Kähler: W⁺_g = f² W⁺_g̃ (conformal weight in 4D), and the Kähler
metric has W⁺ eigenvalues (s̃/6, −s̃/12, −s̃/12). So:
$$
|W^+_g|^2 = f^4\cdot\frac{s̃^2}{24}.
$$

For constant |W⁺_g|² = 1/24: f⁴s̃² = 1, so f²|s̃| = 1.

With f²s̃ = −1 (negative Kähler branch): eigenvalues of W⁺_g are (−1/6, 1/12, 1/12),
matching the calibrated target exactly.

### The conformal factor equation
The conformal scalar curvature relation gives:
$$
s̃ = f^{-2}\bigl(s_g - 6f^{-1}\Delta_g f\bigr).
$$
Substituting s_g = −4 and f²s̃ = −1:
$$
-4 - 6\frac{\Delta f}{f} = -1 \implies \Delta f = -\frac{f}{2}.
$$

### The compact/noncompact obstruction

**On a compact Einstein manifold** with Ric = −g: if f > 0 satisfies Δf = −f/2,
then by Stokes:
$$
0 = \int_M \Delta f\,dV = \int_M \bigl(-\tfrac{f}{2}\bigr)\,dV = -\tfrac{1}{2}\int_M f\,dV < 0.
$$
Contradiction. Therefore f = const, the metric is Kähler, and |W⁺|² = s²/24 = 2/3.
But the calibrated target has |W⁺|² = 1/24. **Contradiction.**

**On a noncompact smooth Einstein limit**: no Stokes theorem for non-compactly-
supported f. Nonconstant solutions to Δf = −f/2 exist (cf. eigenfunctions on
hyperbolic manifolds). The conformally Kähler structure with constant |W⁺|² = 1/24
is locally possible. **No local contradiction from Derdziński alone.**

### Conclusion
The negative-branch argument is **inherently global**. The compact Armstrong/LeBrun
mechanism (compactness + Stokes + Taubes exceptional-sphere area) cannot be replaced
by purely local analysis on noncompact pointed limits.

---

## 3. Noncollapsed convergence chain

The Strategist identified the Cheeger-Naber harmonic-radius bridge as the key tool.

### Step A: Harmonic radius under bounded Ricci
**Cheeger-Naber Remark 1.11 + Theorem 1.13** (arxiv:1406.6534): Under |Ric| ≤ 3
and Vol(B₁(p)) > v > 0 on a 4-manifold:
$$
\mathrm{Vol}\bigl(T_r(\{x\in B_1(p): r_h(x)\le r\})\bigr) \le C(v)\,r^4.
$$
This holds under bounded Ricci alone (not Einstein). The set where harmonic radius
is ≤ r has volume ≤ C r⁴. In particular, outside a set of measure ≤ ε, the harmonic
radius is ≥ r₀(ε, v).

### Step B: C¹,α convergence on harmonic charts
In harmonic coordinates on a ball of radius r_h:
- g_{ij} is C^{1,α} ∩ W^{2,q} for all α < 1 and q < ∞ (standard harmonic-coord regularity)
- The metric components satisfy ||g_{ij} − δ_{ij}||_{C⁰} + r||∂g||_{C⁰} ≤ 10⁻³

For a sequence g_i with Ric(g_i) + g_i → 0 uniformly and harmonic radius ≥ r₀:
the sequence is bounded in C^{1,α}(B_{r₀/2}) for each α < 1. By Arzelà-Ascoli,
a subsequence converges in C^{1,α'} for α' < α.

### Step C: W²,p convergence and smooth limit (Strategist's key observation)
In harmonic coordinates, the Ricci tensor is:
$$
\mathrm{Ric}_{ij} = -\frac12 g^{kl}\partial_k\partial_l g_{ij} + Q(g, \partial g),
$$
where Q is algebraically quadratic in ∂g. Under C^{1,α} convergence of g_i to g_∞:
- Q(g_i, ∂g_i) → Q(g_∞, ∂g_∞) in C^α
- Ric(g_i) + g_i → 0 uniformly means −(1/2)g^{kl}∂²g_{ij} → g_{ij} − Q(g,∂g)
- The RHS converges in C^α
- Interior Schauder estimates give C^{2,α} convergence of g

The limit g_∞ satisfies Ric(g_∞) = −g_∞ (Einstein). By standard bootstrap:
smooth limit.

### Step D: Passage of curvature-ratio remainder
With C²,α convergence, W⁺ converges in C^α pointwise. From the Cauchy-Schwarz
remainder ∫_{B_R(p)}(s+8√6|W⁺|)²dμ → 0 and the C⁰ convergence of both sides:
$$
s_\infty + 8\sqrt{6}\,|W^+_\infty| = 0 \quad\text{on the limit ball}.
$$
Since s_∞ = −4 (from Ric = −g in 4D): |W⁺_∞| = 1/(2√6) **constant** on the limit.

---

## 4. Volume-random basepoint argument

### Setup
Let F_i be a nonnegative local deficit density on M_i (e.g., F_i = (s_i+4)² +
(|W⁺_i|−1/(2√6))² + |E_i|²) with ∫F_i/Vol(M_i) → 0.

### The averaging principle
For R > 0 fixed and a uniformly random basepoint p ∈ M_i:
$$
\mathbb{E}\!\left[\int_{B_R(p)} F_i\,d\mu\right]
= \frac{1}{\mathrm{Vol}(M_i)}\int_{M_i} F_i(x)\,\mathrm{Vol}(B_R(x))\,d\mu(x).
$$

Under Ric(g_i) ≥ −(3+δ_i) (from near-Einstein): Bishop-Gromov gives
Vol(B_R(x)) ≤ V₋₃(R) = C(R) for all x. Therefore:
$$
\mathbb{E}\!\left[\int_{B_R(p)} F_i\,d\mu\right]
\le \frac{C(R)}{\mathrm{Vol}(M_i)}\int_{M_i} F_i\,d\mu \to 0.
$$

This controls **neighborhoods**, not merely the deficit at the selected point. It
requires no diameter bound.

### Consequence
By Markov's inequality: for any η > 0, the set of basepoints p with
∫_{B_R(p)} F_i > η has volume fraction → 0. In particular, the **typical** R-ball
has arbitrarily small total deficit.

### Noncollapsed fraction
Suppose, for contradiction, that a positive fraction τ > 0 of the total volume
of M_i consists of points p with Vol(B₁(p)) ≥ v > 0. Then for large i,
a τ/2-fraction has both:
- Vol(B₁(p)) ≥ v (noncollapsed)
- ∫_{B₁(p)} F_i < ε (small deficit)

On such balls: Cheeger-Naber gives harmonic radius ≥ r₀(v) on most of the ball.
The W²,p chain gives a smooth Einstein limit with constant |W⁺| = 1/(2√6).
Derdziński gives locally conformally Kähler.

---

## 5. The global mechanism and the remaining gap

### What works
The chain: noncollapsed ball → harmonic radius → W²,p → smooth Einstein limit →
constant |W⁺| → two-eigenvalue W⁺ (on the limit) → Derdziński → conformally
Kähler locally.

### What fails
On the noncompact limit: the conformal factor f satisfying Δf = −f/2 need not be
constant. The conformally Kähler structure IS compatible with |W⁺|² = 1/24.
**No local contradiction.**

### What works globally
On the **original compact** manifold M_i:
1. Near-equality forces the SW spinor Φ_i to define an approximate almost-Kähler
   form ω_i (from Prop 2.4 quantitative version).
2. The sign choice in Prop 3.2 gives [c₁(X)]⁺·E_j ≤ 0, hence [ω_i]·E_j ≈ 0.
3. Near-equality forces [c₁(X)]⁺·E_j → 0 for all j (from multi-monopole average).
4. Taubes' theorem on the symplectic manifold (M_i, ω_i) produces a pseudo-
   holomorphic sphere representing E_j with area = [ω_i]·E_j → 0.
5. Gromov compactness for pseudo-holomorphic curves: non-constant curves in a
   fixed homology class have a positive lower bound on energy (area). If this
   lower bound doesn't degenerate, area → 0 contradicts area > 0.

### The remaining gap
The Taubes theorem requires an **exact** symplectic structure, not an approximate
one. The near-equality analysis gives an approximate almost-Kähler form whose
closedness defect is controlled by the Ricci defect. The precise gap is:

**Can the approximate almost-Kähler structure from near-equality be promoted to
an exact symplectic structure on M_i for which the Taubes area argument applies?**

This would require either:
(a) A quantitative Taubes theorem for approximately symplectic manifolds, or
(b) A direct construction of an exact symplectic form near the approximate one
    (Moser stability type argument), or
(c) An alternative global argument using the SW equations directly on M_i
    (without invoking symplectic geometry).

Route (c) is closest to LeBrun's own approach: the SW equations on M_i give
φ_i = σ(Φ_i) = −iF_{A,i}⁺, which is an exact self-dual 2-form. The norm |φ_i|
is controlled by the SW Weitzenböck formula. Near-equality forces |Φ_i|² to be
approximately constant and the form φ_i to lie approximately in the lowest W⁺
eigenspace. The topological constraint comes from [c₁(L)]·[E_j], which is an
integer and hence stable under perturbation. The area integral ∫_{E_j} (−iF_A/2π)
is a Chern number, hence an integer. This stability of integer invariants may
provide the needed rigidity without requiring an exact symplectic form.

---

## 6. S0910A03 Weyl profile filter on collapse models

S0910A03 (msg #218, #219) observes that product hyperbolic surfaces Σ_g × Σ_{g'}
with degenerating metric IS a valid Ric = −g collapse model (short geodesic gives
collapse), but has |W⁺| = 2/√6 (Kähler product value), excluded by the calibrated
profile |W⁺| ≈ 1/(2√6).

**All known collapse models under Ric = −g are excluded by the Weyl profile.**

The open question: are there unknown collapse models with |W⁺| ≈ 1/(2√6)? From
the Bochner analysis, such models would need:
- s = −4 constant
- |W⁺| = 1/(2√6) approximately constant  
- |∇W⁺|² ≈ 1/24 (from Bochner)
- Locally conformally Kähler structure
- A collapsing direction compatible with these constraints

The conformal factor equation Δf = −f/2 on a collapsing Einstein manifold would
need f to oscillate (to avoid Stokes contradiction on any embedded compact region).
This is a strong constraint that may be incompatible with the smooth collapse
structure.

---

## 7. Updated route assessment

### Negative branch (four-dimensional LeBrun families)
**Status**: The near-equality regime k/A → 1/3 is the only remaining boundary.
The local analysis chain is well-developed but hits the compact/noncompact wall.
The global mechanism (Taubes + integer invariants + Stokes) is the natural path
but needs a quantitative formulation.

**Key advance this step**: The conformal-Kähler analysis definitively shows that
the local Derdziński route is insufficient. This corrects the Step 6 direction.

**Next work**: Develop the global argument on M_i using integer invariants of the
SW solution. The topological stability of Chern numbers may close the gap without
needing exact symplectic geometry.

### Positive branch (all dimensions)
**Status**: S0910A02 has the noncollapsed theorem (Vol ≥ v → Einstein existence)
but the volume lower bound is missing. S0910A03's Weyl filter suggests that
collapse models may be constrained, but this is four-dimensional only.

**Next work**: Determine whether positive pinching + diameter control implies a
volume lower bound in special cases (simply connected, or with topological
constraints from the Ricci pinching).

---

## Files and references
- Verification script: `workspace/scripts/step7_bochner_conformal_kahler.py` (all checks pass)
- LeBrun 2001 source: `Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`
- Cheeger-Naber: `Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md`
- Step 6 tensor algebra: `workspace/scripts/step6_tensor_slack_algebra.py`
- Peer confirmation: S0910A03 msgs #218, #219

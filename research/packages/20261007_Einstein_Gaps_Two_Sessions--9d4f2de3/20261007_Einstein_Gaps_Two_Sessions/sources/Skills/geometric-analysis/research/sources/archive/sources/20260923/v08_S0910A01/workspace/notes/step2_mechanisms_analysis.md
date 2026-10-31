# Step 2: Mathematical Mechanisms for Yau Problem 26
## Branch Logic, Source Corrections, Quantitative Bounds, Open Bottlenecks

### 1. Corrected Min-Oo Hypothesis

**Key correction:** The Min-Oo 1990 theorem (JDG 32, 457-472) uses the condition
d²·max|K| < Λ², NOT r⁻²·max|K| < Λ².

Evidence: In §3, the normalization reads "max|K(0)| = 1, d(0) < Λ" (line 246 of the source). The OCR garbles "d" as "rf" in the introduction. The scale-invariance check confirms: under g → λg, d → λ^{1/2}d and K → λ⁻¹K, so d²·max|K| → d²·max|K| (invariant). Meanwhile r⁻²·max|K| → λ·(r⁻²·max|K|) (NOT invariant).

**Full Min-Oo Theorem:** For n > 3 and Λ > 0, there exists ε(n,Λ) > 0 such that if (M^n,g) is compact with:
- r < 0 (negative average scalar curvature)  
- d² max|K| < Λ² (bounded diameter-curvature product)
- max_{SM} |np/r - 1| < ε(n,Λ) (Ricci close to average in normalized sense)

then M admits an Einstein metric ḡ with ρ(ḡ) = -1.

**Escape mechanisms for counterexamples:** A sequence with δ_-(g_j) → 0 must leave the class J⁻(n,Λ) for EVERY Λ. This means d_j² max|K_j| → ∞, which can happen via:
1. max|K_j| → ∞ with d_j bounded (curvature blow-up, especially Weyl)
2. d_j → ∞ with max|K_j| bounded (diameter growth)
3. Both growing simultaneously

The diameter-growth escape is a genuinely different mechanism from curvature blow-up. For negative Ricci, Myers' theorem does not bound diameter, so d → ∞ is possible while Ricci eigenvalues stay near -1.

Source: Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md

---

### 2. Fundamental Branch Asymmetry

**Positive branch (σ = +1):** Ricci eigenvalues in (1-δ, 1+δ) imply Ric > 0, hence:
- Myers: diam(M) ≤ π√(3/(1-δ))
- Bishop-Gromov: Vol(M) ≤ 24π²/(1-δ)² (for n=4)
- Positive scalar curvature: s > 0
- Witten vanishing: SW invariants vanish

**Negative branch (σ = -1):** Ricci eigenvalues in (-1-δ, -1+δ) give:
- No Myers bound: diameter unconstrained
- No volume upper bound from Bishop-Gromov
- Negative scalar curvature: s < 0
- SW invariants can be non-trivial (no obstruction)

This asymmetry is the central structural feature of the problem.

---

### 3. Positive Branch: Elimination of Known No-Einstein 4-Manifolds

**3a. LeBrun manifolds (X#k CP̄², 2A/3 < k < A where A = c₁²(X)):**

These have non-trivial SW invariants. By Witten's vanishing theorem, they cannot admit any metric with s > 0 everywhere. Since δ_+(g) < 1 implies s > 0, we conclude:

**δ_+(g) ≥ 1 for ALL metrics g on LeBrun no-Einstein manifolds.**

LeBrun manifolds are entirely excluded from the positive branch without any quantitative argument.

**3b. Hitchin-Thorpe violating manifolds (#_m CP², m ≥ 3):**

These satisfy χ(#_m CP²)=m+2 and τ=m, hence 2χ-3τ=4-m. Thus the Hitchin--Thorpe violation begins at m≥5; the m=4 equality and m=3 strict case require separate handling. The dossier's Proposition says that if δ_σ(g) < 1/(1+√3), then 2χ > 3|τ|. Therefore the Chern--Weil gap gives:

**δ_+(g) ≥ 1/(1+√3) = (√3-1)/2 ≈ 0.366 for ALL metrics g on #_m CP² with m ≥ 4, with m=4 included as equality and m≥5 as violation.**

This is a UNIFORM bound across all HT-violating manifolds, independent of m.

**3c. Combined positive branch conclusion (dimension 4):**

Every currently known mechanism producing no-Einstein 4-manifolds leads to
δ_+ bounded away from 0. The known mechanisms are:
- HT violation: δ_+ ≥ 0.366 (universal)
- SW/LeBrun obstruction with strict HT: δ_+ ≥ 1 (no positive scalar curvature)

Therefore: **No known no-Einstein 4-manifold can serve as a positive-branch counterexample.** P_4^+ is consistent with all current evidence.

---

### 4. Negative Branch: Quantitative LeBrun Bound

For LeBrun manifolds M = X#k CP̄² with the negative branch:

**Theorem (derived in this step):** For any metric g on M with δ_-(g) = δ < 1/(1+√3):

(A) ∫|E|² dV ≥ 8π²(k - 2A/3)  [from LeBrun + Chern-Gauss-Bonnet]
(B) V ≤ 4π²(A-k)/[2(1-δ)²/3 - 2δ²]  [from self-dual CGB + |W⁺|² ≥ 0]
(C) ∫|E|² dV ≤ 4δ²V  [from |E|² ≤ 4δ² pointwise]

Combining (A), (B), (C):
8π²(k-2A/3) ≤ 4δ² · 4π²(A-k)/[2(1-δ)²/3 - 2δ²]

**Exact formula (TTCS-verified):** Setting q = k - 2A/3 > 0 and B = A - k > 0, the full derivation gives the quadratic
(A-q)δ² + 2qδ - q > 0, with positive root:

**δ_- ≥ √q / (√A + √q)**

This is equivalent to δ₀² ~ q/(3B) as q/B → 0, but the exact formula is cleaner. 

Examples (verified): A=100, k=67, q=1/3: δ₀ ≈ 0.055; A=10000, k=6668, q=4/3: δ₀ ≈ 0.0114.

For the minimum LeBrun manifold (k_min = ⌊2A/3⌋+1, q = O(1)):
δ₀ = O(A^{-1/2}) → 0 as A → ∞

**Critical observation:** The lower bound on δ_- for each FIXED LeBrun manifold is positive, but it tends to 0 as c₁²(X) → ∞ with k/A → 2/3. This is a NECESSARY condition for counterexamples, not a construction.

**Energy budget constraint (from TTCS Generator):** Any successful construction must be NEAR ANTI-SELF-DUAL. From CGB, the W⁺ integral ∫|W⁺|² is constrained to a residual budget near the critical topology. This adds a global constraint beyond pointwise Ricci control.

---

### 5. Varying-Manifold Possibility (from the Strategist)

The negation of Q_n allows the manifold M to vary along the sequence. A refutation would provide: for all ε > 0, some (M_ε, g_ε) with δ_σ(g_ε) ≤ ε and Ein(M_ε) = ∅. The manifold itself can depend on ε.

**Positive branch:** Even with varying manifolds, the HT-violation bound δ_+ ≥ 1/(1+√3) is universal. And SW-obstructed manifolds all have δ_+ ≥ 1. So the positive branch is protected.

**Negative branch:** The LeBrun bound δ ≥ C/√A → 0 for varying manifolds. This does NOT prevent a counterexample sequence. But constructing such a sequence requires:
(a) A sequence of LeBrun manifolds X_j#k_j CP̄² with c₁²(X_j) → ∞
(b) Metrics g_j on each with δ_-(g_j) → 0
(c) The metric construction is the unsolved problem

---

### 6. Jäckel's Result and Its Relation to Yau 26

Jäckel (JGA 36, 2026): Removes diameter/volume/injrad dependence from Min-Oo-type theorems, but retains:
- Negative SECTIONAL curvature (sec ≤ -K < 0)
- Ricci derivative bound (∇Ric bounded)
- Thin-part exactness condition

These are stronger than Ricci pinching alone. The gap between Jäckel and Yau 26 is:
**Yau 26 only controls Ric, not sec or ∇Ric.** The Weyl curvature and Ricci gradient are free under pure Ricci pinching.

---

### 7. Open Bottlenecks (Prioritized)

**B1 (Negative-branch metric construction):** Can we construct metrics with δ_-(g) arbitrarily small on no-Einstein manifolds? The concrete target (from TTCS): build a metric on P = CP̄²\B⁴ with:
  - Two-sided negative Ricci: ‖Ric_p + p‖_op ≤ ε
  - Boundary Cauchy data matching the hyperbolic background
  - Controlled volume (not divergent in ε)
  - Near anti-self-dual energy budget compatible with Chern-Weil
Lohkamp gives one-sided Ric < 0 but not two-sided. DeTurck is local. Bolt-type models (Bianchi IX ansatz) are a concrete ODE family to test.

**B1' (Monopole gap):** Can the full 2^k monopole classes from LeBrun's proof produce a UNIFORM δ gap independent of A? The single-class bound gives only δ ≥ O(A^{-1/2}). If all classes combined give a uniform positive lower bound, counterexamples are excluded.

**B2 (Positive-branch characterization):** Is there ANY closed 4-manifold with Ric > 0 (hence δ_+(g) < 1) and no Einstein metric of any sign? Current evidence says no, but this is not proved.

**B3 (Dimension ≥ 5):** No closed manifold of dimension ≥ 5 is known to have no Einstein metric of any sign. Both branches are wide open in high dimensions.

**B4 (Two-sided Lohkamp):** Does Lohkamp's h-principle extend to the two-sided relation (-1-ε)g < Ric < (-1+ε)g? The formal jet test is necessary but not sufficient due to global Chern-Weil obstructions (even if local fibers are nonempty). The answer would settle the negative branch in dimension 4.

**B5 (Anderson 1989 source):** Exact text of Anderson's Corollary B(4) still not retrieved. This is needed to understand what additional conditions (beyond Ricci) the classical theory requires.

---

### 8. Structural Summary

The problem decomposes by sign:
- **P_n^+** (positive): Strongly protected in dimension 4 by SW/HT. Likely true.
- **P_n^-** (negative): Open and harder. No uniform δ bound in dim 4. The key question is B1.
- **P_n (general):** True iff both branches hold (dossier: Q_n ↔ P_n^+ ∨ P_n^-)

For a complete answer:
- To PROVE Q_n: prove both P_n^+ and P_n^- for all n
- To REFUTE Q_n: refute BOTH P_n^+ and P_n^- in some fixed n
- A single-branch refutation does not refute Q_n

The varying-manifold structure means: negative-branch counterexamples from varying LeBrun manifolds with c₁² → ∞ cannot be ruled out by our current quantitative bounds. But construction of metrics with δ_- → 0 on these manifolds remains the central open problem.

### Source References
- Min-Oo 1990: Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md
- LeBrun 1995: Knowledge/objects/papers/4-Manifolds-without-Einstein-Metrics--c95911daf050--cd7839b9cc3d/object.md
- Lohkamp survey: Knowledge/objects/papers/RICCI-CURVATURE-MODULO-HOMOTOPY--ec0fb68c286e--9206a3ce3fba/object.md
- Dossier: Skills/qiushi-yau26/references/research/20260910.tex

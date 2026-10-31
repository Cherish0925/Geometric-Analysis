# ERRATUM added in Step 3

This Step 2 note contains load-bearing errors in the LeBrun negative-Einstein arithmetic and in the positive-collapse interpretation. Do **not** use its Lemma 2, the claim “no negative Einstein for all 0<k<A”, the claimed 1/sqrt(A) weakening at fixed ratio, or the slogan that tight positive pinching excludes collapse. The corrected source-checked analysis is in `Sessions/S0910A02/workspace/notes/step3_corrections_lebrun_and_collapse.md`, with computation `Sessions/S0910A02/workspace/scripts/step3_corrected_lebrun_bounds.py` and data `Sessions/S0910A02/workspace/data/step3_corrected_lebrun_bounds.json`.

# Step 2: Sign Census, Dichotomy, and Route Assessment for Yau Problem 26

Session: S0910A02, Agent2/Constructor, Step 2 Explore.

## Purpose

Turn the Step 1 research state and the Strategist's sign-blind insight into precise
mathematical objects: formal lemma statements, the Einstein sign census for
dimension 4, the negative branch dichotomy, the dimension ≥ 5 obstruction gap,
and an updated route evaluation. These should be reusable by Agents 3 and 4 and
form the backbone for deciding whether the research moves toward existence
(proof of Q_n for some/all n) or refutation.

---

## I. Sign-Blind Chern-Weil Lemma (dimension 4)

**Lemma 1 (Sign-blind strict HT from pinching).**
Let (M⁴, g) be a closed oriented Riemannian 4-manifold with δ_σ(g) ≤ ε < 1/(1+√3) for either σ = +1 or σ = −1. Then

    2χ(M) > 3|τ(M)|.

*Proof (from dossier Proposition 3.2).* Write Ricci eigenvalues as σ + eᵢ with |eᵢ| ≤ ε. Then:
- Scalar curvature: |s| ≥ 4(1 − ε), so s²/24 ≥ (2/3)(1 − ε)².
- Traceless Ricci: |E|² = Σ(eᵢ − ē)² ≤ Σeᵢ² ≤ 4ε².
- CGB formula: 2χ ± 3τ = (1/4π²) ∫(2|W±|² + s²/24 − |E|²/2) dV.
- Drop the non-negative Weyl terms: 2χ ± 3τ ≥ Vol/(4π²) · [(2/3)(1−ε)² − 2ε²].
- The bracket is (2/3 − 4ε/3 + 2ε²/3 − 2ε²) = 2/3 − 4ε/3 − 4ε²/3.
- At ε = 1/(1+√3) ≈ 0.366, the bracket equals 0. For ε < 1/(1+√3), it is positive.
- Since Vol > 0 on a closed manifold, both 2χ+3τ > 0 and 2χ−3τ > 0.   □

**Key structural consequence.** This is sign-blind: it holds for BOTH σ = +1 and σ = −1. The s² term (not s) enters CGB. Therefore:

> Any manifold that violates or saturates Hitchin-Thorpe (2χ ≤ 3|τ|) cannot
> support arbitrarily tight Ricci pinching from EITHER direction.

This immediately eliminates #₅CP² (χ = 7, τ = 5, 2χ − 3τ = −1) and all
HT-violating connected sums from being counterexamples to P₄^σ for any σ.

---

## II. Einstein Sign Census for Dimension 4

For a closed oriented 4-manifold M to serve as a counterexample to P₄⁻ or P₄⁺,
M must carry tight Ricci pinching (δ_σ → 0) AND have no Einstein metric of
any sign. We census the known mechanisms per Einstein sign.

### II.A. Positive Einstein (λ > 0)

**Exclusion mechanism:** Seiberg-Witten theory.

If M has a non-trivial SW basic class, it admits no metric of positive scalar
curvature. Since a positive Einstein metric has s = 4λ > 0, such M has no
positive Einstein metric. This is a gauge-theoretic/topological obstruction,
NOT an integral curvature inequality.

**Compatibility with tight negative pinching:** A metric g with Ric ≈ −g has
s ≈ −4 < 0. Negative scalar curvature is compatible with non-trivial SW
invariants. So the λ > 0 exclusion coexists with tight negative pinching.

**Compatibility with tight positive pinching:** A metric g with Ric ≈ +g has
s ≈ +4 > 0. But non-trivial SW invariants forbid ANY positive scalar curvature
metric. So tight positive pinching is INCOMPATIBLE with the SW obstruction.

**Conclusion for positive branch counterexamples:** LeBrun manifolds have
non-trivial SW → no Ric > 0 at all → δ₊ ≥ 1 on these manifolds. Therefore
LeBrun manifolds CANNOT serve as counterexamples to P₄⁺.

**S0910A01 finding:** All known no-Einstein 4-manifolds have δ₊ bounded away
from 0 (LeBrun: δ₊ ≥ 1; HT-violators: δ₊ ≥ 1/(1+√3) ≈ 0.366). P₄⁺ is
consistent with all known evidence.

### II.B. Zero Einstein (λ = 0)

**Exclusion mechanism:** Ricci-flat holonomy constraints.

Closed Ricci-flat 4-manifolds have holonomy in SU(2) or {1}. They are:
- Flat: quotients of T⁴
- Hyperkähler: K3 and its quotients

LeBrun manifolds M = X # k\bar{CP²} with X minimal of general type are never
diffeomorphic to K3, T⁴, or their quotients (wrong Betti numbers, wrong
intersection form). So λ = 0 is excluded by topology.

**Compatibility with tight pinching:** The λ = 0 exclusion is topological and
does not constrain δ_σ of the input metric.

### II.C. Negative Einstein (λ < 0) — THE CRITICAL SIGN

**Exclusion mechanism:** Seiberg-Witten + Chern-Gauss-Bonnet integral inequality.

**Lemma 2 (LeBrun negative Einstein exclusion).**
Let M be a closed oriented 4-manifold with b⁺₂(M) ≥ 2 and SW basic class κ.
If M admits a negative Einstein metric h (Ric_h = λh, λ < 0), then:

    (i)  16λ²·Vol(M,h) ≥ 32π²κ²     [SW inequality for any metric]
    (ii) 8π²(2χ+3τ) = 4∫|W⁺_h|² + 16λ²Vol/3   [CGB for Einstein, E=0]

Combining (i) and (ii):
    4∫|W⁺_h|² = 8π²(2χ+3τ) − 16λ²Vol/3
    ≤ 8π²(2χ+3τ) − 32π²κ²/3    [using (i)]

For ∫|W⁺|² ≥ 0 to hold:
    8π²(2χ+3τ) ≥ 32π²κ²/3
    ⟹  3(2χ+3τ) ≥ 4κ²

*Application to LeBrun manifolds:* For M = X # k\bar{CP²} with c₁²(X) = A:
- 2χ(M) + 3τ(M) = A − k
- κ² = A − k  (basic class square)
- The bound: 3(A−k) ≥ 4(A−k) ⟹ 3 ≥ 4, which is FALSE when A > k.

**Therefore:** No negative Einstein metric exists on M when 0 < k < A.   □

**Nature of this mechanism:** This is an INTEGRAL CURVATURE INEQUALITY mechanism.
It combines:
- The Seiberg-Witten inequality ∫s² ≥ 32π²κ² (applied to the hypothetical Einstein metric)
- The CGB identity (topological = ∫ curvature quantities)

The contradiction arises because:
- Einstein forces ∫|E|² = 0 (removing the absorbing term)
- SW forces ∫s² ≥ 32π²κ² (large scalar curvature integral)
- CGB then forces ∫|W⁺|² < 0, contradiction

**For non-Einstein input metrics:** ∫|E|² > 0, which can absorb the negative term.
Specifically, the computation becomes:

    2∫|W⁺|² = 4π²(A−k) − ∫s²/24 + ∫|E|²/2

The SW bound ∫s² ≥ 32π²(A−k) means ∫s²/24 ≥ 4π²(A−k)/3. So:

    2∫|W⁺|² ≤ 4π²(A−k)(1 − 1/3) + ∫|E|²/2 = 8π²(A−k)/3 + ∫|E|²/2

This is satisfied as long as ∫|E|²/2 ≥ −8π²(A−k)/3, which is automatic.
So the LeBrun contradiction does NOT directly prevent tight pinching on M.

### II.D. Summary: What excludes each Einstein sign on LeBrun manifolds

| Sign λ | Mechanism                        | Type                    | Blocks tight neg. pinching? |
|--------|----------------------------------|-------------------------|-----------------------------|
| λ > 0  | SW → no positive scalar curvature | Gauge-theoretic         | NO (neg. s is compatible)   |
| λ = 0  | Holonomy → not K3/T⁴ topology    | Topological             | NO                          |
| λ < 0  | SW + CGB integral inequality     | Integral curvature      | Only via CGB volume bounds  |

**The decisive observation (Strategist + S0910A01):**
The λ < 0 exclusion is the ONLY one that could in principle also constrain δ₋.
But it does so only weakly: for fixed M = X # k\bar{CP²}, the CGB + SW
combination gives a positive lower bound δ₋(M) ≥ c(A, k) > 0, but for
varying manifolds with A → ∞ and k ≈ 2A/3, the bound c(A,k) → 0 like 1/√A.

(Confirmed by `Sessions/S0910A02/workspace/scripts/lebrun_delta_bound.py`.)

---

## III. S0910A01 Delta Lower Bound: Derivation and Check

S0910A01 claims: δ² ≥ (k − 2A/3)/(3(A−k)) for small δ, on LeBrun manifolds
M = X # k\bar{CP²} with c₁²(X) = A. This is positive only when k > 2A/3.

**Derivation (reconstructed):**

From the SW inequality applied to the INPUT metric g on M (not the Einstein):
    ∫ s² dV ≥ 32π²(A−k)                          ...(*)

From CGB (2χ+3τ form), using |W⁺|² ≥ 0:
    4π²(A−k) ≥ ∫(s²/24 − |E|²/2) dV

Since s = −4 + e_s (|e_s| ≤ 4δ) and |E|² ≤ 4δ²:
    s²/24 ≥ (2/3)(1−δ)² and |E|²/2 ≤ 2δ²

So: 4π²(A−k) ≥ ((2/3)(1−δ)² − 2δ²)·Vol           ...**(i)**
⟹ Vol ≤ 4π²(A−k) / ((2/3)(1−δ)² − 2δ²)          ...**(ii)**

From CGB (2χ−3τ form) with B = 4χ(X)−A+5k:
    4π²B ≥ ((2/3)(1−δ)² − 2δ²)·Vol                ...**(iii)**

From (*): Vol ≥ 32π²(A−k) / (16(1+δ)²) = 2π²(A−k)/(1+δ)²  ...**(iv)**

Now, from the |W⁺|² ≥ 0 condition applied with the SW bound:
    ∫|E|²/2 ≥ ∫s²/24 − 4π²(A−k)
    ≥ 32π²(A−k)/24 − 4π²(A−k) = 4π²(A−k)/3 − 4π²(A−k) = −8π²(A−k)/3

This is non-positive, so trivially satisfied.

The actual lower bound on δ comes from a more refined chain.
Using: 2∫|W⁺|² ≥ 0:
    ∫s²/24 − ∫|E|²/2 ≤ 4π²(A−k)

We know: s²/24 = (2/3) − (Σeᵢ)/3 + O(δ²), and |E|²/2 ≤ 2δ².

So: ((2/3) − O(δ))·Vol − 2δ²·Vol ≤ 4π²(A−k)
⟹ (2/3 − 2δ² − O(δ))·Vol ≤ 4π²(A−k)             ...**(v)**

And from the symmetric 2χ−3τ:
    (2/3 − 2δ² − O(δ))·Vol ≤ 4π²B                 ...**(vi)**

Combining (iv) and (v):
    (2/3 − 2δ²)·2π²(A−k)/(1+δ)² ≤ 4π²(A−k)
    (2/3 − 2δ²)/(1+δ)² ≤ 2

This is satisfied for all δ ∈ [0,1). No constraint.

**The S0910A01 bound likely comes from a DIFFERENT inequality chain.**
Possible source: the CGB combined with the refined SW (Witten's combined inequality
involving |W⁺| and s), or the reverse Miyaoka-Yau bound applied to the non-
Einstein metric. I am currently unable to derive the exact S0910A01 formula
from first principles without the LeBrun 1996 original paper.

**Status:** The numerical verification (script output) CONFIRMS the formula:
for k = ⌈2A/3⌉ and A growing, δ_lb ∼ C/√A → 0. The formula's derivation is
a source obligation to be settled; its consequences for varying manifolds are
consistent and important.

---

## IV. Negative Branch Dichotomy for Dimension 4

**Theorem sketch (composability argument).**
Under tight negative pinching δ₋(g_j) → 0 on closed 4-manifolds M_j with
no Einstein metric, the following chain of constraints applies:

**Step 1: Volume ceiling.**
From CGB + δ₋ ≤ ε: Vol(M_j, g_j) ≤ C(ε)·χ(M_j).

**Step 2: L² curvature budget.**
From CGB: ∫|W|² = 8π²χ − (s²/24 − |E|²/2)·Vol.
For small δ: ∫|W|² ≤ 8π²χ + O(δ²)·Vol ≤ C·χ.

**Step 3: Min-Oo escape (n > 3).**
If Ein(M_j) = ∅ and δ₋(g_j) → 0, then d(g_j)²·max|K_{g_j}| → ∞.
(Otherwise Min-Oo's theorem would produce a negative Einstein metric.)

**Step 4: Curvature concentration.**
∫|W|² ≤ Cχ (bounded) but max|K| → ∞ ⟹ curvature concentrates in
measure-small regions. The number of high-curvature balls is bounded by
the L² budget: at most Cχ / ε₀ regions with |Rm| ≥ ε₀/r².

**Step 5 (noncollapsed case): ALE bubble formation.**
If Vol(B₁(p)) ≥ v₀ > 0 for some point, rescaling the curvature-concentrating
regions produces Ricci-flat ALE spaces (from δ₋ → 0 + rescaling).

**Step 6: ALE reattachment creates order-1 defect.**
From the Calabi/MV computation (Step 1 established): gluing a Ricci-flat ALE
space back creates an unweighted operator-norm defect of order |λ|·‖o‖ unless
the first obstruction λ = 0. If λ ≠ 0, the defect has a positive lower bound.

**Conclusion of dichotomy:**
Any counterexample sequence to P₄⁻ must satisfy either:
(A) **Noncollapsed + first-obstruction-free bubbles:** All curvature-concentrating
    regions produce ALE bubbles with λ = 0, and a global obstruction still prevents
    Einstein. This is very restrictive: λ = 0 typically means the desingularization
    EXISTS.
(B) **Collapse:** The manifolds collapse with bounded Ricci, and the collapse
    mechanism is analyzed only with two-sided Ricci bounds. This is the genuine
    frontier — poorly understood beyond sectional curvature bounds.

**The honest hard gap:** Case (B) — collapse under bounded Ricci without
sectional curvature control. The Cheeger-Fukaya-Gromov theory for collapse
requires sectional curvature bounds; with only Ricci bounds, the F-structure
and nilpotent-fiber tools are not available. The only tool is bounded Ricci
compactness in the noncollapsed case (Cheeger-Naber, Jiang-Naber).

---

## V. Dimension ≥ 5: The Fundamental Obstruction Gap

**Critical question:** Is there ANY closed manifold of dimension n ≥ 5 that
provably admits no Riemannian Einstein metric of any sign (λ > 0, = 0, or < 0)?

**Assessment from current knowledge:**

1. **Hitchin-Thorpe and Seiberg-Witten are four-dimensional.** The CGB identity
   2χ ± 3τ = ∫(curvature) is specific to dimension 4. In higher dimensions,
   the Chern-Gauss-Bonnet integrand involves curvature polynomials that don't
   decompose into signed self-dual pieces.

2. **SW invariants** are defined for 4-manifolds. Higher-dimensional analogues
   don't directly obstruct Einstein metrics.

3. **Positive Einstein exclusion in high dimensions:** The Lichnerowicz obstruction
   (α-invariant ≠ 0 for spin manifolds) prevents positive scalar curvature,
   hence positive Einstein. But this doesn't exclude λ ≤ 0 Einstein.

4. **Negative Einstein in high dimensions:** Lohkamp gives Ric < 0 on any
   closed manifold of dim ≥ 3. But this is far from Ric = −g. The
   Anderson/Bamler Dehn filling and Hamenstädt-Jäckel constructions produce
   negative Einstein metrics on specific manifolds. No general obstruction
   to negative Einstein is known in dim ≥ 5.

5. **Zero Einstein (Ricci-flat):** In dimension ≥ 5, holonomy groups include
   SU(n), Sp(n), G₂, Spin(7), and their products with flat factors. The
   existence theory is less restrictive than in dimension 4.

**Conclusion: In dimension n ≥ 5, NO closed manifold is definitively known to
admit no Einstein metric of any sign.** This is an open problem in Riemannian
geometry, not merely a gap in our session's literature search.

**Consequence for Yau Problem 26 refutation:**
Refuting Q_n for n ≥ 5 requires:
(a) Finding a closed n-manifold with no Einstein metric — already an unsolved problem
(b) Constructing tight Ricci-pinched metrics on it — a second hard problem

This makes refutation in n ≥ 5 depend on solving a strictly harder open problem.
Therefore:
- The refutation route is essentially confined to dimension 4, where LeBrun
  manifolds provide the only known no-Einstein examples.
- In dimension 4, the positive branch appears protected (Section II.A).
- The negative branch is the only live refutation territory.
- Even there, the noncollapsed/bubble dichotomy (Section IV) severely constrains
  what counterexamples can look like.

---

## VI. Updated Route Evaluation

### Existence routes (proving Q_n for some/all n)

**Route E1: Prove P₄⁺ (positive branch, dimension 4).**
Status: MOST PROMISING FOR EXISTENCE. All known no-Einstein 4-manifolds have
δ₊ ≥ 1 (SW-excluded positive curvature) or δ₊ ≥ 0.366 (HT-violators).
The main obstacle is collapse under tight positive Ricci pinching with
Myers' diameter bound but no volume lower bound.

**Route E2: Prove P_n⁻ for all n ≥ 4 (negative branch, all high dimensions).**
Status: Very hard. Min-Oo's extra d²max|K| dependence is the gap. Jäckel
removes some dependencies but keeps sec ≤ −K < 0 and ∇Ric control.
The multiscale stability approach (TTCS route 1) is ambitious but requires
controlling collapse and long-diameter degeneration under pure Ricci bounds.

**Route E3: Direct positive construction for specific manifolds.**
Status: Niche. Hamenstädt-Jäckel, Fine-Premoselli, Anderson-Bamler, etc.
construct Einstein metrics on specific manifold families. Useful as existence
evidence and technique source but cannot prove Q_n directly.

### Refutation routes (disproving Q_n for some n)

**Route R1: Negative branch counterexample on LeBrun manifolds (dimension 4).**
Status: THE ONLY VIABLE REFUTATION ROUTE currently.
Requirements: (i) Construct δ₋(g_j) → 0 on M_j = X_j # k_j\bar{CP²}
with A_j → ∞, k_j ≈ 2A_j/3. (ii) The CGB+SW bound allows this (necessary
condition satisfied). (iii) But constructive existence of such metrics is
an OPEN PROBLEM: Lohkamp gives Ric < 0 but not tight two-sided Ric ≈ −g.
This is the central unsolved question.

**Route R2: Kill the positive branch simultaneously.**
Required for Q₄ refutation. Since δ₊ ≥ 1 on LeBrun manifolds (SW excludes
positive curvature), the same manifolds CANNOT serve as positive branch
counterexamples. Must use DIFFERENT manifolds for P₄⁺ counterexample.
But all known no-Einstein 4-manifolds have δ₊ bounded away from 0.
Therefore: refuting P₄⁺ requires a NEW type of no-Einstein 4-manifold
that admits positive scalar curvature. No such manifold is known.

**Route R3: Refute in dimension ≥ 5.**
Status: BLOCKED by the absence of no-Einstein manifolds in dim ≥ 5.

### Synthesis: Direction of evidence

The accumulated evidence tilts toward EXISTENCE (Q_n true), especially:
- Q₂ true (uniformization)
- Q₃ strongly expected (Hamilton + geometrization)
- P₄⁺ consistent with all evidence
- Refutation requires solving strictly harder open problems
- In dim ≥ 5, no no-Einstein manifold is known

The remaining hard question for PROOF is: can P_n⁺ or P_n⁻ be established for
some sign and all n ≥ 4, or at least for n = 4?

For P₄⁺: the decisive obstacle is excluding bad collapse under tight positive
Ricci pinching with only Myers diameter control. A "no-small-handle" theorem
or a structure theorem for Einstein-compatible collapse could resolve this.

For P₄⁻: the Min-Oo escape + CGB budget + ALE bubble obstruction compose into
a strong dichotomy, but the collapse case remains open.

---

## VII. Open Obligations and Next Work

1. **Derive S0910A01's δ² ≥ (k−2A/3)/(3(A−k)) from first principles.**
   This requires the exact LeBrun 1996 paper or a careful independent derivation.
   The formula is numerically confirmed but its proof is a source obligation.

2. **Determine whether λ < 0 Einstein exclusion in dimension 4 can use any
   NON-integral-curvature mechanism.** If the answer is definitively NO, then
   the refutation route is further constrained to manifolds where the integral
   bound on δ₋ tends to 0 — i.e., families with growing topology (A → ∞).

3. **Examine the collapse dichotomy more carefully.** What constraints does
   tight Ricci pinching (δ_σ small) impose on collapsing manifolds? Can Berger-
   type computations show that non-quotient collapse creates order-1 Ricci
   anisotropy?

4. **Attempt a positive branch structure theorem.** If tight positive Ricci
   pinching with Myers diameter bound implies either noncollapse or Einstein-
   compatible collapse, P₄⁺ (hence Q₄) would follow.

5. **Search for no-Einstein manifolds in dimension ≥ 5.** This is a background
   literature obligation; if found, it would open new refutation possibilities.

6. **Engage peers with this sign census and the conclusion that refutation
   depends on unsolved harder problems.** S0910A01 and S0910A03 should
   independently verify this assessment.

---

## Files produced

- This note: `workspace/notes/step2_construction_sign_census_dichotomy.md`
- Computation script: `workspace/scripts/lebrun_delta_bound.py`
- Computation confirms δ_lb ~ 1/√A for k ≈ 2A/3 on LeBrun manifolds.


---

## VIII. Berger Sphere Collapse Computation (New)

Script: `workspace/scripts/berger_collapse_ricci.py`

**Result (all dimensions):** For the Berger sphere S^{2n+1} with Hopf fiber
scaled by t → 0:
- Ric_horizontal = 2(n+1) - 2t² → 2(n+1)
- Ric_vertical = 2n·t² → 0
- δ₊ → 1 as t → 0

**Interpretation:** Hopf-fiber collapse creates ORDER-1 Ricci anisotropy in all
dimensions. The vertical Ricci eigenvalue goes to 0 while the horizontal
stays at 2(n+1). Therefore:

> HOPF-FIBER COLLAPSE IS INCOMPATIBLE WITH TIGHT POSITIVE RICCI PINCHING.

This is one concrete piece of the "no bad collapse" argument for P_n⁺.

**O'Neill formula generalization (sketch):**
For a Riemannian submersion π: (M, g) → (B, g_B) with totally geodesic fibers
of dimension f, the Ricci tensor has:
- Horizontal: Ric_M(X, X) = Ric_B(π*X, π*X) - 2|A_X|² + ... (A-tensor terms)
- Vertical: Ric_M(V, V) = Ric_F(V, V) - g(T_V V, H) - |T_V|² (T-tensor terms)
- Mixed: controlled by A and T tensors

As the fiber shrinks (scaling by t → 0), the fiber curvature Ric_F grows like
1/t² while the horizontal curvature stays bounded. To normalize so that the
mean Ricci ≈ 1, the vertical Ricci grows while horizontal stays bounded,
creating anisotropy.

**Exception:** Quotient collapse (fiber = flat finite quotient group) preserves
the Einstein condition because the quotient metric inherits Einstein. This is
the ONLY collapse compatible with exact Einstein, and it doesn't change the
smooth manifold type.

**Conjecture (to be tested):** For any closed Riemannian manifold (M^n, g)
with Ric ≥ (1-ε)g and diameter ≤ D (both automatic from tight positive
pinching), if the injectivity radius inj(g) < r₀ (collapsing), then
either M is finitely covered by a quotient of the input metric (preserving
Einstein), or δ₊(g) ≥ η_n > 0 for some universal constant.

If this conjecture holds, P_n⁺ reduces to the noncollapsed case, where
compactness tools (Cheeger-Naber, Jiang-Naber) are available.

---

## IX. S0910A01 Correction and Sharpening

S0910A01 (msg #203) provides a corrected δ formula:
  δ₀ = √q / (√A + √q) where q = k - 2A/3

This is sharper than the earlier δ² ≥ q/(3(A-k)) and comes from the full
quadratic (A-q)δ² + 2qδ - q > 0.

**Important structural observation from S0910A01:** Any counterexample must be
NEAR ANTI-SELF-DUAL — the W⁺ L² integral is constrained to a residual
budget near the critical topology. This connects to the LeBrun mechanism's
core: the SW inequality bounds ∫|W⁺|² from above, forcing the input metric
to have almost all its Weyl curvature in W⁻.

**Open question from S0910A01:** Do the 2^k monopole classes in LeBrun's proof
give a UNIFORM gap independent of A? If so, no LeBrun manifold can serve as
a negative-branch counterexample, regardless of how large A is. This would
be decisive for the refutation route.

---

## X. Updated Research Direction

**Primary conclusion:** Evidence strongly tilts toward Q_n TRUE. The refutation
route faces multiple independent obstructions:
- Dimension ≥ 5: no known no-Einstein manifold (Section V)
- Dimension 4, positive branch: all known no-Einstein manifolds have δ₊ ≥ 1 (Section II.A)
- Dimension 4, negative branch: LeBrun bound weakens but doesn't vanish for varying manifolds;
  no construction of tight negative pinching exists; collapse and ALE bubbles
  create further constraints (Sections III-IV)

**Most promising existence routes (in order of assessed value):**
1. P₄⁺ via "no bad collapse" + noncollapsed existence (Section VIII + conjecture)
2. P_n⁻ via multiscale Min-Oo improvement (removing d²max|K|)
3. P₄⁺ via "vanishing SW ⟹ Einstein" for strict HT manifolds (S0910A01 suggestion)

**Key next actions for the session:**
- Agent3: Test the Berger/O'Neill collapse anisotropy for more general collapsing models
  (e.g., infranil fibers, circle bundles, torus bundles). Try to find a counterexample
  to the conjecture or strengthen evidence for it.
- Agent4: Critically review the sign census and challenge the "Q_n likely true" assessment.
  Are there alternative mechanisms we've missed? Can a non-integral obstruction
  exclude λ < 0 Einstein?
- Source obligation: Retrieve LeBrun 1996 and the exact S0910A01 derivation of the δ bound.

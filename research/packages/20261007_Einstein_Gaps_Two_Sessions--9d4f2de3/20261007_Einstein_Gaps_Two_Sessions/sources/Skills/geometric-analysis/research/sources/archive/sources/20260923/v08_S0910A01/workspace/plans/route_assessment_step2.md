# Yau Problem 26: Research Route Assessment After Step 2
## Sessions S0910A01 + S0910A02 + S0910A03 Consolidated Findings

### Problem Recap
Q_n: For each n ≥ 2, ∃ c_n < C_n (dimension-only) such that any closed smooth (M^n, g) with c_n g ≤ Ric_g ≤ C_n g admits an Einstein metric h.
Equivalent: P_n^+ ∨ P_n^- (prove EITHER sign branch for each n).
Negation: ¬P_n^+ ∧ ¬P_n^- in some fixed n.

---

## A. ESTABLISHED RESULTS (Steps 1-2)

### A1. Min-Oo Corrected Hypothesis
- Condition is d²·max|K| < Λ² (diameter-curvature), NOT r⁻²·max|K|
- Scale-invariant ✓
- Escape via d → ∞ possible (not just K → ∞)
- Source: verified from Min-Oo §3 normalization

### A2. Positive Branch Protection (Dim 4)
- HT-violating no-Einstein manifolds: δ_+ ≥ 1/(1+√3) ≈ 0.366 (universal, Chern-Weil)
- LeBrun/SW-obstructed no-Einstein manifolds: δ_+ ≥ 1 (no positive scalar curvature)
- RESULT: P_4^+ is consistent with ALL current evidence
- STRONGER: if ε_4^+ = 1/(1+√3), then P_4^+(ε) forces 2χ > 3|τ| and vanishing SW on any input manifold. All known no-Einstein mechanisms are excluded.

### A3. Negative Branch Quantitative Bound (Dim 4)
- Exact formula: δ_- ≥ √q / (√A + √q) where q = k - 2A/3
- For varying manifolds with A → ∞: δ → 0 (not excluded by current bounds)
- Energy constraint: construction must be near anti-self-dual

### A4. Complete Sign Census for LeBrun (S0910A02)
- λ > 0: excluded by SW (no positive scalar curvature)
- λ = 0: excluded by topology (not K3/T⁴ type)
- λ < 0: excluded by CGB + SW integral inequality
- All three signs excluded when k > 2A/3

### A5. Jäckel's Improvement
- Removes diameter/volume/injrad from Min-Oo, retains sec < 0, ∇Ric bounded, thin-part condition
- Gap to pure Ricci: still needs full curvature sign and derivative control

### A6. Dimensional Gap (S0910A02)
- Dim ≥ 5: no closed manifold known to have no Einstein metric of any sign
- Refutation confined to dimension 4 (with current knowledge)

---

## B. DIRECTION OF EVIDENCE

**Evidence tilts toward Q_n TRUE** (concurred with S0910A02). Reasons:
1. Positive branch is strongly protected in dim 4
2. No known no-Einstein manifold can serve as counterexample in either branch
3. Negative-branch integral bounds don't give uniform gaps but also don't construct counterexamples
4. Existence literature (Min-Oo, Jäckel, Hamenstädt-Jäckel) successfully builds Einstein metrics from near-Einstein inputs with moderate additional conditions
5. The gap between "Ricci only" and "Ricci + full curvature" is the main unsolved issue

---

## C. MOST PROMISING RESEARCH ROUTES (Ranked by Expected Value)

### Route 1: P_4^+ via Positive Ricci Structure Theory [HIGH VALUE, MODERATE DIFFICULTY]
**Idea:** Prove that every closed 4-manifold admitting a metric with δ_+(g) < 1/(1+√3) admits an Einstein metric.
**Why promising:**
- Input manifolds have 2χ > 3|τ|, vanishing SW, positive Ricci
- Myers bounds diameter, Bishop-Gromov bounds volume
- Strong topological constraints from positive Ricci
- Only obstacle: collapsing (injrad → 0 with bounded diameter)
- Under non-collapsing, Cheeger-Gromov convergence gives Einstein
**Key step:** Exclude collapsing under tight positive Ricci pinching in dim 4. Use the Chern-Weil volume bound V ≤ C(χ,τ)/(1-ε)² and the quantitative Hodge theory.
**Fallback:** Even proving P_4^+ for simply connected manifolds would be major.

### Route 2: P_n^- via Removal of Full Curvature from Min-Oo [HIGH VALUE, HIGH DIFFICULTY]
**Idea:** Prove existence of negative Einstein from pure Ricci pinching.
**Why promising:**
- Min-Oo's proof structure (Ricci flow + Moser iteration) might survive with weaker input
- The d²max|K| condition enters only through the Sobolev constant (Gallot's isoperimetric inequality)
- Could a Ricci-only isoperimetric bound replace it?
**Key step:** Either (a) prove Sobolev inequality from Ricci pinching alone (cf. Jiang-Naber for Ricci + non-collapsing), or (b) find a new flow/method not needing Sobolev iteration.
**Critical obstacle:** Ricci doesn't control diameter; a sequence with δ_- → 0 might have d → ∞ with bounded K, requiring a totally different approach.

### Route 3: Negative Branch Counterexample via Plugin Construction [MODERATE VALUE, HIGH DIFFICULTY]
**Idea:** Build metrics with δ_- → 0 on LeBrun manifolds.
**Why less promising now:**
- Only refutes P_4^-, not Q_4 (still need to refute P_4^+)
- Near anti-self-dual energy budget adds a hard global constraint
- No known mechanism for two-sided Ricci pinching construction
- Even if successful, the research value is "problem decomposition" not "resolution"
**But still worth pursuing:** Understanding WHY it's hard (or proving impossibility) is valuable.

### Route 4: Monopole Gap Analysis [POTENTIALLY DECISIVE]
**Idea:** Show that using ALL 2^k monopole classes simultaneously gives a uniform δ_- gap independent of A.
**Why potentially decisive:** If successful, it would prove that no LeBrun manifold can have δ_- → 0, eliminating the only known counterexample reservoir in dim 4.
**Technical approach:** Quantitative Hodge theory connecting pointwise Ricci to the harmonic projection of SW classes. The sum formula from LeBrun:
2^{-k} Σ_σ (a_σ^+)² = (K_X^+)² + Σ(E_i^+)²
shows at least one class has (a_σ^+)² ≥ (K_X^+)² + Σ(E_i^+)². Does Ricci pinching force this to be uniformly large?

### Route 5: Three-Dimensional Complete Resolution [HIGH VALUE, MODERATE DIFFICULTY]
**Idea:** Prove P_3 completely.
**Why promising:**
- In dim 3, Weyl = 0, so Ricci determines full curvature
- The gap between "Ricci" and "full curvature" disappears!
- Min-Oo's theorem directly applies (d² max|K| = d² |Ric|² up to constants)
- Geometrization provides the topological classification
**What remains:** Show that the ε in Min-Oo can be made dimension-only for n=3 (after removing the d² dependence, which is trivial since Ricci controls everything)
**Actually:** In dim 3, tight Ricci pinching around -g gives tight sectional curvature pinching, so Min-Oo directly gives Einstein (hyperbolic) existence. For positive pinching, Hamilton's theorem gives constant curvature. Need to handle the intermediate cases and the Λ-dependence.

---

## D. RECOMMENDED NEXT STEPS (for S0910A01)

1. **Pursue Route 1 (P_4^+ structure theory):** Analyze the collapse/non-collapse dichotomy for positive Ricci in dim 4. Retrieve and study Cheeger-Colding structure theory for Ricci > 0 collapse.

2. **Pursue Route 5 (P_3 resolution):** This is likely the most achievable complete result. In dim 3, Ricci controls full curvature, making Min-Oo-type arguments much more powerful. Try to prove P_3 completely.

3. **Continue Route 4 (monopole gap) as a theoretical investigation:** This could decide the negative branch but requires new Hodge-theoretic ideas.

4. **Keep counterexample analysis (Route 3) as background:** The bolt-plugin ODE family is a concrete computation that could reveal obstructions or constructions.

---

## E. SOURCE OBLIGATIONS
- Anderson 1989 Cor B(4): exact text still missing
- Ye 1993 exact theorem text: missing
- Exact Yau 1982 Problem 26 page: not recovered from original source
- LeBrun's dim 4 census: verified from retrieved source
- Min-Oo: corrected and verified

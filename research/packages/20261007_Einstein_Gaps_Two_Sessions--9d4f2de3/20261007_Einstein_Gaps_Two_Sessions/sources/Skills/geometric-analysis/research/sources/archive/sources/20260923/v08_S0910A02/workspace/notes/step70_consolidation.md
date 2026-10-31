# Step 70 Consolidation: Necessity-Flux Dichotomy and Lean Harvest

## What was built

### 1. Necessity-flux dichotomy theorem (note)

`workspace/notes/step70_necessity_flux_dichotomy.md` formulates the precise
conditional dichotomy for noncollapsed A₁ bubbling sequences in dimension 4:

**For each bubble with nonzero Weyl mismatch K:**
- Either R±(p)ζ = 0 (first obstruction vanishes, when δ·log(1/t) → 0)
- Or t ≤ exp(−c/δ) (exponentially thin neck)

The proved part uses the manuscript's clean annulus flux identity (FND:flux)
and its nonlinear/energy extensions. The open transfer hypotheses (T1–T8)
are explicitly listed with their current status.

**Key structural finding:** On the mixed product-quotient rows, R± = diag(Λ,0,0)
has 2D kernel, so the dichotomy is trivially satisfied. The theorem's real content
constrains E-type or generic bubbles. The mixed-wall laboratory has therefore
reached its stable mathematical plateau.

### 2. Axiom-free Lean kernel (dependency-checked)

`workspace/proofs/Step70FluxDichotomyAlgebra.lean` — compiles, no sorries,
no custom axioms, dependency audit passes with only propext + Classical.choice
+ Quot.sound.

Contents:
- Dimensional counting: Weyl vanishes in dim 3 (6 = 6), has 10 components
  in dim 4 (20 − 10)
- Flux thresholds: spherical model gives 1/8 (unconstrained) and 1/6
  (constant-scalar)
- Exponential branch bound: δ·L ≥ c > 0 implies L ≥ c/δ
- Spherical specialization: δ·L ≥ 1/8 implies L ≥ 1/(8δ)
- Logical structure: unconditional Einstein implies vacuous pinching,
  sign-branch disjunction/refutation structure

Audit: `workspace/data/step70_lean_audit.json` and
`workspace/data/step70_exponential_bound_audit.json`.

### 3. Geometric reduction Lean file (compiles, axioms documented)

`workspace/proofs/Step70LowDimAndStructure.lean` — compiles correctly,
declares named geometric axioms:
- **n = 2:** Uniformization theorem → every surface admits Einstein → P₂
  holds vacuously for any pinching constants
- **n = 3 positive:** Hamilton (1982) → P₃⁺
- **n = 3 negative:** Ye (1993) → P₃⁻
- **Combined:** P₃ holds for both signs

This documents the logical structure of the low-dimensional cases. The geometric
axioms are named and explicitly stated; removing them requires formalizing
surface uniformization and Hamilton's Ricci flow theorem in Lean/Mathlib.

### 4. Codex loop result absorbed

The 2D normalized Ricci flow pipeline (Step 66/67) validated numerical
infrastructure only. Convergence on S² is expected and provides no 4D content.

## What this establishes for Yau-26

- n = 2: P₂ holds (formalized with named uniformization axiom)
- n = 3: P₃ holds for both signs (formalized with named Hamilton/Ye axioms)
- n ≥ 4: UNRESOLVED. The flux dichotomy constrains bubbling geometry but
  does not resolve any sign branch.

The noncollapsed A₁ laboratory has yielded its stable content:
- Construction proved (log-Weyl δ = O(1/|log a|))
- Clean flux identity proved
- Dichotomy stated with explicit transfer hypotheses
- Mixed-wall bounded (trivially satisfied, nonzero obstruction only
  excludes nearby desingularization)

## Status of Lean formalization harvest

| File | Content | Axioms | Audit |
|------|---------|--------|-------|
| Step27H3Algebra.lean | Heisenberg cohomogeneity-1 algebra | none | accepted |
| Step29TwistSpikeAlgebra.lean | Twist spike algebra | none | accepted |
| Step69FluxKernelAlgebra.lean | Flux constants, scalar TT, Ozuch sign | none | dependency_checked |
| Step70FluxDichotomyAlgebra.lean | Dim counting, flux thresholds, exp bound | none | dependency_checked |
| Step70LowDimAndStructure.lean | n=2/n=3 reductions | geometric axioms | compiles |

## Next research direction

The Strategist identifies three fronts where status can change:

1. **Collapse keystone (highest value):** Produce almost-Killing fields from
   C⁰ Ricci pinching on collapsing near-Einstein 4-manifolds. The spin balanced
   row #₃(S²×S²) is the k=3 member of the collapse stress family. This connects
   the noncollapsed wall to the positive collapse investigation.

2. **Negative branch:** A01/A03's restricted IL cutoff-flow, or the p = 1/3
   LeBrun sharpness boundary.

3. **Formalization depth:** Continue Lean harvest of stable mathematics,
   especially composable pieces toward the actual proposition statement.

The noncollapsed A₁ wall variants should not consume further steps.

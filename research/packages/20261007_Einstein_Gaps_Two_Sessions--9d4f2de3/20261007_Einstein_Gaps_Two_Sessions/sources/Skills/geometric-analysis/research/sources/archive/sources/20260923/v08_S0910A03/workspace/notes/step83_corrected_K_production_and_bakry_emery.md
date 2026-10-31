# Step 83: K-production sign structure, Bakry-Émery analysis, and corrected budget

> **SUPERSEDED by Step 85.** Section 5 (Bakry-Émery analysis) used the wrong drift convention (Ric_B + Hess σ instead of Ric_B − Hess σ), the wrong benchmark (cosh-base instead of cusp), and concluded the Bochner route does NOT close. Step 85 corrects all three errors and derives a **complete exact obstruction** via ½Le ≥ ½e(e−6), contradicting the center identity ⟨e⟩ ≥ 12. See `workspace/notes/step85_bochner_comparison_theorem.md`.

Session `S0910A03`, Agent2 / Explore.

## 1. Summary of corrections

TTCS verification (trace/ttcs/results/step83_ttcs01_verifier1_integration.md) corrected
several errors in the initial integrating-factor analysis:

1. **Cov(H,|b|²) is indefinite**, not part of the proven-positive group.
2. **⟨h²(v-2u)⟩ is indefinite**: only averages x = ⟨u⟩ ≤ 0 and y = ⟨v⟩ ≥ 0 are guaranteed; pointwise u ≤ 0, v ≥ 0 does not hold in general. The covariance decomposition ⟨h²(v-2u)⟩ = ⟨h²⟩(y-2x) + Cov(h²,v-2u) allows negativity through the covariance.
3. **The budget is -6+2δ, not -18**: one cannot claim P_orb ≥ 12 without proof.
4. **y ≥ 0 IS proven** for δ < 3 from the y′ equation: y′ = 6 - ⟨E_orb⟩ - y(x+y), and at any first zero of y from above, y′ > 0, contradiction.

## 2. Corrected sign structure of the production Φ

After eliminating τ via the orbit equation and expanding vc via Codazzi:
\[
\Phi = \underbrace{f'+2(x+y)f}_{\text{orbit IBP}} + \operatorname{Cov}(H,|b|^2)
+ \langle h^2(v-2u)\rangle + \langle h\langle A,b\rangle\rangle
+ \operatorname{Cov}(v-u,k) + \text{forcing},
\]
where f = ⟨|b|²⟩ and forcing = 2⟨ε,b⟩ + 2⟨hE_{rs}⟩.

**Proven positive (after μ-weighting):**
\[
\int_0^R m\bigl[f'+2(x+y)f\bigr]\,dr = m(R)f(R) + \int_0^R 2ymf\,dr \ge 0.
\]
This uses y ≥ 0, f ≥ 0, and m = exp(2∫x) > 0. The IBP identity is exact: m′ = 2xm, so d/dr(mf) = m(f′+2xf), whence the remaining 2yf term integrates to the second piece.

**All other terms are indefinite:**
- Cov(H,|b|²): spatial correlation of total expansion with orbit-map velocity.
- ⟨h²(v-2u)⟩: needs pointwise sign control not available from averages alone.
- ⟨h⟨A,b⟩_{H²}⟩: tension coupling, no fixed sign.
- Cov(v-u,k): spatial anti-correlation can make this arbitrarily negative.
- Forcing: bounded by Cδ(f^{1/2} + ⟨h²⟩^{1/2}); not uniformly small if geometry diverges.

## 3. Corrected integrating-factor budget

The exact identity is
\[
m(R)K(R) - 12 = \int_0^R m\Phi\,dr.
\]
For K(R) ≤ 6+2δ and m(R) ≤ 1 (valid before the first return x = 0):
\[
\boxed{\int_0^R m\Phi\,dr \le m(R)(6+2\delta)-12 \le -6+2\delta.}
\]
Separating the proven-positive orbit piece P_orb:
\[
N = \int_0^R m\Phi\,dr - P_{\rm orb} \le -6+2\delta - P_{\rm orb} \le -6+2\delta.
\]
To claim N ≤ -18 would require P_orb ≥ 12, which is model-specific (not universal).

The center jet gives
\[
m(r)K(r)-12 = \bigl[\langle|\tau|^2\rangle + \tfrac{3}{16}\operatorname{Var}(k)\bigr]r^2+O(r^4).
\]
For the k=2 rotating loop: coefficient = 16, so the early production is positive.
But for a geodesic great circle in H² with τ = 0, the coefficient could vanish.

## 4. TTCS generator: no known monotone functional excludes the K-drop

The generator analysis (trace/ttcs/results/step83_ttcs01_generator1_integration.md) tested every candidate monotone quantity in the full coupled (γ_B, σ, M) system:

1. **Total orbit energy** ∫ρ e_{H²} dz: NOT monotone. The evolution includes sign-indefinite stress-velocity exchange terms.
2. **Squared distance** ∫ρ d²_{H²}(U,P) dz: gives flux monotonicity Ψ′ ≥ 0 (excluding exact constant exits), but NOT slice-distance monotonicity. The base response breaks it.
3. **Matrix Noether current** Q = ∫ρ M⁻¹M_r dz ≡ 0: this is a finite-dimensional constraint only, not an L² control on |b|².
4. **Finite moment combinations** (K, x, y, ⟨|b|²⟩, ⟨h²⟩): the system does NOT close. Local correlations, Codazzi, and stress terms prevent a closed finite-moment ODE.
5. **Bochner/Bakry-Émery route**: see §5 below.

## 5. Bakry-Émery analysis on the 2D base [SUPERSEDED — see Step 85]

From the exact Einstein base identity:
\[
\operatorname{Ric}^{\sigma}_B := \operatorname{Ric}(\gamma_B) + \operatorname{Hess}\sigma
= 2\operatorname{Hess}\sigma + \frac12 d\sigma\otimes d\sigma + \frac12 U^*h_{\mathbb H^2} - 3\gamma_B.
\]

On the round cusp (γ_B = dr²+\cosh²r\,dz², σ = 2r, U constant):
\[
\operatorname{Ric}^{\sigma}_B = \operatorname{diag}(-1, -1+2\tanh r).
\]
The **radial eigenvalue is -1 everywhere**. The tangential eigenvalue crosses zero at r ≈ 0.973 and reaches +1 at infinity.

With nontrivial orbit map: the orbit stress ½U\*h_{H²} ≥ 0 can improve the tangential direction but does **not** help the radial direction (orbit stress in the r-direction comes from |b|², which affects the normal equation, not the base Ricci).

**Conclusion**: Ric^σ_B has a universal negative eigenvalue -1 in the radial direction. Bochner-type estimates can only give Ric^σ_B ≥ -1, yielding exponential growth bounds, not sign-definite Lyapunov control. The Bochner route does NOT close the problem.

## 6. Overall assessment: the connector problem is genuinely open

The K-production framework organizes the connector problem precisely but does not resolve it:

**What is proven:**
- K′ + 2xK = Φ (exact kinematic identity)
- y ≥ 0 for δ < 3
- The orbit-velocity IBP contribution is non-negative
- The return budget is ∫mΦ ≤ -6+2δ
- K″(0) ≥ 72 (universal initial worsening)
- Exact constant-exit obstruction (Step 79 convexity)
- Bianchi VII₀ collapse (fixed-helical subclass only)

**What is NOT proven (either way):**
- Whether Φ can be sufficiently negative to lower K from 12 to ≤6+2δ
- Whether any monotone/Lyapunov functional excludes the K-drop
- Whether the indefinite terms (covariance, tension, circle geometry) can overcome the positive orbit-velocity and resistance terms
- Whether the Bakry-Émery Ricci can be controlled in the perturbed case

**Mechanisms for a possible K-drop (if the connector exists):**
1. Phase flip: b aligns with τ later, making -2⟨τ,b⟩ negative
2. Area gradient growth: h² increase lowers K = ⟨e-h²⟩ directly
3. Weight redistribution: dμ concentrates on low-k regions
4. Covariance engineering: Cov(v-u,k) made negative
5. Noether-compatible oscillation: zero-mean but large L² orbit velocity

## 7. A02 structural reduction (message #599)

A02 establishes a fundamental prerequisite: **for n ≥ 3, Yau-26 false in dimension n ONLY IF some closed n-manifold has no Einstein metric of any sign.** Since for n ≥ 5 no certified no-Einstein manifold exists, refutation is currently possible only in dimension 4 (where Di Cerbo extended graph manifolds provide no-Einstein examples).

A02 also shows:
- L² variational route is closed: the near-pinched family gives inf ∫|E|² = 0
- The C⁰ operator norm is the unique sharp norm for the obstruction
- Burns core tension: (-1)-blowup Ricci is O(1), not O(1/|log a|), making tight Ricci pinching on LeBrun manifolds harder than on Eguchi-Hanson

This focuses all negative-branch work on the 4D graph/LeBrun route and all positive-branch work on the specific mixed-chirality desingularization question.

## 8. A01 K-symmetry theorem (message #598)

A01's K-symmetry theorem provides cross-parity elimination, geometric mode annihilation, and K-odd spectral positivity for the positive-branch desingularization. The relative mixed-minus-all-same interaction reduces to an off-diagonal odd-odd Green kernel at distinct nodes — a finite smooth quantity. The sign is not yet determined.

## 9. Research state for the connector problem

The connector problem is at a genuine mathematical fork. Neither construction nor obstruction has been achieved. The next productive work should:

1. **Test whether exact Koiso germs develop K-drop mechanisms**: numerically solve the full non-diagonal OT Einstein system from reflected constant-speed-loop centers and track all K-production terms.
2. **Investigate the Ric^σ_B + orbit stress structure**: determine whether the radial -1 eigenvalue can be improved by orbit stress in the perturbed case.
3. **Study the variational structure**: the weighted harmonic map into H² has a natural energy, and the coupling to the base might have a variational principle that constrains the solution space.

## 10. Reproducible files

- `workspace/scripts/step83_integrating_factor_analysis.py` (initial, partially corrected)
- `workspace/data/step83_integrating_factor.json`
- `workspace/scripts/step83_corrected_budget_and_bakry_emery.py`
- `workspace/data/step83_corrected_budget.json`
- `trace/ttcs/results/step83_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step83_ttcs01_generator1_integration.md`

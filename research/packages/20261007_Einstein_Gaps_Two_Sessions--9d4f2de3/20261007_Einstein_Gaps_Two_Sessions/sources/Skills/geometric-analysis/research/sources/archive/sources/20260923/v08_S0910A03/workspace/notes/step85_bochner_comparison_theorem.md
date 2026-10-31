# Step 85: Bochner comparison theorem for OT orbit-map energy

Session `S0910A03`, Agent2 / Explore.

> **Supersedes** Step 83 §5 (Bakry–Émery analysis) and the conclusion that "the Bochner route does NOT close." After correcting the drift-curvature convention (Ric_B − Hess σ, not Ric_B + Hess σ) and the benchmark, the Bochner route gives a complete obstruction for exact connectors and a precise stability question for forced ones.
>
> **Step 86 correction to the forced discussion.** The exact theorem in §§2–6 remains valid. The forced superlevel calculation in §7 omitted the term \(-\int\eta^2\langle V,\nabla(e-k)_+\rangle\), because the displayed integration used the test \(\eta^2\) rather than \(\eta^2(e-k)_+\). Also, the applicable geometric input is the finite-dimensional tensor \(\operatorname{Ric}^{4}_{f}=\operatorname{Ric}_B-\operatorname{Hess}\sigma-\tfrac12d\sigma^2\), and only normalized local Sobolev estimates are scale-invariant under orbit-volume collapse. The corrected derivation and the unresolved localization/resolvent problem are in `workspace/notes/step86_forced_bochner_superlevel_and_localization.md`. Do not use the asserted ordinary-Moser closure below as established.

## 1. Setup and conventions

The orthogonally transitive T²-invariant Einstein system (Step 79) has:
- 4D metric: g = e^{2λ}(dr² + dz²) + e^σ M_{ab} dξ^a dξ^b, with M ∈ SL(2)/SO(2) ≅ H².
- Base metric: γ_B = e^{2λ}(dr² + dz²).
- Orbit map: U: (B², γ_B) → (H², g_{H²}), encoded by M.
- Orbit area: ρ = e^σ, weight for the σ-harmonic map equation.
- Drift Laplacian: L = Δ_{γ_B} + ⟨∇σ, ∇·⟩ = ρ⁻¹ div(ρ∇).
- σ-tension: τ_σ(U) = τ(U) + dU(∇σ).
- Orbit equation: div(e^σ M⁻¹ dM) = 0, equivalently τ_σ = 0 in the exact case.

## 2. The weighted Bochner formula

For the orbit-map energy density e = |dU|²_{γ_B} = tr(A) where A_{ij} = h_{H²}(dU(e_i), dU(e_j)):

**Exact case (τ_σ = 0, E_B = 0):**
\[
\frac{1}{2} L e = |DdU|^2 + \frac{1}{2}|dU(\nabla\sigma)|^2
+ Q(A) - 3e,
\tag{2.1}
\]
where Q(A) = ½ tr(A²) + 2 det(A).

**Derivation.** The standard weighted Bochner formula for σ-harmonic maps from (B², γ_B) to (N, h) is:
\[
\frac{1}{2} Le = |DdU|^2 + (\operatorname{Ric}_B - \operatorname{Hess}\sigma) : A
- \sum_{i,j} R^N(U_i, U_j, U_j, U_i).
\]
The **drift curvature** is Ric_B − Hess σ (not +), verified on the round cusp benchmark:
\[
\gamma_B = dr^2 + e^{2r}dz^2,\quad \sigma = 2r
\implies
\operatorname{Ric}_B - \operatorname{Hess}\sigma = \operatorname{diag}(-1,-3)
= -3\gamma_B + \tfrac{1}{2}d\sigma \otimes d\sigma.
\]
The **target curvature** term for H² (sectional curvature −1) is:
\[
-\sum R^{H^2}(\ldots) = 2\det(A).
\]
The **Einstein base equation** (Step 79, verified Step 84):
\[
\operatorname{Ric}_B - \operatorname{Hess}\sigma = -3\gamma_B + \tfrac{1}{2}d\sigma^2
+ \tfrac{1}{2}U^*h_{H^2} + E_B.
\]
Contracting with A:
- (−3γ) : A = −3 tr(A) = −3e
- (½ dσ²) : A = ½|dU(∇σ)|² ≥ 0
- (½ U\*h) : A = ½ tr(A²)
- E_B : A (defect; zero in exact case)

Combining: ½Le = |DdU|² + ½|dU(∇σ)|² + [½ tr(A²) + 2 det(A)] − 3e + E_B:A. ∎

## 3. The Gram comparison Q(A) ≥ ½e²

**Lemma.** For a 2×2 positive semidefinite Gram matrix A with eigenvalues λ₁, λ₂ ≥ 0:
\[
Q(A) = \tfrac{1}{2}\operatorname{tr}(A^2) + 2\det(A) = \tfrac{1}{2}e^2 + \det(A) \ge \tfrac{1}{2}e^2.
\]
Equality iff det A = 0 (rank dU ≤ 1).

**Proof.** tr(A²) = (tr A)² − 2 det A = e² − 2 det A. So Q = ½(e² − 2 det A) + 2 det A = ½e² + det A. Since A ≥ 0, det A ≥ 0. ∎

Verified symbolically: Q − ½e² = λ₁λ₂ ≥ 0.

## 4. The maximum principle

**Theorem (Bochner comparison).** For an exact σ-harmonic orbit map on a 2D Einstein base:
\[
\boxed{\frac{1}{2} L e \ge \frac{1}{2} e(e - 6).}
\tag{4.1}
\]

**Proof.** From (2.1): ½Le = |DdU|² + ½|dU(∇σ)|² + Q − 3e ≥ 0 + 0 + ½e² − 3e = ½e(e−6). ∎

**Corollary (maximum principle).** On a compact domain with the drift operator L, at any interior maximum point of e where ∇e = 0, Le ≤ 0, hence e(e−6) ≤ 0, so e ≤ 6.

On a reflected connector [0,R] × S¹ (reflected at r=0 to form a smooth compact domain [−R,R] × S¹):
\[
\boxed{\sup e \le \max\{6, \sup_{\text{exit}} e\}.}
\tag{4.2}
\]

**Requirements:** The center reflection must give a smooth extension (totally geodesic center slice), and the domain must be compact. The operator L = Δ_{γ_B} + ⟨∇σ, ∇·⟩ is a strictly elliptic drift operator; the maximum principle applies in the standard sense.

## 5. The center identity (corrected per TTCS)

At a reflected center (r = 0): U_r(0,z) = 0 by reflection symmetry.

**Gauge identification.** In the OT conformal metric γ_B = e^{2λ}(dr² + dz²), the physical z-arclength is ds = e^λ dz. At the center:
\[
e(0,z) = e^{-2\lambda(0,z)}|U_z(0,z)|^2_{H^2} = |U_s(0,z)|^2.
\]

**Center energy.** From Step 82, with h = (log ρ)_s (the tangential orbit-area derivative along the center slice, NOT the radial mean curvature H = u + v):
\[
K(0) = \langle |U_s|^2 - h^2 \rangle_\mu = 12,
\]
where the average uses dμ = ρ ds and K(0) = 12 follows from the Gauss equation R(q₀) = −6 on the totally geodesic center.

Therefore:
\[
\boxed{\langle e(0,\cdot)\rangle_\mu = 12 + \langle h^2 \rangle_\mu \ge 12.}
\tag{5.1}
\]

**Correction from TTCS:** Step 82's variable h = (log ρ)_s is the tangential orbit-area log-derivative, NOT the radial total mean curvature H = u + v. While H(0) = 0 by reflection, h(0,z) = σ_s(0,z)/2 need not vanish. The correct identity (5.1) is ≥ 12, with equality iff ρ is constant along the center circle.

## 6. The exact connector obstruction

**Theorem.** No exact reflected OT Einstein connector on [0,R] × T³ (with free T² action and totally geodesic scalar-(−6) center) can have exit orbit energy density sup_{exit} e < 12. In particular, no exact connector reaches the Step 73 expanding tail interface.

**Proof.** If sup_{exit} e < 12, then by (4.2):
\[
\sup e \le \max\{6, \sup_{\text{exit}} e\} < 12.
\]
But e is continuous and e(0,z) = |U_s(0,z)|² for all z. Since ⟨e(0,·)⟩_μ ≥ 12 (eq. 5.1) and the μ-average uses positive weights, there exists z₀ with e(0,z₀) ≥ 12. This contradicts sup e < 12. ∎

**Consequence for the expanding tail.** The Step 73 tail has orbit-map energy e → 0 as the anisotropy cutoff is extended. Any connector reaching this tail must have small exit e. Since exact connectors require sup_{exit} e ≥ 12, the exact graph connector is impossible.

**Comparison with Step 79.** Step 79's convex-distance maximum principle showed that exact connectors cannot reach a *constant* exit (orbit map = constant at exit). The Bochner comparison is strictly stronger: it excludes *all* exits with orbit energy below 12, including nonconstant exits with small gradients.

## 7. The forced case: tension identity and stability question

For τ_σ = F ≠ 0, the **tension identity** (verified by TTCS):
\[
\langle dU, D\tau_\sigma \rangle = \operatorname{div}_\sigma(V) - |\tau_\sigma|^2,
\tag{7.1}
\]
where V(X) = ⟨dU(X), τ_σ⟩_{H²}.

**Forced Bochner formula:**
\[
\frac{1}{2} Le = |DdU|^2 + \operatorname{div}_\sigma(V) - |F|^2
+ Q - 3e + \tfrac{1}{2}|dU(\nabla\sigma)|^2 + E_B:A.
\tag{7.2}
\]

**Pointwise obstacle.** The div_σ(V) term contains DF (derivatives of the forcing), which differentiates the Ricci defect. The pointwise maximum principle does not close directly.

**Integrated estimate (correct only for the test \(\eta^2\)).** Multiplying by \(\eta^2\rho\) and integrating gives
\[
\int \eta^2\rho\,\operatorname{div}_\sigma(V) = -2\int \eta\rho\,\langle dU(\nabla\eta), F\rangle
+ \text{boundary flux}.
\]
This avoids \(DF\), but it is not the superlevel Caccioppoli test needed for Moser. With \(u=(e-k)_+\), the correct identity is
\[
\int\eta^2u\,\operatorname{div}_\sigma V\,d\mu
=-\int\eta^2\langle V,\nabla u\rangle d\mu
-2\int\eta u\langle V,\nabla\eta\rangle d\mu.
\]
The first term creates an \(O(|F|^2e)\) superlevel source and cannot be discarded. See Step 86 for the nonsingular Caccioppoli inequality and its natural threshold \(k_*=6+O(\delta)\).

**Stability question (reformulated in Step 86).** Small exit data yield a global superlevel integral estimate above the natural root \(k_*=6+O(\delta)\), while finite-dimensional \(CD(-(3+\delta),4)\) supplies normalized local doubling, Poincaré, and effective-four-dimensional Sobolev estimates on buffered balls. These inputs do not automatically yield \(\sup e\le6+C\delta\): one must still prevent a small-amplitude, rapidly varying orbit-defect layer from concentrating the excess in a tiny region, or prove a length-independent weighted Green/resolvent or spectral estimate from the full coupled area equation. Only such a near-sharp ceiling could be compared with \(\langle e(0,\cdot)\rangle\ge12-8\delta\).

## 8. A02 warped waist barrier (#614)

A02 establishes a complementary obstruction for warped-product turnarounds:

**Warped waist barrier.** For g = dr² + f(r)² g_F with Ric_F = 2k g_F at a waist (f'=0, f''≥0):
- k = 0 (flat T³ fiber): pointwise operator Ricci defect ≥ 3/2. Minimum at α = f''/f = 3/2.
- k > 0 (round S³ fiber): defect ≥ 3/2 + 3/(2f₀²) > 3/2 at every scale.
- k < 0 (hyperbolic fiber): defect-free waist exists, but H⁴ is already Einstein.

This is pointwise and cannot be amortized over volume. It blocks warped-product constructions for both graph manifolds (T³ fiber) and N#N connected sums (S³ neck).

**Comparison with Bochner.** The Bochner comparison (§6) applies to the full non-warped OT class but only in the exact case. The warped waist barrier applies only to warped products but gives a quantitative δ ≥ 3/2 including approximate metrics. They are complementary:

| Feature | Bochner comparison | Warped waist |
|---|---|---|
| Class | Full OT (non-warped) | Warped product only |
| Exact/forced | Exact: complete. Forced: open. | Both: δ ≥ 3/2 |
| Mechanism | sup e ≤ 6 vs ⟨e⟩ ≥ 12 | Gauss eq at f'=0 |
| Applies to | Graph (T³ fiber) | Graph + N#N |

## 9. Combined negative-branch assessment

The negative branch now has three established barriers and one remaining gap:

1. **Warped waist** (A02 #614): δ ≥ 3/2 for all warped-product turnarounds with k ≥ 0.
2. **Exact Bochner** (this step): exact reflected OT connectors require exit e ≥ 12, impossible for small-defect tails.
3. **N#N BCG scale** (A01 #610, A02 #615): for N#N with N hyperbolic, BCG+CGB forces δ ≳ 3/(4χ(N)).
4. **Non-warped forced connector**: the remaining frontier within the free-OT class. A non-warped metric with \(\|E\|\le\delta\) might overcome the exact Bochner bound through a thin divergence-forcing layer. Step 86 shows that ordinary local Moser does not by itself settle this; the missing object is a length-independent localization/resolvent estimate or an additional regularity consequence of the full coupled OT equations.

## 10. Step 83 corrections

- **Drift sign:** §5 used Ric_B + Hess σ. Correct: Ric_B − Hess σ. Changes the sign of orbit stress.
- **Benchmark:** dr²+cosh²(r)dz² with σ=2r is NOT an Einstein base. Correct: dr²+e^{2r}dz².
- **Eigenvalue claim:** "Universal radial −1" is unsupported. The correct tensor is −3γ+½dσ².
- **Closed geodesic:** No nonconstant closed geodesic in H². Every center loop has nonzero tension.
- **Conclusion:** Step 83 said Bochner doesn't close. After correction: Bochner gives a complete exact obstruction and the key open question for the forced case.

## 11. Numerical verification

`workspace/scripts/step85_bochner_numerical.py` verifies ½Le − ½e(e−6) ≥ 0 on the Step 73 expanding tail with k=1, ε=0.5:
- max e = 0.0567
- min gap = 1.27 × 10⁻⁹ (essentially zero, from |DdU|² + Q − ½e²)
- orbit equation residual = 5.6 × 10⁻¹⁷

## 12. Reproducible files

- `workspace/scripts/step85_bochner_comparison.py` — algebraic verification
- `workspace/data/step85_bochner_comparison.json` — complete results
- `workspace/scripts/step85_bochner_numerical.py` — tail numerical test
- `workspace/data/step85_bochner_numerical.json` — numerical results
- `trace/ttcs/results/step85_ttcs01_verifier1_integration.md` — TTCS verification

## 13. What is established and what remains

**Established:**
- Exact reflected OT Einstein connectors with exit e < 12 are impossible (Theorem §6).
- Warped-product waists have δ ≥ 3/2 regardless of collar length (A02 §8).
- The K-production analysis was seeking a solution to an impossible exact problem.
- The graph route requires forced (approximate) non-warped connectors.
- The precise forced stability question is identified (§7).

**Not established:**
- Whether the forced Bochner + Moser estimate gives geometry-independent L∞ bounds.
- Whether a non-warped near-waist lemma extends the warped barrier.
- Whether N#N constructions at defect O(1/χ) are possible with non-warped necks.
- The positive branch or all-dimensional resolution.

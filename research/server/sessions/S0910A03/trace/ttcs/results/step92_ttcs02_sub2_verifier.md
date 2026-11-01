# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step92_constrained_spike_koiso.py",
    "Sessions/S0910A03/workspace/data/step92_constrained_spike_koiso.json",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Knowledge/objects/papers/1106.2066-The-Cauchy-problems-for-Einstein-metrics-and-parallel-spinors--e588543ba837--cf493e3a7afe/object.md"
  ]
}
```

## Task

Verify a proposed exact family of analytic stable minimal T^3 Cauchy data for local Ric=-3g germs. Let P(s)>0 be analytic periodic on a circle. Choose a closed immersed curve U:S^1->H^2 with |U_s|^2=12+2P(s), and set q=ds^2+M(U(s))_{ab}dx^a dx^b with det M=1. Let A=(1/2)M^{-1}M_s. Choose a target unit normal N(s) perpendicular to U_s, let C_N=M^{-1}dM(N), and define a vertical tracefree Weingarten endomorphism B=sqrt(P/2) C_N, with W(T)=0 and W|vertical=B. Check carefully, in the normalization e_s=(1/2)tr[(M^{-1}M_s)^2], that: Scal_q=-e_s/2; tr W=0; tr W^2=P; the momentum constraint d tr W+delta W=0 is exactly tr(A B)=0 (and all other components vanish by T^2 invariance); the Hamiltonian constraint Scal_q+tr W^2-(tr W)^2=-6 holds; |II|^2=P and e_nu=2P; invariant stability is equivalent to -d_s^2+3-P>=0. If P is a sufficiently narrow analytic von Mises bump of fixed mass m<2sqrt(3)tanh(sqrt(3)L/2), does the stability hold for large concentration, and does Koiso's analytic theorem then yield a genuine local analytic Einstein germ with arbitrarily large e_nu on the center? Identify any hidden error: target-to-matrix normalization, momentum divergence connection terms, global closed curve/normal, analyticity, sign of W, or distinction between invariant and full stability. Explain exactly what this would establish for the connector route and what it would not.

## Output

## Verification memo — analytic stable minimal T³ Cauchy data for local Ric = −3g germs

**Verdict up front.** I re-derived all seven identities by hand (not relying on the numerics) and the construction is exact and correct. I found no error in the target-to-matrix normalization, in the momentum divergence, in the closed-curve/normal construction, in the analyticity input, or in the sign of W. One item the task lists as a possible hidden problem — the invariant-vs-full-stability distinction — actually resolves in this construction's favor: full stability follows from the invariant test here. The genuine substance to keep in view is not an arithmetic error but the reach of the conclusion: Koiso gives a genuine local analytic Einstein germ per fixed spike, but nothing about a uniform t-extent as the spike sharpens, and nothing about matching to two ends. I give the derivations and then the exact structural reasons each piece is tight.

---

### 1. Independent re-derivation of the seven identities

Write the T³ metric as q = ds² + M(s)_{ab}dx^a dx^b, det M = 1, and A := ½M⁻¹Mₛ. Two structural facts drive everything:

- **det M = 1 ⟹ tr A = 0**, since tr(M⁻¹Mₛ) = ∂ₛ log det M = 0.
- **√det q = 1 ⟹** for any function of s alone, Δ_{T³}φ = φₛₛ (no first-order drift term).

**(1) Scal_q = −eₛ/2.** The T² fibers are flat, so applying the Gauss contraction one dimension down (fiber shape operator Ŵ = −A, tr Ŵ = 0):
Scal_{T³} = 0 + 3 tr(A²) − 0 − tr(M⁻¹M_{ss}). Differentiating tr(M⁻¹Mₛ)=0 gives tr(M⁻¹M_{ss}) = tr((M⁻¹Mₛ)²) = 4 tr(A²). Hence Scal_{T³} = 3tr A² − 4tr A² = −tr A². Since eₛ = ½tr((M⁻¹Mₛ)²) = 2 tr A², we get **Scal_q = −eₛ/2**, i.e. with eₛ = 12+2P, **Scal_q = −6−P**. ✓

**(2) tr W = 0.** W(T)=0 and W|vert = B = √(P/2)C_N, C_N = M⁻¹dM(N). tr C_N = ∂_N log det M = 0, so tr B = 0. ✓

**(3) tr W² = P.** The H² metric induced by ½tr((M⁻¹dM)²) satisfies tr(C_V²) = 2|V|²_{H²}. With |N|²_{H²}=1, tr(C_N²)=2, so tr B² = (P/2)·2 = P; |II|² = |W|² = P. ✓ (The code verifies tr(C_N²)=2 indirectly through `max_norm_B_squared_minus_P ≈ 7e-14`.)

**(4) Momentum ⟺ tr(AB) = 0, exactly.** With ∇_{e_a}∂_s = A e_a and WT = 0, only the s-component of div W survives; a direct computation gives (div W)(T) = −tr(AB), and all vertical components vanish because M(s) is x-independent (flat fibers, zero intrinsic Christoffels, translation-invariant B). Now A = ½C_{U_s} and B = √(P/2)C_N, so
tr(AB) = ½√(P/2)·tr(C_{U_s}C_N) = √(P/2)·⟨U_s, N⟩_{H²}.
This is **zero exactly** because N was chosen H²-orthogonal to U_s — the momentum constraint is not a numerical near-miss, it is enforced by the orthogonality of the target normal. ✓ (`max_tr_A_B_momentum_residual ≈ 5e-14` confirms.) I checked specifically for the "connection terms" concern: no term proportional to ∂ₛB enters (∂ₛ) because W kills the T-slot, and no vertical divergence enters because B is fiberwise constant. The reduction to tr(AB) is complete.

**(5) Hamiltonian.** Scal_q + tr W² − (tr W)² = (−6−P) + P − 0 = **−6 = (n−1)λ = 2·(−3)**. ✓

**(6) e_ν = 2P.** In the germ, ġ_t = −2W ⟹ M_t = −2MB ⟹ M⁻¹M_t = −2B, so e_ν = ½tr((M⁻¹M_t)²) = 2 tr B² = **2P**, using the same H²-normalization as eₛ. The "12" in eₛ = 12+2P is exactly what makes Scal_q carry a fixed −6 background plus a −P that cancels the +P from |W|² in the Hamiltonian; the design is internally consistent, no factor error. ✓

**(7) Jacobi form.** T³ is minimal (tr W = 0) and Ric_Z(ν,ν) = λ = −3, so the stability operator is J = −Δ_{T³} − (|II|²+Ric(ν,ν)) = −Δ_{T³} + 3 − P. On T²-invariant φ(s), Δ = ∂ₛ², giving **−∂ₛ² + 3 − P**. ✓ For κ=800 the lowest eigenvalue is 2.72 > 0.

I found **no sign, factor, or normalization error** in any of these. The numerics (residuals 1e-13–1e-16) are consistent with the exact algebra I reproduced independently.

---

### 2. The invariant-vs-full-stability point resolves in the construction's favor

The general note (§2) rightly flags that the minimizing-loop argument only controls T²-invariant speeds. But for **this specific product T³**, invariant stability implies full stability. Since √det q = 1 and M^{ab}(s) is x-independent, J block-diagonalizes over the fixed Fourier basis e^{ik·x}:
J(ψ(s)e^{ik·x}) = (−ψₛₛ + M^{ab}(s)k_ak_b ψ + (3−P)ψ) e^{ik·x}.
For k≠0 the added potential M^{ab}k_ak_b > 0 strictly raises the lowest eigenvalue relative to the k=0 block. By min–max, the lowest eigenvalue of the full J equals that of the invariant operator −∂ₛ²+3−P. So the fiber modes are strictly stabilizing and **full stability = invariant stability** here. The concentration threshold m < 2√3 tanh(√3 L/2) ≈ 3.464 (from the square-well capacity limit A ℓ → 2√a tanh(√a L/2), a=3, L=2π) is therefore the genuine condition for full stability of arbitrarily narrow bumps. With m=1 this holds comfortably.

---

### 3. Analyticity is real, so Koiso gives a genuine germ (not merely formal)

Three points make Koiso's Theorem 2.1 (Ammann–Moroianu–Moroianu, Thm 2.1 / Koiso [42]) genuinely applicable:

- **P > 0 strictly and analytic.** The von Mises profile P = m·e^{κ(cos s−1)}/(L·i0e(κ)) is analytic and bounded below by a positive constant, so √(P/2) is analytic. This is why B is analytic. A literal compact-support bump would make √P non-analytic and would void Koiso; the von Mises choice is the correct one.
- **The closed curve is genuinely closed and analytic.** Taking a geodesic circle of radius R = arcsinh((∫v)/2π) in H² and reparametrizing by θ(s) with θ' = v/sinh R makes ∫₀^L θ' = 2π *exactly* (by the definition of R), so U(s) is L-periodic and analytic across the seam. The unit normal N = +π/2 rotation of U_s is single-valued and analytic on the oriented H² (no monodromy). The residuals (`max_speed_squared_residual`, `max_unit_normal_residual`, `max_tangent_normal_inner_product` ≈ 1e-14–1e-16) confirm the exact-arithmetic reasoning.
- **The sign of W is immaterial** to the constraints (tr W, tr W², and tr(AB)=0 are all sign-insensitive), and both ±W yield valid analytic germs with the same e_ν = 2P.

Consequently, for each fixed κ the data (q, W) is analytic and satisfies (2.9)–(2.10), so Koiso produces a **genuine analytic Einstein metric** g^Z = dt²+g_t with Ric = −3g^Z on some neighborhood (−ε,ε)×T³, with T³ a stable minimal slice carrying e_ν = 2P, sup e_ν = 2 P_max → ∞ as κ → ∞. This is an actual metric, strictly stronger than the formal-jet spike of note §5.

---

### 4. What this establishes, and what it does not

**Establishes (for the free-T² connector analysis):** slice-level data — Jacobi stability, the Hamiltonian and momentum constraints, |II|², and orbit-trace information — **cannot bound the normal orbit energy e_ν**. The obstruction one might hope to build from a single stable minimal separator does not exist: there are genuine, fully stable, analytic minimal T³ separators inside real local Einstein (Ric=−3) metrics with arbitrarily concentrated e_ν at the center. This confirms, with an actual germ rather than a formal series, the caution in §5 that any e_ν control must originate at collar/global scale.

**Does not establish:**

1. **Uniform germ t-extent.** Koiso's ε is not controlled as κ → ∞. The e_ν→∞ family lives on collars whose t-width may shrink to 0. A connector needs a t-interval of definite size joining two ends; nothing here provides that. This is the single most important thing the germ does *not* deliver, and it is exactly why sup-e_ν across the family does not translate into a usable structure.
2. **Two-ended matching.** The germ is one collar around a minimal slice; it imposes no prescribed asymptotics and is not glued to the rest of a manifold M. The remaining horizontal reduced equations and Codazzi–Bianchi compatibility are not part of Koiso's slice data.
3. **Any resolution of Yau 26 in this class.** It neither constructs a connector nor excludes one, does not touch the positive-λ branch, non-free-T² or non-symmetric metrics, and — even if a slice obstruction had existed — a perturbative obstruction on this symmetry class would not exclude unrelated Einstein metrics on the smooth T³ (or its products). The note's §6–§7 statement of the remaining collar-transport question is the accurate placement.

**Net:** the file is mathematically sound; the "spike" it exhibits is real Einstein geometry, not a formal artifact. Its function is to close off the slice-level route to bounding e_ν and to sharpen the remaining question to a collar-scale transport/regularity statement (uniform germ width plus two-ended matching), which is where any exclusion in the free-T² class would have to come from.
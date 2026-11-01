# Step 52 — The kernel-direction Burns insertion theorem on an arbitrary Einstein background

Session S1003A01, Agent2, Step 52. Status labels: **[E]** exact symbolic/rational computation;
**[P]** written proof; **[C]** conditional or relies on an inherited result named explicitly;
**[N]** floating evidence only.

This note supersedes the open items of Step 51 (item (A) of its handoff) and the conditional status of
Step 50 Theorem 3.1. The inherited inputs are: the Step-50 exact W⁻ identity
(`workspace/scripts/step50_exact_identity.py`, `data/step50/exact_identity.json`), the CGB pointwise identity,
and **one** statement of Ch. 5 of `web_research_collected.tex` (the CH perpendicular construction has no
order-ε term, eq. (5.A)), used only to fix the order-ε flux constant up to a nonzero factor (§3.3).
The Ch. 5 value −18 is **no longer an input**: it is reproduced exactly below.

## 1. Setting and notation

(X,g) Einstein, Ric = (s/4)g, p ∈ X, normal coordinates x on B_{4T}(p). Λ⁺_p is identified with
span(J₁,J₂,J₃) (quaternionic structures, quaternion convention of the Step-49–52 scripts), the Burns orientation
ζ = J₃; v_m = J_m x, v₀ = x, u = |x|², P_m = v_m v_mᵀ/u.

R⁺ = W⁺ + s/12 on Λ⁺ (eigenvalues sum to s/4); μ_ζ = R⁺(ζ,ζ); T = trace-free part of R⁺ restricted to
ζ^⊥ ∩ Λ⁺ (a 2×2 symmetric matrix in an orthonormal basis), |T|² = (μ₁−μ₂)²/2 when ζ is an eigenvector.

Flat Burns: δ + εk_B, k_B = (v₁v₁ᵀ + v₂v₂ᵀ)/u² (indices m = 1,2 ⊥ ζ), exactly ASD and scalar-flat,
exceptional sphere of area πε, Kähler form ζ (self-dual in X's orientation, so the blow-up is X#CP̄²).

Chiral curvature 𝒞 = (2W⁺, s/√12); f(g) = |𝒞|² dV_g. Pointwise CGB:
|Ric°|² dV = f − 16π² e − 24π² l (e Euler, l signature density). Hence for closed M,
P(g) = ∫_M f(g) − 8π²(2χ+3τ)(M).

## 2. The exact local coefficient [E]

Scripts: `workspace/scripts/step52_exact_su2minus_fast.py` (exact rational quadratic form by polarization,
truncated bivariate (a,ε) arithmetic in Fractions, 0.2 s per evaluation) and `step52_analyze_Q.py`.
Data: `workspace/data/step52a/exact_su2minus_Q.json`, `exact_su2minus_analysis.json`.

**Reduction.** If W⁻_p = 0 and Ric°_p = 0, every ingredient (the 2-jet h₂ = −(1/3)R_{ikjl}x^kx^l,
k_B, and correctors built from x and the v_m) is SU(2)₋-equivariant; SU(2)₋ commutes with the J_m and acts
transitively on S³. For SU(2)₋-invariant correctors the a²ε² CGB density is therefore **constant on S³**, so
F = density(x₀)/4 exactly. The corrector functional is convex (its Hessian is the flat (W⁺,s)-linearization
norm), so its infimum over any SU(2)₋-stable class of degree-0 correctors is attained on the invariant ones:
the 10 tensors sym(v_i v_jᵀ)/u, 0 ≤ i ≤ j ≤ 3. This is the full answer in the (s,W⁺) sector, for an
**arbitrary** W⁺ (U(1)₊ rotation allows w₂₃ = 0 without loss).

**Checks inside the run.** The a-linear W⁺ and s of the jet equal the prescribed (w, s) exactly; CH k_B-only
gives F = 12 exactly (Step 49 floating 11.9999999999); the [aε] coefficient and the pure-Burns ε² coefficient
vanish identically for all 120 polarization vectors.

**Theorem 2.1 [E].** Let ζ be an eigenvector of W⁺_p (w₁₃ = w₂₃ = 0). Over all degree-0 correctors in the
(s,W⁺) sector,

  F_opt(Rm_p, ζ) = −μ_ζ(μ_ζ − s/8) − |T|²,

exactly (output `Fopt`, `Fopt_minus_Phi_w13=0 = −2w₁₂²`, which is precisely the off-diagonal part of
−(μ₁−μ₂)²/2 in a non-eigenbasis of ζ^⊥). This is A02's Theorem 57.Φ, now an exact theorem in this sector,
obtained by an independent normal-coordinate computation. Special values: U(2) locus reproduces
(s−24λ)(s+12λ)/288 (Step 51) exactly; W⁺ = 0 gives +s²/288 > 0.

**Theorem 2.2 (explicit kernel corrector) [E].** On the kernel locus μ_ζ = 0, with A = −s/12, the family

  k₀^{ker} = (7A/4)(P₁+P₂) + (A/2)P₃ + (1/3) Σ_{i,j≤2} T_ij (J_i x)⊗(J_j x)/u

(Spirit #61) satisfies F(k₀^{ker}) = −|T|² identically in (s, T), and the gradient of F at k₀^{ker} vanishes in
all 10 directions: it is an exact minimizer, not only a competitor. At s = −24, T = diag(3,−3) its coefficients
are (4.5, 2.5, 1), the degree-zero part of the Ch. 5 neck c_* = (9/4,3/4,1/2) (the extra +1 on the Kähler
fibre is the C² = 1 + t² + … factor of the CH radius). Hence the Ch. 5 value −18 = −|T|² is reproduced exactly.

**W⁻ and Ric° sectors.** The integrated F is SU(2)₋-invariant on (jet ⊕ corrector) space. The (s,W⁺)-jets and
k₀^{ker} are SU(2)₋-invariant; W⁻ and its corrector k₀^W = (3/2)sym(h_W k_B) − (1/4)tr(h_W k_B)δ lie in the
spin-2 isotypic part. Cross terms vanish by irreducibility, and the W⁻ self-term vanishes pointwise by the
Step-50 exact identity. So **for every Einstein 2-jet with ζ ∈ ker R⁺_p,**

  F(k₀^{ker} + k₀^W) = −|T|²   [E + representation theory].

(Ric° = 0 for Einstein. For non-Einstein jets the Ric° self-term is ≥ 0 and floating-zero, Step 51 [N];
a closed-form Ric° corrector is being sought in `scripts/step52_ric0_corrector.py`, see §7.)

**Mixed block [E].** If w₁₃ ≠ 0, F contains 2w₁₃(−9c₂ + 15c₆ + 7w₁₃)/9, where c₂ multiplies sym(x⊗J₂x)/u,
a null direction of the corrector Hessian (it is L_{(log r)J₂x}δ, a rotation of the Burns orientation by an
angle growing like log r). The log coefficient is then unbounded below. This happens whenever the mixed block is nonzero; combined with μ_ζ = 0 it forces R⁺ indefinite; there a direction with μ > 0 already gives a first-order saving, and rotating ζ
along the neck exploits the gradient 2R⁺(ζ,ζ'). On R⁺ ≤ 0, μ_ζ = 0 forces R⁺ζ = 0, so this does not occur.

## 3. The two-scale construction and its remainder [P]

### 3.1 The metric
Fix T ≤ inj(p)/4 small, cutoffs χ_in(ρ) (0 on ρ ≤ 1, 1 on ρ ≥ 2), χ_out(ρ) (1 on ρ ≤ 1, 0 on ρ ≥ 2), and
k = k_B + k₀, k₀ = k₀^{ker} + k₀^W (degree 0, smooth on R⁴∖0). Define

- r ≤ T:  g_ε = δ + εk_B + χ_in(r/√ε)·[(g − δ) + εk₀];
- r ≥ T:  g_ε = g + ε χ_out(r/T)·k;  g_ε = g outside B_{2T}.

The formulas agree on 2√ε ≤ r ≤ T (both equal g + εk). On r ≤ √ε, g_ε is exactly flat Burns, which extends
smoothly over the exceptional sphere (blow-up of (C², J₃) at 0, self-intersection −1 in X's orientation).
Positivity holds for ε small since k_B ≥ 0, g − δ = O(r²), εk₀ = O(ε). So g_ε is a smooth metric on
M = X#CP̄², identical to g outside B_{2T}(p).

Since 2χ+3τ drops by one, P(g_ε) − P(g) = 8π² + Δ, Δ = ∫_{B̃} f(g_ε) − ∫_{B_{2T}} f(g).

### 3.2 Region estimates
Scale invariance: in polar coordinates ∫_{r₁<r<r₂} f(g) = ∫ (dr/r) ∫_{S³} f(ĝ_r)(θ) dθ with
ĝ_r = r⁻²Φ_r^* g (Φ_r(x) = rx).

**Core, r ≤ 2√ε.** ε⁻¹Φ_{√ε}^* g_ε = Burns₁ + χ(|x̂|)·ε·m_ε(x̂) with m_ε bounded in C^k on 1 ≤ |x̂| ≤ 2; on
|x̂| ≤ 1 it is exactly Burns (f = 0). Since 𝒞(Burns) ≡ 0 and f is quadratic in 𝒞, f = O(ε²) there; the core
contributes O(ε²), as does ∫_{B_{2√ε}} f(g).

**Neck, 2√ε ≤ r ≤ T.** With z = ε/r²,
  ĝ_{r} = δ + G(r,x) + z k_B(x) + z r² k₀(x),  G(r,x) = g(rx) − δ = r²h₂ + r³h₃ + … (Cartesian components; TTCS repair of an erroneous r⁻² factor),
smooth in (r, x) up to r = 0. Put Ψ(r,z) = (8π²)⁻¹∫_{S³} f(ĝ_{r,z}); Ψ is smooth on [0,T]×[0,1/4].
(a) Ψ(0,z) = 0 (flat Burns). (b) Ψ is even in r: the antipodal map x ↦ −x has det +1, preserves S³ with its
orientation, fixes k_B and k₀ (even tensors) and maps h_m to (−1)^m h_m, i.e. r to −r.
(c) 𝒞(ĝ) = r²𝒞₂(z) + r³𝒞₃(z) + … (no r¹ term), so Ψ = O(r⁴) uniformly in z.
Let R = Ψ(r,z) − Ψ(r,0) − z∂_zΨ(r,0). R vanishes to order 4 in r and order 2 in z, so by Hadamard
R = r⁴z²ρ(r,z) with ρ smooth, ρ even in r, and ρ(0,0) = (8π²)⁻¹∫_{S³}[a²ε²]f = F (§2: only h₂ and k₀ enter,
since the r⁴ coefficient of |𝒞|² is |𝒞₂|²). With |ρ − F| ≤ C(r² + z):
  ∫_{2√ε}^{T} R dr/r = ε² ∫ ρ(r, ε/r²) dr/r = (F/2) ε² log(1/ε) + O_T(ε²),
using ∫ r dr ≤ T²/2 and ∫ ε r⁻³ dr ≤ 1/8 as in Ch. 5. The term Ψ(r,0) is the background and cancels.

**Outer transition, T ≤ r ≤ 2T.** f(g + εχk) = f(g) + ε Df_g[χk] + O_T(ε²).

### 3.3 The order-ε term is a flux, and vanishes on the kernel
The z-linear neck term and the outer linear term together equal ε∫_{r≥2√ε} Df_g[χ_out k] dV (the z-coefficient
at fixed r is the ε-derivative of f(g + εk)). Since g is Einstein, D(|Ric°|² dV)_g = 0 pointwise, and the
variations of the Chern–Weil forms are exact: Df_g[h] = dΘ_g(h), Θ linear and local in h. Because χ_out k = 0
near r = 2T,
  ε∫_{r≥2√ε} Df_g[χk] = −Λ(2√ε),  Λ(r) := ε∮_{S_r} Θ_g(k).
Θ is scale invariant and vanishes at the flat metric (CW forms are quadratic in curvature), so
Λ(r) = ε[θ₂ + θ₃ r + O(r²)] + ε·O(r²) (the k₀ part starts at r²), and θ₃ = 0 by the antipodal parity. Thus the
order-ε contribution is −εθ₂ + O(ε²), where θ₂ is bilinear in (Rm_p, k_B): a U(2)_ζ-invariant linear function of
Rm_p. The only such invariants are s and W⁺(ζ,ζ) (W⁻, Ric° and T carry nontrivial SU(2)₋ or U(1)₊ weight), so
θ₂ = αs + βW⁺(ζ,ζ).

**Direct computation (TTCS step52 verifier, replaces the calibration below) [P].** With f − |Ric°|²dV = 8π²p₁(Λ⁺) and Θ_g(h) = −2tr(Ȧ⁺[h]∧F⁺): the flat Burns family is Kähler for J_ζ, its Λ⁺-connection variation is Ȧ⁺[k_B] = L_ζ·r⁻²η (η = r⁻²ι_xΩ, Ω = √2ζ, ∫_{S³}η∧dη = 4π²), and the L_ζ-component of F⁺ pairs through μ_ζΩ, giving θ₂ = 8π²μ_ζ. Hence the order-ε term is exactly −8π²εR⁺_p(ζ,ζ), i.e. ℓ = −μ_ζ in P/8π² units (agreeing with Step 50). The Ch. 5 calibration that follows is retained only as a consistency remark: the verifier notes that its normal-coordinate equivalence (singular linear part a multiple of k_B modulo gauge and degree ≥ 0 terms) was not established from the supplied material.

Calibration [C: Ch. 5 (5.A), superseded]. Ch. 5's CH construction (Ric = −6g, ζ ⊥ ω, a kernel direction since
R⁺_CH = (−6,0,0)) has in normal coordinates the same two-scale form with k_B at leading order (its extra
terms are degree ≥ 0 and enter Λ only at O(εr²)), and its theorem has no order-ε term. Hence
α·(−24) + β·2 = 0, i.e. θ₂ = β·R⁺(ζ,ζ) (β = 12α). The Kähler period law of Step 8 (aligned Kähler collar, P = 2(2π − λt)² + L/4, t the exceptional
period, λ the Einstein constant) has a nonzero first-order term in t whenever λ ≠ 0, and the aligned direction
has R⁺(ω,ω) = s/4 ≠ 0; so β ≠ 0, with cost −εθ₂ ∝ −R⁺(ζ,ζ) (positive for negative KE, μ_ω = s/4 < 0, and a
saving for positive KE, as in Step 8). This agrees with the TTCS-derived flux
ℓ = −R⁺_p(ζ,ζ) of Step 50; only its vanishing on ker R⁺ is used below.

### 3.4 Theorem
**Theorem 52.A (kernel insertion) [P, with §2 exact and the Ch. 5 order-ε calibration].** Let (X,g) be an
Einstein four-manifold, p ∈ X, ζ ∈ Λ⁺_p a unit vector with R⁺_pζ = 0, and T the trace-free part of R⁺_p on
ζ^⊥. The metrics g_ε of §3.1 (with k₀ = k₀^{ker} + k₀^W) are smooth on X#CP̄², equal g outside B_{2T}(p), and

  P(g_ε) = P(g) + 8π² − 4π²|T|² ε² log(1/ε) + O(ε²),

with O(ε²) depending on g|_{B_{4T}(p)}, ζ, T and uniform for (p,ζ) in compact sets. If X is closed, P(g) = 0
and, for T ≠ 0 and ε small, P(g_ε) < 8π².

Remarks. (i) Every negative or positive KE point, ζ ⊥ ω: T = diag(s/8, −s/8), |T|² = s²/32 (= 18 at s = −24,
giving −72π²ε² log(1/ε) = 8π²·(−9ε² log(1/ε)), Ch. 5). (ii) No smallness of W⁻ and no CH collar is required.
(iii) The fixed-configuration use needs only one such (p,ζ) and one fixed small ε; uniformity over moving
insertion data is not needed for that contradiction (Spirit #61). (iv) This is an upper construction only.

**Corollary 52.B.** For an Einstein point p, a Burns insertion lowers P below P(g)+8π² at leading order iff
either R⁺_p has a positive eigenvalue (first order, ζ = that eigenvector) or R⁺_p has a kernel vector with
T ≠ 0 (ε² log order) — within this two-scale ansatz with fixed degree-0 correctors and at these two orders.
Full expansion for an eigenvector ζ: (P(g_ε) − P(g) − 8π²)/8π² = −μ_ζε + ½[−μ_ζ(μ_ζ − s/8) − |T|²]ε²log(1/ε) + O(ε²).
No decrease at these orders exactly in the cases (i) R⁺_p < 0; (ii) s < 0, spec R⁺_p = (0, s/8, s/8)
(W⁺ = diag(−s/12, s/24, s/24), Derdziński degenerate type); (iii) R⁺_p = 0 (s = 0, W⁺ = 0).

## 4. No open degenerate-kernel stratum on an Einstein metric [P]

**Lemma 52.C.** Let g be Einstein with s < 0 on a connected open set U on which W⁺ has eigenvalues
(a, −a/2, −a/2), a = −s/12. Then U = ∅.

Proof. The simple eigenvalue gives a smooth (up to sign, locally) unit self-dual form u with
W⁺ = (3a/2)(u⊗u) − (a/2)·Id_{Λ⁺} (|u|² normalized so u⊗u is the orthogonal projector), a constant.
Einstein metrics satisfy δW⁺ = 0 (second Bianchi + Ric parallel). The identity term is parallel, so
∇^i(u_{ij}u_{kl}) = 0, i.e. (δu)_j u_{kl} + u_{ij}∇^i u_{kl} = 0. Contract with u^{kl}: |u|² constant gives
u^{kl}∇u_{kl} = 0, hence δu = 0. Then u_{ij}∇^iu_{kl} = 0 for all j,k,l; u is nondegenerate (u² = −c·Id), so
multiplying by u^j_m gives ∇_m u_{kl} = 0. A parallel self-dual form makes g Kähler with W⁺(u) = (s/6)u, while
here W⁺(u) = a u = −(s/12)u; equality forces s = 0, contradiction. ∎

Consequently, for s < 0, the contact set Z = {p: λ_max(W⁺_p) = −s/12, λ_mid = λ_min} of an Einstein metric with
R⁺ ≤ 0 is closed with empty interior (for s = 0, R⁺ ≤ 0 forces R⁺ ≡ 0, a separate branch; s > 0 is impossible). The maximum principle does not remove isolated contact: at p ∈ Z, with e the top
eigenvector extended radially parallel, φ = ⟨W⁺e,e⟩ has Δφ(p) = ⟨ΔW⁺ e,e⟩ = (s/2)a − 6a² + 2|W⁺|² = −9a² < 0
(Einstein formula ΔW⁺ = (s/2)W⁺ − 6W⁺∘W⁺ + 2|W⁺|²Id, checked on KE), consistent with a maximum. The lemma
does not apply to non-Einstein P-critical bulk, and does not by itself produce T ≠ 0 kernel points nearby.

## 5. Consequences for the degeneration chain, with the correct sign statement

In A02's energy-equality configuration (Theorem 53.B), bubble movement plus Theorem 52.A excludes Einstein bulk
points with a positive R⁺ eigenvalue and kernel points with T ≠ 0. Any surviving Einstein bulk satisfies
R⁺ ≤ 0 everywhere, R⁺ < 0 off a closed set Z with empty interior, and λ_max(W⁺) ≤ |s|/12, so
|W⁺|² ≤ s²/24 with equality nowhere (equality needs eigenvalues (a,a,−2a), a two-dimensional kernel with T ≠ 0).

Correction to the "negative on the whole cone" reading: F ≤ 0 is the conclusion **on the kernel**. In the
interior R⁺ < 0 the log coefficient can be positive (W⁺ = 0: F = s²/288 > 0; generally
−μ_ζ(μ_ζ − s/8) > 0 when s/8 < μ_ζ < 0); it is subordinate to the positive first-order cost −εθ₂ ∝ ε|μ_ζ|.
The strictly negative cone (e.g. real hyperbolic metrics, W⁺ = 0) is a genuine survivor and is a global problem,
not a remainder term. LeBrun's Weyl estimate with Gauss–Bonnet does not exclude it when c₁² = A
(1/4 + 2t − 5t² ≥ 0 on [0,1/2], t = √6|W⁺|/|s|; Step 51).

## 6. Relation to the four public problems
- Problem 2 (optimal P on blow-ups): p_*(X#CP̄²) < 8π² for every Einstein X having a kernel point with T ≠ 0
  — all KE surfaces of either sign — strengthening Step 50 from KE-collars to arbitrary Einstein kernel points,
  with an explicit closed-form corrector. Replication on covers and the Yamabe shortcut (Step 50 §4) give the
  strict sub-four slope on covers of any fixed such base. No lower bound is implied.
- Problem 3 (attainment / non-Bach-flat minimizers): the theorem supplies the local strict-decrease input in the
  fixed energy-equality configuration; what remains open is the R⁺ < 0 bulk branch and isolated contact.
- Problem 1: the surviving pointwise constraint t ≤ 1/2 is exactly the missing t-distribution information of
  Step 48; excluding Einstein bulk with t ≤ 1/2 on a manifold with an SW basic class and c₁² = A needs a
  differential/global input.

## 7. Open items
1. Closed-form Ric° corrector (non-Einstein P-critical bulk). `step52_ric0_corrector.py` (data/step52/ric0_corrector.json):
   the 17-tensor natural span contains a floating solution (least-squares residual 1e-14, rank 12 of 17, so
   non-unique), but naive rationalization (limit_denominator) gave wrong rationals and the symbolic identity check
   failed. Next: exact rational solve with the 5 free parameters fixed (e.g. eliminate dependent columns), then
   re-verify. Averaging-closed corrector classes are required in the §2 averaging statement (TTCS repair).
2. Non-Einstein bulk: the order-ε term acquires the bulk first variation DP_g[χk] unless g is P-critical, and
   Lemma 52.C uses δW⁺ = 0.
3. The ε² analysis at isolated contact points of Z and whether bubbles can be moved to nearby T ≠ 0 kernel
   points (kernel points are only on Z when R⁺ ≤ 0, so this reduces to the R⁺ < 0 branch near Z).
4. The R⁺ < 0 global branch (Problem 1 link).

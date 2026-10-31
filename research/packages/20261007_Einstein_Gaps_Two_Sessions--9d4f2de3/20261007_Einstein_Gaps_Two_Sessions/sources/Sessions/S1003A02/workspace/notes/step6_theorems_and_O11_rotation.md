# Step 6 — Theorem library entries (L′, structural quadratic, K, Z) and the O11 relative-orientation computation

Conventions: `Skills/geometric-analysis/references/conventions-and-literature.md`
(V, S=∫s², P=∫|Ric°|², W=∫|W⁺|² operator-HS, T₊=2χ+3τ, p=(a⁺_g)², D_β, E, J).
Session sources: `notes/step4_O10_localization_and_orbifold_test.md`,
`trace/ttcs/results/step5_ttcs01_verifier1_integration.md` (full proof of L′, K),
`trace/ttcs/results/step5_ttcs01_verifier2_integration.md` (zero-gap, Ozuch direction).

This note organises the mathematics in three layers, because the Step 4–5 work showed they are
genuinely different objects:

* **alignment defects** κ_β = ⨍|Ric+g|² + D_β/V (field–curvature alignment for an actual monopole);
* **the Einstein defect** E(g) = inf_λ ∫|Ric−λg|²/(λ²V) and α(M) = inf_g E(g);
* **bridges**: E ≤ κ-type bounds go one way only; the canonical-model sequence (Theorem Z) shows
  κ_β (β≠2) can stay ≥ 4(β−2)²/β while E → 0.

---------------------------------------------------------------------------------------------

## 1. Theorem L′ (density-free alignment endpoint below ratio 3/4)

**Statement.** Fix θ<3/4. Let M be closed oriented, [g] a conformal class, and suppose one fixed
Spin^c structure with determinant class a admits an unperturbed monopole for every metric of [g].
Put p=(a⁺_h)² (conformally invariant), and assume p ≥ A > 0, a² ≥ T₊, T₊ ≤ θA. Then there is
c_L(θ)>0 depending only on θ with

  κ_β(h) ≥ c_L(θ)   for every h∈[g] and every finite β ≥ 2.

No Euler-density hypothesis enters. The hypothesis a² ≥ T₊ is used only when 2/3 ≤ θ < 3/4.

**Proof** (complete; verified by two independent branches, Step 5): exact rewriting
Vκ_β = (13/12+1/β)S + (6β+10)W + ∫(s+4)²/4 − 8π²T₊ − 72π²p; LeBrun split
72π²p ≤ (1+1/γ)S + 6(1+γ)W; optimal γ_max=(9β−θ+6)/(9+θ) cancels W and gives
κ_β ≥ 16a/(1+4a) with a(θ,β)=N_θ(β)/(β(9β−θ+6)); three cases T₊≤0 (κ_β ≥ 1), θ<2/3
(N_θ>0 everywhere), 2/3≤θ<3/4 (bad interval (β₋,β₊)∋8 handled on the Yamabe representative
by the single-parameter theorem with its true factor b=(−a²)₊/V̂ = 0, transfer
κ̂_β ≤ κ_β/(1−√κ_β−κ_β/16), 0≤δ≤D_β). Full text with every inequality: verifier-1 integration
§§2–4. The constant does not survive θ↑3/4 because a_∞(θ)=1/12−θ/9.

## 2. Structural theorem: one quadratic produces 2/3, β=8 and 3/4

N_θ(β) = (3/4−θ)β² + (1/2−11θ/4)β + 6−θ,  disc N_θ = (57/16)(θ−2/3)(θ+142/19).

(i) θ<2/3: N_θ>0 for all β; (ii) θ=2/3: N_{2/3}(β)=(β−8)²/12 (double root at β=8);
(iii) 2/3<θ<3/4: N_θ<0 exactly on (β₋,β₊) with 2<β₋<8<β₊; (iv) θ=3/4: leading coefficient
vanishes, a_∞=0. Together with the Chern–Weil identity D₈ = 108π²(T₊−(2/3)p) + (27/2)P,
this shows that LeBrun's Einstein-obstruction ratio 2/3, the corpus's aligned parameter β=8, and
the large-parameter threshold 3/4 are the discriminant zero, its double root, and the vanishing
of the leading coefficient of a single quadratic. Interpretation: the elementary Chern–Weil +
LeBrun information is exhausted precisely in the window T₊ ≥ (3/4)A, β→∞, whose zero
sequences would have to saturate LeBrun's W⁺-improved estimate at W⁺=0 (p/V→2/(9π²),
T₊/p→3/4). This is the only place where Euler density can matter.

## 3. Corollary K (Kähler blow-ups)

X minimal Kähler of general type, p_g ≥ 1, A=c₁²(X), M=X#k CP̄². Universal c_K>0:
κ_β(g) ≥ c_K(β−2)²/β² for all metrics, all β≥2. Proof: sign averaging p ≥ A, a²=T₊=A−k;
k ≥ 0.3A → L′ with θ=0.7; k<0.3A → Noether gives χ/A ≤ 53/10+36/A ≤ 41.3 → finite-density
theorem. c_K=min{c_L(7/10), c_FD(41.3)}. The (β−2)² factor is necessary (KE: κ_β=4(β−2)²/β).

---------------------------------------------------------------------------------------------

## 4. Theorem Z (the h=0 endpoint of the balanced theory) — statement and scope

Let X be a compact minimal complex surface of general type, M its underlying smooth manifold.

(Z1) α(M)=0. Construction: canonical model X_can has only ADE singularities and carries an
orbifold Kähler–Einstein metric g_KE with Ric=−g (Kobayashi, Tsuji, Aubin–Yau in orbifold form);
glue Kronheimer ALE hyperkähler metrics of scale ε into each singular point via cut-offs in an
annulus ε^{1/2}-type. Ricci residual is O(1) on a region of volume O(ε²) (plateau + annulus) and
O(ε^2/r^4)-small-times on the transition, so ∫|Ric+g|²/V → 0, hence E→0.
(Ricci-flat cores contribute zero; E is scale-invariant, so normalisation is irrelevant.)

(Z2) Attainment. Because E=(4P+L_s)/R ≥ 0 with E(g)=0 iff Ric=λg with λ≠0, the infimum 0 is
attained iff M carries an Einstein metric with non-zero Einstein constant. (A Ricci-flat metric
has E=4.) For general-type M, λ>0 is impossible (b₊ ≥ 1 with SW class excludes positive
Ricci ... actually λ>0 forces finite π₁ and positive Yamabe, excluded by the SW class), so
attainment ⇔ existence of a negative Einstein metric on M.

(Z3) K_X ample ⇒ attained (Aubin–Yau). K_X nef, not ample ⇒ no KE metric for the given complex
structure; the smooth question (another complex structure obtained by smoothing X_can, or a
non-Kähler Einstein metric) is open in general and is *exactly* the attainment question for α.

(Z4) Local obstruction structure (A₁ points, Ozuch's first two compact obstructions). In the
Kähler splitting of Λ⁺ at a negative KE orbifold point, R⁺ = W⁺ + s/12 = diag(s/4,0,0) = diag(−1,0,0).
First obstruction: gluing direction ζ∈Λ⁺ must satisfy R⁺ζ=0. The holomorphic resolution direction
ζ∥ω fails it; directions ζ⊥ω (rotated hyperkähler / smoothing directions) pass it. The second
obstruction is the determinant of the residual 2×2 block of R⁺ on ω^⊥, which is 0 — passes
automatically. Hence the published obstructions forbid only the holomorphic resolution
direction: they do not exclude Einstein metrics near the orbifold built with ζ⊥ω.
Not derived for A_{k−1}, k≥3.

Attribution status: (Z1) is very likely known folklore in the Einstein/LeBrun–Kotschick
literature (almost-Einstein metrics on minimal surfaces with (−2)-curves); a literature check is
running (task s6_t1_tool2). What is specific to this programme: the equivalence (Z2) at the level
of α, its placement as the Q=0 (h=0) endpoint of the balanced family c·h ≤ α ≤ 4h/(1+h), the
contrast with the alignment defects (κ_β ≥ 4(β−2)²/β along the same sequence), and the
direction analysis (Z4).

## 5. Degeneration dichotomy — precise form and what is missing

Candidate Theorem D. Let g_j on fixed M have E(g_j)→0, normalised by λ_j=−1 (possible: the SW
class forces negative Yamabe type). Then V_j ∈ [2π²A, 12π²χ+o(1)] (LeBrun scalar bound and
Gauss–Bonnet), ∫|Rm|² ≤ 8π²χ+o(1). Claim: after passing to a subsequence, either (a) the
sequence is noncollapsed and converges to a negative Einstein orbifold with Ricci-flat ALE
bubble trees at finitely many points, or (b) it collapses on a set of positive measure.

What is proved in the literature: (a) holds for Einstein metrics (Anderson, Bando–Kasue–Nakajima)
and for critical metrics of quadratic functionals with a Sobolev bound (Tian–Viaclovsky).
What fails for arbitrary minimizing sequences: ∫|Ric+g|² → 0 is an L² (critical-exponent)
Ricci bound and gives no ε-regularity; conformal or bubbling defects of size o(1) in L²Ric can
in principle accumulate. The theorem therefore needs either an L^p (p>2) Ricci bound along the
sequence or selection of near-critical sequences with an equation that has ε-regularity. Which
hypothesis can be *supplied* (e.g. by a Ricci-flow smoothing of the minimizing sequence, which
preserves smallness of ⨍|Ric+g|² for short time and yields L^∞ control at scale √t) is the open
analytic step. This is the correct frame for the Braungardt–Kotschick Q=0 question: α=0 there
would require (a) a negative Einstein orbifold whose resolution is the non-Kähler symplectic
manifold, or (b) collapse.

---------------------------------------------------------------------------------------------

## 6. O11: the relative-orientation modulus of the blow-up cell (computation run this Step)

Script: `scripts/o11_rotated_cell.py` (curvature by automatic differentiation of the coordinate
metric; validated: flat ⇒ 0; CH ⇒ s=−24, Ric°=0, |W⁻_c|=0, |W⁺_c|²=24=s²/24; Burns ⇒ s=0,
W⁺_c=0; constant rotation ⇒ isometric invariants; θ=0 Kähler cell reproduces the U(2) code
P_K(0.01,1)=1.0618551601104 to 1e-14; identity residual (P−1)−(4ΔW⁺+ΔS/12)/8π² ≤ 2e-10).

Family: g = dx²/4G + h_ij s^i s^j, h = Rot₂(φ(x)) diag(x e^{w}, x e^{−w}, F) Rot₂(φ)^T.
φ ≡ θ near the bolt, φ → 0 (C²) at the CH boundary x=X; w, and the U(2) modes of F, G free.
This is the full SU(2)_L-invariant cell class with one free relative angle: since CH and Burns
are both SU(2)_L × U(1)-invariant, θ∈[0,π/2] is the *only* modulus of the tangent-space
identification modulo symmetries, i.e. exactly the angle between the Burns Kähler form ω_B and
ω_CH in Λ⁺. θ≠0 cells are non-Kähler for every complex structure compatible with either end.

### 6.1 Results (X=1, degU=6, degw=4, degr=6, 2×300 Gauss nodes; `data/o11rot/summary.csv`,
`figures/o11_rotation_slope.png`, localized-rotation runs `data/o11rot/loc_*.json`)

slope := (P_opt/8π² − 1)/x₀ (upper bound for the optimum in the family):

| x₀ | θ=0 | π/8 | π/4 | 3π/8 | π/2 | π/2 (localized rotation) |
|---|---|---|---|---|---|---|
| 0.001 | 5.956 | 6.950 | 9.581 | 13.107 | 16.894 | 15.37 |
| 0.003 | 5.900 | 6.828 | 9.207 | 12.205 | 15.200 | 14.30 |
| 0.01  | 5.779 | 6.651 | 8.771 | 11.208 | 13.395 | 12.97 |
| 0.03  | 5.619 | 6.447 | 8.324 | 10.236 | 11.721 | — |

All identity residuals (P−1) − (4ΔW⁺+ΔS/12)/8π² are ≤ 3e-10. In every cell both 4ΔW⁺>0 and ΔS>0.

What this shows.
1. **θ=0 reproduces the U(2) picture**: slope → 6 as x₀→0 with a negative second-order non-Kähler
   correction (ΔP_nonK ≈ −4.6e-4 at x₀=0.003, −4.1e-3 at x₀=0.01: exponent ≈ 1.8).
2. **Misalignment is penalized at first order.** P(θ)−P(0) ≥ 0 in every run and is of order
   x₀ (not o(x₀)): for small angles [P(θ)−P(0)]/(8π²x₀ sin²θ) ≈ 5.9–6.8, close to the Kähler
   slope itself. At θ=π/2 the penalty per x₀ grows slowly as x₀↓0 (≈1 per unit of log(1/x₀));
   the localized-rotation runs reduce it by only ~10%, and several optimizations stopped at
   iteration/line-search limits, so the log growth is not yet separated from parametrization
   effects. Empirical law at moderate angles: slope(θ) ≈ 6(1+sin²θ).
3. Consequently the relative-orientation modulus — the only remaining modulus of the
   SU(2)_L-invariant cell, and the one along which Malchiodi–Malizia's Weyl interaction
   W^M⊛W^Z ∝ (3cos²θ−1) changes sign — does not produce P(U)<8π²: the Weyl saving it could
   create is of order a⁴ while the misalignment penalty enters at order x₀ through *both*
   4ΔW⁺ (dominant) and ΔS. Within SU(2)_L-invariant cells the Kähler alignment is the
   first-order optimum; this is evidence for coefficient 4, not a lower-bound proof.
   Mechanism: the Burns r⁻² tail is anisotropic along ω_B, the CH quadratic jet is anisotropic
   along ω_CH (W⁺_CH ∝ diag(2,−1,−1) in (ω_CH,…)); the two anisotropies change sign at the
   crossover radius x ~ √x₀, and rotating the axis where both are O(√x₀) costs O(x₀ θ²).

Remaining O11 cell freedom not covered: cells without SU(2)_L symmetry (genuinely
four-dimensional profiles), cells whose exceptional region is not Burns-like (non-Kähler
ASD fillers), and fixed-scale cells far from the x₀→0 regime (x₀≥0.1 was covered only in U(2)).

---------------------------------------------------------------------------------------------

## 7. New consequence of the literature check: zero Einstein gap on non-Kähler minimal
##    symplectic manifolds (Theorem Z′), and why BK manifolds escape this mechanism

Sources read: Şuvaina, *The Yamabe invariant of a class of symplectic 4-manifolds*
(arXiv 1410.1236; Knowledge `The-Yamabe-invariant-of-a-class-of-symplectic-4-manifolds--93fc75a3247d`),
Theorem A, Prop. 4.1–4.2, §3 construction; LeBrun, *Kodaira dimension and the Yamabe problem*
(CAG 1999, cited there as [18]) for the Kähler/ADE case.

**Attribution of (Z1).** LeBrun's 1999 Yamabe computation for minimal Kähler surfaces uses exactly
the canonical-model orbifold KE metric with ADE ALE cores, and Şuvaina extends it to T-singularities
with Ricci-flat ALE Kähler rational balls B_{n,m}. Their sequences are built to make
∫s² → 32π²c₁²; on their interpolation annuli g−g_eucl=O(t²), ∂g=O(t), ∂²g=O(1) and the annular
volume → 0, while the cores are Ricci-flat and the bulk is Einstein. Hence the *same* sequences
satisfy ∫|Ric+g|²/V → 0. So (Z1) is a direct consequence of LeBrun 1999 / Şuvaina 2015 and must be
attributed to them; the α-level content added here is (Z2)–(Z4) and the endpoint placement.

**Theorem Z′.** Let N be the generalized rational blowdown (Şuvaina Theorem A) of linear chains of
type 1/n²(1,nm−1) in a complex surface M such that the contracted orbifold M̂′ has ample K. Then α(N)=0. (Blow-ups N#ℓCP̄² are not covered; whether the corpus lower bound c·h applies to them depends on
its supply hypotheses for N and must be checked separately.) In particular the simply connected, minimal,
symplectic, **non-Kähler** manifolds Y_n (n≥4) on the half-Noether line, c₁²=n−3, c₂=11n+3
(Prop. 4.2), have α(Y_n)=0. Proof: Şuvaina's metrics g_t on Y_n are orbifold KE outside shrinking
annuli, Ricci-flat Kähler ALE (B_{n−2,1} and the A_{n−4} resolution) inside, with bounded curvature
on annuli of volume → 0; E(g_t) ≤ ∫|Ric+g_t|²/V_t → 0. ∎ (Attainment on Y_n ⇔ a negative Einstein
metric on Y_n; none is Kähler–Einstein since Y_n is not complex.)

Consequence for the Q=0 question: **non-Kählerness alone does not create a positive Einstein gap.**
The strategist's "Einstein-gap version of O10" therefore cannot be a principle of the form
"Q=0 and non-Kähler ⇒ α>0".

**Why the Braungardt–Kotschick family (fixed c₁²=A, χ_h→∞) is different.** Y_n has bounded density
χ/A→11. For the orbifold-KE mechanism on a manifold with c₁²=A, the limit is a stable surface with
quotient (T or ADE) singularities and K ample, K²=A; by Alexeev's boundedness of stable surfaces with
fixed K² (to be retrieved and cited exactly), these form a bounded family, and the Ricci-flat ALE
Kähler fillers of a given group are finitely many (Kronheimer; Şuvaina/Răsdeaconu–Şuvaina
classification, Knowledge `ALE-Ricci-flat-Kahler-surfaces-and-weighted-projective-spaces`). Hence
**Proposition B (to be completed with the exact Alexeev statement):** for fixed A, only finitely many
diffeomorphism types arise as single-level Kähler-orbifold Einstein desingularizations with
c₁²=A. So on all but finitely many members of a BK sequence, α=0 would require a *non-Kähler*
Einstein orbifold limit, a deeper bubble tree, or collapse — exactly the dichotomy of §5, with the
Kähler branch removed. This is the sharp form of the Einstein-gap density question.


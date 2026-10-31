# Step 8 — First-order O11 cell law, ASD Yamabe upper bound, intrinsic Q-principle

Conventions: `Skills/geometric-analysis/references/conventions-and-literature.md`
(`P=∫|Ric°|²`, `R=P+S/4`, `T_±=2χ±3τ`, operator Weyl norms, `E=(4P+L_s)/R`).
Surgery data: `variational_geometry.tex` §1 (`M=X#kCP²bar#ℓ(S¹×S³)`, `Q=k+4ℓ`, `T_+=A−Q`).

## 1. O11: the first-order cell cost is −x₀R⁺(ζ,ζ), not 6x₀(1+sin²θ)

**What was computed.**

(a) `scripts/o11_rotation_hessian.py` (repaired: Step-6 filenames are `grid_x0<x0>_th0.json`;
options `--degr --nq --out`). Relaxed θ²-Hessian (Schur complement over linear rotation
modes) at the aligned optimized cells. Data `data/o11rot/rh_x*_d*_n*.json`,
merged `data/o11rot/rotation_hessian.json`. Rotation block positive definite in every run;
quadrature-independent (nq 300 = 600 to all digits).

(b) `scripts/o11_rotation_density.py`: pointwise second variation `L=Aφ'²+2Bφ'φ''+Cφ''²`
(gauge invariance under constant right rotation makes L independent of φ). It reproduces
the Chebyshev Schur value to 4e-9 relative (e.g. x₀=0.01: 5.902830531 vs 5.902830555),
then minimizes over profiles with 64 modes on the whole interval. Relaxed coefficient
`(1/2)H_eff/x₀`:

| x₀ | 0.03 | 0.01 | 0.003 | 0.001 | 3e-4 | 1e-4 |
|---|---|---|---|---|---|---|
| relaxed (N=64) | 5.552 | 5.712 | 5.858 | 5.940 | 5.983 | 5.999 |
| aligned slope (P₀−1)/x₀ | 5.619 | 5.779 | 5.900 | 5.956 | 5.984 | 5.994 |

The optimal rotation profile peaks at x/√x₀ = 0.85, 0.90, 0.96, 0.98, 0.98, 0.98: at the
Burns/CH crossover. Data `data/o11rot/rotation_density_x0*.json/.npz`.
New aligned cells x₀=3e-4, 1e-4 (`grid_x00.0003_th0.json`, `grid_x00.0001_th0.json`).

(c) **Correction of Step 6.** That Hessian lives in the *diabatic* family of
`o11_rotated_cell.py`: h = R(φ)diag(xe^w, xe^{−w}, F)R^T with the single slot F carrying
both the bolt-collapsing direction and the CH fibre. Writing the off-diagonal mode as
h₁₃ = φ(F−x) shows it forces h₁₃ = 0 at the crossover F=x — an artificial constraint.
The superposition picture h ≈ xI − x₀nn^T + x²e₃e₃^T has an avoided eigenvalue crossing
there: the collapsing branch ends *perpendicular* to the CH fibre (adiabatic family).

`scripts/o11_perp_cell.py` implements fixed-slot cells: bolt in s¹ slot, CH fibre in s³ slot,
frame rotation β(x) with relative angle θ = π/2 − β(bolt) (`--theta=`), a fixed-slot aligned
control (`--aligned`, reproduces 5.906 at x₀=0.003 and 5.992 at 0.001, i.e. the Kähler cell),
and a `--smooth` option making the bolt anisotropy O((x−x₀)²) (charge-4 smoothness; the
w-mode u·poly is only C^{1,1} at the bolt; values identical to 5 digits, e.g. perp 0.01:
1.001996 vs 1.002006). Runners: `o11_perp_runs.sh`, `o11_adia_runs.sh`. Data
`data/o11perp/*.json`, table `data/o11perp/first_order_law.csv`, figure
`figures/o11_first_order_law.png` (script `o11_first_order_law_fig.py`).
Chern–Weil identity residuals ≤ 4e-10 in all cells.

Best cell (upper bound) (P/8π²−1)/x₀ at x₀=0.003, versus 6cos²θ:

| θ | 0 | π/8 | π/4 | 3π/8 | π/2 |
|---|---|---|---|---|---|
| best found | 5.900 | 6.19 | 3.25 | 0.96 | 0.044 |
| 6cos²θ | 6 | 5.12 | 3.00 | 0.88 | 0 |
| 4ΔW₊/x₀ | 3.88 | 4.15 | 1.24 | −1.06 | −1.99 |
| 2(3cos²θ−1) | 4 | 3.12 | 1 | −1.12 | −2 |
| (ΔS/12)/x₀ | 2.01 | 2.04 | 2.01 | 2.02 | 2.03 |

At x₀=0.01 the adiabatic θ=π/8 cell (5.720) is already *below* the aligned Kähler cell (5.779).
At θ=π/2 the excess is second order: P/8π²−1 = 1.0e-5, 1.3e-4, 2.0e-3, 1.9e-2, 0.154 at
x₀ = 0.001, 0.003, 0.01, 0.03, 0.1 (≈ +10…21 x₀², still positive; optimizer stopped by
line search, so upper bounds).

**First-order cell law (conjecture with strong evidence).** For a Burns bubble of scale x₀
(x=r² units) in the complex-hyperbolic ball (s=−24), with orientation ζ ∈ Λ⁺ (|ζ|=1,
the Burns Kähler form), the infimum over SU(2)_L cells is

  P(U)/8π² = 1 − x₀ R⁺(ζ,ζ) + O(x₀²),  R⁺ = W⁺ + s/12 = diag(s/4,0,0) in (ω_CH, ω₂, ω₃),

  4ΔW₊ = −x₀ W⁺(ζ,ζ)·8π² = 2x₀(3cos²θ−1)·8π²,  ΔS/12 = −x₀(s/12)·8π² = 2x₀·8π².

Mechanism: at order x₀ = a²·|Rm_CH| the excess is the linear response of the Burns metric
to the background curvature at the blown-up point; SO(3)₊-equivariance allows only the
spin-0 (s) and spin-2 (W⁺ ∈ S²₀Λ⁺) parts of the background to pair with ζ⊗ζ, so the
θ-dependence must be a + b·P₂(cosθ). The measured components fit exactly this form,
with the Malchiodi–Malizia sign-changing pattern (3cos²θ−1) appearing in the Weyl term
already at order a² (the strict Weyl saving, maximal −2x₀ at θ=π/2, exactly cancels the
universal scalar cost +2x₀). A proof would compute the two response coefficients
(−1 for W⁺ and s) from the Burns ALE asymptotics; the numerics fix them to <2%.

**Consequences.**
1. The aligned (holomorphic) blow-up is the *most* expensive orientation at first order,
   not the cheapest. Step 6's "misalignment penalty ≈6x₀sin²θ" is a diabatic-ansatz
   artifact; its log growth at π/2 came from the ansatz, not geometry.
2. The first-order cost is ≥0 exactly because R⁺ ≤ 0 on a negative Kähler–Einstein
   background, and vanishes precisely on ker R⁺ = ω^⊥ — the same directions in which
   Ozuch's first obstruction R⁺ζ=0 is satisfied (Step 5–6 analysis). The O11 cell cost and
   the Einstein-desingularization obstruction are the same tensor.
3. O11 at fixed scale therefore reduces to the *second-order* term at ζ ⊥ ω:
   numerically +O(10–20)x₀² > 0. No tested cell has P(U) < 8π²; coefficient 4 survives,
   but the margin is now O(x₀²), not O(x₀). A sub-threshold cell, if any, must be sought at
   ζ ⊥ ω_CH and finite x₀ (0.03–0.3), beyond SU(2)_L symmetry.
4. For the lower-bound theorem, the natural statement becomes: cell excess ≥ −x₀R⁺(ζ,ζ)
   + c x₀² with R⁺ ≤ 0 — a "no-A-loss" inequality must be quadratic, not linear, near ω^⊥.

## 2. ASD Yamabe upper bound (new theorem)

**Normalization check.** Chern–Weil (ledger): W₊ = 2π²T₊ − R/12 + P/3, R = P + S/4, hence
P = 4W₊ + S/12 − 8π²T₊. With W₊=0 and T₊=A(1−h): P = S/12 + 8π²A(h−1),
R = S/3 + 8π²A(h−1) — Agent4's formula is exact in corpus conventions
(sympy: `scripts/asd_yamabe_bound.py`).

**Theorem ASD.** Let M be closed oriented with a monopole class a such that, for the metric
in question, p=(a⁺)² ≥ A > 0, and T₊(M) = A(1−h). Let [g] be an anti-self-dual conformal
class (W⁺=0) and g_Y its Yamabe metric, σ = S(g_Y)/(8π²A).
(i) σ ≥ 9 (LeBrun: ∫(s−√6|W⁺|)² ≥ 72π²p with W⁺=0). Strict unless equality in LeBrun,
    which forces Kähler with W⁺=0 hence s=0, impossible; so σ>9.
(ii) inf_{g∈[g]} E(g) = E(g_Y) = 1 + 9(h−1)/(σ+3h−3).
    Proof: W⁺=0 is conformally invariant, so every g∈[g] has R = S/3+8π²A(h−1) and
    E = 4 − 3ι/(σ_g+3h−3), ι = (∫s)²/(8π²AV). In a negative Yamabe class
    (∫s)²/V ≤ Y² = S(g_Y) and S(g) ≥ S(g_Y), so E(g) ≥ E(g_Y), equality at g_Y.
(iii) For h>1, E(g_Y) is decreasing in σ, hence
    1 < E(g_Y) < (4h−1)/(h+2) = 4 − 9/(h+2);
    for h<1 the inequalities reverse: max(0,(4h−1)/(h+2)) < E(g_Y) < 1.
    Uniformly: |E(g_Y)−1| < 3|h−1|/(h+2).

**Corollary (large-h window).** Let X be minimal of general type (b⁺≥2 or the corpus's
polarized supply), A = c₁²(X), M = X#ℓ(S¹×S³)#kCP²bar, Q = k+4ℓ, h=Q/A. By Taubes
(existence of ASD conformal structures on N#kCP²bar, k ≥ k_T(N)), for k ≥ k_T and h>1:

   1 ≤ α(M) < (4h−1)/(h+2) < 4h/(1+h).

The lower bound is the orientation-specific Hitchin–Thorpe estimate (T₊≤0 ⇒ R ≤ 4P ⇒ J≥1).
The improvement over surgery recovery is 4h/(1+h) − (4h−1)/(h+2) = (5h+1)/((h+1)(h+2)) > 0.
If k_T ≤ A (unknown), the same gives α<1 for 1/3≤h<1 and, at h=1 exactly, α(M)=1 attained
by a non-Einstein ASD Yamabe metric.

**Large-h question, sharpened.** Over ASD competitors α_ASD → 1 iff σ_Y/h → ∞ along Taubes
classes; for general metrics J = (σ+48w+12h−12)/(σ+12w+3h−3) (w = W₊/8π²A) is decreasing
in σ and increasing in w for h>1, so the H–T value 1 is approached only by W₊ = o(Ah),
S ≫ Ah. The asymptotic of α at large h is in [1, 4−9/(h+2)); whether σ_Y can be made ≫ h
on X#kCP²bar is the open quantitative Taubes problem.

## 3. Intrinsic Q-principle

**Budget.** For closed oriented M let 𝔐 be the (finite) set of monopole classes with
a² ≥ T₊ (automatic for classes with nonzero ordinary SW invariant: expected dimension
(a²−T₊)/4 ≥ 0). Define

   A(M) = max{ c² : c ∈ conv 𝔐 },  Q(M) = A(M) − T₊(M) ≥ 0,  h = Q/A,  U = 3min(T₊,T₋)/A.

**Lemma (metric-wise supply).** If A(M)>0, every metric g admits a ∈ 𝔐 with
(a_g⁺)² ≥ A and a² ≥ T₊, chosen constantly on the conformal class.
Proof: c = Σtᵢaᵢ attains A; a ↦ (a_g⁺)² is a positive semidefinite quadratic form, hence
convex, so max_i(aᵢ⁺)² ≥ (c⁺)² ≥ c² = A; H⁺_g is conformally invariant.

This is exactly the "common A on every conformal class" input of `cor:trf-nu`,
`thm:linear-window`. Examples: X#kCP²bar with X minimal general type: 𝔐 = {±K ± E₁ ±…±E_k},
conv = image of a cube, A = K_X², Q = k (sign averaging is the convex hull). With handles,
the loop-insertion classes have a² = A − k > T₊, Q = k+4ℓ. **Note:** the alternative
"Q = A − max_{𝔐} a²" is wrong for handle summands (it gives Q=0 for handle-only manifolds,
where the corpus proves α = 4h/(1+h) > 0); the correct excess is A − T₊.

**Theorem Q (positive direction, proved pieces).** Assume A(M)>0.
(Q1) h ≥ 1 (T₊ ≤ 0): α ≥ 1 (no monopole needed).
(Q2) 1/3 ≤ h < 1: α ≥ c_* universal (N1/trace-free gap, `cor:trf-nu`, since a² ≥ T₊ > 0
     removes the negative-square cost and (T₊/A−2/3)₊ = 0). By the relative-shortfall
     form, positivity extends to h > 1/3 − c.
(Q3) 0 < h < 1/3: α ≥ J ≥ (L_h − U)₊/(L_h + U/18), L_h = 1+(1+c₀)h (`thm:linear-window`);
     α ≥ c h whenever 3T₋ ≤ A(1+h) (handle-dominated; includes the balanced family as
     arranged in the corpus).
(Q0) h = 0 can give α = 0: Theorem Z (minimal general type), Z′ (Şuvaina Y_n).

**Conjecture Q.** α(M) > 0 ⟺ Q(M) > 0, under A(M) > 0.
Open in the positive direction exactly on 0<h<1/3 with 3T₋ > A(1+(1+c₀)h)
(blow-up-dominated: X#kCP²bar with k ≪ A has 3T₋/A ≈ 1+15h). Open in the negative
direction on Q=0 manifolds outside the Kähler/Şuvaina-orbifold mechanism (e.g.
Braungardt–Kotschick, fixed A, χ→∞; Proposition B remains suspended).
Relation to §1: for the blow-up-dominated region the corpus balanced theorem needs the
cell cost; §1 shows the per-blow-up excess over 8π² is O(x₀²) at ζ ⊥ ω, so the
positive direction there hinges on a lower bound of P at the 8π²k level (no-A-loss), not on
an O(x₀) margin.

## 4. Zero-gap exposition repair (Z′)

In Şuvaina's metrics g_t: exterior exactly negative KE (Ric = −g after scaling), so
|Ric+g|² = 0 there; the rescaled Ricci-flat ALE interiors have |Ric+g|² = |g|² = 4
pointwise, contributing 4·Vol(interior) = O(t⁴)→0; the interpolation annuli have
g−g_eucl = O(t²), ∂g = O(t), ∂²g = O(1), uniformly elliptic, hence |Rm|, |Ric| = O(1)
and contribution O(Vol(annulus)) → 0. Hence ∫|Ric+g|²/Vol → 0 and α = 0. Assumptions:
contracted orbifold with ample canonical sheaf; Y_n are non-Kähler (the inspected source
does not assert absence of all complex structures).

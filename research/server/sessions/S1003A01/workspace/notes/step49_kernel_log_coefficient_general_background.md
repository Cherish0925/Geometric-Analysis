# Step 49 — The logarithmic Burns saving on an arbitrary negative Kähler–Einstein background: the W⁻ cost is a removable corrector artifact, and the CH coefficient −9 is universal

Session S1003A01, Agent2, Execute.  Script `workspace/scripts/step49_kernel_log_coefficient.py` (usage in docstring); data `workspace/data/step49/summary_<BG>_NS*_A<deg>_K*.json`, `quadform_*.npz`, logs `log_*_A4.txt`, `log_H2H2_A6.txt`.
Status labels: [P] proved here; [N] numerically exact computation (Cauchy/Laurent extraction, errors ≤ 2e-11) inside a stated corrector class; [C] conditional / outline.

## 0. Question (A02 #826, #827(4); Spirit #58)
At a negative KE point p, R⁺_p = diag(s/4,0,0) has kernel ω^⊥, so the first-order Burns response 8λ²⟨R⁺_p,UΦU^T⟩ (A02 Thm 53.F′) vanishes for a perpendicular insertion (Burns Kähler form ζ ⊥ ω).  On complex-hyperbolic (CH) backgrounds Ch.5 of `web_research_collected.tex` gives the next term
P/8π² = 1 − 9ε² log(1/ε) + O_R(ε²)  (Ric = −6g), i.e. 1 − ¼x²log(1/x) + O(x²) with x = Area(E)/π in Ric = −g.
Does the logarithmic saving survive on a non-CH KE background, for arbitrary W⁻_p?  A W⁻ jet is invisible to Bianchi-IX radial functions; the computation must use the full curvature jet and non-invariant angular modes.

## 1. Exact reduction to a corner Taylor coefficient [P]
Cartesian normal coordinates x of g_bg; neck metric g_ε = g_bg + εk, k = k_B + k_0 + k_2 + …, with k_B = σ₁²+σ₂² (σ_m = (q̄dq)_m/|q|², left-invariant).
Exact fact: Ch.5's Burns core a = (√(t²+ε), √(t²+ε), t) is **exactly** δ + εk_B (a_m² − t² = ε).  Correctors k_0 (components homogeneous of degree 0) and k_2 (degree 2) are free.
For Einstein g_bg, P(g_ε) = ε²∫|Ric°′_{g_bg}(k)|²dV + O(ε³) in √ε ≪ r ≪ 1.  With z = ε/t², y = t², the density is (ε²/t)F(z,y) and the log coefficient is the z²y² Taylor coefficient F(0,0):
(a) total t-derivatives cannot alter it: t d/dt(z^a y^b) = (2b−2a)z^a y^b vanishes at a = b = 2;
(b) F(0,0) = C/(8π²), C = ∫_{S³} f_{−4}dΩ, f_{−4} the degree −4 homogeneous part of |Ric°′(k)|²_{g_bg}√det g_bg; then P/8π² ⊃ (F/2)ε²log(1/ε).
Only the background jet to degree 4 enters (Rm_p quadratically via |x₁|², x₁ = L_flat k_0 + L_{Rm}k_B; Rm⊗Rm and ∇²Rm linearly via 2⟨b₁,x₂⟩, b₁ = L_flat k_B; norm/volume corrections against |b₁|²).
k_2 enters only through ∫⟨b₁,L_flat k_2⟩; Burns is Bach- and scalar-flat, so L*_flat b₁ = 0 and the term is a radius-independent flux difference, i.e. zero (numerically ≤ 1e-11).

## 2. Representation-theoretic structure [P]
Burns is U(2)_ζ-invariant, U(2)_ζ = (U(1)_+×SU(2)_−)/Z₂ (SU(2)_− trivial on Λ⁺, SO(3) on Λ⁻).  The optimal corner coefficient is a U(2)_ζ-invariant quadratic polynomial in Rm_p plus a linear functional of ∇²Rm_p.
- W⁻_p is the spin-2 representation of SU(2)_−: only quadratic invariant |W⁻_p|²; no linear invariant; no invariant cross terms with W⁺, s, Ric°.
- ∇²W⁻ has no linear invariant (symmetric ∇² ∈ (0,0)⊕(1,1) has SU(2)_− spin ≤ 1); ∇²W⁺ contributes only ΔW⁺(ζ,ζ), fixed on Einstein metrics by the Weitzenböck formula and zero for KE-type W⁺.
- Hence for every Einstein background whose W⁺_p is of KE type with ζ in the −s/12 eigenspace (every point of every negative KE surface):
  F(p) = F_CH + κ |W⁻_p|²/s²,  with one universal constant κ (depending on the admitted corrector class).
- The Bianchi-IX/SU(2)-diagonal class cannot see W⁻: SU(2)_L-invariant curvature at the centre has W⁻_p = 0 and Ric°_p = 0 (SU(2)_L = SU(2)_−), and the squash modes c are SU(2)_−-invariant, so they do not couple linearly to W⁻ (this corrects A02 #826's expectation).  W⁻ effects can only be corrected by non-invariant angular modes.

## 3. Computation [N]
Exact backgrounds: CH, a = (sinh t, sinh t cosh t, sinh t); H²(−6)×H²(−6) in product normal coordinates; both Ric = −6g (residual ≤ 5e-15), complex structure J₂ (CH fibre σ₂), Burns ζ = J₃ (perpendicular, same Λ⁺).  H²×H² has |W⁻|² = |W⁺|² = s²/24.  Laurent coefficients by Cauchy averages over λ = 0.3e^{iθ}, x = λω (holomorphic JAX derivatives), Gauss–Legendre×trapezoid on S³, exact quadratic form over the tangent tensors listed.

| background | F at c = 0 | F at c* | opt. SU(2)-diag. c | opt. all E_ab·(angular monomials ≤ 2) (215 dims) | opt. all E_ab·(angular monomials ≤ 4) (465 dims) |
|---|---|---|---|---|---|
| CH | 14.75 (=59/4 ✓) | −18.000 ✓ | −18.000 | −18.000 | −18.000 |
| H²×H² | 20.35 | −12.40 | −12.40 | −15.900 | **−18.000** (|Δ| ≤ 2e-11) |

Checks: CH reproduces Ch.5's F(0,0;c) at c = 0 and c* to 1e-12; enlarging the corrector class never changes the CH value; k_2 couplings vanish; imaginary parts ≤ 4e-13.  Angular degree 6 (1305 dims) on H²×H² is running (task s49_t16_tool1); a larger class can only lower F.

Reading.  In the Ch.5 diagonal ansatz the W⁻ background *costs* 5.6 units of F; angular-degree-2 non-invariant correctors recover 3.5 of them and angular-degree-4 correctors recover all of them exactly.  Thus within the degree-4 class κ = 0 to 2e-11:
**on every negative KE background, at every point, the optimal perpendicular Burns insertion has the CH logarithmic coefficient**
P/8π² = 1 − ¼ x² log(1/x) + O(x²),  x = Area(E)/π (Ric = −g),
independently of W⁻_p.  The exact cancellation strongly suggests a structural identity (the W⁻-part of the Burns–background interaction is entirely in the range of the flat linearized trace-free Ricci operator on degree-0 tensors, with matching quadratic jet terms), not yet proved.  If degree-6 correctors lowered F below −18, W⁻ would *help*; either way the saving persists.

## 4. Consequences [C: modulo the rigorous general-background version of Ch.5's remainder estimate, §5]
1. p_*(X#CP̄²) < 8π² — indeed P/8π² ≤ 1 − ¼x²log(1/x) + C_X x² — for **every** compact negative KE surface X (every smooth canonical model of general type with K ample), at an arbitrary insertion point, not only for ball quotients or ramified CH-containing towers.  The only background input is KE-type W⁺_p and ζ ∈ ker R⁺_p.
2. A02's attainment chain (Thm 53.B/D, 54.A): a KE bulk component cannot carry a Burns-type bubble anywhere (moving the bubble to any point gives strict decrease, contradicting energy equality).  This extends "no exact CH region" to "no KE bulk component at all", i.e. the Einstein-bulk alternative (c) of Thm 53.E is excluded when the bulk is KE for the orientation selected by the bubble.  The non-KE Einstein bulk and non-Einstein bulk cases remain (they bring W⁺ shapes other than KE type and Ric°_p invariants |Ric°_p|², |Ric°_p(ζ)|²).
3. Replication: since the coefficient is the same at every point, fixed-ε cells can be placed on arbitrary unramified covers of any negative KE surface; the strict sub-four linear coefficient of Ch.5 (5.6.1) extends from compact CH surfaces to every fixed negative KE base (with base-dependent δ_X, by the same order of limits).
4. The CH ball is not special for the logarithmic mechanism: the saving is a property of the R⁺-kernel orientation alone (to this order).

## 5. What remains
- Degree-6 convergence (running) and a proof of κ = 0 (identify the explicit corrector; representation theory restricts it to the SU(2)_− spin-2 isotypic component).
- Rigorous general-background construction: Ch.5 analytic factorization with g_ε = cutoff interpolation of g_bg + εk (exact Burns core = δ + εk_B makes the inner region Burns + O(r²)); prove the analytic (z,y)-representation of the angular-integrated density and the O_R(ε²) remainder; order-ε terms: only the invariant R⁺(ζ,ζ) can appear (zero here), k_0-linear ones vanish by Burns criticality.
- Non-KE W⁺ shapes with R⁺ ≤ 0, ζ ∈ ker R⁺ (W⁺ = (|s|/12, w, −|s|/12−w)): needs an Einstein 4-jet framework; ∇²Rm enters only via ΔW⁺(ζ,ζ).
- Non-Einstein bulk minimizers (Problem 3 setting): add Ric°_p invariants and the ε²⟨Ric°_bg, Ric°″⟩ term.

# Step 15–17 synthesis: projected ACH dynamics and a validated Einstein filling of the blown-up ball

Session S1003A02. This note records the exact structure found in Step 15, the repaired validated
computation of Steps 16–17, and the resulting existence theorem. It replaces the dropped
"Step-15 note". Every numerical statement below is tied to a script and a data file.

## 1. Setting

Diagonal Bianchi IX metrics on (0,∞)×SU(2),
  g = dt² + a1(t)² σ1² + a2(t)² σ2² + a3(t)² σ3²,  dσ_i = 2 σ_j∧σ_k,
with Einstein normalization Ric = −6g (complex hyperbolic CH² has holomorphic sectional curvature −4;
in these variables CH² is a1=a3=sinh t, a2=sinh t cosh t, up to slot permutation).
With L_i = log a_i, y_i = L_i' the Einstein equations are
  y_i' = 6 − y_i (y1+y2+y3) + Pot_i,
  Pot_i = 2 e^{2L_i−2L_j−2L_k} − 8 e^{−2L_i} sinh²(L_j−L_k),
together with the constraint C = y1y2+y2y3+y3y1 − 6 − ½ΣPot_i = 0, which propagates by C' = −2SC.
Bolt: slot 3 collapses, a3 = t + O(t³), a1(0)=a2(0)=b. With σ3 normalized as for the Burns metric
this is the zero section of O(−1) → CP¹, so the manifold is the total space of O(−1), i.e. the
interior of D⁴ # CP̄² (blown-up ball). The regular bolt data form a two-parameter family (b,d),
d = p4 − q4 the t⁴ coefficient of a1 − a2 (Step 13, `scripts/einstein_bolt_series.py`).

## 2. Compact ACH system (Step 15, `scripts/ach_projected.py`, `data/ach_projected/structure.json`)

For fibre slot f and horizontal slots (g,h) in cyclic order put
  W = (y_f, y_g, y_h, κ, q, ζ),  κ = a_f/(a_g a_h),  q = log(a_g/a_h),  ζ = 1/(a_g a_h).
The system is exactly autonomous:
  y_f' = 6 − y_f S + 2κ² − 8ζ² sinh²q/κ²,
  y_g' = 6 − y_g S − 2κ² + 4ζ e^{−q} + 4ζ² sinh 2q/κ²,
  y_h' = 6 − y_h S − 2κ² + 4ζ e^{q} − 4ζ² sinh 2q/κ²,
  κ' = κ(y_f − y_g − y_h),  q' = y_g − y_h,  ζ' = −ζ(y_g + y_h).
(Agreement with the (L,y) field: 1.4×10⁻¹⁵ relative.)

**Equilibrium curve.** ACH_f = {E(q) = (2,1,1,1,q,0)}. A metric converging to E(q∞) has
a_f ~ c_f e^{2t}, a_g, a_h ~ e^{t}, κ → 1: it is asymptotically complex hyperbolic, its
conformal infinity is the left-invariant CR structure on S³ with contact form σ_f and Levi form
proportional to ρσ_g² + ρ⁻¹σ_h², ρ = e^{q∞} (Rossi sphere). ρ and 1/ρ are CR-equivalent; ρ=1 is the
standard sphere (validated by the smooth-nut computation of Step 14, which recovers CH² at ρ=1).

**Spectrum.** The Jacobian at E(q) has characteristic polynomial
  λ(λ−2)(λ+2)(λ+4)(λ+6)(λ+8)
(exact sympy). Modes: one unstable (+2), ζ/time-shift (−2), anisotropy a=y_g−y_h (−4), −6, the
constraint mode (−8), and the neutral Rossi direction (0). Left unstable eigenvector
  l_u = (1, −1, −1, 6, 0, −2 cosh q).
Consequence: the ACH stable set is codimension one; the two-parameter bolt family meets it
generically in a curve. This is the observed one-parameter family d*(b) and explains why no
stronger matching (e.g. prescribing ρ) is available inside the symmetric class.

**Neutral invariant.** Φ̃ = q + (y_g − y_h)/4 − ζ sinh q has derivative exactly quadratic in
(W − E(q), ζ) (`scripts/ach_phi_drift.py` verifies symbolically that the constant and linear
ζ-terms cancel). Φ̃ → q∞ on the equilibrium curve, so ρ∞ is read off any section with an
O(ζ²) error.

## 3. Cusp isolating block (Step 15, `scripts/ach_block_verify.py`, `data/ach_block/`)

Eigen-coordinates with the linear ζ-forcing removed (dy_f=y_f−2, ds=y_g+y_h−2, dk=κ−1, a=y_g−y_h):
  u = dy_f − ds + 6dk − 2cosh q ζ  (rate +2),  σ1 = dy_f − ds − 2dk + 2cosh q ζ  (−6),
  σ2 = 2dy_f + 3ds + 2dk − 4cosh q ζ  (−8),  â = a + 4 sinh q ζ  (−4).
Block B(K,ζ0,Q) = {|u|,|σ1|,|σ2|,|â| ≤ Kζ, 0<ζ≤ζ0, q∈Q}; rescaled coordinates ub=u/ζ etc.

**Lemma B (Arb-verified).** For K=1, ζ0=10⁻², Q=[0.70,0.90]:
(i) on the slabs ½K ≤ ±ub ≤ K, ±ub' > 0 (margins ≥ 1.87); (ii) on the faces s1b, s2b, ab = ±K the
flow points strictly inward (margins ≥ 1.82); (iii) y_g + y_h ≥ c = 1.99846 on B, hence
ζ' ≤ −cζ; (iv) on B, |Φ̃'| ≤ M ζ² with M = 19.5825 (`data/ach_block/phidrift_K1_z0.01_q0.7_0.9.json`).
Face functions are divided by ζ symbolically and the hyperbolic functions rewritten through E=e^q
(interval arithmetic cannot cancel 12e^q − 12e^q; the unrewritten version failed falsely).
Further patches up to q ≤ 3.2 are in `data/ach_block/` (margins ≥ 1.64).

Consequences inside B: a solution in B at time T with q(T) a distance
δ_q = (K + 4 sinh 0.9)ζ(T)/c from ∂Q keeps q∈Q while it stays in B; a solution that stays in B
for all t ≥ T has ζ → 0 exponentially, |W − E(q)| ≤ C ζ, q → q∞ with |q∞ − Φ̃(T)| ≤ Mζ(T)²/(2c);
it is therefore a complete ACH end with Rossi parameter q∞.

## 4. The regular bolt: analytic Fuchsian lemma (Step 17, `scripts/ach_bolt_fuchs.py`)

Put s = t², a1 = A(s), a2 = B(s), a3 = tC(s), D = s d/ds. Exactly (sympy check of
s(a1''−rhs1) = E_A, s(a2''−rhs2) = E_B, t(a3''−rhs3) = E_C returns 0, 0, 0):
  E_A = 4D²A + 4DA(DB/B + DC/C) − 6sA − 2(A⁴−B⁴)/(AB²C²) − 4s/A + 2s²C²/(AB²),
  E_B = (A↔B),
  E_C = (4D²+2D)C + 2(C+2DC)(DA/A+DB/B) − 6sC − [2s²C⁴ − 2(A²−B²)²]/(CA²B²).
With σ = (A+B)/2 − b, δ = A − B, γ = C − 1 the linear part at s=0 is
L = (4D², 4D² − 16, 4D² + 2D): σ and γ are nonresonant for k≥1, δ has the resonance k=2,
whose coefficient is the free parameter d. The formal solution (b = 4/5) begins
  σ = 49s/20 − 2335s²/1536 + …,  δ = d s² + 497 d s³/240 + …,  γ = −25s/24 + 68837 s²/15360 + …,
agreeing with the t-series of Step 13 (p2, r3, r5 differences = 0).

**Lemma F.** Let N=6, m=7, s0=10⁻⁴ (t0 = 10⁻²), d ∈ [0.28697953, 0.28701987]. Write
Y = Y_N + R with Y_N the exact order-N polynomial. R solves
  R = L⁻¹[Φ(Y_N+R) − Φ(Y_N) + ρ_N],
where the inverses are the radial integrals (D−c)⁻¹f(s) = ∫₀¹ λ^{−c−1} f(λs) dλ, giving on functions
with |f| ≤ F|s|^m the bounds
  (4D²)⁻¹: |R| ≤ F|s|^m/(4m²), |DR| ≤ F|s|^m/(4m);
  (4D²−16)⁻¹: |R| ≤ F|s|^m/(4(m−2)(m+2)), |DR| ≤ F m|s|^m/(4(m−2)(m+2));
  (4D²+2D)⁻¹: |R| ≤ F|s|^m/(2m(2m+1)), |DR| ≤ F|s|^m/(2(2m+1)).
The residual ρ_N is an exact rational function, its numerator exactly divisible by s^m; Arb/acb
bounds over 60 complex squares covering the closed disc |s| ≤ s0 give sup|ρ_N|/|s|^m ≤
(1.78×10⁵, 3.40×10³, 1.47×10⁶). Interval Jacobians of Φ over {|s|≤s0} × (Y_N + ball) give a
nonnegative matrix M with M r + c ≤ r/2 componentwise for
  r = (1.81×10³, 1.27×10⁴, 37.8, 2.64×10², 1.39×10⁴, 9.75×10⁴)
(seminorm constants of R_σ, DR_σ, R_δ, DR_δ, R_γ, DR_γ), and contraction factor 0.0325 in the
r-weighted max norm. Hence there is a unique solution with these bounds; since the integral
operators preserve holomorphy on the disc, A, B, C are holomorphic in s, so the metric is
real-analytic across the bolt (A, B even in t, a3 odd, A−B = O(t⁴), C(0)=1: the smoothness
conditions for the O(−1) bolt). Uniqueness among solutions with R = O(s^m) (contraction on small
discs plus regular ODE uniqueness) identifies it with the bolt Einstein metric of data (4/5, d).
The constraint holds identically: t²C is continuous, vanishes at t=0 because C(0)=1, and C' = −2SC
with S = 1/t + O(t) forces t²C ≡ const = 0.
Data: `data/ach_capd/fuchs_boxes_N6_complex.json` (complex-disc, used) and `fuchs_boxes_N6.json`
(real interval, identical boxes). The remainder at s0 is ≤ 10⁵ s0⁷ ≈ 10⁻²³, below binary64
resolution of the boxes; it is nevertheless included before outward rounding.

## 5. Validated transport (Steps 16–17)

`scripts/ach_bolt_capd.cpp` is a CAPD C0-Lohner integrator for X = (m, δ_L, L3, y_m, η, y3) with
L1,2 = m ± δ_L/2, y1,2 = y_m ± η/2, using the cancellation-free identities
  P1 + P2 = 8e^{−2m} cosh δ_L − 4e^{2L3−4m},
  P1 − P2 = 8e^{−2L3} sinh 2δ_L − 8e^{−2m} sinh δ_L,
  P3 = 2e^{2L3−4m} − 8e^{−2L3} sinh² δ_L.
The Step-16 version had a wrong y_m equation (it used a non-identity for P1+P2), which is why the
Step-16 pilot ran away to ub ≈ −1988. It was repaired. `scripts/ach_capd_field_check.py` parses the
field string directly from the C++ source: symbolic difference from the exact potentials = 0 in
all seven components; 2000 random states agree with `rhs_md` to 1.4×10⁻¹⁴; a CAPD point box chained
from t0=0.01 to t=2.7 contains the DOP853 solution at every checkpoint (widths ≤ 3.3×10⁻⁶)
(`data/ach_capd/field_check.json`). The Step-16 pilot files `ach_capd_pilot_t0*.json` enclose the
erroneous system and are void.

`scripts/ach_wazewski_run.py` transports the 40 Fuchsian boxes (d-subintervals of width
1.0085×10⁻⁶ tiling [0.28697953, 0.28701987]) from t0 = 0.01 to T = 2.75 (dt 0.05, order 30).
Result (`data/ach_capd/wazewski_T2.75.json`): every box lies in B(1, 10⁻², [0.70,0.90]) with
ζ(T) ∈ [0.009647, 0.009658], q(T) ∈ [0.80095, 0.80105], |s1b|, |s2b| ≤ 0.05, ab ≈ 0.27, and the
q-faces at distance > δ_q ≈ 0.024; the first box has ub ∈ [−0.754, −0.708] (lower egress slab) and
the last ub ∈ [0.708, 0.754] (upper slab); ub increases monotonically across the tiling.
Floating design (`data/ach_capd/passage_design_T2.75.json`): dub/dd ≈ 3.7×10⁴ at T.

## 6. Theorem (complete ACH Einstein metric on the blown-up ball with non-standard CR infinity)

**Theorem E.** There is d₀ ∈ [0.28697953, 0.28701987] such that the diagonal SU(2)-invariant metric
with regular O(−1) bolt data (b, d) = (4/5, d₀) is a complete real-analytic Einstein metric,
Ric = −6g, on the total space of O(−1) → CP¹ (the interior of D⁴#CP̄²). It is asymptotically complex
hyperbolic with fibre direction σ1: y1 → 2, y2, y3 → 1, a1/(a2a3) → 1, all at rate O(e^{−1.99t}),
and its CR infinity is the left-invariant Rossi sphere with
  ρ∞ = lim a2/a3 ∈ [2.19013, 2.19242]  (q∞ ∈ [0.78396, 0.78500]),
in particular not the standard CR sphere. The metric has exactly SU(2) symmetry in the diagonal
class with a1 ≢ a2 (δ = d₀ s² + …, d₀ ≠ 0) and a2/a3 ↛ 1.

*Proof.* Lemma F gives the real-analytic bolt solution for every d in the interval, with rigorous
state boxes at t0; CAPD transports them to T = 2.75, where all lie in B. Let S± ⊂ [d−,d+] be the
sets of d whose orbit leaves B after T through the face ub = ±1. Strict egress (Lemma B(i)) makes
exit times continuous, so S± are relatively open; they are disjoint. Only the u-faces can be exit
faces: stable faces are strict ingress, ζ = ζ0 is ingress (ζ' < 0), ζ = 0 is not reached in finite
time, and q-faces are not reached while in B by the drift bound. The left endpoint lies in the
lower slab, which is forward-invariant until exit through ub = −1, so d− ∈ S− unless its orbit stays
forever, and likewise d+ ∈ S+. Connectedness of the d-interval then gives d₀ ∉ S+ ∪ S−: its orbit
stays in B for all t ≥ T. By §3 it converges exponentially to E(q∞) with
|q∞ − Φ̃(T)| ≤ Mζ(T)²/(2c) ≤ 4.57×10⁻⁴; Φ̃(T) ∈ [0.784419, 0.784546] over all boxes
(`data/ach_capd/rossi_enclosure_b0.8.json`). Completeness: t is arclength on [0,∞) and the orbits are
compact. Einstein: the second-order system plus C ≡ 0 (§4). ∎

Scope. This is one value b = 4/5 of the branch. It proves existence, not uniqueness in b or d,
and gives no nonexistence. Not proved here: non-Kählerness for an arbitrary (non-invariant) complex
structure and the failure of half-conformal flatness. Inside the diagonal class the Kähler bolt
condition 3b²+2 = n fails (3.92 ≠ 1, Step 13), and Step 14 found both Weyl halves large near the
bolt numerically, but a rigorous pointwise interval evaluation of W± (e.g. |W±|² ≠ 24, the
Kähler–Einstein value for Ric = −6g) is still to be done; the bolt 2-jet makes this an exact
algebraic computation at t = 0.

## 7. Branch picture (numerical, Step 15; not part of Theorem E)

`data/ach_projected/brA–brD.json`, `cont_down.json` (468 pts), `cont_up.json` (240 pts):
d*(b) smooth and monotone on b ∈ [0.138, 400]; ρ(b) has a minimum ρ_min ≈ 2.1897 near b ≈ 0.765,
rises to 5.88 at b = 0.138 (d* ≈ 3×10⁻⁹, collapse of the anisotropy) and grows like ≈1.343 b for
large b; ρ converges in ζ* as O(ζ*) (6×10⁻⁸ between ζ* = 10⁻⁴ and 10⁻⁵). At b = 0.8,
d* = 0.286999618893, ρ = 2.19185374, inside the rigorous enclosure above. The fate enumeration at
b = 0.8 (363 signed d values, `data/ach_fate/fate_b0.8.json`) found exactly four fate changes: the
mirror ACH1/ACH2 pair d = ±0.28699961889 (ρ and 1/ρ) and SING/OTHER boundaries at |d| ≈ 20.65
approaching no ACH stratum; no orbit approached the Kähler-type ACH3 stratum. The Step-15
background continuation/root task s15_t16_tool2 hit its 3600 s limit with no further output; the
earlier `roots` mode is flawed (U undefined on singular orbits) and superseded by the fate method.

## 8. Literature position

Primary sources now in Knowledge (read via the strategist's retrieval):
Biquard–Herzlich, *A Burns–Epstein invariant for ACHE 4-manifolds*
(`Knowledge/objects/papers/A-Burns-Epstein-invariant-for-ACHE-4-manifolds--4fc106911938--96372cf5692f/object.md`):
for every ACH Einstein 4-manifold
  (1/8π²)∫(3|W⁻|² − |W⁺|² + Scal²/24) = χ − 3τ + ν(X)
(Thm 1.2/Cor. 7.3), with a variation formula for ν in terms of the Cartan tensor (Thm 8.1).
Biquard's Astérisque 265 produces ACH Einstein fillings of small CR deformations of the standard
sphere on the ball; Akbar's Taub-bolt-AdS metrics are biaxial real-AH with CP² topology;
Calderbank–Singer toric self-dual fillings require special-orbit self-intersection ≥ 3; Page–Pope
metrics live on O(−n) with the wrong topology for n=1. None gives an ACH Einstein metric on O(−1),
and none fills a Rossi sphere off the ball. Theorem E is therefore new as far as the primary
literature located goes. For the blown-up ball χ − 3τ = 2 − 3(−1) = 5, and ν(S³_std) = −1, so the
Biquard–Herzlich identity does not obstruct a standard-CR Einstein filling: any diagonal
nonexistence statement is dynamical (separatrix geometry), not characteristic-class.

**Independent check available.** On Theorem E's metric the identity predicts
ν(S³_ρ) = (1/8π²)∫(3|W⁻|² − |W⁺|² + 24) − 5 with ρ ∈ [2.1901, 2.1925]; computing the convergent
integral along the branch and comparing with ν of Rossi spheres (via Thm 8.1 integrated from ρ=1)
would validate the whole branch and the ρ-readout independently.

## 9. What this means for the Einstein-gap problem

Theorem E is a realization/existence result on the Einstein side of the single blow-up problem:
the blown-up ball carries complete ACH Einstein metrics, but the ones found have non-standard CR
infinity, so they cannot be glued into a ball quotient as exact-collar cells. The complete-cell
infima p_{1,0}, 𝔓_{k,ℓ} concern defect cells with *standard* CH collar; Step 14/15 showed the
certified cheap cells pay in a Burns core and do not shadow this branch. The branch is therefore
relevant as (a) the possible P→0 compactness endpoint in the diagonal class — a sequence of
diagonal standard-collar cells with P → 0 would have to converge to an Einstein filling with
ρ = 1 or degenerate — and (b) an exact example in the existence/realization axis. Diagonal
nonexistence at ρ = 1 requires the whole branch (both ends) plus completeness of the stratum
enumeration; it remains open.

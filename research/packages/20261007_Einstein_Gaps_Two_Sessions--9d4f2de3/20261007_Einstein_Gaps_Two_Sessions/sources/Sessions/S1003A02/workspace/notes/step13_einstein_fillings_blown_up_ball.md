# Step 13 — SU(2)-invariant Einstein fillings of the blown-up ball and the "total depletion" endpoint of 𝔓_{1,0}

Agent2, Execute. Scripts: `workspace/scripts/einstein_bolt_series.py`, `einstein_bolt_shoot.py`, `einstein_bolt_fig.py`.
Data: `workspace/data/einstein_bolt/series_n{1,3}.json`, `workspace/data/einstein_bolt_runs/` (bisection records `bis*_n1.json`,
biaxial `biax_n1.json`, `biax_n3.json`, summary `ach_family_summary.csv`). Figure: `workspace/figures/einstein_bolt_ach_family.png`.

## 1. Why this question

The cell cost satisfies the Chern–Weil identity P = 8π² + 4ΔW₊ + ΔS/12 relative to the CH ball it replaces. "Total depletion",
𝔓_{1,0} = 0, is exactly the existence (in a limit) of an Einstein metric with Ric = −6g on the blown-up ball D#CP̄² which is
asymptotic to CH² with *standard* CR infinity, fast enough that truncation costs vanish. For ACH Einstein metrics the free
(mass-type) term enters at order e^{−4r}, so truncation at radius R costs O(e^{−4R}) against volume e^{4R}; existence would give
𝔓_{1,0} = 𝔍_{1,0} = 0 and, through covers, α(X#kCP̄²) = o(h) along large-injectivity-radius ball quotients — inside LeBrun's open
range k < c₁²/3. Nonexistence is the geometric reason one expects p_{1,0} > 0. This step settles the question inside the
cohomogeneity-one class that contains every cell built so far (diagonal Bianchi IX), and finds a new family on the way.

## 2. Exact setup and local theory at the bolt

g = dt² + a₁²σ₁² + a₂²σ₂² + a₃²σ₃², dσᵢ = 2σⱼ∧σₖ. Orthonormal Ricci (Cartan-checked in S1003A01):
R₀₀ = −Σaᵢ''/aᵢ, Rᵢᵢ = −aᵢ''/aᵢ − (aᵢ'/aᵢ)(aⱼ'/aⱼ + aₖ'/aₖ) + 2(aᵢ⁴ − (aⱼ² − aₖ²)²)/(a₁a₂a₃)².
Checks: CH (a₁=a₃=sinh t, a₂=sinh t cosh t) gives Ric = −6 in all four components; Burns (a₁=a₂=√(t²+x₀), a₃=t) is scalar-flat.
All three slot forms ωᵢ = aᵢ dt∧σᵢ + aⱼaₖ σⱼ∧σₖ are self-dual for dt∧σ₁∧σ₂∧σ₃, so with the bolt in slot 3 and a₃'(0)=1 the
manifold is the blown-up ball with its complex orientation, whichever slot carries the CH Kähler direction at infinity:
slot 3 = aligned (U(2), Burns direction ∥ ω_CH), slot 1 or 2 = perpendicular (Burns direction ⟂ ω_CH).

**Regular series (sympy, exact).** For a₃ = n t + …, a₁(0) = a₂(0) = b, Einstein Ric = −6g with the constraint:
- n = 1: p₂ = q₂ = (3b² + 2)/(2b), r₃ = −2/(3b²), r₅ = (27b⁴ + 72b² + 53)/(60b⁴); the t⁴ anisotropy d = p₄ − q₄
  (a₁ − a₂ = d t⁴ + …, the charge-4 bolt mode) is free. Regular O(−1) Einstein bolts form a **two-parameter family (b, d)**.
- n = 3: no free anisotropy through order 6; p₄ = q₄ = −(12b² + 35)/(24b³), r₃ = −2/b².

**Kähler condition read from the series.** The slot-3 Kähler condition (a₁a₂)' = 2a₃ at second order gives
2(3b² + 2) = 2n. For n = 3 this forces b² = 1/3, the Calabi-ansatz KE metric on O(−3) with bolt area πb² = π/3 = 2π(n−2)/6
(matches ∫_E ρ = 2π c₁·E = −6 Area). For n = 1 it reads 3b² + 2 = 1: impossible — the local form of the global obstruction
∫_E ρ = 2π > 0 > −6 Area(E) to any negative KE metric containing a (−1)-curve. The slot-1 Kähler condition (a₂a₃)' = 2a₁ fails at
the bolt (b ≠ 2b), so the perpendicular solutions below are not Kähler for any slot structure.

## 3. Asymptotic types and the shooting method

In Lᵢ = log aᵢ, yᵢ = Lᵢ': yᵢ' = 6 − yᵢ² − yᵢ(yⱼ+yₖ) + Potᵢ, constraint y₁y₂+y₂y₃+y₃y₁ = 6 + ½ΣPotᵢ (held to ≤10⁻¹¹).
Fates: AH (yᵢ → √2, conformal infinity a triaxial Berger sphere); ACH with Kähler slot k (yₖ → 2, others → 1,
κₖ = aₖ/(aᵢaⱼ) → 1, Rossi ratio ρ = aᵢ/aⱼ → const; ρ is a neutral direction: (L_i−L_j)'' + 4(L_i−L_j)' = O(e^{−2t}), so ρ freezes);
singular (one aᵢ blows up, the other two collapse in finite t). ACH is a saddle: in the 2-parameter bolt family it is the
separatrix between AH and singular, found by bisection in d at fixed b (70 halvings; plateau length limited by binary64).

**Validation.** O(−3), U(2): b < 1/√3 singular, b > 1/√3 AH, b = 1/√3 stays on the ACH₃ plateau (deviation 8×10⁻⁸ at t ≈ 8)
before roundoff exit — the method recovers the Calabi KE ACH metric exactly where the series predicts.

## 4. Results for the blown-up ball (n = 1)

**(A) Aligned/U(2) bolts are never ACH.** With a₁ = a₂ enforced exactly, every b ∈ [0.003, 100] gives an AH metric
(Taub–bolt–AdS type) with Berger squashing c₃/c₁ ≤ 0.2887 (max near b = 1; 0.0013 at b = .003, 0.0047 at b = 100). Never ACH,
never round. (Consistent with the Kähler obstruction: U(2) ACH Einstein ⇒ Calabi/Page–Pope ⇒ impossible for n = 1.)

**(B) A one-parameter family of complete perpendicular ACH Einstein metrics on D#CP̄².** For each b ≳ 0.29 the AH/singular
separatrix d*(b) approaches the ACH₁ fixed point (κ₁ → 0.998–0.9998, y → (2,1,1) to 10⁻³–10⁻⁴), the Kähler-type direction at
infinity being slot 1, perpendicular to the bolt fibre. The CR infinity is a **Rossi sphere** with ratio ρ(b) = a₂/a₃:

| b | 0.29 | 0.4 | 0.55 | 0.7 | 0.8 | 0.9 | 1.1 | 1.5 | 2 | 4 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ρ | 3.20 | 2.63 | 2.30 | 2.20 | 2.196 | 2.22 | 2.32 | 2.65 | 3.18 | 5.63 | 10.9 |

ρ_min ≈ 2.20 at b ≈ 0.75–0.8; ρ ≈ 1.36 b for large b; ρ increases as b ↓ 0.29, below which the separatrix no longer approaches
ACH (min deviation 0.1–0.8, a different transition). Plateau drift of ρ is ≈ 3 % and comes from the departure; the neutral-mode
estimate above bounds the remaining asymptotic change by ≈ 10⁻³ relative. Since ρ and 1/ρ are CR-equivalent, the image of the
family in the Rossi line is ρ ∈ [≈2.20, ∞), and **the standard sphere ρ = 1 is not reached.**

**(C) Consequence (numerical theorem-level evidence, not a proof).** Within diagonal SU(2)-invariant metrics there is no Einstein
metric on the blown-up ball with Ric = −6g asymptotic to CH² with standard CR infinity: aligned bolts are AH, and perpendicular
ACH bolts realize only Rossi spheres with ρ ≳ 2.2. Hence the "total depletion" endpoint of the cell problem does not occur in the
class containing all cells constructed so far, and the codimension count is overdetermined: 2 bolt parameters versus the 2
conditions (ACH separatrix, ρ = 1). The cheap cells are *perpendicular* precisely because the perpendicular bolt family is the
only one that reaches the ACH stratum at all; their cost below 8π² measures how far the exact-CH collar can be bent toward an
Einstein filling whose CR infinity sits at ρ ≥ 2.2.

## 5. What this does and does not settle

Settled numerically: the structure of SU(2)-diagonal Einstein O(−1) bolts (two parameters; AH generic; ACH separatrix only in the
perpendicular orientation; Rossi ratio bounded below by ≈ 2.2; U(2) bolts AH with squashing ≤ 0.289).
Not settled: (i) a proof — needs a rigorous separatrix enclosure (e.g. interval shooting from an ACH asymptotic expansion with
parameter ρ inward to the bolt) or a monotone quantity for the ODE; (ii) non-diagonal/non-symmetric Einstein fillings of the
standard sphere (Biquard's ACH deformation theory makes the filling map Fredholm; the standard sphere is far from ρ ≈ 2.2 in CR
moduli); (iii) the quantitative lower bound for 𝔓_{1,0}: nonexistence of an Einstein limit suggests, but does not imply,
𝔓^{SU(2)}_{1,0} > 0 — one still needs compactness of P-minimizing SU(2) sequences with variable outer radius (ODE compactness
on the bolt side plus control of where the defect sits).

## 6. Proposed next constructions

1. **Rigorous version of (B)/(C):** asymptotic expansion of ACH₁ Einstein solutions with Rossi ρ (free data: ρ, the e^{−4t}
   mass-type coefficient and t-shift), interval integration inward, matching with the bolt series — a computer-assisted
   theorem "ρ(b) ≥ 2.1 for all b" plus large/small-b asymptotics.
2. **Ball cross-check:** the same shooting from a nut gives the SU(2) Einstein ACH fillings of Rossi spheres on B⁴, which must pass
   through CH² at ρ = 1 (Biquard's family); this calibrates the ρ measurement.
3. **Cost of CR mismatch:** a lower bound P_cell ≥ F(ρ_min) in the SU(2) class via a calibration/Lyapunov functional built from the
   neutral mode u = L₂ − L₃ (u'' + 4u' is forced only by Einstein defects), i.e. "to bend the Einstein separatrix's ρ ≈ 2.2 to the
   collar's ρ = 1 one must pay Ricci defect"; compare with the certified p ≈ 0.9991 cell.
4. **Literature:** SU(2)-invariant ACH Einstein metrics and Rossi spheres (Hitchin's Painlevé VI SDE family, Biquard's
   "Métriques autoduales sur la boule", Biquard–Herzlich Burns–Epstein invariant, which gives χ − 3τ = 5 for these fillings).

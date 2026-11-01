# Step 65 — The exceptional-flux ledger of the certified sub-tariff cells

Agent2, Execute. Script `workspace/scripts/step65_cell_twist_flux.py` (batch `step65_family_batch.sh`);
data `workspace/data/step65_cell_twist_flux.json` (x0=.03, X=128, d20, with J-profiles) and
`workspace/data/step65_family/*.json`, summary `workspace/data/step65_family/summary.txt`.
Floating quadrature on A01's reconstructed perpendicular cells (read-only import of `perp_dual_cost.py`);
not interval-certified. The x0 = .05 and .10 records reconstruct to P ≈ 32.9 and 32.2, not to their
recorded values 0.9963 and 1.0153 (both curvature routes agree, so the reconstruction rather than the
quadrature is at fault). They are excluded. All other records reproduce P_record to ≤ 1e-6.

## 1. A metric-only form of the frame-twist identity

Let g be any metric on M = X#kCP̄², a a best-sign class, and h an ASD harmonic form. Write B_g : Λ⁺ → Λ⁻
for the tracefree-Ricci block of the curvature operator; Frobenius |B|² = |Ric°|²/4.

For every orthogonal J with Kähler form Ω, the ASD part of R(Ω) is B_g Ω = ρ₀ᴶ. Hence the Step-64 identity
H⁻(t_J⁻) = 2πh_a⁻ − H⁻(ρ₀ᴶ), tested against h, reads

  ⟨t_J⁻, h⟩ = 2π⟨a, h⟩ − ∫⟨Ω, B_g^*h⟩ dμ.   (65.1)

Put 𝔉_h(g) := √2 ∫ |B_g^* h| dμ (since |Ω| = √2). Then for every J in the class:

  ⟨t_J⁻, h⟩ ≥ 2π⟨a,h⟩ − 𝔉_h(g),   P/2 ≥ 𝔉_h(g)² / ‖h‖²_{supp Ric°}.   (65.2)

The second inequality is Cauchy–Schwarz together with ‖B‖₂² = P/4. Thus 63.T has the metric-only
content p ≥ (𝔉_h/2π‖h‖)². A sub-tariff metric must have **exceptional Ricci flux** 𝔉_h(g) < 2π√p⟨a,ĥ⟩.
Equivalently, define the flux deficit δ := 1 − 𝔉/(2π⟨a,ĥ⟩); then **every** J in the class carries
harmonic twist flux at least 2πδ. The exact ledger is

  p = (1 − δ)²/‖h‖² + L,   L = (P/2 − 𝔉²/‖h‖²)/(4π²) ≥ 0,   (65.3)

where L measures Ricci misalignment: B not of the form λ·(unit SD)⊗ĥ, and |B^*h|/|h| not constant.
The saving therefore obeys 1 − p ≤ 2δ − δ² − L + (1 − ‖h‖⁻²).

## 2. Diagonal Bianchi-IX realization (exact formulas used by the script)

Setup.
- Coframe e0 = dt, e_i = a_i s_i, with ds_i = 2 s_j∧s_k. Slots (1,2,3) = (bolt, transverse, CH fibre).
- Λ⁺ = span{w_i = e0i + ejk}, with ∇w_i = −A_k w_j + A_j w_k and A_k = −(v_k/a_k) e_k.
- v_k = ȧ_k − γ_k, γ_i = (a_j² + a_k² − a_i²)/(a_j a_k).
- In CH, v₁ = v₂ = 0 and v₃ = 3 sinh² t, so w₃ = ω_CH is parallel.
- At the bolt, w₁ (the Burns direction) is smooth, while w₂ and w₃ rotate. The invariant J_CH-type
  structure J₃ is therefore singular along E. This is the codimension-2 analogue of the Step-64 Hopf
  zero, with a power-divergent twist energy.

Curvature.
- R(w_i) = R⁺_i w_i⁺ + m_i w_i⁻, with R⁺_i = ½[−v̇_i/a_i − (2v_i + v_j v_k)/(a_j a_k)].
- m_i = ½[−v̇_i/a_i + (2v_i + v_j v_k)/(a_j a_k)] = (r₀ + r_i)/2.
- Checks: m agrees with the coordinate Ricci tensor to 8e-7 relative; Σ R⁺_i = s/4; P = 4∫Σ m_i².

Exceptional harmonic form.
- h = φ w₁⁻ with φ = −G/(a₂a₃), G' = −2a₁G/(a₂a₃), G(0) = 1/π, so ∫_E h = 1.
- ‖h‖²_cell = 1 − (G∞/G0)² = 0.99897 at x0 = .03 (two independent evaluations agree to 5e-7).
- The SU(2)-average of the global harmonic representative on the ball is exactly h. Pairings with
  invariant forms supported in the ball are therefore exact.

Smooth class-a structures.
- Ω = cos θ w₁ + sin θ w₃, with θ = 0 at the bolt and θ = π/2 in the Kähler exterior.
- Twist:
  t⁻ = ½[sθ̇v₁/a₁ − c v₂v₃/(a₂a₃)] w₁⁻ + ½[−cθ̇v₃/a₃ − s v₁v₂/(a₁a₂)] w₃⁻.
- Sign of γ_J = R(Ω) + σt: the closedness test gives σ = +1 (residual 7e-16; σ = −1 gives 0.72).
- (65.1) then holds to 5e-7 for five different rotation windows, from the bolt layer to the CH exterior.
  This is an end-to-end check of the frame formula on a genuine sub-tariff metric.

Structural facts.
- (i) B^*h ∝ w₁⁺, so 𝔉 = ∫2|m₁φ|.
- (ii) For J₁ (θ = 0 wherever Ric° ≠ 0) the twist on the cell is t = (v₂v₃/(a₂a₃)) e23, i.e.
  t⁻ = −½(v₂v₃/(a₂a₃)) w₁⁻, pointwise parallel to h.
- (iii) Rotation through a Ricci-flat region produces only w₃⁻ twist, which is orthogonal to h. So the
  topologically forced rotation from the Burns direction to ω_CH is flux-neutral, and its twist norm is
  a gauge artifact of the choice of J.
- (iv) The harmonic twist flux of J₁ equals 2πδ exactly. It is the product of two non-Kähler defects:
  v₃ (J₁ ⟂ ω_CH, forced by the ambient Kähler geometry) and v₂ (the cell's transverse response).
  Pure Burns has v₂ = v₃ = 0; pure CH has v₂ = 0.

## 3. Numbers

Columns: δ = flux deficit; 𝔉/2π = exceptional Ricci flux; Hodge = (1−δ)²/‖h‖²; L = misalignment
loss; sav = 1 − p; eff = harmonic efficiency of the J₁ twist on the cell; x_med = median position of
the twist flux.

| x0, X | p | δ | 𝔉/2π | Hodge | L | sav/δ | eff(J₁) | x_med/x0 | x_med/√x0 |
|---|---|---|---|---|---|---|---|---|---|
| .003, 64 | 0.999796 | 1.80e-4 | 0.99982 | 0.99965 | 1.48e-4 | 1.13 | 0.033 | 15.5 | 0.85 |
| .01, 64 | 0.998701 | 1.27e-3 | 0.99875 | 0.99757 | 1.13e-3 | 1.02 | 0.069 | 8.0 | 0.80 |
| .02, 128 | 0.996860 | 3.43e-3 | 0.99660 | 0.99360 | 3.26e-3 | 0.91 | 0.091 | 5.45 | 0.77 |
| .03, 128 (certified) | 0.995663 | 5.49e-3 | 0.99459 | 0.99008 | 5.58e-3 | 0.79 | 0.100 | 4.30 | 0.75 |
| .03, 256 | 0.995598 | 5.48e-3 | 0.99456 | 0.99009 | 5.51e-3 | 0.80 | 0.100 | 4.29 | 0.74 |
| .07, 128 | 1.001156 | 8.76e-3 | 0.99153 | 0.98775 | 1.34e-2 | — | 0.083 | 2.47 | — |
| .15, 128 | 1.052546 | −3.9e-3 | 1.00469 | 1.02702 | 2.55e-2 | — | — | — | — |

At the certified cell, splitting the J₁ twist flux by sign gives +0.00740 − 0.00191 (×2π). The w₁⁺⊗w₁⁻
block carries 99.47% of P. The exceptional Ricci flux of the J₁ representative concentrates where P
does (deciles at x/x0 = 1.06, 1.47, 3.6). The twist flux sits farther out.

## 4. What the cell says about how the saving is paid

1. **Where.**
   - The flux deficit is carried at the geometric-mean scale of the matching annulus. Its median lies at
     x ≈ 0.75–0.85 √x0 (x = r²) uniformly across the family, with deciles spread over a decade.
   - Neither the bolt layer (where the Ricci flux sits) nor the CH collar carries it. The twist flux is
     log-distributed over the neck x0 ≪ x ≪ 1, the same annulus that produces the second-order
     ε² log(1/ε) Burns coefficient of Theorem 59.R.
   - This gives a geometric meaning to the log term: it is twist flux v₂v₃ generated where the Burns
     tail (v₂) meets the perpendicular ambient Kähler geometry (v₃ ∝ r²).

2. **How much.**
   - The deficit is second order: δ/x0 = 0.06, 0.13, 0.17, 0.18 and δ/x0² = 20, 13, 8.6, 6.1. The
     certified-cell value is δ ≈ 0.0055 per class.
   - The largest value seen on the family is δ ≈ 0.0088 (x0 = .07), and that cell is already above tariff.

3. **Conversion.**
   - The Hodge gain 2δ is roughly half lost to misalignment: L/δ = 0.82, 0.89, 0.95, 1.02, and
     saving ≈ (1.1 → 0.8)·δ, with ratio sav/(2δ) ≈ 0.57 → 0.40.
   - As the cell grows, L outgrows δ and the saving turns negative near x0 ≈ 0.065. This is the
     Step-50 sign change, now read as misalignment overtaking flux deficit.

4. **Efficiency.**
   - The natural smooth structure J₁ has twist pointwise aligned with h, yet only 3–10% of its twist
     norm is harmonic. The twist profile v₂v₃/(a₂a₃) extends into the collar, where h ∝ e^{−3t} is
     negligible.
   - The J-free quantity δ is the meaningful one, and it is small.

5. **Consequence for the diffuse template.**
   - By (65.3), any closed sequence with p ≤ c·k (c < 1) needs Σ_classes δ_i ≳ (1 − √c) per class
     on average, i.e. an O(1) exceptional-Ricci-flux shortfall.
   - Burns-type cells supply δ ≤ 10⁻² at a saving of the same order. So a p ≪ k state is not a dilute
     gas of improved Burns cells. Its Ric° must fail to carry the exceptional flux at O(1) relative size,
     while every class-a J carries O(1) harmonic twist flux.
   - In AK language this is u_rms ≳ 2√(k/A). In the cell language it means v₂v₃-type double non-Kähler
     defects of unit size over a region of volume ~ A, rather than in a neck annulus of a Burns core.
   - The cell provides no seed for that regime. Its twist efficiency and deficit are both small and
     second order.

## 5. Consistency of the Weyl/Yamabe channel (Spirit #80, constants corrected)

- For an AK metric at s = −4 with Kähler-type eigenvalue λ = s/6 + u (Step-42/63 conventions,
  u = |∇Ω|²/4), we have |W⁺|² ≥ (3/2)(2/3 − u)² = 2/3 − 2u + (3/2)u².
- Hence κ ≤ (3/8π²)(2∫u − (3/2)∫u²) up to the volume normalization. At u ≡ 2√(k/A) on volume 2π²A
  this gives κ ≲ 3√(kA) − 4.5k, not (9/8)√(kA).
- Identity 62.1 with p ≈ 0 then forces υ = 4κ − 3k + 3p ≈ 12√(kA) − 21k.
- So the Yamabe constant of the conformal class must be more negative than the extremal value
  −4π√(2A) by a relative amount ≈ 6√(k/A). This is allowed: LeBrun gives Y² ≥ 32π²A only.
- The LeBrun envelope υ ≥ κ + 3κ²/4A is then satisfied with room. None of 62.1, 62.A, 63.T or 65.3
  excludes p ≪ k. A Yamabe-excess upper bound sharper than LeBrun's in the near-ASD-exceptional regime
would be decisive; no candidate mechanism is in hand.

## 5′. The sharpened open problem (misalignment–deficit coercivity)

Since p ≥ (1−δ)² + L (taking ‖h‖ ≤ 1 locally), any estimate

  L ≥ c·δ − o(1),   0 ≤ δ ≤ 1 per class,

yields:
- a tariff p ≥ c − c²/4 per class when 0 < c < 2;
- the full tariff p ≥ 1 when c ≥ 2.

On the perpendicular cells L/δ ∈ [0.82, 1.02], i.e. c ≈ 1. A general inequality with this constant
would give a 3/4-type per-class tariff. Conversely, a p ≪ k sequence must make L = o(δ) with δ ≈ 1.

Pointwise, L = 0 means B_g = μ·Ω₀⊗ĥ with constant μ and a unit SD form Ω₀. That is, Ric° is
exactly aligned with the exceptional harmonic form along one almost-complex structure, and Ω₀ is not
Kähler when δ > 0.

The equality and near-equality structure is therefore the concrete question: does a compact metric
with Ric° = μ Ω₀ ⊙ ĥ (non-Kähler Ω₀) exist? And what does near-alignment force on ∇Ω₀ through the
contracted Bianchi identity div Ric° = ds/4? Ric° is built from Ω₀ and ĥ, and ĥ is harmonic, so this
becomes a first-order equation coupling ∇Ω₀ to ∇ĥ. That is the natural place to look for coercivity.

## 6. Status

- (65.1)–(65.3): proved, by elementary consequences of 63.T/64 and Cauchy–Schwarz.
- The Bianchi-IX formulas of §2: derived and checked numerically end-to-end.
- The table: floating, reproducible.
- The readings in §4: empirical on the A01 perpendicular family only. They are not statements about
  non-symmetric or multi-class metrics.
- A01's analysis (#838) locates the obstruction to an F_h cancellation in Sym₀∇²Ω, which the AAD system
  does not fix algebraically. It is consistent with the cell: there the harmonic twist arises from the
  product v₂v₃ of first-derivative defects, whose size is set by the global matching, not by any local
  algebraic identity.


## 7. Step-66 binding corrections (TTCS step66_ttcs01 verifier)

These supersede §§1, 3 and 5′ where they conflict. Full text: `step66_rank_one_exceptional_ricci_rigidity.md` §7.

**Ledger normalization.** With unit ĥ:
- q = (h_a⁻, ĥ),
- δ = 1 − 𝔉_ĥ/(2πq),
- p = q²(1−δ)² + L.

**Two invalid statements.**
- "𝔉 < 2π√p⟨a,ĥ⟩" is replaced by 𝔉_ĥ ≤ 2π√p.
- The saving bound is 1 − p ≤ 2δ − δ² − L (for H ≤ 1, q_h = 1). The extra term printed in §1 had the wrong sign.

**The table's δ column.** It is the signed J₁ deficit, not the metric deficit. At the certified cell:

| | metric (correct) | printed (signed J₁) |
|---|---|---|
| δ | 0.00541 | 0.00549 |
| Hodge | 0.99023 | 0.99008 |
| L | 0.00543 | 0.00558 |

**Other corrections.**
- The amplitude variable in L is |B^*h|/|h|².
- A01 confirms the x0 = .05/.10 records are not authoritative.
- §5′: L ≥ cδ for all metrics would exclude Einstein metrics on X#kCP̄² (δ = 1, L = 0), so it is not a reduction of the gap problem. The local version near cscK is the quadratic eigenvalue problem c_K of Step 66 §8.

# Step 80 — Q4 order-6 structure: universal functional, λ-quadratic Φ₆, and the refutation of Conjecture 79.C at order 6

Status tags: [P] proved, [N] exact/numerical computation with stated coverage, [C] conjectural.
Conventions as in `step77_79_Q4_higher_prolongation.md` (Darboux gauge, g = e^H, H anti-J₀ symmetric, torsion jet f = cz + (S+A)z̄, cone ‖A‖² = ‖S‖² + 8|c|², unit torsion norm tn² = 4|c|² + 2‖S‖² + 2‖A‖² = 1 unless stated). Even branch H₃ = 0 throughout this note.

## 0. Bottom line

Order 6 does **not** obstruct nondegenerate torsion zeros of almost-Kähler Einstein germs. The single surviving scalar condition Φ₆ ≤ 0 has **both signs** on the strict cone, already at λ = 0 and at λ < 0. At three strict jets with Φ₆ < 0 I constructed an explicit real jet H₂,…,H₈ solving Ric(e^H) − λe^H = 0 through x-degree 6, with every unreduced residual ≤ 1.2×10⁻⁷. Conjecture 79.C ("no real formal AKE germ has a nondegenerate torsion zero") is therefore **false at order 6**. Order 6 cuts the strict cone into a semialgebraic region {Φ₆ > 0} of obstructed jets and an open region {Φ₆ ≤ 0} of jets that extend. Whether order 8 or higher closes the remaining region is open. Every jet tested in Steps 78–79 happened to lie in the obstructed region; that is why the earlier evidence looked uniform.

## 1. The surviving functional is universal [N]

The reduction leaves one row π of the 259-dimensional cokernel of the flat L₆. As a functional on the 840 degree-6 Ricci coefficients, ℓ = C₆π. At four jets (two generic, the A01 shared jet, and a μ²-rescaled jet) |cos(ℓᵢ, ℓⱼ)| = 1 to 10⁻¹⁵ (`data/step80/universal_pi.json`, `universal_pi.npz`). So the obstruction is ⟨ℓ, E₆⟩ for one fixed flat functional ℓ: the degree-6 Taylor coefficient of a single universal scalar compatibility expression. This matches the excess count C(k+1,3) (one scalar function Φ), and ℓ is the natural object to identify invariantly.

## 2. Weighted homogeneity and exact λ-dependence [N]

Under x → μx, (H_k, λ) → (μ^k H_k, μ²λ), and Φ₆(μ² jet, μ² λ) = μ⁸ Φ₆(jet, λ) with ratio 1 + 1.6×10⁻¹² (`universal_pi.json`). Across λ ∈ [−20, 20] at two unit jets, Φ₆(λ) fits a quadratic exactly (cubic and quartic coefficients 10⁻¹¹, 10⁻¹³; `lambda_scan_a.json`):
  Φ₆ = F₀(θ) + F₁(θ)λ + F₂(θ)λ²,  with weights 8, 6, 4,
where θ is the unit-torsion jet. The universal quadratic form ℓ·𝒬(H₄,H₄) on all of H₄ is indefinite (99 positive, 84 negative eigenvalues). It is definite only on the 12-dimensional active subspace selected by the reduction.

## 3. Map of F₀, F₁, F₂ [N] (`data/step80/log_F012.txt`; three λ-points −5, 0, 5 per jet)

| jet | c²-fraction | F₀ (= Φ₆ at λ=0) | F₁ | F₂ | Φ₆ at λ = −5, 0, 5 |
|---|---|---|---|---|---|
| gen0 | .033 | +0.052 | −0.034 | −1.1e-4 | +0.217, +0.052, −0.119 |
| gen1 | .067 | +0.714 | +0.134 | −2.5e-4 | +0.036, +0.714, +1.380 |
| **gen2** | .053 | **−0.165** | +0.014 | +2.1e-5 | **−0.237, −0.165, −0.093** |
| gen3 | .019 | +0.183 | −0.031 | −1.8e-3 | +0.290, +0.183, −0.015 |
| gen4 | .055 | +0.787 | −0.047 | −5.0e-4 | +1.011, +0.787, +0.538 |
| **gen5** | .059 | +0.162 | +0.108 | −1.4e-3 | **−0.416**, +0.162, +0.668 |
| **gen6** | .028 | +0.155 | +0.063 | −1.1e-3 | **−0.184**, +0.155, +0.441 |
| gen7 | .052 | +0.307 | −0.039 | −1.1e-3 | +0.474, +0.307, +0.086 |
| smallc0–3 | ≤.001 | +0.05…+0.22 | ≈0 | +1.1e-3…+3.6e-3 | all positive |
| bigc0–2 | ≈.107 | +4.5…+79 | ±0.14 | +1e-4…+2e-4 | all positive |
| bigc3 | .069 | +0.516 | +0.095 | −2.2e-4 | +0.034, +0.516, +0.987 |

Facts:
- F₀ has both signs, so the Ricci-flat case is not obstructed (gen2).
- F₂ has both signs, so the λ-band picture of the first draft of this note is withdrawn.
- F₁ is comparable to F₀ at moderate λ. At λ = −5 with unit torsion, 4 of 8 generic jets are obstructed and 4 are not.
- Small-c jets (near-degenerate in the W₂⁺ direction) and large-c jets were all obstructed in this sample.
- The Steps 78–79 test jets all have Φ₆ > 0. The near-degenerate D6 jet has small c, and the A01 shared jet has c-fraction 1/26 and large F₀.

## 4. Explicit real order-6 jets [N] (`scripts/step80_reconstruct.py`, `data/step80/recon_*.json|npz`)

Construction. With y = Pz + Kw, the scalar row is solved on the positive-definite 12-dimensional block by
  z = z* + t v,  z* = −H_π⁻¹ j,  t = √(−2Φ₆/h_min).
The other 34 rows are solved linearly in w (rank 34). Then u = u₀ + Ny gives H₄…H₇, and H₈ solves the flat L₆. All unreduced equations are then evaluated directly:

| case | λ | detDf (index +1) | Φ₆ | ‖Ψ‖ after solve | E₀ | E₂ | E₄ | E₆ (E₆ before H₈) |
|---|---|---|---|---|---|---|---|---|
| gen2 | 0 | 0.0166 | −0.165 | 3.5e-8 | 9e-17 | 1.3e-11 | 3.6e-11 | **6.1e-8** (2.6e7) |
| gen2 | −5 | 0.0166 | −0.237 | 4.0e-8 | 3e-15 | 3.8e-11 | 2.5e-10 | **1.2e-7** (3.4e7) |
| gen5 | −5 | 0.0234 | −0.416 | 2.2e-9 | 3e-15 | 6.6e-12 | 5.8e-11 | **7.8e-9** (2.1e6) |
| lsA jet0 (control, Φ₆>0) | −1 | 0.0502 | +0.842 | 0.842 = Φ₆ | 7e-16 | 5e-12 | 1e-11 | 4.64 (residual stays) |
| lsA jet0 | −40 | — | (−0.19) | 0.125 | — | 3e-5 | 1.5e-3 | 26.4: **ill-conditioned** (H_π min eig 7e-15, quad rank 13); value from the λ-scan at λ = −40 is unreliable and is withdrawn |

E₁, E₃, E₅ vanish (H₃ = 0, parity). The jet coefficients have norm ‖y‖ ~ 10³, so the relative residual is ~10⁻¹⁵. The positive control behaves as the criterion predicts: the minimum residual of the scalar row equals Φ₆.

**Proposition 80.R [N, floating point, three jets].** There are real formal AKE jets through order 6, with λ = 0 and with λ = −5 (unit torsion, so λ/tn² = −5), whose torsion vanishes at 0 with nondegenerate differential of index +1. The order-2 cone (76.Z) and the order-6 scalar condition are satisfied, and no odd jets are needed.

What this does not show: existence of a germ. Orders 7 and 8 are untested. Order 8 carries excess 84, H₅H₅ and H₄H₆ terms, and H₄H₄H₂-type cubic terms, so the remaining region could still be cut there.

## 5. Consequences for Q4

1. The local route "nondegenerate torsion zeros are impossible" does not close at order 6. Steps 78–79 (Φ₆ > 0 at all tested jets) remain correct as data, but the generalization was a sampling artifact.
2. The correct order-6 statement is a semialgebraic constraint. At a nondegenerate AKE torsion zero, the jet (θ, λ/tn²) satisfies Φ₆ ≤ 0. Combined with 76.Z this cuts the strict cone further but leaves open regions for every sign of λ.
3. The next local test is order 8 along the constructed real order-6 family. If order 8 still leaves an open real region, the local formal route to closed negative Goldberg is not viable, and Q4 needs global input: forced zero count 5χ+6τ, index +1 at nondegenerate zeros (76.Z), and A01's degenerate-zero theory. Even if 79.C fails completely, one consequence stands: a closed negative AKE manifold has at least 5χ+6τ zeros counted with index, and every nondegenerate one has index +1 and satisfies the cone and Φ₆ ≤ 0 constraints.
4. For A01: one pipeline disagreement is resolved. Their converged D=6/D=8 runs are consistent if their seeds lay in {Φ₆ ≤ 0}. The shared jet lies in {Φ₆ > 0}.

## 6. Files
- `scripts/step80_universal_pi.py` → `data/step80/universal_pi.{json,npz}`
- `scripts/step80_lambda_scan.py` → `data/step80/lambda_scan_a.json`, `ell_ref_a.npy`
- `scripts/step80_F012_scan.py` → `data/step80/log_F012.txt` (the JSON write at the end failed after the table printed; the table is authoritative)
- `scripts/step80_reconstruct.py` → `data/step80/recon_{F012_gen2_lam0, F012_gen2_lam-5, F012_gen5_lam-5, lsA_jet0_lam-1, lsA_jet0_lam-40}.{json,npz}`. The npz holds H2…H8, u0, N, C6, ell, pi, P, Hpi, jv, cpi, z, y, mons, mon_d*. Coefficient convention: H = Σ_d Σ_{a<6} Σ_{m∈mon_d[d]} v_d[a·n_d + m_index] B_a x^m, with B_a = anti_basis() of `step77_gn_germ.py`.

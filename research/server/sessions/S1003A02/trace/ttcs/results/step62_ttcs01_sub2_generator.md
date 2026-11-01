# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/plans/step61_open_range_global_mechanisms.md"
  ]
}
```

## Task

Research generation on the decisive remaining quantity in the four-manifold Einstein-gap lower-bound problem. Step 62 (file attached) shows that on M=X#kCP2bar (X minimal general type, A=c1^2(X), SW nonzero) the Einstein defect obeys the exact identity P/8pi^2=(k-kappa)+(upsilon-kappa)/3 at the Yamabe representative, with kappa the conformal Weyl deficit (kappa=A/2-(3/8pi^2)int|W+|^2) and upsilon the Yamabe excess, and LeBrun forces upsilon>=kappa+3kappa^2/4A. Hence the open-range lower bound is governed only by how much self-dual Weyl energy kappa per exceptional class a conformal structure can remove while keeping P small. Generate serious, mathematically specific mechanisms (a) to PROVE a bound kappa<=k+beta*p (or kappa_* = A/2-(3/8pi^2)inf int|W+|^2 <= k, or the stronger Gursky-type kappa<=k/2) — e.g. Weyl-energy localization/epsilon-regularity on blow-up necks, conformal capacity of a (-1)-class, harmonic ASD representatives of E_i and Weitzenböck formulas on Lambda^-, twistor or Penrose-type arguments, Bach-flow monotonicity, use of the full 2^k sign family on the Lambda^- side, orientation reversal with Bauer-Furuta; and (b) to REFUTE it by construction: conformal structures removing more than 8pi^2/3 of W+ energy per CP2bar summand at bounded P (ASD gluing à la Taubes/Donaldson-Friedman, large Burns cores, conformally symplectic or LeBrun-equality almost-Kähler metrics, period-violating approximations of the formal common mode). For each, state the precise inequality or construction, its quantifiers, which known objects (Kähler kappa<=0; certified CH cell kappa≈0.056/class, upsilon≈0.212/class; formal common mode kappa≈k) it must accommodate, and the cheapest decisive calculation. Do not invent literature; name precise knowledge requests if needed.

## Output

# Generator memo: what controls the Weyl deficit κ, and the self-dual Einstein configuration it must exclude

The central finding is a correction to Step 62. Corollary 62.D silently assumes κ ≤ k. The region κ > k admits p = 0 exactly, through self-dual Einstein data. Every SW and Chern–Weil constraint used so far is compatible with that data. Any proof of κ ≤ k + βp must therefore exclude near-self-dual, near-Einstein phases, and any refutation should be sought there. The derivations below are mine. Facts about literature appear only as named knowledge requests.

## 1. Two exact rewritings that fix the target

**κ as an anti-self-dual Weyl budget.** Use ∫|W⁺|² − ∫|W⁻|² = 12π²τ_M with τ_M = τ_X − k. Then for every g:

κ[g] = 9k/2 + (A − 9τ_X)/2 − Ω⁻[g],  where Ω⁻ := (3/8π²)∫|W⁻|².

For a ball quotient (A = 9τ_X), κ = 9k/2 − Ω⁻. In units of one Fubini–Study CP̄² summand (12π² of ∫|W⁻|²), the bounds on κ become per-class lower bounds on ∫|W⁻|²:

| Statement | Required per-class ∫\|W⁻\|² |
|---|---|
| 62.W (κ ≤ k) | ≥ 7/9 unit |
| 62.G (κ ≤ k/2) | ≥ 8/9 unit |
| Trivial bound (κ ≤ 9k/2) | ≥ 0 |

Known per-class budgets:
- Kähler and Burns cells: about 1 unit.
- Certified cell: 1 − 0.0125 unit.
- Formal common mode: 7/9 unit exactly. It sits on 62.W.

The independent unknown is how little anti-self-dual Weyl energy an exceptional class can carry. Equivalently, it is the per-class Pareto frontier φ(q) := sup{κ_class : p_class ≤ q}. 62.C(i) is the statement φ(q) ≤ 1 + βq.

**The SW-only window.** Apply LeBrun's (62.2) through the parametric Cauchy–Schwarz inequality

(1 + 1/μ)∫s² + 6(1 + μ)∫|W⁺|² ≥ 72π²(A + Π).

This gives ∫|W⁺|² + t∫s² ≥ 72π²A·t/(1 + 6t), with t = 1/(6μ). Rewrite 62.C(iii) with P = 4∫|W⁺|² + Y²/12 − 8π²(A − k). It is a weighted inequality of the same shape, with weight t_β = β/(12(3 + 4β)) and right side π²[4(A − 2k) + 8β(A − k)]/(3 + 4β).

LeBrun's family at t_β gives (4β/(2+3β))π²A. The A-coefficient gap is 8(1+β)²/((3+4β)(2+3β)). Hence:

**SW Λ⁺ quadratic estimates prove 62.C(i) with constant β exactly when k ≥ A(1+β)/(2+3β).**
- At β = 0 this is k ≥ A/2, which is vacuous because κ_* ≤ A/2.
- As β → ∞ it becomes k ≥ A/3, LeBrun's threshold.
- At β = ∞, (iii) reduces to Gauss–Bonnet.

This is a closed explanation of why Steps 36–48 stopped at 2/3. Field theory on Λ⁺ covers the band A/3 ≤ k ≤ A/2 and nothing below it. A short corroborating check: the formal mode saturates 62.W but not this window.

## 2. Self-dual Einstein data: compatible with every constraint used so far

Suppose g is Einstein with W⁻ = 0 (self-dual Einstein, i.e. 4-dimensional quaternion-Kähler) on M = X#kCP̄², with X a ball quotient. Normalise s = −4. Gauss–Bonnet and signature then fix everything:
- 12π²τ = ∫|W⁺|² gives ∫|W⁺|² = 12π²(A/9 − k).
- 8π²χ − 12π²τ = ∫s²/24 gives V = 2π²A + 30π²k.

Hence κ = 9k/2, υ = 15k and p = 0. Identity 62.1 checks: k − 6k + 5k = 0.

LeBrun's (62.2) holds: 2√(A+15k) + √(A−9k) = 3√A + 10.5k/√A + …, and it holds for all k ≤ A/9. LeBrun's Einstein estimates also hold:
- 2χ + 3τ = A − k ≥ (2/3)A, i.e. k ≤ A/3;
- V ≥ 2π²A.

Theorem 62.A holds because L_A(k, 9k/2) < 0.

**Consequences.**
1. Step 62's Corollary 62.D derives κ/k → 1 and υ − κ = o(k) from p/k → 0. That inference silently assumes the Weyl shortfall k − κ is nonnegative. For κ > k, p = 0 is consistent with υ − κ = 3(κ − k) of any size. The dangerous region is κ > k, and it is populated by self-dual Einstein data.
2. This configuration exists formally only when τ_M ≥ 0, i.e. k ≤ A/9. For A/9 < k < A/3 the analogous template must carry W⁻ ≠ 0.
3. A geometric picture is a hybrid: a complex-hyperbolic (CH) bulk containing pockets that are approximately real-hyperbolic (RH⁴) and approximately self-dual. Per exceptional class the bookkeeping is exact:
   - remove 18π² of CH volume, which carries W⁺ energy 12π²;
   - add 48π² of RH volume, a ball of radius ≈ 1.5 curvature radii at curvature −1/3.

   So the building block is an O(1)-size cell, not a diffuse mode.

**A rigorous local input: the parity lemma.** A conformally flat neighbourhood of a sphere with odd self-intersection does not exist.
- The disc bundle is simply connected, so it develops by a codimension-0 immersion into S⁴.
- An immersed sphere in S⁴ satisfies e(ν) + 2d = 0, where d is the signed double-point count. Hence e(ν) is even.

So pure RH pockets cannot contain the E_i. Every exceptional sphere in a self-dual Einstein cell must sit where W⁺ ≠ 0, in an intermediate (non-CH, non-RH) curvature type.

Analytic continuation adds a second constraint. Self-dual Einstein is elliptic modulo diffeomorphisms. A self-dual Einstein structure equal to CH² on an open set is therefore locally CH² everywhere. Self-dual Einstein cells cannot have exact CH collars: the CH–cell transition must itself cost Ric°, or the whole metric must be a non-symmetric self-dual Einstein metric.

**Decisive local computations.**

1. *U(2)-invariant transition cell.* Take metrics dr² + a²(σ₁² + σ₂²) + c²σ₃² with s ≡ −4, closing on an O(−1) bolt (c ~ r, a(0) > 0) and matched at radius R to the CH² profile. Minimise ∫|Ric°|² subject to ∫|W⁻|² ≤ (7/9 − δ)·12π², and plot the resulting per-class frontier φ(q).
   - This is a two-function ODE optimisation.
   - Cost scale: the Step-48/49 Bianchi IX machinery, plus interval certification of one profile.
   - If φ(q) > 1 + βq for small q at some R, then 62.C(i) fails for that β locally. If instead the minimal cost for κ_class > 1 is bounded below, its value is the first piece of a per-class Weyl capacity theorem.

2. *Exact self-dual Einstein data with U(2) or T² symmetry.* Do Pedersen-type U(2)-invariant self-dual Einstein metrics with s < 0, or Calderbank–Pedersen toric self-dual Einstein metrics, realise a neighbourhood of a (−1)-sphere with W⁻ = 0? If they do, the cell problem reduces to an interface between an exact self-dual Einstein cell and a CH collar. The interface cost per unit area, times the area, is then the whole tariff.

## 3. Proof mechanisms

**(a) Excluding self-dual Einstein phases: Λ⁻ as a definite connection.** If W⁻ = 0 and Ric° = 0, the curvature of the Levi-Civita connection on Λ⁻ is exactly (s/12)·id from Λ⁻ to Λ⁻, and zero on Λ⁺. This is an anti-self-dual SO(3)-connection whose curvature is nondegenerate (definite). On M̄ this is the setting of Fine's definite-connection formulation of anti-self-dual Einstein metrics with s < 0.

The inequality to aim for:

∫|W⁻|² + C·P ≥ c·(number of exceptional classes),

obtained by showing that a near-definite connection on a bundle with w₂ = w₂(M) cannot be near-definite near a (−1)-sphere. The local reason would be the parity lemma, upgraded from conformally flat to definite.

Cheapest test: check whether Λ⁻ restricted to the E_i sphere, which has p₁-type degree tied to E_i² = −1, admits a connection with definite curvature on a tubular neighbourhood. This is a finite-dimensional topological computation about SO(3)-bundles over the O(−1) disc bundle, once the definite structure is written as a bundle isomorphism F: Λ⁻ → ad.

**(b) The almost-Kähler gauge of E_i⁻ on M̄ (near-symplectic forms).**

Setup.
- Let ψ be the harmonic anti-self-dual representative of E_i⁻. It is closed, and ∫|ψ|² = |E_i⁻|² ≥ 1.
- Off its zero set Z(ψ), generically circles, the gauge g_ψ = (|ψ|_g/√2)·g makes (M̄, g_ψ, ψ) almost-Kähler. So ψ is a near-symplectic form on M̄.

Derivation, using the Weitzenböck identity at |ψ| = √2 with s* := 2⟨Rψ, ψ⟩:
- s* − s = |∇ψ|²;
- the Hermitian scalar identity ∫(s + s*)/2 = 4π c₁(J_ψ)·[ψ];
- together: ∫(2s/3 + W⁻(ψ, ψ)) dμ_ψ = 4π c₁(J_ψ)·[ψ].

With W⁻(ψ, ψ) ≤ 2√(2/3)|W⁻| and Vol_ψ = |E⁻|²/2,

∫|W⁻|² ≥ (3/4)·[4π c₁(J_ψ)·[ψ] − (2/3)∫s_ψ dμ_ψ]²₊ / |E_i⁻|²  (plus Z(ψ) corrections).

Calibration: Fubini–Study on CP² gives exactly 12π² with c₁·[ω] = 3.

To reach the 7/9 threshold one needs 4π c₁·[ψ] − (2/3)∫s_ψ ≥ (4√7/3)π. That requires:
- c₁(J_ψ)·[ψ] close to 3;
- control of ∫s_ψ in a conformal class with Y < 0, where ∫s_ψ need not have a sign;
- the Taubes-type corrections from Z(ψ).

Cheapest test: on the Burns cell and the certified cell, compute ψ (from the existing cell solver), Z(ψ), c₁·[ψ] and ∫s_ψ. If c₁·[ψ] can be 1 rather than 3 at small P, this route closes at 1/9 of a unit and must be abandoned.

**(c) Phase separation and interface tension.** Theorem 48.L gives exponential coercivity near CH. An analogous Koiso-gap statement near any Einstein phase would give the following structure. Write κ = κ_small + κ_large:
- κ_small is the part with W⁺ within η of the Kähler orbit 𝒦. It is controlled at second order by Theorem 62.A and Theorem Y.
- κ_large comes from regions far from 𝒦. Its price is interface area times a tension σ_η, because Einstein phases cannot interpolate slowly (localized coercivity). Area dominates volume through the linear isoperimetry of CH-like regions.

The target inequality is κ_large ≤ Vol(far region)/(4π²) ≤ P/(4π²σ_η h). The hard case is the self-dual Einstein deformation phase, where σ_η may vanish as phases approach each other. The U(2) computation of §2 measures σ directly.

**(d) Orientation-reversed field theory.** A monopole class on M̄ would bound ∫|W⁻|² below by LeBrun-type estimates. The relevant square is c²(M̄) = 2χ − 3τ = A/3 + 5k for ball quotients, which would be more than enough. However, M̄ = X̄#kCP², and CP² summands carry positive scalar curvature and b⁺ = 1. SW and stable cohomotopy invariants are expected to vanish for such sums; this needs a source. If so, the route yields nothing unless a k-parameter family invariant exists.

## 4. Refutation candidates, sorted by what they can reach

| Candidate | Realised κ_class | Range | What it decides |
|---|---|---|---|
| Large Burns cores | ≈ 0 | — | Nothing new: W⁻ budget is 1 unit by conformal equivalence with CP̄² minus a point |
| Conformally symplectic and LeBrun-equality almost-Kähler metrics (formal mode, period-violating approximations) | ≈ 1 | — | They sit on the locus κ ≈ k. They test the constant β, not 62.W |
| Taubes/Donaldson–Friedman anti-self-dual (W⁺ = 0) structures | A/2 | needs k ≥ A/9 (τ_M ≤ 0) | Refutes 62.W purely conformally if the anti-self-dual threshold k_T is below A/2. Irrelevant for P: LeBrun gives p ≥ k − A/4 |
| Self-dual Einstein cells | 9/2 | k ≤ A/9 | The only configuration that could reach both 62.C and α itself. A compact self-dual Einstein metric on X#kCP̄² would give α = 0 |

## 5. Knowledge requests

1. Compact self-dual Einstein (quaternion-Kähler) 4-manifolds with s < 0: rigidity of locally symmetric examples, and existence of non-symmetric ones. Sources: LeBrun's H-space theorem; Biquard's Einstein deformations with prescribed conformal infinity.
2. Pedersen metrics and Calderbank–Pedersen toric self-dual Einstein metrics: the local topology they realise near (−1)-spheres.
3. Fine's definite connections, and any related Fine–Panov results on obstructions.
4. The Hermitian scalar identity ∫(s + s*)/2 = 4π c₁·[ω], and its normalisation of s* (Apostolov–Drăghici survey).
5. Taubes' Seiberg–Witten theory for near-symplectic forms, including the zero-circle contributions.
6. Quantitative Taubes thresholds for anti-self-dual structures on blow-ups of general-type surfaces.
7. Vanishing of SW and Bauer–Furuta invariants for connected sums with CP².
# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step45_o10_cell_tiling_tidal_radius_charge.md",
    "Sessions/S1003A01/workspace/scripts/step45_tnads_cartan.py",
    "Sessions/S1003A01/workspace/data/step45/tnads_cartan.json",
    "Sessions/S1003A01/workspace/scripts/step45_killing_moment_check.py",
    "Sessions/S1003A01/workspace/data/step45/killing_moment_check.json",
    "Skills/geometric-analysis/research/sources/archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/research/B/O10_Global_Compatibility.md",
    "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_generator2_integration.md"
  ]
}
```

## Task

Scientific verification of the Step-45 O10 note. Context: the O10 problem (density-free zero-Weyl endpoint lower bound for the four-manifold Einstein gap) and its escape regime chi/p->infinity, |W^-|/V->infinity, with a bounded resolvent negative spinor v, (L-2)v=q->0 in normalized L^2, m=|v|^2->m_*=128/81, and the Gibbons-Hawking/Taub-NUT tangent v=sqrt(m_*/2) d(bar f), m=m_*R/(R+ell). The note claims: (1) Taub-NUT-AdS with F=1+R(R+2ell)/3 is exactly Ric=-g with W^+=0 in the hyperkahler orientation (Cartan script + JSON supplied); (2) a tiling identity |Omega|=E_Omega/(2m_*) for flux-free completions and the interpretation of R(R+ell)^2=3ell/4 as a Wigner-Seitz radius of a nut lattice with base nut density theta Vbar/(pi ell); (3) the tidal coincidence ell/R_*^3->4/3, |W^-|^2->32/3; (4) Section 3: the radial/v0 solvability condition of the order-epsilon cell problem equals the flux balance, so there is no leading-order radial obstruction; (5) Proposition 4.1: on Einstein W^+=0 manifolds, nabla_X (dK)^+ = (s/6)(X wedge K)^+ for Killing K, with fixed-point values |(dK)^+| = 0 (nut), sqrt2 (bolt), 2sqrt2 (anti-nut) for unit-weight semi-free actions, giving the path bound int|K| >= 12/|s| from a nut to a bolt; checked on TNAdS; (6) the Stokes/Euler-number statement that a nut-only collapsed region must have boundary Euler number N, and the homogenized Helmholtz law Delta_gamma Vbar = -4 theta Vbar. Please check each mathematically: signs and constants (especially in Prop 4.1, the Killing identity nabla^2 K = R(.,K), the norms at fixed points, and whether the Lambda^- -> Lambda^+ block is Ric^0), the validity of the Stokes/Euler-number argument for semi-free circle actions (orbit-space boundary, orientation of nut charges relative to the 4D orientation and W^+), whether the claim that isolated cores are excluded 'by an exact identity' is justified or needs extra hypotheses (pointwise smallness of Delta m outside cells is not established in the unbounded-density regime), the Wigner-Seitz density and the averaged GH equation, and the interpretation in Section 6 (opening-volume heuristic, complex-hyperbolic cusp count). Identify any error, overstatement, or missing hypothesis, and state precisely which parts are rigorous, which formal, and which heuristic. Also say whether Prop 4.1 is known in the literature (quaternionic-Kahler moment map) only if you are confident, otherwise name the precise knowledge_request to make.

## Output

# Verification memo on the Step‑45 O10 note: concentration cells, the Killing‑moment identity, and the charge argument

Each item below is checked against the supplied scripts and JSON files, the O10 resolvent note, and independent calculations. The memo ends with a table that sorts each statement into rigorous, formal or heuristic.

Two items need correction:

- **Proposition 4.1 has the wrong sign.** The correct form is ∇_X(dK)⁺ = −(s/6)(X∧K)⁺.
- **The homogenized Wigner–Seitz law is missing a power of V̄.** The correct flat‑base law is Δ_γV̄ = −4θV̄², not −4θV̄.

Several interpretive statements also need extra hypotheses, or are not supported by the computation they cite:

- "isolated cores excluded by an exact identity";
- "TNAdS realizes the discharge";
- the charge‑discharge volume count.

---

## 1. Taub–NUT–AdS cell (item 1): exact, with three small corrections

**Frame structure.** I checked `frame_structure` by hand.
- With e¹=Bσ₁ and dσ₁=−σ₂∧σ₃, de¹ = (B′/AB)e⁰¹ − C⁻¹e²³.
- de² has the coefficient +C⁻¹ on e¹³.
- de³ = (C′/AC)e⁰³ − (C/B²)e¹².

The curvature conventions are sphere‑positive. Ric_{bd}=Σ_a R_{abad} gives +3 on S⁴, and the 6×6 matrix is the curvature operator. Λ⁺ is spanned by e⁰¹+e²³, e⁰²+e³¹, e⁰³+e¹² in orientation e⁰¹²³. So the reported chirality is meaningful.

**W⁺=0 holds exactly, not only numerically.** Put u = R(R+2ℓ). The radicand in the JSON is
R⁸+8R⁷ℓ+…+81 = (u+3)⁴.
I expanded u⁴+12u³+54u²+108u+81 term by term against the printed polynomial. The prefactor is P = R⁴+4R³ℓ+4R²ℓ²+6R²+12Rℓ+9 = (u+3)². Hence P − √(P²) ≡ 0. Since F = (u+3)/3, all W⁺ entries vanish identically.

**Numerical misquote.** The values 10⁻³⁰…8.7·10⁻¹⁸ in `flux_balance_rows` are float cancellation in P−√(P²). The note's "≤3·10⁻²¹ at all tested points" misquotes the JSON: the ℓ=10⁻⁶ row gives 8.7·10⁻¹⁸.

**Scalar‑curvature string.** The `scalar` entry is an unsimplified sympy expression. I evaluated it at R=ℓ=1. The six terms are −1, −0.75, −0.75, −1.75, −0.75, +1, which sum to −4. This is consistent with the four Ricci entries equal to −1.

**Literature form.** Write the standard self‑dual Euclidean Taub–NUT–AdS metric (Λ=−3/L²) in the form
Δ = (r−n)²[1+(r−n)(r+3n)/L²],
ds² = (r²−n²)Δ⁻¹dr² + 4n²Δ(r²−n²)⁻¹σ₃² + (r²−n²)(σ₁²+σ₂²).
Substitute r=R+n, ℓ=2n, L²=3. This gives exactly A²=H/F, B²=HR², C²=ℓ²F/H. So item 1 matches the known self‑dual TN–AdS family.

**A consistency check worth recording.** The TNAdS/TN ratio of |W⁻|² on the balance radius is 1−(2/3)ℓ² to the printed precision:

| ℓ | relative deficit of TNAdS |W⁻|² | (2/3)ℓ² |
|---|---|---|
| 10⁻² | 6.67·10⁻⁵ | 6.67·10⁻⁵ |
| 10⁻³ | 6.67·10⁻⁷ | 6.67·10⁻⁷ |
| 10⁻⁴ | 6.67·10⁻⁹ | 6.67·10⁻⁹ |

The rows ℓ=10⁻⁵ and 10⁻⁶ are roundoff (their deficit grows as ℓ decreases). The data therefore point to the exact formula
W⁻_TNAdS = ℓ(1−ℓ²/3)(R+ℓ)⁻³ · diag(−1,−1,2).
This vanishes at ℓ=√3, i.e. n=L/2, which is the known point where self‑dual TN–AdS becomes hyperbolic space. A one‑line `sp.factor` on the TNAdS W⁻ eigenvalue, after substituting the radicand by (u+3)², would confirm it. The note's "decreases rapidly" is thus precisely O(ℓ²).

**Norm convention.** The Frobenius norm of the 3×3 operator is the manuscript's convention. With it, CGB reads χ/V = 1/(12π²) + b/(8π²). Independent check:
∫_TN |W⁻|² = 16π²ℓ·6ℓ² ∫₀^∞ R(R+ℓ)⁻⁵ dR = 96π²ℓ³ · (1/12ℓ³) = 8π²,
i.e. χ(TN)=1. Each cell therefore carries one unit of Euler characteristic, and b ≈ 8π²N/V ≈ 2θ/ℓ² in the tiled phase.

---

## 2. Tiling identity (item 2): exact in integrated form; the pointwise sentence is wrong

**Mass equation.** With div‑grad Δ, Δm = 2|∇v|² − 4m − 2Re⟨q,v⟩ is correct.

**One‑centre data.** All four values are confirmed: E(R), flux 2E, M(R) = (16π²/3)m_*ℓR³, and the cubic from 4M=2E.

**Interpretation of the cubic.** M uses m, not m_*. So the cubic is the radius where ∫m/m_* (not the volume) reaches E/(2m_*). The two agree to relative order ℓ^{2/3}, which matches the 0.8779→0.9085 convergence.

**Hypotheses that are implicit.** |Ω| = E_Ω/(2m_*) + o(ℓ²) is an exact consequence of integrating over Ω, provided:
- ∮_{∂Ω}∂_νm = o(ℓ²);
- ∫_Ω |q|² = o(|Ω|);
- ∫_Ω |m−m_*| = o(|Ω|).

The last two follow from global normalized smallness only for all but a vanishing fraction of cells (Chebyshev), not for every cell. The existence of a flux‑free completion around a given core is assumed, not derived.

**The pointwise sentence is false, and the cell itself contradicts it.** The sentence in §2.1 reads "outside the cells … forces |∇v|²≈2m pointwise".
- Inside a TN cell, at R≈R_*, |∇v₀|² = m_*ℓ²/(R+ℓ)⁴ ~ ℓ^{2/3} → 0.
- Re⟨Lv,v⟩ ≈ 2m_*, so Δ⁺m ≈ 4m_*.
- Explicitly, the eigenvalue correction gives m ≈ m_*(1 − ℓ/R − (2/3)R²) for ℓ≪R≪1. Its radial derivative vanishes exactly at R³=3ℓ/4. This is a cleaner derivation of the balance radius: it is the radial maximum of m.

So the bulk of every cell has |∇v|²≈0, not 2m. In the exterior, m→m_* in measure and Δm bounded in normalized L² give Δm→0 only weakly, never pointwise.

**What the identity does give exactly.** It is an excluded‑volume (depletion) law, valid whatever the exterior does. For any flux‑free Ω containing a core ball B,
∫_{Ω∖B} (2m − |∇v|²) = E_B − 2∫_B m + o(ℓ²) = E_B + o(ℓ²).

Each core removes ambient gradient energy equal to its own energy. A core embedded in a bulk with |∇v|²≈2m_* is **not** excluded; it forces a depletion zone of volume ≈ E_B/(2m_*). What is excluded is only the configuration "cores plus an exterior with small total gradient energy and θ<1." That follows from the exact closed‑manifold identity ∫|∇v|² = 2∫m + Re∫⟨q,v⟩.

The phrase in §6.1, "isolated cheap insertions are excluded by an exact identity," overstates this. Isolated cores with depletion shells are compatible with every integrated identity in the note.

---

## 3. Wigner–Seitz density and the averaged GH law (items 2, 6): coefficient error

The Gibbons–Hawking data are verified:
- with V = V̄ + ℓ/R, ψ‑period 4πℓ and dω = *dV, the 4‑volume element is 4πℓ V vol_γ;
- ΔV = −4πℓΣδ_a;
- Δ_g = V⁻¹Δ_γ on invariant functions.

**The error.** The note keeps the cell volume 4π²ℓ²/θ independent of V̄. That is inconsistent with m→m_*. With background V̄,
g = V̄ · g_TN(ℓ′), ℓ′ = ℓ/V̄.
This follows from rewriting V̄(1+ℓ′/R)dx² + V̄⁻¹(1+ℓ′/R)⁻¹ℓ²σ₃² as V̄[H′dx² + H′⁻¹ℓ′²σ₃²].

The field normalized so that m→m_* has energy E = 8π²m_*ℓ′²·V̄ = 8π²m_*ℓ²/V̄, because bounded‑section Dirichlet energy scales as the metric homothety factor. Then:
- cell volume = 4π²ℓ²/V̄;
- base volume per nut = πℓ/(θV̄²);
- n₃ = θV̄²/(πℓ).

The averaged law is therefore
Δ_γV̄ = −4θV̄²,  equivalently  Δ_gV̄ = −4θV̄.
It is not Helmholtz. On flat ℝ³ the Lane–Emden exponent 2 lies below the Serrin exponent n/(n−2)=3, so no positive supersolution exists on all of ℝ³ (nor on exterior domains). The qualitative conclusion "V̄ cannot stay positive on a whole flat base" survives. The profile sin(2√θr)/r and its first zero do not; the length scale is (θV̄)^{−1/2}. The closed‑base obstruction (∫Δ_γV̄=0 against a strictly signed source) survives unchanged.

**The flat‑base model breaks down at the scale it predicts.** At distances O(θ^{−1/2}) the Einstein correction is O(1) in the metric, not only in Ricci. So "where V̄→0 the circle opens" is not derivable from this model.

**Exact replacement: Bochner subharmonicity.** For a Killing field K of a metric with Ric = −g, the Bochner formula gives
½Δ|K|² = |∇K|² − Ric(K,K) = |∇K|² + |K|².
Hence |K|² is strictly λ‑subharmonic, Δ|K|² ≥ 2|K|². A collapsed circle cannot keep a roughly constant length over distances ≳1 in an exactly invariant Einstein region. TNAdS realizes this: |K|² = 4ℓ²FR/(R+ℓ) ~ (4/3)ℓ²R².

The same formula carries a structural fact the note does not use: **a closed manifold with Ric = −g has no nonzero Killing field.** Every exact‑symmetry statement in §4 can therefore hold only on proper regions. Any global use concerns approximate symmetries.

---

## 4. Tidal coincidence (item 3): correct, and an algebraic consequence of the balance

- The table values are reproduced.
- For R≫ℓ, R_*³ → 3ℓ/4, so ℓ/R_*³ → 4/3 and 6ℓ²/R_*⁶ → 32/3.

This is not an independent coincidence. The cell volume ≈ (16π²/3)ℓR³ is fixed at E/(2m_*) = 4π²ℓ² by the eigenvalue 2. The TN Weyl scale ℓ/R³ is then ℓ²/(volume) up to constants. The content is that the eigenvalue 2 and the Einstein normalization s=−4 are the same scale in O10.

The physically important consequence is correctly drawn in the note: neighbouring cells overlap at O(1) Weyl curvature, so a lattice of cells is not a perturbative superposition. In the Ric = −g setting the multi‑centre problem is the nonlinear Toda problem, not linear GH superposition.

---

## 5. Order‑ε cell problem (item 4): formal, correct on round cells, unchecked on lattice cells

**Scale counting.** w ~ R_*² ≍ ε and torsion corrections ≍ ε^{1/2} are consistent.

**The v₀‑pairing.** Green's identity on the cell turns the v₀‑pairing into the integrated mass equation. "No obstruction" means precisely that this solvability condition fixes one parameter (the cell volume, i.e. the nut density). It is a constraint, not a free pass.

**The orthogonal kernel element, written explicitly.** On a GH space:
- x₃ is harmonic, since Δ_g = V⁻¹Δ_flat on invariant functions;
- the Killing 1‑form K♭ = V⁻¹η is harmonic, since Δ_dK♭ = 2Ric(K) = 0;
- I₃dx₃ = ±V⁻¹η;
- on a Kähler manifold Δ_d preserves type.

Hence
v₀^⊥ = √(m_*/2) (dx₃ ∓ iK♭),  with |v₀^⊥|² = 2/V = |v₀|²/(m_*/2) up to the same constant,
is a bounded L_h‑harmonic section pointwise orthogonal to v₀ = √(m_*/2) d f̄.

**When the v₀^⊥ pairing vanishes.** Under rotation about the x₃‑axis (which preserves I₃), v₀ has charge ±1 and v₀^⊥ has charge 0. So the v₀^⊥‑pairing of *every* SU(2)×U(1)‑invariant operator acting on v₀ vanishes on a round cell. This includes the TN→TNAdS correction of L, which the note listed but did not evaluate. On a periodic Wigner–Seitz cell only the lattice symmetry remains, and this pairing is not shown to vanish.

The note's statement that the obstruction must sit in the torsion, determinant‑curvature and quadratic monopole terms is therefore justified only on round cells.

---

## 6. Proposition 4.1 (item 5): sign error; constants, fixed‑point values and the path bound are correct and sharp

**Sign.** Take a Killing field K with ∇²_{X,·}K = R(X,K). Then dK = 2(∇K)♭ and ∇_X dK = −2ℛ(X∧K), where ℛ is the sphere‑positive curvature operator.

- *Unit S².* K = ∂_φ gives dK♭ = 2cosθ vol. Its derivative along e_θ is −2sinθ vol, while e_θ∧K♭ = +sinθ vol.
- *Projection to Λ⁺.* The Λ⁻→Λ⁺ block is indeed Ric° (the traceless‑Ricci block of ℛ). With W⁺=0 and Ric°=0, ℛ|_{Λ⁺} = (s/12)Id. Therefore
  **∇_X(dK)⁺ = −(s/6)(X∧K)⁺.**
- *TNAdS confirms the minus sign.* I verified by hand a+b = 2ℓF′R/(R+ℓ) = 4ℓR/3. So (dK)⁺ = (2√2/3)ℓR increases along e₀ in the same direction as (e⁰∧K)⁺ = C(e⁰³+e¹²), with coefficient +2/3 = −s/6 at s=−4.

The script compares only |s|/6, which hides the sign. The sign does not affect the Kato‑type bounds below.

**Fixed‑point values.** For weights (λ₁,λ₂) in an oriented frame, dK = 2λ₁e¹² + 2λ₂e³⁴. Hence |(dK)^±| = √2|λ₁±λ₂|. This gives 0 (triholomorphic nut, weights (1,−1)), √2 (bolt), and 2√2 (anti‑nut). These values are pure linear algebra and need no Einstein condition. The normalization K = 2∂_ψ with period 2π gives unit weights.

**Path bound.**
- A decomposable form satisfies |(X∧K)⁺| = |X∧K|/√2 ≤ |K|/√2.
- So |∇|(dK)⁺|| ≤ (|s|/(6√2))|K|.
- This gives ∫|K| ≥ 12/|s| from nut to bolt and ≥ 24/|s| from nut to anti‑nut.
- At s=−4 these are 3 and 6.

**Sharpness.** Along the radial geodesic of TNAdS, |K|·ds = 2C·A dR = 2ℓ dR exactly. So ∫₀^{3/(2ℓ)}|K|ds = 3, which equals the threshold. TNAdS saturates the inequality: e₀ ⊥ K, and (dK)⁺ stays on one ray. The constant 12/|s| cannot be improved by this argument.

**Wording in §4.** "Opening of the circle and loss of the triholomorphic type occur together" is inaccurate. (dK)⁺ becomes nonzero immediately, linearly in R. What coincides with circle length of order one is reaching the bolt value √2.

**Literature.**
- I am confident that the nut/bolt/anti‑nut classification by the duality type of dK, together with the localization of χ and τ on fixed points, is Gibbons–Hawking, "Classification of gravitational instanton symmetries," Comm. Math. Phys. 66 (1979).
- The identity is structurally the four‑dimensional case of the Galicki–Lawson quaternionic‑Kähler moment map, with (dK)⁺ playing the role of μ_K and ∇μ_K ∝ ι_KΩ. I am confident of this interpretation but not of a reference that states it with this normalization.
- Precise knowledge_request: *"For a self‑dual Einstein 4‑manifold with Killing field K, the identity ∇_X(dK)^{sd} = c·s·(X∧K)^{sd} and the use of |(dK)^{sd}| as the Toda/LeBrun coordinate z: exact statement and normalization in Tod (1995/97, SU(∞)-Toda paper), Przanowski (1991), and Calderbank–Pedersen (2002, self-dual Einstein metrics with torus symmetry)."*

---

## 7. Stokes/Euler‑number argument (item 6): correct under hypotheses the note does not state

**What holds.** For a smooth semi‑free S¹‑action on a region U:
- isolated fixed points map to interior points of the 3‑dimensional orbit space U*;
- bolts map to its edge (Fintushel's description).

The degree of the circle bundle over the linking S² of an isolated fixed point is ±1. Nuts and anti‑nuts carry opposite signs relative to the 4D orientation. Stokes on U* minus small balls gives deg(∂U*) = N_nut − N_anti, with bolts as the other source. So "nut‑only with closed orbit space is impossible" and "∂U* carries degree N" are rigorous.

**Hypotheses that must be added.**

1. **The action is global, exact, semi‑free and orientable.** If the collapse is described only by an F‑structure whose circle is defined up to sign (Z₂‑twisted), η is not globally defined, and the degree count fails. The hyperkähler analogue shows this is the generic mechanism:
   - Foscolo's collapsing K3 metrics (J. Differential Geom. 2019) cancel the Gibbons–Hawking nut charge on T³/Z₂ at D_k ALF / Atiyah–Hitchin pieces;
   - those pieces carry no triholomorphic circle and live at the collapsed scale.

   "Bolts and anti‑nuts are the only fixed components that can contribute with the opposite sign" is thus true only for orientable circle actions. Whether s=−4, W⁺=0 analogues of D_k pieces exist is the relevant open question. Prop 4.1 is linear in K and survives K→−K, so it does not exclude them.

2. **Degree is not Euler characteristic.** The degree of the circle bundle is not χ(M): nuts and anti‑nuts both add +1 to χ. The note uses "Euler number" for both, notably for the complex‑hyperbolic cusp in §6.3.

3. **The count from c₂(E₋) is signed.** c₂(E₋) counts zeros of v with sign. It bounds N from below only if every positive zero is a nut and no oppositely oriented zeros occur. At a nut, d f̄ ~ z̄₂dz̄₁ + z̄₁dz̄₂ has local degree +1, which fits, but the global identification is formal.

4. **Transfer to O10 is the hardest gap.** O10 sequences have no Killing field: by §3, they cannot have one when exactly Einstein. With |W⁻|² unbounded on average, Cheeger–Fukaya–Gromov theory does not supply an N‑structure. The note's open item (ii) is precisely this.

**TNAdS does not discharge anything.** Its circle bundle has degree 1 on every sphere R = const, out to conformal infinity. R = 3/(2ℓ) is only the earliest radius at which a bolt could appear on that geodesic.

---

## 8. Charge‑discharge volume (§6.3): an exact coarea bound shows the volume is O(V) unless |dK| is controlled

The following holds in an exactly K‑invariant region T with Ric = −g and W⁺ = 0, where u = |(dK)⁺| runs from 0 (nuts) to √2 (bolts). Anti‑nuts have u = 2√2 and so lie outside T.

**Step 1 (Prop 4.1).** |∇u| ≤ (√2/3)|K|.

**Step 2 (coarea).** The level sets Σ̃_t are free K‑invariant 3‑manifolds with area element 2π|K| dA_Σ in the quotient metric. Therefore
Vol(T) ≥ ∫₀^{√2} ∫_{u=t} |∇u|⁻¹ ≥ 6π · inf_t Area_q(Σ_t).

**Step 3 (degree).** Let η = K♭/|K|², with period 2π. Its horizontal curvature is dK♭|_hor/|K|², because the d|K|∧K♭ term vanishes on horizontal vectors. Stokes gives 2πN = ∫_{Σ_t} dη. Hence
Area_q(Σ_t) ≥ 2πN · inf_{Σ_t}(|K|²/|dK|).

**Step 4 (combine).**
Vol(T) ≥ 12π² N · inf_T(|K|²/|dK|).
With |K| ≈ 2ℓ and N ≈ θV/(4π²ℓ²), this becomes **Vol(T) ≳ 12θV / sup_T|dK|**.

**Consequences.**
- Keeping the circle collapsed is the cheapest route, because opening only increases |K|²/|dK|.
- When |dK| ≍ 1 on the collar (its value at every nut is 2√2), the discharge volume is a fixed fraction of V. There is no contradiction.
- A volume obstruction requires |dK| ≲ |K| on the collar, i.e. bounded O'Neill tensor. That gives Vol ≳ Nℓ ≍ θV/ℓ ≫ V.
- The open item (iv) therefore reduces to one quantity: **the ratio |dK|/|K| in the collar, equivalently whether a large O'Neill tensor at collapsed scale must cost Ric° or W⁺ energy, or can be paid entirely in W⁻.**

The complex‑hyperbolic cusp count is consistent with this. Its Nil slices of degree d have area ∝ d × (fibre length), so the volume is ≍ d at unit length and ≍ dℓ² ≍ θV at length ℓ.

Two further points are unchecked:
- whether the CH² end in its W⁺=0 orientation carries degree of the sign of the nuts;
- that a closed M cannot end in a cusp. The cusp would have to be capped by a bolt, which Cor 4.2 places at ∫|K| ≥ 3.

---

## 9. Classification of the note's statements

| Statement | Status |
|---|---|
| TNAdS: Ric = −g, W⁺ = 0 exactly; matches self‑dual TN–AdS (ℓ=2n, L²=3) | Rigorous (radicand = (u+3)⁴) |
| W⁻_TNAdS = (1−ℓ²/3) W⁻_TN; ℓ=√3 gives H⁴ | Numerically inferred, one factorization from exact |
| TN energies, flux, mass, cubic, R_* table | Rigorous |
| \|Ω\| = E_Ω/(2m_*) for flux‑free Ω | Rigorous under three local hypotheses (most cells) |
| Depletion law ∫_{Ω∖B}(2m−\|∇v\|²) = E_B | Rigorous; the correct form of "exclusion" |
| "\|∇v\|² ≈ 2m pointwise outside cells"; "isolated insertions excluded" | Unsupported; false inside cells |
| Wigner–Seitz n₃ = θV̄/(πℓ), Helmholtz Δ_γV̄ = −4θV̄ | Incorrect power: n₃ = θV̄²/(πℓ), Δ_γV̄ = −4θV̄² |
| Closed‑base averaged obstruction | Rigorous for the averaged equation |
| Tidal values 4/3, 32/3 | Rigorous; algebraic consequence of the balance |
| §3 v₀‑solvability = flux balance; v₀^⊥ pairing zero | Formal; v₀^⊥ zero proven only on round cells |
| Prop 4.1 | Correct after the sign change −s/6 |
| Fixed‑point values; ∫\|K\| ≥ 12/\|s\|, 24/\|s\| | Rigorous for exact symmetry; sharp (TNAdS) |
| Stokes degree N on ∂U* | Rigorous for global orientable semi‑free actions; open for Z₂‑twisted structures |
| "TNAdS realizes discharge" | Incorrect |
| §6.3 volume ≫ V, CH² cusp | Heuristic; the coarea bound gives only O(V) unless \|dK\| ≲ \|K\| |
| Transfer of §4 to O10 sequences | Missing: no Killing fields on closed Ric = −g; no N‑structure under unbounded W⁻ |

**Net scientific content.** The exact pieces fit together:
- the depletion law;
- the corrected Killing‑moment identity, with TNAdS saturating its path bound;
- Bochner subharmonicity of |K|²;
- the coarea bound Vol ≥ 12π²N inf(|K|²/|dK|).

They reduce the density‑free O10 question in the collapsed‑nut picture to a single local quantity: the cost, in Ric° and W⁺ energy, of a large horizontal dK at collapsed circle length. The Z₂‑twisted (Atiyah–Hitchin‑type) discharge channel is the competing mechanism.
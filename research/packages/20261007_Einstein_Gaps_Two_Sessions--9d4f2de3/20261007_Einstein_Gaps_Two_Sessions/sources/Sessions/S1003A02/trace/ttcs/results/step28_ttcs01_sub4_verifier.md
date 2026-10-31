# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/scripts/chiral_flux_identity.py",
    "Sessions/S1003A02/workspace/data/chiral_flux.json",
    "Sessions/S1003A02/workspace/scripts/chiral_flux_models.py",
    "Sessions/S1003A02/workspace/data/chiral_flux_models.json",
    "Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py"
  ]
}
```

## Task

Independently verify Theorem X in the supplied Step-27 note. Check the orientation and normalization of the two chiral curvature blocks, the derivation of the signature transgression from the displayed exact formula/data/script, both localized identities, and every entry of the charge table (smooth centre, O(-1) bolt, Berger collapse, CH, Burns, Taub-bolt). Look especially for constant shifts, sign reversals, or a false identification of block A with W+ in the blow-up orientation. Give a direct mathematical verification rather than accepting the zero symbolic residual.

## Output

# Verification memo: Theorem X (chiral transgressions), Step 27

## Summary

Theorem X is correct as stated, and its orientation and normalization are right. The two localized identities hold. Every charge in the table checks against independent hand computation, against the model metrics, and against four closed cohomogeneity-one manifolds.

The polynomial 𝔰 has a much simpler closed form than the 21-term numerator in `chiral_flux.json`. That form exposes the mechanism: each chiral flux is minus a frame Chern–Simons invariant of one chiral connection, shifted by a constant. Through this structure, the + identity reduces to identities that `perp_cartan_verify.py` already proves.

Four textual or mathematical corrections are needed (§6):

- a factor-2 slip in the Hitchin–Thorpe display;
- a ±6 offset between the `bA`/`bB` fields in `chiral_flux.json` and the note's b_±;
- a wrong remark in Corollary X2;
- an unstated hypothesis in the Berger-collapse charge.

The last one turns into a sharper anisotropic charge formula tied to the 4/ε mode of §3.

## 1. Closed form of 𝔰 and its Chern–Simons origin

Write p_i = a_i' and γ_i = (a_j²+a_k²−a_i²)/(a_j a_k).

**Grouping the numerator.** Dividing the numerator of `S` by a²b²c² and collecting terms gives two pieces.

- The derivative terms collect exactly to Σp_i² − (γ₁p₂p₃ + γ₂p₃p₁ + γ₃p₁p₂). For example, the a₁b₁ coefficient is (c²−a²−b²)/(ab) = −γ₃.
- The jet-free part is [2Σa_i⁶ − 2Σ_{i≠j}a_i⁴a_j² + 12a²b²c²]/(a²b²c²) = 2Σγ_i². Expanding Σ a_i²(a_j²+a_k²−a_i²)² reproduces this numerator term by term.

Hence

  S = 2Σγ_i² + Σp_i² − Σγ_i p_j p_k,

which is fully symmetric under permutations of the three slots.

**Chiral connections.** Restrict the Levi-Civita connection to an orbit. In the σ-coframe its components are ω_{i0} = p_iσ_i and ω_{jk} = γ_iσ_i. The two chiral SO(3) connections have components that are constant on the orbit:

- u = p − γ, the variable of `perp_cartan_verify.py`;
- ũ = −(p + γ).

Both are flat on the Euclidean cone (u = 0; ũ = −2 gives F_i ∝ 2ũ_i + ũ_jũ_k = 0).

Their frame Chern–Simons functions, in the normalization of `C` in that module, are:

- CS₋ = C = Σu² + u₁u₂u₃;
- CS₊ = Σ(p+γ)² − Π(p+γ).

**Euler flux.** The Step-26 flux equals b_E = ½(CS₊ − CS₋) exactly. The verification uses the identity a_ja_kK3_i = 2γ_i − γ_jγ_k, checked by direct expansion, so that b_E = Σp_i(2γ_i − γ_jγ_k) − p₁p₂p₃.

**Signature flux.** ½(CS₊ + CS₋) = Σp² + Σγ² − Σγ_ip_jp_k − γ₁γ₂γ₃. The law-of-cosines identity Σγ_i² + γ₁γ₂γ₃ ≡ 4 (the algebraic form of Σcos² + 2Πcos = 1) turns this into

  𝔰 = S − 6 = ½(CS₊ + CS₋) − 2.

**Resulting chiral fluxes.**

  b₊ = b_E − 𝔰 = 2 − C(u),  b₋ = b_E + 𝔰 = CS₊ − 2.

The uniqueness asserted in the note is consistent with this. Total-derivative kernels on 2-jets are constants, and the CS combination lies in the 84-term ansatz.

## 2. Orientation and normalization of the blocks

**Self-duality of block A.** In `LA`, the rows are (e₀ₖ + e_{jk})/√2 with pairs (01|23), (02|31), (03|12). These are self-dual for e⁰¹²³ = dt∧σ₁₂₃. So B_A = tr(W₊²) in that orientation, with W_A = U₊ − s/12, where U₊ is the Λ⁺ block of the curvature operator.

**Sign of the trace subtraction.** The trace of U₊ is s/4, because the cross terms cancel by the first Bianchi identity. The sign of the subtraction is confirmed by two outputs: H⁴ gives B_A = B_B = 0, and CH gives B_B = 0. If the subtraction carried the wrong sign, both of these would be nonzero.

**Normalization.** For Fubini–Study (s = 24), W₊ = diag(4, −2, −2), so trW₊² = 24 and ∫trW₊² = 24·π²/2 = 12π². Hence τ = (1/12π²)∫(B_A − B_B)dvol, the standard normalization. The Burns quadrature confirms this independently: (1/12π²)·(−2π²·6) = −1 = τ(O(−1)).

**Block A carries the Kähler Weyl curvature of CH.** On CH (a = sinh t cosh t, b = c = sinh t), the form d(½sinh²t σ₁) equals e⁰¹ + e²³. It is self-dual and is the Kähler form. So e⁰¹²³ is the complex orientation, and W₊ = (−4, 2, 2) is the Kähler Weyl tensor (s = −24). In the u-variables, u = (3sinh²t, 0, 0): a single nonzero component, which is the U(1)-reduction of the Λ⁺ connection.

**Block A is W₊ in the blow-up orientation.** For Burns, d(½r²σ₃) = e⁰³ + e¹² is again self-dual and is the Burns Kähler form. The holomorphic curve r² = m is the exceptional curve, of self-intersection −1 in the complex orientation. The identification therefore holds: e⁰¹²³ is simultaneously the CH-Kähler and the blow-up orientation. This is forced by the sign dσ_i = +2σ_j∧σ_k, which makes σ₁-circles complex Hopf circles. All permutations within the σ-convention preserve this orientation; only t → −t reverses it. This is consistent with 𝔰 being even and b_E odd in p.

## 3. Direct proof of both localized identities

**The + identity.** Since b₊ = 2 − C, the derivative is b₊' = −C' = −W Σr_iv_i. This is the `C_transgression_identity` of `perp_cartan_verify.py`. The + identity, W|Ric°|²/4 = b₊' + WB_A + Ws²/48, therefore becomes

  B_A = Σ(r_i − v_i)²/4 + Σr_iv_i − (Σ(r_i + v_i))²/12 = Σq_i²/4 − (Σq_i)²/12,  q_i = r_i + v_i.

Here the identities |Ric°|² = Σ(r−v)² and s = −2Σq from the same module have been used.

This is the statement that U₊ = −½ diag(q). It holds for a structural reason. The u-connection has curvature r_i e⁰ⁱ + v_i e^{jk}. Its self-dual projection along ξ_i is ∝ (r_i + v_i), and the diagonal Bianchi-IX reflections kill the off-diagonal entries. The trace s/4 = −Σq/2 then fixes the constant at −½. The anti-self-dual projection ∝ (r − v) is the Ric° block, consistent with the module.

Explicit confirmations of U₊ = −½ diag(q):

- CH: q = (12, 0, 0), so B_A = 36 − 12 = 24.
- Burns: u = (0, 0, −m/r²), r₃ = 2m/r⁴, v₃ = −2m/r⁴, so q = 0 and B_A = 0; r − v gives |Ric°|² = 16m²/r⁸.

**Integration.** With orbit volume 2π²W, the three non-flux terms integrate to (1/2π²)∫|W₊|² and (1/96π²)∫s², and the Ricci term integrates to P̂. So (1.1) follows from the pointwise identity.

**The − identity.** This is (Step-26 Euler identity) + 𝔰', with 𝔰' = W(B_A − B_B)/2 = b_E' − b₊'. The same chiral argument applied to ũ gives B_B = Σq̃²/4 − (Σq̃)²/12. I did not expand this by hand for a general jet. It is confirmed on the CH, Burns, Taub-bolt and Taub-NUT quadratures below.

## 4. Charge table: every entry recomputed from (u, ũ)

| orbit | p | γ | C(u) | b₊ = 2 − C | CS₊ | b₋ = CS₊ − 2 | b_E |
|---|---|---|---|---|---|---|---|
| smooth centre, a_i = t + O(t³) | (1,1,1) | (1,1,1) | 0 | 2 | 12 − 8 = 4 | 2 | 2 |
| regular bolt, fibre a (a' = 1, b − c = O(t²)) | (1,0,0) | (2,0,0) | 1 | 1 | 9 | 7 | 4 |
| Berger, a = ε, a' → 0, b = c | (0,U,U) | (2,0,0) | 4 + 2U² − 2U² = 4 | −2 | 4 | 2 | O(ε) |
| CH, radius t | | | 9sinh⁴t | 2 − 9sinh⁴t | 1 + 6k² − 3k⁴, k = cosh t | 2 − 3sinh⁴t | 2 − 6sinh⁴t |

All entries agree with the note.

- **Euclidean values.** S = 6 at the Euclidean point was confirmed by summing the coefficients: the jet-free part gives 6 and the derivative part gives 0.
- **Berger second order.** The O(ε²) form of 𝔰 matches `berger` in the json, as recomputed from the grouping in §1.
- **Bolt rows.** The bolt values require γ_b, γ_c → 0, i.e. (b² − c²)/(ac) → 0. This holds when b − c = O(t²), which is what regularity at a Z₁-Hopf bolt imposes. It is consistent with the `bolt3` jet.
- **Real-hyperbolic row.** The orbits are round with p = λ, so b₊ = b₋ = b_E = 3λ − λ³ (λ = cosh t for H⁴). This is consistent with the json value bE = −(sinh²t − 2)cosh t.

## 5. Model and global checks

**Burns.** Exactly, b₊(r) = 2 − m²/r⁴ and b₊' equals the P̂-density, so P̂[0,t] = b₊(t) − 1 at every t. This is the equality case of X1. Further:

- W dt = r³ dr, so ∫WB_B = 24∫₁^∞ r⁻⁵ dr = 6 and P̂ = 4∫₁^∞ r⁻⁵ dr = 1.
- The − identity balances: (2 − 7) + 6 = 1.
- The bolt is regular with c' = 1.

**Taub-bolt (n = 1).** Here W dt = 16(r² − 1) dr.

- ∫₂^∞ 16(r²−1)·243/(8(r+1)⁶) dr = 486·(1/81 − 1/162) = 3.
- ∫₂^∞ 16(r²−1)·3/(8(r−1)⁶) dr = 6(1/3 + 1/2) = 5.
- Regularity: c' = 2nV'(2n) = 1.
- At infinity, u → (2, 2, −2), so C = 8 + 4 − 8 = 4 and b₊ = −2.

The block norms have the form B_A = 6(M+n)²/(r+n)⁶ and B_B = 6(M−n)²/(r−n)⁶ with M = 5n/4.

**Taub-NUT (M = n).** The table predicts W_B ≡ 0 and ∫WB_A = 2 − (−2) = 4. Direct computation gives 384∫₂^∞ (x − 2)x⁻⁵ dx = 384/96 = 4, and B_B = 0 since M − n = 0. This also gives ∫|W|² = 8π², i.e. χ = 1 with a vanishing ALF Euler term.

**Closed manifolds.** The end orbit at t₁ has p → −p. The relation Δb_± = −(2χ ± 3τ) holds in all four cases:

| manifold | b₊ start → end | Δb₊ = −(2χ+3τ) | b₋ start → end | Δb₋ = −(2χ−3τ) |
|---|---|---|---|---|
| S⁴ | 2 → −2 | −4 | 2 → −2 | −4 |
| CP² | 2 → −7 | −9 | 2 → −1 | −3 |
| CP̄² | 1 → −2 | −3 (τ = −1) | — | — |
| CP² # CP̄² (two Z₁ bolts) | 1 → −7 | −8 (χ = 4, τ = 0) | — | — |

Fubini–Study (P̂ = 0) also checks the closed formula P̂ = (1/2π²)∫|W±|² + (1/96π²)∫s² − (2χ ± 3τ): the + side gives 6 + 3 − 9 = 0 and the − side gives 0 + 3 − 3 = 0.

These four manifolds pin down the constant normalization of 𝔰 and the orientation independently of the symbolic residual.

## 6. Corrections

**1. Hitchin–Thorpe display.** The display "8π²(2χ ± 3τ) = ∫(2|W±|² + s²/24 − |Ric°|²/2)" should read **4π²**; Fubini–Study gives 36π² = 4π²·9. The closed formula on the following line is correct as written.

**2. Offset in the json fields.** The `bA`/`bB` fields in `chiral_flux.json` (CH, H⁴, Euclid) are b_E ∓ S with the unnormalized S. They differ from the note's b_± by ∓6; for example Euclid gives −4 and 8 instead of 2 and 2. `chiral_flux_models.py` uses the normalized S − 6, so `chiral_flux_models.json` matches the note. The derivatives are unaffected, but the json and the note's table disagree as printed.

**3. Corollary X2 remark is wrong.** The statement that X2 is "compatible with orbits that are CH-like at every positive radius" is false. A CH-shaped orbit has b₊ = 2 − 9sinh⁴τ, and X2 requires b₊ ≤ 1 + P̂[0,t]. This forces

  sinh⁴τ ≥ (1 − P̂)/9.

So a subthreshold cell cannot contain a CH-shaped orbit with sinh τ < ((1 − P̂)/9)^{1/4}, which tends to 9^{−1/4} (τ ≈ 0.549) as P̂ → 0. This is a direct-from-bolt analogue of X3's τ < 0.700, which assumes a collapsed starting orbit. The X3 constant itself checks: sinh τ = 3^{−1/4} gives τ = 0.7010.

**4. Hypotheses of the Berger charge, and an anisotropic formula.** The value (−2, 2) needs a' → 0, not merely bounded a'/a·R, together with |b − c| = O(ε). Take fibre a = ε, b = Re^{q/2}, c = Re^{−q/2}. Then γ_b ≈ −2Rq/ε and γ_c ≈ +2Rq/ε, and the CS functions give, to leading order in ε and q:

  b₊ ≈ −2 − R²(q' + 4q/ε)²,  b₋ ≈ 2 + R²(q' − 4q/ε)².

Two consequences follow.

- **Collapsed charges are extremal.** Every collapsed orbit has b₊ ≤ −2 and b₋ ≥ 2, with equality exactly along the decaying and growing eigen-directions q' = ∓4q/ε. These are precisely the rate-4/ε modes of the §3 equation Ric_aa − Ric_bb ≈ −q'' + 16q/ε². X3 therefore holds for every collapsed starting orbit, and sharpens to a decollapse cost of at least β + 2 + R²(q' + 4q/ε)².
- **Positivity in X3 and X4.** The inputs those corollaries use, b₊ ≈ −2 and b₋ ≈ 2 at a collapsed neck, rely on q/ε → 0 there.

## 7. Remaining points

- **Theorem C link.** The relation between (1.1) and Theorem C in §2 is arithmetically correct: 1 vs 2 and 7 vs 2 at the origin, and 12∫W dt = 48 Vol/(8π²) at s = −24. It assumes that the flux terms at the common CH end cancel in the renormalized difference.
- **Cheeger–Tian reading in §4.** The value 𝔰 → 2 is a frame Chern–Simons value relative to the left-invariant trivialization of S³, normalized by 𝔰 = 0 at the round orbit. The gauge-independent content is b₋ − b₊ = 4 on collapsed orbits versus 0 on round orbits. On a closed manifold without a global left-invariant frame, the analogue is an η/CS quantity defined up to framing shifts. Any transfer through F-structures has to fix that integer ambiguity.
- **General-jet expansion of B_B.** The relation B_B = Σq̃²/4 − (Σq̃)²/12 is supported by the structural argument, the CH, Burns, Taub-bolt and Taub-NUT checks, and the symbolic residual. I did not expand it by hand for a general 2-jet.
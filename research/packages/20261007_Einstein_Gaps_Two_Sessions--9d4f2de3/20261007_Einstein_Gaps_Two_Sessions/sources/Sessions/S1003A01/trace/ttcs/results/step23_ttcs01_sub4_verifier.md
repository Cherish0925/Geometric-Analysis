# TTCS Independent Branch Record

```json
{
  "step_id": 23,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md",
    "Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md",
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md",
    "Sessions/S1003A02/workspace/scripts/cr_pinning_check.py",
    "Sessions/S1003A01/workspace/scripts/arb_piece_diagnose.py",
    "Sessions/S1003A01/workspace/data/perp_tail/arb_diag_x0038_X256_p32.json"
  ]
}
```

## Task

Independently verify the mathematical synthesis joining the exact-CH conformal infimum equality, the corrected mu>2 normalized class, the peer CR-pinning identity/Lemma P, and the exact CH exterior response. Determine exactly what is proved, what still depends on decay/noncollapse/shadowing, and whether CR pinning and the exterior null-line response can be interpreted as components of one terminal map without conflating variables or normalizations. Also read the Arb diagnosis and assess the proposed local-basis certification repair.

## Output

# Verification memo: conformal reduction, the μ class, CR pinning, the exterior response, and the Arb box test

## Summary

- **Conformal reduction.** The Step-22 exact-CH reduction is correct as written for every μ in (2, 2+2√3). For μ > 2+2√3 the argument gives only one inequality.
- **CR pinning and the exterior response.** These are the same penalized coordinate, not two complementary ones. Step 19's off-null-line mismatch is exactly the linearized Rossi datum: δ = −2θ_∞^{int}. Step 19's I(ρ) and Step 25's G(T) satisfy I = 4G at x = sinh²T, checked at three radii to about 1%. Lemma P is the nonlinear lower bound whose sharp linear value is δ²/I. A terminal map that adds both penalties would count one cost twice.
- **Arb box test.** The test does not separate certifiable from uncertifiable records. Its data point to a G-channel representation problem rather than generic global Chebyshev growth.

---

## 1. Exact-CH conformal reduction (Step 22; Step 23 §1)

### 1.1 Checked computations

**Normalization.**
- J₆ = P + ¼∫(s+24)², because |(s/4+6)g|² = 4(s/4+6)².
- On normalized CH², the mean curvature of distance spheres is Δr = 2coth 2r + 2coth r = 3coth r + tanh r. Its derivative is −3csch²r + sech²r < 0, so it decreases strictly to 4. Hence H ≥ 4 on the exact end. Volume grows like e^{4r}.

**Barriers.**
- Δ(1−e^{−at}) = a(H−a)e^{−at} and Δ(1+(M−1)e^{−at}) = a(a−H)(M−1)e^{−at}. Both signs are correct.
- The kinks are lattice operations: u₋ = max(0, ·) and u₊ = min(M, ·). Here 0 is a global solution and M is a global supersolution, since F(M) = M(s_g+24M²) ≥ 0. Max and min therefore give weak sub- and supersolutions directly; the jump-sign discussion in Step 22 is consistent with this.

**Decay.**
- With v = u−1, the equation is −6Δv + 48v + 72v² + 24v³ = 0.
- The indicial roots are 2 ± 2√3.
- On distance spheres, angular eigenvalues enter as λ/sinh²r and λ/(sinh²r cosh²r), which tend to 0. So every angular mode has the same leading root. Generically,
  u − 1 ∼ e^{−(2+2√3)r} φ on the conformal-infinity S³.

**Energy identity.** I rederived it from P = ½∫|W|² + (1/12)∫s² − 16π²χ + transgression.
- Pointwise, ŝ²dV̂ = (s−6Δu/u)²dV.
- Substituting s = 6Δu/u − 24u² gives 3(Δu/u)² − 24uΔu, which becomes 24|∇u|² + 3(Δu/u)² minus the flux 24∫_{S_R} u∂_νu.
- ∫_{C_R}|W|² and ∫_{C_R}s² each diverge like e^{4R}. The identity works only because the W-terms cancel pointwise on the same coordinate domain before R → ∞. That is how the proof proceeds; it is worth stating explicitly.
- The flux and transgression differences are linear in v. They vanish iff m > 4, which holds automatically because 2+2√3 ≈ 5.46. So m > 4 is a consequence of the theorem, not a hypothesis.

**Uniqueness.** The max/min argument for w = u₁/u₂ is correct.

**Splicing.** J₆(h_R) − P(h) is bounded by the annulus residual plus the discarded tail, both O(e^{(4−2μ)R}). No linear term appears, because only squared residuals enter. So μ > 2 suffices for splicing.

### 1.2 A structural consequence used implicitly in Step 23

Apply the same identity with ĝ (where ŝ = −24) as the reference metric. For w → 1, with w−1 decaying faster than e^{−4r} so the flux vanishes:

  P(w²ĝ) − P(ĝ) = 24∫|∇log w|²_ĝ dV_ĝ + 3∫(Δ_ĝ w/w)² dV_ĝ ≥ 0.

So ĝ is the unique minimizer of both P and J₆ on its end-normalized conformal class. The "scalar-relaxed" Schur complement in `angular_isotype_conformal.py` approximates the second variation of exactly this minimization. This explains why, at radial orders 4 and 6, the lowest mode already lies in the sampled scalar kernel.

### 1.3 The μ range is overstated

Write C^μ = C^{aCH,μ}_{−24}. The available relations are:
- (a) P ≤ J₆ on exact-ended metrics.
- (b) Normalized images ĝ lie in C^μ only for μ < 2+2√3 (or μ ≤ 2+2√3 given the sharp asymptotic).
- (c) Splicing gives inf_exact J₆ ≤ inf_{C^μ} P for every μ > 2.
- (d) The classes are nested: C^μ ⊂ C^{μ′} for μ > μ′.

For μ ∈ (2, 2+2√3), (a)–(c) close the chain:
  inf_{C^μ} P ≤ inf_exact P ≤ inf_exact J₆ ≤ inf_{C^μ} P.

For μ > 2+2√3, both (c) and (d) point the same way, giving only inf_{C^μ} P ≥ the common value. The normalized images decay exactly at rate 2+2√3 and are not in C^μ. Re-normalizing a spliced metric reproduces the same rate.

Consequently, the sentence in Step 22 §5 ("Inclusion … and splicing therefore show that their P-infima are all the same") and the "for every fixed μ > 2" in Step 22 item 4 and Step 23 §1 are proved only on (2, 2+2√3). Nothing downstream needs more: the r e^{−4r} tail of the Step-19 cells lies in C^μ for every μ < 4.

**What would extend it.** A scalar-preserving localized deformation on CH annuli (Corvino type), which would make ĝ exactly CH outside a compact set while keeping s = −24.
- The algebraic input holds. A static potential f (∇²f − Δf·g − f·Ric = 0 with Ric = −6g) satisfies Δf = 8f and ∇²f = 2fg. This gives R(X,Y)∇f = 2(Xf·Y − Yf·X), so every plane containing ∇f has curvature −2. The plane span(∇f, J∇f) has curvature −4. Hence ∇f = 0 and then f = 0, on every open subset of CH².
- The missing analytic substance is uniform estimates on annuli {R < r < R+1}, whose volume grows like e^{4R}.
- If supplied, this would also show that exact-ended metrics with s ≡ −24 realize the same infimum.

**Symmetric version.** The radial factor u preserves diagonality, and splicing in diagonal coordinates preserves the ansatz. So the diagonal statement used in Step 25 holds on the same μ range.

---

## 2. Lemma P: independent check of the dynamical system

The docstring of `cr_pinning_check.py` states that its check 1 tests the y-system only on CH and H⁴. Both metrics have q = 0, so the q-dependent potentials are never exercised away from q = 0. The Step-23 "independent check" is a rerun of the same script.

I therefore checked Pot_i against the standard diagonal Bianchi-IX formula with dσ_i = 2σ_j∧σ_k:

  Ric_ii = −y_i′ − y_iS + 2[a_i⁴ − (a_j²−a_k²)²]/(a₁a₂a₃)².

The normalization is confirmed by the Berger sphere: fiber value 2ε², horizontal value 4−2ε².

In the variables κ, q, ζ, the identities (a_g²−a_h²)²/(a_ga_h)² = 4sinh²q, 1/a_g² = ζe^{−q}, and a_f² = κ²/ζ² give exactly:
- Pot_f = 2κ² − 8ζ²sinh²q/κ²
- Pot_g = −2κ² + 4ζe^{−q} + 4ζ²sinh2q/κ²
- Pot_h = −2κ² + 4ζe^{q} − 4ζ²sinh2q/κ²

These match the script. The equations κ′, q′, ζ′ also match. So identity (1.1) holds for arbitrary diagonal metrics.

**Lemma P constants.**
- P = 2π²∫W|Ric°|²dt ≥ π²∫W(e_g−e_h)².
- Cauchy–Schwarz gives ¼·√8 = 1/√2, i.e. the bound (P̂/2)^{1/2}(∫dt/W)^{1/2}.
- With ∫_T^∞ 16e^{−4t}/c = 4e^{−4T}/c, this yields (c/2)e^{4T}(…)².
- All constants are correct.

**Drift resolution.** In the standard-end block (ζ ≤ 10⁻², i.e. x ≥ 100), the drift bound is
  sup|G_drift|·ζ²/(2c_B) ≤ 7.354·10⁻⁴/3.997 ≈ 1.8·10⁻⁴.
The block bound uses only y_g + y_h ≥ c_B on the region, not the Einstein flow, so it is valid for controlled trajectories.

---

## 3. CR pinning and the exterior null line: one penalized coordinate

### 3.1 Dictionary

| Quantity | Step 19 | Step 25 |
|---|---|---|
| Radial variable | x | t, with x = sinh²t (dx²/(4x(1+x)) = dt²) |
| Contact slots | a₁ (σ₂), a₃ (σ₁) | g, h |
| Reeb slot | a₂ (σ₃) | f |
| Antisymmetric variable | θ = log(a₁/a₃) | q (sign depends on labelling) |
| Kernel weight | k = (x/(1+x))² | k = tanh⁴t (same) |
| Linear kernel | θ = k⁻¹[C + (c/2)∫₀ˣ f₋²] | {k⁻¹, k⁻¹∫m} (same two-dimensional space) |
| Cost units | 8π² | 8π² |

**Symbol collision.** "G" denotes four different objects:
- the metric lapse in dx²/(4G), which is also the Arb channel `G`;
- G₁₉(x) = ∫_x^∞ f₋² (Step 19);
- G₂₅(T) = ∫_T^∞ M²/w (Step 25);
- the drift polynomial G_drift in ζ²G.

Any unified write-up needs separate names.

### 3.2 δ is the linearized Rossi datum

Continue the entrance data (w₀, Θ) at ρ by the linear kernel. Then v₋/f₋ = c = w₀ and C = kΘ − (w₀/2)∫₀^ρ f₋². Using ∫₀^∞ f₋² = 1/12, the conformal-infinity squashing is

  θ_∞^{int} = C + w₀/24 = k(ρ)Θ + ½w₀G₁₉(ρ) = −δ/2.

This holds exactly. So E_ext = δ²/I = 4(θ_∞^{int})²/I(ρ).

### 3.3 I(ρ) = 4G₂₅(T) at x = sinh²T

Write I = ∫_ρ^∞ (6x²+4x+1)²/(36x³(1+x)⁴) dx.

| T | x = sinh²T | I(ρ) | 4G₂₅(T) from Step 25 |
|---|---|---|---|
| ∞ (asymptotic) | — | ≈ 1/(2ρ²) − 8/(9ρ³) → 8e^{−4T} | 8e^{−4T} (since e^{−4T}/G₂₅ → ½) |
| 2 | 13.15 | ≈ 2.55·10⁻³ | 2.54·10⁻³ (e^{−8}/0.5283 = 6.35·10⁻⁴) |
| 0.5 | 0.2715 | ≈ 0.78 (piecewise power-law quadrature) | 0.776 |

The two notes therefore compute the same exterior cost:

  E_ext(T) = (θ_∞^{int})²/G₂₅(T) → ½e^{4T}(θ_∞^{int})²,

which is the constant of Corollary P1.

### 3.4 Φ̃ is the nonlinear extension of θ_∞^{int}

Linearize at CH: δΦ̃ = θ + θ_t/4 − θ/sinh²t.
- On the constant mode θ = C·coth⁴t, the e^{−2t} terms cancel (8 − 4 − 4 = 0), so δΦ̃ = C + O(e^{−4t}).
- On the mass mode θ ≈ −4c·e^{−4t}, θ + θ_t/4 cancels, leaving a higher-order remainder.
- In t, Step 19's θ_∞^{int} = kθ + G₁₉(kθ)_x/f₋² also reduces at leading order to θ + θ_t/4.

The exact linear statement follows from (1.1), because θ_∞ is conserved along the linear kernel and δΦ̃ moves only by the drift:

  δΦ̃(T) = θ_∞^{int}(T) − ∫_T^∞ δ(ζ²G_drift) dt.

### 3.5 Consequences

**Correction to Step 23 §3.** The text says the exterior penalty and CR pinning "complement rather than duplicate." In the linear regime they are the same observable. The data at radius T have two antisymmetric coordinates:
- the penalized Rossi coordinate θ_∞^{int}, whose nonlinear form is Φ̃ plus drift;
- the mass-mode amplitude c, which costs nothing (the null line).

The symmetric sector decouples at quadratic order (H₁ = H₃ = 0 on CH). The consistent terminal map is

  (state at T) ↦ (θ_∞^{int}, c, symmetric data), with cost (θ_∞^{int})²/G₂₅(T) + cubic terms.

For large deviations, Lemma P supplies the nonlinear lower bound, with c_W/2 in place of 1/G₂₅. Keeping the port (w₀, Θ) as state is fine; attaching separate penalties to the port mismatch and to Φ̃ would count one cost twice.

**What each tool actually sees.**
- *Step-19 cells.* For x₀ = .038, δ = −7.7·10⁻⁴ at ρ = 10, so θ_∞^{int} ≈ 3.85·10⁻⁴. On the optimal exterior θ_∞^{int}(x) ∝ I(x), giving about 4.5·10⁻⁶ at x = 100. That is far below the block drift 1.8·10⁻⁴, and at ρ = 10 the block does not apply (ζ = 0.1). Lemma P therefore carries no information about the actual stationary cells.
- *Theorem E.* For O(1) Rossi deformations, e.g. log 2.19 ≈ 0.784, Lemma P is decisive.
- *Common order.* The far-field charge sits at the same e^{−4T} order as the drift. A refined drift bound Lipschitz in the distance to the CH trajectory (G_drift vanishes on that trajectory) would let Lemma P resolve the charge.

**λ as the costate of the Rossi coordinate.**
- λ = −δ/I = 2θ_∞^{int}/I ≈ ¼e^{4T}θ_∞^{int}, i.e. 0.1827 from 3.85·10⁻⁴ and I(10).
- The Cauchy–Schwarz equality case of Lemma P gives a far field with e_g − e_h ∝ 1/W.
- Using Φ̃ ≈ 4λe^{−4T}, this predicts W(Ric°_gg − Ric°_hh) → 4λ ≈ 0.73 (sign by convention) on [4, X/8]. The drift is O(e^{−8t}) and negligible there.
- This is a gauge-invariant, nonlinear check of the identification on the actual cells.

**Log cancellation.** The tail θ ∼ A t e^{−4t} gives Φ̃ ∼ (A/4)e^{−4t} with no logarithm. This is consistent with Φ̃ ∝ I(x) and with membership in C^μ for μ < 4.

**Reach.** Φ̃ and Lemma P are defined only in the diagonal class. The j = 1 angular problem needs a nondiagonal Rossi functional (a CR-deformation tensor at infinity) obeying an analogue of (1.1). That functional does not yet exist.

---

## 4. Status

**Proved** (modulo standard elliptic theory):
- Step 22 items 1–3 and uniqueness.
- Equality of the exact-ended P- and J₆-infima.
- Equality with inf_{C^μ} P for μ ∈ (2, 2+2√3).
- The symmetric and diagonal versions on the same μ range.
- Conformal-class minimality of ĝ.
- Identity (1.1), with independently checked potentials.
- Lemma P, and Corollary P1 given the block hypothesis.
- The closed-form linear exterior response.
- The identity δ = −2θ_∞^{int}.

**Strongly supported, not yet written as a theorem:**
- I(sinh²T) = 4G₂₅(T) identically. A symbolic change of variables would close it.

**Conditional:**
- Attainment of p^{diag}_{1,0}.
- Theorem D, which needs: bolt bounds 0 < c ≤ b_j ≤ C; orbit noncollapse; tails in the block uniformly in j; the truncation lemma (rate-2 matching and forced response); the shadowing lemma; and a validated face phase portrait (currently numerical).
- The terminal penalty for traces far from CH at ρ (Step 19 §5.3); Lemma P covers only traces in the ACH block.
- Equality for μ > 2+2√3, via scalar-preserving annular gluing.

**Not touched by these results:** collapsed connectors, large bolts, non-Euclidean necks, and ρ_∞(b) ≠ 1 along the separatrix family.

---

## 5. Arb box test (`arb_diag_x0038_X256_p32.json`)

### 5.1 What the data show

The test does not discriminate. Step 23 states that the certifiable control (x₀ = .03, X = 64, d16) also does not close at radius 1/64; that file was not supplied. If so, the test cannot explain why the long cell does not certify.

The supplied file contains more structure than the "global high-degree Chebyshev" explanation accounts for:

- **Channel disparity.** At k = 11, FH ∈ [0.891, 0.978] while G ∈ [−23, 27] and GH ∈ [−15, 20], with G ≈ 1.7 there. At k = 29, FH ∈ [0.61, 1.46] while G = ±3.9·10⁹. G and GH straddle zero in all 32 boxes, whereas FH is tight and h₁ is positive on the middle range.
  - If FH and G use comparable-degree series on the same box, the amplification is specific to the G representation. Possible causes are cancelling or large coefficients from the overwritten cG[0] and bolt constraint, or an exponentiated series. This is consistent with the flat Hessian directions (1.9·10⁻⁶).
  - The per-channel quantities that settle this are Σ|c_n| and Σn²|c_n|. The latter controls the second derivatives that curvature needs; the Markov factor is 576 at degree 24 versus 256 at degree 16.
- **Near-bolt signature.** For k = 1…6, log₁₀ of the FH width runs 305, 108, 38, 13, 4.7, 1.7, a ratio of about 2.8–2.9 per box. That is ∝ e^{−33u}, i.e. ∝ x^{−3.8} with ℓ = log(256/.038) = 8.82. GH behaves similarly. These boxes cover the physically tiny range x ∈ [0.038, 0.09]. The blow-up comes from the bolt-adapted formula (a negative power or a removable zero inside an exponential or quotient), not from interval length.
- **Far field.** The residual z ∼ x^{−5/2}, about 10⁻⁶ at x = 256, is a cancellation between O(1) curvature components. For the upper bound ∫(|z|+r)²W with W ∼ x² to stay within 10⁻⁷ up to X = 256, the residual ball radius must be about 10⁻⁷. Interval dependency on separate O(1) terms will not reach this regardless of precision. This is the same cancellation that shows up in float at X = 1024.

### 5.2 Assessment of the local-basis repair

The repair is sound in direction but needs three specific components:

1. **Exact re-expansion.** Each polynomial channel can be re-expanded on subintervals as an exact centered Taylor polynomial (rational or ball coefficients, no remainder). This removes Clenshaw wrapping; enclosure width becomes about |p′(c)|r + O(r²). Rigorous remainders are needed only for the transcendental compositions (exp, log, sqrt, e^{ℓu}), via Taylor-model arithmetic.
2. **Bolt factor.** The bolt zero must be divided out at the coefficient level, or handled in a √(x−x₀)-type variable. Finer partition alone does not cure the k ≤ 7 signature.
3. **Background subtraction in the far field.** Write the channels as CH × (1 + perturbation), so the residual is computed as linear plus quadratic in small quantities. Beyond ρ, the tail can be bounded by the explicit Step-19 quadratic form δ²/I = (θ_∞^{int})²/G₂₅ plus a rigorous cubic remainder. This uses the terminal map of §3 as part of the certificate.

Real-interval Taylor-model quadrature (exact polynomial integral plus remainder × length) is an alternative to complex-ellipse quadrature. It needs only real positivity of F, G, and e^w.

Before building, one inexpensive measurement would tell which mechanism dominates: the largest box radius r*(u) at which each channel is finite and separated from zero, for the certified control and the long record side by side. The certified x₀ = .03, X = 128 value is unaffected by any of this.

---

## 6. Interpreting the j = 1 Ritz sequence

J₆ is diffeomorphism-invariant. For compactly supported j = 1 fields X:
- dJ(L_Xg) = 0 by isotype orthogonality;
- Hess(L_Xg, L_Xg) = −dJ(L_XL_Xg), which vanishes at exact criticality.

So over a complete basis the j = 1 Rayleigh infimum tends to the gauge value 0. The sequence 0.896 → 0.178 → 0.121 is consistent with convergence toward gauge directions; it is not evidence of a positive spectral bottom. Any value away from zero there arises from residual j = 0 non-criticality of the truncated cell.

The meaningful statement is positivity on the quotient by {L_Xg}. Two exact relations can be measured on the stored lowest modes:
- their overlap with exact L_Xg;
- the Ward residual Hess(L_Xg, ·).
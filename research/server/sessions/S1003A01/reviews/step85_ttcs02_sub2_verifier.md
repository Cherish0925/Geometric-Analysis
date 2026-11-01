# TTCS Independent Branch Record

```json
{
  "step_id": 85,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step85_coupled_center_theorem_neck_trace_and_endpoint_reduction.md",
    "Sessions/S1003A01/workspace/data/step85/center_algebra.json",
    "Sessions/S1003A01/workspace/scripts/step85_center_algebra.py",
    "Knowledge/objects/papers/2603.09028-Einstein-deformations-of-Kähler-Einstein-metrics--062c0a015de6--2a0f3c1e029d/object.md"
  ]
}
```

## Task

Check, line by line, the mathematics of the Step-85 note on closed negative Goldberg near Kahler-Einstein (KE) metrics and A1 orbifolds. Focus on: (1) Proposition 85.1 (exact identity |a omega + beta|^2 = 2a^2+|beta|^2 for beta in Re H^{2,0}; constant |theta| forces K trivial; orbifold validity; quadratic estimate). (2) Theorem 85.A: does Nagy's Theorem 1.6 normal form apply to formal second-order Einstein jets; correctness of the pointwise algebra A1-A5 in the script (conventions g^{-1}g_t = 1 + tH1 + t^2/2 H2, Hodge star, ASD projection); the holomorphic-transport construction of beta' (J' = J H1, g_s = omega(., J_s .), first-order integrability from dbar H1 = 0, ddbar-lemma step, why <omega,beta'>=0 pointwise); whether admissible length corrections compatible with the other second-order equations are exactly the constants; any missing second-order term. (3) Theorem 85.B: indicial classification of closed self-dual forms on flat R^4 minus 0 (degrees >=0 and <=-4; -2,-3 empty; no logs), Gamma-parity; neck argument that the constant mode drifts only by the integrated metric error; whether the metric-error hypothesis is plausibly supplied by Ozuch's weighted closeness; Liouville statements; uniform L^infty bound; b+(M)=b+(V). (4) 85.D: at a KE point R^+ = (s/4) I(x)I, Biquard/Ozuch first obstruction forces the EH period direction into I-perp; is the conclusion (bubble's parallel form orthogonal to zeta, smoothing rather than resolution, vanishing cycle asymptotically Lagrangian) correct? EH potential expansion and anti-self-duality of i ddbar(1/r^2). (5) T_+(M)=T_+(V) for EH with W+=0 and D(g)=(S_hat^2(g)-S_hat^2(V))/16. (6) Conditional Theorem 85.M: is hypothesis (b) correctly scaled, does the mean-value argument work, is the Kahler smoothing locus of codimension one. Give corrections with explicit formulas and state which statements are fully proved, which need repair, and any counterexample.

## Output

# Verification memo: Step 85 (Goldberg near KE metrics and A1 orbifolds, E<0)

I checked Step 85 line by line against `step85_center_algebra.py`, `center_algebra.json` and the Nagy source (arXiv 2603.09028). Notation follows the note: |ω|² = ½ω_{ab}ω^{ab}, so |ω|² = 2, and g^{-1}g_t = 1 + tH₁ + (t²/2)H₂.

**Summary of status**

| Item | Status |
|---|---|
| Lemma 85.0, Prop 85.1 | Correct; can be strengthened |
| Theorem 85.A | Correct; needs one added volume step and an orbifold transfer remark |
| Theorem 85.B | (ii) correct; the neck step needs a replacement proof (supplied below) and two precisions in (H) |
| 85.C | Correct; follows more directly from Prop 85.1 |
| 85.D | Correct; one normalization slip |
| (5.1) | Correct |
| 85.M | Mean-value step and codimension count correct; hypothesis (b) has a scaling inconsistency |

No counterexample to any stated result was found. The one statement that is false as literally written is 85.B(iii) on an untruncated neck (§3.4).

---

## 1. Lemma 85.0 and Proposition 85.1

**Lemma 85.0.** Correct.
- A self-dual (SD) form with |ω|² = 2 in this normalization is exactly g(J·,·) for a g-orthogonal J of the given orientation.
- Closed SD forms are coclosed, hence harmonic.
- Continuity of λ(g) uses that dim H⁺_g = b⁺ is locally constant, which holds.

**Pointwise identity.** On a Kähler surface, Λ⁺ = ℝω ⊕ Re Λ^{2,0} orthogonally, and H⁺ = ℝω ⊕ Re H^{2,0}, so b⁺ = 1 + 2p_g. Hence |aω + β|² = 2a² + |β|² exactly.

**Normalization check.** For θ = dz₁∧dz₂ one has |Re θ|² = 2 and Hermitian |θ|² = 4, so |β|² = ½|θ|² is consistent.

**Triviality of K.** The argument (constant |θ| ⇒ K trivial ⇒ c₁ = 0, contradiction) is correct on manifolds and on orbifolds via K_V^orb. A pointwise argument is stronger and simpler:
- Where θ ≠ 0, i∂∂̄ log|θ|²_g = ρ_g = Eω. This is the Ricci form of the induced metric on K⁻¹, up to a sign convention.
- So |θ| cannot be constant on any open set where θ ≠ 0 when E ≠ 0.
- Consequently Q₀(β) = 0 forces β = 0 by a local argument. This needs neither compactness nor the orbifold canonical bundle, and it holds equally at an A1 point (where θ(p) ≠ 0 is allowed, as the note remarks).

**Estimate (85.1).** Q₀ is continuous and 2-homogeneous on a finite-dimensional space and vanishes only at 0. The minimum on the L²-unit sphere is therefore positive. **Fully proved.**

**Simplification of 85.C.** The limit form ω_∞ on V∖p is closed, SD and of constant length, and it extends over p because it is bounded. Prop 85.1 then gives ω_∞ = ±ω_V directly. Neither T_AK → 0 nor the holonomy argument is needed.

---

## 2. Theorem 85.A

### 2.1 Applying Nagy's Theorem 1.6 to formal 2-jets

I checked the logical chain in the source.
- Prop 3.8 (gauge) uses only Taylor coefficients.
- Thm 3.9 uses the first- and second-order Einstein equations together with Lemma 3.7 (volume).
- Prop 4.20 and Thm 4.21 use only Hodge theory of Δ_E and of Δ − 2E on functions.

So the normal form is a statement about second-order jets with Ric(g_t) − Eg_t = O(t³). The jet should be stated in this form, not with the DeTurck term δ*B.

**Missing step: volume.** Nagy assumes vol(g_t) is constant, and his gauge group consists of volume-preserving diffeomorphisms. For fixed E ≠ 0 this holds to the needed order:
- Einstein metrics with constant E are critical points of 𝒮_E(g) = ∫(s_g − 2E) dv_g.
- Along the jet, d/dt 𝒮_E(g_t) = O(t³). Also s_t = 4E + O(t³).
- Hence 2E·Vol(g_t) = 𝒮_E(g) + O(t³), so Vol(g_t) = Vol(g) + O(t³).
- Moser's lemma, applied to the rescaled volume forms, then puts the jet in Nagy's class to O(t³).

This step should be inserted. It also explains why no t²·g correction appears.

**Orbifolds.** Koiso's identification 𝓔 = {anti-J, ∂̄-closed, divergence-free} and Nagy's computation are proved for manifolds. Transfer to orbifolds via invariant local lifts is routine but not in the source, and should be stated as such.

### 2.2 Script checks A1–A5

`hodge` implements (*F)_{ab} = ½√|G| ε_{abcd}F^{cd} with F^{cd} = (G⁻¹FG⁻ᵀ)^{cd}, and `norm2` implements |F|² = ½F_{ab}F_{cd}g^{ac}g^{bd}. Both are correct.

- **A1.** ω_{ab}ω_c{}^b = g_{ac} exactly. So d|ω|²_{g+tH} = −tr H for every symmetric H, not only for J-types.
- **A2.** Write ω = gJ and b = gK with JK = −KJ. Then JK is skew, so its contraction with symmetric H vanishes.
- **A3, A4.** These follow from representation theory:
  - Sym₀² ≅ Λ⁺⊗Λ⁻ (dimension 9) splits as ω⊗Λ⁻ (the J-invariant trace-free part, dimension 3) ⊕ ReΛ^{2,0}⊗Λ⁻ (the anti-J part, dimension 6).
  - The ASD variation of ω sees only the first summand.
  - The ASD variation of b ∈ ReΛ^{2,0} sees the second summand, which is generically nonzero.
- **A5.** This has a structural explanation that should replace the random-matrix check as the proof.
  - If HJ = −JH, then A = e^{tH} satisfies A⁻¹JA⁻¹J = −1 exactly. So g·e^{tH₁} is exactly ω-compatible.
  - Adding (t²/2)K with K anti-J preserves compatibility to O(t⁴).
  - The two expressions differ from 1 + tH₁ + (t²/2)(H₁² + K) only at O(t³).
  - **Conclusion:** Nagy's normal form says that (g_t, ω) is ω-compatible, hence almost-Kähler, through second order. The control perturbation diag(1,1,−1,−1) commutes with J and is trace-free, so the control in the script is the right one.

### 2.3 Holomorphic transport

I verified every step.

1. **Compatibility.** ω(X, J'Y) = g(JX, JH₁Y) = g(X, H₁Y), so ω(·,J_s·) = g + sH₁ exactly.
2. **Almost complex to first order.** JJ' + J'J = −H₁ + JH₁J = 0.
3. **Integrability to first order.** By Nagy Rem. 4.9, J_{sh} = J − 2sJh + O(s²). Here J' = JH₁ corresponds to h = −H₁/2, so first-order integrability is equivalent to ∂̄H₁ = 0.
4. **Hermitian and Kähler to first order.** g_s(J_s·,J_s·) = g_s + O(s²), and the fundamental form is ω, which is closed.
5. **Closedness of θ'.** One needs (θ')^{0,2} = 0 at first order and (θ')^{1,1} = ι_φθ.
   - ∂̄(ι_φθ) = 0, because contraction with holomorphic θ is a holomorphic bundle map.
   - The (2,1)-form ∂(ι_φθ) is ∂-closed, ∂̄-closed and ∂-exact. The ∂∂̄-lemma therefore gives ∂(ι_φθ) = ∂∂̄ξ with ξ of type (1,0).
   - Setting (θ')^{2,0} = ∂ξ gives ∂(ι_φθ) + ∂̄∂ξ = 0.
6. **Orthogonality ⟨ω,β'⟩ ≡ 0.** Differentiate ⟨ω, β_s⟩_{g_s} = 0. The metric-derivative term is the A2 contraction, which vanishes for every H.

The transport also answers an existence question the note leaves implicit. The ASD part of a closed form must be L²-orthogonal to H⁻, and the transport produces a closed solution of (2.1) directly.

### 2.4 Completeness of the second-order list

**SD equation.** The t² coefficient of P⁻_{g_t}ω_t is

 [P⁻_{g_t}ω]_{t²} + DP⁻[H₁]β₁ + ½β₂⁻,

and the first term vanishes by A5. Hence β₂ ∈ 2β' + H⁺_g.

**Length equation.** The t² coefficient of N(g_t, ω_t) is

 [N(g_t, ω)]_{t²} + 2[B_{g_t}(ω,β₁)]_{t} + ⟨ω,β₂⟩ + |β₁|²,

whose first two terms vanish by A5 and A2.

**Available corrections.** All admissible corrections to the length are constants:
- γ ∈ H⁺ contributes the constant 2c_γ.
- Additions to H₂ from 𝓔 are anti-J and trace-free, so they contribute nothing by A1 and A3.
- Simultaneous gauge contributes L_X|ω|² = 0.
- Scaling is excluded by fixed E.

**Conclusion.** |β₁|² = −2c_γ must be constant, so β₁ = 0. No second-order term is missing.

**One precision.** The remark about β ~ t^{3/2} is formal. If the first Re H^{2,0} component of ω_t − ω appears at order k, the order-2k length equation contains |β_k|² together with order-2k metric-sector terms that need not be constant. So 85.A excludes tangent rotation, not rotation at higher order.

**Status.** Fully proved for manifolds once the volume step is added. On orbifolds it is proved modulo the routine transfer of Koiso and Nagy.

---

## 3. Theorem 85.B

### 3.1 Indicial classification

**Reduction to harmonic coefficients.** Closed and SD imply harmonic, so in a parallel frame the coefficients are harmonic.

**No logarithms; modes separate.** Harmonic functions on annuli in ℝ⁴ are Σ(a r^ℓ + b r^{−2−ℓ})Y_ℓ. The two exponents never coincide, so no logarithmic terms occur. Closedness preserves homogeneity. A given degree d is reached by the growing family (ℓ = d ≥ 0) or by the decaying family (ℓ = −2−d, so d ≤ −2), never by both. So closedness does not mix the families.

**Gap.** Degree −1 is absent automatically. Degrees −2 and −3 are empty by exact rank computation in the script.

**What is proved for d ≤ −4.** The statement "exactly d ≥ 0 and d ≤ −4" is verified only for |d| ≤ 5. The argument uses only the gap (−4, 0) and the fact that degree 0 consists of constants, both of which are proved.

**Group action.** Γ ⊂ SU(2) acts trivially on Λ⁺ in the complex orientation. A nontrivial Γ acts freely on S³, so there are no invariant linear functions and degree 1 is killed. For A1, −1 kills all odd degrees. The A1 indicial set {…, −6, −4} ∪ {0} ∪ {2, 4, …} is correct.

### 3.2 Neck drift: the stated argument is incomplete, and a corrected proof

The note argues that "nonconstant modes have sphere average zero". For a first-order system this does not isolate the constant mode:
- dr∧ω_i has ℓ = 1 coefficients in a parallel frame.
- The radial variation of the ℓ = 0 part therefore couples to ℓ = 2 modes.

**Corrected proof: an exact conservation law.** Define

 θ_i = r^{−4} ι_xω_i (homogeneous of degree −3).

Then

 dθ_i = 2r^{−4}ω_i − 4r^{−6} x^♭∧ι_xω_i.

Since the SD part of x^♭∧ι_xF equals (r²/2)F for SD F, the 2-form dθ_i is flat-ASD.

On the sphere one has (ω_j∧ι_xω_i)|_{S_r} = ±δ_{ij} r vol_{S_r}. Hence, for a closed form ω with flat-SD coefficients f_j,

 ∫_{S_r} ω∧θ_i = ±2π²·⨍_{S_r} f_i + ∫_{S_r} ω^{−,0}∧θ_i,

 d(ω∧θ_i) = ω∧dθ_i = ω^{−,0}∧dθ_i.

Here ω^{−,0}, the flat-ASD part, satisfies |ω^{−,0}| ≤ C|e||ω| when ω is g_n-SD. Therefore

 |⨍_{S_{r₂}} f_i − ⨍_{S_{r₁}} f_i| ≤ C sup|ω| ( ∫_{r₁}^{r₂} sup_{S_r}|e| dr/r + sup_{r₁,r₂}|e| ).

This is exactly the stated drift bound. It requires only C⁰ control of the error e, not ∇e, which makes (H) easier to supply. The dual element θ_i is the degree −3 = −(n−1) − 0 adjoint solution associated with the root 0.

Uniform closeness ω ≈ c on the neck interior then follows from the decay of the remaining modes, by weighted elliptic estimates with the rates (r/ρ₂)^{1 or 2} and (ρ₁/r)⁴.

### 3.3 Hypothesis (H) and Ozuch's closeness

**The error on the full neck does not tend to zero.** On A(ε, 1) the naive desingularization deviates from flat by roughly r² + ε⁴r^{−4}. Then ∫_ε^1 (r² + ε⁴r^{−4}) dr/r stays bounded but does not tend to 0.

**Fix.** The neck must be A(Rε, ρ) with R → ∞ and ρ → 0 diagonally. Then the integral is ≲ ρ² + R^{−4}, and the ends are handled by smooth convergence.

**Weight direction still to be checked.** The perturbation g_n − g^D enters through Ozuch's C^{2,α}_{β,*} norm. The drift integral converges only if that norm controls |g − g^D| ≤ δ_n r_D^{+β} on the neck. A weight r_D^{−β} would give δ_n ε^{−β}/β, which needs separate control. I could not verify the sign from the supplied material (Ozuch around line 420).

### 3.4 Remaining parts of 85.B

**Liouville.** W⁺ = 0 and s = 0 make Λ⁺N flat. Bounded harmonic coefficients on a complete manifold with Ric ≥ 0 are constant (Yau). A bounded closed SD form on the whole cone is constant by the two-sided indicial argument. Both statements are correct.

**(i) Uniform L^∞ bound.** The argument is not circular as long as (iii) is applied to sup-normalized forms. The constant propagates to the region r ~ ρ, which has volume of order ρ⁴ (fixed). Correct.

**(ii) b⁺(M) = b⁺(V).** This is purely topological:
- H¹ and H² of S³/Γ vanish over ℝ, so Mayer–Vietoris gives H²(M) = H²(V) ⊕ H²_c(N), with the intersection forms adding.
- For an orientation-matched ALE filling, H²_c is spanned by (−2)-curves, so b⁺(N) = 0.

Convergence of the spaces H⁺ follows from (i), from the vanishing volume of the cores (so no L² mass is lost), and from equality of dimensions.

**(iii) as written.** "ω_n = c_n + o(1) uniformly on each neck" is false if the neck reaches r ~ 1, because there ω_V(x) − ω_V(p) = O(r). It holds on the truncated neck of §3.3.

**Cor 85.B′.** The proof never uses that g_n is Kähler. It applies to the continued subspace of Re H^{2,0}_orb(V) for any g_n satisfying (H). This is exactly what 85.E uses.

---

## 4. 85.D and the Eguchi–Hanson tail

**Curvature at a KE point.** On a Kähler surface W⁺ has eigenvalues s/6, −s/12, −s/12, with the first along I. Hence R⁺ = W⁺ + (s/12)·Id = (s/4) I⊗I and ker R⁺(p) = I^⊥, which is two-dimensional. Correct.

**Geometric conclusion.** In the hyperkähler 2-sphere of EH, the period of ω_u on the exceptional sphere S is proportional to ⟨u, ζ⟩. Combining:
- the obstruction gives ζ̂ → I^⊥;
- 85.C gives a bubble form along I;

therefore ω_b ⊥ ζ. So S is ω_b-Lagrangian, and EH in the complex structure I is the affine smoothing {xy = z² + c}, not the resolution. This is consistent with Kähler smoothings having 2 real parameters, which equals dim ker R⁺. Correct, given Ozuch's first obstruction as quoted.

**Normalization slip.** The area of S is of order ε² ~ |ζ|. The correct statement is

 ∫_S ω_n = [ω_n]·[S] = o(|ζ_n|), not "o(t_n)".

**Expansion of φ.** With x = a²/u:
- √(u²+a⁴) = u + a⁴/(2u) + …
- log(1 + x + x²/2 + …) = x − x³/6 + …
- Hence φ = u − a⁴/(2u) + O(u^{−3}), agreeing with the script.

**ASD tail.** r^{−2} is harmonic on ℝ⁴, so i∂∂̄(r^{−2}) is primitive of type (1,1), hence flat-ASD. The script confirms this in the convention dz = dx + i dy.

**No tail for dz₁∧dz₂.** dz₁∧dz₂ is exactly the holomorphic symplectic form in the coordinates where the potential is u-radial, so it has no tail. Correct.

---

## 5. (5.1) and topology

For Einstein metrics,

 4π²(2χ+3τ) = ∫(2|W⁺|² + s²/24).

Hence

 D := ∫(s²/24 − |W⁺|²) = 𝒮/16 − 2π²T₊, with 𝒮 = ∫s² dv.

For a KE orbifold, |W⁺|² = s²/24 pointwise, so 𝒮(V) = 32π²T₊(V).

**Bubble charge.** χ(M) = χ_orb(V) + χ(N) − 1/|Γ|, and τ(M) = τ_orb(V) + τ(N) + η(S³/Γ), with the sign fixed by orientation. For EH: χ = 2, τ = −1, η(ℝP³) = 0. The bubble charge is

 2(2 − ½) + 3(−1) = 0.

In general this charge equals (1/4π²)∫_N(2|W⁺|² + s²/24) = 0.

**Result.** D(g) = (𝒮(g) − 𝒮(V))/16 for every Einstein g on M. **Proved.**

**Sign of D.** LeBrun's estimate 𝒮 ≥ 32π²T₊ for Einstein metrics with a monopole class gives D ≥ 0. Taubes supplies the monopole class for symplectic M with b⁺ ≥ 2, but only when the symplectic orientation is the one in which 2χ+3τ is computed.

---

## 6. Conditional Theorem 85.M

### 6.1 Scaling of hypothesis (b)

The note simultaneously:
- quotes Ozuch's value errors as O(|ζ|^{1+δ}), which presupposes λ_I ≈ c₀(s/4)ζ_I, so that λ ~ |ζ|·ζ̂_I;
- writes the derivative in (b) as c₀s/(4|ζ|), which presupposes λ_I ≈ c₀(s/4)ζ̂_I, of size O(1).

These two normalizations are incompatible. In the normalization matching the quoted errors, (b) should read

 |∂_{ζ_I}λ_I − c₀s/4| ≤ o(1),

uniformly on the cone {|ζ_I| ≤ η|ζ|}. Equivalently, the condition is that the relative error of ∂_{ζ_I}λ_I tends to 0.

Note also that ∂_{ζ_I}(ζ_I/|ζ|) = (1 − ζ̂_I²)/|ζ|, so the |ζ|^{−1} form is correct only on that cone.

### 6.2 Mean-value step

Once the normalization is fixed, the mean-value step works:
- The first obstruction gives ζ̂_I → 0 for all Einstein metrics that are GH-close to V. On 𝒦 one also has κ = o(|ζ|).
- So the segment from κ to ζ_I lies in the cone, with |ζ| ≈ |ζ_⊥| along it.
- Then λ_I = (ζ_I − κ)(c₀s/4 + o(1)), so zeros of λ_I lie on 𝒦.

**Implicit input.** Ozuch's parametrization must be injective up to gauge, so that each Einstein metric corresponds to one parameter point. This should be stated.

### 6.3 Codimension of the Kähler locus

The parameter space is P = ℝ³_ζ × 𝓔(V), of real dimension 3 + 2h¹(T_V).

Under (a), the KE smoothings (which exist by Aubin–Yau, since K stays ample) have real dimension 2 + 2h¹. Here ζ_⊥ is linear in the local smoothing parameter c, so the Kähler locus has codimension one.

**Exact zero of the period on Kähler smoothings.** For Kähler smoothings,

 ∫_S ω_KE = (2π/|E|)·c₁·[S] = 0,

because K·S = 0 for a vanishing (−2)-cycle. So the I-period of the Kähler locus is exactly zero.

**A possible normal coordinate (suggestion, not proved in the note).** Replace ζ_I by the topological pairing [ω̂_n]·[S], where ω̂_n is the continuation of ω_V from 85.B(ii). This is defined for every Einstein metric on M. It vanishes exactly on Kähler smoothings, and by 85.D it equals ζ_I(1 + o(1)) on the cone. If ∂_{ζ_I}λ_I could be compared with the derivative in this coordinate, the C¹ estimate in (b) would become a statement about one cohomological pairing.

**Failure of (a).** The localization of a possible strict branch to configurations violating (a) is correctly formulated. No example of a KE orbifold with E<0 for which (a) fails is supplied, so this remains a search target, not a construction.

---

## 7. Status of each statement

**Fully proved:**
- Lemma 85.0.
- Prop 85.1, which can be strengthened to the pointwise version.
- Theorem 85.A on manifolds, once the volume step of §2.1 is added.
- 85.B(ii).
- (5.1) and T₊(M) = T₊(V).
- The EH computations B1 and B2.
- 85.C, via Prop 85.1.

**Correct, but needing the stated repairs:**
- 85.B(i) and (iii): replace the neck argument by the θ_i conservation law, truncate the neck to A(Rε, ρ), and check the direction of Ozuch's weight.
- Cor 85.B′: remove the Kähler hypothesis.
- 85.D: write o(|ζ|) for the period.
- 85.A on orbifolds: transfer of Koiso and Nagy.

**Conditional, with a scaling correction needed:**
- 85.M: hypothesis (b) must be restated as in §6.1.
- 85.E: the order comparison is formal; only the stated inequality itself is rigorous.
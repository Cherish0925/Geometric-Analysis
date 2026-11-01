# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/scripts/step80_regularized_model_fast.py",
    "Sessions/S1003A01/workspace/scripts/step80_zero_models.py",
    "Sessions/S1003A01/workspace/data/step80/regularized_model_fast.json",
    "Sessions/S1003A01/workspace/data/step80/zero_model_regularization.json",
    "Sessions/S1003A01/workspace/data/step59/chiral_exact.json"
  ]
}
```

## Task

Independently verify the mathematics in the new Step-80 note. Focus on: (i) signs and integration by parts in the regularized scalar identity (80.R) from the displayed Δq equation; (ii) signs in the equally regularized Kodaira identity (80.K); (iii) the local distributional limits for q=c rho^{2m} at an isolated four-dimensional zero versus a smooth codimension-two stratum, including constants 4π²m R² and 4πm; (iv) the exact Bianchi-VIII rational formulas and asymptotic/scaling interpretation, including whether the indefinite ∂v term really cancels half of 24|eta|² at leading order; (v) any overstatement in the conclusions about what uniform estimate remains. Return corrected formulas and a direct scientific assessment. Do not rely on numerical output as proof beyond its scope.

## Output

# Verification memo: Step 80, regularized torsion identity, zero residues, and the Bianchi‑VIII model

## Summary

- **Exact identities.** (80.R) and (80.K) are correct, signs included.
- **Bianchi‑VIII rationals.** These are internally consistent. The cross term is exactly −½·24|η|² at leading order.
- **Three statements need correcting:**
  - Isolated zeros of every order, and zero curves, carry no residue. Only two‑dimensional strata do, so the withdrawal of the Step‑79 "zero curves have no residue" statement was itself mistaken.
  - The large residuals in the ε‑sweep are the truncated end flux at u_max = 32, not cancellation error.
  - The normalized torsion α̂ cannot wind around a codimension‑two stratum.
- **Where the real obstacle sits.** The model's ε‑nonuniformity lives at its ACH end, not at a torsion zero. The quantity still missing is a global inequality that uses finite volume, not ε‑uniformity near Z.

## (i) The scalar identity (80.R)

**Δq equation.** Step 79 gives Δq = 8trV² − 24|η|² − (3s/2)q − (9/4)q² + 16X with X = −2Im⟨α,K∂_Dv⟩, so 16X = −32Im⟨α,K∂_Dv⟩.

With s<0 this is exactly (80.1): Δq = −D + (3|s|/2)q − (9/4)q².

**Integration by parts.** With Δ = div grad,
- Δlog(q+ε) = Δq/(q+ε) − |dq|²/(q+ε)², and
- ∫_M Δlog(q+ε) = 0 because log(q+ε) is smooth.

Substituting (80.1) gives (80.R) with the stated signs. Only smoothness of q and D is used, and D is smooth because α, v and η are smooth gauge‑covariant quantities.

**What the ε‑family actually says.** The gradient term increases monotonically as ε↓0. By monotone convergence,
\[
\lim_{\varepsilon\to0}\int\frac{D}{q+\varepsilon}=\frac{3|s|}{2}V-\frac94Q-\int_{M\setminus Z}|d\log q|^2\in[-\infty,\infty).
\]
So the ε‑family is equivalent to a dichotomy:
- either |d log q| ∈ L² and ∫D/(q+ε) has a finite limit;
- or both diverge together (this is what happens at two‑dimensional strata).

The ε‑limit of the combined left side never sees a residue; the residue appears only when it is compared with the pointwise integrand on M∖Z (see (iii)).

**New pointwise fact at torsion zeros.** On Z = {q=0} we have α = 0, so the cross term vanishes and D|_Z = 24|η|² − 8trV². Because q has a minimum on Z, Δq ≥ 0 there, and (80.1) gives
\[
\operatorname{tr}V^2-3|\eta|^2=\tfrac18\Delta q\ \ge 0,\qquad\text{i.e. }|v|^2\ge\tfrac32|\eta|^2\ \text{on }Z.
\]
The inequality is strict at nondegenerate zeros. There W⁺ cannot be of Kähler type: v ≠ 0.

## (ii) The weighted Kodaira identity (80.K)

**The identity.** div(j/(q+ε)) = div j/(q+ε) − ⟨dq,j⟩/(q+ε)². Integrating gives ∫F_f/(q+ε) = ∫⟨dq,j_f⟩/(q+ε)². The sign is correct.

**The underlying Kodaira identities.** I rechecked these from d(f̄Df∧ω) = \overline{Df}∧Df∧ω + ik|f|² db∧ω, using:
- db∧ω = ⟨db,ω⟩dV = −(2s+q)/4 · dV (ω is self‑dual with |ω|² = 2);
- weight k = 2 for v, giving κ_v = |s| − q/2;
- weight k = 1 for η, giving κ_η = |s|/2 − q/4.

Both agree with Step 79.

**Behaviour near a two‑dimensional stratum.** Write q = cρ^{2m} in the normal plane.
- The leading angular average of the normal component j_ρ vanishes, because j is a constant vector to leading order.
- The next order is (ρ/2)div_N j.

For m = 1 both sides of (80.K) then diverge like (π/c)·(div j)|_Z·log(1/ε), and the divergent parts match.

Hence (80.K) has no finite ε→0 limit at such strata unless F_f|_Z = 0. A residue formula for (80.K) needs the normal 1‑jet of j_f along Z; Step 80 does not supply one.

## (iii) Local limits at zeros

**Constants (verified analytically).**
- *Isolated zero in ℝ⁴:* flux = 2π²R³·2mcR^{2m−1}/(cR^{2m}+ε) → 4π²mR².
- *Codimension two, per unit area:* flux = 2πR·2mcR^{2m−1}/(cR^{2m}+ε) → 4πm. This equals 2m · Δ_N log ρ = 2m·2πδ, so the residue is +4πm[Z₂].

**Correction 1 (isolated model).** At an isolated radial zero the separate terms do converge, for every m:
- ∫|d log q|² → 4π²m²R²;
- ∫Δq/q → 4π²m(m+1)R².

These are 157.91 and 236.87 for m = 2, matching the data. Only the hypothesis 1/q ∈ L¹ breaks for m ≥ 2. The combined integrand D/q = −Δq/q + 3|s|/2 − 9q/4 remains in L¹, so Theorem 79.L's conclusion survives unchanged.

**Correction 2 (general analytic zero sets).** Let Z have dimension d.
- Łojasiewicz gives q ≥ c·dist(·,Z)^N.
- Choose cutoffs φ_ρ with φ_ρ = 1 on the ρ‑tube, supported in the 2ρ‑tube, and |Δφ_ρ| ≤ Cρ⁻².

Then
\[
|\langle\Delta\log q,\varphi_\rho\rangle|\le C\rho^{-2}\,|T_{2\rho}|\,(N|\log\rho|+C)\le C'\rho^{2-d}|\log\rho|\to0\quad(d\le1).
\]
Consequences:
- Isolated zeros of any order, including the degenerate ones of Step 65, and zero curves carry no residue. ∫_{M∖Z}Λ = 0 holds as an improper limit.
- Step 79's statement about curves was correct. Only its assertion "codimension ≥ 3" was unjustified.
- The leading‑polynomial question of §2.1 is irrelevant for isolated zeros.

**Correction 3 (anisotropic normal forms).** For a two‑dimensional stratum the residue density is 2π × (degree of the lowest homogeneous part of q in the normal variables). For example, q ~ x² + y⁴ gives 4π. The formula 4πm stands with 2m defined as this degree.

**Corrected global identity (smooth two‑strata Z_i of normal order 2m_i).** The pointwise combined integrand is L¹ near Z: the two 4m²/ρ² singularities cancel. Then
\[
\int_{M\setminus Z}\Big[|d\log q|^2+\frac Dq\Big]=\frac{3|s|}{2}V-\frac94Q+4\pi\sum_i m_i\,\mathrm{Area}(Z_i),
\]
whereas the ε‑limit of (80.R) has no residue term. The difference is concentrated in the layer ρ ~ ε^{1/2m}. The residue is positive, so two‑dimensional strata raise the average of B above 3|s|/2.

## (iv) The Bianchi‑VIII model

**Exactness of the rational formulas.** With x = p², I checked by hand the polynomial identity
\[
D-24|\eta|^2+8\operatorname{tr}V^2=(80.2).
\]
Both sides equal 216(p²−1)³(135x³+63x²−79x+9)/(3p²+1)⁶. The coefficients are 29160, 13608, −17064, 1944.

**Consistency of D with Δq at the two ends.**
- *Bolt, p = 1/3:* D = −32, so Δq = −32 and Δlog q = −3. This matches the profile value −3.00003.
- *End, t → 0:* G ≈ 1/(2t²), vol ≈ 32/(3t²), and Δq = 27t³ = −D + 18q with D = 54t³.

These two checks plus the polynomial identity do not prove the full rational D. That still requires symbolic simplification of (vol/√G · q′)′/(vol√G) against the displayed rational.

**Leading‑order cancellation.**
- (p²−1)³ ≈ −8t³ and the polynomial evaluates to 128, so the cross term ≈ −54t³.
- 24|η|² ≈ 108t³.

The cross term cancels exactly half at leading order.

**Asymptotic constants.** With x = q/ε and t⁻³dt = (9/2)^{2/3}ε^{−2/3}x^{−5/3}dx/3, every ε‑integral reduces to a Beta integral.
- RHS_ε ≈ 64π√(2/3)(9/2)^{2/3} ε^{−2/3} ≈ 447.5ε^{−2/3}. This gives 4.4747·10¹⁰ at ε = 10⁻¹²; the table has 4.4748·10¹⁰.
- The gradient, D, η and cross terms are exactly 1/3, 2/3, 4/3 and −2/3 of RHS_ε. The table matches these fractions.

These effective weights differ from the pointwise end densities (18, 12, 12, −6 against 18). The 1/(q+ε) weight is genuinely nonuniform at the end.

**Peak of the regularized flux.**
- The flux is Φ ≈ 144√2·t/(4.5t³+ε). It peaks at t = (ε/9)^{1/3}, not at the q = ε layer t = (2ε/9)^{1/3}.
- The peak value is 96√2·9^{−1/3}ε^{−2/3} ≈ 65.26ε^{−2/3}. This matches the data (6.5254·10⁹ at ε = 10⁻¹²).
- Using t ≈ (4/3)e^{−u}, the peak sits at u_peak = (1/3)log(1/ε) + (2/3)log 3 + log(4/3) = (1/3)log(1/ε) + 1.020. The fitted 0.99 reflects the node grid.

**Correction 4 (the sweep residuals).** Every residual equals 3.4387·10⁻¹²/ε. This is exactly the truncated end flux 144√2·(4/3)e^{−32}/ε at u_max = 32.
- The residual is a cutoff effect, not cancellation error.
- Relative to RHS it grows like ε^{−1/3}.
- Once Φ(u_max) is included, (80.R) holds at every tabulated ε.

**Normalization.** The q2 entry converges to 203.6467 = (9/4)·64√2. The Step‑80 measure therefore differs from the Step‑79 table (Q = 64) by a factor √2.

## (v) Statements in §§4–5 that go beyond what is shown

1. **The model's moving layer is at infinity.** On the model q > 0 everywhere; its nonuniform layer sits on the ACH end. It therefore tests nothing about ε→0 at a closed zero set. On closed M the only nonuniformity is at two‑dimensional strata, and it is captured by the residue formula in (iii).

2. **The cross term is the mild singularity.** It carries the factor |α| = √(q/2), so
\[
\Big|\frac{32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle}{q+\varepsilon}\Big|\le16\sqrt2\,|\partial_Dv|\,q^{-1/2}.
\]
This bound is L¹ at isolated zeros with m < 4 and at m = 1 two‑strata, so dominated convergence applies. The transport terms satisfy |dq| ≤ 2|∇²ω|√q and are bounded by C|f||Df|q^{−3/2}, which is L¹ at nondegenerate isolated zeros. The ε‑uniform control demanded in §4 is therefore largely automatic. What is not automatic is a global sign.

3. **The no‑go extends to fixed ε.** At fixed ε all weighted currents have zero end flux on the model: Φ ~ t/ε → 0, and the j_f terms carry an extra decaying dq factor. The model satisfies (80.R) and (80.K) exactly for each ε, so any argument at fixed ε is refuted by it, as in Proposition 79.1. A proof must pass to ε→0 and use V < ∞, i.e. the boundedness of ∫q/(q+ε), which on the model grows like ε^{−2/3}.

4. **The winding statement is incorrect.** α is a section of the rank‑two complex bundle Λ^{1,0}, so α̂ takes values in S³. Since π₁(S³) = 0, α̂ has no normal winding around a two‑dimensional stratum. The 4πm residue comes purely from the vanishing order of |α|². Degree data sit at isolated zeros (S³ → S³, index +1, 5χ+6τ of them), which carry no log residue. The proposed transport interpretation of (80.K) through α̂ is unsupported as stated.

5. **What remains unresolved.** The open problem is a global inequality, on a closed almost‑Kähler Einstein manifold with s<0, comparing
\[
\int_{M\setminus Z}\Big(|d\log q|^2+D/q\Big)\quad\text{with}\quad \frac{3|s|}{2}V-\frac94Q+4\pi\sum_i m_iA_i .
\]
Usable inputs not yet exploited include:
- the zero‑set constraint |v|² ≥ (3/2)|η|²;
- the √q factor in the cross term;
- the positivity of the two‑stratum residue.
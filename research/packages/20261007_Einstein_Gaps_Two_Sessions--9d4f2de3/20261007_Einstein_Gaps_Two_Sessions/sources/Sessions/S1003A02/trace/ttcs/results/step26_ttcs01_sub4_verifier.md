# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md",
    "Sessions/S1003A02/workspace/scripts/cr_pinning_check.py",
    "Sessions/S1003A02/workspace/scripts/squash_escape_cost.py",
    "Sessions/S1003A02/workspace/scripts/ach_projected.py",
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md"
  ]
}
```

## Task

Read Step 25's exact CR-pinning identity, Lemma P, and conditional Theorem D as a geometric analyst. Verify constants, tensor/norm inequalities, control quantifiers, and what genuinely follows. Then analyze the proposed truncation lemma in the ACH diagonal block: identify the eigenmodes at standard CH, separate radial-translation/defining-function or other gauge directions from physical metric modes, and determine the weakest decay sufficient to splice a standard-CR finite-P or Einstein ACH metric to an exact CH collar with vanishing added P. Give either a complete proof route with explicit mode projections and estimates, or a precise mathematical obstruction/counterexample. Keep the relationship among zero infimum, attainment, and standard-CR Einstein existence exact.

## Output

# Verification memo: Step 25 (CR pinning, Lemma P, Theorem D, truncation in the ACH block)

**Summary.**
- Identity (1.1), Lemma P and the sharp constant ½ check out.
- The drift is not ζ²·(polynomial) on state space. It is O(ζ²) only on boxes where the deviation is O(ζ).
- Corollary P1 has an intrinsic form in ζ(T) that removes the W-hypothesis and makes it uniform in j.
- The truncation lemma is provable under the stated block and standard-CR hypotheses, with s = −24 or J₆ < ∞ added. It needs only o(ζ) = o(e^{−2t}) deviation in C¹ of the log-coefficients, and finite cost supplies this automatically.
- The only obstruction to truncation is the neutral Rossi mode, and Theorem E's filling is an explicit instance of it.
- In Theorem D, two hypotheses are missing (scalar normalization and a uniform box). Attainment can only mean attainment in an extended standard-CR class.

---

## 1. Identity (1.1) and Lemma P

**The free drift in closed form.** From the compact system,

$$\widetilde\Phi'_{\rm free}=(y_g-y_h)\Bigl(1-\tfrac S4-\zeta\cosh q\Bigr)+\zeta\sinh q\,(y_g+y_h-2)+\frac{2\zeta^2\sinh 2q}{\kappa^2}. \tag{D}$$

The control part is exactly −(e_g−e_h)/4, as the script confirms. Two consequences follow.

- (D) is not divisible by ζ² as a function on state space. The first two terms are O(|dev|²) and O(ζ|dev|). So "ζ²G" with sup|G| < ∞ is meaningful only on boxes of the form B_K = {|(y,κ)−E_CH(ζ)| ≤ Kζ, |q| ≤ q₀, ζ ≤ ζ₀}. On such boxes |G| ≤ C(K, q₀).
- The quoted sup_B|G| values are therefore valid if the Step-15 blocks have this shape; "K = 1" suggests they do.
- Near standard CH, (D) is ≈ 5ζ²q. Hence a linearized Einstein end has Φ̃(T) = θ_∞ + O(e^{−4T}θ_∞), which is what the sharpness comparison uses.

**Constants.** All of the following check out:
- The orbit volume is 2π²W.
- e_g − e_h = Ric°_gg − Ric°_hh, since the scalar part cancels. Lemma P therefore needs no scalar normalization.
- The bound x² + y² ≥ (x−y)²/2 holds.
- (1/4)√(8P̂) = √(P̂/2).

(1.2) holds for every diagonal metric on every interval, with no constraint used.

Equality requires Ric°_tt = Ric°_ff = 0 and Ric°_gg = −Ric°_hh ∝ 1/W. This is the antisymmetric linear optimizer. If the script's z_i are the Λ⁺⊗Λ⁻ entries z_i = r_t + r_i, then Σz_i² = |Ric°|² exactly. In the antisymmetric sector Σdz_i = 0, so Q is the same under either reading.

**Corollary P1 in intrinsic form.** Since W = a_f a_g a_h = κ/ζ², on a box with y_g + y_h ≥ c_B and κ ≥ κ_min:

$$\int_T^\infty\frac{dt}{W}\le\frac{\zeta(T)^2}{2c_B\kappa_{\min}},\qquad 
\widehat P_{[T,\infty)}\ \ge\ 4c_B\kappa_{\min}\,\frac{(|\widetilde\Phi(T)|-\delta(T))_+^2}{\zeta(T)^2},\qquad \delta(T)=\frac{\sup_B|G|\,\zeta(T)^2}{2c_B}.$$

On CH (c_B = 2, κ = 1, ζ = sinh⁻²T) this is exactly ½e^{4T}(…)². This form has three advantages:
- **No W-hypothesis.** The separate assumption W ≥ ce^{4t}/16 is not needed. That constant c = e^{−4t₀} depends on the cell's radial offset, so the note's "uniform in j via 4e^{−4T}/c" silently assumes uniform offsets.
- **Only pointwise box properties enter:** sup|G|, inf(y_g + y_h) and inf κ. The ingress/egress verification of the Einstein flow plays no role, because box membership of the controlled trajectory is a hypothesis.
- **The q-gap closes cheaply.** Applying P1 to Theorem E's filling requires covering q ∈ [0, log 2.19 ≈ 0.784]. The verified blocks leave a gap at q ∈ (0.3, 0.7). That gap is filled by elementary interval bounds of these three quantities, not by new flow enclosures.

**Sharpness.** The asymptotics m ~ 4e^{−4t}, w ~ e^{−4t}/8 and M ~ e^{−4t} give M²/w ~ 8e^{−4t}, so G ~ 2e^{−4T} and Q_min ~ ½C²e^{4T}. The table converges to 0.5. The constant ½ is asymptotically optimal.

**Theorem E consequence.** The cost lower bound ½e^{4T}(0.784)² is proved for completions whose state stays in the union of boxes over q ∈ [0, 0.784]. Completions that leave the box at large W are the §2 shadowing question.

---

## 2. Linear modes at standard CH: gauge versus physical

At E(0), the Jacobian has a block-triangular ζ-row (0,…,−2). The g↔h parity splits the remaining modes.

**Antisymmetric sector (q, η = y_g − y_h).** The linear equations are q′ = η and η′ = −4η + O(ζ). The eigenvalues are 0 and −4.

**Symmetric sector.** Write u = δy_f, v = δy_g = δy_h, w = δκ, z = δζ. Then

$$\begin{pmatrix}u\\v\\w\end{pmatrix}'=\begin{pmatrix}-6&-4&4\\-1&-6&-4\\1&-2&0\end{pmatrix}\begin{pmatrix}u\\v\\w\end{pmatrix}+\begin{pmatrix}0\\4z\\0\end{pmatrix},\qquad z'=-2z,$$

with linearized constraint δC = 2u + 6v + 2w − 4z.

| rate | eigenvector (y_f,y_g,y_h,κ,q,ζ) | δC | role |
|---|---|---|---|
| +2 | (−4,3,3,−5,0,0) ∝ the face vector (0.8,−0.6,−0.6,1) | 0 | non-ACH growth (toward H⁴ end or singular); absent on Einstein ACH ends; in cells its amplitude must be held by control |
| 0 | q | — | Rossi deformation of the CR structure: physical, non-normalizable for P |
| −2 | (0,2,2,2,0,4) = exact CH approach (y_g−1 ≈ κ−1 ≈ 2e^{−2t}, ζ ≈ 4e^{−2t}, y_f−2 = O(e^{−4t})) | 0 | gauge: radial translation, i.e. constant rescaling of the contact form. This is the only continuous defining-function freedom in the diagonal class; the overall scale is fixed by Ric = −6 |
| −4 | antisymmetric, θ = k⁻¹∫_t^∞ m ~ e^{−4t} | — | physical normalizable mode |
| −6 | (−4,1,1,1,0,0) | 0 | physical normalizable U(2)-symmetric mode |
| −8 | (2,1,0,0,0,0) | 10 | constraint-violating |

**The −8 mode.** For diagonal metrics, C = σ₂(y) − 6 − ½ΣPot = G_tt − 6 = (Ric_tt + 6) − (s+24)/2. When s = −24, C = Ric°_tt pointwise. So this mode is driven by a component of Ric°; it is not an Einstein mode.

**Count of Einstein ACH ends.** Modulo translation, the ends form a 3-parameter family (q_∞, c₄, c₆). The bolt separatrix family is one-dimensional, so ρ_∞ = 1 is a codimension-one condition along it.

**Gauge-free reduction.** Match the contact area by comparing with CH at the same ζ:

$$E_{\rm CH}(\zeta)=\Bigl(\tfrac{2+\zeta}{\sqrt{1+\zeta}},\sqrt{1+\zeta},\sqrt{1+\zeta},\sqrt{1+\zeta},0,\zeta\Bigr),$$

and set Y = state − E_CH(ζ), with five components. E_CH is an exact orbit and ζ′ − ζ′_CH(ζ) = −ζ(Y_g + Y_h). Hence

$$Y'=(A_{\rm face}+O(\zeta))Y+O(|Y|^2)-B\,e,\qquad \operatorname{spec}A_{\rm face}=\{2,0,-4,-6,-8\},$$

with no inhomogeneous term. The gauge mode is gone. The neutral left eigenfunction is dΦ̃, and Lemma P is exactly the Duhamel formula for the neutral projection.

---

## 3. Truncation lemma: proof route and the weakest decay

**Statement (T).** Let g be a complete diagonal metric on O(−1) with:
- P̂(g) < ∞, and either s = −24 or J₆(g) < ∞;
- state in B_K for t ≥ T₀;
- Φ̃(t) → 0.

Then there are exact-CH-ended diagonal metrics g_R with P(g_R) → P(g).

**Why s = −24 or J₆ < ∞ is needed.** The forcing is e_i = Ric°_ii + (s+24)/4 together with C. Only when s = −24, or (s+24) ∈ L²(W dt), are all forcing components in L²(W dt) with tail norm ε(t) := P̂_{[t,∞)} → 0 (or the J₆ analogue).

**Step 1: neutral mode.** Apply Lemma P on [t, ∞) with Φ̃(∞) = 0:

$$|\widetilde\Phi(t)| \le \delta(t) + \zeta(t)\sqrt{\varepsilon(t)/(4c_B\kappa_{\min})} = o(\zeta).$$

**Step 2: remaining modes.** The perturbation O(ζ) = O(e^{−2t}) is integrable, so the dichotomy with rates {2; −4, −6, −8} persists (Levinson). Box membership makes the nonlinear and ζ-coupled terms O(K²ζ²). This includes ζq, since q = Φ̃ − η/4 + ζ sinh q = O(ζ).
- **Stable components (rates λ > 2).** Cauchy–Schwarz with the split at t′ = (t + T₀)/2 gives Y_λ = O(e^{−2t}[√ε(t′) + e^{−(λ−2)(t−t′)}] + te^{−4t}).
- **Unstable component.** Since e^{−2s}Y₊(s) → 0, Y₊ = −∫_t^∞ e^{2(t−s)}(f + N) = O(e^{−2t}√ε(t) + e^{−4t}).

Hence |Y| = o(ζ).

**Step 3: splice.** Let D_i = log a_i − log a_i^{CH}(·+τ_R), with τ_R defined by ζ_CH(R + τ_R) = ζ(R). Set log a_i^R = log a_i^{CH} + χD_i on [R, R+1].
- τ_R converges, since (log ζe^{2t})′ is integrable.
- At t = R: D_g + D_h = 0, D_g − D_h = q = o(ζ), and D_f = O(|Y|). On the annulus, |D| + |D′| = O(sup|Y|).
- The key structural fact: Ric_ii = −y_i′ − y_iS + Pot_i and Ric_tt = −Σ(y_i′ + y_i²) are affine in y′ with constant coefficients. With y^R′ = χy′ + (1−χ)y^{CH}′ + 2χ′D′ + χ″D, this gives

$$|\mathrm{Ric}^\circ(g_R)|\le|\mathrm{Ric}^\circ(g)|+C(|D|+|D'|)\quad\text{on }[R,R+1].$$

Therefore

$$P(g_R)\le P_{[0,R]}(g)+2P_{[R,R+1]}(g)+C\,W(R)\sup_{[R,R+1]}(|D|+|D'|)^2=P(g)+o(1).$$

No sphere-flux term arises, because no integration by parts is used. This is unlike the J₆/conformal identity of Step 22, where m > 4 was needed.

**Weakest decay.** For this unit-annulus splice the sufficient condition is

$$\sup_{[R_k,R_k+1]}(|D|+|D'|)=o(\zeta(R_k))=o(e^{-2R_k})\quad\text{along some }R_k\to\infty.$$

- Only C¹ of the log-coefficients is needed, not C². The second derivatives of g are reused with weight χ ≤ 1 and cost at most 2P_ann(g) → 0. This C¹ sufficiency is special to the ODE structure. A general 4D splice would need gauge-fixed W^{2,2}-type control.
- The threshold is the √W weight, so it is scale-natural. It matches Step 22's remark that quadratic energies are finite for m > 2.

**Corrections to the note's sketch.**
- For finite-P non-Einstein metrics the forced response is o(e^{−2t}), not O(e^{−4t}). The added cost is O(ε(R) + e^{−4R}), not O(e^{−4R}).
- The note's list of rates 4 and 6 omits the neutral mode 0, the unstable mode +2 and the constraint mode −8. The neutral mode is the one carrying the obstruction.
- No separate "CH scale" matching is needed.
- For Einstein standard-CR ends the rates are ≥ 4. Resonances 4 = 2·2, 6 = 3·2 and 8 = 4·2 may add polynomial factors; parity excludes ζ² forcing of the antisymmetric sector. The added cost is O(t^k e^{−4R}).

**Which hypotheses are essential, mode by mode.**

- **Neutral direction.** Lemma P gives P̂_{[R,∞)}(any in-box completion) ≥ 4c_Bκ_min(|Φ̃(R)| − δ)²/ζ(R)². So Φ̃(R) = o(ζ(R)) is necessary for any vanishing-cost completion. It is automatic exactly when q_∞ = 0.
- **Stable modes.** These need no control: moving the splice outward reduces their cost like e^{(4−2λ)R}.
- **Unstable mode.** Its O(ζ) amplitude would cost O(1). It is excluded by convergence to the curve.

**Counterexample showing Φ̃ → 0 cannot be dropped.** Theorem E's filling has J₆ = 0, ACH curvature asymptotics and an in-box tail. Yet every in-box exact-CH completion beyond R costs ≥ ½e^{4R}(0.784)² + o(e^{4R}) → ∞. So "finite cost and ACH" does not suffice; standard CR is the exact extra input.

---

## 4. Theorem D: what follows exactly

**Missing hypotheses.**

- **(H1) Scalar normalization.** Use the Yamabe-normalized sequence ĝ_j = u_j²g_j. By Step 22, P(ĝ_j) ≤ P(g_j); SU(2)×Q₈-invariance follows from uniqueness; Φ̃(ĝ_j) → 0 because q and y_g − y_h are unchanged where q = 0. Without this, the limit may have s ≠ −24, and the forcing (s+24)/4 is uncontrolled. The per-component pinning ∫|e_i| ≤ 2√P̂(∫dt/W)^{1/2} used in §2 of the note (constant 2, not 1/√2) also needs s = −24.
- **(H2) Uniform box.** T₀, K, ζ₀ and q₀ must be uniform in j. With the intrinsic form of P1 this already gives the uniformity used in alternative 7, without a W-constant.
- **(H3) Two-sided compact control.** Two-sided bounds on the a_i on compact radii and bolt radius in [c, C] are needed for H²_loc compactness, which in one variable gives C¹ convergence of y. At the bolt, finite P in the limit excludes a codimension-two cone, because a Ricci measure on the bolt sphere is not L². Convergence there still needs an ODE estimate near t = 0.

**What then follows.**

- **Escape of cost to infinity inside the box is harmless.** Lower semicontinuity gives P(g_∞) ≤ p. Truncation (T) applied to g_∞ gives P(g_∞) ≥ p.
- **Attainment holds in the extended class**
  Ĉ = {complete diagonal, J₆ < ∞, in-box tail, Φ̃ → 0}.
  Here inf_Ĉ P = p exactly, by (T).
- **Criticality.** g_∞ is critical for compactly supported diagonal variations. By Palais symmetric criticality (diagonal metrics are the fixed set of SU(2)×Q₈), it is fully critical. Using grad∫s² = 2∇²s − 2(Δs)g − 2sRic + ½s²g, which has trace −6Δs, the trace of the Euler–Lagrange equation gives Δs = 0. With s → −24 at the single end, the maximum principle gives s ≡ −24. The equation then reduces to

$$2\,\mathrm{grad}\!\int|W|^2-\tfrac{s}{6}\mathrm{Ric}^\circ=0,$$

  a Bach-type equation that Einstein metrics satisfy. This gives a finite-dimensional shooting problem for the p > 0 alternative.
- **Non-attainment in the exact-CH class.**
  - For p = 0 this follows from Lemma R (O(−1): Δχ = 1 ≠ 3Δτ = −3).
  - For p > 0, an exact-class minimizer would be critical and Einstein on the collar. Unique continuation for the critical system would then make it Einstein everywhere, contradicting Lemma R. Unique continuation is immediate if the reduced fourth-order diagonal system is regular in its top derivative, with the lapse equation acting as a first integral; that regularity is what remains to check.

**Exact logical relations.**

1. A complete diagonal standard-CR Einstein ACH filling exists ⇒ p^diag = 0, unconditionally. This uses (T) in the Einstein case, which is proved by the mode analysis above. The infimum is then not attained in the exact class.
2. p^diag > 0 ⇒ no such filling.
3. p^diag = 0 together with a minimizing sequence satisfying (H1)–(H3) ⇒ such a filling exists. The limit has Ric° = 0, is in-box, has Φ̃ → 0, and converges to E(0).
4. "Attained" refers to Ĉ. In the exact class the infimum is never attained (modulo unique continuation when p > 0).

---

## 5. Face dynamics (§2 of the note)

The κ↑ unstable branch has y_g = y_h → −∞. Then a_g a_h decreases, ζ grows and W = κ/ζ² falls, so control becomes cheap along this branch. An off-curve excursion at large W can therefore reach a small-W region, which is the interior-neck alternative 4. Alternative 5 is not independent of alternative 4.

The κ↓ branch keeps W large, since W grows like e^{3√2 t} toward the H⁴ point. The shadowing argument applies there with integrated control ≤ 2√P̂ (∫dt/W)^{1/2}.

Excluding nonstandard-CR escape (alternative 6) outside the boxes reduces to these same two branches.
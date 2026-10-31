# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md",
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A02/workspace/scripts/o11_collar_arb_certificate.py",
    "Sessions/S1003A01/workspace/scripts/perp_spin_diagnostics.py",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json"
  ]
}
```

## Task

Derive a concrete rigorous certification route for the frozen diagonal Bianchi-IX cell J_6/(8π²)<1 using its explicit F,G,w profile. The raw spin formulas suffer bolt cancellation. Starting from y=x-x0, F=y Fhat, G=y Ghat, w=y² what and/or a regular proper-radius variable, derive regularized formulas or Taylor-model structure for the relative-plus-scalar density that can be enclosed by Arb/MPFI on finitely many intervals. Specify which analytic bounds and endpoint expansions suffice, how to handle exp/log/Chebyshev terms with decimal coefficients, and how to turn the 8.84e-4 numerical margin into a theorem-level upper bound without relying on optimizer convergence or empirical Richardson error. Use the supplied formulas and scripts, and pursue an implementable proof rather than general advice.

## Output

# Certifying J₆/(8π²) < 1 for the frozen degree-8 perpendicular cell

## 1. Why the raw formulas cancel, and the regular variable

The trouble near the bolt does not come from the geometry. It comes from computing functions that are odd in proper time through square roots of quantities that vanish there. The cure is the half-power variable s = √y, y = x − x₀.

With F = yF̂, G = yĜ, w = y²ŵ, the proper time satisfies dt = dx/(2√G). This gives

$$
\frac{d}{dt}=2s\sqrt{\widehat G}\,\frac{d}{dy}=\sqrt{\widehat G}\,\frac{d}{ds},
\qquad t=\sqrt y\cdot(\text{analytic, positive in }y).
$$

So s is a regular proper-radius variable, and y is analytic in t². The bolt-adapted axes are

$$
a_1=\sqrt x,\qquad a_2=\sqrt x\,e^{w/2},\qquad a_3=s\sqrt{\widehat F}.
$$

Write D = √Ĝ and let primes denote d/dy. Every Cartan quantity then has a definite parity:

- u₁ = sU₁ and u₂ = sU₂.
- u₃ = U₃.
- u̇₁ = D(U₁ + 2yU₁′), u̇₂ = D(U₂ + 2yU₂′), u̇₃ = 2sDU₃′.
- λ₁ = sL₁, λ₂ = sL₂, λ₃ = L₃/s.
- H₁ = sh₁, H₂ = sh₂, H₃ = U₃ + yU₁U₂/2.

Here U_i, L_i, h_i and H₃ are analytic functions of y. Substituting these into S₁, S₂, S₃, the cubic term and the scalar square, each t-density becomes exactly s·(analytic in y). The Jacobian dt/dx = 1/(2sD) cancels that s.

**Consequence.** The x-density R(x) is real-analytic on the closed interval [x₀, X]. Every raw 0/0 is algebraically removable. No Taylor expansion at the bolt is needed beyond one removable entire function, E₁ in §2. This is the Z₂ parity t → −t that encodes bolt smoothness, made explicit.

## 2. Regularized primitives in the logarithmic variable u ∈ [0,1]

Integrating in u removes log1p and Λ-type removable singularities, because the Chebyshev data are polynomial in u. Define:

- ℓ = log(X/x₀) = log 800.
- x = x₀e^{ℓu}, and y = x₀(e^{ℓu} − 1) = uν, with ν = x₀ℓE₁(ℓu) and E₁(z) = (e^z − 1)/z.
- S̃(u) = 10 − 15u + 6u², so that S(u) = u³S̃(u).
- P_F, P_G, P_w are the Chebyshev sums Σcₙ Tₙ(2u − 1), evaluated by Clenshaw recurrence.
- q_F = (1 − u)³P_F and q_G = (1 − u)³P_G.

The profile functions and their regularized forms are:

$$
\begin{aligned}
F&=y e^{q_F}+x_0u^3\tilde S, &\widehat F&=e^{q_F}+x_0u^2\tilde S/\nu,\\
G&=\big(y+(x^2+x_0)u^3\tilde S\big)e^{q_G}, &\widehat G&=\big(1+(x^2+x_0)u^2\tilde S/\nu\big)e^{q_G},\\
w&=\log(1+x)\,u^3\tilde S+u^2(1-u)^3P_w, &\omega:=w/y&=u\big(\log(1+x)u\tilde S+(1-u)^3P_w\big)/\nu .
\end{aligned}
$$

Note that ν ≥ x₀ℓ > 0, so 1/ν is harmless. The first y-derivatives are F_y = F_u/(ℓx) and w_y = w_u/(ℓx), taken from the unfactored expressions; neither involves division by y. Using x(e^w − 1)/y = xωE₁(w), the U_i are:

$$
\begin{aligned}
U_1&=\frac{D}{\sqrt x}-\frac{\widehat F+x\,\omega E_1(w)}{\sqrt{x\widehat F}\,e^{w/2}},\\
U_2&=De^{w/2}\Big(\frac1{\sqrt x}+\sqrt x\,w_y\Big)-\frac{\widehat F-x\,\omega E_1(w)}{\sqrt{x\widehat F}},\\
U_3&=\frac{D\,F_y}{\sqrt{\widehat F}}-2\cosh\frac w2+\frac{y\widehat F e^{-w/2}}{x}.
\end{aligned}
$$

The derivatives are U_{i,y} = U_{i,u}/(ℓx). The auxiliary quantities are:

- L₁ = e^{w/2}√F̂, L₂ = e^{−w/2}√F̂, L₃ = xe^{w/2}/√F̂.
- h₁ = U₁ + U₂U₃/2, h₂ = U₂ + U₁U₃/2, H₃ = U₃ + yU₁U₂/2.
- V_i = D(U_i + 2yU_{i,y}) for i = 1, 2.

Then

$$
J_6/(8\pi^2)=1+\int_0^1 R\,\ell x\,du,
$$

with

$$
2D\,R=\frac{L_1}{4}\Big(V_1+\frac{2h_1}{L_1}\Big)^2+\frac{L_2}{4}\Big(V_2-\frac{2U_2-U_1U_3}{L_2}\Big)^2
+L_3\Big(DU_{3,y}+\frac{H_3}{L_3}\Big)^2+\frac{2U_1U_2U_3}{L_2}+\frac{xe^{w/2}\sqrt{\widehat F}}4(\Sigma-12)^2,
$$

where

$$
\Sigma=\frac{V_1}{\sqrt x}+\frac{V_2e^{-w/2}}{\sqrt x}+\frac{2DU_{3,y}}{\sqrt{\widehat F}}+\frac{2h_1e^{-w/2}+2h_2}{\sqrt{x\widehat F}}+\frac{2H_3e^{-w/2}}{x}.
$$

**Positive form as a cross-check.** The same substitution gives Ppos with three sign changes: (V₁ − 2h₁/L₁)², (V₂ − 2h₂/L₂)², and L₃(DU_{3,y} − H₃/L₃)², with no cubic term.

**Values at u = 0.** These are exact consequences of the construction:

- D = √g₁ and F̂ = f₁, with f₁g₁ = 1.
- w = ω = 0 and E₁ = 1.
- U₁ = U₂ = (√g₁ − √f₁)/√x₀ ≈ 0.316 and U₃ = −1.

So the integrand is finite and continuous at the bolt.

**Jet orders.** The profile functions (F, w, and their pieces) need order-2 jets in u. U_i, D, F̂ and ω need only order-1 jets: their first u-derivatives are what produce U_{i,y}. Only the value and first-derivative components of the U-level jets are used. This matters because the existing J2 class silently truncates the third derivative when it promotes a′ to a jet.

**The only removable function: E₁.** It is needed at z = ℓu ≤ 6.69 and at z = w (|w| ≲ 3 on this profile). For any real or complex ball,

$$
E_1^{(k)}(z)\in\sum_{n=0}^{N}\frac{z^n}{n!\,(n+k+1)}\;\pm\;\frac{|z|^{N+1}e^{|z|}}{(N+1)!}.
$$

Taking N ≈ 80 gives a tail below 10⁻⁴⁰ everywhere, with no case split. Jets are composed by Faà di Bruno at order 1 or 2. For higher-order series, the coefficientwise majorant Ẑ^{N+1}e^{Ẑ}/(N+1)! bounds the tail, where Ẑ has absolute-value coefficients.

**Exp, log and Chebyshev terms** are ordinary ball operations. Branch points can occur only at F̂ = 0, Ĝ = 0, x = 0 and x = −1, all far from the real segment.

## 3. The constant 1 is an exact Chern–Simons end term

The script's variable C = Σu_i² + u₁u₂u₃ is not the correct end term. Compare the completed squares directly. Each pair shares the same λ_i u̇_i²/4 part, so the differences are:

- Ppos₁ − S₁ = −2u̇₁H₁.
- Ppos₃ − S₃ = −2u̇₃H₃.
- Ppos₂ − S₂ = −u̇₂u₁u₃ + 2u₁u₂u₃/λ₂.

Summing,

$$
\mathrm{Ppos}-(S_1+S_2+S_3+2u_1u_2u_3/\lambda_2)=-\frac{d}{dt}\Big(u_1^2+u_3^2+u_1u_2u_3\Big)=: -\dot B .
$$

The right-hand side contains no u₂² term. This matters. In complex hyperbolic space (CH), with x = sinh²r, one has u₁ = u₃ = 0 but u₂ = 3x. A u₂² term would therefore contribute 9X² ≠ 0 at the collar.

In regular form, B = yU₁² + U₃² + yU₁U₂U₃, which is analytic on the closed interval. The end values are:

- At the bolt, B = U₃² = 1 exactly.
- At X, B = 0 exactly.

The value at X is structural. Every free coefficient is multiplied by (1 − u)³, and S(1) = 1, S′(1) = S″(1) = 0. Hence the values, first jets and second jets of F, G, w at X are those of the CH profile (x, x + x², log(1 + x)) for any coefficient vector. Since u_i depends only on (a, ȧ), this gives u₁(X) = u₃(X) = 0.

Two further consequences:

- P/(8π²) = 1 + ∫rel holds exactly, by the fundamental theorem of calculus on [x₀, X]. B is continuous through the bolt because the metric is smooth there.
- The identity is a polynomial identity in the variables (u_i, u̇_i, λ_i). A Lean `ring` proof or a SymPy expansion settles it in a few lines.

## 4. The exact object being certified

Treat the 24 JSON decimal strings as exact rationals. Since Tₙ(−1) = (−1)ⁿ, replace c_G[0] by

$$
c_G[0]-\sum_{n=0}^{7}(-1)^n\big(c_{F,n}+c_{G,n}\big),
$$

computed in exact rational arithmetic. Then q_F(0) + q_G(0) = 0 exactly, so F′G′ = 1 at the bolt exactly. The other exact properties are w = O(y²), the CH second jet at X, and positivity of F and G from the profile formula.

The theorem concerns this one rational metric. Ball arithmetic (initialized from exact fmpq values, or from the binary64 values as exact dyadics) encloses its values. No optimizer output enters.

The present Arb script departs from this in three places:

- It converts the decimal strings to balls via `arb(repr)`.
- It omits [0, 10⁻¹²] without enclosing it.
- It bounds the Simpson remainder by Richardson extrapolation.

The regularized integrand removes the need for all three.

## 5. Two independent rigorous integration engines

**Engine A: complex-ball Gauss quadrature.** The integrand f(u) = R ℓx is holomorphic in a complex neighbourhood of [0, 1]. Implement the order-2 jet class over `acb`. Use `sqrt(analytic=True)` and `log(analytic=True)`, which return non-finite balls if a box touches a branch cut, and E₁ as in §2. Then call `acb.integral(f, 0, 1)` (Arb `acb_calc_integrate`).

Error control is Petras' bound. On a panel mapped to [−1, 1], if f is holomorphic on the Bernstein ellipse E_ρ with |f| ≤ M there, the n-point Gauss error is at most (64M/15)ρ^{−2n}/(ρ² − 1), times the panel's half-length. Arb applies this with adaptive bisection, so the output ball is a rigorous enclosure of the integral. No derivative bounds and no empirical convergence enter.

Splitting [0, 1] into about 64 panels and running them in parallel processes, at 128–192 bits, the expected result is about −8.8376 × 10⁻⁴ with an enclosure radius far below 10⁻¹⁰.

**Engine B: real Taylor models.** This independent check uses no complex analysis. On a panel [m − h/2, m + h/2],

$$
\int f = h f(m)+\frac{h^3}{24}f''(m)+E,\qquad |E|\le \frac{h^5}{1920}\sup_{\text{panel}}|f^{(4)}|.
$$

- f(m) and f″(m) are computed at the point m.
- sup|f⁽⁴⁾| comes from the fourth Taylor coefficient of f, evaluated with `arb_series` on the ball covering the whole panel. This requires order-6 profile jets.
- With 400 equal panels, the total remainder is about 2.5 × 10⁻¹⁴ · sup|f⁽⁴⁾|.

The margin of 8.8 × 10⁻⁴ therefore tolerates overestimating sup|f⁽⁴⁾| by roughly ten orders of magnitude. Dependency inflation is harmless once the 0/0 has been removed algebraically, which is precisely what the raw spin variables did not allow.

**Built-in consistency check.** Compute 1 + ∫rel and ∫Ppos separately. The endpoint value B = 1 enters only the first, so the overlap of the two enclosures tests both the transcription and the identity of §3.

**Pointwise check.** On u ≥ 0.05, compare the regularized R with the raw JAX density at sample points. This catches transcription slips; it is not a proof step.

## 6. Algebraic certificates outside the quadrature

1. **Curvature formula.** For e⁰ = dt and eⁱ = a_iσ_i, with the structure-constant convention fixed by the flat case u_i = 0, show in SymPy that the curvature density, normalized by orbit volume, equals Σ(λ_i/4)(u̇_i − 2H_i/λ_i)² pointwise. Likewise show that the scalar density equals a₁a₂a₃(Σ − 12)²/4. Also verify |Ric + 6g|² = |Ric°|² + (s + 24)²/4. The method is to substitute ȧ_i = u_i + (a_j² + a_k² − a_i²)/(a_ja_k), clear denominators and reduce to zero. If the agreement held only up to a total derivative, the extra end term would be read off at the same two endpoints.
2. **Regularization.** Substitute a₃ = s√F̂, F = yF̂, w = yω into the raw densities, with s² = y symbolic. Show that the raw x-density minus R is identically zero.
3. **End-term identity.** Prove the B identity of §3 (Lean `ring` or SymPy).

## 7. From the C² cell to a smooth exact-collar cell

No quantitative cutoff estimate is needed. Let d = (profile − CH profile).

- d is C^∞ on [x₀, X], vanishes to second order at X, and is zero beyond X.
- Fix a smooth ψ equal to 1 on [x₀, 1] and 0 on [2, ∞).
- Set d_ε = ψd + (1 − ψ)(ρ_ε ∗ d), where ρ_ε is a mollifier in x.

Then d_ε is smooth, equals d near the bolt, vanishes for x ≥ X + ε, and converges to d in C² on compact sets. Curvature and volume depend continuously on the 2-jet of the metric, so J₆(d_ε) → J₆(d), and positivity persists. Hence for every ε₀′ < ε₀(certified), smooth exact-CH-collar cells exist with J₁ ≤ 8π²(1 − ε₀′). The transfer coefficient is then strictly below 4 − 8ε₀′/9.

## 8. Resulting statement and immediate extensions

**Statement.** For the rational metric of §4, ∫₀¹ f du lies in a computed ball whose upper end is below −8.8 × 10⁻⁴. Combined with the identities of §3 and §6 and the mollification of §7, this gives J₆/(8π²) < 1 for a smooth bolt cell with an exact CH collar. Feeding that cell into the transfer formula gives O11 with coefficient strictly below 4.

**Extensions with the same code:**

- **Open set of cells.** Run Engine A with every coefficient inflated to a ball of radius 10⁻⁶ (keeping the exact shift relation). The enclosure then certifies a whole open set of subthreshold cells, so the result does not depend on the decimal representation.
- **Families in x₀.** Making x₀ a ball parameter certifies families; the reported subthreshold values at x₀ = 0.003 and 0.03 can be tested this way.
- **Mechanism.** Panel-wise enclosures over u ∈ (0, .1), (.1, .3), (.3, .6), (.6, .9), (.9, 1) convert the recorded cubic-versus-square bookkeeping into enclosed numbers.
- **X = 16 witness.** It has the same structure and a larger margin, and needs no new formulas.
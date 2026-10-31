# Step 68: Absorption of 20260912.tex into active research

Session: S0910A03. Agent2 / Constructor. Phase: Explore.

## 1. Two complementary difficulties (manuscript line 6436)

The manuscript isolates the central strategic fact, stated at lines 6436–6437:

> "Surface bundle route has δ → 0 on a fixed manifold but lacks Einstein
> nonexistence. Extended graph manifold route has Einstein nonexistence
> but lacks δ → 0 construction. Splicing their advantages does not
> automatically produce a manifold with both properties."

**This is the organizing principle for all further Yau 26 negative-branch work.**

## 2. Surface bundle: what is established

On a fixed Dehn-twist surface bundle E_D (fiber Σ_p, base Σ_q, p,q ≥ 2,
monodromy = positive non-separating Dehn twist):

### 2.1 δ → 0 construction (Chapter 6, lines 3278–3433)
- Slow interpolation metric G_ℓ with complete Ricci matrix in
  orthonormal frame (eq. 3.66):

  Φ(G_ℓ)_ON = diag(-v²/2, 0, -v²/2, v²/2) + off-diagonal v-derivative terms

  where v = Qz', Q = a·ζ', and a = cusp width, z = interpolation profile.

- δ(G_ℓ) ≤ (A₀²M₁²)/(2L²) + O(L⁻¹) → 0 as collar length L → ∞.
- Volume exactly V₀ = 16π²(p−1)(q−1), bounded curvature + all derivatives.

### 2.2 Double-collar improvement (lines 3472–3543)
- Balanced profiles using ε → 0 with β = ε²:
  **δ(G_ε) = (2/π⁴)ε² + O(ε⁴)** — exact coefficient.

### 2.3 Second-order correction (lines 3545–3641)
- Linearized Einstein operator J_g splits into three scalar equations on
  the product cylinder. All solvable with explicit Green operators.
- Bianchi gauge satisfied identically (commutation identity).
- Corrected metric G̃_ε = G_ε + ε²ΨK achieves:
  **||Φ(G̃_ε)||_{C^k} ≤ C_k ε³** for each fixed k.

### 2.4 Global TT obstruction (lines 3661–3732)
- Concentrating holomorphic quadratic differentials provide a global TT
  tensor Q_ε with ∫⟨Φ(G_ε), Q_ε⟩ = −ε³β/(2π²)(1+o(1)).
- Nonlinear lower bound: **c·ε³ ≤ C·δ(g_ε) + C·ε²·a_ε + C·a_ε²**
  for any global C² correction a_ε = ||h||_{C²}.
- Achievable rate is **δ = Θ(ε³)** — matched between upper and lower.
- To break past ε³ requires a_ε ≥ c·ε^{3/2} (critical scale).

### 2.5 Topology (lines 4034–4329)
- χ = 4(p−1)(q−1), τ = 0, b₁ = 2p+2q−1 (odd).
- Aspherical: K(G,1).
- **No complex structure on any finite cover** (Kotschick).
- **Not virtually Kähler** (deeper odd-b₁ covers always exist).
- **No sec ≤ 0 metric** (Kapovich–Leeb CAT(0) obstruction).
- Variational identities: Y(E_D) = −4√V₀, inf∫|Ric|² = 4V₀ (not attained),
  inf∫|Rm|² = 8V₀.
- **Einstein existence ⟺ inf∫|Rm|² attained** (eq. 4.33).
- The non-attainment of scalar and Ricci energy does NOT pass to full
  curvature energy. In particular, a normalized Einstein output need not have
  the approximating sequence's volume \(V_0\): Chern–Gauss–Bonnet gives
  \(V_0<\operatorname{Vol}<3V_0\) for a hypothetical \(\operatorname{Ric}=-g\)
  metric, while its full curvature energy is topologically fixed at \(8V_0\).
  **Einstein nonexistence on E_D is genuinely open.**

## 3. Extended graph manifolds: what is established

For a closed Frigerio–Lafont–Sisto extended graph 4-manifold M with
at least one purely hyperbolic block (Chapter 10, lines 6436–6507):

- Di Cerbo: **every Einstein metric excluded** (all λ signs).
- V* = inf_{Ric≥−g} Vol(M) = 12π²χ(M).
- For ||Ric+g||_op < δ < 1/3:
  - Volume: V*/(1+δ)² ≤ Vol ≤ V*/(1−δ)²
  - Mean Weyl: (1/V)∫|W|² ≤ (8/3)δ
  - Sup Weyl: **||W||_∞ ≥ (1−3δ)/√3** (Preissmann)
  - With ∇W bounded: **diam ≥ √(2/7)·log(1/δ) − C**
- **No δ → 0 construction exists on these manifolds.**

## 4. Boundary mean curvature threshold (lines 1658–1725)

For compact W^{m+1} with two boundary components Σ₀, Σ₁,
Ric ≥ −mk²g, outward mean curvatures H ≥ hᵢ, distance L:
$$h_0 + h_1 \le 2mk\tanh(kL/2) < 2mk.$$

Applied to 4D normalized hyperbolic (m=3, Ric ≥ −3k²g):
- Sphere of radius R: H_R = √3·coth(R/√3)
- Interface with ||Ric+3g||_op ≤ δ: **δ > csch²(R/√3)**
- **R > (√3/2)·log(1/δ) + √3·log 2 + o(1)**
- Bridge length L ≥ 2√(3/(1+δ))·artanh(coth(R/√3)/√(1+δ))

This means: any neck connecting two hyperbolic cusp interfaces at defect
δ must have logarithmically growing collar. This is compatible with the
diameter bound above and does NOT exclude δ → 0; it just constrains
the geometry.

## 5. Local curved-neck mechanism (lines 1409–1463)

Confirms our Step 67 local theorem. Explicit seed:
$$h_0 = dz^2 + e^{2\sin z}dx^2 + e^{-2\sin z}dy^2, \quad s_{h_0} = -2\cos^2 z.$$
Yamabe minimizer gives analytic h with s_h = −2 (or −6 after rescaling).
Koiso analytic Cauchy → Ric = −g band (or Ric = −3g after rescaling).
H = t + O(t³), central T³ calibrated and area-minimizing.

For S³ initial data: necessary anisotropy ||T||_op > (1−5δ)/3 when δ < 1/5.

## 6. Berger core analysis (lines 1465–1603)

Explicit biaxial extension has curvature singularity at finite distance
T_max < a/2. Near-Einstein biaxial metrics have T_max ≤ a/√(4+a²−δa²).
Three-axis variation: if δ ≤ 1, then a₂,a₃ keep shrinking, L < 11a/5.
**Every specified symmetric extension of the Berger core hits a singularity.**

Shape quantity u' + Hu' = 4(q−1)/a² + η, |η| ≤ 2δ: "slowing down" does
not automatically give O(L⁻¹) error because the intrinsic source persists.

## 7. Fibered Einstein equations (Chapter 8, lines 5426–5583)

Two rigidity theorems:
1. **Integrable horizontal + Einstein → product** (Theorem 8.1).
   Proof: K minimum point forces H=0, div-integral forces K≡λ, TT
   tensor on high-genus fiber forces S=0.

2. **Basic mean curvature + Einstein → product** (Theorem 8.3).
   Uses Euler bundle obstruction, conformal vector field rigidity, Wood's
   harmonic morphism, LeBrun Hermitian rigidity.

Both exclude Einstein adapted to the fiber structure. **Neither excludes
a metric not adapted to the projection.**

WP energy bound (lines 3457–3470):
$$\frac12\int_B|dF|^2 dA \ge 6\pi^2|\tau(E)|.$$
Non-zero signature → moduli speed can't uniformly → 0. Single-twist
bundles have τ=0, so this is not an obstruction.

## 8. Formula corrections

### 8.1 Equation (E) trace factor (Step 67 note, now fixed)
The tangential Einstein evolution is:
$$\ddot{g}_t = 2\operatorname{Ric}^{g_t} + \dot{g}(g^{-1}\dot{g}\cdot,\cdot) - \frac12\operatorname{tr}(g^{-1}\dot{g})\dot{g} - 2\lambda g.$$
The factor is **1/2**, not 1 as originally written. Verified by trace
consistency with the normal equation. The Koiso conclusion (g̈₀ = 2Ric+6g,
H'(0) = 3) is unaffected since ġ₀ = 0.

### 8.2 ASD obstruction to totally geodesic T³ in Li-Liu family
Reflection across a codimension-1 hypersurface reverses 4D orientation.
Under orientation reversal: W⁺ ↔ W⁻. If W⁺ = 0 (ASD), the reflection
isometry forces W⁻ = 0 also → conformally flat → constant curvature K=−1
→ totally geodesic T³ inherits K=−1, impossible for π₁=Z³. **Confirmed:
no ASD Einstein 4-manifold has a totally geodesic T³.**

## 9. What each approach needs to complete

### Surface bundle → negative-branch counterexample:
**Missing: Einstein nonexistence on E_D.**
- All standard tools fail: Hitchin–Thorpe satisfied, b₊>1 breaks simple
  SW, no complex structure doesn't exclude non-Kähler Einstein, no sec≤0
  doesn't exclude positive-curvature Einstein.
- The exact criterion is: inf∫|Rm|² = 8V₀ attained iff Einstein exists.
- Fibered rigidity is only for adapted metrics.
- This is the hardest open question on this route.

### Extended graph manifold → negative-branch counterexample:
**Missing: δ → 0 global construction.**
- Local Koiso reversal confirmed.
- The deleted-ball radius estimate and the flat-cusp bridge length estimate
  are distinct: neither supplies a shrinking-volume construction.
- Weyl must concentrate: ||W||_∞ ≥ (1−3δ)/√3.
- In a warped slice, shrinking scale amplifies intrinsic Ricci by \(f^{-2}\),
  while slow interpolation only reduces normal derivatives. The missing object
  is a coupled anisotropic compensation into a thin flat cusp, not a generic
  long adiabatic path.
- No metric on a graph manifold is currently known to achieve ||Ric+g||_op→0.
- Chapter 6 avoids this conflict because one curved product direction remains
  at Einstein scale while a different base circle degenerates.

### Both approaches have complementary advantages that can't simply be
    spliced. Each requires new mathematics at its weakest point.

## 10. Key formulas for reuse

1. **Ricci matrix** (surface bundle, eq. 3.66): the boxed formula provides
   the complete error structure for the slow interpolation.

2. **Balanced double-collar rate**: δ = (2/π⁴)ε² + O(ε⁴).

3. **Global TT obstruction**: c·ε³ ≤ C·δ + C·ε²a + Ca².

4. **Two interface costs**: the \(\operatorname{csch}^2(R/\sqrt3)\) bound
   concerns deleted hyperbolic balls; two flat cusp interfaces instead force
   \(L\ge(2/k)\operatorname{artanh}(1/k)\), \(k=\sqrt{1+\delta/3}\).

5. **Fibered area equation**: Δ_B a = 4πχ(F) + 2ℓa + a·Q̄ − a·t̄_V.

6. **Product rigidity**: integrable horizontal + Einstein → local product.

7. **Einstein ↔ full energy attainment**: on E_D, Einstein ⟺ inf∫|Rm|²=8V₀.

## 11. Research directions after absorption

**Priority 1 (sharpest):** Can Einstein nonexistence on E_D be proved?
This would immediately give the first negative-branch counterexample to
Yau 26 in dimension 4 (fixed manifold, δ→0, no Einstein of any sign).
The standard exclusion mechanisms all fail; a new argument is needed.

**Priority 2:** Global graph-manifold construction. The Koiso germ +
interface cost + Weyl concentration picture is now clear. What's missing
is matching the Koiso half-core to two flat cusp ends at small δ. The
Li-Liu PE-cusp family provides exact mixed-end models but can't directly
supply a reflection core (ASD obstruction).

**Priority 3:** The restricted IL chain is 8/8 (A01). Per-datum existence
is now established. This gives a positive gap for specified IL families
but is not a dimension-only result.

**Priority 4:** Higher dimensions. The first open KK case is n=6 with
μ₅ unknown. The manuscript does not address this.

Files: `Skills/qiushi-yau26/references/research/20260912.tex` (6558 lines).

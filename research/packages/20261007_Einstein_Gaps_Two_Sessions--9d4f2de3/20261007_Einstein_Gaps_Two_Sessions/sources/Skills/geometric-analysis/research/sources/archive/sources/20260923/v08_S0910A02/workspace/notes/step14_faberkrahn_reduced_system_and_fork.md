# Step 14: Faber–Krahn base pinning, corrected reduced system, and the χ-uniform fork

Session S0910A02, Agent2/Constructor, Execute.

## 0. Scope

This note records four discoveries from Step 14 and the resulting sharpened
fork for the four-dimensional positive-branch volume-gap question. None of
this proves or refutes P₄⁺ or Yau Problem 26.

## 1. CZ spike determinant invariance (confirmed)

In the Step 11 opposite-warping ansatz f₁ = F₁ + u, f₂ = F₂ − u with
F₁ = log sin x, F₂ = log sin y, the orbit-area density is
$$
  w = e^{f_1}e^{f_2} = e^{F_1 + F_2} = \sin x\,\sin y,
$$
**independent of u**. Verified symbolically: ∂w/∂u = 0.

Consequence: the CZ spike concentrates curvature at FIXED 4-volume. A volume-
collapsing sequence requires genuinely small p AND q simultaneously, which is a
different and harder construction than opposite warping.

Data: `workspace/data/step14_faberkrahn_corner_pinning.json` part A.

## 2. Faber–Krahn base-area lower bound

The Step 13 spectral bound λ₁ᴰⁱʳ(Ω, g_B) ≤ 2(1+δ) combined with the Faber–
Krahn inequality gives an absolute lower bound on the orbit-space area:
$$
  \operatorname{Area}(\Omega) \ge \frac{\pi j_0^2}{2(1+\delta)},
$$
where j₀ = 2.40483 is the first zero of J₀. At δ = 0 this gives Area ≥ 9.08.

**The orbit space cannot shrink.** Any invariant collapse under tight positive
pinching is purely fiber-side: all fixed 2-spheres (rods) thinning at once while
the base stays large.

Caveat: the sharp Faber–Krahn constant is for the metric g_B (not just flat R²).
The qualitative conclusion Area ≥ c(δ) > 0 holds whenever a Faber–Krahn-type
inequality is available, but the exact constant may depend on the base geometry.

Data: `workspace/data/step14_faberkrahn_corner_pinning.json` part B.

## 3. χ-uniformity requirement for Proposition A (decision-critical)

Proposition A (Step 11): a simply connected positive-pinched 4D volume gap v₀
implies a universal gap via Myers → finite π₁ → universal cover → Cheeger–Naber
finite type → Euler multiplicativity.

**If the gap is v₀(χ) → 0 as χ → ∞, Proposition A becomes circular.** The
Cheeger–Naber step bounds χ(M̃) ≤ X(δ₀, v₀), but if v₀ depends on χ, then
χ(M̃) ≤ X(δ₀, v₀(χ(M̃))) is an implicit inequality that does not bound χ(M̃).

Therefore the invariant volume gap must be **χ-uniform** to power Proposition A.
This merges the toric route with the Step 8–9 tail dichotomy: #_k(S²×S²) has
χ = 2k + 2 and is quasitoric, and the energy budget permits ~χ bubbles, so the
toric collapse question and the tail dichotomy are the same wall.

Data: `workspace/data/step14_faberkrahn_corner_pinning.json` part D.

## 4. CORRECTED base-curvature formula and complete reduced system

### 4.1. The corrected horizontal equation

For a twist-free toric metric g = g_B + p²dθ² + q²dφ², with w = pq,
v = log(p/q), the horizontal Einstein equation
$$
  \operatorname{Ric}_B - \frac{\nabla^2 p}{p} - \frac{\nabla^2 q}{q} = \lambda g_B
$$
in the (w, v) parametrization (p = √w · e^{v/2}, q = √w · e^{−v/2}) becomes:
$$
  \frac{\nabla^2 p}{p} + \frac{\nabla^2 q}{q}
  = (\log w)_{ab} + \tfrac{1}{2}\bigl[(\log w)_a(\log w)_b + v_a v_b\bigr].
$$
**Note:** the factor 1/2 on v_a v_b arises because log p = (log w + v)/2, NOT
log w/2 + v. The earlier (retracted) formula Hess(log w) = (K_B−1)g_B was based
on the incorrect identification p = √w · e^v.

### 4.2. Base curvature

Taking the trace and using Δ(log w) = −2λ − |∇log w|² gives:
$$
  \boxed{K_B = \tfrac{1}{4}\bigl(|\nabla v|^2 - |\nabla\log w|^2\bigr)
       = -\langle\nabla\log p,\,\nabla\log q\rangle.}
$$
**Verification:**
- S²×S²: p = sin x, q = sin y, flat g_B. K_B = 0. ✓
- S⁴(√3): p = √3 sinψ cosφ, q = √3 sinψ sinφ, g_B = 3(dψ²+sin²ψ dφ²).
  K_B = 1/3 (constant positive curvature of S²(√3)). ✓

The retracted formula K_B ≥ 3 was wrong; K_B can be positive or negative.

### 4.3. Complete reduced system (twist-free, polar)

For a closed simply connected toric Einstein 4-manifold with Ric = λg:

| # | Equation | Origin |
|---|----------|--------|
| 1 | −Δ_B w = 2λ w, w = 0 on ∂Ω | Vertical trace (determinant eigenvalue) |
| 2 | div_B(w ∇v) = 0, v → ±∞ at alternating rods | Vertical difference |
| 3 | (log w)_{zz} + ½[(log w)_z² + v_z²] = 0 | Traceless horizontal |
| 4 | K_B = ¼(|∇v|² − |∇log w|²) | Horizontal trace |
| 5 | ∫_Ω K_B dA = 2π − (π/2)χ | 2D Gauss–Bonnet with right-angle corners |
| 6 | Unit closure: collapsing circles have slope 1 at rods | Smooth toric topology |

Source scope: equations 1–4 are verified symbolically (Step 12 + this step).
Equation 5 requires the polygonal orbit-space structure from the sourced
toric classification (arXiv:2311.04840 lines 84–87). Equation 6 is the
standard primitive-lattice condition for smooth toric manifolds. The POLAR
(twist-free) assumption for simply connected Einstein is sourced from
arXiv:2311.04840 lines 181–210.

Data: `workspace/data/step14_corrected_reduced_system.json`,
      `workspace/data/step14_S4_KB_anchor.json`.

### 4.4. Corrected edge equation

Near a rod where p → 0 at unit slope, with base Fermi coordinates (r, s) where
g_B = dr² + a(r,s)²ds², the transverse circle profile Q(s) satisfies:
$$
  Q'' + (1 - 2K_B\big|_{\text{edge}})Q = 0,
  \qquad Q(0)=0,\ Q'(0)=1,\ Q(L)=0,\ Q'(L)=-1.
$$
For constant K_B on the edge, ω = √(1−2K_B):

| K_B at edge | ω | Rod length L | Rod flux Φ = ∫Q ds | Example |
|-------------|---|-------------|---------------------|---------|
| 1/3 | 1/√3 | √3 π ≈ 5.44 | 6 | S⁴ |
| 0 | 1 | π ≈ 3.14 | 2 | S²×S² |
| −1 | √3 | π/√3 ≈ 1.81 | 2/3 | negative-curvature edge |
| −A (A ≫ 1) | √(1+2A) | π/√(1+2A) | 2/(1+2A) → 0 | short rod |

**Negative K_B at the edge shrinks rods and reduces flux.** Since GB forces
∫K_B = 2π − (π/2)χ, which is negative for χ ≥ 5, negative base curvature must
predominate for large χ. This is the mechanism by which large-χ toric metrics
could in principle have small total rod flux and hence small volume.

## 5. The sharp fork: build or break, uniformly in χ

### 5.1. Volume = flux

The exact flux/volume identity (from −Δw = 2λw, λ = 1, divergence theorem):
$$
  2\int_\Omega w\,dA = -\int_{\partial\Omega}\partial_\nu w\,ds
  = \sum_{i=1}^m \Phi_i = \text{total rod flux}.
$$
Hence Vol₄ = 4π² ∫w = 2π² × (total flux).

### 5.2. Bishop ceiling forces average flux → 0

Bishop: Vol₄ ≤ 24π²/(1−δ)². So total flux ≤ 12/(1−δ)².
With m = χ rods: **average flux ≤ 12/(χ(1−δ)²) → 0 as χ → ∞.**

This is NOT a contradiction — it just means that for large χ, most rods must
have small flux. The question is whether the TOTAL flux can also go to zero.

### 5.3. The fork

**BUILD (gap exists χ-uniformly):** Prove that equations 1–6 with Faber–Krahn
(Area ≥ c) and unit closure force total flux ≥ c₀ > 0 independently of χ. The
key constraint is the **traceless condition (eq 3)**, which couples the shape of
w to the ratio v and may prevent the negative-K_B mechanism from simultaneously
shrinking all rods while maintaining the eigenvalue equation.

**BREAK (gap fails for large χ):** Construct a sequence of toric reduced data on
polygons with m → ∞ corners, all rods short (Φᵢ → 0), total flux → 0, while
satisfying equations 1–6 and Faber–Krahn. The key difficulty is that the CZ spike
(opposite warping) preserves w and CANNOT break volume; a genuine collapse needs
small p AND q everywhere, not just concentration of Hessian.

### 5.4. Corner pinning argument (incomplete)

At each T²-fixed point, the local model is R⁴ with w = s₁s₂, rising at unit
rate in both directions. The corner integral ∫_{B_R ∩ quarter-plane} w dA = R⁴/8.
A corner contributes negligible volume only if both adjacent edges are short.

If the traceless condition forces at least one "long" rod to thread through the
polygon (connecting two distant corners), its flux could provide the uniform lower
bound. But this is not proved. The traceless condition is a nonlinear conformal
PDE in (log w, v), and its global implications for the polygon geometry are
genuinely open.

## 6. Connection to peer routes

A03's L² propagation mechanism (msg #263) claims: Ye Li smoothing + L² Einstein
defect evolution + Sobolev absorption gives a smoothed metric that is simultaneously
bounded-curvature and nearly-Einstein on the calibrated good set. If correct, this
provides an ALTERNATIVE route to the positive-branch conclusion, bypassing the
toric reduction. The key remaining gap is localizing Li's all-centers theorem.
This should be independently verified.

A01's rank-one reduction (msg #261) has been corrected: the static/rank-one
closure was withdrawn, but the normalized equations remain valid after smoothing.

## 7. Status

The toric determinant route has been sharpened to a precise 2D question about
the complete reduced system (eqs 1–6). The corrected formulas, verified on two
independent anchors (S²×S² and S⁴), establish the mathematical framework. The
fork (build vs break) is symmetric and sharp; resolving it would either prove
the invariant volume gap (powering Proposition A toward P₄⁺) or locate the
invariant counterexample (making Proposition A vacuous).

## 8. Uniform-K_B stabilization (new discovery)

Under the idealization that K_B is constant on all edges (with the value
fixed by Gauss–Bonnet: K_B = (2π − πχ/2)/Area), the total flux is:
$$
  \text{total flux} = \chi \cdot \frac{2}{1 - 2K_B}
  = \chi \cdot \frac{2\,\text{Area}}{\text{Area} + \pi\chi - 4\pi}.
$$
For large χ: the denominator ~ πχ, so **total flux → 2·Area/π**, independent
of χ. With Faber–Krahn Area ≥ πj₀²/2 ≈ 9.08:

$$
  \boxed{\text{total flux} \ge \frac{2\cdot\pi j_0^2/2}{\pi} = j_0^2 \approx 5.78,
  \qquad \operatorname{Vol}_4 \ge 2\pi^2 j_0^2 \approx 114.}
$$

The mechanism: each rod shrinks by factor ~1/χ (because ω² ~ πχ/Area), but
there are χ rods, and the product stabilizes. This is a **χ-uniform** lower
bound under the uniform-K_B assumption.

**Critical caveat:** this assumes K_B is the SAME constant on all edges. In
reality, K_B varies across the polygon, and the traceless condition constrains
this variation. The question is whether dramatically nonuniform K_B (very
negative at some rods, positive at others) can beat the uniform bound. Under
the full reduced system, K_B at each rod equals −a₂ = −(−K_B|_edge), and the
global system couples all rods through the interior eigenfunction and ratio
equations.

Data: `workspace/data/step14_chi_uniform_flux_test.json`.

## 9. Updated status

The fork **tilts toward BUILD** under the uniform-K_B idealization. The genuine
remaining question is whether the traceless conformal condition (eq 3) allows or
prevents dramatic K_B nonuniformity at the rod edges. A rigorous proof would
show that the traceless condition, combined with the eigenvalue equation and unit
closure, constrains K_B at each edge to be within a bounded factor of the GB
average. A constructive counterexample would show that the traceless condition
admits solutions where K_B is much more negative at some edges than the average,
allowing those rods to carry negligible flux while the total flux still drops.

**The most decisive next computation** is either:
1. A rigorous proof that the traceless condition prevents dramatic K_B
   nonuniformity (e.g., via a maximum principle or gradient estimate for K_B
   restricted to the boundary), or
2. A numerical FEM solution of the reduced system on polygons with m = 6, 8, 10
   corners to test whether small-total-flux solutions exist with dramatically
   nonuniform edge K_B.

---

### Files produced this step

| File | Content |
|------|---------|
| `scripts/step14_faberkrahn_corner_pinning.py` | CZ invariance, Faber–Krahn, corner integral, χ-uniformity |
| `scripts/step14_intw_lower_bound_crux.py` | Flux identity, unit closure, rod-flux scaling |
| `scripts/step14_rodflux_crux_analysis.py` | Horizontal equation derivation, K_B correction, S²×S² checks |
| `scripts/step14_corrected_reduced_system.py` | Complete system in (w,v), symbolic verification |
| `scripts/step14_S4_KB_anchor.py` | S⁴ anchor verification |
| `data/step14_faberkrahn_corner_pinning.json` | Faber–Krahn constants and CZ determinant invariance |
| `data/step14_intw_lower_bound_crux.json` | Flux/volume identity and unit closure analysis |
| `data/step14_rodflux_crux_analysis.json` | K_B derivation and correction chain |
| `data/step14_corrected_reduced_system.json` | Full system verification on S²×S² |
| `data/step14_S4_KB_anchor.json` | K_B = 1/3 on S⁴ orbit space |
| `scripts/step14_chi_uniform_flux_test.py` | Uniform-K_B stabilization test |
| `data/step14_chi_uniform_flux_test.json` | Total flux → 2A/π as χ → ∞ |

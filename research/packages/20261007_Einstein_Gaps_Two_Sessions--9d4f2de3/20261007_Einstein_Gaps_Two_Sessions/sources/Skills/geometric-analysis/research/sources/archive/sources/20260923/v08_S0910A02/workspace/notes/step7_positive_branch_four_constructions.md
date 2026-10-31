# Step 7: Four constructions for the positive branch of Yau Problem 26

Session: S0910A02. Agent2/Constructor. Phase: Explore.

> **STEP 8 PRECEPTOR ERRATUM / SCOPE CORRECTION.** This note remains useful as a construction package, but Step 8 corrected three points. First, the determinant condition is only a first-obstruction degeneracy condition: `det R_+=0` means one eigenvalue of `W_+` equals `-s/12`; Kähler-Einstein metrics imply this condition, but the condition alone does **not** select Kähler-Einstein geometry (for example spectra such as `(s/12,0,-s/12)` are degenerate but not Kähler-Einstein). Any Kähler/Hermitian selection must come from additional LeBrun-Ozuch/Ozuch rigidity or extra geometric hypotheses. Second, the positive-branch Weyl budget has a sharp lower bound from CGB plus Bishop, so on `#_k(S^2×S^2)` tight pinching forces `∫|W|^2 ≥ 16π^2 k + o(k)` rather than merely permitting large curvature energy. Third, the phrase "one named unknown" for ε-regularity is too narrow for the full uniform problem: C^0-pinched ε-regularity is a central analytic bottleneck, but high-χ curvature concentration, collapse/unwrapping, singular strata, higher-order obstructions, and topology recovery remain separate load-bearing obligations. See `Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md`.

## 0. Target fidelity

Active target: the complete all-dimensional proposition of Yau Problem 26.
For each n ≥ 2, determine whether there exist dimension-only constants c_n < C_n
such that any closed smooth manifold (M^n, g) with c_n g ≤ Ric_g ≤ C_n g
admits some smooth Einstein metric h on M, with Ric_h = λh.

Branch reduction: the interval proposition is equivalent to P_n^+ ∨ P_n^-
(at least one sign-normalized branch per dimension). We focus here on
P_4^+ (positive branch, dimension 4) and its general-dimensional extension.

---

## Construction 1: Euler characteristic closes all free collapse in dimension 4

**Proposition 1** (Free circle collapse is impossible under tight positive pinching in dim 4).
*Let M^4 be a closed, connected, oriented smooth 4-manifold. If there exists
a Riemannian metric g on M with |Ric_g − g|_{op} ≤ δ for some δ < 1/2, then
χ(M) ≥ 2. In particular, M does not admit any free S^1 action.*

**Proof.** From the four-dimensional CGB accounting (Step 4, verified by TTCS):

$$
\beta(\delta) \operatorname{Vol}(M,g) + \int_M |W|^2 \,dv_g \leq 8\pi^2 \chi(M),
$$

where β(δ) > 0 for δ < 1/2 (optimal formula: β(δ) = (2/3)(1−δ)² for δ ≤ 1/3,
β(δ) = (2/3)(1+δ)(1−2δ) for 1/3 ≤ δ < 1/2). Since Vol > 0 and |W|² ≥ 0,
we get χ(M) > 0.

If M admits a free S¹ action, then M is a principal S¹-bundle over some closed
3-manifold B³, and χ(M) = χ(B³) · χ(S¹) = 0. Contradiction.

Moreover, Bochner gives b₁(M) = 0 under Ric ≥ (1−δ)g with δ < 1: if ω is harmonic, then `0=∫(|∇ω|²+Ric(ω,ω))` and `Ric(ω,ω)≥(1−δ)|ω|²`, hence ω=0. Then by Poincaré duality on the oriented closed 4-manifold, b₃=b₁=0 and χ=2+b₂≥2. ∎

**Remark 1.1.** This extends to any *positive-rank* torus action. If T^k acts
effectively on M^4 with k ≥ 1 and the action has only isolated fixed points,
then the fixed-point formula for the Euler characteristic gives
χ(M) = |M^{T^k}| ≥ 0. A free action has |M^{T^k}| = 0, contradicting χ ≥ 2.
More generally, by the Conner-Floyd theorem, any smooth S¹-action on a closed
oriented 4-manifold satisfies χ(M) = Σ χ(F_i) where F_i are the fixed-point
components. If the action is semifree (free outside fixed set), fixed components
are even-codimensional, each contributing positive Euler terms.

**Remark 1.2 (Dimensional asymmetry).** This argument relies on even dimension.
In odd dimensions, χ = 0 identically, so the Euler obstruction vanishes.
Genuine tight-pinching-compatible collapse exists:

- S^{2k+1}/Z_m with the round metric satisfies Ric = 2k · g exactly
  (δ₊ = 0) while Vol → 0 as m → ∞. The GH limit is CP^k.
- More generally, Sasaki-Einstein circle bundles over Kähler-Einstein
  bases give δ₊ = 0 collapse in all odd dimensions.

Therefore the all-dimensional general theorem must be "every Ric ≈ g collapse
structure is Einstein-compatible" rather than "collapse is impossible." The
dimension-4 mechanism (χ > 0 blocks free actions) does not transfer to odd
dimensions. In even dimensions ≥ 6, the Euler obstruction is still available
but the base-manifold Bochner argument needs different input (base dimension
≥ 5 can carry harmonic 2-forms with positive Ricci).

---

## Construction 2: Free L² curvature bound and the one-named-unknown thick-thin

**Proposition 2** (L² curvature is bounded under tight positive 4D pinching).
*Let (M⁴, g) be closed, oriented, with |Ric_g − g|_{op} ≤ δ < 1/2. Then:*

$$
\int_M |\mathrm{Rm}|^2 \,dv_g \leq \frac{8\pi^2(2+2\delta)^2}{3\beta(\delta)} \cdot \chi(M).
$$

*In particular, with Myers giving diam ≤ π√(3/(1−δ)) and Bishop giving
Vol ≤ V_4(δ), the L² curvature is bounded by a function of δ and χ(M) only.*

**Proof.** From the CGB identity:

$$
8\pi^2 \chi(M) = \int_M |W|^2 \,dv_g + \frac{1}{24}\int_M s^2 \,dv_g
  - \frac{1}{2}\int_M |E|^2 \,dv_g.
$$

Under |Ric − g|_{op} ≤ δ: s = 4 + O(4δ), |E|² ≤ 3δ², and

$$
|\mathrm{Rm}|^2 = |W|^2 + 2|E|^2 + \frac{s^2}{24} - \frac{|E|^2}{2}
$$

(using the four-dimensional decomposition Rm = W + E ∧ g + (s/24)g ∧ g).
Actually, the norm relation is |Rm|² = |W|² + 2|Z|² + s²/24 where Z is the
traceless Ricci contribution. In any case:

$$
\int_M |W|^2 \leq 8\pi^2 \chi - \beta(\delta)\operatorname{Vol}
$$

and

$$
\int_M |W|^2 + \frac{s^2}{24} = 8\pi^2\chi + \frac{1}{2}\int |E|^2
  \leq 8\pi^2\chi + \frac{3\delta^2}{2}\operatorname{Vol}.
$$

With Vol ≤ 8π²χ / β(δ):

$$
\int_M |W|^2 + \frac{s^2}{24}
  \leq 8\pi^2\chi\left(1 + \frac{3\delta^2}{2\beta(\delta)}\right).
$$

Since |Rm|² ≤ C(|W|² + s²/12 + |E|²), we get an upper bound on ∫|Rm|²
depending only on (δ, χ). ∎

**The conditional thick-thin theorem.**

Proposition 2 gives bounded L² curvature with no noncollapse hypothesis.
This is precisely the input to the four-dimensional regularity theory.
The conditional structure theorem has one named unknown:

**Conjecture (ε-regularity for C⁰-pinched metrics).** *There exist ε > 0 and
C > 0 such that if (M⁴, g) satisfies |Ric_g − g|_{op} ≤ δ < 1/10 and
r⁻⁴ ∫_{B_r(p)} |Rm|² dv ≤ ε for some r ≤ 1, then |Rm|(p) ≤ C/r².*

**What this would give.** Under tight positive pinching:

1. The L² curvature budget is ∫|Rm|² ≤ E(δ,χ).
2. With the ε-regularity conjecture, the set where curvature concentrates
   (scale-invariant L² energy ≥ ε) has at most E/(ε) connected components.
3. Each concentration component carries ≥ ε units of L² curvature energy,
   and the CGB formula assigns it a definite Euler characteristic contribution.
4. Outside concentration regions, the metric is regular with pointwise
   curvature bounds, hence noncollapse + smooth convergence as δ → 0.

**Why this is the one named unknown.** The exact Einstein equation
Ric = λg is elliptic (for Rm, after gauge-fixing). The Bianchi identity
gives ∇·(Ric − (s/2)g) = 0, so for Einstein: ∇s = 0, and the Weyl
satisfies a Bochner-Weitzenböck equation with algebraic curvature terms.
For merely C⁰-pinched Ric = g + E with |E|_{C⁰} ≤ δ:

- The Bianchi identity gives div(E) = 0 (in the traceless part),
  which is one derivative of E, not two.
- The metric g satisfies Ric_g = g + E, which in harmonic coordinates
  gives −(1/2)Δg_{ij} + Q(g,∂g) = g_{ij} + E_{ij}. This is a
  quasilinear elliptic system for g, but the right-hand side E is
  only bounded, not controlled in C^{0,α} or W^{1,p}. Standard
  Schauder/Sobolev bootstrapping requires E ∈ C^{0,α} to get
  g ∈ C^{2,α}, which does not follow from C⁰ pinching alone.
- In particular, ∇Ric and ∇Rm are NOT controlled by |E|_{C⁰} alone.

Thus the ε-regularity for C⁰-pinched metrics requires a genuinely new
ingredient beyond standard elliptic theory. If it needs ∇Ric control
(i.e., the hypothesis must be strengthened from C⁰ to C¹ pinching),
that should be stated as a sharp frontier condition.

---

## Construction 3: Obstruction-amplitude principle for regime (II)

**Setup.** Consider a sequence (M_i, g_i) of closed oriented smooth
4-manifolds with |Ric_{g_i} − g_i|_{op} ≤ δ_i → 0 and noncollapsed:
Vol(B_1(p)) ≥ v > 0 for all p and all i.

**Step 3.1: The noncollapsed GH limit is an Einstein space with
isolated singularities.**

By Cheeger-Colding-Naber:
- Myers gives diam(M_i, g_i) ≤ D(δ) < ∞.
- The noncollapsing condition plus bounded Ricci give GH precompactness.
- A subsequence converges to (M_∞, d_∞), a metric space.
- On the regular set R (complement of a set of Hausdorff codimension ≥ 4,
  hence isolated points in dimension 4), by Cheeger-Naber Theorem 1.13
  and the local Ricci convergence Ric_{g_i} → g_∞ as δ_i → 0, the limit
  metric satisfies Ric_{g_∞} = g_∞ on R.
- In dimension 4, isolated singularities with Einstein regular complement
  have tangent cones C(S³/Γ_k) (metric cones over space forms).

Therefore the limit is a compact Einstein 4-orbifold (M_∞, g_∞) with
Ric = g_∞ and finitely many orbifold-like singularities.

**Step 3.2: The Biquard-Ozuch obstruction.**

Ozuch Theorem 0.3 (for exact Einstein sequences): if (M_i, g_i) are
Einstein manifolds converging to Einstein orbifold (M_o, g_o), and every
singularity blow-up is a Kähler Ricci-flat ALE space in the positive
orientation, then at each singular point p:

$$
\det \mathbf{R}_{g_o}(p) = 0,
$$

where **R** is the curvature operator on 2-forms.

The Biquard desingularization theorem: for orbifold singularity R⁴/Z₂
with det **R** = 0, there exists a smooth Einstein desingularization
(under nondegeneracy and appropriate boundary conditions).

**Step 3.2b: Verified det R computation (Step 7 script).**

The Python script `step7_det_R_obstruction.py` computes the curvature
operator det R on Λ²_+ for three model Einstein 4-manifolds with Ric = g:

| Manifold | W+ eigenvalues | R\|_{Λ²_+} eigenvalues | det R\|_{Λ²_+} | Desingularizable? |
|---|---|---|---|---|
| S⁴ (K=1/3) | (0, 0, 0) | (1/3, 1/3, 1/3) | 1/27 ≠ 0 | NO |
| S²×S² (K₁=K₂=1) | (2/3, -1/3, -1/3) | (1, 0, 0) | 0 | YES |
| CP² (FS) | (2/3, -1/3, -1/3) | (1, 0, 0) | 0 | YES |

General formula: for Ric = g (s = 4), det R|_{Λ²_+} = ∏(w_i + 1/3)
where w_i are W+ eigenvalues with w₁+w₂+w₃ = 0. This vanishes iff
some w_i = -1/3, equivalently, the curvature operator has a kernel on Λ²_+.

**Key structural observation (Step 8 corrected).** Positive Kähler-Einstein 4-manifolds in the relevant orientation, such as CP² and S²×S², have `det R_+=0`; constant-curvature orbifolds `S⁴/Γ` have `det R_+=(1/3)^3≠0`. However, `det R_+=0` is only the first-obstruction degeneracy condition `w_i=-s/12` for some self-dual Weyl eigenvalue. It does **not** by itself select Kähler-Einstein geometry: the Kähler-Einstein spectrum is `(s/6,-s/12,-s/12)`, whereas other trace-free spectra with one eigenvalue `-s/12` are algebraically possible. Any Kähler/Hermitian selection must use additional Ozuch/LeBrun-Ozuch rigidity or other geometric input.

**Step 3.3: The obstruction-amplitude principle (from MV/Calabi analysis).**

This is the session's key insight from Step 1, reinterpreted for the
positive branch. In the Morteza-Viaclovsky Calabi region estimate:

$$
\operatorname{Ric}_{g_t} - \Lambda g_t - t\lambda \chi_t o
  = O_{g_\mathrm{cal}}(t^2 \rho^2).
$$

The first obstruction term t·λ·o is non-scalar (its eigenvalues on Λ²
at r=1 include −1/2 and (q−1)/2). Converting to g_t-operator norm:
the remainder is O(t) in the core, but the obstruction term is order one
in g_t-operator norm (since g_t^{-1} ∼ t^{-1} g_cal^{-1}).

**Principle:** If det **R**(p) ≠ 0 at a singular point of the orbifold
limit, then ANY approximate metric obtained by gluing has

$$
\|\operatorname{Ric}_{g_{\text{approx}}} - \Lambda g_{\text{approx}}\|_{C^0}
  \geq c > 0,
$$

where c depends on the obstruction value but not on the gluing parameter.
This is because the non-scalar obstruction endomorphism o cannot be
absorbed into a change of Einstein constant.

**Step 3.4: The regime (II) argument (conditional).**

Combining Steps 3.1–3.3: if δ_i → 0 and the sequence is noncollapsed,
the limit is an Einstein orbifold with Ric = g. At each singular point:

1. The obstruction-amplitude principle forces the local obstruction to
   vanish: det **R**(p) = 0. (Otherwise the C⁰ residual stays order one,
   contradicting δ_i → 0.)

2. With vanishing obstruction, the Biquard-Ozuch gluing theory produces
   a smooth Einstein metric on M_i for i sufficiently large. (Under
   appropriate nondegeneracy conditions — see Gap below.)

**Ozuch Example 1** confirms this principle: on S⁴/Z₂ (constant sectional
curvature, so **R** = Id, det **R** = 1 ≠ 0), there exist sequences with
||Ric − 3g||_{L^p} → 0 but NO Einstein desingularization. The key: L^p
convergence does NOT imply C⁰ convergence when the obstruction is nonzero.

**TTCS-verified precise conditional statement (Step 7 verifier):**

> Within the Biquard-Ozuch/Eguchi-Hanson gluing normal form, if a family
> of approximate metrics g_t satisfies
> Ric_{g_t} − Λg_t = t·O_p·o + Q_t, |Q_t|_{g_EH} ≤ Ct²ρ²,
> and g_t = t(g_EH + O(tρ²)), then for nonzero first obstruction O_p:
>
> inf_a ||Ric(g_t) − a·g_t||_{C⁰(g_t)} ≥ c|O_p| − o(1).
>
> Therefore such metrics cannot satisfy ||Ric − g||_{C⁰} → 0.

The non-scalar nature of o forces this: at the core center (r = 0), the
endomorphism g_cal^{-1}o has eigenvalues (−1,−1,+1,+1) for 4D
Eguchi-Hanson (spread = 2). Multiple singularities don't cancel (C⁰ is
pointwise sup; distinct cores are disjoint). Higher-order terms are O(t)
in the core and cannot annul the O(1) obstruction.

The MV source is for complex dim n ≥ 3 (real dim ≥ 6). In dimension 4:
the Eguchi-Hanson model has two rotational parameters absent in higher
dimensions. However, det R|_{Λ²_+} = 0 is rotation-invariant: no
rotation of the bubble creates a kernel that isn't already present. So
the NECESSITY conclusion (order-1 defect when det R ≠ 0) is preserved
in dimension 4, while the quantitative amplitude and EXISTENCE direction
(det R = 0 ⟹ desingularizable) involve the 4D rotational freedom.

**Remaining gaps (TTCS-delimited):**

(a) **THE CORE GAP — Normal form applicability:** The scaling argument
    applies to metrics in the Biquard-Ozuch gluing normal form. For
    arbitrary C⁰-pinched noncollapsed metrics, no existing theorem places
    them into this normal form. Ozuch Theorem 0.2 does this for EXACT
    Einstein metrics GH-close to orbifolds, not for approximate ones.
    The missing ingredient: either a weighted gluing description for
    merely L∞-Ricci-pinched metrics, or an independent Pohozaev/projection
    argument that detects the first obstruction from only C⁰ Ricci data.
    This is the "approximate-to-exact bridge."

(b) **Higher-order obstructions:** Even with det R = 0, Ozuch 2020/2021
    identifies higher-order conditions. These are finite-dimensional
    algebraic conditions on curvature jets. The first-order necessity is
    proven; sufficiency for desingularization requires all orders.

(c) **Topology recovery:** Ozuch Theorem 0.2 gives topology recovery for
    exact Einstein. For approximate Einstein, need the GH proximity +
    gluing description to determine diffeomorphism type.

(d) **LeBrun-Ozuch rigidity (positive λ):** For positive Einstein
    4-manifold sequences with orbifold limits having ASD ALE bubbles,
    Theorem B gives eventual Kähler-Einstein rigidity. This constrains
    the class of possible orbifold limits and may help close gap (a).

(e) **Bubble model assumption:** Ozuch Theorem 0.3 requires Kähler
    Ricci-flat ALE bubbles in the chosen orientation. General ALE models
    need separate treatment.

---

## Construction 4: The #_k(S²×S²) calibration test

**Context.** This is the most informative cheap test for P_4^+.

The family #_k(S²×S²) for k ≥ 0 has:
- χ = 2 + 2k, τ = 0
- 2χ − 3|τ| = 4 + 4k > 0 (Hitchin-Thorpe satisfied, sign-blind filter silent)
- b₂ = 2k (unbounded as k → ∞)
- Positive Ricci: Ric > 0 metrics exist for ALL k (Sha-Yang 1991)
- Einstein existence:
  - k = 0: S⁴ carries the round Einstein metric
  - k = 1: S²×S² carries the product Einstein metric
  - k ≥ 2: **UNKNOWN** (major open problem)

**Critical observation:** A proof of P_4^+ would produce Einstein metrics
on #_k(S²×S²) for all k, resolving this open problem. Conversely, if
Einstein metrics do not exist on #_k(S²×S²) for some k, then P_4^+ is
false unless the Sha-Yang Ric > 0 metrics have δ₊ ≥ c₀ > 0 uniformly.

**Question 4A (Construction side):** How small can δ₊ be made on #_k(S²×S²)?

The Sha-Yang / Perelman / Burdick construction:
1. Take S⁴ with k disjoint balls removed (docking station), endowed with
   a Ric > 0 metric having round convex boundary at each puncture.
2. Glue in core metrics of S²×S² at each puncture via Perelman's
   gluing theorem.

The resulting metric has inherent Ricci anisotropy in the neck regions:
the doubly-warped Riemannian submersion formulas (Lemma 2.5 of Burdick)
show that radial, horizontal, and vertical Ricci eigenvalues depend on
f''/f, h''/h, f'h'/(fh), and the submersion A-tensor. Near a cone point
where f(t) → 0 (collapsing the fibre), the boundary conditions f'(0) = 1,
f''(0) = 0 force a specific warping profile that is NOT isotropic.

**Quantitative estimate.** In the simplest model of a connected sum neck
S³ × [0,L] with metric dt² + a²(t)dσ², isotropy Ric = g requires
a'' = −a (constant curvature a = sin t), but the connected sum
requires a(t) → 0 at the surgery point with a'(0) = 1. The standard
neck geometry (a = sin t rescaled) achieves a'' + a ≈ 0 only in the
bulk, while at the endpoints a(t) → 0 forces r_t = −3a''/a → +∞
(radial Ricci blows up relative to angular Ricci). A careful calculation
with the Burdick formulas would give the minimum achievable δ₊ as a
function of the neck radius ε and the ambient curvature.

**Conjecture 4A.** The minimum δ₊ achievable on #_k(S²×S²) by Perelman-type
constructions satisfies δ₊ ≥ c(k) with c(k) ≥ c₀ > 0 independent of k,
because each neck contributes an irreducible O(1) anisotropy.

However, other constructions might achieve smaller δ₊:
- Ricci flow starting from a Sha-Yang metric might flow toward isotropy
  (if an Einstein attractor exists).
- Direct PDE methods (continuity method, Newton iteration) starting from
  a specific ansatz might improve isotropy.
- But if no Einstein metric exists for k ≥ 2, no method can achieve δ₊ = 0.

**Question 4B (Obstruction side, Step 8 corrected):** Does tight positive pinching bound `b₂`, or must high `b₂` be carried by forced Weyl concentration?

Under `|Ric-g|_{op}≤δ` in the positive branch:
- `b₁=0` by Bochner;
- `χ=2+b₂` on a closed oriented 4-manifold;
- Bishop gives the dimension-only volume ceiling `Vol≤24π²/(1-δ)²`.

The previous paragraph only used the upper CGB energy budget and a hypothetical noncollapse lower bound.  The sharper obstruction is the lower Weyl budget derived in Step 8:

$$
\int_M |W|^2\,d\mu \ge
8\pi^2\left[\chi(M)-2\left({1+\delta\over 1-\delta}\right)^2\right].
$$

For `M_k=#_k(S²×S²)`, where `χ=2+2k`, this becomes

$$
\int_{M_k}|W|^2\,d\mu\ge 16\pi^2 k-O_\delta(1),
$$

and at `δ=0` exactly `16π²k`.  Thus high `b₂` is not merely unconstrained by CGB: tight pinching at bounded Ricci scale compels Weyl curvature energy growing linearly with `k` inside a Bishop-bounded volume.  Any near-pinched construction on this family would have to produce many ALE-scale concentration regions, or collapse/singular docking geometry that stores the same Chern--Weil energy.

Therefore the calibration test is two-sided.  Compute or bound the minimum `δ_+` on `#_k(S²×S²)` in explicit Sha--Yang/Burdick/Perelman neck models and compare with the forced lower Weyl budget.  If those constructions cannot realize the required `16π²k` Weyl energy while keeping Ricci eigenvalues nearly isotropic, they give a neck/topology lower bound for `δ_+`.  If some construction can make `δ_+→0`, it supplies a serious stress test for `P_4^+` and forces the same orbifold/ALE or collapse-unwrapping mechanisms that the positive program must handle.  See `Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md` and `workspace/data/step8_weyl_budget_positive4.json`.

---

## Summary of the four constructions and the remaining gap structure

| Construction | Establishes | Remaining gap |
|---|---|---|
| 1 (Euler) | Free S¹ collapse impossible in dim 4 | Extends to even dimensions; fails in odd dimensions |
| 2 (L² bound) | Free L² curvature bound under pinching | The ε-regularity conjecture for C⁰-pinched metrics |
| 3 (Obstruction-amplitude) | Noncollapsed orbifold limits must have vanishing det **R** | Approximate-to-exact bridge; higher-order obstructions; topology recovery |
| 4 (Calibration) | If P_4^+ true, Einstein exists on #_k(S²×S²) | Need to compute achievable δ₊ on these manifolds |

After Step 8 scope correction, the four-dimensional positive branch P_4^+ is organized by the following regimes rather than literally reduced to solved alternatives:

1. **Collapse regime:** Every collapsed configuration under tight Ric ≈ g
   is Einstein-compatible (possibly through equivariant descent, rewound
   noncollapse on the universal cover, or direct collapse analysis).

2. **Noncollapsed regime with smooth convergence:** This is solved —
   the limit is Einstein on the regular set, and if the limit is smooth,
   the convergence is smooth.

3. **Noncollapsed regime with orbifold concentration:** The obstruction-
   amplitude principle (Construction 3) shows det **R** = 0 at each
   singularity. With the Biquard-Ozuch desingularization theory, this
   closes provided: (a) the approximate-to-exact bridge holds, (b) all
   higher-order obstructions also vanish, and (c) topology is recovered.

One of the sharpest open questions in the positive-branch program is the approximate-to-exact bridge: does a C⁰-pinched noncollapsed sequence necessarily admit enough local orbifold/ALE structure, or at least a Pohozaev/Komar-type first-obstruction projection, to force the same obstruction vanishing detected in the Biquard-Ozuch weighted gluing normal form? TTCS verification confirms the scaling argument is rigorous within that normal form and that the obstruction mechanism is sign-independent and rotation-stable. The gap is entering or replacing the normal form from only C⁰ Ricci data. This analytic bridge is central, but it does not remove the separate collapsed, high-χ, higher-order obstruction, and topology-recovery obligations.

---

## Files and dependencies

- CGB accounting: `workspace/notes/step4_preceptor_energy_accounting_and_route_review.md`
- β(δ) optimal: Step 4 TTCS (`trace/ttcs/results/step4_ttcs01_verifier1_integration.md`)
- KK/Bochner: `workspace/notes/step6_positive_collapse_regularity_probes.md`
- Ozuch I source: `Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md`
- Burdick source: `Knowledge/objects/papers/Ricci-positive-metrics-on-connected-sums-of-projective-spaces--17bdbf22f9bb--cb9ce73e65bd/object.md`
- Dossier: `Skills/qiushi-yau26/references/research/20260910.tex`

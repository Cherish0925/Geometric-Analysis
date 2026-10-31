# Step 17: Exact separated rigidity, general T^k identity, and route assessment

Session S0910A02, Agent2/Constructor, Execute.

## 0. Scope

This note records three results and an honest route assessment:

1. **Theorem 1 (Separated Einstein Rigidity):** Exact Einstein metrics with
   cohomogeneity-one S^1 × SO(3) symmetry and two S^2 bolts must be
   S^2(1) × S^2(1).

2. **Theorem 2 (General T^k Spectral Identity):** For any twist-free
   diagonal T^k-invariant metric on M^{k+m}, tr_h Ric^V = −Δ_B w/w where
   w = √(det h). Verified symbolically for k = 1,...,5 on m = 2 base.
   Consequences in all dimensions.

3. **Conditional Theorem 3 (Pinched separated volume gap):** If the ODE
   matching stability can be established, then δ-pinched smooth separated
   metrics have Volume ≥ 16π² − Cδ.

4. **Route assessment:** Three open bridges from the invariant program to
   Yau-26, with honest evaluation of each.

None of this proves or refutes Yau Problem 26.

## 1. Exact Separated Einstein Rigidity

### Statement

**Theorem 1.** Let (M⁴, g) be a closed smooth Riemannian four-manifold with
Ric_g = g admitting an isometric cohomogeneity-one S^1 × SO(3) action with
principal orbit S^1 × S^2 and two singular orbits, each an embedded S^2 (bolts).
Then (M, g) is isometric to S²(1) × S²(1) with the round product metric
(Vol = 16π²).

### Proof

**Step 1: ODE reduction.** The metric in adapted coordinates is
$$
g = dr^2 + p(r)^2 d\theta^2 + a(r)^2 g_{S^2(\kappa)},
$$
where r ∈ [0, r_*], θ ∈ [0, 2π), and g_{S^2(κ)} is the round metric on S² with
Gaussian curvature κ > 0 (to be determined). Smooth bolt closure requires:

- r = 0: p(0) = 0, p'(0) = 1, a(0) = 1, a'(0) = 0.
- r = r_*: p(r_*) = 0, |p'(r_*)| = 1, a(r_*) > 0, a'(r_*) = 0.

We normalize a(0) = 1 and absorb the bolt-radius dependence into κ.

**Step 2: Einstein equations.** Ric = g in the orthonormal frame gives:
$$
\text{(rr):}\quad -p''/p - 2a''/a = 1,
$$
$$
\text{(θθ):}\quad -p''/p - 2a'p'/(ap) = 1,
$$
$$
\text{(ψψ):}\quad -a''/a - a'p'/(ap) - (a')^2/a^2 + \kappa/a^2 = 1.
$$

From (rr) − (θθ): a''p = a'p', hence d(a'/p)/dr = 0, so a' = Ap for a constant
A = a''(0) ≥ 0. Evaluating (ψψ) at r = 0: −2A + κ = 1, hence κ = 1 + 2A.

**Step 3: First integral.** Substituting a' = Ap into (ψψ):
$$
2aa'' + (a')^2 = \kappa - a^2.
$$
Multiplying by a' and integrating from 0 (where a = 1, a' = 0):
$$
a(a')^2 = \kappa(a - 1) - \frac{a^3 - 1}{3}.
$$
(Verified symbolically, Step 17 script.)

**Step 4: Second bolt value.** At r = r_*, a' = 0, so
$$
\kappa(a_+ - 1) = \frac{a_+^3 - 1}{3} = \frac{(a_+ - 1)(a_+^2 + a_+ + 1)}{3}.
$$
For a_+ ≠ 1: κ = (a_+² + a_+ + 1)/3, i.e., a_+² + a_+ + 1 = 3 + 6A, giving
$$
a_+ = \frac{-1 + \sqrt{9 + 24A}}{2}.
$$
(Verified: a_+(0) = 1, a_+ → √(6A) as A → ∞.)

**Step 5: Second bolt slope.** From the ODE at r = r_*:
$$
a''(r_*) = \frac{\kappa - a_+^2}{2a_+}, \qquad
p'(r_*) = \frac{a''(r_*)}{A} = \frac{\kappa - a_+^2}{2Aa_+}.
$$
The absolute slope (cone angle / 2π) is
$$
\mu = |p'(r_*)| = \frac{2a_+ + 1}{a_+(a_+ + 2)}.
$$
(Equivalence of the two expressions verified symbolically in Step 16.)

**Step 6: Rigidity.** Smooth closure at both bolts requires μ = 1:
$$
2a_+ + 1 = a_+(a_+ + 2) = a_+^2 + 2a_+ \quad\Longrightarrow\quad a_+^2 = 1 \quad\Longrightarrow\quad a_+ = 1.
$$
Then A = 0, κ = 1, a(r) ≡ 1, and p'' + p = 0 with p(0) = 0, p'(0) = 1 gives
p(r) = sin r on [0, π]. The metric is
$$
g = dr^2 + \sin^2\!r\, d\theta^2 + g_{S^2(1)}
$$
which is S²(1) × S²(1) with Vol = 16π². □

### SdS dictionary (Step 16)

This theorem is equivalent to the classical statement that Euclidean
Schwarzschild–de Sitter with Λ > 0 cannot simultaneously smooth both horizons:
the surface gravity ratio μ = κ_c / κ_h ≠ 1 for any M > 0. The A = 0 limit is
the Nariai metric S² × S². Source support: Knowledge objects on SdS thermodynamics,
uniqueness, and Euclidean action.

### Linearization

$$
\mu(A) = 1 - \frac{4}{3}A + O(A^2),
$$
so any nonzero A produces a definite cone-angle defect. This nondegeneracy
is the basis for the pinched stability theorem below.

Data: `workspace/data/step17_separated_rigidity_proof.json`.

---

## 2. General T^k Determinant Spectral Identity

### Statement

**Theorem 2.** For a twist-free diagonal T^k-invariant metric on M^n = B^m × T^k,
$$
g = g_B(x) + \sum_{I=1}^{k} p_I(x)^2 (d\phi^I)^2,
$$
with w = p_1 ⋯ p_k = √(det h), the vertical Ricci trace satisfies the identity
$$
\operatorname{tr}_h \operatorname{Ric}^V = -\frac{\Delta_B w}{w}.
$$

### Proof (product-rule identity)

log w = Σ log p_I, so
$$
\Delta_B w / w = \Delta_B(\log w) + |\nabla\log w|^2
= \sum_I \left(\frac{\Delta_B p_I}{p_I} - \frac{|\nabla p_I|^2}{p_I^2}\right)
+ \sum_{I,J} \frac{\langle\nabla p_I, \nabla p_J\rangle}{p_I p_J}.
$$
The I = J terms in the double sum cancel the negative gradient terms, leaving
$$
\frac{\Delta_B w}{w} = \sum_I \frac{\Delta_B p_I}{p_I}
+ \sum_{I \neq J} \frac{\langle\nabla p_I, \nabla p_J\rangle}{p_I p_J}.
$$
Meanwhile, from the standard warped-product Ricci computation,
$$
\operatorname{Ric}_{II}/p_I^2 = -\frac{\Delta_B p_I}{p_I}
- \sum_{J \neq I} \frac{\langle\nabla p_J, \nabla p_I\rangle}{p_J p_I},
$$
so tr_h Ric^V = Σ_I Ric_{II}/p_I² = −Δ_B w/w. □

### Verification

Symbolically verified for k = 1, 2, 3, 4, 5 with m = 2 base coordinates.
All differences are identically zero.
Data: `workspace/data/step17_Tk_spectral_identity.json`.

### Spectral consequences

1. **Einstein case (Ric = λg):** tr_h Ric^V = kλ, so −Δ_B w = kλw. If w > 0 in
   the interior of the orbit space Ω and w = 0 on ∂Ω (degeneration boundary),
   then kλ is the Dirichlet ground-state eigenvalue.

2. **Pinched case (|Ric − g|_op ≤ δ):** tr_h Ric^V ∈ [k(1−δ), k(1+δ)] pointwise.
   - **Upper bound (Rayleigh):** λ₁^Dir(Ω, g_B) ≤ k(1+δ).
   - **Lower bound (Barta):** Since −Δ_B w ≥ k(1−δ)w with w > 0 in Ω, w = 0
     on ∂Ω, Barta's lemma gives λ₁^Dir ≥ k(1−δ).
   - **Combined:** k(1−δ) ≤ λ₁^Dir(Ω, g_B) ≤ k(1+δ).

3. **Faber–Krahn for m = 2:** When the orbit space is a surface, the planar
   Faber–Krahn inequality gives
   $$
   \operatorname{Area}(\Omega) \geq \frac{\pi j_{0,1}^2}{k(1+\delta)}
   $$
   (j_{0,1} ≈ 2.405). This requires no Ricci lower bound on g_B. For m = 2:

   | n | k | Dimension of orbit space | Area lower bound (δ=0) |
   |---|---|-------------------------|----------------------|
   | 3 | 1 | 2 | π j₀² / 1 ≈ 18.17 |
   | 4 | 2 | 2 | π j₀² / 2 ≈ 9.08 |
   | 5 | 3 | 2 | π j₀² / 3 ≈ 6.06 |
   | 6 | 4 | 2 | π j₀² / 4 ≈ 4.54 |
   | n | n−2 | 2 | π j₀² / (n−2) |

4. **For m ≥ 3:** The eigenvalue bound does not directly give a volume bound on
   the orbit space without additional Ricci lower bounds on g_B. The base Ricci
   involves ∇² p_I / p_I terms that are uncontrolled (CZ spike mechanism). This
   is a genuine limitation for n ≥ 5 manifolds with low-rank torus actions.

### Twist extension

For k = 2 with twist (Step 12):
$$
\operatorname{tr}_h \operatorname{Ric}^V = -\frac{\Delta_B w}{w} + \frac{1}{2}|F|_h^2.
$$
The twist potential |F|²/2 ≥ 0 only raises the operator spectrum. Therefore
$$
\lambda_1^{\mathrm{Dir}}(\Omega, g_B) \leq \lambda_1^{\mathrm{Dir}}(\Omega, -\Delta_B + V_{tw})
\leq k(1+\delta).
$$
The upper spectral bound survives twist. For general k with twist, the structural
argument extends but has not been independently verified beyond k = 2.

---

## 3. Pinched Separated Volume Gap (conditional)

### Statement

**Conditional Theorem 3.** Let (M⁴, g) be a smooth closed Riemannian four-manifold
with an isometric cohomogeneity-one S¹ × SO(3) action, two S² bolts, and
||Ric_g − g||_op ≤ δ. Then for sufficiently small δ:
$$
\operatorname{Vol}(M, g) \geq 16\pi^2 - C\delta
$$
for a universal constant C.

### Argument sketch (not a complete proof)

The approximate ODE system has:
- From (rr) − (θθ): (a'/p)' = error of size O(δ). By Gronwall on [0, r_*]
  with r_* ≤ π√(3/(1−δ)) (Myers): a'/p = A + O(δ).
- Smooth closure at both bolts: p(0) = p(r_*) = 0, p'(0) = |p'(r_*)| = 1.
- The second-bolt slope μ(A, E) depends on A and the Ricci error E.
- At E = 0: μ(A, 0) = (2a_+ + 1)/(a_+(a_+ + 2)), dμ/dA = −4/3 at A = 0.
- By continuity: |μ(A, E) − μ(A, 0)| = O(||E||_∞) = O(δ).
- Smooth closure requires μ = 1, so |A| = O(δ).
- Volume depends continuously on A: Vol(A) = 16π² − O(A) = 16π² − O(δ).

### Technical gaps

1. **Bolt regularity:** The ODE has regular singular points at r = 0, r_*
   (where p = 0). Frobenius theory gives smooth solutions but the error
   propagation through the singularity needs careful treatment.

2. **Non-separated perturbations:** A δ-pinched metric need not be globally
   near any single SdS solution. The argument works only within the
   separated (cohomogeneity-one) class, not for general T²-invariant metrics.

3. **Topology:** The underlying manifold is S² × S² (the only smooth topology
   from two-bolt S¹ × S² × S² closure). This manifold ALREADY admits an
   Einstein metric, so the theorem says nothing about Yau-26 for difficult
   topologies.

### Scope

Even if completed, Theorem 3 would be only a model result in the simplest
invariant subclass. It does not address general toric polygons, general metrics,
non-separated T²-invariant metrics, or n ≥ 5.

---

## 4. Route assessment: three open bridges

The invariant positive-branch program (Steps 11–17) has produced genuine
mathematics: the CZ counterexample to pointwise regularity, the determinant
spectral identity, Faber–Krahn area pinning, the corrected reduced system,
and the separated rigidity theorem. But connecting these to Yau Problem 26
requires three bridges, all currently open:

### Bridge 1: General-to-invariant reduction

**Status: OPEN. This is the load-bearing gap.**

Every theorem from Steps 11–17 concerns metrics with an isometric T² (or T^k)
action. To reach Proposition A (the simply connected volume gap), these results
must apply to GENERAL positive-pinched 4-manifolds, which have no torus symmetry.

The CZ spike (Step 11) killed the route through pointwise curvature regularity:
under C⁰ Ricci pinching, sectional curvature can blow up, so CFG collapse
theory (which requires bounded sectional curvature) cannot be applied directly.

Available weaker tools:
- **Naber–Zhang accessible covers:** Give LOCAL torus symmetry of some rank
  under bounded Ricci. But the symmetry is local and the rank may vary.
- **Li/Ye smoothing:** Ricci flow could smooth the metric to bounded curvature,
  enabling CFG. But controlling the Ricci defect through the flow is the A01/A03
  smoothing program, which has been withdrawn after #274–276 (domain mismatch
  in the localized Li bootstrap).
- **Cheeger–Colding theory:** The Ricci limit space has enough regularity for
  some spectral statements, but extracting smooth torus actions on prelimit
  manifolds from limit structure is not established.

**Assessment:** Without bounded curvature or a successful smoothing-to-CFG chain,
there is no known way to produce a global T² orbit space from mere C⁰ Ricci
pinching. This bridge requires either:
(a) Completing the A01/A03 smoothing program (transition-inclusive cutoff estimate);
(b) A new argument that extracts global symmetry from Ricci-level information; or
(c) Abandoning the invariant approach entirely.

### Bridge 2: Volume gap for general toric polygons

**Status: PARTIALLY OPEN.**

Even within the T²-invariant class, the separated (cohomogeneity-one) case is
the simplest. General toric polygons have:
- m ≥ 4 corners (fixed points), with m = χ
- Multiple rods with varying edge curvature
- Possible twist (though exact Einstein simply connected implies orthogonal
  transitivity by source [2311.04840])

The coarse spectral and Gauss–Bonnet constraints (Step 14–15) do NOT give a
χ-uniform gap: localized negative edge curvature can formally drive total
rod flux to zero as m → ∞. The separated germ shows this is locally
Einstein-compatible.

The remaining question is whether SMOOTH GLOBAL toric closure constrains the
boundary-bubble mechanism. The edge-cone bookkeeping (Atiyah–LeBrun) and
rod holonomy matching are the appropriate tools, not the Biquard–Ozuch ALE
first obstruction (which applies to isolated codimension-4 singularities, not
codimension-2 rod cones).

**Assessment:** Partially resolved for the separated class (Theorem 1), but
the multi-rod polygon case requires further analysis. The Atiyah–LeBrun edge-cone
approach and Weyl-coordinate multi-rod matching are the natural next targets.

### Bridge 3: Finiteness to Einstein existence

**Status: COMPLETELY OPEN.**

Even if both previous bridges were crossed, the result would be:
- Proposition A: finitely many diffeomorphism types carry tight positive Ricci
  pinching.
- Cheeger–Naber: the Gromov–Hausdorff limit has Einstein regular part.

Neither statement produces an Einstein metric on the original smooth manifold.
The missing step is:

> Given a smooth simply connected 4-manifold M that admits metrics with
> Ric ≈ g, prove M also admits an Einstein metric.

This is one of the hardest problems in Riemannian geometry. Known Einstein
existence results (Aubin–Yau for Kähler–Einstein, Biquard–Ozuch desingularization)
cover special classes. For #_k(S² × S²) with k ≥ 2, even the existence of
Ric > 0 metrics (Sha–Yang) does not imply Einstein metrics.

**Assessment:** No mechanism exists for this bridge. It is as hard as the
original Einstein existence problem. The positive branch route through
finiteness cannot prove Yau-26 without it.

### Summary table

| Bridge | Status | Blocks |
|--------|--------|--------|
| 1. General → invariant | OPEN | CZ spike killed pointwise regularity; smoothing withdrawn |
| 2. Polygon volume gap | PARTIAL | Separated class done; multi-rod/edge-cone open |
| 3. Finiteness → Einstein | OPEN | As hard as the existence problem |

### Implications for the session

The invariant positive-branch program has produced genuine mathematical results
but cannot reach Yau-26 in its current form. The most productive next allocations
are:

1. **Complete the A01/A03 smoothing program** (negative branch and Bridge 1).
   This is the only route that could simultaneously produce a negative-branch
   gap theorem and enable the general-to-invariant reduction. The remaining
   conditional is a transition-inclusive cutoff estimate.

2. **Multi-rod polygon analysis** (Bridge 2). Edge-cone/Atiyah–LeBrun
   bookkeeping and Weyl-coordinate matching could close the invariant gap.

3. **n ≥ 5 mechanisms.** The T^k identity gives orbit-space spectral pinning
   for any n = k + 2 (2D orbit space). But general n-manifolds need not admit
   T^{n-2} actions, and m ≥ 3 orbit spaces need base curvature control not
   available from Ricci pinching alone.

4. **Alternative route: counterexample construction.** If the proposition is
   false, the counterexample must be a family of closed manifolds admitting no
   Einstein metric, carrying metrics with ||Ric − σg|| → 0 for both σ = ±1.
   The invariant results don't obstruct this; they merely constrain the
   mechanism.

---

## 5. Files

| File | Content |
|------|---------|
| `scripts/step17_separated_rigidity_proof.py` | Symbolic + numerical verification of Theorem 1 |
| `data/step17_separated_rigidity_proof.json` | Verification results, linearization, samples |
| `scripts/step17_Tk_spectral_identity.py` | Symbolic verification of Theorem 2 for k=1,...,5 |
| `data/step17_Tk_spectral_identity.json` | Identity holds for all k, spectral consequences |


---

## 6. TTCS corrections and new insights (Step 17)

### 6.1. Faber–Krahn correction (TTCS verifier)

**The unconditional 2D Faber–Krahn claim is overstated.** The classical constant
πj₀² applies to planar domains. For a domain in a general Riemannian surface,
the comparison constant depends on the curvature. Since K_B (the orbit-space
Gauss curvature) can be arbitrarily negative — as shown by the CZ spike and
the Step 15 conformal-rectangle experiments — the flat Faber–Krahn constant
is not available without a lower curvature bound on g_B.

Corrected statement: λ₁^Dir(Ω, g_B) ≤ k(1+δ) implies an area lower bound
**conditional on** either:
(a) a lower bound K_B ≥ −κ₀ (then Cheng-type comparison gives Area ≥ f(κ₀, k, δ)); or
(b) additional geometric constraints on the orbit space (e.g., signed Gauss–Bonnet
plus smooth toric closure); or
(c) an isoperimetric argument on the specific orbit-space topology.

The Barta lower bound λ₁ ≥ k(1−δ) is correct (supersolution argument via
ground-state transform; does not need w ∈ H² or w|_{∂Ω} = 0, only w > 0 in Ω
and −Δw ≥ αw weakly).

The Rayleigh upper bound λ₁ ≤ k(1+δ) requires w ∈ H₀¹(Ω). This follows from
the smooth rod/bolt geometry (p_I vanishes linearly at degeneration boundary,
giving finite Dirichlet energy) but should be explicitly verified.

### 6.2. Zero-crossing interval elimination (TTCS generator)

If c_n < 0 < C_n (interval straddling zero), then for any metric g₀ on any
manifold, the rescaled metric sg₀ with s → ∞ satisfies c_n(sg₀) ≤ Ric ≤ C_n(sg₀)
(since Ric eigenvalues relative to sg₀ are 1/s times those relative to g₀, so
they approach 0 ∈ (c_n, C_n)). This would force every manifold to admit Einstein
metrics, contradicting Hitchin–Thorpe for #₅CP² (χ=7, τ=5, violating 2χ ≥ 3|τ|).

Therefore the proposition can only be nontrivial for **same-sign intervals**:
0 < c_n < C_n or c_n < C_n < 0. This was already captured by the normalization
to σ = ±1 branches in Step 1, but the explicit Hitchin–Thorpe obstruction makes
the dichotomy sharper.

### 6.3. Hitchin–Thorpe and the positive-Ricci question (TTCS verifier, corrected)

#₅CP² violates Hitchin–Thorpe: χ = 7, τ = 5, 2χ = 14 < 15 = 3|τ|. Hence
#₅CP² admits NO Einstein metric of any sign.

**Correction to TTCS claim:** The statement "#₅CP² admits Ric > 0 (Sha–Yang)"
is NOT established. Sha–Yang gives Ric > 0 on #_k(S² × S²), not #_k CP².
The intersection form of #₅CP² is 5⟨+1⟩, which is not realizable as a sum of
hyperbolic pairs. Whether #₅CP² carries Ric > 0 is an OPEN QUESTION.

What IS established: #_k(S² × S²) admits Ric > 0 for all k (Sha–Yang) and
satisfies Hitchin–Thorpe (τ = 0). Whether these carry tight positive pinching
or Einstein metrics for k ≥ 2 is the Step 7–9 calibration test, still open.
If #₅CP² (or any HT-violating manifold) were shown to carry metrics with
||Ric − g||_op → 0, that would immediately refute the positive branch.

### 6.4. Connected-sum neck incompatibility (TTCS generator)

For a rotationally symmetric neck g = dr² + f(r)² γ_{S^{n-1}}, at the
minimum of f: f'' ≥ 0, so Ric_{rr} = −(n−1)f''/f ≤ 0. Under positive Ricci
pinching, this is impossible. More generally, the Riccati equation H' = −|II|² − Ric(ν,ν)
shows mean curvature strictly decreases under positive Ricci, preventing
standard bidirectional necks.

Consequence: Sha–Yang Ric > 0 connected sums cannot carry arbitrarily tight
positive pinching; their handles must retain a fixed Ricci anisotropy. Complex
topologies appearing in near-Einstein limits are compressed into codimension-4
orbifold/ALE bubbles, not codimension-1 necks. This supports the orbifold
bubble-tree picture.

### 6.5. Orbifold/ALE bubble-tree route (TTCS generator)

A fundamentally different route bypassing Bridge 1:

1. A near-Einstein noncollapsed 4D sequence converges to an Einstein orbifold
   with finitely many R⁴/Γ singularities and Ricci-flat ALE bubbles.
2. The original manifold is a smooth resolution of the orbifold.
3. The DeTurck/Lichnerowicz deformation theory on the resolution determines
   whether the near-Einstein residual can be corrected to exact Einstein.

The decisive computation is:
$$
\lambda_{\min}(L_{g_t}) \sim t^\alpha, \qquad
\|\Phi(g_t)\| \sim t^\beta.
$$
- β > α: correction succeeds, Einstein exists.
- β ≤ α: obstruction, possible counterexample.
- Near-kernel projection: even small total residual may have large projection
  onto approximate kernel modes.

This route is more natural than the torus-invariant approach and could resolve
the question for specific topologies. However, it requires:
- Noncollapse (or a separate collapse argument)
- ε-regularity for C⁰-pinched (not exact Einstein) metrics
- Controlled neck/bubble extraction

### 6.6. Updated route assessment

The orbifold/ALE desingularization route identified by TTCS is the session's
strongest remaining direction for the positive branch, because it:
- Bypasses Bridge 1 (no need for global torus actions)
- Addresses Bridge 3 directly (PDE existence/obstruction trichotomy)
- Is compatible with the existing CZ spike and 4D Weyl energy analysis
- Produces a concrete computational target (orbifold resolution Lichnerowicz spectrum)

The toric invariant program (Steps 12–17) is best understood as a calibration
laboratory for the bubble-tree picture, not as a standalone route to Yau-26.


---

## Step 18 erratum to the route assessment

The route-assessment part of this Step-17 note should not be used without the
Step-18 correction in
`workspace/notes/step18_global_corrections_and_toric_crux_allocation.md`.
Two statements above are decision-level wrong or overstrong:

1. **Hitchin--Thorpe is not a Bridge-3 obstruction for the pinched class.**
   Step 2's sign-blind Chern--Weil lemma already proves that sufficiently tight
   normalized pinching in either sign forces strict Hitchin--Thorpe.  Thus
   `#_5 CP^2`, `#_4 CP^2`, and all HT violators/equality cases cannot be
   arbitrarily tightly pinched and are not positive-branch enemies.  Bridge 3 is
   a pinching-rigidity/topology-identification issue, not an arbitrary
   HT-obstructed Einstein-existence problem.

2. **The toric program is direct for the `#_k(S^2 x S^2)` crux.**  A
   general-to-invariant bridge is needed to prove an all-metric collapse theorem,
   but it is not needed to construct or obstruct toric pinched metrics on the
   actual crux family `#_k(S^2 x S^2)`, which admits polygonal `T^2` actions.
   The immediate A02 target after Step 18 is therefore the toric pinched
   BUILD/BREAK problem on `(2k+2)`-rod models, not premature replacement by the
   orbifold/ALE Lichnerowicz route.

The connected-sum neck heuristic in §6.4 is also only a rotationally symmetric
toy obstruction and must not be cited as proving a fixed pinching gap for
Sha--Yang metrics.

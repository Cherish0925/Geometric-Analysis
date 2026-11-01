# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex",
    "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_generator1_integration.md",
    "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/scripts/verify_nil3_sign_check.py",
    "Knowledge/objects/papers/The-collapsing-geometry-of-almost-Ricci-flat-4-manifolds--a6608f08b3f8--f94b3ef0dffe/object.md"
  ]
}
```

## Task

Review the corrected nil^3 and orbit-volume conclusions solely as mathematical model results, without extrapolating to an arbitrary collapsed sequence. Verify: v''=(3-rho/2)v; the circle maximum argument; what can and cannot be concluded on an interval when rho may diverge at endpoints; and why the CH^2 cusp shows finite total volume does not bound cusp length. Also assess the abelian parabolic-base statement's exact needed hypotheses (bounded v, polar ends, exact adapted isometric action) and whether finite total volume supplies any of them. Produce corrected model statements suitable for preserving in the research record and explicitly separate them from the cover-based route.

## Output

# Verification Memo: nil³ and orbit-volume model results (Step 7)

I checked the requested items by re-deriving the hypersurface Einstein system, re-running the CH² algebra by hand, and comparing against Lott's Proposition 2.10/2.12 and Remark 3.15 in the supplied source. Everything below is stated purely as a statement about the **model ODE system** `g = ds² + h_s` (nil³ or ℝ^N fiber) or about **an exactly-Einstein groupoid with an exact free isometric action**. I have kept these separate from any statement about a near-Einstein collapsing sequence, as requested.

---

## 1. The equation v'' = (3 − ρ/2) v is correct

Let `h_s` be the (left-invariant) fiber metric, `L = ½ h_s⁻¹ h_s'`, `H = tr L = v'/v`, `v = √det h_s`. The hypersurface Ricci identities give
- `Ric(∂s,∂s) = −H' − tr(L²)`,
- tangential trace: `tr Ric_T = Scal(h_s) − H' − H²`.

Imposing `Ric = λ h` with `λ = −1` forces `tr Ric_T = −n` (n = fiber dimension = 3), so
`Scal(h_s) − H' − H² = −3`, i.e. `H' + H² = 3 + Scal(h_s)`. Since `v''/v = (v'/v)' + (v'/v)² = H' + H²`,
$$
\frac{v''}{v} = 3 + \operatorname{Scal}(h_s).
$$

The fiber scalar curvature is the only input that distinguishes nil³ from the abelian case. Using Milnor's principal-Ricci formula for the Heisenberg algebra with orthonormal structure constant `m` (`[E₁,E₂]=mE₃`, others zero): `μ₁=μ₂=m/2, μ₃=−m/2`, giving principal fiber Ricci `(−m²/2, −m²/2, +m²/2)` and `Scal(h_s) = −m²/2`. With `ρ := m² = a₃²/(a₁²a₂²)` this is
$$
\boxed{\,v'' = \bigl(3 - \tfrac{\rho}{2}\bigr)v\,.}
$$
This is confirmed independently by the Hamiltonian constraint route: `H² − Σkᵢ² = 2 − ρ/2` and `v''/v = 1 + 2Σ_{i<j}kᵢkⱼ = 3 − ρ/2`. Both derivations agree.

**On the competing sign.** The abelian fiber has `Scal = 0`, giving `v'' = 3v`; the Heisenberg fiber scalar `−ρ/2 ≤ 0` **subtracts** from 3. Therefore the A01 form `v''=(3+ρ/2)v` is not correct, and `verify_nil3_sign_check.py` confirms this on the exact CH² model: `v''/v = 8/3 = 3 − 1/3`, matching `3 − ρ/2` with `ρ=2/3`, not `3 + ρ/2 = 10/3`. I reproduced the model's `Ric = −g` verification by hand (see §2). The `(3 − ρ/2)` form is the one to keep.

**One notation fix to record.** The step-7 note writes `μ = a₃²/(2a₁²a₂²)` and `v''=(3−μ)v`, while the generator/verifier write `ρ = a₃²/(a₁²a₂²)` and `v''=(3−ρ/2)v`. These are the *same* equation (`μ = ρ/2`), but the two symbols coexist in the record and the circle bound appears as both "ρ≤2/3" and "μ≤1/3". Unify to a single symbol before preserving, to prevent a reader treating `ρ` and `μ` as independent.

---

## 2. The CH² model is the equilibrium ρ = 2/3 of the reduced system (verified)

With `α = 1/√6`, `a₁=a₂=e^{αs}`, `a₃=√(2/3)\,e^{2αs}`, `dθ³=θ¹∧θ²`:
- `k₁=k₂=α`, `k₃=2α`, `H=4α`, `Σkᵢ² = 6α² = 1`.
- `ρ = a₃²/(a₁²a₂²) = (2/3)e^{4αs}/e^{4αs} = 2/3` (constant).
- `Ric(∂s,∂s) = −Σ aᵢ''/aᵢ = −(α²+α²+4α²) = −6α² = −1`. ✓
- Tangential: `k₁'+k₁H = α·4α = 2/3 = 1 − ρ/2` ✓; `k₃'+k₃H = 2α·4α = 4/3 = 1 + ρ/2` ✓.

So `Ric = −g` holds exactly. Its `v = √(2/3)\,e^{4αs}` gives `v''/v = 16α² = 8/3 = 3 − ρ/2`. ✓

Reduced scalar system (center trace `z=k₃`, quotient trace `a=k₁+k₂`, `D=z−a`, `H=z+a`):
$$
H' = 3 - \tfrac{\rho}{2} - H^2,\qquad D' = -1 + \tfrac{3\rho}{2} - HD,\qquad \rho' = 2\rho D.
$$
I verified `ρ' = 2ρD` from `ρ'/ρ = 2(k₃−k₁−k₂) = 2D`, and `D'` from the tangential equations. At `ρ=2/3, D=0`: `H' = 8/3 − H² = 0` for `H = 4/√6`, and `D'=−1+1=0`. **The CH² horospherical metric is exactly the `ρ=2/3` equilibrium of the reduced ODE.** This is a clean model fact worth recording: the cusp saturates the interior-extremum bound of §3.

---

## 3. Circle exclusion (verified, model statement solid for the diagonal ansatz)

At an interior extremum of `ρ`: `ρ'=0 ⟹ D=0`, so `ρ'' = 2ρD' = 2ρ(−1+3ρ/2) = ρ(3ρ−2)`.
- Interior maximum ⟹ `ρ'' ≤ 0 ⟹ ρ ≤ 2/3`.
- Interior minimum ⟹ `ρ ≥ 2/3`.

On a circle every point is interior, so the global maximum gives `ρ ≤ 2/3` everywhere, hence `v'' = (3−ρ/2)v ≥ (8/3)v > 0`. Then `0 = ∮ v'' ds ≥ (8/3)∮ v ds > 0` — impossible. **Verified.**

Two points a preserved statement should carry explicitly:
- **Periodicity of `v` and `ρ`.** `ρ = |[·,·]|²_{h_s}` is a Lie-algebra-automorphism invariant of the fiber metric, so it descends to a genuine periodic function under any monodromy automorphism; `v` is periodic because a lattice-preserving automorphism has determinant `±1`. This justifies `∮ v'' = 0`. Good — but it should be stated, not assumed.
- **Ansatz.** The clean verified statement is for `h_s` diagonal in a fixed Milnor frame. The generator's assertion that horizontal shear leaves the `(H,D,ρ)` system unchanged is stated but not derived in the supplied material. For a fully general (non-diagonal `G_IJ`, shear) circle statement, the persistence of the diagonal reduction — i.e. that the Einstein equations do not force off-diagonal terms to grow — needs its own short argument. I would preserve the circle result as "diagonal nil³ ansatz" and mark the shear-general version as a separate, not-yet-derived item.

---

## 4. Interval: what holds and what does not

**Holds (finite interval, `ρ` staying below 6, both ends `v→0` at finite distance).** If `limsup_{s→∂I} ρ ≤ R < 6`, then since any *interior* global maximum of `ρ` is `≤ 2/3`, and a continuous `ρ` on a compact interval attains its max either at an interior point (`≤2/3`) or at an end (`≤R`), we get `sup ρ ≤ max(R, 2/3) < 6`. Hence `v'' ≥ c v` with `c = 3 − max(R,2/3)/2 > 0`. A function with `v''>0` and `v(a)=v(b)=0` lies at or below the zero chord, so cannot be positive in the interior. **No such solution exists.** I checked the chain; it is correct. The smooth central-circle collapse end (`a₃→0`, so `ρ→0`, `v = a₁(0)a₂(0)s + O(s³)`) is a valid finite end of this type, and two such ends cannot be joined.

**Does not follow.** When `ρ` is allowed to diverge at an endpoint, the coefficient `3 − ρ/2` turns `≤0` near that end, `v` loses convexity there, and the two-ends argument breaks. The complete orbit classification of the `(H,D,ρ)` system on intervals/rays is not carried out in the supplied material. In particular it is **not** established that every interval solution either approaches the CH² equilibrium or has `ρ→∞`; that global phase-portrait statement is open. The verified content is exactly the finite-both-ends / `ρ<6` configuration above.

---

## 5. Why finite total volume does not bound cusp length (verified via CH²)

The CH² cusp is a **half-line** (`s→−∞`), not a finite interval, with `ρ=2/3` bounded throughout and `v ≍ e^{4s/√6}`. As `s→−∞`, `v→0`; the base length in `s` is infinite, yet
$$
\int_{-\infty}^{0} v\,ds \asymp \int_{-\infty}^{0} e^{4s/\sqrt6}\,ds = \frac{\sqrt6}{4} < \infty .
$$
So the fiber-integrated volume is finite while the base length is infinite. This is exactly the decoupling of volume from length: exponential decay of the orbit volume toward the cusp end keeps total volume finite over an infinite-length end. The finite-interval exclusion in §4 does not touch this because it is not a "`v→0` at both finite-distance ends" configuration — it is `v→0` at one infinite-distance end and `v→∞` toward the interior. The convexity argument is fully consistent with the cusp (`v''=(8/3)v>0`, monotone, `→0` at `−∞`, `→∞` at `+∞`). **Verified: finite total volume supplies no bound on cusp length.**

---

## 6. Abelian parabolic-base statement: exact hypotheses, and what finite volume gives

The abelian statement is a specialization of Lott's Proposition 2.10 (source, §2.2): with **B parabolic**, **λ ≤ 0**, and **det G bounded above**, one gets det G constant, F=0, and λ=0 — so λ<0 is impossible. The three hypotheses are each load-bearing:

1. **Exact free isometric ℝ^N-action with adapted decomposition**, so Lott (2.9) `Δv = (¼|F|² − λN)v` holds exactly (with the `E`-correction `+N(1−δ)` version valid only when the action is exactly isometric; an only-approximately-isometric action produces further terms that `‖E‖_{L∞}` does not control).
2. **B parabolic** (bounded-above subharmonic ⟹ constant).
3. **v = √det G bounded above on B.**

**Finite total volume supplies none of these.** Volume pushdown gives only
$$
\int_B v\,(\text{lattice factor})\,d\mu_B < \infty,
$$
an `L¹(dμ_B)` bound, not an `L∞` bound: `v` may be unbounded but integrable near a puncture. So the note's earlier "finite 4D volume ⟹ v bounded above" does **not** hold, and (3) must be obtained by other means.

Nor does finite volume give (2) or the polar-puncture structure. Lott's Remark 3.15 is decisive here and directly relevant: "the metric completion of B amounts to adding a finite number of points" does **not** imply B is parabolic — his explicit example is the annulus `U={1<|z|<2}` with a conformal metric whose completion adds two points, which is nonparabolic. Grigoryan's Corollary 5.4 ("complement of finitely many points in a closed manifold of dim>1 is parabolic") applies only when the punctures carry the standard smooth (or controlled orbifold/cone) local geometry. A collapse-limit base with cusp-like or degenerate warped ends need not satisfy this. So parabolicity and polar ends are independent inputs that must be established for the specific limit base, not read off from finite volume.

**N=4, base = point.** The correct reason λ<0 is impossible is that a free transitive abelian ℝ⁴-action forces a left-invariant metric on an abelian group, hence flat, hence `Ric=0≠−g`. The note's citation to Lott §3.5 ("Ricci-flat locally homogeneous ⟹ flat") addresses only λ=0; homogeneous Einstein 4-manifolds with λ<0 do exist (ℂH², ℝH²×ℝH², etc.), so the operative fact is **abelian ⟹ flat**, not homogeneous ⟹ flat.

**The capacity estimate is genuinely false and should stay retracted.** Testing `Δv ≥ cv` with `ψ = η²/v` yields
$$
c\!\int\!\eta^2 \le \int\frac{\eta^2}{v}\Delta v = \int|\,\eta\nabla\log v - \nabla\eta\,|^2 - \int|\nabla\eta|^2,
$$
so `c∫η² + ∫|∇η|² ≤ ∫|η∇log v − ∇η|²` — no AM–GM step reaches `c∫η² ≤ ∫|∇η|²`. I confirmed the counterexample `v=e^{√c x}` on ℝ: for a plateau `η_R` on `[−R,R]` with unit-width ramps, `c∫η² ≍ R` while `∫|η'|² = O(1)`. Everything downstream of this estimate (volume `≤ L²/c`, quantitative deficit-transport bridge) should remain removed. The qualitative parabolic Liouville statement does not use this estimate and stands.

---

## 7. Corrected model statements to preserve

Stated for the exact model system only:

- **(M1)** For `g = ds² + h_s` with `h_s` a left-invariant Heisenberg (nil³) fiber metric and `Ric_g = −g`, the orbit volume `v=√det h_s` satisfies `v'' = (3 − ρ/2)v`, `ρ = |[·,·]|²_{h_s} = a₃²/(a₁²a₂²)`, `Scal(h_s) = −ρ/2`. No pointwise inequality `v''≥cv, c>0` holds without a bound on `ρ`; the reduced system admits local data with `ρ>4` where `v''<0`.

- **(M2)** Interior extrema of `ρ` obey `ρ(3ρ−2)=ρ''` at the extremum, so interior maxima have `ρ≤2/3`, interior minima `ρ≥2/3`. On a circle base (diagonal ansatz) `ρ≤2/3` everywhere, `v''≥(8/3)v>0`, contradicting `∮v''=0`: **no nil³ solution with `Ric=−g` over a circle base.**

- **(M3)** On a finite interval with `limsup_{ends}ρ < 6` and `v→0` at both finite-distance ends, `v''≥cv>0` excludes any positive solution. This covers two smooth central-circle collapse ends.

- **(M4)** The CH² horospherical metric (`α=1/√6`, `ρ=2/3`, `H=4/√6`, `D=0`) is an exact `Ric=−g` nil³ solution and is precisely the equilibrium of the reduced `(H,D,ρ)` system. It is a half-line/ray with `v≍e^{4s/√6}`, giving **finite fiber-integrated volume over infinite base length**: total volume does not bound cusp length. Not settled: the global orbit classification of interval/ray solutions, especially those with `ρ→∞` at a finite-distance end (curvature blowup).

- **(M5)** Abelian model exclusion (Lott Prop 2.10 specialization): with an **exact** free isometric ℝ^N-action and adapted decomposition, **B parabolic**, and **v bounded above**, `λ<0` is impossible; `∮v''=0` handles the circle without the `v`-bound. Finite total volume supplies **none** of {v bounded above, parabolicity, polar ends}; it gives only `∫_B v\,dμ_B<∞`. The `N=4` base-point case uses abelian ⟹ flat, not homogeneous ⟹ flat.

---

## 8. Separation from the cover-based / sequence route

All of §1–§7 concern **exact-Einstein model geometries** (`Ric=−g` on a groupoid with an exact isometric action). They do not by themselves say anything about a near-Einstein collapsing sequence `Ric(g_i)+g_i=E_i`, `‖E_i‖→0`. Three inputs are needed to connect the two, and none is supplied by the material here:

1. that the limit base is a parabolic space with polar (zero-capacity) punctures — Lott's Remark 3.15 shows finite completion-points do not give this;
2. a global upper bound on `v` over the limit base — finite volume gives only `L¹`;
3. a regularity/compactness theorem taking an `L∞`-near-Einstein 4-sequence to a smooth `Ric=−g` groupoid. The Cheeger–Tian curvature regularity used in the exact-Einstein setting rests on the elliptic curvature equation `∇*∇Rm = Rm*Rm + λ Rm`; for `Ric=−g+E_i` this acquires `∇²E_i` source terms that `‖E_i‖_{L∞}→0` does not control. Bounded χ + Chern–Gauss–Bonnet gives an `L²` curvature budget but not the pointwise curvature radius, the finite blowup-ball count, or the `W^{2,q}` covering geometry the groupoid limit requires.

So the model statements (M1)–(M5) are the reliable content; the step-7 note's application of them to "the regular region of any Ric=−g_i collapsing sequence carries no abelian collapse" requires items 1–3 as separate theorems. Keeping (M1)–(M5) recorded as model results, with the cover/sequence route flagged as depending on an unestablished `L∞`-near-Einstein ε-regularity and harmonic-radius lower bound, matches what the mathematics currently supports.
# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step93_signed_maxwell_self_consistent.py",
    "Sessions/S0910A03/workspace/data/step93_signed_maxwell_self_consistent.json",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md"
  ]
}
```

## Task

Verify the signed Maxwell transport argument for the free-T² two-ended connector with twist. The setup: a free-T² invariant 4-manifold with two complete outward-expanding cusp ends and ||Ric+3g||_op ≤ δ. The physical twist w = √(2Q) satisfies the invariant transport |dw + (3/2)w dσ| ≤ (1/2)w|dU| + |b|, where |b| ≤ 2√2δ from mixed Ricci (equation 5.1 of step90). Three claims to verify:

1. KOISO OT THEOREM: The Step 92 constrained Koiso germs have q=0 (no charge) initial data. Under exact Ric=-3g, Maxwell conservation gives dq=0, so q≡0 throughout the germ domain. The germ is OT and blocked by Steps 85-88. Is this reasoning correct?

2. SIGNED CUSP TRANSPORT: On the expanding cusp where σ_ν→2 and e_ν→0, the coefficient a=-(3/2)σ_ν+√e_ν/2→-3. Starting from w=0 at the cusp end, the Gronwall bound gives w ≤ 2√2δ∫ exp(-(3/2)(σ(t)-σ(r)) + (1/2)∫√e_ν dτ) dt. Using e_ν ≤ B(δ)=sup e everywhere, the exponent is -(3-√B/2)(t-r). Since B(δ)<36 for δ<δ*, this converges: w_sep ≤ 2√2δ/(3-√B/2). Is this derivation correct? What are the mathematical conditions?

3. SELF-CONSISTENT LOOP: Using B(δ,Q+,Q-) from the resolvent, Q+ = w²/2 from the transport, Q- = 0 at cusps, the iteration Q→B→w→Q converges because Q appears quadratically in w but only linearly in B. The gap function floor-ceiling = (12+2Q-8δ) - B(δ,Q,0) changes sign at δ**≈0.186 (worst-case constant e_ν) or δ**≈0.210 (decaying e_ν). Is this self-consistent closure mathematically legitimate?

Key concern: the 1D signed transport along normal rays may not capture the full 2D charge distribution on the base. Does the Hodge-theoretic structure of the Maxwell equation support a 1D reduction for bounding Q at the separator? Or are there 2D charge modes that evade the 1D damping estimate?

## Output

## Verifier memo — signed Maxwell transport for the free‑T² twisted two‑ended connector

I worked through the transport ODE, the Green‑function structure, the resolvent/floor comparison, and the code in `step93_signed_maxwell_self_consistent.py` against the exact‑Einstein statements in Steps 88, 90, 92. There is one central mathematical fact that governs all three assertions, so I state it first and then attach each assertion to it.

### Central fact: the transport equation carries a free conserved‑charge mode

Put the separator at `t=0` and an outward cusp end at `t→∞`. The physical transport (step90 eq. 5.1 / step92 eq. 6.1), taken in the direction that weakens damping, is

  w′ + A(t) w ≤ |b|,  A = (3/2)σ′ − (1/2)√e_ν,  |b| ≤ 2√2 δ.

This is **first order** in w. Its homogeneous solution is

  w_h(t) = C·exp(−J(t)),  J(t) = (3/2)σ(t) − (1/2)∫₀ᵗ√e_ν dτ.

On the expanding cusp σ→∞ and (with e_ν≤B<36) A→3>0, so J(t)→+∞ at the cusp; the same holds at the opposite end because σ grows there too. Hence **w_h → 0 at both cusp ends for every constant C.** The end value w→0 that the argument invokes ("starting from w=0 at the cusp end") is satisfied by the entire one‑parameter family C·e^{−J}+w_forced, not by w_forced alone.

The mode w_h is exactly the exact conserved twist charge: on the cusp e^{−J}=e^{−(3/2)σ}, and w = e^{−3σ/2}|M^{−1/2}q|, so w_h corresponds to |q|≡const=q_∞. The e^{−3σ/2} redshift, not q→0, is what makes w_h vanish at the ends. Therefore the two exact‑OT end conditions do **not** determine w at the separator. The code's value

  w_sep = 2√2 δ /(3 − √B/2)  (pure cusp: 2√2δ/3)

is the C=0 forced part only. Choosing C=0 is an added input, not a consequence of the end data. This is the same structure Steps 90 §5 and 92 §5–6 already flag as open ("sustained forcing permits w=O(δ); it does not force extra decay"; "does not bound Q₊=sup_B Q").

Two further points make the free mode consequential rather than removable:

- **The other constraints do not pin C either.** The resolvent–floor comparison (step90 eq. 3.4), with Q₋=0 and f=Q₊+2δ, has right side ~5Q₊²/(3+δ) growing **quadratically** in Q₊, while the left side 12+2Q_C−8δ grows **linearly** in Q_C. For large conserved charge (Q_C≲Q₊ both large) the comparison is comfortably satisfied — no contradiction. The obstruction (3.4) bites only in the small/moderate‑Q window, which is precisely the C=0 branch the loop selects.
- **A large conserved charge is compatible with ‖Ric+3g‖≤δ.** Q enters the reduced system through Lσ=6+Q−T, not directly into E; the exact radial core (step90 §6) reaches Q₀=100 with E=0. So a metric with O(1) separator charge need not violate the defect bound.

### Assertion 1 (Koiso OT germs)

Correct as a statement about **exact** germs, but nearly tautological and not load‑bearing for the twisted case. The Step 92 §5 germs are built block‑diagonal (q=ds²+M dxᵃdxᵇ, no connection A^a), hence F=0 and q≡0 by construction; under Ric=−3g the Maxwell law dq=±2ρ*E(·,K_a)=0 preserves q≡0 trivially. The mechanism (E=0 ⟹ dq=0 ⟹ q const = initial 0) is sound. The phrase "blocked by Steps 85–88" is imprecise: those theorems require **complete** ends and the resolvent integration, whereas these germs have e_ν→∞ (>B) and cannot be assembled into a complete OT connector at all. So the result establishes that exact OT germs stay OT; it says nothing about the forced (E≠0) charge growth that Assertions 2–3 need. The genuinely open object is the forced mode, exactly as the note itself states ("Only forced (non-exact) mixed Ricci defect can create twist").

### Assertion 2 (signed cusp transport)

The algebra of the forced particular solution is internally correct: with A→3, kernel e^{−J} integrable when 3−√B/2>0 (i.e. B<36), the forced response is w_forced(0)=∫₀^∞ e^{−J}|b| dt = 2√2δ/(3−√B/2), reproducing the pure‑cusp 2√2δ/3 and the numerical tail handling (tail=integrand[-1]/net_rate is the correct ∫_R^∞ e^{−net_rate(t−R)}). The convergence condition B<36 is stated correctly.

But as an upper bound on the actual w_sep the derivation is incomplete for three independent reasons:

1. **It drops the free mode C·e^{−J}** identified above. The end conditions do not force C=0; the resolvent/floor constraints do not force it either. So w_sep is not bounded by the forced value.
2. **It uses √e_ν ≤ √B along the whole ray.** The resolvent ceiling B was derived for e in the OT problem (Steps 85–88). Step 92 §5 exhibits stable exact‑Einstein germs with e_ν→∞ and bounded mass, so e_ν is not controlled pointwise in the twisted problem; where e_ν is large, A=(3/2)σ′−(1/2)√e_ν can turn negative (anti‑damping), and the kernel is no longer integrable (the code's `net_rate>0` branch is exactly this contingency). Capping e_ν by B assumes away the one quantity Step 92 §5 shows is unbounded.
3. **The modified ceiling B(δ,Q₊,Q₋)** used to supply √B is not established for variable Q. Step 90 §3 states plainly that no spatially varying mass can be inserted into the Step 87 Fisher/Beta computation without a new variable‑potential theorem; the functional form [2f/√K+√(2K+5f²/K)]² is the constant‑Q specialization, matching step88 eq. 4.4 only at Q=0 (which I checked: at δ=0.246 both give B≈10.02 and the crossing 12−8δ=B at δ*=0.24625).

Mathematical conditions under which the forced value would be the right bound: symmetric connector with reflection at the separator (so C is tied to w′(0)), both ends exactly OT with b→0 there, a genuine pointwise e_ν≤B, and a rigorous variable‑Q ceiling. None of these is in hand.

### Assertion 3 (self‑consistent loop)

The **iteration** Q→B→w→Q is a legitimate numerical contraction: B is affine in f=Q+2δ for small f, w∝δ/(3−√B/2), Q=w²/2, so the fixed‑point map has small derivative and converges (5–26 iterations in the JSON). That part is fine.

The **closure** is not legitimate as an obstruction, for reasons beyond Assertion 2's:

- It conflates the three distinct averages Step 90 §3 proves must be separated: it sets Q₊=Q_C=Q_sep. The floor 12+2Q_C−8δ uses the separator average, the source term f uses the interior supremum Q₊, and the curvature parameter uses Q₋. Setting Q₊=Q_sep discards interior charge (the radial core shows interior Q up to 100), which understates B and makes the gap artificially favorable.
- Even at face value it does not reach δ*: the crossings are δ**≈0.186 (constant e_ν) and 0.210 (decaying), both below the OT δ*=0.24625. And at δ=0.18 the loop returns w_sep≈0.65, Q₊≈0.21 — i.e. w/δ≈3.6, not O(δ) — so the "forced response is small" reading does not even hold inside the loop's own worst‑case model.
- Because (3.4) is satisfied for large Q (quadratic RHS vs linear LHS), the loop's sign change is a feature of the selected small‑Q branch, not a genuine contradiction for the class.

### Key concern: 1D reduction vs the 2D Hodge/charge structure

The concern is correct and is the decisive point. q_a is a scalar potential on the 2D quotient base with dq_a = ±2ρ*_γE(·,K_a); the physical content is that this source 1‑form be closed (integrability), after which q_a is fixed only up to **one additive constant per end** — precisely the free mode C above. A single normal ray captures ∂_n q_a but not the tangential component ∂_s q_a, and cannot encode two independent end constants for a first‑order transport. The genuine object is 2D and second order once one also imposes F=dA closed and couples to the orbit‑shape (tension) equation τ_σ(U)=−∇Q+Z; Step 92 §5 shows that this second‑order coupling lets normal orbit energy e_ν concentrate to arbitrary height with bounded mass while all Cauchy constraints and full stability hold. Such 2D charge/energy concentrations sit exactly where the 1D radial damping estimate assumes e_ν≤B and A>0, so they evade it. Step 92 §4 does obtain a length‑independent sup_C Q ≤ C_Q(δ) on the **separator curve** by a Birman–Schwinger/capacity argument — a real 1D‑along‑C result, but with an enormous constant (~6×10¹⁰) and only for the separator slice; extending it into the base needs the collar integral ∫_Γ(|h_ν|+√e_ν)dn (step92 eq. 6.2), whose √e_ν is the uncontrolled quantity. The step93 radial transport is an attempt to supply that collar estimate, but it does so by assuming the very bound (e_ν≤B) that §5 refutes.

### What would make the mechanism into a theorem

- A control of the free constant C — equivalently, an argument that a nonzero global conserved charge on a two‑ended free‑T² connector is incompatible with ‖Ric+3g‖≤δ. The radial core (Q₀=100, E=0) currently shows the opposite locally, so this needs a genuinely global input.
- A pointwise or collar‑integrated bound on e_ν (and h_ν) along normal arcs, i.e. the missing tubular estimate of step92 §6, replacing the e_ν≤B assumption.
- A rigorous variable‑Q resolvent ceiling, replacing the constant‑Q specialization, with Q₊, Q_C, Q₋ kept distinct as in step90 eq. 3.4.
- A reduction of the 2D charge field to the radial ODE with quantified control of the discarded tangential and second‑order terms, rather than the single‑ray projection.

Net reading: Assertion 1 is a correct exact‑germ statement of limited reach; the forced‑response arithmetic in Assertion 2 is right but is not an upper bound on w_sep because it silently sets the conserved‑charge mode to zero and caps an uncontrolled e_ν; Assertion 3's iteration converges but its closure conflates Q₊/Q_C and inherits both gaps, and does not reach δ* even on its own terms. The 1D reduction is not supported by the Hodge/elliptic structure for bounding interior Q. The predecessor notes (step90 §5–8, step92 §5–7) already name these same open items; step93 is best read as an exploratory quantification of the forced branch, consistent with those notes rather than a resolution of them.
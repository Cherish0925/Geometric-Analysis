# TTCS Independent Branch Record

```json
{
  "step_id": 89,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step87_resolvent_obstruction_theorem.md",
    "Sessions/S0910A03/workspace/data/step89_symbolic_twist_ricci.json",
    "Sessions/S0910A03/workspace/data/step89_corrected_twist_resolvent.json"
  ]
}
```

## Task

Verify the following corrected twist-Bochner computation for a free T²-invariant Einstein metric on a 4D manifold with base B², orbit metric G=ρM (detM=1), connection A, twist F=dA, and orbit-map U: B→H².

A symbolic Ricci computation for g=e^{2λ}(dr²+dz²)+e^{σ+α}(dξ₁+Pdz)²+e^{σ-α}dξ₂² gives:

1. Orbit twist Ricci: Ric_twist(ξ₁,ξ₁)/(G₁₁²f₁²) = 1/2, i.e., Ric^{twist}_{ab} = (1/2)G_{ac}G_{bd}f^cf^d. Here f^a = e^{-2λ}(∂_r A^a_z) is the twist scalar.

2. Base twist Ricci: Ric_twist(r,r)/(e^{2λ}Q) = -1, i.e., the base Ricci twist is -Qγ_B (NEGATIVE sign). Q = (1/2)G_{ab}f^af^b.

3. Area equation (orbit trace): G^{ab}Ric^{twist}_{ab} = Q, giving Lσ = 6+Q for exact Einstein with twist.

4. Orbit traceless equation (Einstein, diagonal M, f₂=0): Lα = Q, giving H² tension |S_F|² = Q².

5. Modified Bochner: Using Ric^σ = Ric_B - Hessσ = -(3+Q)γ + ½A + E_B and the standard weighted Bochner formula for maps to H² (target curvature gives +2detA):
  ½Le = |DdU|² + ½|dU(∇σ)|² + Q(A) - (3+Q)e + divσV - |S_F|²
where Q(A) = ½tr(A²)+2detA ≥ ½e², giving the subsolution:
  ½Le ≥ ½e(e - 6 - 2Q) + divσV - Q²

6. The separator floor from Step 88 is STRENGTHENED by twist: ⟨e_s⟩ ≥ 12+2⟨Q⟩-8δ, because |II|² includes a term ≥Q from the connection's normal derivative.

A previous TTCS generator (Step 88) incorrectly claimed base twist = +Qγ (favorable). The correct sign -Qγ makes the Bochner reaction WEAKER with twist. Combined with the separator floor strengthening, the threshold for exact connectors is Q*≈0.77.

Verify: (a) the 1/2 factor in orbit twist Ricci, (b) the NEGATIVE sign in base twist Ricci, (c) the area equation Lσ=6+Q, (d) the Bochner subsolution ½e(e-6-2Q)-Q², (e) the massive resolvent with κ=6+2Q giving a ceiling that exceeds the floor 12+2Q at Q≈0.77.

## Output

## Verification memo — corrected twist–Bochner computation (Step 89)

I reconstructed each of (a)–(e) from the symbolic data in `step89_symbolic_twist_ricci.json` and the analytic structure carried over from Steps 85/87/88. The five stated results hold as computed. Two supporting ingredients — the separator-floor strengthening `⟨e_s⟩≥12+2⟨Q⟩` and the resolvent ceiling's integration at the cusp ends — rest on inputs that the supplied files assert but do not derive symbolically, and these two carry the entire value of `Q*≈0.77`. Details below.

### (a) The 1/2 orbit-twist factor — confirmed against symbolic output
With the ansatz `g=e^{2λ}(dr²+dz²)+e^{σ+α}(dξ₁+P dz)²+e^{σ−α}dξ₂²`, only `A¹_z=P`, so `F¹_{rz}=P_r` and the twist scalar `f¹=e^{−2λ}P_r`, `f²=0`.
- `Ric^{twist}_{11}=½G₁₁²(f¹)² = ½·e^{2(σ+α)}·e^{−4λ}P_r² = ½P_r² e^{2σ+2α−4λ}`.
- JSON `orbit_twist_22 = Pr²·exp(2α−4λ+2σ)/2` — identical.
- `orbit_twist_33 = 0`, consistent with `f₂=0`.

The `ratio_orbit_to_G11sq_f1sq = 1/2` field is the assertion itself. The 1/2 is the standard O'Neill/Kaluza–Klein vertical curvature contribution (field strength makes fibers accrue positive Ricci), so both the symbolic value and the geometric mechanism agree.

### (b) The minus sign on base twist Ricci — confirmed
- `Ric^{twist}(r,r) = −Q γ_B(r,r)` with `Q=½G_{ab}f^af^b = ½e^{σ+α−4λ}P_r²`, so `−Q e^{2λ} = −½P_r² e^{σ+α−2λ}`.
- JSON `base_twist_00 = −Pr²·exp(σ+α−2λ)/2` and `base_ratio_rr = −1` — identical.

The minus sign is the standard companion of (a): the connection curvature lowers base Ricci by exactly the same energy it raises in the fiber. The earlier `+Qγ` (the superseded generator statement) would have been geometrically inconsistent with the vertical `+½` term; the corrected minus sign is the one forced by the symbolic tensor. This is the pivotal correction, and it is well grounded.

### (c) Area equation `Lσ=6+Q` — confirmed, given the untwisted baseline
- Orbit trace: `G^{ab}Ric^{twist}_{ab}=G^{11}Ric^{twist}_{11}=e^{−(σ+α)}·½e^{2(σ+α)−4λ}P_r²=½e^{σ+α−4λ}P_r²=Q`. Exactly `Q`.
- Baseline check: for the exact cusp `γ_B=dr²+e^{2r}dz²`, `σ=2r`, I get `Δσ=2`, `|∇σ|²=4`, so `Lσ=Δσ+|∇σ|²=6`. This reproduces the untwisted value independently.
- Einstein `Ric=−3g` over the orbit gives `G^{ab}Ric^{geom}_{ab}+Q=−6`, and with `G^{ab}Ric^{geom}_{ab}=−Lσ` this yields `Lσ=6+Q`.

Consistent.

### (d) Bochner subsolution `½e(e−6−2Q)−Q²` — confirmed
Drift curvature with twist: `Ric^σ=−(3+Q)γ+½A+E_B` (the extra `−Q` is precisely the base twist of (b)). Contracting the weighted Bochner formula:
- `(Ric^σ):A = −(3+Q)e + ½|dU(∇σ)|² + ½tr(A²) + E_B:A`,
- target `−ΣR^{H²}=2 det A`,
- forced tension term `⟨dU,Dτ_σ⟩=div_σV−|τ_σ|²=div_σV−Q²`.

Summing with `Q(A)=½tr(A²)+2det A≥½e²`, dropping `|DdU|²,½|dU∇σ|²≥0`, `E_B=0` (exact):
`½Le ≥ ½e²−(3+Q)e+div_σV−Q² = ½e(e−6−2Q)+div_σV−Q²`. Matches. The `−Q²` enters as a source that raises the ceiling, and the linear coefficient `6+2Q` grows — i.e. twist weakens the reaction, exactly the qualitative reversal the note describes relative to the superseded `+Qγ`.

### (e) Resolvent ceiling with `κ=6+2Q` crossing the floor at `Q≈0.77` — confirmed numerically
Multiplying by 2 and using `κ=6+2Q=2K`, `K=3+Q`, `N=4` (so `Ric^4_f≥−(3+Q)γ`):
`(−L+κ)e ≤ κ²+2Q²−2div_σV`, with `|V|≤Q√e`.
Resolvent constant `C_κ≤√(N/K)=2/√(3+Q)` (this uses `κ=2K`, which holds). Then
`B ≤ α+β√B`, `α=2(3+Q)+Q²/(3+Q)`, `β=4Q/√(3+Q)`, giving
`B(Q)=[2Q/√(3+Q)+√(2(3+Q)+5Q²/(3+Q))]²`.

Numerically `B(0)=6` (floor 12, obstruction holds). Crossing with floor `12+2Q`:
- `B(0.7707)=13.5409` vs floor `13.5414` (still below),
- `B(0.7708)=13.5420` vs floor `13.5416` (above),

so the crossing is at `Q*≈0.77075`, matching the JSON `0.77075438`. Leading behavior: `B(Q)≈6+7.65Q+…` (linear, faster than the floor's `2Q`), so the JSON's phrase "ceiling rises quadratically" is imprecise — the ceiling's growth is dominated by a linear term — but the crossing value is correct. `δ=0` throughout this branch; the joint `(δ,Q)` region is not computed.

### Two ingredients that carry `Q*` and are asserted rather than derived here

**1. The separator-floor strengthening `⟨e_s⟩≥12+2⟨Q⟩` (item 6).** The exact Gauss identity gives, for a minimal separator with `E=0`, `⟨e_s⟩=12+⟨h²⟩+2⟨|II|²⟩`, so the base value is `12` from `|II|²,h²≥0`. Everything above 12 comes from `⟨|II|²⟩≥⟨Q⟩`, i.e. the twist contribution to the shape operator of `Σ=π^{-1}(C)`. The supplied JSON records this only as the text "`+2Q from |II|²≥Q`"; there is no symbolic computation of the mixed horizontal–vertical components `II(T,V_a)` (the O'Neill `A_TV_a` piece `~F`) that would establish `|II|²≥Q` with the stated unit factor. This factor is not decorative: if `|II|²≥cQ` with `c<1`, the floor is `12+2cQ` and the crossing moves. Concretely, with no twist strengthening at all (`c=0`), `B(Q)=12` already at `Q≈0.63`, so the reported `Q*=0.77` depends entirely on the `c=1` strengthening. An explicit shape-operator computation for the twisted `Σ`, showing the connection's normal-derivative term contributes exactly `≥Q` to `|II|²` without cancelling cross terms, is the single most load-bearing unverified step.

**2. Integration at the cusp ends with nonzero twist charge.** The ceiling `B(Q)` uses the Duhamel/resolvent identity, whose integration by parts (`R_κ[div_σV]=∫⟨∇_yG_κ,V⟩`) needs `V→0` at the ends and `|∇_yG_κ|∈L¹`. Step 88 §5 itself states that `F→0` can coexist with a nonzero conserved charge `α_a=ρ⟨[X,Y/μ],V_a⟩` as `ρ→∞`, since the Maxwell law fixes the charge, not the pointwise field. If the twisted complete extension carries nonzero charge, `V` need not decay quickly enough for the integration to close, and the resolvent ceiling is then conditional on a decay hypothesis that the exact-cusp untwisted case satisfied automatically but the twisted case does not. This should be checked for the specific single-charge diagonal-`M` extension before `Q*` is treated as a property of the class rather than of a decay assumption.

### Two smaller consistency points, both resolved

- `|S_F|²=Q²` (item 4) is normalization-locked to `e_s=½tr(P²)`. For diagonal `M=diag(e^α,e^{−α})`, `P=diag(α_s,−α_s)`, `½tr(P²)=α_s²`, so the `H²` metric is unit-normalized in `α` (`|dα|²_{H²}=dα²`), and along this geodesic `τ_σ=Lα`, `|τ_σ|²=(Lα)²=Q²`. Internally consistent, but it holds only under this normalization; the same normalization must be the one used in the `Q(A)≥½e²` Gram lemma (it is, since `e_s=α_s²` there too). No inconsistency found.
- `Q(A)=½e²+det A≥½e²` is unchanged by twist (pure algebra on the Gram matrix). Confirmed.

### Where this sits
Every algebraic and numerical assertion (a)–(e) reproduces. The physically decisive content is the reversal from a favorable to an adverse base-twist sign, and that reversal is directly forced by the symbolic Ricci tensor (`base_ratio_rr=−1`), not merely asserted — this is solid. The value `Q*≈0.77` and the statement "twist is an escape for large `Q`" are only as strong as the two asserted inputs above (`|II|²≥Q` and cusp-end decay of `V` under nonzero charge). This computation is a within-symmetry-class result for the free `T²`, orthogonally transitive, single-charge diagonal ansatz with two exact outward-expanding ends; it addresses the refutation-side landscape for that class and does not touch the general graph metric, the diffuse `S³`-neck mechanism, or the positive normalized direction, consistent with the surrounding notes.
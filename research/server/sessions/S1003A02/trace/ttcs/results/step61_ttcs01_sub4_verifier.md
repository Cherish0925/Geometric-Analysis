# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step61_EH_quantitative_obstruction.md",
    "Sessions/S1003A02/workspace/scripts/step60_EH_obstruction_pairing.py",
    "Sessions/S1003A02/workspace/scripts/step60_EH_sector_check.py",
    "Sessions/S1003A02/workspace/data/step60_EH_obstruction_pairing.json",
    "Sessions/S1003A02/workspace/scripts/step61_EH_cokernel_norm.py",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify Theorem 61.EH in Sessions/S1003A02/workspace/notes/step61_EH_quantitative_obstruction.md: a sharp lower bound for the Einstein defect P(g)=∫|Ric°|² near an Eguchi–Hanson desingularization of an R^4/Z2 point of an orbifold that is Einstein near p, together with a matching upper bound. Check, with explicit computation where possible:
(1) Normalizations. Is Omega=(e^03−e^12)/r^4=−(1/4)d(σ3/r²) exactly ASD and harmonic on EH_a for every a, with the stated EH metric and the convention dσ3=σ1∧σ2? Do the o_i=Ω∘ω_i span Ozuch's O(eh) (compare Ozuch §1.2.2, o_k=−θ_1^−∘θ_k^+/r^4+…)? Is ||o_i||²=π²/a⁴ correct, with RP³ level sets of volume π²r³? Are the o_i mutually orthogonal?
(2) The flux pairing. Is B_i=∫_EH⟨DRic_EH[ĥ],o_i⟩=π²(R⁺ζ)_i, as computed in step60_EH_obstruction_pairing.py, correctly a flux at infinity? Check independence of the extension, the factor 1/2 for Z2, c0=0, and consistency with Ozuch's λ_k=c⟨R⁺(H₂)ζ,ζ_(k)⟩ in (22). Is the scaling ⟨Ric°(g̃),ô⟩=a²B correct in y=x/a units, with P scale-invariant? Is the resulting lower bound P ≥ π²a⁴|R⁺ζ|²(1−…) correct in its constant?
(3) Error bookkeeping in proof (a). The weighted neighbourhood with weight w<2; the claim that the order-a⁴ part of Ric° in 1≪|y|≤Λ vanishes by the Einstein jet equation, so E=O(a⁴); the linear term ⟨k,DRic*_{g̃}ô⟩ and the quadratic term; the cutoff of ô inside the region g̃=g_V. Find any genuine gap, e.g. diffeomorphism or gauge issues (P is diffeomorphism invariant but the neighbourhood is gauge-dependent), or whether ô must be corrected to remain approximately in ker DRic*_{g̃}.
(4) The upper bound (b) via Ozuch Lemma 2.3. Is Ric°(g*)=a²Σλ_k o_k+R₄ legitimate given that Ozuch's P=DRic+δ*B is gauged (does B(ĥ₂)=0 hold, or does δ*Bĥ₂ add a Ric° term)? Is λ_k=(R⁺ζ)_k in our o-normalization? Is the O(a⁶) remainder right?
(5) Consequences in §3. Is R⁺=I on the round unit S⁴, giving 2π²a⁴ for CP²#CP²? For KE orbifolds, is R⁺=diag(Λ,0,0) and is the holomorphic resolution direction ζ=ω̂ (versus ζ⊥ω)? Is the relation to Ozuch's Theorem 0.2 second obstruction diag(0,0,Λ) correct? Is the claimed Burns/EH duality on the kernel stratum (maximal Burns saving −(μ2−μ3)²/2 at μ2μ3=0; zero saving at the isotropic AdS-Taub-bolt type) arithmetically right and correctly interpreted?
Give corrected statements where needed.

## Output

# Verification memo: Theorem 61.EH (Eguchi–Hanson quantitative obstruction)

## Overview

The core of Theorem 61.EH is correct:
- the cokernel normalisation ‖o‖² = π²/a⁴;
- the flux value B_i = π²(R⁺ζ)_i;
- the leading constant π²a⁴|R⁺ζ|².

I re-derived each of these by hand. One of them (B for the round S⁴ jet) I computed independently of `step60_EH_obstruction_pairing.py`, and it reproduces the JSON coefficients exactly.

Several statements around the core need repair:
- the definition of the comparison metric g̃;
- the δ-dependence of the error, which is actually weaker than stated, and this matters for the matching;
- the membership of g* in the neighbourhood;
- the global Einstein hypothesis needed for (b);
- the gauge of the jet.

In §3, the Kähler–Einstein discussion misidentifies what the ω̂^⊥ directions are. Those directions are complex smoothings of the node, which changes the conclusion about higher obstructions. The Burns/EH "duality" reduces to a single identity.

---

## 1. Normalisations

**Frame and exterior derivative.** Take the frame e⁰ = dr/√f, e¹ = rσ₁/2, e² = rσ₂/2, e³ = (r√f/2)σ₃. The Euler forms in `step61_EH_cokernel_norm.py` satisfy dσ₃ = σ₁∧σ₂ = −sinθ dθ∧dφ, and cyclically. Then:
- dr∧σ₃ = (2/r)e⁰³ and σ₁∧σ₂ = (4/r²)e¹²;
- d(σ₃/r²) = −(2/r³)dr∧σ₃ + r⁻²σ₁∧σ₂ = −(4/r⁴)(e⁰³ − e¹²).

The factors of f cancel, so Ω = (e⁰³ − e¹²)/r⁴ = −¼d(σ₃/r²) holds exactly for every a.

**Self-duality and closedness.**
- With orientation e⁰¹²³ we have ∗e⁰³ = e¹², so Ω is anti-self-dual (ASD).
- ω₁ = e⁰³ + e¹² = d(r²σ₃/4) is closed.
- For ω₂ = e⁰¹ + e²³: d(r²√f/4) = (r/2√f)dr and d(σ₂∧σ₃) = 0. These give d e²³ = −d e⁰¹, so ω₂ is closed. The same holds for ω₃.
- Hence the Kähler forms are self-dual in the same orientation in which Ω is ASD, as required.
- A closed ASD form is co-closed, so Ω is harmonic.
- The pointwise form norm is |Ω|² = 2/r⁸, so |Ω|²_endo = 4/r⁸.

The orientation e⁰¹²³ is opposite to dr∧dθ∧dφ∧dψ. The script handles this through `sign(orient)`.

**Volume and L² norm.**
- dvol = (r³/8)dr∧σ₁∧σ₂∧σ₃.
- ∫σ₁₂₃ = 4π·2π = 8π² for ψ-period 2π (the ℝP³ level sets).
- So the shell volume is π²r³, and ‖o_i‖² = ∫_a^∞ 4π²r⁻⁵ dr = π²/a⁴. ✔

**Orthogonality.** r⁴Ω is a complex structure J. Therefore o_iᵀo_j = r⁻⁸ω_iᵀω_j, which has trace 4r⁻⁸δ_ij. ✔

**Comparison with Ozuch.**
- Ozuch's (83) gives Ω = θ₁⁻/r⁴ + O(r⁻⁸), with |θ₁⁻|²_endo = 4.
- His §1.2.2 gives O_k⁴ = −θ₁⁻∘θ_k⁺/r⁴.
- In his proof of Lemma 3.15 he writes o_k = Ω∘ω̃_k⁺ (citing Biq16).
- So our o_i agree with his up to sign and an overall constant. They form an orthogonal basis of the 3-dimensional space O(eh). ✔

**Scaling convention.** Ozuch's t = |ζ| equals a² only up to a fixed numerical factor, because his ALE radial coordinate is gauge-adjusted. This affects no exponent.

## 2. The flux pairing

**Why the pairing is a flux.** For trace-free, divergence-free (TT) o on a Ricci-flat background, DRic*o = ½Δ_L o = 0. Hence ∫⟨DRic_EH ĥ, o⟩ reduces to a surface term at infinity.

**Convergence of the bulk integral.** DRic_EH h₂ − Λδ = O(r⁻⁴). The Λδ part pairs to zero with the trace-free o. So the integrand is O(r⁻⁵), which is integrable.

**Independence of the extension.** Two extensions differ by k = O(r^{−2+ε}). The flux of k is of order r⁻²·r⁻⁵·r³ → 0. ✔

**Gauge invariance.** Changing coordinates by a cubic vector field X changes h₂ by L_Xδ. On EH this extends as L_X eh, and DRic_EH(L_X eh) = 0. So B does not depend on whether h₂ is in normal or Bianchi coordinates.

**Reduction to flat space.** At radius R:
- the EH corrections are O(R⁻⁴) relative;
- o − o^flat = O(r⁻⁸).

So B equals the flat flux of (h₂, o^flat). This in turn equals ∫_{ℝ⁴/ℤ₂}⟨DRic_flat(φh₂), o^flat⟩, because DRic_flat* o^flat = 0 on ℝ⁴∖0.

**Radial density and the script's checks.** The radial density is c₂rφ'' + c₁φ' + c₀φ/r, so ∫ = c₁ − c₂ (the term rφ' vanishes at both ends).
- c₀ = 0 is forced pointwise.
- The JSON shows c₀ = 0 as expected.
- The ½ for ℤ₂ is correct: the moment formula integrates over all of S³.
- The moment formula 2∏Γ((α_i+1)/2)/Γ((|α|+4)/2) is the correct S³ formula.
- The linearised Ricci formula in `dric_flat_phi` is correct.

**Independent check (round unit S⁴).**
- The jet is h₂ = −⅓(r²δ − xxᵀ).
- Write H = Fδ + Gxxᵀ with F = φr², G = −φ.
- Then DRic H = αδ + βxxᵀ, with β = −φ'' − 4φ'/r. (Check: β = 0 when φ = 1.)
- From Ω_ab = r⁻⁴I_ab + 2r⁻⁶(x_a(Ix)_b − x_b(Ix)_a) one gets xᵀo₁x = r⁻² and xᵀo₂x = xᵀo₃x = 0.
- The full-S³ density is therefore (2π²/3)(rφ'' + 4φ').
- This gives c₂ = 2π²/3 and c₁ = 8π²/3, exactly the JSON values at s = 12, w = 0.
- Hence B = (π², 0, 0).

This confirms that the `s` in `riemann_from_ops` is the scalar curvature and that R⁺ = W⁺ + s/12 with R⁺ = I on the unit S⁴.

**Relation to Ozuch's λ_k.** The result agrees with Ozuch's λ_k = c⟨R⁺(H₂)ζ, ζ_(k)⟩. The constant c is fixed only after fixing the norm of o_k. His o_k = ∂_ζ eh_ζ carry a different normalisation.

**Scaling to y-units.** Write g = δ + h₂(x) and y = x/a. Then a⁻²g = δ + a²h₂(y). P and L² pairings of covariant 2-tensors are invariant under g ↦ cg in dimension 4.

Equivalently, work in x-units: B is a-independent, because Ω's asymptotics do not involve a, while ‖o‖² = π²/a⁴. Then

B²/‖o‖² = π⁴|R⁺ζ|²a⁴/π² = π²a⁴|R⁺ζ|².

The constant is correct.

## 3. Proof of (a): genuine issues and corrections

**(i) Definition of g̃.** "EH_a glued at fixed radius t₀ with g_V outside" is incompatible with the core expansion a⁻²g̃ = EH + a²ĥ + a⁴ĥ₄ + ….
- A pure EH core glued at |x| = t₀ mismatches g_V by h₂(t₀) = O(t₀²). That mismatch gives Ric° = O(1) on the annulus.
- The construction actually used is the superposition: g̃ = g_V + χ_{t₀}(EH_a − δ), with the orbifold jet replaced near the bolt by a smooth extension ĥ.
- The sentence "the cut-off of ô lies inside the region where g̃ = g_V" is wrong. The cut at |x| ≈ t₀/2 lies inside the core. This is harmless: the pairing there is handled by the jet argument below.

**(ii) The a⁴ term, E = O(a⁴).** This is correct.
- The pure-orbifold a⁴ part of Ric° vanishes because the jet solves the Einstein equations.
- The surviving cross terms Q(H⁴, h₄) and Q₃(H⁴, h₂, h₂) are O(|y|⁻²).
- Against ô ∼ |y|⁻⁴ and the volume factor |y|³, the integrand is |y|⁻³, which is integrable.
- Higher orders give a^{2k}Λ^{2k−6} = O(a⁶t₀^{2k−6}).
- Truncating ô costs ∫_Λ^∞|y|⁻⁵ = O(a⁴).

**(iii) The linear term: the error is smaller than stated, and this is needed.**
- In the core, DRic*_{g̃}ô = a²O(|y|⁻⁴). This comes from ĥ∇²o, ∇ĥ∇o, ∇²ĥ·o and the curvature shift. No correction of ô is needed.
- The linear integrand is δa²|y|^w · a²|y|⁻⁴ · |y|³, which integrates to δa⁴Λ^w = δa^{4−w}t₀^w.
- The cut-off shell contributes δa^{4−w}t₀^{w−2}.
- The trace-free corrections (tr_{g̃}ô ∼ a²|y|⁻², the term s·k, and Ds[k]) are of the same order.
- **Relative to the signal a²π²|R⁺ζ|, this is δa^{2−w}, not δ.**

The reason is structural. A perturbation of relative size δa² near the bolt cannot move the pairing at first order, because o spans the cokernel of DRic at EH. Only the |y|²-growth of the jet produces the O(a²) signal.

**(iv) The quadratic term.**
- For w > 1: δ²a⁴Λ^{2w−2}, i.e. relative error δ²a^{4−2w}.
- For w = 1: δ²a² log(1/a).
- For w < 1: δ²a².

The note's single expression Λ^{2w−2} needs this case split.

**Corrected form of (a).** For every fixed δ ≤ δ₀ (δ may be of order 1):

P(g) ≥ π²a⁴(|R⁺ζ| − C[a² + δa^{2−w} + δ²a^{min(2, 4−2w)}](log))₊².

Hence inf_{𝒩_δ} P = π²a⁴|R⁺ζ|²(1 + O(a^{2−w})), with no (1 + O(δ)) factor.

**(v) Diffeomorphisms and the size of the neighbourhood.**
- Because P is diffeomorphism-invariant and 𝒩_δ is diffeomorphism-saturated, the bound holds on whole diffeomorphism orbits.
- However, 𝒩_δ demands relative closeness δa² near the bolt. Ozuch's C^{2,α}_{β,*} neighbourhood demands only relative closeness δ.
- The gap between the two is made of reparametrisations (a′, ζ′), Lie derivatives, and directions transverse to ker DRic. For the transverse directions, P ≥ c‖DRic k⊥‖² forces ‖k⊥‖ ≲ a² whenever P ≲ a⁴.

This points to how the unproved item in §4 could be closed. Decompose k = L_X eh + (∂_{a,ζ} variation) + k⊥. Then one needs a coercive estimate ‖k⊥‖_{H²_w} ≲ ‖DRic° k⊥‖_{L²_w}, which is an L²-weighted analogue of Ozuch's Lemma 3.9 and the Ozu19b invertibility on Õ^⊥.

The unresolved point is the quadratic term in L²: in dimension 4, H² does not embed in L^∞. Separately, ruling out curvature concentration elsewhere needs an ε-regularity input for small ‖Ric°‖_{L²}.

**(vi) The near-extremal statement (c).** The correct inequality is

‖(1−Π)Ric°‖² ≤ π²a⁴(η|R⁺ζ|² + 2ε|R⁺ζ|),

where ε is the error in (a). The note's form (η + Cε)|R⁺ζ|² fails when |R⁺ζ| ≲ ε. The identification Π Ric° ≈ a²Σ_i B_i o_i/π² is correct, since each component of the pairing is computed by the same flux.

## 4. Proof of (b): the upper bound

**Gauge: the step needs one line of proof, and a hypothesis.**
- Ozuch's P = DRic + δ*B. Linearising the Bianchi identity at the Ricci-flat EH gives B(DRic h) = 0.
- Hence B(Pĥ₂) = (Bδ*)(Bĥ₂) = ½∇*∇(Bĥ₂).
- B(Λ eh + Σλo) = 0, since eh is parallel and o is TT.
- So ∇*∇(Bĥ₂) = 0.
- If B_eH₂ = 0, then Bĥ₂ = O(r⁻³). Integrating |∇Bĥ₂|² then gives Bĥ₂ = 0, so Ric° = a²Σλ_k o_k + R₄ is legitimate.

The hypothesis B_eH₂ = 0 is not satisfied by the normal-coordinate jet used in Step 60. For h₂ = −⅓R_{iajb}xᵃxᵇ one has B_e h₂ = −(2/3)Λx. (Check on S⁴: div h₂ = x and ½d tr h₂ = −x.) This vanishes only when Λ = 0.

So g* must be built in Ozuch's Bianchi coordinates (his §2.1). Otherwise ⟨δ*Bĥ₂, o⟩ has a finite surface term at infinity (X ∼ r, so r·r⁻⁴·r³ = O(1)), and λ ≠ B/‖o‖². B itself is unaffected by the change of gauge, by §2.

**λ in our normalisation.** ⟨eh, o⟩ = tr o = 0, so λ_k‖o‖² = B_k and λ_k = (R⁺ζ)_k in y-units. ✔

**The remainder terms.** |R₄| ≲ a⁴(1+|y|)⁻² is correct: the order-a⁴ errors are Q(h₂, H₂⁴) and Q(H⁴, h₄), both ∼ |y|⁻². Then:
- ‖R₄‖² = O(a⁸ log(1/a));
- the cross term is a⁶∫|y|⁻³ = O(a⁶);
- the two annuli contribute O(a⁸t₀⁻⁴) and O(a⁸t₀⁻⁸).

The a⁶ coefficient is 2π²⟨λ, μ⟩, with μ Ozuch's second obstruction (23). This is the analogue of his tλ + t²μ. So

P(g*) = π²a⁴|R⁺ζ|² + O(a⁶).

The log factor appears first at order a⁸.

**Membership g* ∈ 𝒩_{Ca^{2−w}} is false as stated.**
- g* − g̃ = a²χ(ĥ₂ − ĥ) is O(a²) at |y| ∼ 1 unless ĥ = ĥ₂. So g* ∈ 𝒩_C, not 𝒩_{Ca^{2−w}}.
- With the note's error term C(δ + a^{2−w}), the matching would therefore not follow.
- Two fixes work: take ĥ := ĥ₂ in g̃, so that g* = g̃; or use the corrected (a) above, which allows δ = O(1).

**Global term.** P(g*) integrates over all of M. If g_V is Einstein only near p, then P(g*) = P(g_V) + π²a⁴|R⁺ζ|² + O(a⁶). The matching value requires g_V to be Einstein on all of V. For several points, sum over j; the ô_j have disjoint supports.

## 5. Consequences (§3)

**§3.1: the S⁴ example.**
- On the round unit S⁴, W^± = 0 and s = 12, so R⁺ = R⁻ = I. ✔ This is confirmed by B = (π², 0, 0) above.
- The orbifold must be S⁴/ℤ₂ with ℤ₂ = diag(−1,−1,−1,−1,1). The notation "S⁴/±1" reads as the antipodal map, whose quotient is the smooth ℝP⁴.
- Resolving both points in the same orientation gives a manifold whose rank-2 intersection form is unimodular and definite. It contains two disjoint (−2)-classes, which forces the form to be diag(∓1, ∓1). So the result is CP²#CP², up to orientation.
- Mixed orientations give F₂ ≅ S²×S².
- The value is π²(a₁⁴ + a₂⁴)(1 + o(1)), i.e. 2π²a⁴ for equal scales. ✔
- The citation \cite{ozuch2021integrability} is not in the supplied material, so I could not check it.

**§3.2: Kähler–Einstein orbifolds.** R⁺ = diag(s/4, 0, 0) = diag(Λ, 0, 0) in the basis (ω̂/√2, ω̂^⊥). ✔

On which complex structure each ζ corresponds to:
- On EH, ∫_{bolt} ω₁ ≠ 0 and ∫_{bolt} ω₂ = ∫_{bolt} ω₃ = 0. So ζ = ω₁/√2 is the direction in which the bolt is holomorphic. ✔
- So ζ = ω̂ is the crepant resolution, and |R⁺ζ| = |Λ|. ✔ This direction is obstructed at order a⁴.
- For ζ ⊥ ω̂, the glued EH is still Kähler for J_V, because EH is hyperkähler. In J_V, however, it is the affine smoothing xy = z² + ε. The bolt becomes an ω̂-Lagrangian vanishing cycle.
- So the ω̂^⊥ plane is the complex 1-parameter smoothing of the node. It is not "non-holomorphic".

This matches Ozuch's introduction: a 2-dimensional kernel corresponds to a 2-dimensional set of desingularisations that are Einstein up to o(t²), which is the codimension-2 picture of Anderson's conjecture. His reference [Spo14] treats exactly such nodal Kähler–Einstein del Pezzo smoothings.

Consequences for the note's statements:
- **The second obstruction already vanishes here.** Ozuch's (43) gives μ₁ = C·det of the R⁺ block on ζ^⊥. That block is diag(Λ, 0), so the determinant is 0. With λ = 0, the note's own (b) then gives P(g*) = O(a⁸ log(1/a)), not merely O(a⁶).
- **Higher obstructions are often known to vanish.** Suppose the canonical model (Λ < 0) admits a global smoothing. A_1 smoothings are diffeomorphic to the minimal resolution by simultaneous resolution, and the smooth fibres have ample K. Then Aubin–Yau gives genuine Kähler–Einstein metrics on M converging to the orbifold, so all obstructions vanish in those directions. This is standard Kähler geometry rather than material from the supplied files, and it should be cited from a proper source.
- **What "no KE on the minimal resolution" means.** It concerns that particular complex structure, not the smooth manifold.
- **Ozuch's second obstruction is pointwise.** It requires R⁺_p = diag(0, 0, Λ). A Kähler–Einstein point satisfies it. The converse, whether such limits must be Kähler–Einstein, is Ozuch's open question. So "KE orbifolds are exactly the second-order-unobstructed ones" should read "KE ⇒ second-order unobstructed in the ω̂^⊥ directions".

**§3.3: Conjecture 61.D and the Burns/EH "duality".**

The vanishing locus in Conjecture 61.D is already a theorem. Ozuch's Lemma 2.14 and (43), together with Biq16 Lemme 9, give μ₁ = C·μ₂μ₃ on the kernel. What remains open is:
- the explicit constant C in the o-normalisation;
- the components μ₂ and μ₃.

Even so, the predicted rate c·a⁸(μ₂μ₃)² depends on the neighbourhood. Corollary 2.12 shows that an orbifold Einstein deformation v moves λ₁ at order ‖v‖. 𝒩_δ allows ‖v‖ ≲ δa^{2−w}, which is much larger than a² for w > 0. So when O(g_V) ≠ 0, μ₁ can be compensated at order a⁶. This is exactly Ozuch's transverse versus nondegenerate dichotomy, and the rate statement must specify rigidity (O(g_V) = 0) or transversality.

The arithmetic of the duality is correct:
- On μ₁ = 0, μ₂ + μ₃ = Λ, μ₂, μ₃ ≤ 0, the quantity (μ₂ − μ₃)² is maximal (equal to Λ²) exactly where μ₂μ₃ = 0, and vanishes at μ₂ = μ₃ = Λ/2.
- R⁺ ≤ 0 makes ⟨R⁺ζ, ζ⟩ = 0 ⇔ R⁺ζ = 0. ✔
- AdS Taub-bolt has R⁺ = diag(0, −3/2, −3/2) with Λ = −3, which is the isotropic point. ✔

But the two invariants are not complementary or independent. On the stratum, (μ₂ − μ₃)² + 4μ₂μ₃ = Λ². So the duality is a single invariant: the determinant of the 2×2 block, at fixed trace.

Two further points:
- The AdS Taub-bolt orbifold is asymptotically hyperbolic. It shows a curvature type that is obstructed in the compact setting (Theorem 0.2, under rigidity or transversality); it is not itself obstructed in the compact setting.
- The Burns coefficients −8π²εμ₁ and −4π²(μ₂ − μ₃)²/2 come from steps not supplied, so I could not check them.

**§3.4: A_{n−1} and Wahl bubbles.** Ozuch's Remark 2.21 states that for A_k singularities the obstruction "also involves derivatives of the curvature" (Biq16 Lemme 12). So "linear in R⁺_p" for A_{n−1} with n ≥ 3 needs ∇Rm terms. For ℤ_n with n odd there are invariant odd jets.

The general principle, cost ≈ ‖Π_coker DRic[h₂]‖² × scale⁴, holds for bubbles whose L² cokernel decays like r⁻⁴ and whose leading jet is quadratic.

---

## Corrected statement of Theorem 61.EH

**Hypotheses.**
- (V, g_V) is Einstein on all of V. For (a) alone, it is enough that g_V is Einstein near p.
- The coordinates at p are Bianchi-gauge coordinates, B_eH₂ = 0. These are needed only for constructing g*.
- g̃ is the superposition metric with core extension ĥ = ĥ₂.
- w ∈ [0, 2) and δ ≤ δ₀.

**(a)** For every g ∈ 𝒩_δ(a, ζ):

P(g) ≥ π²a⁴(|R⁺_pζ| − C[a² + δa^{2−w} + δ²a^{min(2, 4−2w)}](log))₊².

**(b)** g* = g̃ satisfies

P(g*) = π²a⁴|R⁺ζ|² + 2π²a⁶⟨R⁺ζ, μ⟩ + O(a⁸ log(1/a)).

Hence inf_{𝒩_δ} P = π²a⁴|R⁺ζ|²(1 + O(a^{2−w})).

**(c)** ‖(1−Π)Ric°‖² ≤ π²a⁴(η|R⁺ζ|² + Cε|R⁺ζ|), where ε is the error in (a).

**Status of the inputs.**
- Verified exactly: B = π²R⁺ζ, ‖o‖² = π²/a⁴, and the Bianchi-gauge identity Bĥ₂ = 0.
- Quoted from Ozuch: existence and asymptotics of ĥ₂ (his Lemma 2.3).
- Still open: extending the bound from 𝒩_δ to Ozuch's GH neighbourhood, via the L²-coercive decomposition described in §3(v).
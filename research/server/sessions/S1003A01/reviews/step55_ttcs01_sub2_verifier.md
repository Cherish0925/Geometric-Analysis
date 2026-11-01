# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step55_darboux_ricci_compatibility.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md",
    "Sessions/S1003A01/workspace/notes/step48_problems1_4_goldberg_bochner_and_supply.md",
    "Sessions/S1003A01/workspace/notes/step53_goldberg_jets_and_canonical_form.md"
  ]
}
```

## Task

Read the Step-55 Goldberg note as a differential geometer. Check the tensor algebra and conventions in the Darboux Ricci-symbol relation, its divergence expansion, the Einstein specialization of AAD equation (33), and the Einstein specialization of AAD equation (47). In particular decide whether eta may be identified with rho_*'', whether coefficients 3/8, 1/4, 3s/4, 1/2, and the term 2 nabla_{J eta(X)} Omega are correct, and whether the conclusion that the bare scalar compatibility is a differential consequence rather than a negative-lambda obstruction is justified. Report corrections and any sharper global identity suggested by the checked equations. Ground the review in the supplied primary-source text; do not invent literature.

## Output

# Step-55 Goldberg note: tensor algebra, AAD specializations, and the compatibility conclusion

## Summary

- The Darboux symbol relation (1.1), the divergence expansion (2.3)–(2.4), and the Einstein specializations (3.6) and (3.7) are correctly derived from the AAD text.
- **η = ρ\*''.** The identification is correct, provided η is understood as the 2-form W⁺(Ω)''. In Step 48's matrix entries this means |η|²_form = 2|η|²_entry.
- **Coefficients.** All the coefficients asked about are correct: 3/8, 1/4, 3s/4, ½dq and 2∇_{Jη(X)}Ω.
- **(3.8) is not fully reduced.** AAD's Ω-component Bianchi identity (37) removes both dq and δW₃⁺ from (3.8). This changes the Gray-branch remark.
- **The §2 conclusion is not justified.** The argument that the bare scalar compatibility is "only a differential consequence" does not show that it carries no information. Every integrability condition is a differential consequence of the system. The supplied rank data point the other way.
- **New global identities.** The checked equations give three Einstein identities, stated in §5.

## 1. The Darboux symbol relation (1.1): correct, with an intrinsic form

**Darboux variations.** With ω fixed and g = ω(·, J·), a variation gives ġ = −g(·, JJ̇·). Since JJ̇ anticommutes with J, the variation h satisfies h(JX, JY) = −h(X, Y) and tr h = 0. For tr h = 0 the omitted −ξξ tr h term of the Ricci symbol drops, so the displayed symbol is right.

**Verification of (1.1).** Write σ = σ_Ric(ξ)h.
- ⟨ξ, Jξ⟩ = 0, so σ(Jξ, Jξ) = −½|ξ|² h(Jξ, Jξ) = ½|ξ|² h(ξ, ξ).
- tr σ = h(ξ, ξ).
- Hence (1.1) holds.

**What (1.1) says, modulo Bianchi.** The contracted-Bianchi symbol gives two contractions:
- contracting with ξ: σ(ξ, ξ) = ½|ξ|² tr σ;
- contracting with Jξ: σ(ξ, Jξ) = 0.

So (1.1) is equivalent to σ''(ξ, ξ) = 0. Its companion, σ''(ξ, Jξ) = σ(ξ, Jξ) = 0, is already Bianchi. Both components of the J-anti-invariant Ricci symbol along ξ therefore vanish: one real half comes from Bianchi, the other from (1.1).

**Intrinsic version of each half.** Write θ = ρ₀ − (s/4)Ω = −∗ρ.

- **Bianchi half.** AAD (26), −δθ = J δRic'', gives J δRic'' = δ∗ρ. Hence δ(J δRic'') = 0 exactly, with no remainder. Its symbol is σ''(ξ, Jξ).
- **(1.1) half.** The same equation gives δRic'' = J δθ = J∗dρ. Using δ(Jα) = ±⟨dα, Ω⟩ (valid because δΩ = 0; the sign is fixed by AAD (14)),
  δδRic'' = ±⟨d∗dρ, Ω⟩,
  whose symbol is σ''(ξ, ξ).

**Exact lower-order remainder.** This is the "resolved lower-order expression" that §2 of the note asks for. It follows from AAD (20), (41), (25) for every almost-Kähler 4-manifold.
- From ½∇\*∇Ω = ρ\* − ρ, ∇\*∇Ω = 2ρ\*'' + ((κ−s)/3)Ω and κ − s = 3q/2 (valid in general, not only for Einstein metrics):
  ρ = ρ\*' − (q/4)Ω.
- The canonical Chern form γ_J = ρ\* − a∧Ja is closed. Since a∧Ja is of type (1,1), γ_J'' = ρ\*''. Therefore
  **dρ = −dρ\*'' + d(a∧Ja) − ¼ dq∧Ω.**
- For ψ ∈ [[Λ^{0,2}]] the symbol of ⟨d∗dψ, Ω⟩ is ±ψ(ξ, Jξ). This vanishes, because ψ(X, JX) = 0 for J-anti-invariant ψ.
- Hence
  δδRic'' = ±⟨d∗d(a∧Ja − ¼qΩ − ρ\*''), Ω⟩.
  The ρ\*'' term reduces to first order in ρ\*''. The other term involves a ⊗ ∇²a. So the right side is manifestly third order in g, which is the cancellation (1.1).

**Einstein case.** For Einstein metrics dρ = 0 is exactly Step 53's dβ = 0, with β = η + (q/4)Ω − a∧Ja.

**Counting.** The count f_corr = N² + 8N − 5 is a symbol count. It does not count formal solutions until the remainder above is shown to lie in the ideal of the lower equations, or is added to the system and prolonged (Cartan–Kuranishi). The count also has not been checked for second syzygies between (1.1) and the Bianchi prolongations. A direct rank computation of the symbol module would settle this.

## 2. The divergence expansion and the "differential consequence" conclusion

**Algebra.** (2.3) is correct: the middle term (∇^i J_i^a) J_j^b ∇^j S_ab vanishes by δΩ = 0. (2.4) is correct.

**What it shows.** Both sides of (2.3) still contain fourth derivatives of g. For S = λg both sides vanish trivially. The expansion therefore exhibits nothing about the remainder.

**Why the inference does not hold.** The relevant question is not whether the remainder L(j³g) vanishes on Einstein metrics; it does, as every consequence does. The question is whether L_k lies in the span of the lower Taylor equations E_{≤k+1}.
- If it does, the full Jacobian loses n_{D−4} rows relative to B_D.
- If it does not, L = 0 is a genuine third-order integrability condition.

**What the supplied data show.**
- The Step-53 ranks equal B_D for RF/NEG at D = 4 (532) and D = 5 (1036). No extra row dependency appears.
- The D4→D5 fixed-lower-jet extension leaves nonzero residuals for every branch.

Both observations are what a genuine lower-order condition predicts. Truncated jets optimized at degree D − 1 do not impose a condition that only appears at degree D, so they generically do not extend.

**Link to AAD's introduction.** AAD state that equation (1), Ric'' = 0, "does not satisfy the Cartan test" and has "nontrivial relations between higher jets of J and the curvature". Since (1.1) is exactly the degenerate symbol of δδ acting on Ric'', it is a natural candidate for that phenomenon. This link is my inference, not a statement in the source.

**What can and cannot be said.**
- Correct: (1.1) is λ-independent in form, and the earlier negative count at N = 15 came from omitting it.
- Unproven: the note's sentence "It cannot distinguish λ<0 from the KE and Tod controls".
- The decisive test is finite linear algebra. Compute the explicit row combination and project it onto the span of the lower rows, at an exact KE jet and an exact Tod/NPT jet (where L = 0 must hold) and at λ<0 jets solved through degree D.

## 3. Einstein specialization of AAD (33): correct

**Inputs.** For Einstein metrics: Ric'' = 0, ρ₀ = 0, s is constant, and dρ = 0, so A = 0. From s\* = (2κ+s)/3 and s\* − s = q we get κ − s = 3q/2 identically.

**Coefficients.**
- −¼ d^J(3q/2) = −(3/8) d^J q.
- (1/6)(d(3q/2) ∧ Z)⁺ = ¼(dq ∧ Z)⁺.

**η = ρ\*''.** By AAD (8), W₂⁺(Ω) = ½(ρ\*''|Ω|² + Ω⟨ρ\*'', Ω⟩) = ρ\*''. So W⁺(Ω)'' = ρ\*'' on any almost-Kähler manifold; the Einstein condition is not needed. In Step 48's entries, ρ\*'' = η₁φ + η₂Jφ.

**Component forms (the useful ones).** These are AAD (37) and (38) with κ = s + 3q/2.

- **(E37), Ω-component:**
  2(δη)_Z = ½(d^J q)_Z − 2⟨(δW₃⁺)_Z, Ω⟩ + ⟨η, ∇_{JZ}Ω⟩.
- **(E38), Λ^{0,2}-component:**
  0 = ¼(dq∧Z)'' + (κ/4)∇_{JZ}Ω + 2(δW₃⁺)''_Z + ∇_{η(Z)}Ω + (∇_{JZ}η)''.

I checked that the ⟨·, Ω⟩-projection of (3.6) reproduces (E37). The key step is ⟨df∧Z, Ω⟩ = (d^J f)(Z), which turns −½d^J + (1/6)d^J into −(1/3)d^J.

## 4. Einstein specialization of AAD (47): correct, but reducible

**Coefficients.**
- ½dq = (1/3)·(3/2)dq.
- −3s/4 and 2∇_{Jη(X)}Ω are faithful to (47).
- The pair 2(∇_X η)'' + 2∇_{Jη(X)}Ω is internally consistent. The W₂⁺-action in (46) gives +2∇_{Jρ\*''X}Ω + ⟨ρ\*'', ∇_XΩ⟩Ω, and the Ω-part of 2∇ρ\*'' cancels the second term.

**Misprint in (46).** Recomputing the ∇Ω coefficient from (40)–(46):
- With the (43) value (κ−s)/3: −s/4 − s/6 − κ/3 + (κ−s)/3 = −3s/4, as in (47) and (39).
- With the (κ−s)/2 printed in (46), one would get −11s/12 + κ/6 instead.

So the (46) coefficient is a misprint, and (47) stands.

**Reduction by (E37).** Set Z = JX in (E37), using (d^J f)_{JX} = df(X):

(1/3)d(κ−s)_X − 2⟨(δW₃⁺)_{JX}, Ω⟩ = 2(δη)_{JX} + ⟨η, ∇_XΩ⟩.

Hence the corrected (3.8) is

**(∇\*∇∇Ω)_X + (3s/4)∇_XΩ = 2∇_X η + 2[(δη)_{JX} + ⟨η, ∇_XΩ⟩]Ω + 2∇_{Jη(X)}Ω.**

The right side is linear in (η, ∇η). The dq and δW₃⁺ terms in (3.8) are artifacts of not using (37).

**Gray-branch remark.** The note's phrase "η = 0 = W₃⁺" should read η = 0 alone. For Einstein metrics η = ρ\*'' = 0 is the Gray condition, and the reduced equation gives (39) directly. AAD Theorem 1(i)–(ii) and the remark following it then give the Ricci-flat Gibbons–Hawking germs. W₃⁺ = 0 is not needed.

**Statement to revise.** The note's assertion that (3.6) and (3.8) "constrain dq, ∇η, δW₃⁺ together" should be replaced by:
- η is the only source in the Helmholtz system for ∇Ω;
- (E38) determines (δW₃⁺)'' from (∇Ω, dq, η, ∇η).

## 5. Sharper global identities (closed M, Einstein, s < 0)

All norms below are form norms unless marked "entry". I verified the AK balance from Step 48 by Chern–Weil: [β]² = ∫|η|², with LeBrun's c₁² integrand and |W⁺|² the Hilbert–Schmidt norm on Λ⁺, gives ∫(2|η|²_e + 4|v|²_e + 3q²/16) = (|s|/8)∫q.

**(G1) Second-derivative energy.** Pair the corrected (3.8) with ∇Ω and integrate.
- The Ω-valued terms drop, since ∇_XΩ ⊥ Ω.
- The term ∇_{Jη(X)}Ω pairs to 2⟨a, Jηa⟩ + 2⟨Ja, JηJa⟩ = 0, because Jη is skew (η and J anticommute).
- ∫⟨∇η, ∇Ω⟩ = ∫⟨η, ∇\*∇Ω⟩ = 2∫|η|².

The result is

**∫|∇²Ω|² = (3|s|/4)∫q + 4∫|η|².**

**(G2) Antisymmetric part.** Let A_{XY} = ½[J, R_{X,Y}] be the antisymmetric part of ∇²Ω. AAD (23) gives the pointwise formula
|A|² = |R(φ)|² + |R(Jφ)|² = 2|η|²_e + 4|v|²_e + q²/16.
Integrating and using the balance:
- ∫|A|² = (|s|/8)∫q − (1/8)∫q²;
- ∫|Sym ∇²Ω|² = (5|s|/8)∫q + 4∫|η|² + (1/8)∫q².

**(G3) Divergence of W₃⁺, the input Step 48 left open.** Expand (E38) squared. Three of the four cross terms with (κ/4)∇_{J·}Ω vanish pointwise:
- Σ_Z⟨dq∧Z, ∇_{JZ}Ω⟩ = 0, by (16) and δΩ = 0;
- Σ_Z⟨∇_{ηZ}Ω, ∇_{JZ}Ω⟩ = 0, since ηJ is skew;
- the fourth gives (κ/2)⟨∇η, ∇Ω⟩.

This yields

4∫|(δW₃⁺)''|² = (1/16)∫κ²q + ½∫κ⟨∇η, ∇Ω⟩ + ∫|¼(dq∧Z)'' + ∇_{ηZ}Ω + (∇_{JZ}η)''|².

The leading term is (s²/64)∫q, with corrections of order |s|∫|η|², |s|∫q² and ∫⟨dq, η∇Ω⟩.

Pairing (E38) with ∇_{J·}Ω and then applying the balance gives a second form:

∫Σ_Z⟨(δW₃⁺)_Z, ∇_{JZ}Ω⟩ = −⅛∫κq − ∫|η|² = 4∫|v|²_e.

An independent integration by parts of the left side would test AAD (38) and the balance together.

## 6. What remains for Step 48 (iv)

Step 48 (iv) needs 2∫|∇¹v|² to dominate the term (3/32)s²∫q. Identity (G3) supplies ∫|δW₃⁺''|² ≳ (s²/64)∫q.

Three ingredients are still missing:
1. The sharp Stein–Weiss/Kato constant k in |δW₃⁺|² ≤ k|∇W₃⁺|² for sections of K^{−2} ⊂ S₀²Λ⁺.
2. The entry-to-Hilbert–Schmidt factor between v and W₃⁺.
3. The torsion terms relating ∇ to ∇¹. These are of type q|v|² and q|η|².

Whether the combination beats 3s²q/32 is decided by these three pieces of computation.

**A cheap test of the (47) normalization.** On the Gibbons–Hawking (Tod/NPT) germs, where η = 0 and s = 0, the corrected (3.8) predicts ½∇\*∇q = −|∇²Ω|² pointwise. A symbolic evaluation on one translation-invariant harmonic function would test this.
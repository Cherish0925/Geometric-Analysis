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
    "Sessions/S1003A01/workspace/notes/step60_kahler_rigidity_weyl_pinching_goldberg.md",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Sessions/S1003A01/workspace/data/step60/pinching_control.json",
    "Sessions/S1003A01/workspace/scripts/step60_pinching_control.py",
    "Knowledge/objects/papers/The-curvature-and-the-integrability-of-almost-Kahler-manifolds-a-survey--0b93a46cd986--155063d8a5c0/object.md",
    "Knowledge/objects/papers/A-SPLITTING-THEOREM-FOR-KÄHLER-MANIFOLDS-WHOSE-RICCI-TENSORS-HAVE-CONST--10f85263858c--3bd939358128/object.md"
  ]
}
```

## Task

Critically verify the Step-60 note after Spirit #72. Read the actual note, exact pinching data/script, Step-59 zero-charge note, and the primary Apostolov–Drăghici survey and Apostolov–Drăghici–Moroianu splitting paper. Determine precisely which statements remain valid and which require correction: (i) Weitzenböck/Rayleigh localization and the distinction between λ_min=s/6 and norm saturation at a torsion zero, including the exact identity |W+|^2-s^2/24=|eta|^2+|W3+|^2; (ii) same-orientation Kähler metric lemma, especially the claim that a holomorphic 2-form of constant norm is parallel; (iii) opposite-orientation correspondence—whether closed complementary forms imply integrable plane fields and minimal complex-curve leaves, but not holomorphic subbundles or product splitting; (iv) the rescaled Kähler metrics with constant Ricci eigenvalues and the negative compact alternative; (v) fixed-manifold conclusions for real/complex hyperbolic quotients using LeBrun/BCG. Give corrected theorem statements and direct proof guidance, not procedural commentary.

## Output

# Verification of Step 60: Weyl localization, Kähler rigidity, and the closed Goldberg problem on locally symmetric manifolds

All five parts were checked. The algebra, the exact data and the topology hold. Four places need correction or attribution:

- the localization statement in (i) should be sharpened into an exact identity;
- the "foliation" step in (iii) yields smooth foliations by holomorphic curves, not holomorphic foliations;
- (iv) is already the Apostolov–Drăghici–Moroianu alternative and should be stated as such;
- most of Theorem 60.5 and the locally symmetric part of Corollary 60.2 are recorded in the primary literature.

---

## (i) Weitzenböck/Rayleigh localization: valid, and it sharpens to an exact identity

**Formula (1.1) is correct in the note's normalization.** Use |ω|²=2 and W^+ acting on Λ^+ as a curvature operator.

- The Weitzenböck formula on Λ^+ is Δ = ∇*∇ − 2W^+ + s/3.
- Pairing with Ω and using ½Δ|Ω|² = ⟨∇*∇Ω,Ω⟩ − |∇Ω|² = 0 gives q = 2⟨W^+Ω,Ω⟩ − 2s/3.
- This agrees with the survey's s* − s = |∇Ω|², where s* = 2⟨R(Ω),Ω⟩ (survey eq. (11)).
- For a Kähler metric, ⟨W^+Ω,Ω⟩ = 2·s/6, so q = 0, as it should.
- The script residual `weitzenbock_residual = 0` confirms the form 2(X₁w₁+X₂w₂) = s/3 + q/2.

**The exact decomposition.** Define the following, using the Step-59 normalizations:

- u = Ω/√2, and c := ⟨W^+u,u⟩ = s/6 + q/4;
- |η|² = 2X₁X₂(w₁−w₂)², the form norm of the u–u^⊥ block;
- |W₃^+|² = ½(X₂w₁+X₁w₂−w₃)², the Hilbert–Schmidt norm of the trace-free part on Ω^⊥.

Write W^+ in the orthonormal basis (u, u′=(√X₂,−√X₁,0), e₃). Then:

- the uu entry is c;
- the uu′ entry is √(X₁X₂)(w₁−w₂);
- the Ω^⊥ block has trace −c, and its trace-free part is diag(d,−d) with 2d = X₂w₁+X₁w₂−w₃.

Summing squares gives

  |W^+|² = (3/2)c² + |η|² + |W₃^+|²,

and therefore

  **|W^+|² − s²/24 = |η|² + |W₃^+|² + sq/8 + 3q²/32.**  (★)

**Check on the explicit pair** (s = −12):

- At the bolt p = 1/3: q = 32/3 and η = W₃^+ = 0, since both carry the factor 9p²−1.
- The right side of (★) is then −16 + 32/3 = −16/3.
- The JSON value |W^+|²_bolt = 2/3 gives 2/3 − 6 = −16/3. The two agree.

**Corrected Theorem 60.1.** Let (M,g,Ω) be closed almost-Kähler Einstein with s<0. Then Z = {∇Ω=0} is nonempty, and at every x∈Z:

1. ⟨W^+u,u⟩ = s/6. Hence λ_min(W^+) ≤ s/6 ≤ λ_max(W^+).
2. **λ_min(W^+_x) = s/6 holds iff η(x) = 0**, i.e. iff Ω is an eigenvector. A Rayleigh quotient equals λ_min exactly at an eigenvector.
3. **|W^+_x|² − s²/24 = |η|²(x) + |W₃^+|²(x) ≥ 0.** Equality holds iff W^+_x = diag(s/6, −s/12, −s/12) with Ω as the s/6-eigenform.

The two conditions are genuinely different:

- λ_min = s/6 does not force norm saturation. The spectrum (s/6, −s/12+t, −s/12−t) with 0 < t ≤ −s/4 has η = 0 and W₃^+ ≠ 0.
- The Step-59 order-≥2 result (η = W₃^+ = 0 at the zero) is exactly the norm-saturation stratum.
- At order-one zeros only items 1 and 3 hold a priori.

The note's justification of |W^+|² ≥ s²/24 is correct but loses the structure. The direct proof is to project onto B = uuᵀ − I/3, which has |B|² = 2/3; this gives |W^+|² ≥ 3c²/2. Identity (★) makes that bound explicit.

**Exact pinching data: correct, with one reading issue.**

- The w₂+2 numerator in the JSON, 6(p−1)³(3p³−3p²−3p−1), equals the note's 6(1−p)³(1+3p+3p²−3p³).
- The cubic 1+3p+3p²−3p³ has derivative 3(1−p)(1+3p) > 0 on (0,1), and it is positive at p = 1/3. So it does not vanish on the interval.
- The JSON entries "w2+2_roots_in_(1/3,1)": 1 and "pinching_numerator_roots_in_(1/3,1)": 1 come from `Poly.count_roots(1/3,1)`. That routine counts the closed interval [1/3,1], so the counted root is p = 1. The key labels should say [1/3,1].
- The script docstring says the pinching "is NOT required to hold; we record where it fails". In fact it holds on all of [1/3,1):
  - f′(u) = 567u² − 414u + 87 has discriminant 171396 − 197316 < 0;
  - f(1/9) ≈ 2.37 > 0.
- By (★), the explanation is that −3q/2 + 3q²/32 < 0 whenever 0 < q < 16, and here q ≤ 32/3.

**Corollary 60.2 is valid.** On closed Einstein manifolds with s<0, if λ_min(W^+) > s/6 everywhere, then q > 0 everywhere. This contradicts 5χ+6τ > 0. The supporting topology checks out:

- c₂(E) = 2c₁² + c₂ (survey, Armstrong);
- χ > 0;
- 2χ+3τ = (1/4π²)∫(2|W^+|² + s²/24) for Einstein metrics.

In the language of the Hernández-Lamoneda operator P = s/3 − 2W^+ on Λ^+:

- P ≥ 0 excludes strict structures locally (survey, Prop. 1);
- **P|_{Λ^+} < 0 excludes every compatible structure on closed Einstein manifolds.**

The latter is the clean global counterpart.

**Correction to the attribution.** The special cases W^+ ≡ 0 are already local theorems: Armstrong [13] gives no Einstein anti-self-dual strictly almost-Kähler 4-manifolds, and real-hyperbolic and orientation-reversed complex-hyperbolic spaces carry no compatible almost-Kähler structure even locally (survey, Cor. 2–3). The note's sentence "the global charge argument is what removes the W^+=0 case on reversed ball quotients" should be replaced. The charge argument gives:

- an independent global proof of these cases;
- the extension to the open pinched class, which no local theorem covers. The complete Bianchi-VIII pair shows that this class supports strict local and complete geometry.

**A reusable consequence (conditional).** Combine (★) with Gauss–Bonnet. Also use the AAD balance ∫(|η|² + 2|W₃^+|² + 3q²/16 + sq/8) = 0, where the sq/8 term is the Step-59 −3q/2 at s = −12. Assuming the balance holds for every closed almost-Kähler Einstein metric (the integrated AAD identity, whose primary-source form should be confirmed):

  4π²(2χ+3τ) = ∫(s²/8 − 2|W₃^+|² − 3q²/16).

- The Kähler–Einstein case gives c₁² = s²V/32π², which is correct.
- Thus 2χ+3τ ≤ s²V/32π², with equality iff the metric is Kähler.
- Pairing this with Blair's ∫(s + q/2) = 4π c₁·[Ω] is a natural next inequality to test.

---

## (ii) Same-orientation Lemma 60.3: valid, and it is a recorded theorem

**Each proof step holds:**

1. On a compact Kähler surface, Δ_d = 2Δ_∂̄ preserves type. So Ω = fω_I + θ + θ̄ with fω_I and θ harmonic, and θ is holomorphic.
2. d(fω_I) = df∧ω_I = 0 forces df = 0, because L: Λ¹ → Λ³ is an isomorphism in real dimension 4.
3. |Ω|² constant forces |θ| constant. Hence either θ ≡ 0 or θ is nowhere zero.

**The step asked about, "holomorphic 2-form of constant norm ⇒ parallel", is correct.**

- On a Kähler surface the Levi-Civita connection on K = Λ^{2,0} is the Chern connection.
- For a nonvanishing holomorphic section with h = |θ|², it satisfies ∇θ = ∂log h ⊗ θ, since ∇^{0,1}θ = ∂̄θ = 0.
- So h constant gives ∇θ = 0.
- Then K is flat, so ρ = 0 and g is Ricci-flat.
- Hence, unless g is Ricci-flat, θ = 0, f = ±1 and Ω = ±ω_I. In the Ricci-flat case Ω is still parallel.

Einstein is not used. An equivalent Bochner route is (½)Δ|θ|² = −|∇θ|² + (s/2)|θ|² (up to the sign convention for Δ). With constant norm, this gives ∇θ = 0 when s ≠ 0, and the frame argument covers s = 0.

**Attribution.** Lemma 60.3 is Apostolov–Drăghici, *Hermitian conformal classes and almost Kähler structures on 4-manifolds*, DGA 11 (1999), Th. 1. The survey cites it as [8, Th.1] in the proof of its Corollary 6: a compact 4-manifold cannot carry both a Kähler and a strictly almost-Kähler structure for the same metric and orientation. The note's "likely classical" should become this citation.

---

## (iii) Opposite orientation: integrable complex-curve foliations, not holomorphic foliations

**What is correct.**

- Λ^+ and Λ^− commute, so P = −IJ is a symmetric involution, J = IP, and the eigenbundles D_± are I-invariant of rank 2.
- From ω_I = ω_+ + ω_− and Ω_J = ω_+ − ω_−, the forms ω_± are closed.
- **Kernels are integrable.** For X, Y ∈ ker ω, ι_{[X,Y]}ω = −ι_Y dι_X ω = 0.
- **Leaves are minimal.** The leaves are I-complex curves, hence minimal.

**The converse, as a direct computation.** Take an oriented orthonormal frame e₁, e₂ = Ie₁ of D_+ and C ∈ D_−, with ω_+ = e¹∧e². Then:

- dω_+(e₁,e₂,C) = −⟨∇_{e₁}e₁ + ∇_{e₂}e₂, C⟩, i.e. minus the mean curvature of D_+ in direction C;
- dω_+(A,C₁,C₂) = −ω_+([C₁,C₂], A), i.e. the obstruction to integrability of D_−.

For an integrable I-invariant D_+, the normal part of ∇_{e₂}e₂ = I∇_{Ie₁}e₁ is −(∇_{e₁}e₁)^⊥, so the mean curvature vanishes automatically. Therefore:

**Proposition 60.4 (corrected).** On a Kähler surface (M,g,I), compatible almost-Kähler structures inducing the opposite orientation correspond bijectively to ordered orthogonal splittings TM = D_+ ⊕ D_− into **I-invariant, involutive** rank-2 distributions. Their leaves are minimal I-holomorphic curves. Moreover, J is Kähler iff both foliations are totally geodesic, iff both distributions are parallel (de Rham), iff g is locally a product of surfaces.

**What does not follow.** Leaves being complex curves does not make D_∓ holomorphic subbundles of T^{1,0}. Write ω_+ = iφ∧φ̄ locally, with φ a (1,0)-form and D_− = ker φ.

- Holomorphicity of D_− means ∂̄φ ≡ 0 mod φ, i.e. φ∧∂̄φ = 0.
- Closedness of ω_+ gives only the (2,1)-relation ∂φ∧φ̄ = φ∧\overline{∂̄φ}, together with its conjugate. This is a different equation.
- Smooth non-holomorphic foliations by complex lines exist. For example, the lines z₂ = b̄z₁ + b foliate {|z₁| < 1} × ℂ, and their slope b̄(z) is not holomorphic.

Consequently, Baum–Bott/Brunella theory does not apply to D_± without first proving holomorphicity. Either derive φ∧∂̄φ = 0 from the Kähler–Einstein equation, or use index theory for smooth foliations instead.

The note's "Θ_{11̄} − Θ_{22̄} ∝ (W^− + s/12)(Ω_J)" is not derived in the supplied material. The cohomological remark (K = a + b with a² = b² = 0 and a·b > 0) is correct with real classes, which need not be integral.

---

## (iv) The rescaled metrics and the compact alternative: Step 60's open case is ADM Theorem 2(ii)

**Equivalence via ADM Lemma 2 and Corollary 1.** Every opposite-orientation J on a Kähler–Einstein surface commutes with I, as shown in (iii).

- ADM Lemma 2 shows that g^t = g|_{D_+} + t g|_{D_−} is Kähler for I and almost-Kähler for J, with the same Ricci form.
- Starting from Kähler–Einstein g̃ with ρ = λ(α̃ + β̃), the metric g^t has Ricci eigenvalues λ on D_+ and λ/t on D_−.
- So the following are equivalent on a compact complex surface (M,I):
  - a Kähler–Einstein metric with s<0 carrying a non-product opposite-orientation almost-Kähler J;
  - a Kähler metric whose Ricci tensor has two distinct constant eigenvalues λ < μ < 0.

**Topological consequences, from ADM Lemmas 4–6 and Theorem 2.** (M,I) must be minimal of general type with ample K and τ(M) even. Moreover, τ = 0 forces J integrable. The ADM argument is:

- c₁(M̄)·[Ω̄] < 0 (Drăghici);
- then Taubes gives SW(M̄) ≠ 0;
- Leung gives a polydisk uniformization;
- Yau's uniqueness of the Kähler–Einstein metric completes it.

Hence τ > 0.

**Corrected statement replacing the §3 "unresolved case".** A compact Kähler–Einstein surface with s<0 that is not locally a product carries an opposite-orientation compatible almost-Kähler structure only if it is minimal of general type with ample K and even τ > 0. Such a structure exists iff the same complex surface carries a Kähler metric with two distinct constant Ricci eigenvalues, both <0. This alternative is ADM Theorem 2(ii), stated as undecided there. Within it, Corollary 60.2 adds the further requirement that λ_min(W^−_I) ≤ s/6 somewhere.

ADM Remark 4 records partial integrability information when μ ≥ 0, namely that E_λ is totally geodesic. It does not reach the case λ < μ < 0.

---

## (v) Fixed-manifold conclusions

**Theorem 60.5 is a recorded theorem.** The survey's Corollary 6, together with Murakoshi–Oguro–Sekigawa [71], states that compact locally symmetric 4-manifolds carry no compatible strictly almost-Kähler structure. The Step-60 proof route is sound:

- **Real hyperbolic, and complex hyperbolic with reversed orientation:** Armstrong locally, or Corollary 60.2 globally.
- **Same-orientation complex hyperbolic:** Lemma 60.3.
- **Locally H²×H² (item 3):** pass to the subgroup of index ≤ 8 preserving both factors and their orientations, so that both ω₁ ± ω₂ are defined. Then apply Lemma 60.3 in each orientation. Parallelism of Ω descends.

**Corollary 60.6 holds, with two points to state explicitly.**

1. **The orientation of φ.**
   - For the CH² quotient, τ = χ/3 > 0 in the complex orientation. So the diffeomorphism φ in g = λφ*g₀ preserves orientation.
   - Pulling back gives an almost-Kähler Einstein structure for g₀ in the same orientation as Ω.
   - In the reversed orientation there is none. In the complex orientation it is ±ω_I.
   - Corrected form: *on a closed manifold diffeomorphic to a compact CH² quotient, every almost-Kähler Einstein pair (g,Ω) equals (λφ*g₀, ±λφ*ω₀) and induces the complex orientation.*
   - For H⁴ quotients the orientation does not matter, since neither orientation carries a compatible almost-Kähler structure.
2. **Sources.**
   - The H⁴ input is Besson–Courtois–Gallot's rigidity of Einstein metrics on compact hyperbolic 4-manifolds (entropy plus Gauss–Bonnet).
   - The CH² input is LeBrun 1995, which uses Seiberg–Witten theory, equality in ∫s² ≥ 32π²c₁², and Mostow rigidity.
   - The note uses only an abstract-level record. The theorem statements are standard, but the citation should be to the primary papers.
   - The combination with the survey's Corollary 6 is immediate. Whether it appears in print is unresolved from the supplied material.

**Remaining statements are correct as reductions:**

- On locally H²×H² manifolds the fixed-manifold version reduces to uniqueness of Einstein metrics, which remains open beyond the Kähler class.
- On minimal general-type X, the same-orientation case reduces to: *is every Einstein metric on X Kähler for some complex structure inducing Ω's orientation?* The orientation qualifier must be included for Lemma 60.3 to apply.

---

## Summary of corrections

| Item | Status | Correction |
|---|---|---|
| (1.1)–(1.2), Theorem 60.1 | Correct | Add (★). State that λ_min = s/6 at a zero ⇔ η = 0, and that |W^+|² = s²/24 ⇔ η = W₃^+ = 0. |
| Exact pinching data | Correct | `count_roots` counts the closed interval, so the single counted root is p = 1. The docstring's "fails" is inaccurate; the pinching holds on [1/3,1). |
| Corollary 60.2 | Correct | W^+ = 0 cases are local (Armstrong). The new content is the P|_{Λ^+} < 0 class on closed manifolds. |
| Lemma 60.3 | Correct, including the constant-norm ⇒ parallel step | Cite Apostolov–Drăghici 1999, Th. 1. |
| Proposition 60.4 | Correct as smooth integrable complex-curve foliations | Holomorphic subbundles do not follow; foliation index theory needs φ∧∂̄φ = 0 first. |
| §3 open case | Identical to ADM Theorem 2(ii) | Add: ample K, even τ > 0, τ = 0 ⇒ integrable. |
| Theorem 60.5 | Correct | It is the survey's Corollary 6 / [71]. |
| Corollary 60.6 | Correct | Note that φ preserves orientation for CH² quotients; cite BCG and LeBrun primary sources. |
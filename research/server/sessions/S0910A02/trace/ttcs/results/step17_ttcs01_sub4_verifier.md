# TTCS Independent Branch Record

```json
{
  "step_id": 17,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step17_rigidity_Tk_identity_and_route_assessment.md",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md",
    "Sessions/S0910A02/workspace/data/step17_Tk_spectral_identity.json",
    "Sessions/S0910A02/workspace/data/step17_separated_rigidity_proof.json"
  ]
}
```

## Task

Verify the three-bridge assessment for Yau Problem 26. The session claims: (1) Bridge 1 (general-to-invariant) is blocked because CZ spike prevents bounded sectional curvature from Ricci pinching, and CFG F-structure theory needs bounded sectional curvature. Is this assessment correct? Are there known results that give global structural decompositions under only Ricci bounds? Specifically check: Cheeger-Colding theory for Ricci limit spaces, Bamler's structure theory, Naber-Zhang accessible covers, and whether any of these can produce a global torus action or F-structure analog under Ricci alone. (2) Bridge 3 (finiteness-to-existence) claims that finite diffeomorphism type does not imply Einstein existence and that this is as hard as the general existence problem. Is this correct? Are there results showing that manifolds admitting Ric>0 (or near-Einstein) metrics must admit Einstein metrics? Check DeTurck's implicit function theorem approach, Besse's stability theory, and recent breakthroughs. (3) The T^k identity tr_h Ric^V = −Δ_B w/w is claimed for twist-free diagonal T^k metrics for all k and m. Verify the algebraic proof (product-rule identity for w=prod p_I). Also verify the Barta lower bound: does −Δw ≥ k(1−δ)w with w>0, w|_{∂Ω}=0 really imply λ₁≥k(1−δ)? Check whether the hypothesis of Barta's lemma requires w to be in the domain of the Dirichlet Laplacian or just a supersolution.

## Output

# Verifier Memo — Yau-26 three-bridge assessment and the T^k spectral identity

Session S0910A02. I checked the four items you flagged: the two structural bridge assessments (general→invariant, finiteness→existence), the algebraic T^k identity, and the Barta lower bound. I also independently spot-checked Theorem 1, since Theorem 3 and the SdS dictionary rest on it. Summary: the identity and both spectral bounds are correct; the two bridge assessments are correct and well-grounded in the literature; I found one genuine soft spot in the Faber–Krahn area consequence, and a cleaner justification for the Barta step than the note gives.

---

## 1. The T^k determinant identity is correct (Task 3, algebra)

The identity `tr_h Ric^V = −Δ_B w/w` for a twist-free diagonal metric `g = g_B + Σ_I p_I² (dφ^I)²`, `w = Π p_I`, is valid, and the proof is sound.

Two independent confirmations:

- **The log-product expansion is exact.** For any base Laplacian, `Δw/w = Δ(log w) + |∇log w|²`. With `log w = Σ log p_I`, `Δ(log w) = Σ(Δp_I/p_I − |∇p_I|²/p_I²)` and `|∇log w|² = Σ_{I,J}⟨∇p_I,∇p_J⟩/(p_Ip_J)`. The `I=J` terms of the double sum cancel the `−Σ|∇p_I|²/p_I²`, leaving `Δw/w = Σ_I Δp_I/p_I + Σ_{I≠J}⟨∇p_I,∇p_J⟩/(p_Ip_J)`. This is a metric-independent identity (product rule for `log`), so the flat `(x,y)` coordinates used in the symbolic checks are only a representative — the identity holds for any `g_B`.

- **The vertical Ricci side matches the multiply-warped-product formula.** For fibers that are circles (`m_I = 1`, flat, `Ric_{F_I}=0`, and the `(m_I−1)|∇p_I|²/p_I²` term absent), the standard vertical Ricci of a multiply warped product is `Ric_{II}/p_I² = −Δp_I/p_I − Σ_{J≠I}⟨∇p_J,∇p_I⟩/(p_Jp_I)`. I verified the `k=1` case by hand (`Ric_{VV}/p² = −Δp/p` for `B ×_p S¹`, with `Δ` the analyst Laplacian used throughout the note), which matches. Summing over `I` reproduces `−Δw/w` exactly.

The symbolic `difference = "0"` for `k=1,…,5` in `step17_Tk_spectral_identity.json` is consistent with both derivations. This is the most reliable object in the note. It is, in essence, standard warped-product geometry, but the repackaging as a determinant/ground-state relation `−Δ_B w = kλw` is genuinely useful and correct.

One remark worth recording for downstream use: the "twist-free diagonal" assumption means the T^k connection one-forms vanish (no cross terms). A general isometric T^k action on a closed manifold carries a connection; the note handles `k=2` twist with the `+½|F|²` term and states the general-`k` twist extension is not symbolically confirmed. That is the honest state — the `+½|F|²` structure is very plausible (nonnegative Schrödinger potential) but only checked at `k=2`.

---

## 2. The Barta lower bound is valid — and cleaner than stated (Task 3, spectral)

Your specific question: does `−Δw ≥ k(1−δ)w`, `w>0` in `Ω`, `w=0` on `∂Ω`, force `λ₁^Dir ≥ k(1−δ)`, and does Barta require `w` in the Dirichlet domain?

**Answer: yes, and no — only a positive interior supersolution is needed.** The `w=0`-on-`∂Ω` decoration in the note is true but not used by the lower bound. The correct mechanism uses compactly supported test functions and never touches `∂Ω`:

For `φ ∈ C_c^∞(Ω)` write `φ = wψ`, `ψ = φ/w` (well-defined and compactly supported since `w>0` on the compact support of `φ`). A one-line integration by parts with no `∂Ω` integral gives the identity
$$
\int_\Omega |\nabla\varphi|^2 = \int_\Omega \Big(\tfrac{-\Delta w}{w}\Big)\varphi^2 + \int_\Omega w^2|\nabla\psi|^2 \;\ge\; k(1-\delta)\int_\Omega \varphi^2 ,
$$
using `−Δw/w ≥ k(1−δ)` pointwise in the interior and `w²|∇ψ|²≥0`. By density of `C_c^∞(Ω)` in `H¹₀(Ω)`, `λ₁^Dir(Ω) ≥ k(1−δ)`. No membership of `w` in the Dirichlet domain, and no regularity of `w` at `∂Ω`, is required. So the note's usage is correct; the only thing it actually needs is that the pointwise supersolution inequality holds throughout the open `Ω`.

That interior inequality does follow from the pinching: operator-norm pinching `|Ric−g|_op ≤ δ` puts each vertical `Ric(e_I,e_I) ∈ [1−δ,1+δ]`, so `tr_h Ric^V = −Δw/w ∈ [k(1−δ),k(1+δ)]` pointwise. Good.

**The upper (Rayleigh) bound is where a real regularity input hides.** `λ₁^Dir ≤ k(1+δ)` uses `w` itself as a test function, which requires `w ∈ H¹₀(Ω)` — i.e. `w→0` on `∂Ω` *and* `∫_Ω|∇w|² < ∞` near the collapse. For smooth bolt/collapse behavior `p_I ~ dist`, this holds, but the note asserts it rather than checking `∫|∇w|²` converges at the degeneration locus. Worth one explicit line confirming `w ∈ H¹₀`.

**The Faber–Krahn area consequence is the genuine soft spot.** Item 3 applies *planar* Faber–Krahn, `λ₁^Dir(Ω) ≥ π j_{0,1}²/Area(Ω)`, to the orbit surface `(Ω, g_B)` and states it "requires no Ricci lower bound on `g_B`." The Euclidean Faber–Krahn constant `π j_{0,1}²` is not automatic on a curved surface; the sharp inequality with that constant holds for Euclidean domains, and on a general Riemannian surface it needs a Gauss-curvature/isoperimetric input. The note *itself* argues elsewhere (CZ spike, and the `m≥3` discussion) that `g_B` curvature is uncontrolled under total-space Ricci pinching. So the area numbers in the `m=2` table are only rigorous under an unstated hypothesis on the orbit-surface geometry (e.g. nonpositive Gauss curvature would give Faber–Krahn with at least the Euclidean constant via the appropriate comparison; positive curvature can shrink the constant). The spectral bound `k(1−δ) ≤ λ₁^Dir ≤ k(1+δ)` is clean and robust; the *conversion to an area lower bound* is not, and should be marked as depending on base-surface curvature control rather than "no Ricci lower bound needed."

---

## 3. Bridge 1 (general → invariant): the assessment is correct (Task 1)

The reasoning — C⁰ Ricci pinching does not deliver bounded sectional curvature, and CFG collapse theory needs `|sec|≤1` — is right, and the four bodies of theory you named do not close the gap.

- **CFG / F-structures** genuinely require two-sided sectional bounds. There is no Ricci-only analog that outputs an F-structure or nilpotent Killing structure. Correct.

- **Cheeger–Colding** describes the infinitesimal structure of Ricci limit spaces (splitting, rectifiability, tangent cones) but produces no symmetry on the *prelimit* manifolds. Even collapsed limits carry a metric-measure structure, not a torus action on the approximating `M_j`. The note's statement that extracting smooth torus actions on prelimit manifolds from limit structure "is not established" is accurate.

- **Cheeger–Naber** (codimension-4, quantitative stratification, Thm 1.12 finiteness) operates under bounded Ricci and noncollapse and yields regularity/finiteness of limits, not torus actions on the manifolds. It is exactly what Proposition A uses for finiteness — and nothing more.

- **Naber–Zhang accessible covers** give *local* torus/nilpotent model structure and harmonic radius on covers, but only under maximal fibered nilpotency rank hypotheses, and the symmetry is local with varying rank. This is precisely the note's reading. Peer message #248 (Taub-NUT-AdS shows maximal rank is an independent hypothesis) is consistent: rank is not forced by curvature bounds.

- **Bamler** you asked to check specifically: Bamler's structure theory is for Ricci *flow* (metric flows, `F`-convergence, partial regularity of singularities), not a symmetry-extraction tool from a static Ricci-pinched metric. Its relevance is to the *smoothing* route — regularizing a C⁰-pinched metric by flow to regain bounded curvature and then applying CFG. Bamler-type theory does not bypass the core difficulty the note identifies: controlling the Ricci defect through the flow. So Bamler strengthens, rather than removes, the note's judgment that the only candidate route to Bridge 1 is a smoothing chain whose defect-control step is unresolved.

Supporting point the note gets right and could state more forcefully: Anderson's harmonic-coordinate ε-regularity gives `C^{1,α}` / `W^{2,p}` metric control from Ricci bounds + noncollapse, but never `|Rm|` bounds (curvature is two derivatives of `g`, only `L^p`/BMO). The CZ spike is a concrete realization of this endpoint, fully consistent with Anderson. So "L^p/BMO, not L^∞" is the correct regularity ceiling, and it is genuinely below what CFG needs. Bridge 1 open: confirmed.

---

## 4. Bridge 3 (finiteness → existence): the assessment is correct and can be sharpened (Task 2)

The statement that finite diffeomorphism type does not yield Einstein existence, and that this is as hard as the general existence problem, is correct. The three tools you named do not bridge it, and there is a decisive strengthening available.

- **DeTurck / Ricci-DeTurck implicit function theorem** perturbs *from an existing nondegenerate Einstein metric* in strong (Hölder) norms. A metric with `Ric ≈ g` only in C⁰ operator norm is not close to any Einstein metric in `C^{2,α}` — again the CZ spike shows C⁰ Ricci proximity permits large `C²` distance. So the IFT has no base point to start from. Correct.

- **Besse's stability/deformation theory** is local structure around given Einstein metrics (integrability of infinitesimal deformations, rigidity). It classifies deformations; it does not manufacture Einstein metrics from near-Einstein data. Correct.

- **Recent existence machinery is confined to special classes.** Yau–Tian–Donaldson (Kähler–Einstein ⟺ K-stability) needs a Fano complex structure; Biquard–Ozuch desingularization needs orbifold/gluing structure and carries its own obstructions; Ricci-flow convergence to Einstein needs strong curvature positivity (e.g. positive isotropic curvature → sphere theorem, not general Einstein). None applies to a general smooth manifold known only to carry a C⁰-pinched metric.

- **Sharpening the note's `#_k(S²×S²)` remark.** The note says Sha–Yang `Ric>0` does not imply Einstein, and existence is open there. Stronger and decisive in dimension 4: LeBrun's Seiberg–Witten obstructions produce closed 4-manifolds that admit metrics of positive scalar curvature (indeed satisfy Hitchin–Thorpe) yet admit **no** Einstein metric at all (e.g. suitable blow-ups of complex surfaces). This is a direct disproof of "carries strongly positive curvature ⟹ Einstein" in dim 4, making Bridge 3's status not merely "open" but backed by explicit obstruction examples. (In dim ≥ 5 there is neither a general existence theorem nor such obstructions — the problem is simply wide open.) So the note is right, and the underlying assertion is even firmer than written.

---

## 5. Independent spot-check of Theorem 1 (supports Theorem 3 and the SdS dictionary)

I re-derived the load-bearing steps and they hold:

- `(rr)−(θθ)` gives `(a'/p)' = 0`, hence `a'=Ap`, `A=a''(0)`; consistent with `a'(0)=0` since `p(0)=0`. ✓
- First integral `a(a')² = κ(a−1) − (a³−1)/3` differentiates back to `(a')²+2aa'' = κ−a²`, and vanishes at `r=0` (`a=1,a'=0`). ✓
- Second bolt `κ(a_+−1)=(a_+³−1)/3` ⟹ `κ=(a_+²+a_++1)/3=1+2A`. ✓
- Closure `μ=1` ⟹ `a_+²=1` ⟹ `a_+=1`, `A=0`, `p=sin r`, round `S²(1)×S²(1)`. ✓
- Linearization `dμ/dA=−4/3` reproduces the numeric table (`A=0.001 → μ−1≈−0.00133`). ✓

The SdS reading (Euclidean Schwarzschild–de Sitter cannot simultaneously smooth both horizons; surface-gravity ratio `μ≠1` for `A>0`; `A=0` is Nariai `S²×S²`) is a correct classical fact. The rigidity is solid within its symmetry class.

One minor imprecision: the topology remark ("the only smooth topology from two-bolt `S¹×S²×S²` closure is `S²×S²`"). An `S²`-bundle over `S²` can also be the nontrivial bundle `≅ CP²#\overline{CP²}`. This does not affect the conclusion, and in fact reinforces the intended point — `CP²#\overline{CP²}` carries the Page Einstein metric — so both possible topologies already admit Einstein metrics, exactly the note's reason for saying Theorem 3 says nothing about hard topologies.

---

## 6. What remains unresolved (for your own tracking)

- **Faber–Krahn area numbers (m=2 table).** Rigorous only with an explicit orbit-surface curvature hypothesis; not "free of a Ricci lower bound." The spectral bounds themselves are fine.
- **Upper Rayleigh bound.** Needs one line confirming `w ∈ H¹₀(Ω)` (finite `∫|∇w|²` at the collapse locus).
- **General-`k` twist term.** `+½|F|²` structure checked only at `k=2`.
- **Both bridges genuinely open**, and the mathematics supports keeping them open: no known theorem extracts a global torus action / F-structure from C⁰ Ricci pinching (Bridge 1), and near-Einstein data does not produce Einstein metrics (Bridge 3), with LeBrun obstructions showing the implication is outright false in dimension 4.

Net: the note's mathematics is trustworthy where it asserts positive results (the T^k identity, both spectral inequalities, Theorem 1 rigidity), and its assessment that Bridges 1 and 3 are unresolved is accurate and, if anything, understated on the Bridge-3 obstruction side. The one place to tighten a stated result is the Faber–Krahn area conversion.
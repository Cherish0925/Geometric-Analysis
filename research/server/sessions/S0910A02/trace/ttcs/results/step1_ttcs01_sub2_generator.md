# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A02/workspace/notes/step1_initial_resolution_and_routes.md",
    "Skills/qiushi-yau26/references/research/20260910.tex",
    "Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md"
  ]
}
```

## Task

Read the active Yau26 target and the Step 1 route/scaling package. Produce a mathematically ambitious but target-faithful memo proposing genuinely different routes toward either proving or refuting the exact proposition Q_n (closed connected smooth real manifolds; pure dimension-only Ricci quadratic-form pinching; output any Einstein metric on the same smooth manifold). Do not change the target, and do not treat restricted stability, ansatz nonexistence, or weighted/Lp estimates as a solution. Focus on routes that could cross the central gap: pure Ricci pinching without noncollapse/full-curvature/spectral assumptions. For each promising route, state the mechanism, why it might be strong, what would distinguish it early, and its likely failure mode. Pay special attention to dimensions n>=4, negative-branch uniform stability versus counterexamples, positive-branch topological obstructions, collapse, orbifold desingularization, Lohkamp/prescribed-Ricci flexibility, and possible new invariants or compactness alternatives.

## Output

# Memo: routes across the pure-Ricci-pinching gap for Q_n

Prepared as independent scientific material for the core Yau‑26 effort. Target unchanged: for each `n≥2` produce dimension‑only constants `c_n<C_n` so that any closed connected smooth `M^n` with any smooth `g` satisfying `c_n g ≤ Ric_g ≤ C_n g` (quadratic‑form sense) carries *some* Einstein metric `h` (any sign of `λ`), equivalently `∀n (P_n^+ ∨ P_n^-)`. Everything below respects the exact quantifiers; restricted stability, ansatz nonexistence, and weighted/`L^p` residuals are treated as evidence, never as resolution.

I open with a strategic reordering that I think is the single most consequential point, then give genuinely distinct routes, each with mechanism, why it could be decisive, an early distinguishing observation, and the mechanism that would defeat it.

---

## 0. Strategic reordering: the plus branch is the natural place to attempt a PROOF, and it suffices

Because `Q_n ⟺ P_n^+ ∨ P_n^-`, **proving `∀n P_n^+` alone settles `∀n Q_n`.** The `σ=−1` branch is only needed as a backstop if the plus branch breaks in some dimension. This asymmetry deserves to reorganize priorities, because the plus branch carries three structural advantages that the minus branch does not.

1. **Automatic global structure.** `δ_+(g)≤ε<1` gives `Ric ≥ (1−ε)g>0`, hence Myers: `diam ≤ π√((n−1)/(1−ε))`, `π_1` finite, and Bishop–Gromov gives a dimension‑only volume *upper* bound. The minus branch has none of this: no diameter control, no volume control.

2. **The sign nullifies the known Einstein obstructions.** `δ_+` small forces `s = tr Ric ≥ n(1−ε)>0`, so the *input metric itself* has positive scalar curvature. Therefore the smooth manifold admits a PSC metric, so all Seiberg–Witten / monopole‑class Einstein obstructions of LeBrun type give nothing (the Weitzenböck argument kills SW under PSC). Meanwhile the Chern–Gauss–Bonnet gap already in the dossier (`δ_σ<1/(1+√3) ⇒ 2χ>3|τ|`) removes every Hitchin–Thorpe violator. In `n=4` this closes off *both* families of currently available topological obstructions to a plus‑branch counterexample. In `n≥5` essentially no obstruction to positive Einstein metrics is known at all.

3. **Consequence.** A plus‑branch counterexample would have to invent a brand‑new obstruction to *positive* Einstein metrics that also survives two‑sided Ricci pinching. That is a very heavy demand. The plus branch is therefore an existence/structure problem, not an obstruction problem, and existence/structure is where dimension‑only constants are believable.

The two remaining enemies on the plus branch are **collapse** and **Weyl energy concentration**. Sections 1–2 attack exactly these. The minus branch (Sections 3–5) is where I would keep the refutation program alive, because that is where obstructions can coexist with pinching and where flexibility is plausible.

I state now the central new conjecture that would carry the plus branch:

> **Conjecture N (anisotropy of collapse).** There is `ε_n>0` such that if `δ_+(g)≤ε_n` then `(M,g)` does not collapse in a genuinely non‑quotient way: any small‑volume behavior is realized by isometric finite quotients or homogeneous fibrations of near‑Einstein models, each of which itself carries an Einstein metric.

Evidence for N and its use follow.

---

## 1. Route C — plus‑branch existence by classifying pinched collapse (crosses the gap; uses only Ricci)

**Mechanism.** Split `δ_+`-small inputs by volume. In the *noncollapsed* regime (`Vol ≥ v_0`), two‑sided Ricci + noncollapse is exactly the regime where local `L^2` curvature control and orbifold Gromov–Hausdorff compactness hold (Cheeger–Naber in `n=4`; Anderson‑type in all `n` when the pinching is close). The GH limit is an Einstein orbifold with `s>0`; because `s>0` kills SW, the associated resolution obstructions of Biquard / Morteza–Viaclovsky / Ozuch are not forced to vanish by a topological wall but the *sign* environment is benign, and a direct perturbation of the near‑Einstein input (which is `C^0`-pinched, unlike Ozuch's `L^p`-only Example 1) becomes the target. In the *collapsed* regime one invokes bounded‑Ricci collapse structure (Naber–Tian type nilpotent/Seifert fibration away from a low‑dimensional singular set) and Conjecture N to reduce to Einstein‑carrying model total spaces.

**Why it could be decisive.** On the plus branch collapse is the *only* escape from compactness, and there is strong evidence collapse is essentially forbidden except through Einstein‑preserving quotients. If Conjecture N holds, the plus branch reduces to the noncollapsed Einstein‑orbifold picture with the favorable sign, and `∀n P_n^+` — hence `∀n Q_n` — comes into reach without ever bounding Weyl or assuming spectral data.

**Early distinguishing observation (cheap, decisive).** Compute Ricci principal values under fiber‑shrinking collapse and check compatibility with `δ_+` small.
- Berger 3‑sphere, left‑invariant `g_ℓ = ℓ²σ_1² + σ_2² + σ_3²`: Ricci principal values `(2ℓ², 2−ℓ², 2−ℓ²)` (round at `ℓ=1`, all `=2`). As the Hopf fiber collapses `ℓ→0`, the endomorphism eigenvalues spread to `{0, 4}` (their ratio `→0`), so the pointwise Ricci anisotropy `w=λ_max(A)−λ_min(A) → 4`. Since `w/|s|` is scale‑invariant, **no rescaling can keep the eigenvalues clustered near a common positive value while the fiber collapses.** Thus `δ_+` small *forbids* Hopf‑type collapse.
- Generalize: run the O'Neill/warped computation for shrinking an infranil fiber over a base; the O'Neill `A`-tensor injects order‑one Ricci anisotropy between fiber and base directions. Verify whether every non‑quotient bounded‑Ricci collapse forces `w` bounded below by a dimension constant. This is a finite family of homogeneous ODE/linear‑algebra computations that either establishes Conjecture N's mechanism or exhibits the one collapse channel that evades it.

The contrast case that must be honored: lens spaces `S^n/Γ` and homogeneous space‑form quotients collapse (`Vol→0` as `|Γ|→∞`) yet stay Einstein. So the correct target is *not* a volume lower bound (false), but the structural dichotomy in N: pinched collapse ⇒ Einstein‑carrying quotient/fibration.

**Where it breaks.** Bounded‑Ricci collapse (only `|Ric|≤C`, not `|Rm|≤C`) is far wilder than bounded‑sectional collapse; the nilpotent Killing structure theory is complete in low dimension but partial in high dimension. Passing from "collapsed model exists" to "Einstein metric exists on the same smooth `M`" is the classic hard step. And in the noncollapsed part, converting a `C^0`-pinched near‑Einstein metric into an exact solution still confronts near‑kernel (infinitesimal Einstein deformations of the limit orbifold), which is where uniform invertibility can degrade.

---

## 2. Route G — global elliptic Ricci‑to‑metric stability with dimension‑only constants (plus and minus branches)

**Mechanism.** Ozuch's Appendix inequality is a *local* elliptic stability estimate: near a constant‑curvature model `g_0`, `‖Φ*g − g_0‖_{C^{k+1,α}} ≤ C‖Ric(g) − (n−1)g‖_{C^k}` in divergence gauge, with `C` depending only on the model. Introduce the pointwise Ricci‑anisotropy field `w(x)=λ_max(A_g(x))−λ_min(A_g(x))`; `δ_σ` small `⟺` `w` small and `tr A ≈ nσ`. The route is to globalize Ozuch's estimate around *the nearest Einstein metric* rather than a fixed model, with the near‑kernel (infinitesimal Einstein deformations) split off as a finite‑dimensional bundle. The nonlinear implicit‑function template `βη + βKρ² ≤ ρ`, `2βKρ<1` then needs only that the reduced (Lyapunov–Schmidt projected) linearized operator has an inverse bounded by a dimension‑only `β` after removing the finite‑dimensional near‑kernel.

**Why it could be decisive.** It targets exactly the mechanism the dossier identifies as the reason "small residual ⇒ solution" ruptures: the growth of `β(t)` (inverse operator norm) as geometry degenerates. If one can show the near‑kernel is finite‑dimensional and the transversal inverse is dimension‑controlled *whenever `δ_σ` is small*, the branch closes. It uses only Ricci data plus the second Bianchi identity (which converts the traceless‑Ricci elliptic system into a self‑improving one).

**Early distinguishing observation.** Test the transversal inverse bound on the two model degenerations that are already understood in closed form: (i) the Calabi/Eguchi–Hanson bubble, where the one‑dimensional decaying infinitesimal deformation `o` and the reduced obstruction `λ ∝ (2−n)Λ/2 − (1/8)⟨R(ω),ω⟩` (Morteza–Viaclovsky) are explicit; (ii) the `H²×H²` product on the minus branch. In each, compute whether the transversal linearized Einstein operator's inverse is bounded independently of the degeneration parameter after removing `span(o)`. If yes, the near‑kernel is genuinely finite and controllable; if the transversal inverse itself blows up, the route needs a redesigned function space.

**Where it breaks.** Collapse destroys uniform Sobolev/Poincaré constants; the near‑kernel need not be finite‑dimensional under collapse; and "nearest Einstein metric" may not exist for an input far from every Einstein metric (the whole difficulty of an existence, not a stability, statement).

---

## 3. Route B/E — the minus‑branch refutation program as a compatibility question: pinching budget vs. surviving obstruction

**Mechanism.** To refute `Q_n` one must, in a *single fixed* `n`, defeat both branches; by Section 0 the plus branch resists, so a refutation must at minimum defeat `P_n^-` and then separately defeat `P_n^+` in the same `n`. Focus first on `P_n^-`: build, in fixed `n`, a family `(M_j,g_j)` with `δ_-(g_j)→0` where `M_j` carries no Einstein metric of any sign. The only sign‑independent obstruction available in `n=4` is Seiberg–Witten/LeBrun (Hitchin–Thorpe is already forced by the CGB gap). On the minus branch `s ≈ −n < 0`, so PSC does *not* hold and SW obstructions can survive. The compatibility question is quantitative: LeBrun's inequalities bound topological quantities by `∫ s²` and by the self‑dual Weyl energy `∫|W^+|²`. With `δ_-` small, `∫ s² dV ≈ n² Vol` and `E` (traceless Ricci) is small, but **`W^+` is completely uncontrolled** by Ricci pinching. So the manifold can carry large `∫|W^+|²` and thread LeBrun's Einstein inequality while remaining `δ_-`-pinched — genuine room for a counterexample if the input metric can be built.

**Why it could be decisive.** It cleanly decouples the two hard halves: (a) *existence of the pinched input* is a flexibility problem (Route E below); (b) *nonexistence of Einstein* is SW theory, where LeBrun manifolds (e.g., blown‑up minimal surfaces of general type, satisfying HT yet Einstein‑free) are already available. If the input can be built with `δ_-→0` on such an `M`, `P_4^-` is refuted.

**Early distinguishing observation (the flexibility/rigidity test, decisive and cheap).** Ask whether *tight* minus‑branch pinching is even locally possible. For a cohomogeneity‑one warped model `g = dt² + φ(t)² g_{S^{n-1}}` (unit fiber), the Ricci endomorphism eigenvalues are `−(n−1)φ''/φ` (radial) and `[−φφ'' + (n−2)(1−(φ')²)]/φ²` (spherical). Imposing `Ric = −g` gives `φ''=φ/(n−1)` and then
`(φ')² = 1 + φ²/(n−1)`, i.e. `φ(t)=√(n−1)\sinh(t/√(n−1))` — **exactly hyperbolic space.** So every rotationally symmetric exact minus‑branch solution is hyperbolic; there is no symmetric neck freedom at `Ric=−g`. With `ε`-slack, quantify how much sphere‑direction anisotropy a neck can carry: this measures the pointwise Ricci deviation forced by any nontrivial cohomogeneity‑one transition. If the forced deviation is bounded below by a dimension constant, tight minus‑branch surgery is *rigid* and counterexamples must be genuinely non‑symmetric — strong evidence toward `P_n^-` being true. If long adiabatic necks dilute the deviation to `o(1)`, the refutation program is alive.

**Where it breaks.** The very device that dilutes anisotropy — long necks — is exactly what Anderson–Bamler Dehn filling uses to produce *actual* Einstein metrics. Dilution of Ricci‑anisotropy and existence of Einstein metrics may be the same phenomenon, in which case pushing `δ_-→0` tends to hand back an Einstein metric rather than an obstructed one. Also, Ozuch's Example 1 warns that `L^p`-smallness with a matched GH limit is *not* `C^0` `δ_-`‑smallness, and "no nearby Einstein" is not "no Einstein anywhere on `M`," which is what `Q_n` requires.

---

## 4. Route E (sharpened) — the tight‑flexibility function as the pivotal unknown

**Mechanism.** Define `Φ_n^-(M) = inf_g δ_-(g)` over all smooth metrics on closed `M`. Lohkamp/Gao–Yau give `Ric<0` on every `M`, but their constructions are highly anisotropic and do not control the eigenvalue ratio toward `1`. The decisive dichotomy:
- **Tight flexibility** (`Φ_n^-(M)=0` for all `M`): then any Einstein‑free `M` (e.g. `n=4` LeBrun manifolds; higher `n` via suitable products/fibrations of such) refutes `P_n^-`.
- **Rigidity** (`Φ_n^-(M) ≥ φ_n>0` uniformly): strong evidence for `P_n^-`, and by Section 0 an even stronger case for `Q_n` overall.

**Why it could be decisive.** It isolates a single scalar dichotomy whose resolution flips the entire minus‑branch question, and it is exactly the quantity Lohkamp‑type technology is built to address (but has not addressed in the *tight* regime).

**Early distinguishing observation.** Combine the neck ODE of Section 3 with a handle‑decomposition realization of a target `M`: attempt an explicit long‑neck interpolation between two hyperbolic pieces of differing cross‑section geometry and measure the sup‑norm Ricci deviation as neck length `L→∞`. The rotational rigidity says symmetric necks cannot help; the test is whether *slowly varying* cross‑sections give deviation `O(1/L)`. This is a controlled variational‑ODE computation that directly estimates `Φ_n^-`.

**Where it breaks.** If the deviation cannot be driven below a dimension constant (rigidity), the refutation program stops here — which is itself a high‑value outcome pointing at a proof.

---

## 5. Route A — removing Min‑Oo's `Λ` by multiscale/covering `L²` Bochner (minus‑branch existence)

**Mechanism.** Min‑Oo proves a minus‑branch stability theorem whose only non‑dimensional inputs are (i) short‑time flow control via `d²max|K|<Λ²`, and (ii) the Sobolev constant via the Gallot–Gromov isoperimetric inequality, which needs a diameter *upper* bound with Ricci lower bound. His reaction coefficient in the `L²` inequality for `h=Ric−(r/n)g` is `r(0)≈−n`, a genuine dimension‑only constant. The route: replace the *global* Moser/Sobolev step by a covering‑scale, thick/thin (Margulis) `L²` estimate in the spirit of Jäckel's removal of diameter/volume/injectivity dependence, so that the `−r(0)|h|²` reaction dominates the curvature error *locally at the Ricci scale* without ever invoking `max|K|` or a global diameter bound.

**Why it could be decisive.** It aims straight at the two non‑dimensional inputs and keeps the favorable dimension‑only reaction term. Jäckel's work already shows three of Min‑Oo's dependences (global diameter, volume, injectivity radius) are removable in principle; the target is to remove the last full‑sectional and thin‑part structural inputs and reach a genuinely `n`-only threshold.

**Early distinguishing observation.** On `H²×H²` (exactly `Ric=−g`, mixed sectional curvatures zero, `max|K|` bounded while diameter `→∞` as genus grows), Min‑Oo's `Λ=d²max|K|→∞` even though the conclusion (an Einstein metric) plainly holds. Build small `δ_-→0` deformations of this product and test whether the covering‑scale `L²` reaction argument controls them uniformly. Success here means the `Λ`-dependence is a method artifact, not a real obstruction.

**Where it breaks.** On the minus branch Weyl can concentrate at small scales, injecting high‑frequency curvature energy that the `L²` reaction cannot absorb; universal covers have exponential volume growth complicating preimage counting; and there is no guarantee a stationary point of the flow (an Einstein metric near `g`) exists when `g` is far from every Einstein metric — the flow could translate off to a degenerate limit.

---

## 6. Route D — a parity/degree count for the Einstein operator robust to bubble trees

**Mechanism.** Treat the traceless‑Ricci section `F(g)=Ric_g−(s/n)g` (in a diffeomorphism gauge) as a Fredholm section over the space of pinched metrics; a `δ_σ`-small `g` is an approximate zero. The obstruction to an exact zero is captured by a Lyapunov–Schmidt reduced map onto the near‑kernel. Ozuch's main theorem (included) states that every Einstein metric GH‑close to an orbifold is *explicitly* a gluing‑perturbation, so the Einstein moduli near any degeneration is finitely parametrized by bubble‑tree data. This makes a *local* degree/parity contribution computable per bubble tree; sum to a global mod‑2 or Euler‑class count for `M`, whose nonvanishing forces an exact Einstein metric.

**Why it could be decisive.** It converts existence into a topological count that can be robust to bubbling if bubble contributions are `0` or `±1`, sidestepping the need for a priori compactness of the full moduli.

**Early distinguishing observation.** Compute the local reduced‑map degree at the simplest bubble: the Calabi/Eguchi–Hanson gluing, where the reduced obstruction is the explicit `λ` of Morteza–Viaclovsky and its zero set is Biquard's `det R=0` wall. Determine whether crossing this wall changes a local parity by `1` (nontrivial contribution) or `0`.

**Where it breaks.** Moduli noncompactness is the entire difficulty; the count needs properness that pure Ricci pinching does not supply. The sign of `λ` is not fixed, so contributions may cancel; and diffeomorphism‑gauge and sign‑of‑`λ` freedom can trivialize the invariant.

---

## 7. Complex‑geometry laboratory (sign‑map, not a solution)

Kähler geometry sharpens *which topologies are safe* rather than producing counterexamples. Any smooth 4‑manifold admitting a complex structure with `c_1<0` carries an Aubin–Yau Einstein metric, so such topologies can never be minus‑branch counterexamples; `c_1=0` gives Calabi–Yau; Fano `⟺` K‑polystability gives the positive case. This means a refutation must *avoid every* complex structure with definite `c_1` sign on the underlying smooth manifold — a strong structural filter on candidate `M`. It also provides controlled near‑minus‑Einstein inputs (metrics in a Kähler class near the KE class on a `c_1<0` surface) with which to numerically probe the LeBrun–Weyl compatibility budget of Section 3 on genuinely non‑Kähler smoothings.

---

## 8. Cross‑field transfer: metric‑measure (RCD) almost‑rigidity for the plus branch's collapse enemy

**Mechanism.** The plus branch supplies `Ric ≥ (1−ε)g>0`, exactly a synthetic Bakry–Émery/RCD lower bound, plus a two‑sided pinching that is unusual in that theory (upper Ricci bounds are not GH‑stable). Use Cheeger–Colding / Lichnerowicz–Obata almost‑rigidity: in the noncollapsed case `δ_+` small forces GH‑closeness to a spherical suspension / round‑quotient, and the *two‑sided* bound upgrades this to metric closeness. This is a toolset that needs only Ricci lower bounds (which we have) and could give a synthetic handle on the collapse dichotomy of Conjecture N without any full‑curvature or spectral hypothesis.

**Early distinguishing observation.** Test whether the two‑sided Ricci pinching yields a *synthetic* obstruction to collapse: in the RCD framework, does `δ_+` small force a uniform lower bound on the `n`-dimensional density of the limit measure except along isometric quotients? The Berger computation of Section 1 is the concrete finite model this synthetic statement must reproduce.

**Where it breaks.** RCD theory has no stable notion of a Ricci *upper* bound; encoding the two‑sided pinching synthetically is itself research, and the passage from a synthetic limit to a smooth Einstein metric on `M` is unaddressed.

---

## Consolidated decisive early computations (they reorder priorities cheaply)

1. **Fiber‑collapse Ricci anisotropy (plus branch, Route C / Conjecture N).** Berger `S^3` already shows eigenvalue ratio `→0` under Hopf collapse; extend to general infranil‑fiber/O'Neill collapse and homogeneous fibrations. Outcome sets whether `δ_+`-collapse is confined to Einstein‑carrying quotients.
2. **Rotational minus‑branch rigidity ODE (Routes B/E).** `Ric=−g` cohomogeneity‑one ⇒ `(φ')²=1+φ²/(n−1)` ⇒ hyperbolic; then quantify `ε`-slack anisotropy of any nontrivial neck. Outcome sets whether tight minus‑branch surgery is rigid or flexible.
3. **LeBrun inequality vs. the `δ_-` pinching budget (Route B).** With `s≈−n`, `E` small, and `W^+` free, check numerically whether an Einstein‑free HT‑satisfying 4‑manifold can host large `∫|W^+|²` while `δ_-→0`. Outcome sets whether an SW obstruction can coexist with tight minus‑branch pinching.
4. **`H²×H²` deformation obstruction (Routes A, G).** Build `δ_-→0` deformations and test uniform transversal invertibility / covering‑scale `L²` control. Outcome distinguishes "`Λ`-dependence is a method artifact" from "real high‑frequency obstruction."

The through‑line: the plus branch looks like a provable existence/structure statement once collapse is understood, and proving it alone finishes `Q_n`; the minus branch is where refutation could live, but the local rotational rigidity and the dilution‑equals‑existence tension both currently point toward the minus branch also being an existence statement. The four computations above are inexpensive and would sharply reweight which of these pictures to pursue at full cost.
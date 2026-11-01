# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md"
  ]
}
```

## Task

Generate a concrete mechanism for using harmonic self-dual 2-forms to force covering noncollapse in 4D near-negative-Einstein collapse.

SETUP: On a fixed critical Ishida-LeBrun 4-manifold with δ_i = ||Ric_i + g_i||_∞ → 0:
- There exist near-harmonic self-dual forms H with nearly constant amplitude |H| ≈ const
- The Weitzenböck identity gives ∫|∇H|² = (1 + O(δ))∫|H|² (for the simple eigenform)
- On a collapsed region, the Bochner identity for nearly constant amplitude gives |∇H|² ≈ |H|² pointwise
- The eigenline direction rotates at O(1) rate in base directions (not fiber directions)

QUESTION: Can these properties of the forms (controlled amplitude, controlled gradient energy, eigenline rotation) force the local universal cover to be noncollapsed? Or can a collapsed cover accommodate all these properties?

Consider:
1. Whether the forms define a topological obstruction to collapse (e.g., through Euler class of the eigenline bundle)
2. Whether the O(1) horizontal rotation rate constrains the topology or geometry of the collapse base
3. Whether nearly constant amplitude + approximate harmonicity + controlled gradient produces a Bochner-type constraint on the covering fundamental group
4. Whether the three independent near-harmonic forms (when b₂⁺ ≥ 3) can constrain the collapse rank
5. Explicit collapsed models (torus bundles over surfaces, nilmanifolds) and whether they can support forms with these properties

Produce specific mathematical mechanisms, not general strategy.

## Output

## The central tension you have already surfaced, made sharp

Your Weitzenböck computation says the calibrated simple eigenform has $\int|\nabla\sigma_1|^2=(1+O(\delta))\int|\sigma_1|^2$, i.e. an $O(1)$ rotation rate, not a parallel form. The most productive way to use this is not to look for a topological invariant that a collapse cannot carry (self-dual forms genuinely mix vertical and horizontal indices, so $\Lambda^2_+$ is *not* pulled back from the base and $p_1(\Lambda^2_+)=2\chi+3\tau$ can be carried by fiber$\wedge$base wedges — a direct Euler-class-pullback argument does not close). The leverage is that **the $O(1)$ rotation is exactly what the simplest collapse geometries cannot produce while keeping the form of constant length, and the geometries that can produce it are pinned to the wrong Weyl spectrum.** Below are concrete mechanisms and the explicit computations that decide each one.

## Mechanism 1 — The Ricci sign forbids bundle-curvature collapse and forces warped/nilpotent (cusp-type) collapse

The hypothesis is $\operatorname{Ric}\approx -g$ in *every* direction, including the collapsing ones. This is a strong structural filter that the current notes do not yet exploit. Run O'Neill's submersion formulas explicitly for a shrinking fiber $F$ of scale $\ell$:
$$
\operatorname{Ric}(V,V)=\widehat{\operatorname{Ric}}(V,V)-\langle\nabla_V H,V\rangle-|T_V|^2+|A_{\cdot}V|^2+\dots
$$
Two facts fall out. First, collapse driven by horizontal-distribution curvature (the $A$-tensor, the Berger/Hopf mechanism) contributes $+|A|^2\ge0$ to the vertical Ricci — it pushes the collapsing directions toward *positive* curvature (the shrinking Hopf circle of $S^3$ is the model). You need $-1$ there. Second, intrinsic flat fibers give $\widehat{\operatorname{Ric}}=0$. The only way to obtain $\operatorname{Ric}\approx-1$ along a collapsing direction is the *warping/mean-curvature* term, i.e. the fiber must shrink like a hyperbolic-cusp cross-section, $g\approx dr^2+f(r)^2 g_F$ with $f\sim e^{-r}$, or the two-step warped Heisenberg profile of a complex-hyperbolic cusp. This is decisive scientific content: **negative Einstein collapse is cusp-like (warped, diameter $\to\infty$, finite volume), not F-structure-by-bundle-twist.** It matches your Step 6 conclusion that diameter must diverge while volume stays $32\pi^2A/9$, and it tells you which model families to test. The concrete computation to record: for warped products $dr^2+f^2g_F$ with $F$ flat $T^{k}$ and with $F$ a Heisenberg nilmanifold, solve $\operatorname{Ric}=-g$ for $f$ and the fiber scaling exponents, and read off $W^+$. The real-hyperbolic cusp ($F=T^3$, single warp) gives $W\equiv0$; the complex-hyperbolic cusp ($F=\mathrm{Nil}^3$, two warping rates $e^{-2r},e^{-4r}$) gives the Kähler spectrum. Neither is the calibrated spectrum. This is the geometric shape of the whole question.

## Mechanism 2 — Constant-length harmonic self-dual forms are parallel on flat-fiber collapse (rules out abelian F-structures directly)

Test the flat torus-bundle collapse concretely on $\Sigma^2\times T^2$ (and its twisted versions). Compute the harmonic 2-forms by Künneth:
$$
\mathcal H^2 = \big(H^2(\Sigma)\otimes H^0(T^2)\big)\oplus\big(H^1(\Sigma)\otimes H^1(T^2)\big)\oplus\big(H^0(\Sigma)\otimes H^2(T^2)\big).
$$
The self-dual constant-length combinations are only $\tfrac1{\sqrt2}(\mathrm{vol}_\Sigma+\mathrm{vol}_{T^2})$ and its rotations *within* the mixed piece $H^1(\Sigma)\otimes H^1(T^2)$. On a hyperbolic $\Sigma$ the harmonic 1-forms have **non-constant pointwise length**, so every mixed harmonic self-dual form has non-constant length. Hence the *only* constant-length harmonic self-dual form is the diagonal volume combination, and it is **parallel**, $\nabla\sigma=0$. This contradicts $\int|\nabla\sigma_1|^2\approx\int|\sigma_1|^2$. The general statement to prove and record: on any collapse whose local cover is an approximately flat torus bundle, a constant-length harmonic self-dual form must be a parallel diagonal form, incompatible with the $O(1)$ Weitzenböck rotation. This eliminates the abelian F-structure branch of the collapse cleanly and directs everything to nilpotent fibers.

## Mechanism 3 — The Nomizu/Lie-algebra classification of invariant self-dual forms on nil collapse (the centerpiece computation)

Once abelian collapse is out and the Ricci sign forces nil/cusp warping, the surviving models collapse along nilmanifold fibers, and Fukaya's convergence of forms says the surviving harmonic forms are the invariant ones — computed by Lie-algebra cohomology (Nomizu). This makes "can a collapsed cover accommodate all these properties?" a **finite, explicit computation** rather than a general regularity question.

Set it up for the 3-dimensional Heisenberg algebra $\mathfrak{n}$ with coframe $e^1,e^2,e^3$, $de^3=e^1\wedge e^2$, warped over a radial $e^0=dr$ with fiber scalings $e^1,e^2\sim e^{-r}$, $e^3\sim e^{-2r}$ (the complex-hyperbolic cusp profile). Enumerate the invariant self-dual 2-forms
$$
\sigma=\alpha_1(e^0\wedge e^1+e^2\wedge e^3)+\alpha_2(e^0\wedge e^2+e^3\wedge e^1)+\alpha_3(e^0\wedge e^3+e^1\wedge e^2),
$$
with $\alpha_a=\alpha_a(r)$, impose constant length ($\sum\alpha_a^2=$const) and $d\sigma=0=d{*}\sigma$ using $de^i$ from the structure constants and the warping, and compute (i) $\nabla\sigma$ and (ii) the $W^+$-eigenstructure it forces through the endomorphism Weitzenböck identity you already use in Step 6. The scientific payoff is a trichotomy you can actually establish: each invariant constant-length harmonic self-dual form on a nil-warped negative-Einstein cusp is either parallel (Kähler branch, spectrum $(-2/3,1/3,1/3)$), or has non-constant length (excluded), or has $O(1)$ rotation but forces a spectrum that solves the invariant Einstein–Weyl relations only at the Kähler point. If the calibrated spectrum $(-1/6,1/12,1/12)$ never appears in this finite list, you will have shown that no invariant self-dual eigenform on a negative-Einstein nil collapse is calibrated — the exact analog of your smooth projector lemma, but on the collapsed limit where the projector lemma itself does not apply. This is the missing piece: the projector obstruction lives on smooth Einstein charts; the Nomizu computation extends it to the invariant (collapsed) limit.

Do the same for the 2-step and abelian 3-dimensional algebras, and for rank-2 fibers over a surface with the warped/twisted profiles compatible with $\operatorname{Ric}\approx-1$. The full table of $(\text{Lie algebra}, \text{warping}, \text{invariant self-dual spectra}, \nabla\sigma)$ is a finite, checkable object.

## Mechanism 4 — Parity of the collapse rank via the induced almost-complex structure

The constant-length simple eigenform $\sigma_1$ (norm bounded away from zero on the good set) is exactly a compatible almost-complex structure $J$, $\sigma_1(\cdot,\cdot)=g(J\cdot,\cdot)$, and near-harmonicity makes $J$ nearly integrable. A complex structure preserves only even-dimensional subspaces. This gives a clean rank dichotomy for the collapsing fiber $F$:

- **Even rank ($\dim F=2$):** $J$ can preserve $TF$, i.e. the collapse is a holomorphic (elliptic) fibration. Then $J$ is nearly fiber-invariant, $\sigma_1$ is nearly parallel along and across in the Kähler direction, and the spectrum runs toward the Kähler value $(-2/3,1/3,1/3)$ — not calibrated. Your calibrated-spectrum defect $\int F_i\to0$ then bounds the volume of this branch.

- **Odd rank ($\dim F=1$ or $3$):** $J$ *cannot* preserve $TF$; it must rotate the (collapsing) vertical direction into a horizontal one. This forces the $O(1)$ base rotation you computed — so the odd-rank branch is the only one *consistent* with the calibrated Weitzenböck rotation. But then $F$ is not a $J$-complex fiber, the collapse is not holomorphic, and you are back in the nil/warped odd-fiber setting handled by Mechanism 3.

This parity statement is worth stating precisely because it explains *why* your rotation is $O(1)$ (dimension parity, not an accident) and channels the entire problem into the odd-fiber nilpotent case, where Mechanism 3 is a finite computation.

## Mechanism 5 — b₂⁺ ≥ 3: three orthogonal forms as a near-quaternionic frame and the rank ceiling

When $b_2^+\ge3$ you have $H_1,H_2,H_3$ pairwise $L^1$-orthogonal (your Walsh estimate (47)) and near-constant amplitude, i.e. an approximate orthonormal frame of $\Lambda^2_+$ on the good set — a near-quaternionic triple $(I,J,K)$, $IJ=K$. Two concrete consequences. First, the three complex structures cannot all preserve a common $2$-plane, so a rank-2 holomorphic collapse compatible with all three is impossible: the even-rank Kähler escape of Mechanism 4 is closed once $b_2^+\ge3$, leaving only odd-rank nil collapse for Mechanism 3. Second, on the collapsing fiber $F$ with generator $\xi$ (the collapse Killing-type field), $\xi, I\xi, J\xi, K\xi$ span $TM$; if the frame is nearly parallel along $\xi$ (vertical derivative $O(\ell)$, which you established), then $I\xi,J\xi,K\xi$ are nearly Killing as well, forcing a near-4-dimensional local isometry algebra — a homogeneous/symmetric local model. Check which negative-Einstein homogeneous 4-geometries (real and complex hyperbolic, and the solvable/nil Lie-group Einstein metrics) can appear as such collapse limits, and compute their $W^+$ spectra. The prediction from Mechanisms 1–3 is that they land on $0$ or the Kähler value, never calibrated. This turns $b_2^+\ge3$ into a genuine rank ceiling plus a homogeneous-model finiteness statement, both computable.

## Mechanism 6 — The literature engine you should pull in: Cheeger–Tian Einstein-4 collapse regularity

The one external result that could convert the above from "these particular models cannot" into "no collapse can" is the Cheeger–Tian theory of curvature and injectivity-radius estimates for Einstein four-manifolds (Cheeger–Tian, *J. AMS* 2006, and the earlier Cheeger–Tian annulus/$\varepsilon$-regularity work; also Anderson's Einstein-4 collapse papers and Naber–Tian on Einstein collapse to orbifolds). Their $\varepsilon$-regularity for Einstein four-manifolds does *not* require noncollapse as input — it uses the Einstein equation itself through the second Bianchi identity — and concludes that collapse of Einstein four-manifolds with bounded $\int|\mathrm{Rm}|^2$ proceeds along nilpotent/flat F-structures with curvature concentrated on a controlled set. This is precisely the input that would justify Mechanism 3's reduction to invariant nil geometry on your bounded-energy good set. The high-value question to resolve is stability: **does the Cheeger–Tian $\varepsilon$-regularity survive the near-Einstein perturbation $\|\operatorname{Ric}+g\|_\infty=\delta_i\to0$?** Their proof is elliptic and quantitative, so a perturbation with $\int F_i\to0$ is a natural setting to test. If yes, then the good set either is noncollapsed (your projector obstruction closes it) or collapses along a nil F-structure (Mechanisms 3–5 close it), and the negative branch is finished. This is a far more direct route than the raw "controlled maximal $\int|\mathrm{Rm}|^2$ at every scale forces noncollapse" question, which is genuinely delicate in the critical 4D Sobolev situation and may have collapsing countermodels.

## Mechanism 7 — Cusp decay of the rotation and the volume accounting of the near-Kähler tip

One more concrete constraint links the diameter divergence to the spectrum. On a cusp end (rank-3 warped), $\int_{\text{end}}|\nabla\sigma_1|^2\,d\mu\le\int|\sigma_1|^2<\infty$ while the radial length is infinite, so the rotation rate must decay along the end (like $e^{-r}$). Where the rotation decays, $\sigma_1$ becomes asymptotically parallel, hence asymptotically Kähler, and the $W^+$ spectrum drifts to $(-2/3,1/3,1/3)$, away from calibrated. The calibrated-spectrum defect density is then $O(1)$ on the deep-cusp region, so $\int F_i\to0$ forces the deep-cusp volume to vanish. Consequently the good set (definite volume, genuine $O(1)$ rotation, calibrated spectrum) lives in the *moderate* region, not the tip. This is a useful localization: it says the decisive geometry is a bounded-energy, definite-volume, $O(1)$-rotating region — exactly where Cheeger–Tian structure (Mechanism 6) plus the Nomizu computation (Mechanism 3) apply. Record the volume-versus-defect inequality explicitly: $\int_{\text{tip}}|\text{Spec}(W^+)-(-1/6,1/12,1/12)|^2\,d\mu\ge c\cdot\mathrm{Vol}(\text{tip})$, and combine with $\int F_i\to0$.

## What to compute first, and what each computation decides

The cheapest decisive computation is Mechanism 3's Nomizu table: it is a finite Lie-algebra-cohomology plus warped-product curvature calculation (well suited to the symbolic tools), and it directly answers "can a collapsed cover carry a calibrated $O(1)$-rotating constant-length self-dual harmonic form?" for the only fiber types the Ricci sign allows. If the calibrated spectrum is absent from that finite list, you have the collapsed analog of the projector lemma. The Cheeger–Tian stability question (Mechanism 6) is the higher-value but harder input that would make the reduction to invariant nil geometry rigorous; it is worth a focused reading of whether their $\varepsilon$-regularity constants degrade under $\delta_i\to0$. Mechanisms 4 and 5 (parity and the quaternionic rank ceiling) are short structural arguments that decide which fiber ranks even need testing and should be settled before the heavy computation, since they may collapse the case list to odd-rank nil alone.

Two honest unresolved points to keep in view. The claim "$\Lambda^2_+$ approximately pulled back from the base" is false, so any argument must use the fiber-mixing of self-dual forms rather than a pullback Euler-class count. And the constant-length-implies-parallel statement (Mechanism 2) is proven for flat fibers over a hyperbolic surface; extending it to warped nil fibers is exactly the content of Mechanism 3 and is not automatic — the warping is what allows $O(1)$ rotation without non-constant length, which is why the Kähler/complex-hyperbolic model exists at all. The whole question is whether that same warping can be tuned to the calibrated spectrum rather than the Kähler one, and the Nomizu computation is the instrument that settles it.
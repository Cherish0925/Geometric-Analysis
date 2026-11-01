# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step11_chart_accessibility_and_energy.md",
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A01/workspace/notes/step10_accessible_cover_reassessment.md"
  ]
}
```

## Task

The four-dimensional negative-branch Yau 26 program has reached a precise impasse. On a hypothetical near-critical Ishida-LeBrun sequence (M_i, g_i) with Ric ≈ -g and the calibrated W+ spectrum (-1/6, 1/12, 1/12), the following is established:

1. Chart-accessible exclusion: any point admitting a noncollapsed harmonic chart on a normal cover at fixed scale is excluded by the Derdziński/projector contradiction. Noncollapsed volume → 0.

2. Noether energy bound: global mean |Rcal|² ≤ 12 for all minimal general-type surfaces (verified, no family restriction).

3. Taub-NUT-AdS countermodel (S0910A03): controlled maximal ∫|Rm|² at every scale does NOT imply noncollapse on the local universal cover. The collapsing ψ-circle is contractible through the NUT, so the local universal cover remains collapsed. Maximal fibered rank is an independent geometric hypothesis.

4. Weitzenböck gradient energy (S0910A03): harmonic self-dual 2-forms at the calibrated spectrum have ∫|∇H|² = ∫|H|² (simple eigenform) and 3/2·∫|H|² (double), so forms are NOT nearly parallel. The O(1) rotation rate lives in base directions.

5. Flat rank ≥ 2 collapse is excluded by the definite-pair mechanism (independent SD forms with nondegenerate Gram matrix + closedness + constant amplitude → ∇→0, contradicting Weitzenböck).

The MISSING MECHANISM is how to exclude the remaining collapsed volume on a CLOSED manifold, where the Taub-NUT-AdS countermodel doesn't apply. A03 proposes Pontryagin localization: p₁(Λ²₊) integrates to 4π²(A-k) ~ 8π²A/3 → ∞, and this charge must concentrate on regions where W⁺ is non-basic (not pulled back from a collapsed base of dim ≤ 3). On basic-form collapse regions, Ω_+ ∧ Ω_+ = 0.

Generate NEW MECHANISMS or APPROACHES for converting the closed-manifold topology (monopole structure, Pontryagin localization, controlled Weitzenböck rotation, growing topological charge, Seiberg-Witten near-saturation) into a contradiction with the existence of the entire collapsed near-critical sequence. Consider:

a) Can the Pontryagin charge budget give a quantitative lower bound on the volume of non-basic or high-curvature regions?

b) Does the Seiberg-Witten monopole structure constrain which collapse modes are compatible with near-saturation?

c) Can the eigenline rotation mechanism from the Weitzenböck analysis, combined with the closed-manifold holonomy constraints, exclude rank-1 collapse?

d) Is there a topological or geometric obstruction to having all volume in rank-0 (contractible fiber) collapse on a closed manifold?

e) Can the interaction between W⁺ near-saturation and W⁻ energy (from signature) give additional constraints?

Seek mechanisms that use the SPECIFIC CLOSED MANIFOLD STRUCTURE, not general regularity. The goal is either a proof that the near-critical sequence cannot exist, or a precise identification of which geometric structures can still survive.

## Output

## The actual geometric picture the sequence must realize

Before proposing mechanisms, it helps to fix what a hypothetical near-critical sequence looks like once the chart-accessible exclusion and the energy bookkeeping are combined, because that picture already narrows the surviving structures sharply.

Volume is pinned at $\operatorname{Vol}(M_i,g_i)\to\tfrac{32}{9}\pi^2A$, a fixed number for fixed topology, while noncollapsed volume proportion $\to0$. A fixed 4-volume that is everywhere locally thin is only possible if the diameter diverges: the metrics spread into long thin regions. So the sequence is a *degeneration of a fixed closed $M$ with diameter $\to\infty$, everywhere locally collapsed, at fixed 4-volume* — the pinching-along-fibers picture of Cheeger–Fukaya–Gromov, not a bounded-diameter concentration.

Second, curvature is not everywhere bounded, but the unbounded part is confined to $W^-$. Near-saturation pins $s$, $\operatorname{Ric}$, and $|W^+|$ pointwise (calibrated), while the signature integral $\int(|W^+|^2-|W^-|^2)=12\pi^2\tau$ with $\tau(M)=\tau(X)-k$ forces $\int|W^-|^2\sim cA$ large. So $W^-$ is the reservoir that carries the excess energy. By $\varepsilon$-regularity for the anti-self-dual curvature, $W^-$ concentration is quantized: at most $O(A)$ points absorb bubbles, and each bubble is an *anti-self-dual* ($W^+\to0$) ALE/ALF gravitational-instanton neck. On $M=X\#k\overline{\mathbb{CP}}^2$ with $k\sim A/3$ these are exactly the $\overline{\mathbb{CP}}^2$ blow-up necks. Between bubbles, full curvature is bounded and a local N-structure exists.

Third — a point worth stating precisely because it sets the target — the calibrated spectrum $(-1/6,1/12,1/12)$ is *proportional* to the Kähler–Einstein self-dual spectrum $(-2/3,1/3,1/3)$ (at $s=-4$), scaled down by exactly $1/4$: same shape (simple minus, double plus, ratio $-2:1$), one quarter the size. So $|W^+|^2_{\text{cal}}=\tfrac1{24}=\tfrac14|W^+|^2_{\text{KE}}$. The forbidden germ is "Kähler-shaped self-dual Weyl at sub-Kähler amplitude with $\operatorname{Ric}=-g$." Neither real-hyperbolic ($W^+=0$), complex-hyperbolic ($|W^+|^2=\tfrac23$), nor any listed homogeneous Einstein model sits at this amplitude. That is precisely why the germ is impossible in the noncollapsed limit, and it is the fact the collapse models must be tested against.

With this picture, here are mechanisms that use the closed structure rather than general regularity.

## Mechanism 1 — Fiber-volume monotonicity from $\lambda<0$: the maximum principle closes abelian and low-twist collapse on a closed manifold

This is the sharpest tool and it directly uses closedness. Lott's orbit-volume identity for an exact isometric $\mathbb R^N$-action with orbit-volume $v=\sqrt{\det G}$ under $\operatorname{Ric}=\lambda g$ reads
$$
\Delta_B\, v=\Bigl(\tfrac{|F|^2}{4}-\lambda N\Bigr)v .
$$
At $\lambda=-1$ both terms on the right are strictly positive: $\Delta_B v=(\tfrac{|F|^2}{4}+N)v>0$ wherever $v>0$. Over a **closed base** integration gives $0=\int_B\Delta_B v=\int_B(\tfrac{|F|^2}{4}+N)v>0$, an impossibility. So no isometric torus collapse over a closed base is compatible with $\lambda<0$. The interval/cusp models escape only because their base is an interval or a parabolic surface with an end, where $v$ is allowed to grow without bound.

The nontrivial extension I want to push is the **local, action-free version**. In a CFG collapse the N-structure orbits are only locally defined, but the orbit-volume function $v$ (the density of the local nilpotent orbit) is a genuine local function, and the same Bochner-type identity holds locally with a potential $\tfrac{|F|^2}{4}+N-(\text{twist correction})$. When the potential is positive, $v$ is a subsolution of an operator with positive zeroth-order term, so it admits no interior local maximum. Consequently the local orbit-volume cannot have a uniform thin plateau: it must increase toward the exterior of each collapsed chart. On a closed manifold there is nowhere for $v$ to run off to infinity, so it must climb to regions where the orbits are no longer short — regions of definite fiber size, i.e. noncollapsed regions of definite 4-volume. This is exactly the object the chart-accessible exclusion removes. The chain "closed + $\lambda<0$ + positive orbit-volume potential $\Rightarrow$ noncollapsed region of definite measure $\Rightarrow$ excluded" would close the abelian and low-twist part of the argument without any classification.

What makes this decisive or not is the twist correction. For non-abelian $\mathrm{Nil}^3$ fibers, the note's interval computation gives $v''=(3-\mu)v$ with $\mu=a_3^2/(2a_1^2a_2^2)$. When the Heisenberg twist $\mu>3$ the potential turns to the wrong sign, $v$ becomes oscillatory, and the maximum principle no longer prevents a closed-base solution. So the **entire escape from Mechanism 1 lives in the strongly twisted nilpotent regime $\mu>3$**, and this is the single geometry to attack next.

Distinguishing computation: derive the exact local zeroth-order potential $P(x)=\tfrac{|F|^2}{4}+N-\Theta_{\text{twist}}(x)$ for a general fibered N-structure with $\operatorname{Ric}=-g$, and determine the sign of $\int_M P\,v\,d\mu_{\text{loc}}$ using the global topology. The topological input that could force $\int P>0$ even in the twisted case is the Pontryagin density of Mechanism 3, because strong Heisenberg twist feeds curvature that the self-dual amplitude constraint independently controls.

## Mechanism 2 — The simple eigenline is a global almost-complex structure; the near-symplectic Seiberg–Witten form makes it rigid

Because the calibrated spectrum has a *simple* lowest eigenvalue $-1/6$, over the calibrated region the operator $W^+\in\mathrm{Sym}_0(\Lambda^2_+)$ splits $\Lambda^2_+=L\oplus L^\perp$ into the eigenline $L$ and the double-eigenvalue plane $L^\perp$. A unit section $\omega$ of $L$ is a self-dual 2-form of length $\sqrt2$, hence an orthogonal almost-complex structure $J$ compatible with the orientation. So the calibrated germ *carries a canonical almost-complex structure*, defined wherever the spectrum is strictly of the calibrated shape.

The Seiberg–Witten near-saturation makes this $J$ concrete and near-integrable-tested. The monopole class $c=K_X$ (pulled to $M$) has a harmonic representative whose self-dual part $\omega_c$ near-saturates LeBrun's mixed estimate; saturation forces $\omega_c$ to be the extreme eigenform of $W^+$ (i.e. a section of $L$), of near-constant length, with $\int_M|\omega_c|^2\sim(c^+)^2\sim A$. A closed self-dual 2-form of constant length is symplectic, and $M$ is indeed symplectic with canonical symplectic form. So near-saturation says: the collapse must be a *near-almost-Kähler* degeneration whose fundamental form is the fixed canonical class, and whose $J$ coincides (to $o(1)$) with the eigenline $J$ of $W^+$.

The rigidity to exploit: the Weitzenböck computation gives $\int|\nabla\omega_c|^2=(1+o(1))\int|\omega_c|^2\sim A$, so $J$ is *uniformly far from parallel*, and the eigenline rotates at $O(1)$ rate localized in base directions. Now impose the collapse. In a rank-1 (circle-fiber) or nil-fiber collapse, the almost-complex $J$ must interact with the short fibers: either a fiber direction is $J$-invariant (the fiber pairs with a base direction under $J$) or it is not. If the collapsing circle pairs under $J$ with a horizontal direction, then $J$-rotation of $O(1)$ forces the paired horizontal direction to co-rotate, feeding curvature into the plane $L^\perp$ that the calibrated amplitude $|W^+|^2=\tfrac1{24}$ caps. This is a genuine tension between the $O(1)$ rotation demanded by Weitzenböck and the small self-dual amplitude demanded by calibration. The clean statement to prove or refute is:

> A near-almost-Kähler collapse with $\int|\nabla\omega_c|^2\sim\int|\omega_c|^2$ and $|\omega_c|$ near-constant cannot keep $|W^+|^2$ near $\tfrac1{24}$ (sub-Kähler amplitude) — because the almost-Kähler Weitzenböck identity ties $|\nabla\omega|^2$ to the self-dual Weyl amplitude and the intrinsic torsion of $J$.

Distinguishing computation: write the almost-Kähler Weitzenböck / the Apostolov–Draghici type identity relating $\int|\nabla\omega|^2$, $\int s\,|\omega|^2$, and $\int|W^+|^2$ for a self-dual $\omega$ of constant length, and check whether $\int|\nabla\omega|^2\sim\int|\omega|^2$ is compatible with $|W^+|^2\sim\tfrac1{24}$ and $s\sim-4$, or forces $|W^+|^2$ up toward the Kähler value $\tfrac23$. If it forces the amplitude up, the calibration is broken and no such sequence exists.

## Mechanism 3 — The Pontryagin density is pointwise definite and positive; test each surviving collapse against it

The Levi-Civita representative of $p_1(\Lambda^2_+)$ has pointwise density
$$
P_{\Lambda^2_+}=\frac{1}{4\pi^2}\Bigl(2|W^+|^2+\frac{s^2}{24}-\frac{|\mathring r|^2}{2}\Bigr)\;\xrightarrow[\text{calibrated}]{}\;\frac{1}{4\pi^2}\Bigl(\tfrac{2}{24}+\tfrac{16}{24}-0\Bigr)=\frac{3}{16\pi^2}>0 ,
$$
a strictly positive constant almost everywhere, integrating over $\tfrac{32}{9}\pi^2A$ to exactly $2\chi+3\tau=A-k\to\tfrac23A$. This is fully consistent globally, so there is no integrated contradiction — but it forces a *pointwise* statement: the self-dual bundle carries a definite $\operatorname{tr}(F_+\wedge F_+)$ density everywhere. Crucially, the $\Lambda^2_+$-bundle curvature $F_+$ is $W^++\tfrac{s}{12}$ plus the off-diagonal $\mathring r$, all pinned by calibration, so **$F_+$ is uniformly bounded on the whole sequence even where $W^-$ blows up.** The self-dual bundle is a bounded-curvature bundle over an everywhere-collapsing manifold, yet its Pontryagin density stays definite and positive.

The mechanism is to confront this with the collapse structure directly. A 4-form $\operatorname{tr}(F_+\wedge F_+)$ requires four genuinely curved directions. In a fibered collapse over a base of dimension $b$, split $F_+=F_+^{HH}+F_+^{HV}+F_+^{VV}$ by horizontal/vertical legs. The purely horizontal $F_+^{HH}\wedge F_+^{HH}$ vanishes when $b\le3$ (a 4-form pulled from $\le3$ dimensions is zero). So the *entire* positive density $\tfrac{3}{16\pi^2}$ must be carried by terms with at least one vertical (collapsing) leg — i.e. by the connection curvature of the N-structure and the second fundamental form of the short fibers. This makes precise the earlier "localization" intuition, but now as a pointwise identity with a fixed positive left side: **the short-fiber twist is forced, everywhere, to produce a definite amount of self-dual Pontryagin density.** In a rank-1 collapse this means the circle connection curvature $F^+$ (self-dual part) is pointwise bounded below in the right combination; the tension is that this same twist feeds the O'Neill positive contribution to vertical Ricci, which fights $\operatorname{Ric}=-g$ (Mechanism 1's potential). Quantifying "how much vertical twist is forced by $P_{\Lambda^2_+}=\tfrac{3}{16\pi^2}$" gives a lower bound on $|F|^2$ feeding the orbit-volume potential $\tfrac{|F|^2}{4}+N$, which pushes the twisted-nil case *back into* the positive-potential regime that Mechanism 1 excludes.

Distinguishing computation: for the $\mathrm{Nil}^3$-fiber and circle-fiber models, express $\operatorname{tr}(F_+\wedge F_+)/d\mu$ in terms of the twist $\mu$ and connection curvature, set it equal to $\tfrac{3}{16\pi^2}$, and read off the forced $|F|^2$; then substitute into the orbit-volume potential and test its sign. If the amount of twist needed to source the Pontryagin density always keeps $\tfrac{|F|^2}{4}+N-\Theta_{\text{twist}}>0$, Mechanisms 1 and 3 close jointly, including the $\mu>3$ escape.

## Mechanism 4 — The self-dual bundle as a bounded-curvature bundle over an everywhere-collapsing manifold

Independent of the pointwise picture, there is a global consequence of "$F_+$ bounded, manifold everywhere collapsed." For a bundle with uniformly bounded connection curvature over a manifold collapsing along an N-structure, Chern–Simons transgression expresses the Pontryagin form as $d(\text{a bounded transgression form})$ on each collapsed chart adapted to the local symmetry, and the local invariance of the connection under the N-structure suppresses the transgression contribution as the orbits shrink. The obstruction to running this globally is exactly the anti-self-dual bubbles ($\overline{\mathbb{CP}}^2$ necks) where $F_+$ stays bounded but the N-structure breaks. So the fixed integer $2\chi+3\tau=A-k$ should be recoverable as a sum of bubble contributions plus a collapse remainder that tends to zero. Each anti-self-dual $\overline{\mathbb{CP}}^2$ neck contributes a definite quantum to $p_1(\Lambda^2_+)$; matching the $A-k\sim\tfrac23A$ total against $k\sim\tfrac13A$ available necks and their per-neck self-dual Pontryagin content is a countable bookkeeping that either balances or does not.

Distinguishing computation: compute the self-dual Pontryagin contribution (the $\int\operatorname{tr}(F_+\wedge F_+)$ localized mass) of a single anti-self-dual ALE neck modeled on $\mathcal O(-1)\to\mathbb{CP}^1$ (the $\overline{\mathbb{CP}}^2$ bubble), and check whether $k$ such contributions can account for $A-k$ while leaving a collapse remainder consistent with the bounded-$F_+$ transgression estimate. A mismatch is a contradiction with the existence of the sequence; a match tells you exactly how the topological charge must distribute between necks and bulk.

## Mechanism 5 — $W^-$ reservoir and signature as an independent counting

The reservoir observation $\int|W^-|^2=\int|W^+|^2-12\pi^2\tau(M)\sim c\,A$ is not a passive bookkeeping remark: it says the anti-self-dual energy is topologically forced to be large and, by quantization, must sit in $O(A)$ ALE necks each carrying $\ge\varepsilon_0$ energy. This pins the *number* of bubbling points to be comparable to $k\sim A/3$, matching the blow-up count of $M$. The mechanism is to use this as a rigidity: the near-critical sequence must place one anti-self-dual neck at (essentially) each exceptional $\overline{\mathbb{CP}}^2$, and the bulk between necks must carry calibrated $W^+$ with $\int|W^+|^2\sim\tfrac{4}{27}\pi^2A$ spread over the collapsing region. Then the almost-complex structure of Mechanism 2 and the Pontryagin density of Mechanism 3 are constrained to coexist with $O(A)$ punctures. On a symplectic 4-manifold with an $\omega$-compatible near-almost-Kähler $J$, the exceptional spheres are $J$-holomorphic (Gromov–Taubes), and their normal bundles fix the local self-dual curvature near each neck; whether the calibrated bulk amplitude can be continued across $O(A)$ such $J$-holomorphic $-1$-spheres while maintaining $|W^+|^2\sim\tfrac1{24}$ is the coexistence question.

Distinguishing observation: the Taubes correspondence gives, from the nonzero SW invariant of $M$ (blow-up of general type), a $J$-holomorphic representative of $K_X$ and of each exceptional class; counting the self-dual curvature these curves inject near their neighborhoods and comparing to the calibrated bulk is a finite local computation per curve, aggregated over $O(A)$ curves.

## What to compute first, and what each outcome distinguishes

The mechanisms interlock around one small set of explicit calculations. (i) The exact local orbit-volume potential $\tfrac{|F|^2}{4}+N-\Theta_{\text{twist}}$ for circle- and $\mathrm{Nil}^3$-fibered $\operatorname{Ric}=-g$ collapse, to see whether the $\mu>3$ escape from Mechanism 1 is real once the twist is present. (ii) The self-dual Pontryagin density $\operatorname{tr}(F_+\wedge F_+)/d\mu$ for those same models as a function of twist, set equal to $\tfrac{3}{16\pi^2}$, giving the forced $|F|^2$ to feed back into (i). (iii) The almost-Kähler Weitzenböck identity relating $\int|\nabla\omega|^2$, $s$, and $|W^+|^2$ for a constant-length self-dual $\omega$, to test whether $\int|\nabla\omega|^2\sim\int|\omega|^2$ is compatible with the sub-Kähler amplitude $\tfrac1{24}$. (iv) The per-neck self-dual Pontryagin content of the $\overline{\mathbb{CP}}^2$ ALE model, to check the global counting of Mechanisms 4 and 5.

If (i)+(ii) show the twist forced by the Pontryagin density keeps the orbit-volume potential positive, the closed-base maximum principle excludes all fibered collapse and, with the chart-accessible exclusion, the sequence cannot exist. If (iii) shows the rotation energy forces $|W^+|^2$ toward the Kähler value, calibration breaks directly. If instead a specific strongly twisted nil model reproduces $(-1/6,1/12,1/12)$ at $\operatorname{Ric}=-g$ with a consistent potential sign, that model is the precise surviving geometry to build or refute a genuine collapsed near-critical example from — and it would be the first concrete structure showing whether the $\operatorname{Ric}\approx-g$ route to Yau 26 bends toward existence or nonexistence.

One caution on sources rather than invented facts: the Lott identity and its sign, the LeBrun mixed estimate and its saturation configuration, the Derdziński conformal-to-Kähler theorem, the almost-Kähler Weitzenböck (Apostolov–Draghici type) identity, and the Taubes SW$\Rightarrow$$J$-holomorphic correspondence are all in the standard literature and should be pulled and checked at the formula level before any of the four computations above is trusted; the constants (e.g. $8\sqrt6$ versus $\sqrt6$ in the calibrated defect) differ between the two session notes and must be reconciled against the primary LeBrun estimate.
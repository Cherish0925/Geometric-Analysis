# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step4_weyl_profile_and_bubble_restriction.tex",
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex"
  ]
}
```

## Task

For the non-collapsing problem under two-sided Ricci pinching on a fixed closed 4-manifold:

The key difficulty: we have |Ric_g| ≤ Λ and Vol(M,g) ≥ V₀ > 0 on a FIXED compact manifold M, but we need Vol(B(p,r)) ≥ v₀ r⁴ for ALL p and small r (non-collapsing). Without sectional curvature bounds, the standard Cheeger-Fukaya-Gromov collapse theory doesn't apply.

Propose mechanisms or arguments that could establish non-collapsing, or explain precisely why it might fail (with an explicit model). Consider:

1. Can the diameter grow without bound on a FIXED manifold M with |Ric| ≤ 2? If so, give an example. If not, explain why fixed topology constrains diameter growth under Ricci bounds.

2. Does the Seiberg-Witten data (uniform L^∞ bound on spinor, integral lower bound ∫|Φ|⁴ ≥ cA, first-order elliptic equation D_AΦ = 0) provide any additional compactness beyond what pure Riemannian geometry gives?

3. For the POSITIVE branch (Ric ≈ +g): is there a volume lower bound from Myers + topology?

4. Can the recent Cheeger-Colding-Naber theory (under only Ricci bounds) give non-collapsing in dimension 4, perhaps using the constrained topology of connected sums of algebraic surfaces?

5. Could the Weyl profile concentration ∫(|W+|-1/(2√6))² = O(Aδ²) combined with volume convergence provide additional geometric control?

Give specific mathematical arguments or counterexamples, not just references.

## Output

## Reframing the task: pure Riemannian data cannot deliver non-collapsing here

Before proposing mechanisms, it is worth fixing the decisive fact that reorganizes the whole question. A two-sided Ricci bound together with a global volume lower bound, even on fixed topology, does **not** force local non-collapsing. The cleanest witness is the flat 4-torus: on the fixed manifold $T^4$, take

$$
g_L = L^2\,d\theta_1^2 + L^{-2}\,d\theta_2^2 + d\theta_3^2 + d\theta_4^2 ,\qquad \operatorname{Ric}\equiv 0,\quad \operatorname{Vol}\equiv 1 .
$$

Here the two-sided Ricci pinch holds trivially (both sides zero), the total volume is pinned, and yet for $L^{-1}<r<1$ one has $\operatorname{Vol}(B(p,r))\sim L^{-1}r^3$, so $\operatorname{Vol}(B(p,r))/r^4\sim (Lr)^{-1}\to 0$. This is genuine local collapse on a **fixed** manifold with volume bounded above and below. So non-collapsing is a theorem that must consume the special structure of the Ishida–LeBrun manifolds — their nonzero Seiberg–Witten invariant, $\chi>0$, the sign of the Ricci pinch, and the calibrated Weyl density — and cannot come from Cheeger–Colding–Naber (CCN) generalities, which take non-collapsing as a *hypothesis* and never produce it.

The important point is that the torus does not carry the features your family has: $\operatorname{Ric}=0$ (not $\approx -g$), no Weyl energy, and no monopole class. Below I isolate exactly which of these break the collapse.

## The central new lever: the sign of the pinch forbids bounded-curvature collapse

This is the mechanism I would push hardest, because it is elementary, rigorous on the model, and directly exploits that your pinch is $\operatorname{Ric}\le(-1+\delta)g<0$, i.e. Ricci is **negative-definite with a uniform upper bound below zero**.

Bounded-curvature collapse is governed by Cheeger–Fukaya–Gromov: on a region where $|\mathrm{Rm}|\le K$ and the volume ratio is small, the geometry is an almost-submersion with infranilmanifold orbits shrinking. Model it as a Riemannian submersion $\pi:(M^4,g)\to (B,\check g)$ with totally geodesic fibers and integrability (O'Neill) tensor $A$. For a **unit vertical (collapsing) vector** $U$, O'Neill's formula gives

$$
\operatorname{Ric}_M(U,U)=\operatorname{Ric}_{\mathrm{fiber}}(U,U)+\sum_i |A_{X_i}U|^2 .
$$

For a flat torus fiber, $\operatorname{Ric}_{\mathrm{fiber}}=0$, hence $\operatorname{Ric}_M(U,U)=\sum_i|A_{X_i}U|^2\ge 0$. For a nilpotent (Heisenberg) fiber the intrinsic Ricci is sign-indefinite but the **center direction has positive Ricci** (for $[X,Y]=Z$ orthonormal, $\operatorname{Ric}(Z,Z)=+\tfrac12$ up to scale), and this sign persists under any rescaling of the fiber. In every infranil collapse, therefore, at least one collapsing direction $U$ satisfies

$$
\operatorname{Ric}_M(U,U)\ \ge\ 0 .
$$

But the pinch demands $\operatorname{Ric}_M(U,U)\le(-1+\delta)|U|^2<0$. Contradiction. Concretely, a shrinking round $S^3$ neck already shows the flavor: $S^3(\rho)\times\mathbb R$ has fiber-block Ricci $2/\rho^2$ and flat line direction Ricci $0$, so $|\operatorname{Ric}+g|\ge 1$ in the line direction — $\delta\ge1$, exactly the earlier scalar-flat-connector exclusion in disguise. So:

**A uniform pinch $\operatorname{Ric}\le(-1+\delta)g$ with $\delta<1$ is incompatible with bounded-curvature collapse: the collapsing directions carry Ricci $\ge 0$, contradicting the strict negativity of the upper bound.**

This is the structural reason hyperbolic and other Einstein metrics of sign $-1$ are non-collapsed, promoted to the pinched setting. It is the analog, in the *volume/injectivity-radius* channel, of your earlier observation that scalar-flat necks force $\delta\ge1$.

## Why this does not instantly finish: curvature is only bounded through $\operatorname{Ric}$

The one thing we do **not** have a priori is a pointwise $|\mathrm{Rm}|$ bound — only $|\operatorname{Ric}|\le C$. So the fiber-Ricci obstruction applies only where curvature is bounded. The needed input is $L^2$-curvature $\varepsilon$-regularity **without** assuming non-collapsing:

- On the fixed manifold, Chern–Gauss–Bonnet and signature make $\int|\mathrm{Rm}|^2$ a topological quantity, and with $\int|\operatorname{Ric}^\circ|^2\to0$ and $s\to-4$ it is bounded by $\sim A$. So total curvature energy is finite and topologically fixed.
- Cheeger–Tian's $\varepsilon$-regularity for Einstein (and almost-Einstein) 4-manifolds is precisely designed to bound $|\mathrm{Rm}|$ on a ball when the energy on a slightly larger ball is $<\varepsilon_0$, *not* requiring a volume lower bound. This is the crucial point that breaks the circularity CCN cannot break. It needs an elliptic identity for curvature; Einstein gives $\Delta \mathrm{Rm}=\mathrm{Rm}\ast\mathrm{Rm}$, and the pinched case gives this modulo a $\nabla\operatorname{Ric}$ error controlled by the second Bianchi identity $\operatorname{div}\mathrm{Rm}=d^{\nabla}\operatorname{Ric}$, whose size is governed by $\delta$ and its derivatives. Making this error harmless is the honest technical task; it is the analytic heart of the argument, and it is where I would invest.

Granting the $\varepsilon$-regularity, the logical chain closes as follows.

1. Curvature is bounded except on $\le N=\int|\mathrm{Rm}|^2/\varepsilon_0$ energy-concentration points.
2. On the complement (bounded curvature, $\operatorname{Ric}\approx -g$), the fiber-Ricci obstruction forbids collapse: **uniform local non-collapsing holds on the bulk.**
3. Near a concentration point, rescale by the curvature scale $\ell_i\to0$. Since $|\operatorname{Ric}|\le C$ is scale-covariant, the rescaled limit is Ricci-flat. The finite-energy Ricci-flat ALE/ALF/ALG bubble carries the concentrated curvature. That curvature is **Weyl only** (Ricci is bounded, so it does not concentrate), and by the profile below it is $W_-$, not $W_+$.

## The Weyl profile makes the concentration analysis rigid

Your profile concentration $\int(|W_+|-\tfrac1{2\sqrt6})^2=O(A\delta^2)$ says $|W_+|$ is $L^2$-close to a **constant** $1/(2\sqrt6)$, so the self-dual Weyl energy has **nearly uniform density** $|W_+|^2\approx 1/24$, not concentrated. Two consequences that sharpen the collapse picture:

- **$W_+$ energy cannot sit at concentration points.** On any region $U$ of small volume, $\int_U|W_+|^2\le 2Y+\tfrac1{12}\operatorname{Vol}(U)\to0$. So a curvature bubble carries zero $W_+$ energy in the limit: bubbles are Ricci-flat and self-dually flat, i.e. hyperkähler ALE (Eguchi–Hanson / Kronheimer ADE). The concentrating Weyl is entirely $W_-$.
- **$W_+$ energy cannot be carried by a collapsing bulk region.** Where curvature is bounded, $|W_+|^2$ is bounded, so $\int_{\text{collapsing}}|W_+|^2\le C\cdot\operatorname{Vol}\to0$. But the total $\int|W_+|^2\to\tfrac{4}{27}\pi^2 A>0$. Hence a definite fraction of volume must remain non-collapsed carrying density $1/24$. Combined with (2), this is consistent and reinforcing.

The instructive contrast is the **Gross–Wilson collapse of K3**: hyperkähler (so $\operatorname{Ric}=0$ and $W_+=0$) Ricci-flat metrics collapse along an elliptic $T^2$-fibration to $\mathbb P^1$, with $\int|\mathrm{Rm}|^2=8\pi^2\chi(K3)=192\pi^2$ concentrating at $24$ singular fibers. This is a genuine bounded-Ricci, $\chi\ne0$, volume-bounded-below **collapse**. It proves that neither fixed topology nor $\chi\ne0$ obstructs collapse under Ricci bounds — the obstruction CCN/topology alone cannot supply. The two features that make K3 collapsible are exactly the two your family lacks: $\operatorname{Ric}=0$ (compatible with fiber-Ricci $\to0$) and $W_+\equiv0$ (nothing forcing non-collapsed density). Your family has $\operatorname{Ric}\approx -g$ (killed by the fiber-Ricci obstruction) and $\int|W_+|^2\sim A>0$ (killed by the density argument). This comparison is the sharpest way to see that the two levers are genuinely doing the work.

## Point 1: diameter

On your critical family the volume is pinned, $\operatorname{Vol}(M,g_i)\to 32\pi^2A/9$. With volume bounded **above**, a packing argument along a minimizing geodesic of length $D$ (disjoint $r$-balls at $r$-separated points) gives, under a uniform non-collapse constant $v_0$, $\operatorname{Vol}\ge \tfrac{D}{2r}\,v_0 r^4$, i.e. $D\le 2\operatorname{Vol}/(v_0 r^3)$. So on this family, **unbounded diameter is equivalent to local collapse** (loss of a uniform $v_0$). Diameter is therefore not an independent difficulty: control it exactly by controlling collapse. Absent the pinch, diameter can indeed run to infinity with bounded Ricci and bounded volume — but only through fiber collapse (a straight $S^3$ neck stays fat, cross-section radius $\ge1$ under $|\operatorname{Ric}|\le2$; thinning it is a Berger/nil collapse), and that collapse route is precisely what the sign-$(-1)$ pinch forbids.

## Point 2: does Seiberg–Witten add compactness beyond Riemannian geometry?

The SW data give global, not directly local, control, but they are what certifies the profile that then drives everything:

- The Weitzenböck/maximum principle bound $|\Phi|^2\le -s\le 4(1+\delta)$ and $|F_A^+|=|\Phi|^4/8$ are uniform from the pinch alone — no injectivity radius needed. The lower bound $\int|\Phi|^4\ge cA$ (nonvanishing monopole in a nonzero SW class) forces $\int s^2\ge 32\pi^2(a^+)^2$, which with $|s|$ bounded yields the global volume lower bound, and — through the scalar–Weyl estimate — the definite $\int|W_+|^2\sim A$ that the density argument then localizes. In this sense SW is the *source* of the non-collapsing lever, even though it does not itself bound $\operatorname{Vol}(B(p,r))/r^4$.
- A distinct, potentially decisive route is the almost-Kähler form. Where $\Phi\ne0$, $\omega=\sigma(\Phi)/|\Phi|^2$ is a self-dual 2-form of norm $\sqrt2$ sitting in the lowest $W_+$-eigenline. A **near-parallel** symplectic form obstructs fiber collapse independently of curvature bounds: nondegeneracy means $\omega(U,\cdot)\ne0$ on the collapsing direction $U$, and a bounded, nearly closed $\omega$ with $|\omega|^2=2$ cannot survive an $S^1$/$T^2$-collapse to a lower-dimensional base (where a self-dual 2-form must degenerate along the vanishing fiber). Taubes' identification $SW=Gr$ turns the nonzero monopole class into pseudoholomorphic curves with $\int_C\omega\ge$ a fixed positive area, another quantitative non-degeneration. The honest missing step, already flagged in your Step 4, is upgrading the $L^6$ near-constancy of $|\Phi|^2$ to a pointwise nonzero lower bound so that $\omega$ is globally nondegenerate; that upgrade would both give the forbidden symplectic structure (Armstrong contradiction) and independently exclude collapse.

## Point 3: the positive branch

Two things combine, and one of them is decisive for your family.

- Myers gives bounded diameter: $\operatorname{Ric}\ge(1-\delta)g$ implies $\operatorname{diam}\le \pi\sqrt{3}$ in dimension $4$, plus finite fundamental group. But bounded diameter with a lower Ricci bound does **not** give a volume lower bound — Berger spheres ($\operatorname{Ric}>0$ bounded, $\operatorname{Vol}\to0$, collapse $S^3\to S^2$) show Myers alone cannot prevent collapse.
- The decisive observation: $\operatorname{Ric}\ge(1-\delta)g>0$ forces $s>0$, i.e. positive scalar curvature, which **forbids a nonzero Seiberg–Witten invariant**. Every Ishida–LeBrun obstructed manifold has $SW\ne0$, hence admits no PSC metric. Therefore the positive-Ricci pinch is **vacuous on exactly the manifolds where the sign-$(-1)$ obstruction lives**. The positive branch has to be settled on a completely different topological class (the PSC 4-manifolds: connected sums of $S^4$, $\mathbb{CP}^2$, $\overline{\mathbb{CP}^2}$, $S^2\times S^2$ and quotients, by Gromov–Lawson/SW). On that class the Einstein-existence question is its own problem — many-fold connected sums can again be obstructed by LeBrun — but it is disjoint from the analysis here, and this cleanly splits the two branches.

## Point 4: what CCN and its refinements can and cannot give

CCN structure theory (codimension-4 singular set, tangent-cone analysis) is conditional on non-collapsing and cannot manufacture it. The correct heavy tool is the **Cheeger–Tian / Naber–Tian collapse theory for (almost-)Einstein 4-manifolds**, which provides $L^2$-curvature $\varepsilon$-regularity and the decomposition into bounded-curvature regions plus finitely many concentration points, *without* a volume lower bound as hypothesis. This is exactly the input needed to reduce your problem to the bounded-curvature fiber-Ricci obstruction. The constrained topology enters not through a "$\chi\ne0\Rightarrow$ non-collapse" statement (false, by K3), but through bounding the number of hyperkähler bubbles by $\int|\mathrm{Rm}|^2/\varepsilon_0$ and forcing all of them to be $W_+$-flat, so they cannot host the $\sim A$ units of $W_+$ energy. The topology and the profile act jointly: topology bounds the concentration; the profile forbids $W_+$ from concentrating; the sign of the pinch forbids the bulk from collapsing.

## Point 5: the Weyl profile plus volume convergence, made into control

Beyond what is above, the profile gives one more quantitative filter worth exploiting directly. Because $|W_+|^2\approx 1/24$ with $L^2$-error $O(A\delta^2)$ and $\operatorname{Vol}\to 32\pi^2A/9$, the *fraction* of volume in any bounded-curvature collapsing region is bounded by that region's contribution to $\int|W_+|^2$, which vanishes. So define $\mathcal N_i=\{p:\operatorname{Vol}(B(p,r))\ge v_0 r^4\ \forall r\le1\}$. The density identity forces $\operatorname{Vol}(\mathcal N_i)\ge \tfrac{9}{24}\cdot\tfrac{1}{ \sup|W_+|^2}\cdot\int|W_+|^2 - o(1)$, a definite fraction of the total. On $\mathcal N_i$ CCN applies and extracts an $\operatorname{Ric}=-g$ Einstein limit of dimension 4 carrying the calibrated profile $|W_+|=1/(2\sqrt6)$ with eigenvalues $(1/12,1/12,-1/6)$ — a *strictly* almost-Kähler saturating geometry ($s^*=-2\ne-4=s$). That is exactly the configuration your Armstrong tension excludes for a compact smooth limit; the remaining subtlety is whether the local (possibly complete non-compact) Einstein almost-Kähler limit still obeys Armstrong-type rigidity. Determining the correct non-compact almost-Kähler-Einstein rigidity statement (does a complete strictly almost-Kähler $\operatorname{Ric}=-g$ 4-manifold with $|W_+|^2\equiv1/24$ exist?) is the sharp decisive question this route reduces to.

## The one decisive computation I would run

Test the only escape left after the fiber-Ricci obstruction and the profile: an $S^1$- (or $T^2$-) collapse in which curvature is **not** bounded, but stays compatible with $\operatorname{Ric}\approx -g$ and $|W_+|\approx 1/(2\sqrt6)$. Set the adiabatic model $g_t=\pi^*\check g + t^2\theta\otimes\theta$ on an $S^1$-bundle over $B^3$ with connection curvature $F=d\theta$, and compute, to leading order in $t$, the four Ricci eigenvalues and the three $W_+$-eigenvalues in terms of $(\operatorname{Ric}_{\check g}, |F|^2, \nabla F)$. Two outcomes are decisive:

- If the vertical Ricci $\operatorname{Ric}(U,U)\to \tfrac{t^2}{4}|F|^2\to 0$ (bounded-curvature regime), the pinch is violated — recovering the obstruction analytically and quantifying the minimal $\delta$ as a function of $t$ and $|F|$.
- To keep $\operatorname{Ric}(U,U)\approx -1$ one must send $|F|^2\sim t^{-2}$, i.e. **unbounded** curvature; then compute whether $W_+$ can simultaneously equal the constant $1/(2\sqrt6)$ with the split $(1/12,1/12,-1/6)$. Since $B^3$ is conformally flat (3D Weyl vanishes), the entire $W_+$ of $g_t$ is generated by $F$ and its derivatives; the eigenvalue equations will either fix $F$ rigidly (a concrete over-determined system) or show no solution matches the calibrated profile. Either result is a clean, self-contained obstruction to the last collapse channel.

This computation is inexpensive (explicit tensor algebra, verifiable symbolically) and directly distinguishes "collapse is impossible" from "a specific twisted degeneration must be analyzed further." It is the highest-value next calculation because it turns the qualitative fiber-Ricci obstruction into a quantitative exclusion covering the unbounded-curvature case that $\varepsilon$-regularity leaves open.

## What remains genuinely unresolved, stated precisely

The non-collapsing argument is complete *modulo* one analytic input and one rigidity input: (i) $L^2$-curvature $\varepsilon$-regularity for the pinched (not exactly Einstein) equation, with the $\nabla\operatorname{Ric}$ error controlled by $\delta$ through the second Bianchi identity — this is what removes the a priori $|\mathrm{Rm}|$ bound and reduces everything to bounded-curvature regions where the fiber-Ricci obstruction bites; and (ii) the correct rigidity for possibly-complete-non-compact almost-Kähler Einstein limits carrying $|W_+|^2\equiv 1/24$, which is what upgrades the local Einstein limit on $\mathcal N_i$ into a contradiction. The adiabatic computation above closes the unbounded-curvature $S^1$-collapse channel independently of (i). Together these convert "non-collapsing under two-sided Ricci pinch" from an appeal to unavailable sectional-curvature theory into a statement resting on the *sign* of the pinch, the *topologically fixed and profile-uniform* Weyl energy, and Cheeger–Tian $\varepsilon$-regularity — the three ingredients the flat torus and the collapsing K3 precisely lack.
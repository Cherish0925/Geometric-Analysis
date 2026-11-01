# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step10_multiscale_cover_and_diffuse_pontryagin.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex"
  ]
}
```

## Task

Consider a closed oriented Einstein 4-manifold (M, g) with Ric = -g that is collapsing with circle fibers of length function ℓ. The self-dual Weyl operator in the static circle reduction is W+ = 2J(h - I/3) where h = Hess(ℓ)/ℓ, plus twist corrections that are O(ℓ²|F|²) where F = dA is the connection curvature. The calibrated spectrum (-1/6, 1/12, 1/12) requires h eigenvalues (3/8, 3/8, 1/4) in the static case, but the ONLY constant-eigenvalue static Einstein circle metric has h = I/3 (i.e., W+ = 0). This is the static incompatibility.

Near a smooth NUT (ℓ → 0), twist corrections vanish as O(ℓ²), so the static formula dominates: W+ → 2J(h - I/3) with h constrained to the isotropic value by Einstein. This means the calibrated anisotropy cannot persist into the NUT core.

Develop a rigorous argument connecting this anisotropy constraint to fiber survival at a fixed buffer scale on the calibrated good set. Specifically:

1. For a good point p (bounded curvature mean at all scales ≤ 1, small calibrated deficit), can the fiber length ℓ(p) be arbitrarily small? The Riemann tensor in the e_a ∧ e_4 directions contains h_{ab} = Hess(ℓ)_{ab}/ℓ, which diverges if ℓ → 0 with |∇ℓ| bounded. Use the curvature mean bound to derive a lower bound on ℓ(p) at good points.

2. If ℓ(p) ≥ ℓ₀ > 0, then the fiber survives in a ball B_R(p) of fixed radius (from the slow variation of ℓ implied by the curvature bound). This gives a buffer-scale covering chart, which transports the calibrated deficit and produces the forbidden Einstein germ.

3. Alternatively, if ℓ(p) can be small at a good point, show that the static incompatibility forces a positive calibrated deficit or excessive curvature on B_R(p), using the fact that calibrated W+ requires substantial twist energy (O(ℓ²|F|²) ≥ c), while the total twist energy is controlled by the topology.

The scientific product should be a clear mechanism connecting the W+ anisotropy, the circle-reduction Hessian, and fiber survival, leading to a conditional or unconditional exclusion of circle-collapse on the calibrated good set.

## Output

# Generator memo — circle reduction, fiber-length Hessian, and exclusion of circle-collapse on the calibrated good set

This addresses the negative-scale (Ric = −g) circle-collapse question. I first pin the reduction dictionary with verified arithmetic, then show the static incompatibility is a base-level version of the Step‑6 projector obstruction, then sharpen the three requested parts. The main working mechanism turns out to be cleaner and more decisive than "curvature mean ⟹ ℓ bounded below": the true content is **fixed-point (NUT) avoidance by two complementary energy estimates**, after which the fiber survives, unwraps, and the four-dimensional obstruction fires. I also isolate the one genuinely open residue (twist-supported small ℓ) and show it cannot rescue a fixed point.

## 1. Circle-reduction dictionary (arithmetic checked)

Write the collapsing metric on a rank‑one region as a variable-length circle bundle
$$
g = g_B + \ell^2\,\eta^2,\qquad \eta = d\theta + A,\quad F=dA,\quad \phi=\ln\ell,
$$
with $g_B$ a metric on a 3‑manifold base $B$, $\ell>0$ the fiber-length function, $A$ a connection with base curvature $F$. Using the O'Neill/warped-submersion formulas (Besse, *Einstein Manifolds*, Ch. 9; the $A$- and $T$-tensors have magnitudes $|A|\sim \tfrac{\ell}{2}|F|$, $|T|\sim|\nabla\phi|$), the orthonormal-frame Riemann components are, with $e^4=\ell\eta$ and $U=\ell^{-1}\partial_\theta$,
$$
R_{a4b4} = -\frac{(\operatorname{Hess}\ell)_{ab}}{\ell} + \frac{\ell^2}{4}(FF)_{ab},\qquad
R_{abc4} = \frac{\ell}{2}\big(D_cF_{ab}\big)+\tfrac{\ell}{2}(\phi\!\cdot\!F\text{-terms}),
$$
$$
R_{abcd}= R^B_{abcd} - \tfrac34\,\ell^2(\text{$F$-quadratic}) .
$$
Set $h=\operatorname{Hess}(\ell)/\ell$ (a symmetric base 2‑tensor). The **static reduction** ($A=0$) of Ric $=-g$ gives cleanly
$$
\text{base:}\quad \operatorname{Ric}^B = h - g_B,\qquad
\text{fiber:}\quad \Delta_B\ell = \ell,\qquad \operatorname{tr} h = 1 .
$$
On the self-dual bundle spanned by $\omega_a = e^a\wedge e^4 + \tfrac12\varepsilon_{abc}e^b\wedge e^c$, the mixed block $R_{a4b4}=-h_{ab}$ feeds $W^+$ as
$$
\boxed{\;W^+ = 2\big(h - \tfrac13 I\big) + (\text{twist, }O(\ell^2|F|^2))\;}
$$
Arithmetic check of the calibrated germ: $h=\operatorname{diag}(\tfrac14,\tfrac38,\tfrac38)$ (trace 1) gives $h-\tfrac13 I=(\tfrac1{24},\tfrac1{24},-\tfrac1{12})$, so $W^+ = (\tfrac1{12},\tfrac1{12},-\tfrac16)$ — exactly the calibrated spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$, and $|W^+|^2=\tfrac1{24}$. Isotropy $h=\tfrac13 I$ gives $W^+=0$. This confirms the task's $J$ acts as (a reordering of) the identity here; no free normalization remains.

Static base data for the calibrated germ: $\operatorname{Ric}^B = h-g_B=\operatorname{diag}(-\tfrac34,-\tfrac58,-\tfrac58)$, scalar $s_B=-2$. Note $\Delta_B\ell=\ell>0$: **$\ell$ is subharmonic on the base**, so it has no interior maximum; it can only dip toward zero at interior minima — the fixed points of the circle action.

## 2. The static incompatibility is the Step‑6 projector obstruction, read on the base

The static system forces the overdetermined Obata-type equation
$$
\operatorname{Hess}(\ell) = \ell\,h,\qquad h=\operatorname{Ric}^B+g_B .
$$
Requiring the calibrated **constant** $W^+$ spectrum means $h$ has constant eigenvalues. Differentiating the Obata equation and commuting derivatives,
$$
R^B_{abcd}\,\nabla^d\ell = \nabla_a(\ell h_{bc}) - \nabla_b(\ell h_{ac})
= \ell_a h_{bc}-\ell_b h_{ac} + \ell(\nabla_a h_{bc}-\nabla_b h_{ac}),
$$
and contracting/tracing with the constant-eigenvalue projectors reproduces, one dimension down, the same rigidity that Step 6 obtained upstairs: the simple eigenline of $h$ (the $W^+$ eigenvalue $-\tfrac16$, i.e. the $h$-eigenvalue $\tfrac14$) must be parallel, which forces $\nabla h=0$; a parallel anisotropic $h$ with $\operatorname{Hess}\ell=\ell h$ then forces $R^B\nabla\ell=0$ and, via de Rham/Obata splitting, either $\nabla\ell\equiv$ eigen-aligned with $h$ isotropic, i.e. $h=\tfrac13 I$ and $W^+=0$. This is the **exact mirror** of Step 6: constant two-eigenvalue $W^+$ with $\delta W^+=0$ $\Rightarrow\nabla W^+=0\Rightarrow$ Kähler $\Rightarrow$ spectrum $(-\tfrac23,\tfrac13,\tfrac13)\cdot(s/12)$, never $(-\tfrac16,\tfrac1{12},\tfrac1{12})$; and the Einstein–Weyl identity demands $|\nabla W^+|^2=\tfrac1{16}\neq0$.

Two structural payoffs. First, this gives a version of the projector obstruction that survives *without noncollapse* — it lives on the 3‑manifold $B$, precisely the object Step 9/10 could not previously reach. Second, it identifies the extremal static solution concretely: the only static circle-Einstein limits are the isotropic ones with $W^+=0$, matching Step 10's computation that the unwrapped Taub–NUT–AdS limit is real-hyperbolic $H^4$ with $W^+=0$ (Step 10 eqs. (7)–(8)). Taub–NUT–AdS is thus the extremal case of the static incompatibility, not a counterexample.

**Near-static upgrade (needed for the small-ℓ analysis).** For $\ell\to0$ the twist enters only at $O(\ell^2|F|^2)$. If in addition $\ell^2|F|^2\to0$ (near-static), the perturbed Obata system gives a lower bound on the calibrated deficit: any Einstein metric with $W^+$ inside a fixed neighborhood of the calibrated spectrum and $\ell^2|F|^2\le\epsilon$ carries deficit $F_{\mathrm{def}}\ge c_0(1-C\epsilon)>0$. In words: **near-static + calibrated ⟹ positive deficit.** This is the quantitative form of "the calibrated anisotropy cannot persist where twist is negligible."

## 3. Sharpening Part 1 — what the curvature mean actually delivers

The literal target "good point ⟹ $\ell(p)\ge\ell_0$" is not correct as stated, and it is worth saying why, because the reason points to the real mechanism.

- **Scale invariance of the anisotropy.** Under $\ell\mapsto\varepsilon\ell$ with fixed base and profile, $h=\operatorname{Hess}\ell/\ell$ is unchanged, so both $W^+=2(h-\tfrac13 I)$ and $|Rm|$ (through $R_{a4b4}=-h$) are unchanged. Uniform circle collapse therefore produces good points with $\ell\to0$ and bounded curvature mean. A bare lower bound on $\ell$ from the curvature mean alone cannot hold.
- **What does hold.** $R_{a4b4}=-h+O(\ell^2|F|^2)$ gives the integral control
$$
\int_{B_r}\frac{|\operatorname{Hess}\ell|^2}{\ell^2}\;\lesssim\;\int_{B_r}\!\big(|Rm|^2+\ell^4|F|^4\big)\ \le\ (K+\text{twist})\,\mathrm{Vol}(B_r),
$$
so $\ln\ell\in W^{2,2}$ with norm bounded by $K$ on good balls. In dimension four $W^{2,2}$ is the borderline case: it embeds in BMO/VMO but not $C^0$. A genuine fixed point makes $\ln\ell\to-\infty$ with $\operatorname{Hess}\ln\ell\sim1/\mathrm{dist}^2$, whose square integrates logarithmically — exactly at the edge of $W^{2,2}$. The finite, $K$-controlled $W^{2,2}$ norm therefore controls the *oscillation* of $\ell$ on good balls (Morrey–Campanato), giving $\ell(x)/\ell(p)\in[e^{-C},e^{C}]$ on a definite-measure subset, but it does not by itself forbid a fixed point inside the buffer.

The decisive lower bound is not on $\ell(p)$ but on the **distance from a calibrated-good point to any fixed point of the circle action** (any NUT). This is where the anisotropy mechanism becomes essential, through two complementary energy estimates.

**(a) Singular/shrinking fixed point — curvature-good excludes it.** A fixed point where the fiber closes non-smoothly, or a family of shrinking NUTs (Taub–NUT $\nu\to0$), carries a definite curvature energy: Step 10 eq. (6) gives Weyl energy $\to32\pi^2$ per NUT, and Anderson $\varepsilon$-regularity guarantees $\int_{B_r(q)}|Rm|^2\ge\varepsilon_0$ whenever the fixed point sits in a nonflat region at scale $r$. If $q$ is such a point at distance $d=\mathrm{dist}(p,q)\le\tfrac12$, then with the Bishop upper bound $\mathrm{Vol}(B_{2d}(p))\le C d^4$ (from $\operatorname{Ric}\ge-3g$),
$$
\fint_{B_{2d}(p)}|Rm|^2 \ \ge\ \frac{\int_{B_d(q)}|Rm|^2}{\mathrm{Vol}(B_{2d}(p))}\ \ge\ \frac{\varepsilon_0}{C d^4}.
$$
The good-point bound $\le K$ forces $d\ge d_*(K)=(\varepsilon_0/CK)^{1/4}>0$.

**(b) Smooth bounded-curvature fixed point — deficit-good/anisotropy-death excludes it.** A smooth fixed point of a circle action on a smooth 4‑manifold is locally linear, hence the metric is asymptotically flat there and $W^+\to0$ (twist included; a smooth fixed point cannot carry $O(1)$ self-dual Weyl). Since the calibrated germ needs $|W^+|^2=\tfrac1{24}$, on the zone $B_{r_0}(q)$ where $|W^+|^2\le\tfrac1{48}$ the calibrated deficit obeys $F_{\mathrm{def}}\ge c_0>0$. Then
$$
\fint_{B_{2d}(p)}F_{\mathrm{def}} \ \ge\ \frac{c_0\,\mathrm{Vol}(B_{r_0}(q))}{\mathrm{Vol}(B_{2d}(p))}\ \gtrsim\ c_0\Big(\tfrac{r_0}{d}\Big)^{4},
$$
which contradicts the deficit-good bound $\fint F_{\mathrm{def}}\le\varepsilon_i\to0$ once $d\lesssim r_0\,\varepsilon_i^{-1/4}$. So calibrated-good points also keep a definite distance from smooth fixed points.

Estimates (a) and (b) are complementary and jointly cover every fixed point: the anisotropy-death argument (b) is precisely what handles the smooth-NUT case that the pure curvature bound (a) misses. Together: **every calibrated-good point has a fixed-point-free buffer $B_{\rho_*}(p)$ with $\rho_*=\rho_*(K,\varepsilon_i)>0$.** This is the correct replacement for the requested Part‑1 statement.

## 4. Part 2 — fixed-point-free buffer ⟹ fiber survival ⟹ noncollapsed cover ⟹ forbidden germ

Inside $B_{\rho_*}(p)$ the Killing field has no zero, so $\ell\ge\ell_{\min}>0$ there (continuity + oscillation control of §3). Hence the circle fiber is a nontrivial loop in $\pi_1(B_{\rho_*}(p))$: it can only die by contracting through a fixed point, which the buffer excludes. This is exactly the maximal-rank condition on the buffered image $\Gamma(p;\rho,A,\eta)$ of Step 10 eq. (12), now established rather than assumed for the rank‑one stratum.

Pass to the local universal cover $\widetilde{B_{\rho_*}(p)}$. For pure circle collapse $\pi_1$ is cyclic (generated by the fiber), so the cover unrolls the fiber to $\mathbb R$ and is **noncollapsed**, with the deck degree cancelling as in Step 9 eq. (8): the number of sheets in a unit cover-ball is $\sim1/\ell$, the sheet volume is $\sim\ell\cdot(\text{base}^3)$, so $\mathrm{Vol}\,B_1(\tilde p)\sim(\text{base}^3)=O(1)$ and the injectivity radius is bounded below by $\min(\text{base-inj},\rho_*)$. (Even for a nilpotent rank-one substructure the universal cover unrolls everything to a contractible group, hence is noncollapsed; only genuinely higher-rank abelian/torus collapse can leave the cover collapsed.) The mean-transport lemma (Step 9 eqs. (8)) carries both $|Rm|^2\le C_TK$ and $F_{\mathrm{def}}\le C_T\varepsilon_i$ to the cover. Noncollapse + bounded curvature mean + $\operatorname{Ric}=-g$ then gives a harmonic radius bounded below (Anderson), $C^{1,\beta}$/$W^{2,p}$ convergence to a smooth Einstein limit with the calibrated germ $s=-4$, $\operatorname{Spec}W^+=(-\tfrac16,\tfrac1{12},\tfrac1{12})$ — which the Step‑6 projector obstruction forbids. Contradiction.

This closes the rank‑one (circle) collapse stratum on a fixed critical Ishida–LeBrun manifold, conditional only on (i) the region collapsing by circles and (ii) the two energy inputs of §3, both of which are standard-strength.

## 5. Part 3 — the twist-supported residue does not rescue a fixed point

The only way to keep calibrated $|W^+|^2=\tfrac1{24}$ while $\ell\to0$ is the twist-supported regime $\ell^2|F|^2\gtrsim1$, i.e. $|F|\gtrsim\ell^{-1}$ (otherwise §2's near-static upgrade forces positive deficit). Three facts constrain it.

- **It cannot reach a fixed point.** A smooth fixed point is locally linear ⟹ $W^+\to0$ regardless of $|F|$; a non-smooth fixed point is curvature concentration excluded by §3(a). So twist-support can only sustain calibrated $W^+$ in regions of small-but-nonvanishing $\ell$ (uniform-type collapse), where §4 already applies (no fiber death). Twist does not open a new route to fiber contraction.
- **Reduced electric–magnetic calibrated system.** Decompose the self-dual curvature into an "electric" part from $\operatorname{Hess}\ell/\ell$ (the $e^a\wedge e^4$ block) and a "magnetic" part from $*_3F$ (the horizontal block); $W^+=0$ is the Gibbons–Hawking monopole balance $\nabla(\ell^{-2})=\pm *_3F$. Calibrated $W^+$ is a *specific imbalance* of these, giving a closed PDE system for $(g_B,\ell,A)$ on $B^3$:
$$
\operatorname{Ric}^B = h - g_B - (\text{$F$-quadratic}),\qquad \Delta_B\ell=\ell+\tfrac14\ell^3|F|^2,\qquad
2(h-\tfrac13 I)+\mathcal T(F,\ell)=W^+_{\text{cal}} .
$$
A genuine twist-supported countermodel must solve *this reduced system* with constant $W^+$ spectrum on an open 3‑set — the base analogue of "solving a reduced mixed-curvature equation with diffuse Chern–Simons flux" (Step 10 eqs. (24)). It is the sharp object to attack or to search for numerically, not a finite NUT-cap construction.
- **Diffuse Pontryagin consistency.** With $|F|\sim\ell^{-1}$ the O'Neill $A$-tensor energy $|A|^2\sim\ell^2|F|^2\sim1$ is exactly the order-one mixed curvature $\fint_U|\Xi|^2\ge c(K)$ of Step 10 eq. (22), and its self-dual content matches the diffuse density $\rho_+\to\tfrac{3}{16\pi^2}$ (Step 10 eqs. (14)–(15)). The derivative term $R_{abc4}\sim\tfrac{\ell}{2}DF$ stays $O(1)$ only if $F$ varies on an $O(1)$ base scale; if the calibrated imbalance forces $F$ to vary faster than the fiber-collapse scale, $R_{abc4}$ inflates and re-enters the curvature-good exclusion. The reduced system above is where this is decided.

## 6. Distinguishing computations and the remaining frontier

Concrete tests that would confirm or break the mechanism, in ascending cost:

1. **Validate the dictionary on Taub–NUT–AdS.** Recompute $W^+=2(h-\tfrac13 I)+\mathcal T$ symbolically on the Step‑10 family and confirm it reproduces the half-conformally-flat result $W^+=0$ and the $H^4$ limit; this checks the twist term $\mathcal T$ and the electric–magnetic balance numerically.
2. **Biaxial Bianchi IX / squashed-$S^3$ cohomogeneity-one Einstein ODE (Ric $=-g$).** Reduce to the ODE for the three principal fiber lengths and integrate; read off $h$ and $W^+$ along the flow to see whether any orbit sustains anisotropic constant-spectrum $W^+$ into small fiber length, or whether it is always driven to $W^+\to0$ at the closing orbit. This directly probes the twist-supported residue in the most symmetric setting.
3. **Twisted circle bundle over a hyperbolic 3-base.** Take $g_B$ hyperbolic-type with $\operatorname{Ric}^B$ near $\operatorname{diag}(-\tfrac34,-\tfrac58,-\tfrac58)$ and solve the reduced system of §5 for $(\ell,A)$; test whether the Obata integrability obstructs a nonconstant calibrated solution, giving a computational read on §2's rigidity with twist included.
4. **Morrey exponent for $\ln\ell$.** Quantify the $W^{2,2}\!\to$ oscillation constant in §3 to sharpen $\rho_*(K)$ and confirm the fixed-point energy gaps $\varepsilon_0$, $c_0$, $r_0$ are dimensional constants.

**What remains genuinely open.** This mechanism settles the rank‑one circle stratum. The frontier is (i) higher-rank collapse — $T^2$, $T^3$, and nonabelian (nil, Berger $SU(2)$) F‑structures, where unwrapping a single circle need not decollapse and the base is lower-dimensional still; the reduced-system and projector-obstruction ideas of §§2,5 should be pushed to $T^k$-reductions where $W^+$ becomes a function of a *matrix* fiber-Gram tensor and several twists; and (ii) the varying-topology case $A_i\to\infty$, where the deficits are only $o(A_i)$ and a small noncollapsed island can absorb defect, so the absolute energy inputs of §3 weaken to measure-relative form (as already noted in Step 6). Both are the correct next objects; neither is touched by the circle argument, and the logical reduction $Q_n\Leftrightarrow P_n^+\lor P_n^-$ still requires the positive-scale branch independently.
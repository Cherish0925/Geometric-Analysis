# Step 34: Mode-diagonal indicial theorem, resonance analysis, and collapsed-front identification

## 0. Scope and target fidelity

This note concerns the four-dimensional positive subroute of the full Yau-26 problem. It does not prove or refute the full proposition and does not address dimensions $n\ge5$, the negative branch, or Lean formalization.

The exact active target: for every $n\ge2$, decide whether dimension-only $c_n<C_n$ exist such that $c_ng\le\operatorname{Ric}_g\le C_ng$ implies the same closed connected smooth $M$ admits some Einstein metric, with no proximity, symmetry, topology, noncollapse, or sign assumptions.

## 1. Mode-diagonal indicial theorem on $C(S^3/\mathbb{Z}_2)$

### Statement

On the flat cone $\mathbb{R}^4/\{\pm1\}$ with metric $\mathbf{e} = dr^2+r^2g_{S^3}$, the linearized Einstein operator $\operatorname{Ric}_\mathbf{e}^{(1)}$ and the bilinear Taub–Wronskian form $\operatorname{Ric}_\mathbf{e}^{(2)}$ preserve the angular harmonic decomposition on $S^3/\mathbb{Z}_2$.

Symmetric 2-tensors on the cone decompose by angular degree $l$. The $\mathbb{Z}_2$ quotient keeps only even $l\in\{0,2,4,\ldots\}$. For each $l$, the homogeneous solutions of the linearized equation in Bianchi gauge have radial rates:
$$
\alpha_{\rm reg} = l,\qquad \alpha_{\rm sing} = -(l+2).
$$
The key properties are:

1. **Mode-diagonality of the Wronskian.** The boundary integral
$$
\int_{S^3/\mathbb{Z}_2}\operatorname{Ric}_\mathbf{e}^{(2)}(h_l, k_{l'})(X,\partial_r)\,dv = 0\quad\text{if }l\ne l',
$$
by orthogonality of tensor harmonics on $S^3/\mathbb{Z}_2$.

2. **Gauge triviality of $l=0$.** The growing $l=0$ mode is the constant cone metric / linear-coordinate gauge, removable by tangent-cone normalization. The decaying $l=0$ mode is the mass/volume parameter $r^{-2}$, which is the ALE mass. It is **Wronskian-invisible** to $l\ge2$ test fields by angular orthogonality.

3. **$l=2$ is the Ozuch obstruction.** The growing mode $H_2\sim r^2$ is the orbifold curvature 2-jet. The decaying mode $H^4\sim r^{-4}$ is the EH asymptotic coefficient. Their Wronskian, via Ozuch (2021) Corollary 4.10:
$$
\int_{S^3/\mathbb{Z}_2}\operatorname{Ric}_\mathbf{e}^{(2)}(H_2, H^4)(r\partial_r,\partial_r)\,dv = C\cdot R^+_{kl}
$$
where $R^+$ is the first variation of the self-dual Weyl curvature of the orbifold. This is exactly zero iff the Ozuch first-obstruction $R^+_\mathbf{e}(H_2)\omega_1^+=0$ is satisfied, equivalently iff $W^+$ has eigenvalue $-1/3$ at the singular point.

### Source support

Ozuch 2021 \cite{ozuch2021integrability} equation (59) line 626:
$$
\operatorname{Ric}_\mathbf{e}^{(2)}(H^4, H_2) = \sum_j R^+_{kj}\frac{\theta_l^-\circ\omega_j^+}{r^4}
$$
lives in the same angular space as $H^4 = \theta_l^-\circ\omega_k^+/r^4$, confirming mode-diagonality at the algebraic source level.

## 2. Pairing table at the balance radius

Convention: $t^4$ for the ALE insertion coefficient; balance radius $r=t^{2/3}$.

| Mode | Rate pair | Size at $r=t^{2/3}$ | Signal | Status |
|------|-----------|---------------------|--------|--------|
| $l=0$ mass | $(0,-2)$ | reg: $1$, sing: $t^{2/3}$ | Angular-orthogonal to $l\ge2$ | Gauge/invisible |
| $l=2$ Ozuch | $(2,-4)$ | reg: $t^{4/3}$, sing: $t^{4/3}$ | $\mathbf{t^4}$ **(radius-independent)** | **Main obstruction** |
| $l=4$ higher | $(4,-6)$ | reg: $t^{8/3}$, sing: $t^{8/3}$ | $t^{16/3}\ll t^4$ | Subleading |
| Cross $l\ne l'$ | — | — | $0$ | Angular orthogonality |
| Same-dir $(2,2)$ | — | $t^{8/3}\ll t^4$ | $0$ (Wronskian antisymmetry) | Vanishes |
| Same-dir $(-4,-4)$ | — | — | $0$ (Wronskian antisymmetry) | Vanishes |

**Key observation from the strategist:** The $l=0$ mass mode has size $O(t^{2/3})$ at the balance radius, which is **larger** than the $l=2$ modes ($O(t^{4/3})$). But it is invisible to the $l=2$ Wronskian by mode-diagonality. This means the metric need not be "cone + two modes + small." All that must hold is that the **flux-visible** part is the $l=2$ dual pair.

## 3. Resonance analysis

### The radial ODE

In the $l=2$ sector, the inhomogeneous radial equation is:
$$
f'' + \frac{3}{r}f' - \frac{8}{r^2}f = S(r),
$$
with homogeneous solutions $r^2$ and $r^{-4}$, Wronskian $W=-6r^{-3}$.

### Source from Ricci defect

A $\delta$-small Ricci-endomorphism defect $E = \operatorname{Ric}_g - \Lambda g$ with $|E|\le\delta$ projects onto the $l=2$ sector with a source $S_2(r)$ that is approximately constant ($\sim\delta$) in the transition region.

### Variation of parameters

For a constant source $S=\delta$, the particular solution on $[r_0, r]$ is:
$$
f_p(r) = \frac{\delta}{6}\,r^2\log\frac{r}{r_0} - \frac{\delta}{36}\bigl(r^2 - r_0^6 r^{-4}\bigr).
$$

The first term is the **logarithmic resonance**: rate $r^0$ resonates with the $r^2$ homogeneous mode, producing $\delta r^2\log r$.

### Resonance at the balance radius

At $r=t^{2/3}$ with $r_0\sim t^{1/2}$ (ALE scale):
$$
|f_p^{\rm resonant}| = \frac{\delta}{6}\,t^{4/3}\cdot\frac{1}{6}\log\frac{1}{t} = \frac{\delta}{36}\,t^{4/3}\log\frac{1}{t}.
$$

This correction enters the Wronskian as an additive error to the $r^2$ coefficient:
$$
\text{Wronskian error} = C\,\delta\,t^4\,\log\frac{1}{t}.
$$

**Relative error:** $C\,\delta\,\log(1/t)$.

### Can the Bianchi identity remove the resonance?

**No.** The contracted Bianchi identity $\operatorname{div}_g E=0$ constrains the **total** error, not each angular $l$-component separately. The $l=2$ projection of $E$ need not itself be divergence-free; cancellation with other $l$-components is allowed. Therefore the constant ($r^0$) source in the $l=2$ sector is not automatically killed.

### Rate condition — RETRACTED (Steps 35–36)

**The condition $\delta_i\log(1/t_i)\to0$ is an artifact of reading the growing $H_2$ coefficient through the neck.** In the rescaled bubble frame $\hat g=t^{-2}g$, the Ricci defect has size $t^2\delta$ and the signal has size $t^2(R_+v)$. Over a fixed annulus $\rho\in[1,R]$, relative nonconservation is $O(\delta\log R)+O(1/R)$. The correct procedure is the iterated limit: fix $R$ large, let $\delta_i\to0$, then $R\to\infty$. No coupling between $\delta$ and $t$ survives.

See `workspace/notes/step36_edge_cone_accounting_correction.md` §1 for the full correction.

## 4. Updated Route-A bridge statement

**A2 (balanced-annulus comparison).** At $r\approx t^{2/3}$, after Bianchi/volume gauge, the metric equals
$$
\mathbf{e} + A_2 r^2 T_2 + t^4 B_{-4} r^{-4} T_2 + (\text{$l=0$ mass/gauge}) + (\text{$l\ge4$ subleading}) + \text{corrections}.
$$
The $l=2$ Wronskian signal is $t^4\cdot R^+\cdot v$. The relative error is $O(\delta)+O(\delta\log R)+O(1/R)$ for fixed $R$ in the bubble frame. **No rate condition between $\delta$ and $t$ is required** (iterated limit; see Step 36 correction).

If $R^+\cdot v\ne0$, then $\delta$ is bounded away from zero for any bubble scale $t$.

Combined with Theorem A (regular limit gives Einstein metric) and the spectral partition ($\det R_+=0$ is codimension-1), this gives:
- Branch (a): smooth limit → Einstein metric on $M$. **Done.**
- Branch (b) with $\det R_+\ne0$ (e.g., $S^4$-like limit): no EH bubble possible. Either the sequence is regular (back to (a)) or another singularity type appears, requiring further analysis.
- Branch (b) with $\det R_+=0$: EH bubble allowed, but the Wronskian argument shows the first obstruction must vanish (it does by hypothesis). Higher-order obstructions remain open.

## 5. Collapsed-front structural identification

The strategist identified a crucial structural connection for the collapsed positive branch.

### Energy quantization in collapse

For a collapsing sequence with $\|\operatorname{Ric}_g-g\|_{\rm op}\to0$ and $\operatorname{Vol}\to0$, CGB with scalar curvature $s=4(1+O(\delta))$ gives:
$$
\int|W|^2 + \frac{s^2}{24}\operatorname{Vol} \le 8\pi^2\chi,
$$
and in the limit $\delta\to0$:
$$
\int|W|^2 \to 8\pi^2\chi\quad\text{exactly.}
$$
The signature identity splits: $\int|W^\pm|^2\to2\pi^2(2\chi\pm3\tau)$. This is a **quantization statement**, not merely an inequality.

### The $\alpha$-family bolt rescaling

For the toric $\alpha$-family with edge curvature $A_m = m^\alpha$ ($1<\alpha\le2$):

- Each rod's bolt is an $S^2$ with Gaussian curvature $K_\Sigma = 1+2A$.
- Bolt area $\approx 4\pi/(1+2A)\approx 2\pi/A$ for large $A$.
- Collar transverse width $\approx L/2\pi = \pi/(2\pi\sqrt{1+2A})\approx 1/(2\sqrt{A})$.
- Curvature at bolt: $|\operatorname{Rm}|\sim 2A$.
- Energy per bolt region: $\int|\operatorname{Rm}|^2\approx (2A)^2\cdot(2\pi/A)\cdot(\pi/A) = 8\pi^2$.

**One quantum per rod**, with $m=\chi-2$ rods (for the $\#_k(S^2\times S^2)$ family).

### Rescaled limit is Euclidean Schwarzschild

Rescaling a bolt neighborhood by $\sqrt{2A}$:
- Distances scale by $\sqrt{2A}$, curvature by $1/(2A)$.
- The cosmological constant $\Lambda=1$ rescales to $\Lambda/(2A)\to0$.
- The limit is a **Ricci-flat ALF metric with an $S^2$ bolt**: this is **Euclidean Schwarzschild**.

More precisely, the Step-17 SdS dictionary gives the cone-angle ratio $\mu(A) = 1-\frac{4}{3}A+O(A^2)$. The rescaled metric limit as $A\to\infty$ is:
$$
\hat M = \frac{\sqrt{2A}(A+1/3)}{(2A+1)^{3/2}} \to \frac{1}{2},\qquad \rho^{2/3}\to0,
$$
i.e., Euclidean Schwarzschild at mass $M=1/2$ with vanishing cosmological constant.

### Structural consequence

The collapsed adversary is an **ALF bubble tree**, one bubble per rod. And the Step-17 rigidity $\mu=1\iff A=0$ is precisely the **exact-Einstein obstruction**, expressed as a cone-angle defect rather than a curvature defect.

**Critical difference from noncollapsed case:** Euclidean Schwarzschild is:
- **Ricci-flat** but **not anti-self-dual** (it has both $W^+$ and $W^-$).
- **ALF** (asymptotically locally flat), not ALE.
- Therefore the LeBrun–Ozuch admissibility hypothesis ($W^+=0$ on ALE bubbles) does **not** apply to the collapsed case.

This means the noncollapsed and collapsed halves of $P_4^+$ require **different obstruction theories**:
- Noncollapsed: ALE bubbles, Ozuch $R^+$ obstruction, potential LeBrun–Ozuch classification.
- Collapsed: ALF bubbles (Euclidean Schwarzschild), cone-angle obstruction, different bookkeeping via edge-cone Chern–Weil (Step 16 Atiyah–LeBrun).

## 6. Correction: A03 retraction of message #330

Messages #332 and #333 from A03 retract the per-manifold conclusion from message #330. The error was a Sobolev-constant convention mix-up: $S^2$ vs $S_{\rm cal}$ in the embedding constant. The correct embedding gives a collapse-independent absorption coefficient. Additionally, Ricci lower bound plus total volume does not bound diameter or fixed-radius ball volume on fixed topology.

**Corrected status:** The negative cutoff-flow route remains **unresolved** (neither dimension-uniform nor per-manifold). The genuine open work is the spacetime recurrence with all time factors retained.

Step 33 §9's assimilation of #330 (recording the per-manifold conclusion) is **invalid** and must not be used.

## 7. Current Route-A load-bearing obligations

1. **Harmonic-radius epsilon lemma** (merges A1/A2): noncollapse + $C^0$ Ricci pinching + small annular $L^2$ energy $\Rightarrow$ harmonic-radius control at the annulus scale. This may also remove the logarithmic resonance.

2. ~~**Resonance resolution**~~: **RESOLVED (Steps 35–36).** No rate condition between $\delta$ and $t$ is needed. The rescaled bubble-frame iterated limit removes the logarithmic artifact.

3. **Higher-order obstructions** for the $\det R_+=0$ case: Ozuch's Theorem 0.15 excludes some configurations, but the chessboard family survives all known constraints (at $\Lambda=0$). The positive-$\Lambda$ version remains open.

4. **Collapsed positive branch**: the ALF/Euclidean-Schwarzschild identification gives a new structural starting point but requires a separate obstruction theory.

## Files

- Script: `workspace/scripts/step34_indicial_modediag_resonance.py`
- Data: `workspace/data/step34_indicial_modediag_resonance.json`
- This note: `workspace/notes/step34_indicial_modediag_resonance_and_collapse.md`

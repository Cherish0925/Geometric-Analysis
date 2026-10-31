# Step 36: Edge-cone accounting correction and Route A consolidation

**⚠ PARTIALLY SUPERSEDED by Step 38:** `workspace/notes/step38_period_transport_corrected_collapse.md`

Step 37 (Preceptor) identified that §5–6 below contain a false inference:
"alternating adjacent Delzant labels exclude struts." This is WRONG. Conical
singularities live on rods (period defects), not at corners. Nonadjacent rods
with labels $\pm v$ generate the same circle and must share a global period.
The NUT smoothing cost argument in §5–6 is based on this false premise.
§§1–4 (Route A correction, edge-cone accounting, rod count) remain valid.

Session S0910A02, Agent2/Constructor, Execute.

## 0. Scope and target fidelity

This note corrects the collapsed-front energy accounting from Steps 34–35 and consolidates the noncollapsed Route A theorem. It concerns the four-dimensional positive subroute only. Nothing here proves or refutes the full Yau-26 proposition.

Active target: for every $n\ge2$, decide whether dimension-only $c_n<C_n$ exist such that $c_ng\le\operatorname{Ric}_g\le C_ng$ on any closed smooth manifold implies it admits some Einstein metric.

---

## 1. Correction: δ log(1/t) is an artifact, not a theorem hypothesis

**Step 34 claimed** that the balanced-annulus Wronskian comparison carries a rate condition $\delta_i\log(1/t_i)\to0$, arising from a logarithmic resonance in the $l=2$ radial ODE.

**Step 35 corrected this.** The log arises from reading the *growing* $H_2$ coefficient by pairing against $r^{-4}$ through a long neck. In the rescaled bubble frame $\hat g = t^{-2}g$:
- The Ricci defect has size $t^2\delta$ relative to the fixed EH scale
- The ambient curvature signal is $t^2(R_+v)$
- Over a fixed annulus $\rho\in[1,R]$, relative Wronskian nonconservation is $O(\delta\log R)+O(1/R)$
- **Iterated limit:** fix $R$ large, let $\delta_i\to0$, then $R\to\infty$. No coupling between $\delta_i$ and $t_i$ survives.

The certificate at `workspace/data/step35_rescaled_flux_and_rod_chain.json` verifies: for any $\epsilon>0$, choosing $R=8/\epsilon$ and then $\delta<\epsilon/(8\log R)$ gives relative error $<\epsilon$.

**The real missing input** (unchanged from Step 30) is the second-order bubble-frame blow-up:
$$k = \lim_{i\to\infty}\frac{\hat g_i - g_{\rm EH}}{t_i^2}$$
with quadratic growth, solving $D\operatorname{Ric}_{\rm EH}(k)=\Lambda g_{\rm EH}+O(\delta_i)$, and matching of $k$'s quadratic part to the orbifold 2-jet. The Cheeger–Naber $C^{1,\alpha}\cap W^{2,q}$ convergence does not transmit a 2-jet for non-Einstein $g_i$.

---

## 2. Noncollapsed Route A: current honest statement

**Theorem A (unconditional regular limit).** Let $(M_i^4, g_i)$ be closed with $\|\operatorname{Ric}_{g_i}-g_i\|_{\rm op}\le\delta_i\to0$ and $\operatorname{Vol}(M_i)\ge v_0>0$. If the Cheeger–Naber limit orbifold has no singular set, then $M_i$ admits an Einstein metric for all large $i$.

*Proof:* Myers/Bishop give diameter upper bound and global noncollapse. Cheeger–Naber convergence gives a $C^{1,\alpha}\cap W^{2,q}$ limit solving $\operatorname{Ric}=g$ weakly. Elliptic regularity gives smoothness. Cheeger–Gromov diffeomorphism recovery puts the Einstein metric on the original $M_i$.

**Route-A bridge (conditional).** If the limit orbifold has singular points, EH bubbles can form only at points satisfying $\det R_+=0$ (Ozuch first obstruction). The mode-diagonal indicial structure (Step 34) shows:

1. The $l=0$ mass/volume mode is Wronskian-invisible to the $l=2$ obstruction mode by angular orthogonality.
2. The $l=2$ Wronskian is radius-independent (signal $O(t^4)$).
3. Higher modes and cross-mode pairings are subleading.
4. **No rate condition between $\delta$ and $t$ is forced** (bubble-frame iterated limit).

The remaining load-bearing inputs are:
- **A1:** Harmonic-radius epsilon regularity for merely $C^0$-Ricci-pinched metrics (not established; CZ spike compatible)
- **A2:** Second-order bubble-frame convergence and 2-jet matching (Step 35 formulation)

---

## 3. Correction: edge-cone accounting for the collapsed front

### The error in Steps 34–35

Steps 34–35 argued: "each bolt consumes exactly $8\pi^2$ of Weyl energy, $\chi$ bolts saturate $8\pi^2\chi$, leaving no slack for struts." The strategist correctly identified this as conflating two different terms in the Gauss–Bonnet identity.

### The Atiyah–LeBrun edge-cone formulas

Source: Atiyah–LeBrun, arXiv:1203.6389, Theorems 2.1, 2.2, Theorem A.

For a 4-manifold with edge-cone singularity of angle $2\pi\beta$ along embedded surface $\Sigma$:

**Gauss–Bonnet:**
$$\chi(M)=\frac{1}{8\pi^2}\int_{M-\Sigma}\left(|W|^2-2|\mathring{\operatorname{Ric}}|^2+\frac{s^2}{24}\right)dV+(1-\beta)\chi(\Sigma)$$

**Signature:**
$$\tau(M)=\frac{1}{12\pi^2}\int_{M-\Sigma}(|W^+|^2-|W^-|^2)\,dV-\frac{1-\beta^2}{3}[\Sigma]^2$$

The defect terms $(1-\beta)\chi(\Sigma)$ and $(1-\beta^2)[\Sigma]^2/3$ are **separate** from the bulk curvature integrals. A strut enters through these defect terms, not as additional $\int|W|^2$. Therefore "bulk energy saturated $\Rightarrow$ no room for struts" does not follow directly.

### But the smooth metrics have no defect terms

For the smooth $g_i$ ($\beta=1$ everywhere), the standard CGB applies:
$$\int|W|^2_{g_i}+\frac{s^2}{24}\operatorname{Vol}_{g_i}=8\pi^2\chi.$$
As $\operatorname{Vol}\to0$ and $s\to4(1+O(\delta))$, the bulk Weyl energy $\int|W|^2\to8\pi^2\chi$.

If the limit develops edge-cone singularities, the smooth approximants must **smooth them**, contributing curvature to the bulk integral. This smoothing cost lives in $\int|W|^2_{g_i}$, competing with the bolt curvature for the total budget $8\pi^2\chi$.

---

## 4. The crucial structural finding: NUTs, not struts

### Alternating rod labels in the toric α-family

The toric $\alpha$-family on $\#_k(S^2\times S^2)$ has a Delzant polygon with $\chi=2+2k$ edges. The Delzant condition requires adjacent edge normals to form a $\mathbb Z^2$-basis, which forces **alternating labels**: adjacent rods collapse *different* circles.

- At each **bolt** (rod interior): one $S^1$ degenerates, the other is regular. This is a codimension-2 fixed set (an embedded $S^2$).
- At each **NUT** (corner): both $S^1$ factors degenerate to a point. This is a codimension-4 fixed point.

**There are no axis segments where neither circle degenerates.** Between any two rods, the transition goes through a NUT (codim-4 point).

### NUTs are not struts

An Israel–Khan strut is a codimension-2 conical deficit on an axis where one circle remains regular. The edge-cone defect terms apply to this.

A NUT is a codimension-4 point where both circles degenerate. It is an **orbifold point**, not an edge-cone singularity. The Atiyah–LeBrun edge-cone formula does not apply to NUTs.

### Energy cost of NUT smoothing

A codimension-4 point singularity in 4D has curvature concentrated in a ball of radius $\varepsilon$:
$$\int_{\text{NUT}}|{\rm Rm}|^2\sim\frac{1}{\varepsilon^4}\cdot\varepsilon^4=O(1).$$
Compare to the strut smoothing cost for codimension-2:
$$\int_{\text{strut}}|{\rm Rm}|^2\sim\frac{(1-\beta)^2|\Sigma|}{\varepsilon^2}\to\infty\quad\text{as }\varepsilon\to0.$$

**NUT smoothing costs $O(1)$, not $O(\sqrt{A})$.** The divergent strut energy argument does not apply.

### Comparison with same-label rods

The Step-17 rigidity theorem ($\mu=1\iff A=0$) concerns **same-label** rods: both bolts collapse the *same* $S^1$ (cohomogeneity-one $S^1\times SO(3)$ symmetry). In that case, the axis between bolts is where the other $S^1$ is regular, creating a codimension-2 strut potential.

The alternating-label case is structurally different: the Delzant condition prevents same-label adjacent rods for *any* toric 4-manifold.

---

## 5. Revised collapsed-front assessment

### Energy budget

For the smooth collapsing $g_i$ on $\#_k(S^2\times S^2)$:
$$\int|W|^2_{g_i}\to8\pi^2\chi.$$
The decomposition is approximately:
$$8\pi^2\chi\approx\underbrace{\chi\times 8\pi^2}_{\text{bolts}}+\underbrace{\chi\times O(1)}_{\text{NUTs}}+\underbrace{\text{negligible}}_{\text{collars}}.$$

The NUT contributions are $O(1)\ll 8\pi^2\approx 79$, so the budget is asymptotically consistent. This is why no coarse integral identity has killed the $\alpha$-family.

### The $\alpha$-family survives this analysis

With alternating labels:
- All rod, corner, spectral, and CGB conditions are satisfied (Steps 19–26)
- NUT smoothing is $O(1)$ per NUT (no energy divergence)
- Bolt energy $\approx 8\pi^2$ per bolt saturates the budget with $O(1)$ slack per unit cell
- No topology-uniform energy obstruction has been found

### What could still kill the collapsed adversary

1. **Global nonlinear filling failure:** The formal local model does not guarantee a smooth global metric. The nonlinear PDE problem of constructing a global toric metric with the prescribed rod structure and near-Einstein Ricci is open.
2. **Bochner/Killing obstruction (Steps 28–29):** The weighted Bochner bound controls the central bracket in $L^2$ average. Converting this to the geometry needed for collapse control requires the missing "almost-Killing" bridge.
3. **Holonomy or fundamental-group obstruction:** Not investigated for this family.
4. **Higher-order conformal obstruction or new integral identity.**

### What a BREAK would require

Even if a smooth collapsing family with $\operatorname{Ric}\to g$ exists on $\#_k(S^2\times S^2)$, this is a Yau-26 counterexample only if $\#_k(S^2\times S^2)$ admits **no Einstein metric of any sign**. No such nonexistence result is known for $k\ge2$.

---

## 6. The Weyl rod-chain question

The rescaled collapsed limit is a periodic Ricci-flat toric metric with alternating-label rods and smooth NUTs. In the Euclidean Weyl formalism:

- Each bolt rescales to Euclidean Schwarzschild (mass $M=1/2$, $\Lambda=0$)
- NUTs should become multi-Taub-NUT-type centers
- But Schwarzschild is NOT self-dual, while multi-Taub-NUT IS

The key PDE question: **does a smooth periodic alternating toric Ricci-flat 4-manifold exist with Schwarzschild-type bolts and smooth NUT transitions?**

Known examples:
- Multi-Taub-NUT / Gibbons–Hawking: smooth, self-dual, ALF. Has smooth NUTs but no $S^2$ bolts.
- Euclidean Schwarzschild: single $S^2$ bolt, ALF, NOT self-dual.
- Israel–Khan: multiple same-label bolts, has forced struts.

The alternating-label case with mixed Schwarzschild bolts and NUTs is a **new Weyl problem** not covered by the standard Israel–Khan or multi-Taub-NUT literature. Its resolution would decide the collapsed positive branch.

---

## 7. Summary of Route A status

| Component | Status | Load-bearing input |
|-----------|--------|-------------------|
| Regular limit (Theorem A) | **Proved** (unconditional) | Cheeger–Naber + elliptic reg |
| Mode-diagonal indicial | **Verified** (Step 34) | Flat cone + Ozuch eq (59) |
| Bubble-frame no-rate | **Corrected** (Step 35) | Iterated $R,\delta$ limit |
| Harmonic-radius ε-reg | **Open** (A1) | CZ-spike compatible |
| 2-jet bubble matching | **Open** (A2) | Hard; beyond $C^{1,\alpha}$ |
| Collapsed NUT accounting | **Corrected** (this step) | NUT ≠ strut; O(1) energy |
| Global Weyl rod-chain | **Open** | New PDE problem |
| Collapsed Bochner bridge | **Open** (Steps 28–29) | Almost-Killing from Ric |
| Higher-order obstruction | **Open** | Ozuch chessboard at $\Lambda=0$ |

The complete four-dimensional positive branch ($P_4^+$) requires closing BOTH the noncollapsed (A1+A2) and collapsed (Bochner bridge or Weyl rod-chain) components.

---

## Files

- Script: `workspace/scripts/step36_edge_cone_strut_scaling.py`
- Data: `workspace/data/step36_edge_cone_strut_scaling.json`
- Script: `workspace/scripts/step36_alternating_rod_analysis.py`
- Data: `workspace/data/step36_alternating_rod_analysis.json`
- This note: `workspace/notes/step36_edge_cone_accounting_correction.md`

# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A01/workspace/data/step33/cusp_closing_Wminus.json",
    "Sessions/S1003A01/workspace/scripts/step33_cusp_closing_Wminus.py",
    "Knowledge/objects/papers/Weyl-energy-and-connected-sums-of-four-manifolds--aac98700a100--c47de95b9e22/object.md",
    "Knowledge/objects/papers/1303.0827-Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--ac8a5635dfbc--5258e72d2de1/object.md",
    "Knowledge/objects/papers/Degenerating-Kähler-Einstein-cones-locally-symmetric-cusps-and-the-Tian--adb04d311c2f--499d8f08a8b4/object.md"
  ]
}
```

## Task

Propose high-value next mathematical routes for the ramification-cap interaction problem, beyond repeating the separated-retention argument. Context: Existing certified CH perpendicular blow-up cell gives sub-four coefficient; Step 33 shows the upper law depends on blow-up fraction theta while lower theory depends on sigma=4r+18theta. The r-gap is now localized to ramification neighbourhoods carrying the KE background W^- energy B_Delta. Kähler blow-up cells have exact unit tariff; cheap cells require non-Kähler/paired-field relative rotation. We need genuinely different geometry: compute or bound the cost of a blow-up/handle cell in the exact cusp-closing Calabi KE cap near the elliptic divisor, and then decide what is realizable in actual ramified towers. Please propose concrete, technically plausible routes (analytic, variational, numerical, symbolic, gauge-theoretic, or local model construction) that could decide whether interacting cap cells improve the upper law or whether a localized field/volume estimate enforces retention. Tie each route to the actual formulas and sources, state what first calculation or proof object should be built, and warn against low-value distractions.

## Output

# High-Value Routes for the Ramification-Cap Interaction Problem

## Orientation: What Must Be Decided

The core dichotomy, precisely stated in Step 33 §4, is:

*Does there exist a metric family on $M_m$ with $\mathcal{E}/h < 4(1-6\theta)$ for positive $r$?*

Answering yes requires constructing cells that deplete the anti-self-dual energy $B_\Delta = 8\pi^2\Delta/3$ at a favourable exchange rate. Answering no requires proving a localized retention inequality $B \geq B_\Delta - C(P + L_s + S - S_0) - o(Q)$. The separated-depletion argument of Step 33 shows that depletion *spatially separated* from surgery never improves the coefficient. So the unresolved question is whether surgery cells that *interact* with the cusp-closing geometry near the ramification divisor $D'$ can achieve lower cost than CH-site cells.

Below are five routes, ordered by the precision of the first calculation each demands.

---

## Route 1: Second-Order Cost on the Exact Calabi Cap

**Mechanism.** The cusp-closing Kähler–Einstein model from Biquard–Guenancia (and verified in `cusp_closing_Wminus.json`) is
$$g = \tau\,(dx^2 + dy^2) + \frac{d\tau^2}{\Theta(\tau)} + \Theta(\tau)\,\eta^2, \qquad \Theta = \tfrac{2}{3}\tau^2 - c/\tau,$$
with $s = -4$, $|W^+|^2 = 2/3$, $|W^-|^2 = 6c^2/\tau^6$. The metric closes smoothly at $\tau_0 = (3c/2)^{1/3}$, where the divisor $D'$ sits.

Step 33's first-order neutrality shows that gluing the certified cell into this background (instead of pure CH) changes the cost $D = \int |\operatorname{Ric}+g|^2$ only at second order in the background deviation $\kappa = g_{\text{Calabi}} - g_{CH}$. The deviation on the collar annulus $\{\tau_0 + \delta \leq \tau \leq \tau_0 + R\}$ is controlled by:
$$\kappa_{ij} = -\frac{c}{\tau}\,(\text{terms from }\Theta^{-1}\text{ and connection form}) = O(c/\tau_0) = O(e_c^{1/3})$$
where $e_c$ is the Euler number of the circle bundle (self-intersection of $D'$). On the collar, where $\operatorname{Ric}+g = 0$ at zeroth order, the linearised Einstein operator $D(\operatorname{Ric}+g)[\chi\kappa]$ vanishes, so:
$$\delta D = \int_{\text{collar}} |D(\operatorname{Ric}+g)[\chi\kappa]|^2 + 2\langle \operatorname{Ric}+g,\, D^2(\operatorname{Ric}+g)[\chi\kappa,\chi\kappa]\rangle = O(\|\kappa\|_{C^2}^2).$$

**First calculation.** Use the SymPy Riemann/Weyl computation framework (already in `step33_cusp_closing_Wminus.py`) to:
1. Compute the Christoffel symbols of $g_{\text{Calabi}}$ in the collar region $\tau \in [\tau_0 + \epsilon, \tau_0 + R]$ (where $R = e^{7.645/2} \approx 45$ in the $\operatorname{Ric}=-g$ scaling).
2. Evaluate the deviation $\kappa$ from the round CH metric in the same collar coordinates.
3. Compute the quadratic form $\delta^2 D[\kappa,\kappa]$ symbolically. This is a radial integral on the collar, involving the cell profile functions $(F,G)$ from the certified cell and the deviation tensors from the Calabi cap.

**What it would distinguish.** If $\delta^2 D > 0$, ramification-site cells cost *more* than CH-site cells, and the upper law is $r$-independent at second order — retention holds for the construction. If $\delta^2 D < 0$, cells placed near the divisor are genuinely cheaper, the upper bound improves with $r$, and the gap between upper and lower theory narrows for $r > 0$.

**Warning against distraction.** Do *not* attempt to solve the full cell ODE on the Calabi background. The second-order expansion around the CH solution is sufficient and orders of magnitude cheaper. The cell profile is already certified; only the background changes.

---

## Route 2: Weyl Interaction Classification at Ramification Points

**Mechanism.** Malchiodi–Malizia (Theorem 1.1 and Proposition 5.13, equation (1.6)) prove that for connected sum $Y = Z \# M$ the Weyl energy balance is:
$$\mathcal{W}^Y(g_Y) - \mathcal{W}^M(g_M) - \mathcal{W}^Z(g_Z) = a^4\!\left(C - \tfrac{4}{9}\pi^2\lambda^2\, W^{\bar M}(p) \circledast W^Z(q) + O(\lambda^2\gamma^2)\right) + \text{h.o.t.}$$
where the interaction product is (Gursky–Viaclovsky, Lemma 12.2):
$$W^{\bar M}(p) \circledast W^Z(q) = \tfrac{3}{2}\langle W^{\bar M}(p),\, W^Z(q)\rangle$$
after simultaneous diagonalisation.

For a blow-up at a ramification point $q \in D'_\lambda$, with $M = \overline{\mathbf{CP}}^2$ (Burns metric, self-dual: $W^+_{FS} = \operatorname{diag}(4,-2,-2)$, $W^-_{FS} = 0$ in the $R=24$ normalisation), one has $\bar M = \mathbf{CP}^2$ so $W^-_{\bar M} = W^+_{FS}$ and $W^+_{\bar M} = 0$. At a CH site ($W^-_Z = 0$), the ASD–ASD interaction vanishes; at a ramification site ($W^-_Z \neq 0$), it does not.

**First calculation.** From the cusp-closing model, at the divisor ($\tau = \tau_0$):
$$|W^-|^2(q) = 6c^2/\tau_0^6 = 8/3$$
independent of $c$. The $W^-$ eigenvalues on $\Lambda^-$ can be extracted from the full Weyl tensor computation (the SymPy script already computes the Weyl tensor; one needs only the $\Lambda^-$ eigenvalues at $\tau = \tau_0$). Since the Calabi model is $U(1)$-symmetric with a flat torus base, $W^-$ at the bolt is determined by a single parameter.

Compute $W^-_Z(q)$ eigenvalues $(\lambda^-, \mu^-, \nu^-)$ at $\tau_0$. Then:
$$W^{\bar M} \circledast W^Z = 6(4\lambda^- - 2\mu^- - 2\nu^-) = 6\cdot 4\lambda^- \quad (\text{since }\lambda^- + \mu^- + \nu^- = 0)$$

**What it would distinguish.** If the product is positive, the Weyl energy of $Z \# \overline{\mathbf{CP}}^2$ can be made strictly less than at a CH site (where it vanishes). This geometric effect suggests that ramification-site cells interact favourably with the $W^-$ reservoir. If the product is zero (e.g., if $W^-$ at the bolt has eigenvalues proportional to $(2/3, -1/3, -1/3)$, matching $W^+_{KE}$, which would give the interaction $6(8/3 + 2/3 + 2/3) = 24 > 0$), the Weyl energy decreases more at ramification sites than at CH sites.

Note: a positive Weyl interaction does not immediately reduce the cell cost $D = \int|\operatorname{Ric}+g|^2$ (which involves the full Ricci tensor, not just Weyl). But it identifies a geometric channel through which the ramification geometry can influence the cell, and provides the leading term for Route 1.

---

## Route 3: Spectral Stability and Global $W^-$ Retention

**Mechanism.** The Kähler–Einstein metric on $\bar X$ minimises $\int |W^-|^2$ among KE metrics on $X^\circ$ with the given topology at infinity (this follows from $B_\Delta = 8\pi^2\Delta/3$ being an exact topological computation plus $|W^-|^2 \geq 0$). Any metric $g$ on $M_m = \bar X_m \# k\overline{\mathbf{CP}}^2 \# \ell(S^1\times S^3)$ that agrees with $g_{KE}$ outside a compact region must satisfy:
$$\int_{M_m} |W^-_g|^2 \geq \int_{\bar X_m \setminus \text{surgery}} |W^-_{KE}|^2 - \int_{\text{surgery}} |W^-_{KE}|^2 + 0$$
since the surgery regions are chosen CH-close (where $|W^-_{KE}| = O(\varepsilon)$). The question is whether $W^-$ can be *transferred* from the ramification neighbourhood to the surgery region.

The Einstein linearisation stability of the KE metric constrains this. On a stable KE manifold, the second variation $\delta^2 \int |W^-|^2$ at the KE metric is positive-definite on TT-tensors orthogonal to the KE deformation space. This means local perturbations cannot lower $\int |W^-|^2$ without paying a quadratic penalty. The penalty is controlled by the spectral gap of the Lichnerowicz Laplacian $\Delta_L$ on TT-tensors.

**First calculation.** On the Calabi model, compute the spectrum of $\Delta_L$ restricted to $U(1)$-invariant TT-tensors. The radial ODE system is 2nd order in $\tau$ (3 components for a general TT tensor in the $U(1)$-symmetric setting). If the lowest eigenvalue $\lambda_1(\Delta_L)$ satisfies $\lambda_1 \geq c_0 > 0$ uniformly in $c$ (the cusp-closing parameter), then:
$$\delta^2 \int |W^-|^2 \geq c_0 \|\delta g\|_{L^2}^2$$
This would establish that $W^-$ depletion at rate better than $O(\|\delta g\|^2)$ is impossible, proving retention in the perturbative regime.

**Warning.** The spectral gap might close as $c \to 0$ (approaching the pure cusp), which would mean the argument only works for $r$ bounded. This is still valuable information.

---

## Route 4: Monopole Insensitivity and the $r$-Loss as a Purely Topological Artefact

**Mechanism.** The standard Seiberg–Witten Weitzenböck formula on a 4-manifold:
$$\nabla_A^*\nabla_A \Phi + \frac{s}{4}\Phi + F_A^+ \cdot \Phi = 0$$
involves $s$ and $F_A^+ = \sigma(\Phi)$ but does **not** involve $W^-$ at all. On a Kähler–Einstein surface with $\operatorname{Ric} = -g$:
- $s = -4$ everywhere (same on CH and on the cusp-closing model)
- $W^+$ eigenvalues $= (-2/3, 1/3, 1/3)$ everywhere (Kähler identity)

These are **identical** on CH and on the cusp-closing cap. Therefore:

> The local Seiberg–Witten equations, the amplitude bound $0 \leq \rho \leq 2$, the kinetic identity $K = \frac{1}{2}\int \rho(2-\rho)$, and the scalar budget $S \geq 32\pi^2 p$ are all **independent of whether the background is CH or cusp-closing**.

This means the monopole-based lower theory cannot detect the difference between CH sites and ramification sites through *local* PDE analysis. The $r$-dependence enters only through the *global* Chern–Weil identity:
$$P = \frac{S-S_0}{12} + 4B + 8\pi^2 A\theta_\Delta$$
where $\theta_\Delta = h(3-\sigma)/3$ depends on $\Delta$ (hence $r$) through the topology.

**First object to build.** Prove the statement: *For any metric $g$ on $M_m$ that agrees with $g_{KE}$ on $\bar X_m \setminus (\text{CH-close sites} \cup \text{modification region}\ N)$, with $N$ contained in a ramification neighbourhood, the monopole estimates (scalar budget, amplitude theorem) give the same numerical bounds regardless of what $g$ does on $N$, provided $s_g = s_{KE} = -4$ on $N$.*

This would establish that the $r$-gap in the lower theory is an *artefact of the topological identity*, not of any geometric flexibility: the monopole scalar budget controls total $S$, not its allocation between ramification and surgery regions. The $r$-question then reduces to whether a construction can beat $4h(1-6\theta)$ by exploiting volume reallocation (Step 38's $\Delta_N B = P_N/4 - \Delta_N V/3$), not by exploiting any local curvature advantage.

---

## Route 5: Numerics on the Mixed Cell — Blow-up with Background $W^-$

**Mechanism.** Rather than the perturbative expansion (Route 1), directly solve the Bianchi-IX ODE system for the optimised perpendicular cell on the Calabi background. The Calabi metric at distance $R$ from the divisor has:
$$\Theta(R) = \frac{2}{3}R^2 - \frac{c}{R}, \quad |W^-|^2 = \frac{6c^2}{R^6}$$
For the perpendicular-topology cell with bolt at radius $R_0$, the collar annulus sees background curvature components that differ from CH by $O(c/R_0)$ terms.

**First calculation.** Implement the following in the existing numerical PDE framework:
1. Write the background Calabi metric in the Bianchi-IX coordinates $(a_1, a_2, a_3)$ used for the cell ansatz. The $U(1)$ symmetry of the Calabi model means two of the three scale functions are equal on the collar.
2. Set up the cell ODE with Calabi boundary conditions at radius $R_0$ (instead of pure CH).
3. Optimise the cell parameters $(x_0, \text{degree})$ to minimise $J_6 = D - T^2/(4V)$.
4. Compare the resulting $J_6/(8\pi^2)$ with the certified CH value $0.99567\ldots$

If the optimised value at a ramification site is lower, then the upper bound improves with $r$ and the exact improvement can be read off. If higher, retention holds in the explicit cell family.

**Concrete numbers.** For the cusp-closing model with $e = 1$ (minimal self-intersection), $c = (2/3)\tau_0^3$, and $\tau_0 = 1$, the deviation from CH at distance $\tau_0 + 45 \approx 46$ (the collar radius) is $|W^-|^2 \approx 6/(46)^6 \sim 6 \times 10^{-10}$, which is extremely small. This suggests the second-order cost correction from Route 1 is tiny compared to $\eta_{\rm cert} \approx 0.004$. But for cells placed *very close* to the divisor (overlapping the region where $|W^-| \sim O(1)$), the effect could be substantial.

**Warning.** The cell collar radius in $\operatorname{Ric} = -g$ units is $\sqrt{6}\operatorname{arsinh}\sqrt{128} \approx 7.645$, which corresponds to $\tau \approx e^{7.645/2} \approx 45$ in the Calabi coordinates. At $\tau = 45$, the cusp-closing deviation is exponentially small. Only cells placed within a few units of $\tau_0$ (the divisor) would see substantial $W^-$. Such cells would need a completely different collar matching — they would not be perturbations of the CH cell but fundamentally new objects. This is a much harder construction problem.

---

## Summary: Priority Ordering

| Route | Type | First Object | Value Signal |
|-------|------|-------------|-------------|
| 4 (Monopole insensitivity) | Proof | Theorem: local SW identical on CH and Calabi | Clarifies that $r$-gap is topological |
| 1 (Second-order cost) | Symbolic computation | $\delta^2 D[\kappa,\kappa]$ quadratic form | Sign determines retention/depletion |
| 2 (Weyl interaction) | Symbolic computation | $W^-$ eigenvalues at $\tau_0$ | Geometric mechanism for energy decrease |
| 3 (Spectral gap) | Spectral analysis | $\lambda_1(\Delta_L)$ on Calabi model | Quantitative retention bound |
| 5 (Direct numerics) | Numerical PDE | $J_6$ for Calabi-background cell | Definitive number |

Route 4 should come first because it is a clean theoretical result that reframes the entire problem: if correct, it proves that the $r$-dependence is a global topological effect invisible to local cell optimisation, and redirects effort toward global volume/Weyl exchange rather than local cell improvement. Routes 1 and 2 provide the quantitative content; Route 3 provides the rigorous obstruction; Route 5 is the computational verification.
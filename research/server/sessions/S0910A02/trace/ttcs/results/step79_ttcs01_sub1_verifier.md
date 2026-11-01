# TTCS Independent Branch Record

```json
{
  "step_id": 79,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step79_alignment_closure_and_collapse_transition.md",
    "Sessions/S0910A02/workspace/data/step79_ale_exclusion.json",
    "Sessions/S0910A02/workspace/data/step79_transition_constants_verify.json",
    "Sessions/S0910A02/workspace/notes/step71_collapse_quantum_and_lean_scope.md"
  ]
}
```

## Task

Verify the following two mathematical results for the four-dimensional positive branch of Yau's Problem 26.

RESULT 1 (Transition-Scale Theorem): For a collapsing sequence of closed Riemannian 4-manifolds with Ric >= (n-1)κg (κ > 0) and Vol → 0, define the transition scale ρ_ε(x) = sup{r : Vol(B(x,r))/V_κ(r) >= ε}. Choose p_i maximizing ρ_ε and rescale by ρ_i^{-2}. Then: (a) the rescaled sequence is noncollapsed at unit scale, (b) Euclidean volume ratio ≤ ε at all larger scales, (c) Ric → 0, (d) any pointed GH limit has AVR ≤ ε, (e) if the limit is ALE with group Γ, then |Γ| ≥ 1/ε.

RESULT 2 (ALE Exclusion): For χ = 8, using the Hitchin-Nakajima CGB formula int|W|² = 8π²(χ_top - 1/|Γ|) for ALE resolutions of C²/Γ: the outermost ALE bubble must satisfy rank ≤ 7 (since energy ≤ 64π²). The maximum |Γ| among all ADE groups with rank ≤ 7 is 48 (E_7, energy ≈ 63.83π²). E_8 (|Γ|=120, energy ≈ 71.93π²) exceeds the budget. Therefore for ε < 1/48, NO hyper-Kähler ALE 4-manifold can be the outermost collapse model.

Check: (1) Is the transition-scale proof correct? Pay attention to the volume comparison rescaling and the claim that ρ_i → 0. (2) Is the Hitchin-Nakajima CGB-ALE formula stated correctly? Source-check against the standard literature. (3) Is the ALE exclusion argument complete — are there non-ADE ALE Ricci-flat 4-manifolds that could evade the bound? (4) Does the conclusion correctly follow: outermost model must be ALF/ALG/ALH for ε < 1/48?

## Output

# Scientific verification memo

## 1. Transition-scale construction

### Valid parts: existence of the scale, \(\rho_i\to0\), and volume estimates

Let \(D_\kappa=\pi/\sqrt{\kappa}\). By Bonnet–Myers,
\[
\operatorname{diam}(M_i,g_i)\le D_\kappa.
\]
For large \(i\),
\[
\frac{\operatorname{Vol}(M_i,g_i)}{V_{n,\kappa}(D_\kappa)}<\epsilon,
\]
so every \(\rho_\epsilon(x)\) is finite and lies below \(D_\kappa\).

The function
\[
(x,r)\longmapsto \Theta_i(x,r)
=\frac{\operatorname{Vol}_{g_i}(B(x,r))}{V_{n,\kappa}(r)}
\]
is continuous, including across cut loci because geodesic spheres have zero \(n\)-dimensional volume. Its monotonicity in \(r\) implies that \(\rho_\epsilon(x)\) is upper semicontinuous. Hence a maximizing point \(p_i\) exists on compact \(M_i\).

The proof that \(\rho_i:=\rho_\epsilon(p_i)\to0\) is correct. If \(\rho_i\ge c>0\) along a subsequence, monotonicity gives
\[
\operatorname{Vol}(M_i,g_i)
\ge \operatorname{Vol}(B(p_i,c))
\ge \epsilon V_{n,\kappa}(c)>0,
\]
contrary to \(\operatorname{Vol}(M_i,g_i)\to0\).

Since the transition is finite and \(\Theta_i(p_i,\cdot)\) is continuous,
\[
\Theta_i(p_i,\rho_i)=\epsilon.
\]
Consequently,
\[
\begin{aligned}
\frac{\operatorname{Vol}_{\rho_i^{-2}g_i}
 (B(p_i,R))}{\omega_nR^n}
&\le
\epsilon\,
\frac{V_{n,\kappa}(R\rho_i)}
     {\omega_n(R\rho_i)^n}.
\end{aligned}
\]
For positive \(\kappa\),
\[
V_{n,\kappa}(t)\le \omega_nt^n,
\]
because \(\sin(\sqrt\kappa\,t)/\sqrt\kappa\le t\). Thus one actually obtains the stronger estimate
\[
\frac{\operatorname{Vol}_{\rho_i^{-2}g_i}(B(p_i,R))}
     {\omega_nR^n}
\le\epsilon
\qquad (R\ge1),
\]
rather than merely the displayed \(1+C_n\kappa\rho_i^2R^2\) estimate. At unit scale,
\[
\operatorname{Vol}_{\rho_i^{-2}g_i}(B(p_i,1))
=\epsilon\,\rho_i^{-n}V_{n,\kappa}(\rho_i)
\longrightarrow \epsilon\omega_n.
\]
After discarding finitely many indices, \(\epsilon'=\epsilon/2\) works.

The maximality corollary is also valid at the volume-ratio level: for every \(y\in M_i\) and \(R\ge1\),
\[
R\rho_i\ge \rho_i\ge\rho_\epsilon(y),
\]
and hence the same upper volume estimate holds at \(y\).

### Part (c) does not follow from a Ricci lower bound

Under constant rescaling \(\widetilde g_i=\rho_i^{-2}g_i\), the Ricci tensor as a \((0,2)\)-tensor satisfies
\[
\operatorname{Ric}_{\widetilde g_i}=\operatorname{Ric}_{g_i}.
\]
The given assumption yields only
\[
\operatorname{Ric}_{\widetilde g_i}
\ge (n-1)\kappa\rho_i^2\widetilde g_i.
\]
It provides no upper estimate. In particular, the expression
\[
\operatorname{Ric}_{\widetilde g_i}
=(n-1)\kappa\rho_i^2\widetilde g_i+O(\rho_i^2)
\]
is unsupported.

A concrete counterexample is
\[
(M_i,g_i)=(S^4,t_i^2g_{\rm rd}),\qquad t_i\to0,
\]
where \(g_{\rm rd}\) has sectional curvature \(1\). Then
\[
\operatorname{Ric}_{g_i}
=3g_{\rm rd}
=\frac{3}{t_i^2}g_i
\ge3g_i,
\qquad
\operatorname{Vol}(g_i)\to0.
\]
For fixed \(\epsilon\), the transition scale satisfies \(\rho_i/t_i\to a_\epsilon\in(0,\infty)\) after passage to a subsequence. Therefore
\[
\rho_i^{-2}g_i\longrightarrow a_\epsilon^{-2}g_{\rm rd},
\]
a compact round sphere with Ricci curvature bounded away from zero.

Part (c) becomes correct after adding a uniform two-sided Ricci estimate. For example,
\[
|\operatorname{Ric}_{g_i}|_{g_i}\le\Lambda
\]
implies
\[
|\operatorname{Ric}_{\widetilde g_i}|_{\widetilde g_i}
=\rho_i^2|\operatorname{Ric}_{g_i}|_{g_i}
\le\Lambda\rho_i^2\to0.
\]
The near-Einstein hypothesis
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{g_i}\le\delta_i
\]
gives precisely such an estimate.

### Parts (d) and (e)

Using measured pointed convergence, the Ricci lower estimates and the unit-ball volume lower estimate yield a subsequential noncollapsed RCD\((0,n)\) limit. Volume convergence then gives
\[
\frac{\mathcal H^n(B(p_\infty,R))}{\omega_nR^n}\le\epsilon
\qquad (R\ge1),
\]
and therefore
\[
\operatorname{AVR}(X_\infty)\le\epsilon.
\]
This part does not require Part (c). It produces an RCD\((0,n)\) space, not by itself a Ricci-flat smooth space. The limit can even be compact under the hypotheses as stated, as the shrinking-sphere example illustrates.

If the limit has an ALE end asymptotic to \(\mathbb R^4/\Gamma\), then
\[
\operatorname{AVR}(X_\infty)=\frac1{|\Gamma|},
\]
so
\[
|\Gamma|\ge\frac1\epsilon.
\]
Thus Part (e) is correct as a metric-volume implication.

Bishop–Gromov alone supplies a volume transition, not annular curvature control, smooth convergence, holonomy information, or a curvature-energy identity.

---

## 2. The ALE Chern–Gauss–Bonnet formula

For a smooth, one-ended ALE four-manifold \(X\) asymptotic to \(\mathbb R^4/\Gamma\), the standard ALE Chern–Gauss–Bonnet identity is
\[
\chi(X)
=
\frac1{8\pi^2}\int_X
\left(
|W|^2-\frac12|E|^2+\frac{s^2}{24}
\right)dV
+\frac1{|\Gamma|}.
\]
This agrees with the formula quoted in the supplied `Curvature-cones-and-characteristic-numbers` object and with the normalization used in Step 71.

For Ricci-flat \(X\), \(E=s=0\) and \(Rm=W\), so
\[
\boxed{
\int_X|W|^2\,dV
=
8\pi^2\left(\chi(X)-\frac1{|\Gamma|}\right).
}
\]
Thus the Hitchin–Nakajima formula is stated correctly for a smooth ALE manifold.

For an ALE orbifold with interior singular points of local groups \(\Gamma_j\), the corresponding identity instead contains the orbifold Euler characteristic:
\[
\frac1{8\pi^2}\int_X|W|^2\,dV
=
\chi_{\rm top}(|X|)
-\sum_j\left(1-\frac1{|\Gamma_j|}\right)
-\frac1{|\Gamma_\infty|}
\]
in the Ricci-flat case. Therefore the smooth-resolution formula cannot be applied unchanged to an outer ALE orbifold carrying deeper singular points.

---

## 3. ADE energy arithmetic

The \(64\pi^2\) total energy budget requires more than \(\chi=8\). Under
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{g_i}\to0,
\qquad
\operatorname{Vol}(g_i)\to0,
\]
Chern–Gauss–Bonnet gives
\[
\int_{M_i}|W|^2
=
64\pi^2
+\frac12\int|E|^2
-\frac1{24}\int s^2
\longrightarrow64\pi^2.
\]
A smooth bubble limit, together with curvature-energy semicontinuity on compact exhaustions, then has energy at most \(64\pi^2\). Under only the Ricci lower estimate from Result 1, no such energy upper estimate follows.

For a smooth globally hyper-Kähler ALE space, Kronheimer’s classification gives the minimal resolution of \(\mathbb C^2/\Gamma\), where \(\Gamma\subset SU(2)\) is of ADE type. If \(r\) is the Dynkin rank, then
\[
\chi(X)=r+1.
\]
The energy inequality becomes
\[
r+1-\frac1{|\Gamma|}\le8,
\]
which forces \(r\le7\). The group orders through rank seven are
\[
|A_r|=r+1,\qquad |D_r|=4(r-2),\qquad
|E_6|=24,\qquad |E_7|=48.
\]
Hence the maximum is \(48\), attained by \(E_7\). Its exact energy is
\[
8\pi^2\left(8-\frac1{48}\right)
=\frac{383}{6}\pi^2
\approx63.8333\pi^2.
\]
For \(E_8\),
\[
8\pi^2\left(9-\frac1{120}\right)
=\frac{1079}{15}\pi^2
\approx71.9333\pi^2,
\]
which exceeds \(64\pi^2\). The arithmetic in `step79_ale_exclusion.json` is correct.

Combining \(|\Gamma|\le48\) with
\[
|\Gamma|\ge1/\epsilon
\]
does exclude a smooth Kronheimer ALE transition limit when
\[
\epsilon<\frac1{48}.
\]

### ALE geometries not covered by that calculation

Within complete smooth globally hyper-Kähler ALE four-manifolds, the ADE table is exhaustive. The argument does not cover:

1. Ricci-flat ALE manifolds whose holonomy is not globally hyper-Kähler;
2. finite locally hyper-Kähler quotients for which \(\chi\) and the group at infinity obey a different relation;
3. ALE orbifolds with interior singular points.

The last case is especially concrete. The flat orbifold \(\mathbb C^2/\Gamma\) has zero regular curvature energy and
\[
\operatorname{AVR}=\frac1{|\Gamma|},
\]
with arbitrarily large ADE group order. Its interior orbifold correction cancels the end correction in Chern–Gauss–Bonnet. Such an outer level can carry deeper bubbles, so assigning the full resolution energy to that outer level is not valid.

---

## 4. Consequence for ALF/ALG/ALH models

The conclusion “the outermost model must be ALF, ALG, or ALH” does not follow.

At \(\epsilon<1/48\), the verified conditional conclusion is only:

> A transition limit cannot be a smooth globally hyper-Kähler ALE manifold of Kronheimer type, provided the sequence is near-Einstein, the \(64\pi^2\) energy estimate applies, and the convergence transfers the bubble energy.

Other possibilities include a singular ALE orbifold, a Ricci-flat ALE space with different holonomy, a compact or singular RCD limit under the original one-sided hypothesis, or a non-ALE space with \(0\le\operatorname{AVR}\le\epsilon\). Even \(\operatorname{AVR}=0\) does not by itself yield ALF/ALG/ALH asymptotics; those labels require additional smoothness, finite-energy, decay, holonomy, and end-classification results.

Also, taking \(\epsilon\to0\) changes \(p_i\), \(\rho_i\), and potentially the pointed limit. A diagonal sequence of different transition models does not show that one fixed model has AVR zero.

Finally, `step79_transition_constants_verify.json` records `CW_chiral_limit_pi2: 64`, whereas for \(\chi=8,\tau=0\) each chirality tends to \(32\pi^2\). The total \(W\)-energy is \(64\pi^2\); the consistent per-chirality value is \(32\pi^2\).
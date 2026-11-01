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

The strongest new direction is to stop treating the remaining geometry as generic Ricci collapse. A surviving sequence must be a **collapsed sequence with almost calibrated Chern–Weil density**, not merely controlled \(L^2\) curvature. That extra algebraic/topological input is much sharper than the Taub–NUT–AdS countermodel.

## 1. Calibrated \(p_1(\Lambda^2_+)\) density forces non-basic curvature on most volume

Let \(A_i^+\) be the Levi–Civita \(SO(3)\)-connection on \(\Lambda^2_+\), with curvature \(\Omega_i^+\). In four dimensions,

\[
\operatorname{tr}(\Omega_i^+\wedge \Omega_i^+)
=
\gamma\left(
\left|W_i^+ + \frac{s_i}{12}I\right|^2
-\left|B_i\right|^2
\right)d\mu_i ,
\]

where \(B_i\) is the trace-free Ricci off-block and \(\gamma\) is the fixed normalization constant. Since \(\operatorname{Ric}_{g_i}+g_i\to0\),

\[
B_i=o(1).
\]

On the calibrated set,

\[
s_i\to -4,\qquad 
\operatorname{Spec}(W_i^+)\to\left(-\frac16,\frac1{12},\frac1{12}\right),
\]

hence

\[
\left|W_i^+ + \frac{s_i}{12}I\right|^2
\to
\left(-\frac12\right)^2+2\left(-\frac14\right)^2
=
\frac38 .
\]

Thus, in the connection norm,

\[
\operatorname{tr}(\Omega_i^+\wedge\Omega_i^+)
=
\gamma\frac38\,d\mu_i+o(d\mu_i)
\]

on the \(F_i\)-small region. In the topological normalization used in the prompt,

\[
\int_M p_1(\Lambda^2_+)
=
4\pi^2(A-k)
\sim \frac{8}{3}\pi^2A,
\]

while

\[
\operatorname{Vol}(M_i,g_i)
\sim \frac{32}{9}\pi^2A,
\]

so the average \(p_1^+\)-density tends to \(3/4\) in that normalization. This is not a small topological residue; it is an order-one density spread through the calibrated volume.

Now suppose a collapsed regular region has base dimension \(\le3\), with vertical distribution \(V\). Decompose

\[
\Omega_i^+=\Omega_{H,i}^+ + \Omega_{\mathrm{mix},i}^+,
\]

where \(\Omega_{H,i}^+\) has only horizontal legs and \(\Omega_{\mathrm{mix},i}^+\) has at least one vertical leg. Since a horizontal \(4\)-form vanishes over a base of dimension \(\le3\),

\[
\operatorname{tr}(\Omega_{H,i}^+\wedge\Omega_{H,i}^+)=0.
\]

Therefore

\[
\left|\operatorname{tr}(\Omega_i^+\wedge\Omega_i^+)\right|
\le
C\left(
|\Omega_{H,i}^+|\,|\Omega_{\mathrm{mix},i}^+|
+
|\Omega_{\mathrm{mix},i}^+|^2
\right)d\mu_i .
\]

On regions where \(|\Omega_i^+|\le L\) and \(F_i\) is small, the calibrated \(p_1^+\)-density gives

\[
|\Omega_{\mathrm{mix},i}^+|
\ge c(L)>0
\]

on a large subregion. Integrated form:

\[
\int_U |\Omega_{\mathrm{mix},i}^+|^2\,d\mu_i
\ge
c(L)\operatorname{Vol}(U)-o(\operatorname{Vol}(U)).
\]

So the \(p_1^+\) budget does give a quantitative lower volume statement, but for **non-basic curvature**, not necessarily for high curvature. High-curvature localization alone is too crude; the calibrated charge can be carried by \(O(1)\)-curvature mixed vertical-horizontal connection curvature throughout a collapsed region.

A useful sharpened statement is:

\[
\operatorname{Vol}
\left\{
F_i\le \varepsilon,\ |\Omega_i^+|\le L,\ 
|\Omega_{\mathrm{mix},i}^+|\le \eta
\right\}
\le
C(L)\left(\varepsilon+\eta\right)\operatorname{Vol}(M_i)+o(A).
\]

This would turn Pontryagin localization into a direct exclusion of genuinely basic collapse on most volume.

High-curvature \(p_1^+\) concentration is also strongly restricted by \(F_i\). If \(|W_i^+|\gg1\), then

\[
F_i\ge \left(s_i+8\sqrt6\,|W_i^+|\right)^2
\gtrsim |W_i^+|^2,
\]

so an \(O(A)\) amount of \(p_1^+\) carried by large \(W^+\) spikes would force \(\int F_i\gtrsim A\), incompatible with \(\int F_i=o(A)\). Thus \(p_1^+\) cannot hide mainly in \(W^+\)-bubbles. By contrast, anti-self-dual Ricci-flat bubbles with \(W^+=0\) cost essentially no \(F_i\), but they carry \(p_1(\Lambda^2_-)\), not \(p_1(\Lambda^2_+)\).

## 2. Rank-one collapse as a 3D Chern–Simons–Higgs system

On a regular rank-one collapsed region, write

\[
g_i \approx h_i + \ell_i^2\theta_i^2,\qquad \ell_i\to0,
\]

and set \(e_i^0=\ell_i\theta_i\). In a local gauge for \(\Lambda^2_+\),

\[
A_i^+ = a_i + \phi_i e_i^0,
\]

where \(a_i\) is the horizontal \(SO(3)\)-connection and \(\phi_i\) is an \(so(3)\)-valued Higgs field measuring connection rotation in the collapsing direction. Then

\[
\Omega_i^+
=
F_{a_i}
+
(D_{a_i}\phi_i)\wedge e_i^0
+
\phi_i\,de_i^0
+
\text{vertical-variation terms}.
\]

Since \(F_{a_i}\wedge F_{a_i}=0\) over a \(3\)-dimensional base,

\[
\operatorname{tr}(\Omega_i^+\wedge\Omega_i^+)
=
2e_i^0\wedge
\operatorname{tr}
\left(
F_{a_i}\wedge D_{a_i}\phi_i
+
F_{a_i}\wedge \phi_i\,\iota_{e_i^0}de_i^0
+\cdots
\right).
\]

Thus \(p_1^+\) becomes a **3D flux density**: base curvature paired with Higgs variation and fiber twisting. If \(\phi_i\) is covariantly constant and the fiber twist is basic-trivial, \(p_1^+\) vanishes. The calibrated density forces one of

\[
D_{a_i}\phi_i,\qquad \phi_i\,\iota_{e_i^0}de_i^0,\qquad \text{vertical variation}
\]

to be order one on most calibrated volume.

For contractible fibers, the small circle holonomy satisfies

\[
\operatorname{Hol}_{\psi}(A_i^+)
=
\exp\!\left(\int_{\psi}A_i^+\right)
=
\exp\!\left(O(\ell_i)\right)\to I,
\]

but this does **not** force \(\phi_i\to0\); it only says the coordinate integral around the shrinking orbit vanishes. Hence Taub–NUT-type collapse can still carry \(O(1)\) Higgs curvature.

The closed-manifold content enters after fiber integration:

\[
\pi_*\operatorname{tr}(\Omega_i^+\wedge\Omega_i^+)
=
d_B\,\mathcal{CS}(a_i,\phi_i,\theta_i)
+
\mathcal E_i,
\]

where \(\mathcal E_i\) records non-invariance and transition terms. Over a closed regular circle bundle this integrates to zero. Therefore \(p_1^+\sim A\) must be sourced by links around NUT-type loci, nil-twisted regions, transition walls, or places where the rank-one description changes.

This converts rank-one collapse into a Yang–Mills–Higgs monopole problem over a \(3\)-dimensional base. The decisive calculation is the local charge/energy table for a contractible-fiber end:

\[
\left(
\int p_1^+,\ 
\int F_i,\ 
\int |\Omega_{\mathrm{mix}}^+|^2,\ 
\text{fiber holonomy residue}
\right).
\]

If every smooth contractible-fiber Einstein end has

\[
\fint_{\text{annulus}}F_i\ge \varepsilon_0>0,
\]

then \(O(A)\) such ends contradict \(\int F_i=o(A)\). If some end has annular \(F_i\to0\), that end is the surviving local model and should satisfy the calibrated Higgs equations above.

The immediate source family to compute is:

- Taub–NUT–AdS with the formula supplied by S0910A03;
- Pedersen-type self-dual Einstein metrics;
- Calderbank–Pedersen toric self-dual Einstein metrics;
- Bianchi IX Einstein metrics with NUT/bolt behavior;
- complex-hyperbolic and real-hyperbolic cusp normalizations.

For each, compute

\[
|W^+|^2,\qquad \operatorname{tr}((W^+)^3),\qquad F,\qquad p_1^+\text{ density}.
\]

The known real and complex hyperbolic cusps have large \(F\)-density, so they cannot occupy most near-saturating volume. Taub–NUT–AdS currently only shows that mean curvature control does not produce cover noncollapse; its compatibility with \(F_i\to0\) is a separate curvature-spectrum computation.

## 3. The saturated monopole class gives a rank-one reduced form system

Near equality in LeBrun’s Seiberg–Witten inequality supplies a harmonic self-dual form \(\omega_i\) aligned with the simple \(W_i^+\)-eigenline and with almost constant amplitude. On a rank-one collapsed region,

\[
\omega_i
=
e_i^0\wedge \beta_i
+
*_{h_i}\beta_i
+
o(1),
\]

where \(\beta_i\) is a base \(1\)-form. Since \(d\omega_i=0\), writing \(u_i=\log\ell_i\),

\[
d_{B}\beta_i
=
du_i\wedge\beta_i
+
o(1),
\]

and

\[
d_B(*_{h_i}\beta_i)
+
e^{u_i}d\theta_i\wedge\beta_i
=
o(1).
\]

Equivalently,

\[
d_B(e^{-u_i}\beta_i)=o(1).
\]

Thus the saturated monopole form makes the eigenline almost hypersurface-orthogonal on the \(3\)-dimensional base. Meanwhile the Weitzenböck calculation says

\[
\int |\nabla\omega_i|^2
\sim
\int |\omega_i|^2,
\]

so the base form \(\beta_i\) must rotate at order-one rate.

This gives a rank-one overdetermined system:

\[
\begin{cases}
\operatorname{Ric}_{g_i}+g_i\to0,\\
F_i\to0,\\
\omega_i=e_i^0\wedge\beta_i+*_{h_i}\beta_i+o(1),\\
d_B(e^{-u_i}\beta_i)\to0,\\
\operatorname{Spec}(W_i^+)\to(-1/6,1/12,1/12).
\end{cases}
\]

A plausible rank-one exclusion theorem would say that no punctured \(3\)-dimensional base carrying a NUT residue solves this system with \(|\beta_i|\) bounded away from zero and calibrated \(p_1^+\)-density.

The concrete calculation is to insert the Kaluza–Klein curvature formulas into the two scalar Weyl invariants

\[
|W^+|^2=\frac1{24},
\qquad
\operatorname{tr}((W^+)^3)
=
\left(-\frac16\right)^3
+
2\left(\frac1{12}\right)^3,
\]

together with the reduced Einstein equations. The double eigenvalue of \(W^+\) should force transverse isotropy in the base variables. Combined with \(d(e^{-u}\beta)=0\), this may reduce the local model to an ODE. Smooth NUT residues can then be tested directly.

## 4. Seiberg–Witten near equality gives a strong cohomological ledger

Let \(K\) denote the canonical-type class with \(K^2=A\), and let \(E_1,\dots,E_k\) be the blow-up classes. The monopole classes include

\[
a_{\varepsilon}
=
K+\sum_{j=1}^{k}\varepsilon_jE_j,
\qquad
\varepsilon_j=\pm1.
\]

For any metric,

\[
\max_{\varepsilon}
\left|(a_{\varepsilon})^+\right|^2
\ge
\mathbb E_{\varepsilon}
\left|K^+ + \sum_j\varepsilon_jE_j^+\right|^2
=
|K^+|^2+\sum_j|E_j^+|^2.
\]

Also

\[
|K^+|^2\ge K^2=A.
\]

Near equality in the LeBrun curvature chain at \(k/A\to1/3\) gives

\[
\max_{\varepsilon}
\left|(a_{\varepsilon})^+\right|^2
\le
A+o(A).
\]

Therefore

\[
|K^-|^2=o(A),
\qquad
\sum_{j=1}^{k}|E_j^+|^2=o(A).
\]

This is a major closed-manifold constraint:

1. The canonical class is almost self-dual.
2. The blow-up classes are almost anti-self-dual in aggregate.
3. The many sign choices of monopole classes do not create many independent calibrated self-dual forms; the near-saturating self-dual geometry is essentially the canonical direction.
4. The exceptional topology must be carried by the \(W^-\)/anti-self-dual sector, by small-scale bubbles, or by collapsed topology invisible to \(p_1^+\).

This interacts strongly with high-curvature analysis. A blow-up at curvature scale \(r_i\to0\) has Ricci tending to zero after rescaling. If its \(F_i\)-energy tends to zero, then in the chosen orientation the bubble must have

\[
W^+=0,
\]

so it is an anti-self-dual Ricci-flat gravitational instanton. Such bubbles can carry \(p_1(\Lambda^2_-)\) and \(W^-\)-energy without contributing \(p_1(\Lambda^2_+)\). They cannot account for the calibrated \(p_1^+\sim A\).

Thus the topology separates into two ledgers:

\[
p_1^+ \sim A
\quad\text{must live in calibrated collapsed background volume,}
\]

while

\[
p_1^-,\ W^- \text{ energy, and exceptional classes}
\]

may live partly in anti-self-dual bubble trees.

This suggests a lattice problem: Ricci-flat anti-self-dual ALE bubbles have intersection lattices of ADE type in the classical hyperkähler cases, whereas the blow-up summands supply an opposite-sign diagonal lattice generated by the \(E_j\). A near-critical sequence would need to embed the diagonal exceptional lattice into a combination of ALE root lattices plus background cycles while maintaining

\[
\sum_j |E_j^+|^2=o(A).
\]

If that lattice decomposition is impossible for a chosen Ishida–LeBrun family, the collapsed sequence cannot exist. If it is possible, the surviving geometry is much more specific: calibrated collapsed background carrying \(p_1^+\), plus anti-self-dual bubble trees carrying exceptional topology.

## 5. Eigenline rotation as a 3D holonomy-charge problem

Let \(P_i\) be the rank-one projector onto the simple \(W_i^+\)-eigenline. Since the eigenvalues are separated,

\[
\nabla W_i^+
\approx
(\text{eigenvalue gap})\,\nabla P_i.
\]

The Weitzenböck calculation gives order-one rotation:

\[
\fint |\nabla P_i|^2 \sim c_0>0.
\]

In rank-one collapse, vertical holonomy around the shrinking fiber tends to the identity, so the rotation is horizontal. Thus \(P_i\) descends to an approximate map

\[
n_i:B_i^3\to S^2
\]

with

\[
\int_{B_i}\ell_i|\nabla n_i|^2\,d\mu_{B_i}
\sim
\operatorname{Vol}(M_i).
\]

The \(SO(3)\)-connection \(A_i^+\), the Higgs field \(\phi_i\), and the eigenline \(n_i\) should satisfy a Chern–Simons identity of the schematic form

\[
p_1(\Lambda^2_+)
=
e_i^0\wedge
\left[
\langle F_{a_i},D_{a_i}\phi_i\rangle
+
\langle F_{a_i},\phi_i\,\kappa_i\rangle
+
\langle D_{a_i}n_i\wedge D_{a_i}n_i,\phi_i\rangle
+\cdots
\right],
\]

where \(\kappa_i\) encodes fiber twisting. This is analogous to a \(3\)-dimensional monopole/Hopf charge density.

Contractible fibers impose trivial meridian holonomy, so any large charge must come from Higgs winding, base rotation of \(n_i\), or singular residues. The energy available for this is not arbitrary: it is fixed by the Weitzenböck identity and by the Noether \(L^2\)-curvature budget. A sharp inequality of the form

\[
\int_{B_i}\ell_i
\left(
|D\phi_i|^2+|F_{a_i}|^2+|\nabla n_i|^2
\right)
\ge
C\left|\int_{M_i}p_1(\Lambda^2_+)\right|
\]

would be scale-matched: both sides are \(O(A)\). The decisive part is the equality system. If equality forces a smooth noncollapsed Einstein germ or a global Hamiltonian circle geometry, rank-one collapse is eliminated. If equality admits a NUT residue, that residue becomes the exact local survivor.

## 6. Symplectic/Hamiltonian obstruction to all-volume contractible circle collapse

The saturated monopole form is closed, self-dual, and almost constant in norm. On most calibrated volume it behaves as a symplectic form compatible with the metric.

For a local collapsing circle generated by a coordinate vector \(X_i\) of length \(\ell_i\),

\[
\iota_{X_i}\omega_i
=
\ell_i\,\beta_i+o(\ell_i).
\]

Since \(d\omega_i=0\),

\[
d(\iota_{X_i}\omega_i)
=
\mathcal L_{X_i}\omega_i.
\]

If the collapse has approximate local symmetry, then \(\mathcal L_{X_i}\omega_i\) is small and

\[
\iota_{X_i}\omega_i\approx dH_i.
\]

Thus contractible circle collapse in the saturated monopole geometry resembles a Hamiltonian circle action with NUT centers as fixed points.

A global version would be very restrictive: compact symplectic \(4\)-manifolds with Hamiltonian \(S^1\)-actions are classified by moment graphs and are rational or ruled in the standard classification theory. General-type Ishida–LeBrun pieces are not of that type. Therefore an all-volume rank-zero collapse would need to avoid becoming a global Hamiltonian circle geometry by inserting transition walls, nil-twisted pieces, or dense singular residues. Those insertions carry Chern–Simons and eigenline-rotation energy, hence can be measured by the \(p_1^+\) and Weitzenböck ledgers.

If a Hamiltonian model is close enough, ABBV localization gives explicit fixed-point contributions:

\[
\int c_1(J)^2
=
\sum_p
\frac{(m_p+n_p)^2}{m_pn_p},
\]

with \((m_p,n_p)\) the isotropy weights. Since the almost-complex structure induced by the self-dual form has

\[
c_1(J)^2=2\chi+3\tau=A-k,
\]

the fixed-point graph would have to reproduce the critical value \(A-k\sim 2A/3\), together with \(\chi\) and \(\tau\). This provides a discrete topological model for NUT foam. Either the graph is incompatible with the Ishida–LeBrun topology, or it identifies exactly how many NUT centers and which weights are required.

## 7. \(W^-\), signature, and the cell-charge cone

The calibrated defect \(F_i\) controls \(W^+\) and Ricci, not \(W^-\). Signature gives

\[
12\pi^2\tau(M_i)
=
\int(|W_i^+|^2-|W_i^-|^2)\,d\mu_i,
\]

so

\[
\int |W_i^-|^2
=
\int |W_i^+|^2
-
12\pi^2\tau(M_i).
\]

Equivalently,

\[
p_1(\Lambda^2_+)=2\chi+3\tau=A-k,
\]

while

\[
p_1(\Lambda^2_-)=2\chi-3\tau
=
4\chi-(A-k).
\]

Thus \(p_1^+\) and \(p_1^-\) should be tracked separately.

Candidate geometric cells have charge vectors

\[
\mathcal Q
=
\left(
\operatorname{Vol},\
p_1^+,\
p_1^-,\
\int F,\
\int|\mathcal R|^2,\
\int|\nabla P|^2
\right).
\]

Known model behavior:

- Real hyperbolic cusp: \(W^+=0\), large \(F\)-density.
- Complex hyperbolic cusp: Kähler–Einstein, \(|W^+|^2=2/3\), large \(F\)-density.
- Anti-self-dual Ricci-flat bubble: \(F=0\), \(p_1^+=0\), contributes to \(p_1^-\) and \(W^-\).
- Calibrated collapsed background, if it exists: \(F\to0\), \(p_1^+/\operatorname{Vol}\to\rho_0\), no fixed-scale noncollapsed normal cover.

The global Ishida–LeBrun vector must be assembled from these cell vectors. Since \(\int F_i=o(A)\), cells with \(F/\operatorname{Vol}\ge c>0\) cannot occupy \(O(A)\) volume. Since \(p_1^+\sim A\), anti-self-dual bubbles alone cannot account for the topology. Therefore the essential surviving object is sharply identified:

\[
\boxed{
\text{a fixed-volume-ratio collapsed background with }
F_i\to0,\quad
p_1^+\text{ density }\rho_0,\quad
\text{and no fixed-scale noncollapsed normal cover.}
}
\]

That object is far more special than Taub–NUT–AdS. It must satisfy the calibrated Weyl spectrum, the rank-one Chern–Simons–Higgs flux equations, the saturated monopole form equations, and the closed-manifold \(p_1^+\) ledger simultaneously.

## Most promising synthesis

The highest-value route is a combined theorem with three inputs:

1. **Calibrated Chern–Weil density:**  
   \(F_i\to0\) forces \(p_1^+\) density to be order one on most volume.

2. **Rank-one reduction:**  
   In collapsed rank-one geometry, \(p_1^+\) becomes a \(3\)-dimensional Chern–Simons–Higgs flux sourced by Higgs variation, fiber twist, eigenline rotation, or singular residues.

3. **Saturated monopole form:**  
   The aligned harmonic self-dual form reduces to  
   \[
   \omega=e^0\wedge\beta+*_B\beta,\qquad d(e^{-u}\beta)\approx0,
   \]
   while Weitzenböck forces order-one base rotation.

The resulting reduced system is overdetermined. The key local calculation is:

\[
\operatorname{Ric}+g=0,\qquad
F=0,\qquad
d(e^{-u}\beta)=0,\qquad
p_1^+\text{ density }=\rho_0
\]

for a rank-one collapsed Einstein/Higgs model with a contractible-fiber NUT residue. If no such model exists, the entire collapsed near-critical sequence is excluded. If such a model exists, it is the precise geometric survivor: a calibrated NUT/Higgs foam carrying \(p_1^+\) through mixed vertical-horizontal \(\Lambda^2_+\)-curvature, with \(W^-\) and exceptional classes possibly carried by anti-self-dual bubble trees.
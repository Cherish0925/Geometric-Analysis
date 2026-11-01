# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/notes/step65_cell_exceptional_flux_ledger.md",
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md"
  ]
}
```

## Task

Context: the unrestricted Einstein-defect problem α(M)=inf∫|Ric°|² on M=X#kCP̄² (X minimal general type, A=c₁²(X), open range 0<k<A/3 where LeBrun's SW bound is vacuous). Step 65 proved a metric-only exceptional flux ledger p=(1−δ)²/‖h‖²+L (δ = exceptional Ricci-flux deficit, L ≥ 0 misalignment). Step 66 showed (on the constant-scalar slice, which is WLOG) that L splits as L_rank+L_amp; L_rank=0 is exactly the Riemannian Einstein–Maxwell system with F⁻ ∝ the exceptional harmonic ASD form ĥ_a; L=0 is the subclass with |F⁺| constant = AK metrics with J-invariant Ricci (Blair–Ianus class), joining cscK (δ=0, p=|a⁻|²≥k) to Einstein (δ=1, p=0). The near-equality Bianchi estimate gives no coercivity. Generate the strongest scientifically serious ideas for what new information could decide the open range, now that the problem is organized by Einstein–Maxwell theory: (i) Seiberg–Witten curvature estimates adapted to Einstein–Maxwell metrics or to metrics near the EM layer (what inequality, which class, which weight), and whether they would give a k-threshold or a k²/A law; (ii) whether the Blair–Ianus variational characterization (critical points of ∫s on ω-compatible metrics) plus Taubes' symplectic SW theory constrains the strictly-AK members with [ρ₀]∥a⁻ and δ near 1 (e.g. via c₁·[ω], Hermitian scalar curvature integrals, the exceptional (−1)-spheres being symplectic); (iii) a construction route: conformally Kähler or other EM metrics on general-type blow-ups with small L_amp and δ bounded away from 0, or an argument they cannot exist; (iv) a quantitative formulation that is genuinely weaker than Einstein nonexistence but still gives a tariff for metrics near the Kähler end (δ ≤ δ₀). For each idea give the exact inequality or construction, why it might work, the decisive first computation, and what would falsify it. Do not invent literature; name precise knowledge requests where needed.

## Output

The Einstein–Maxwell organization makes the decisive unknown much sharper: low Einstein defect forces the tracefree Ricci tensor to lie near a harmonic Maxwell field whose anti-self-dual part is the exceptional harmonic representative. The open range can therefore be decided by one of four mechanisms: a Seiberg–Witten price for the self-dual Maxwell part, a symplectic-cohomological obstruction to the strictly almost-Kähler equality class, an explicit Einstein–Maxwell construction, or a local coercivity theorem near the Kähler end. Below are the strongest forms of these possibilities.

---

## 1. A Seiberg–Witten/Weyl estimate adapted to the Einstein–Maxwell layer

### 1.1 The coupled Weyl-susceptibility inequality

In the coordinates of Step 62,

\[
\kappa[g]=\frac A2-\frac{3}{8\pi^2}\int_M |W^+_g|^2\,d\mu_g,
\qquad
p[g]=\frac{1}{8\pi^2}\int_M |\operatorname{Ric}^\circ_g|^2\,d\mu_g .
\]

The open-range lower bound is controlled by how large \(\kappa\) may become relative to \(p\). The formal common mode saturates

\[
\kappa \approx k,
\qquad
p \approx \frac{k^2}{4A}.
\]

Thus the decisive Einstein–Maxwell-compatible Seiberg–Witten statement would be:

\[
\boxed{
\kappa[g]\le k+\beta\,p[g]+C\sqrt{L_{\mathrm{rank}}[g]}
}
\tag{1.1}
\]

for metrics on the \(s=-4\) Yamabe slice, with \(\beta\) an absolute or topology-controlled constant and \(L_{\mathrm{rank}}\) the rank-misalignment part of the Step 66 ledger. On the exact Einstein–Maxwell layer \(L_{\mathrm{rank}}=0\), this becomes

\[
\boxed{
\kappa[g]\le k+\beta\,p[g].
}
\tag{1.2}
\]

Equivalently,

\[
\boxed{
\int_M |W^+_g|^2\,d\mu_g
\ge
\frac{4\pi^2}{3}(A-2k)-\frac{8\pi^2\beta}{3}p[g].
}
\tag{1.3}
\]

This is the natural Einstein–Maxwell refinement of LeBrun’s curvature estimate: each exceptional class can remove at most one unit of Weyl capacity for free; any additional Weyl deficit must be paid by Einstein defect.

By Corollary 62.C, if (1.2) holds with finite \(\beta\), then

\[
\boxed{
\frac{\alpha(M)}{8\pi^2}
\ge
\frac{k^2}{(4+4\beta)A}\bigl(1+O(k/A)\bigr).
}
\tag{1.4}
\]

Thus (1.2) gives the sharp \(k^2/A\) scale when \(\beta=O(1)\). If a stronger per-class estimate holds,

\[
\kappa[g]\le (1-\eta)k+\beta p[g],
\tag{1.5}
\]

then one obtains a genuine per-class tariff rather than only the \(k^2/A\) law.

### 1.2 Why this is the correct Seiberg–Witten target

The usual Seiberg–Witten estimates see the monopole class through \((a^+)^2\) and produce lower bounds on Yamabe excess. They do not directly bound \(\kappa\). The Einstein–Maxwell layer supplies the missing structure:

- the anti-self-dual Maxwell part is fixed to be the exceptional harmonic representative \(h_a^-\);
- the self-dual Maxwell part \(\varphi\) is the only object capable of carrying additional Weyl deficit;
- the Bianchi identity couples \(\varphi\) to \(\operatorname{Ric}^\circ\);
- the ledger prices \(\varphi\) through \(L_{\mathrm{amp}}\).

A Seiberg–Witten estimate adapted to this layer should therefore be written not merely as a scalar-curvature estimate but as a Weyl-curvature estimate weighted by the Maxwell field. One natural form is:

\[
\boxed{
\frac{3}{8\pi^2}\int_M |W^+|^2
\ge
\frac A2-k
-\frac{3}{8\pi^2}\int_M \mathcal{Q}_h(\varphi)
}
\tag{1.6}
\]

where \(\mathcal{Q}_h(\varphi)\) is a quadratic expression in the self-dual Maxwell part, comparable to the weighted norm

\[
\int_M |\varphi|^2 |h_a^-|^2\,d\mu_g,
\]

which is exactly the norm appearing in \(L_{\mathrm{amp}}\) and in \(p\) on the rank-one layer.

The desired conclusion is that the extra Weyl deficit beyond \(k\) is controlled by the Maxwell amplitude, and the Maxwell amplitude is itself controlled by \(p\). This converts (1.6) into (1.2).

### 1.3 Decisive first computation

Compute the optimal constant

\[
\beta_{\min}
=
\sup_{\text{known EM/near-EM metrics}}
\frac{\kappa-k}{p}
\]

on:

1. the certified perpendicular cells;
2. the formal common mode;
3. local blow-up deformations of a constant-scalar Kähler metric;
4. any known conformally Kähler Einstein–Maxwell model.

The certified cells have \(\kappa<k\) per class, so they are harmless. The formal common mode has \(\kappa=k+O(k^3/A^2)\) and \(p=O(k^2/A)\), so it is compatible with \(\beta=0\) to leading order. The decisive new calculation is the Hessian of

\[
\kappa-k-\beta p
\]

at the Kähler blow-up metric, restricted to the exceptional deformation directions. If the Hessian is bounded above for some finite \(\beta\), then (1.2) is plausible. If one finds a deformation direction along which

\[
\kappa-k \gg p,
\]

then the \(k^2/A\) law from this route is refuted.

### 1.4 Knowledge requests

- LeBrun’s equality analysis for the scalar/Weyl estimate, especially the structure when equality is approached by almost-Kähler metrics.
- Seiberg–Witten curvature estimates with prescribed anti-self-dual harmonic curvature or with self-dual perturbations.
- Weitzenböck formulas for \(W^+\) on Einstein–Maxwell four-manifolds, including the Maxwell source term.
- Gursky-type per-exceptional-class Weyl estimates in the \(Y<0\) regime, if they exist.

---

## 2. Blair–Ianus variational structure plus Taubes symplectic constraints

The equality class with \(L=0\) and \(\delta\in(0,1)\) consists of constant-\(s\) almost-Kähler metrics with \(J\)-invariant Ricci tensor and primitive Ricci class proportional to the exceptional class. These are precisely the compact Blair–Ianus objects in the \(s<0\) regime. The most direct way to eliminate the dangerous \(\delta\approx1\) members is to use the fact that their Kähler forms are symplectic.

### 2.1 Cohomological consequence of \(\delta\to1\)

Let \((g,J,\Omega)\) be such an almost-Kähler structure, with \(s=-4\). Write

\[
\rho = \frac{s}{4}\Omega+\rho_0,
\]

where \(\rho_0\) is primitive and, in the equality class, harmonic anti-self-dual. Since \(\rho\) represents \(2\pi c_1(J)\),

\[
2\pi b^- = \frac{s}{4}H^-(\Omega)+\rho_0,
\qquad b=c_1(J).
\]

With \(s=-4\), this says, up to the Step-66 sign convention for \(t^-\),

\[
2\pi b^- = -H^-(\Omega)+\rho_0.
\]

Pairing with the normalized exceptional harmonic form \(\hat h\) gives

\[
2\pi\langle b^-,\hat h\rangle
=
-D+F,
\]

where

\[
D=\langle t^-,\hat h\rangle,
\qquad
F=\langle \rho_0,\hat h\rangle,
\qquad
\Phi_b=F+D.
\]

The invariant content is:

\[
\delta_b=\frac{D}{\Phi_b}\to1
\quad\Longrightarrow\quad
F\to0
\quad\text{and}\quad
H^-(\Omega)\text{ carries almost all of }2\pi b^-.
\]

Thus a strictly almost-Kähler equality metric with \(\delta_b\approx1\) would have a symplectic class whose anti-self-dual harmonic projection is almost the full exceptional Chern class, while its primitive Ricci flux almost vanishes.

### 2.2 Taubes symplectic cone feasibility problem

Let

\[
\xi=[\Omega]\in H^2(M;\mathbb{R}).
\]

For a symplectic form on \(X\#k\overline{\mathbb{CP}}^{\,2}\), Taubes’ symplectic Seiberg–Witten theory and the Li–Liu cone description impose:

1. \(\xi^2>0\).
2. \(K_J\cdot \xi>0\), where \(K_J=-c_1(J)\). Since \(s<0\), this is also forced by
   \[
   c_1(J)\cdot\xi=\frac{s}{4\pi}\operatorname{Vol}<0.
   \]
3. \(\xi\cdot C>0\) for every Taubes exceptional curve class \(C\), in particular the relevant \((-1)\)-sphere classes.
4. The anti-self-dual harmonic projection of \(\xi\) must satisfy the flux relation above:
   \[
   \langle H^-(\xi),\hat h\rangle
   =
   2\pi\Phi_b(1-\delta_b)
   \quad\text{or the corresponding sign variant}.
   \]

This gives a finite-dimensional quadratic/linear feasibility problem:

\[
\boxed{
\text{Maximize }\delta_b
\text{ over }\xi\in H^2(M;\mathbb{R})
\text{ satisfying the symplectic cone constraints and the flux projection.}
}
\tag{2.1}
\]

If the maximum satisfies

\[
\delta_b\le 1-\eta
\]

for some \(\eta>0\), then the dangerous Blair–Ianus equality metrics are cohomologically excluded. If \(\delta_b\to1\) is possible only when some exceptional area \(\xi\cdot E_i\to0\), then Taubes curve compactness would still exclude a smooth compact member.

### 2.3 Why this could work

The exceptional sign class \(b\) contains the components

\[
b^- \sim K_X^-+\sum_i \varepsilon_i E_i^-.
\]

If \(H^-(\xi)\) is forced to be close to \(2\pi b^-\), then positivity of \(\xi\) on the exceptional curve classes becomes a strong condition. When the exceptional periods \(E_i^+\) are small, as required for a cheap state by Step 62, the anti-self-dual part alone tends to make some \(\xi\cdot E_i\) too small or of the wrong sign. To compensate, the self-dual part of \(\xi\) must be large, increasing volume and Weyl energy. This may either exclude \(\delta_b\approx1\) or force enough Weyl/Yamabe cost to restore a lower bound on \(p\).

### 2.4 Decisive first computation

For fixed \(A\), \(k\), and a sign vector \(\varepsilon\), solve the quadratic program:

\[
\begin{aligned}
&\text{maximize } \delta \\
&\text{subject to } \xi^2>0,\\
&\qquad K_\varepsilon\cdot\xi>0,\\
&\qquad \xi\cdot E_i>0,\\
&\qquad \langle H^-(\xi),\hat h_\varepsilon\rangle
=2\pi\Phi_\varepsilon(1-\delta),
\end{aligned}
\]

using the known generators of the symplectic cone for minimal general-type blow-ups. This computation uses only intersection data and harmonic projections.

### 2.5 What would refute it

An explicit cohomology class \(\xi\) satisfying all Taubes cone conditions and having \(\delta_b\) arbitrarily close to \(1\) would refute the cohomological exclusion. A stronger refutation would be a construction of a symplectic form in that class together with a compatible almost-complex structure satisfying \(J\)-invariant Ricci. If such objects exist, the Blair–Ianus class remains live.

### 2.6 Blair–Ianus second variation

The Blair–Ianus characterization says that these metrics are critical points of the Hilbert functional

\[
\mathcal{H}(J)=\int_M s_J\,d\mu_J
\]

among metrics compatible with a fixed symplectic form \(\Omega\). In the \(J\)-invariant Ricci class, \(\rho\) is closed and represents \(2\pi c_1(J)\), so

\[
\int_M s\,d\mu = 4\pi c_1(J)\cdot[\Omega].
\]

Thus, for fixed \([\Omega]\) and fixed \(c_1(J)\), the first-order information is nearly topological. The decisive object is the second variation.

A concrete target identity is:

\[
\boxed{
\delta^2\mathcal{H}
=
\int_M
\Bigl(
(-s)|\dot\Omega|^2
+
\text{torsion terms}
+
\text{curvature terms involving }W_3^+,\rho_*''
\Bigr).
}
\tag{2.2}
\]

The AAD identities provide the ingredients: \(d^Ju\), \(W_3^+\), \(\rho_*''\), and the anti-Hermitian Ricci part. The desired theorem shape is:

\[
\boxed{
\delta^2\mathcal{H}
\ge
c\,\|\dot\Omega\|^2
}
\tag{2.3}
\]

on the subspace of variations that preserve the symplectic class and the exceptional flux orientation. If (2.3) holds only when \(\delta_b\le1-\eta\), then the Blair–Ianus class cannot approach \(\delta_b=1\) smoothly.

The first computation is to expand (2.2) on the certified Bianchi-IX cell, where the torsion profile is explicit, and identify the coefficient of the variation that increases \(\delta_b\). If that coefficient becomes small or changes sign only near \(\delta_b=1\), the route is promising. If the coefficient remains positive and allows a path with \(\delta_b\to1\) while decreasing \(\mathcal{H}\), the route is refuted.

---

## 3. Construction routes: conformally Kähler and diffuse Einstein–Maxwell states

A lower-bound theory must be tested by construction. The Einstein–Maxwell layer gives two natural construction programs.

---

### 3.1 Conformally Kähler Einstein–Maxwell ansatz

Let \(g_K\) be a Kähler metric on \(M=X\#k\overline{\mathbb{CP}}^{\,2}\), with Kähler form \(\omega_K\). Let \(a^-\) be an exceptional anti-self-dual harmonic class, and for a conformally related metric

\[
g=f^{-2}g_K
\]

let \(h_g\) be the \(g\)-harmonic anti-self-dual representative of \(a^-\). Consider the closed Maxwell field

\[
F=\omega_K+2\pi h_g.
\]

Because conformal changes preserve the self-dual/anti-self-dual decomposition in dimension four, \(F^+=\omega_K\) and \(F^-=2\pi h_g\) with respect to \(g\). The Einstein–Maxwell equation is

\[
\boxed{
\operatorname{Ric}^\circ_g
=
4\pi\,(\omega_K\circ h_g)_0,
}
\tag{3.1}
\]

with constants adjusted to the Step-66 convention.

Using the conformal transformation law for tracefree Ricci curvature, (3.1) becomes a coupled elliptic system for \(f\) and \(h_g\):

\[
\boxed{
\operatorname{Ric}^\circ_{f^{-2}g_K}
-
\operatorname{Ric}^\circ_{g_K}
=
4\pi\,(\omega_K\circ h_g)_0
-
\operatorname{Ric}^\circ_{g_K}.
}
\tag{3.2}
\]

Since both sides are \(J\)-invariant when \(h_g\) is of type \((1,1)\) relative to \(J\), this reduces to a scalar or vector-scalar system for \(f\). If \(g_K\) is extremal or constant-scalar Kähler, the linearization is especially simple.

#### Why this might work

Known conformally Kähler Einstein–Maxwell metrics on blow-ups of \(\mathbb{CP}^2\) arise through closely related conformal transformations of extremal Kähler metrics. The Arezzo–Pacard blow-up machinery supplies constant-scalar Kähler metrics on general-type blow-ups. If the linearized operator around such a metric is solvable with a positive conformal factor \(f\), one obtains a genuine compact Einstein–Maxwell metric with prescribed \(F^-\).

#### Decisive first computation

Linearize (3.2) at a constant-scalar Kähler blow-up metric \(g_K\). Write \(f=1+v\) and \(h_g=h_{g_K}+\dot h\). The linearized equation has the form

\[
\mathcal{L}_{K}v+\mathcal{M}_{K}\dot h
=
4\pi(\omega_K\circ h_{g_K})_0-\operatorname{Ric}^\circ_{g_K}.
\]

The first computation is to solve this equation on the certified cell and on the Arezzo–Pacard model, using the known Green’s functions near the exceptional spheres. The output should be:

- the induced flux deficit \(\delta\);
- the amplitude loss \(L_{\mathrm{amp}}\);
- the sign of \(v\), ensuring \(f>0\).

#### Refutation

The route is refuted if:

1. the linearized equation has no solution except \(v=0\) for all relevant exceptional \(h\);
2. a maximum-principle argument forces \(f\) to be constant whenever \(h_g\) is harmonic anti-self-dual;
3. numerical continuation shows that before \(\delta\) becomes \(O(1)\), the metric crosses above tariff, i.e.
   \[
   p\ge |a^-|^2
   \]
   or higher.

---

### 3.2 Diffuse common-mode Einstein–Maxwell construction

The certified Burns cells supply only small \(\delta\le O(10^{-2})\). A state with \(p\ll k\), if it exists, must be diffuse. The natural ansatz is an almost-Kähler structure with

\[
s=-4,
\qquad
u=\frac{|\nabla\Omega|^2}{4},
\qquad
u_{\mathrm{rms}}\approx 2\sqrt{\frac{k}{A}},
\]

and with harmonic twist projection

\[
\mathsf{H}^-(t_J^-)\approx 2\pi h_\Sigma,
\]

where \(h_\Sigma\) is a diffuse harmonic anti-self-dual form representing the combined exceptional flux.

The exact identities governing this ansatz are Step 64’s flux relation and Step 66’s torsion-financing identity. For a constant-\(s\) almost-Kähler metric,

\[
\boxed{
4\Phi_b^2\delta_b(1-\delta_b)
=
\int_M u(-s-6u)
-
2\|\rho_*''\|^2
-
4\|W_3^+\|^2.
}
\tag{3.3}
\]

At \(s=-4\),

\[
4\Phi_b^2\delta_b(1-\delta_b)
=
\int_M u(4-6u)
-
2\|\rho_*''\|^2
-
4\|W_3^+\|^2.
\]

The construction problem is to find \((g,J)\) such that:

1. \(u\) is diffuse with RMS size \(2\sqrt{k/A}\);
2. \(\mathsf{H}^-(t_J^-)=2\pi h_\Sigma+o(\sqrt{k})\);
3. \(W_3^+\) and \(\rho_*''\) balance (3.3);
4. the full Levi-Civita and Bianchi equations hold.

#### Decisive first computation

Project the system onto the finite-dimensional space spanned by:

- the lowest self-dual Weyl eigenforms of the Kähler host;
- the Green’s functions centered at the blow-up points;
- the exceptional harmonic anti-self-dual forms.

Solve the projected algebraic system for the amplitudes. The formal common mode is the algebraic solution with

\[
p\sim \frac{k^2}{A},
\qquad
\kappa\sim k.
\]

The decisive question is whether the projected system admits a branch with

\[
p=o(k)
\]

while keeping the twist harmonic projection aligned. If it does, one has the seed of a cheap diffuse construction. If the projected system has no such branch, the obstruction is already visible at the level of global flux balance.

#### Refutation

The construction route is refuted if the projected system forces either

\[
L_{\mathrm{amp}}\ge c\,\delta
\]

with \(c\) large enough to restore a tariff, or if the necessary Nijenhuis cores produce logarithmic twist energy of order \(k\) through the Hopf-type mechanism of Proposition 64.H. Conversely, an explicit numerical solution of the projected system with \(p/k\to0\) would be strong evidence that no positive tariff exists.

---

## 4. A weaker but provable Kähler-end tariff

Even if the full open range remains undecided, there is a serious local theorem near the Kähler end. This theorem would be genuinely weaker than Einstein nonexistence because it applies only when all exceptional flux deficits remain small.

### 4.1 Local coercivity of misalignment

For each exceptional harmonic form \(h_i\), define the flux deficit \(\delta_i\) and ledger loss \(L_i\) by the Step-65 relation

\[
p
=
\frac{(1-\delta_i)^2}{\|h_i\|^2}
+
L_i.
\]

A natural local coercivity statement is:

\[
\boxed{
L_i \ge c_0\,\delta_i
\qquad
\text{for }0\le\delta_i\le\delta_0,
}
\tag{4.1}
\]

with \(c_0>0\). The certified perpendicular cells suggest \(c_0\approx 0.8\) to \(1.0\). If (4.1) holds, then

\[
p
\ge
(1-\delta_i)^2+c_0\delta_i
=
1-(2-c_0)\delta_i+\delta_i^2.
\]

For \(\delta_i\le\delta_0\),

\[
p
\ge
1-(2-c_0)\delta_0.
\]

With \(c_0\approx0.8\), this gives a local tariff of roughly

\[
p\ge 1-1.2\delta_0.
\]

For \(k\) nearly orthogonal exceptional classes, a summed version gives

\[
\boxed{
\frac{P}{8\pi^2}
\ge
\bigl(1-(2-c_0)\delta_0\bigr)k
-
O(k^{1/2}),
}
\tag{4.2}
\]

provided the exceptional harmonic representatives have controlled Gram matrix. This is weaker than Einstein nonexistence because it says nothing when some \(\delta_i\) approaches \(1\). It is nevertheless a real tariff near the Kähler end.

### 4.2 Proof mechanism: second variation around cscK blow-ups

Let \(g_0\) be a constant-scalar Kähler blow-up metric. At \(g_0\),

\[
\delta_i=0,
\qquad
L_i=0.
\]

The first-order Burns efficiency calculation shows that no first-order deformation can produce saving beyond the efficiency \(1/4\). The certified cell’s saving appears at second order and is accompanied by comparable misalignment. Therefore the relevant object is the quadratic form

\[
\boxed{
Q_{c,i}(h)
=
\delta^2 L_i(h)-c\,\delta^2\delta_i(h)
}
\tag{4.3}
\]

on the space of blow-up deformations and transverse-traceless deformations.

The desired local theorem is:

\[
\boxed{
Q_{c_0,i}\ge0
\quad\text{for all exceptional deformations,}
}
\tag{4.4}
\]

with \(c_0>0\). The Koiso-type spectral gap on the minimal general-type host controls the non-exceptional modes; the exceptional modes can be computed explicitly using the Green’s functions of the scalar Laplacian and the Burns-cell profiles.

#### Decisive first computation

Assemble the Hessian matrix of \((L_i,\delta_i)\) with respect to:

- exceptional area parameters;
- relative positions of blow-up points;
- the lowest transverse-traceless modes of the host.

Evaluate the smallest eigenvalue of

\[
\delta^2L_i-c\,\delta^2\delta_i.
\]

The certified one-cell family already gives the diagonal entry. The new computation is the off-diagonal interaction between different exceptional classes. If the matrix remains positive for \(c=c_0>0\), then (4.1) follows in a neighborhood of the Kähler metric.

#### Refutation

A deformation direction with

\[
\delta_i\to0,
\qquad
\frac{L_i}{\delta_i}\to0
\]

would refute (4.1). The certified cells indicate that \(c_0\) cannot be much larger than \(1\); if the Hessian has a direction with \(L_i/\delta_i\to0\), then even the local tariff is absent.

---

### 4.3 Torsion-based Kähler-neighborhood tariff

There is an alternative formulation that uses the almost-Kähler torsion directly. For a constant-\(s\) almost-Kähler metric with \(J\)-invariant Ricci tensor, Step 66 gives

\[
4\Phi_b^2\delta_b(1-\delta_b)
=
\int_M u(-s-6u)
-
2\|\rho_*''\|^2
-
4\|W_3^+\|^2.
\tag{4.5}
\]

At \(s=-4\),

\[
4\Phi_b^2\delta_b(1-\delta_b)
\le
\int_M u(4-6u).
\tag{4.6}
\]

Suppose the metric is near the Kähler end in the sense

\[
\int_M u \le \varepsilon\Phi_b^2,
\qquad
\int_M u^2 \le \varepsilon^2\Phi_b^2,
\qquad
\|\rho_*''\|^2+\|W_3^+\|^2 \le \varepsilon^2\Phi_b^2.
\]

Then (4.6) implies

\[
\delta_b \le C\varepsilon
\]

for an explicit constant \(C\). The ledger then gives

\[
\boxed{
p
\ge
|b^-|^2(1-C\varepsilon)^2.
}
\tag{4.7}
\]

For \(k\) exceptional classes, this becomes

\[
\boxed{
\frac{P}{8\pi^2}
\ge
k(1-C\varepsilon)^2
-
O(k^{1/2}).
}
\tag{4.8}
\]

This formulation is especially clean because it does not require proving \(L_i\ge c\delta_i\) directly; it uses the exact torsion-financing identity to show that small torsion forces small flux deficit.

#### Decisive first computation

Solve the variational problem:

\[
\text{maximize }\delta_b
\text{ subject to }
\int u(4-6u)\ge 4\Phi_b^2\delta_b(1-\delta_b),
\quad
\int u\le\varepsilon\Phi_b^2.
\]

This gives the optimal constant \(C\). Then compare with the certified cell, where \(u\) and \(\delta_b\) are computable.

#### Refutation

An almost-Kähler metric with \(J\)-invariant Ricci tensor, small \(u\), but \(\delta_b\) bounded away from zero would refute the torsion-based local tariff. Such an object would already be a serious step toward a global cheap state.

---

## 5. Comparative scientific value

The four mechanisms have different consequences:

1. **Seiberg–Witten/Weyl susceptibility**  
   If
   \[
   \kappa\le k+\beta p
   \]
   holds on the Einstein–Maxwell layer, the open range is resolved with a \(k^2/A\) law. This is the strongest analytic route.

2. **Taubes/Blair–Ianus symplectic obstruction**  
   If the symplectic cone feasibility problem excludes \(\delta_b\approx1\), then the strictly almost-Kähler equality class collapses toward the Kähler end or Einstein points. This would remove the main intermediate equality class.

3. **Einstein–Maxwell construction**  
   A conformally Kähler or diffuse Einstein–Maxwell family with \(p=o(k)\) would refute every positive tariff and show that the correct scale is smaller than \(k\), possibly zero. This is the strongest constructive route.

4. **Kähler-end local tariff**  
   The coercivity estimate
   \[
   L_i\ge c_0\delta_i
   \quad\text{for }\delta_i\le\delta_0
   \]
   or the torsion-based estimate
   \[
   p\ge k(1-C\varepsilon)^2
   \]
   would give a rigorous theorem near the Kähler end without deciding Einstein existence or the deep \(\delta\approx1\) regime.

The most decisive immediate observations are therefore:

- compute the Hessian of \(\kappa-k-\beta p\) on exceptional blow-up deformations;
- solve the Taubes symplectic-cone feasibility problem for \(\delta_b\) near \(1\);
- linearize the conformally Kähler Einstein–Maxwell equation around a constant-scalar Kähler blow-up;
- compute the optimal constant in the torsion-financing inequality (4.6).
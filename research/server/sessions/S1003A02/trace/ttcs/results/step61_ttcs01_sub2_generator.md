# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Sessions/S1003A02/workspace/notes/step61_EH_quantitative_obstruction.md",
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md"
  ]
}
```

## Task

Research goal: a lower bound for α(M)=inf_g ∫|Ric°|² on M=X#kCP̄² (X minimal general type, A=c1²(X)) in the open range 0<k<A/3. Equivalently, the inequality C₊(g)=(1/2π²)∫|W⁺|²+(1/96π²)∫s² ≥ A−(1−c)k for some c>0, or a k²/A-type law, or a construction showing P/k→0. The files record what is known. Proved: LeBrun's monopole bound gives only C₊≥2A/3. The fixed-complex Kähler infimum is exactly 8π²k. A certified non-Kähler cell has P/8π² ≈ 0.99566 per blow-up. The new local laws (Theorem 59.R/Φ, Theorem 61.EH) show that the tensor R⁺=W⁺+s/12 governs both Burns (CP̄²-bubble, positive mass) and Eguchi–Hanson insertion costs: first order through the kernel, second order through the splitting of the complementary eigenvalues. Theorem Y/K give necessary Yamabe/Weyl-departure conditions. The Anderson ledger gives conditional minimizer structure, with collapse and (N0) gates open. Task: propose the two or three most promising genuinely new mechanisms that could yield a GLOBAL lower bound P≥c·k·f(k/A) for all metrics in the open range, or a decisive construction with P/k→0. Each must accommodate the certified sub-unit cell and the formal common mode P≈2π²k²/A. Possible ingredients include: a global identity combining the monopole Weitzenböck formula with the local R⁺-response law (e.g. a 'response-weighted' SW estimate); a Yamabe-excess obstruction; using that near-minimizers must have R⁺≤0 with |T|² controlled at bubble points to feed back into the C₊ integral; and the collapse gate. For each mechanism give the precise inequality to aim for and its quantifiers, the first decisive calculation or counterexample test, and the exact place where previous attempts failed (from the files) that it circumvents. Do not propose additive universal surgery tariffs or Weyl-only arguments, which are known to fail.

## Output

The organizing identity is

\[
\frac{P(g)}{8\pi^2}=C_+(g)-A+k,
\qquad 
C_+(g)=\frac1{2\pi^2}\int_M |R^+|^2,
\qquad 
R^+=W^++\frac{s}{12}I .
\]

Thus a law \(P\ge 8\pi^2 c\,k^2/A\) is exactly

\[
C_+(g)\ge A-k+c\,\frac{k^2}{A}.
\]

The local insertion laws say that an exceptional cell becomes sub-unit only when the local \(R^+\)-Rayleigh quotient and the transverse splitting are tightly controlled. The missing global input is therefore not another local tariff, but a way to force the \(L^2\)-mass of \(R^+\) to respond to the total exceptional charge \(k\). Three mechanisms look most promising.

---

## 1. Response-weighted Seiberg–Witten capacity

### Target inequality

For unit-volume metrics on \(M=X\#k\overline{\mathbb{CP}}^2\), at least in the noncollapsed regime and then extended by pricing collapse, one wants

\[
C_+(g)\ge A-k+\frac{1}{\mathfrak C_X(g)}
\left(\sum_{i=1}^k q_i(g)\right)^2,
\]

where \(q_i(g)\) is the local exceptional charge carried by the \(i\)-th blow-up class and \(\mathfrak C_X(g)\le C(A+k)\) is a chiral capacity. In the near-Einstein or near-Kähler regime one expects \(\mathfrak C_X\approx A\), giving

\[
P(g)\ge 8\pi^2 c_W\,\frac{k^2}{A+k}.
\]

Equivalently,

\[
C_+(g)\ge A-k+c_W\frac{k^2}{A+k}.
\]

The formal common mode \(P\approx 2\pi^2 k^2/A\) corresponds to \(c_W=1/4\).

### Mechanism

Use the Seiberg–Witten monopole equations for the blow-up basic classes

\[
K_X+\sum_i \varepsilon_i E_i,\qquad \varepsilon_i=\pm1.
\]

The Weitzenböck identity pairs \(R^+\) with the self-dual two-form built from the spinor. The Burns and Eguchi–Hanson laws identify an exceptional cell as a localized source for exactly this pairing: the first-order insertion cost is \(R^+(\zeta,\zeta)\), and the second-order cost is governed by the splitting of the complementary eigenvalues.

The new step is to weight the family of basic classes by the local response. Instead of applying one monopole inequality to one class, sum a weighted Weitzenböck identity over the basic-class cube, with weights chosen so that the exceptional directions add coherently. The result should be a global source term of total charge \(k\). The canonical monopole curvature on the minimal model supplies a test field whose energy is proportional to \(A\). Cauchy–Schwarz, or equivalently a Dirichlet/capacity principle for the Green’s operator of the linearized \(R^+\)-response equation, then gives a lower bound of the form

\[
\int_M |R^+|^2 \;\gtrsim\; \frac{k^2}{A}.
\]

This directly converts the local \(R^+\)-response law into a global \(L^2\) lower bound.

### First decisive calculation

Work on a Kähler–Einstein or canonical-orbifold background \(X\). Linearize the gauged \(P\)-equation, or equivalently the \(R^+\)-Weitzenböck operator, and compute its Green’s operator \(G\). A Burns insertion in direction \(\zeta\) at \(p\) gives a source schematically of the form

\[
S_{p,\zeta}=\delta_p\left(\zeta\otimes\zeta-\frac13 I\right).
\]

Compute the quadratic form

\[
Q(\{p_i,\zeta_i\})
=
\sum_{i,j}
\langle S_{p_i,\zeta_i},G(S_{p_j,\zeta_j})\rangle .
\]

The capacity mechanism is real if, for the all-ones vector of \(k\) equal charges,

\[
Q \sim \frac{k^2}{A}.
\]

For symmetric backgrounds, such as compact complex-hyperbolic quotients, this can be tested spectrally. One expands \(G\) in tensor spherical modes and checks whether the constant or lowest mode contributes \(1/A\) to the total charge channel. A numerical finite-element or spectral computation on a ball quotient would also decide the point quickly.

A second test is to solve the monopole equations on a Kähler surface with \(k\) small disks removed and with spinor zeros forced at those disks. If the additional Weitzenböck energy is \(k^2/A\), the mechanism is confirmed.

### Where earlier attempts stopped, and how this circumvents them

LeBrun’s monopole estimate sees only one global topological square and yields \(C_+\ge 2A/3\). It does not separate the \(k\) exceptional charges. The local Burns expansion gives the correct one-cell response but has no interaction term between cells. The capacity mechanism supplies precisely the missing interaction: the exceptional charges are sources for a global \(R^+\)-field, and the field energy is controlled by the chiral capacity \(A\). This is not an additive surgery tariff; the cost is global and depends on the total charge channel.

---

## 2. Yamabe-excess and scalar matching

### Target inequality

A second route is to use the scalar part of \(R^+\). A model inequality is

\[
P(g)
\ge
c_Y A(\bar s-s_X)^2
+
\frac{c_Y'}{A}
\left(k-\beta A(s_X-\bar s)\right)^2,
\]

where \(\bar s\) is the constant scalar curvature of a Yamabe representative, \(s_X\) is the scalar value associated with the minimal model at the same volume normalization, and \(\beta\) is a universal constant fixed by the Chern–Weil normalization. Optimizing over \(\bar s\) gives

\[
P(g)\ge c_Y''\,\frac{k^2}{A}.
\]

Equivalently,

\[
C_+(g)\ge A-k+c_Y''\frac{k^2}{A}.
\]

One can also formulate this in terms of the Yamabe constant \(Y([g])\): if \(Y_{\rm SW}(A,k)\) is the maximum Yamabe value allowed by the monopole topology, then one wants

\[
P(g)\ge c_Y A\bigl(Y([g])-Y_{\rm SW}(A,k)\bigr)^2
+
c_Y'\frac{k^2}{A}.
\]

### Mechanism

The bulk minimal model has a scalar/Yamabe capacity of order \(A\). Exceptional Burns or Eguchi–Hanson cells are scalar-flat to leading order and carry a definite local Yamabe contribution. If \(P\) is small, the metric is close to an Einstein metric and the scalar curvature must be almost constant after a conformal change. But \(k\) scalar-flat exceptional cells cannot be attached to a bulk of scalar curvature of order one without shifting the global scalar value by an amount of order \(k/A\). The conformal factor producing this shift has Hessian energy, and that energy contributes to \(\int|{\rm Ric}^\circ|^2\).

This mechanism also uses the near-minimizer information \(R^+\le 0\) at bubble points. If the bubble points sit in the kernel of \(R^+\), they cannot absorb scalar excess locally. The scalar mismatch must therefore be redistributed over the whole manifold, and the global scalar response is again governed by a capacity proportional to \(A\).

The Yamabe route is especially useful because it detects a conformal degree of freedom that local \(P\)-expansions miss. The certified sub-unit cell may have a small local \(P\)-saving, but the conformal representative with constant scalar curvature may carry an additional global scalar cost.

### First decisive calculation

Take the multi-Burns ansatz on a Kähler–Einstein surface, with insertions in kernel directions \(\zeta_i\perp\omega\). The local \(P\)-expansion is known:

\[
\frac{P(g_\varepsilon)}{8\pi^2}
=
k
-
k\frac{s^2}{64}\varepsilon^2\log(1/\varepsilon)
+
O(\varepsilon^2).
\]

Now compute the Yamabe functional of the same family, or better compute the conformal factor that restores constant scalar curvature and evaluate the resulting trace-free Ricci energy. The decisive term to look for is a positive rank-one quadratic form

\[
\frac{1}{A}\left(\sum_i \varepsilon_i\right)^2
\]

or, for unit exceptional charges, a term \(k^2/A\). If this term appears and cannot be removed by an allowed conformal deformation, the Yamabe-excess mechanism gives the desired global lower bound.

A concrete first test is to compute the Yamabe constant of the certified CH-collar cell numerically, using Yamabe flow or conformal finite elements. If the cell’s Yamabe excess above the monopole-allowed value is of the same order as its defect from the unit tariff, then the scalar channel is quantitatively active.

### Where earlier attempts stopped, and how this circumvents them

The local Burns expansion was performed in a fixed conformal representative. It captured the \(R^+\)-kernel saving but did not account for global scalar redistribution. Weyl-only arguments miss this because they ignore the scalar trace part of \(R^+\). The Yamabe mechanism uses the full tensor \(R^+\), including \(s\), and uses conformal geometry to convert scalar mismatch into trace-free Ricci energy.

---

## 3. Orbifold/ALE pricing, collapse pricing, and possible zero-gap construction

### Target lower-bound form

For a minimizing sequence with an Anderson decomposition into an Einstein orbifold bulk and ALE/Burns bubble regions, one wants a finite-dimensional pricing formula

\[
\liminf P(g_i)
\ge
\inf_{\mathcal D}
\left\{
\sum_{j\in{\rm EH}}
\pi^2 a_j^4 |R^+_{p_j}\zeta_j|^2
+
\sum_{\ell\in{\rm Burns}}
\left[
8\pi^2
-
8\pi^2\varepsilon_\ell \mu_\ell
+
4\pi^2\Phi_\ell\varepsilon_\ell^2\log(1/\varepsilon_\ell)
\right]
+
\frac{c}{A}Q(\mathcal D)^2
\right\},
\]

where \(Q(\mathcal D)=k\) is the total exceptional charge carried by the decomposition. If every topologically allowed direction has positive first or second obstruction, this gives

\[
\liminf P(g_i)\ge c\,\frac{k^2}{A}.
\]

If, however, there is an allowed orbifold smoothing with \(R^+\zeta=0\) and vanishing second obstruction, the same formula gives \(\alpha(M)=0\), and in a family with \(k/A\to0\) it gives \(P/k\to0\).

### Mechanism

The Eguchi–Hanson theorem gives a sharp leading price for resolving an Einstein orbifold point by an EH bubble:

\[
P_{\rm EH}
=
\pi^2 a^4 |R^+_p\zeta|^2
+
O(a^6\log(1/a)).
\]

The Burns expansion gives the analogous price for a \(\overline{\mathbb{CP}}^2\)-type bubble. Anderson decomposition supplies the possible global configurations. Topological reassembly supplies the charge constraint \(Q=k\). The global capacity term \(Q^2/A\) can be supplied by Mechanism 1, but even without it the finite-dimensional obstruction matrix can force a positive price if the kernel directions are not topologically available.

The collapse channel must be priced as well. Total collapse cannot occur for \(X\#k\overline{\mathbb{CP}}^2\) because \(\chi>0\). Partial collapse along an \(F\)-structure can carry only fiber homology. The exceptional class with square \(-1\) cannot be wholly absorbed by spin circle fibers. In an adiabatic circle-invariant model, the reduced three-dimensional energy contains a Yang–Mills/Chern–Simons term for the exceptional line bundle, and that term is at least charge squared divided by the base capacity, or else it forces an ALE bubble. Thus collapse should not provide a free escape channel; it either reduces to the same \(k^2/A\) price or produces one of the orbifold/ALE configurations already being priced.

### Zero-gap construction branch

The same mechanism can produce a decisive construction if one can find a compact Einstein orbifold \(V\) whose isolated singularities admit Ricci-flat ALE replacements or Milnor-fibre smoothings giving

\[
M\cong X\#k\overline{\mathbb{CP}}^2
\]

in the open range \(0<k<A/3\). Candidates include:

- hyperbolic or ball-quotient orbifolds with many \(\mathbb Z_2\) points;
- Wahl-type orbifolds satisfying the known lattice conditions;
- cusped hyperbolic fillings or doubles if their topology can be matched to general-type blow-ups.

If such a \(V\) exists and the relevant gluing directions satisfy

\[
R^+_p\zeta=0
\]

and the second obstruction also vanishes, then gluing Ricci-flat ALE spaces at scale \(\lambda\) gives

\[
P(g_\lambda)=O(\lambda^q)\to0.
\]

For a family with \(k/A\to0\), this would give \(P/k\to0\) and would disprove any positive \(c k\) law.

### First decisive calculation

The most decisive local computation is the second Eguchi–Hanson obstruction on \(\ker R^+\). In the notation of Step 61, one wants the quadratic form governing

\[
\inf P
\quad\text{when}\quad
R^+_p\zeta=0.
\]

The conjectural structure is that the second pairing is a quadratic form in the complementary eigenvalues \(\mu_2,\mu_3\), possibly vanishing exactly when \(\mu_2\mu_3=0\). This can be attacked by the flux method applied to the fourth-order jet \(\hat h_4\), using the \(U(2)\)-invariance of Eguchi–Hanson space to reduce to cohomogeneity-one ODEs.

If the second obstruction is positive on all topologically allowed directions, EH channels cost at least \(\Theta(a^4)\) and contribute to a positive lower bound. If it vanishes in a topologically allowed direction, then one should attempt the gluing construction immediately.

A second decisive step is topological: solve the orbifold Noether relation

\[
(2\chi+3\tau)_V+\text{singularity contributions}=A-k
\]

for Einstein orbifolds \(V\) whose smoothings are \(X\#k\overline{\mathbb{CP}}^2\). A single verified example gives a zero-gap construction. A classification excluding such orbifolds in the open range strengthens the lower-bound program.

### Where earlier attempts stopped, and how this circumvents them

The earlier orbifold route relied on assuming that all nontrivial bubbles are Ricci-flat and on an unproved energy equality. The Eguchi–Hanson flux computation replaces the first assumption by an explicit price for non-Ricci-flat channels, and flux conservation gives a route to the missing neck energy accounting. The certified sub-unit cell is then not an additive tariff but one priced local piece inside a global decomposition.

---

## Priority order

The strongest candidate for an all-metrics lower bound is Mechanism 1: response-weighted Seiberg–Witten capacity. It directly targets

\[
C_+(g)\ge A-k+c\frac{k^2}{A}
\]

and uses the known local \(R^+\)-response laws as source terms.

The fastest decisive test is Mechanism 3: compute the second Eguchi–Hanson obstruction and search for an Einstein orbifold smoothing. This can either produce the desired lower-bound price or produce a zero-gap construction.

Mechanism 2 is the main conformal reinforcement. It closes the possible loophole that local \(P\)-expansions miss scalar redistribution, and it is likely needed to turn a near-Einstein local analysis into a global inequality.
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

Write
\[
p(g):=\frac{P(g)}{8\pi ^2},\qquad d(g):=A-C_+(g)=k-p(g).
\]
Thus a \(k^{2}/A\) estimate is naturally a response estimate for the chiral-energy deficit \(d\). The sharp-looking target is
\[
\boxed{\quad d(g)_+^2\le 4A\,p(g).\quad} \tag{R}
\]
Indeed, \((k-p)^2\le4Ap\) implies
\[
p(g)\ge \big(\sqrt{A+k}-\sqrt A\big)^2
=\frac{k^2}{(\sqrt{A+k}+\sqrt A)^2}
=\frac{k^2}{4A}+O\!\left(\frac{k^3}{A^2}\right),
\]
hence
\[
P(g)\ge 2\pi^2\frac{k^2}{A}\left(1+O(k/A)\right).
\]
Any version \(d_+^2\le CAp\) would already give \(P\ge c\,k^2/A\).

This formulation separates the genuinely hard regime from isolated surgery. The certified cell has \(p/k\simeq0.9956627\), hence \(d/k\simeq0.0043373\); it lies very far from \(d\simeq k\), which is what \(p\ll k\) would require. Thus no per-cell estimate near one can settle the common mode.

A useful preliminary reduction is to Yamabe representatives. In each conformal class the \(L^2\)-norm of \(W^+\) is fixed, while the Yamabe representative minimizes the relevant scalar \(L^2\)-term. Put
\[
\mathcal E_Y=\frac1{96\pi^2}\int s^2-\frac A3\ge0,\qquad
\mathcal R_W=\frac{2A}{3}-\frac1{2\pi^2}\int |W^+|^2.
\]
Then
\[
p=k+\mathcal E_Y-\mathcal R_W,\qquad
d=\mathcal R_W-\mathcal E_Y.
\]
Consequently \(p\ll k\) requires a collective drop \(\mathcal R_W\simeq k+\mathcal E_Y\), not merely a favorable local value of \(W^+\). The mechanisms below couple that drop to \({\rm Ric}^\circ\); none is a Weyl-only estimate.

---

## 1. A response-weighted Seiberg–Witten identity retaining the full blow-up hypercube

For
\[
\mathfrak a_\varepsilon=K+\sum_{j=1}^k\varepsilon_jE_j,
\qquad \varepsilon_j\in\{\pm1\},
\]
all \(2^k\) classes are monopole classes and \(\mathfrak a_\varepsilon^2=A-k\). For every metric,
\[
\begin{aligned}
\mathfrak D_g
&:=2^{-k}\sum_\varepsilon
 \left((\mathfrak a_\varepsilon^+)^2-\mathfrak a_\varepsilon^2\right)\\
&=(K^+)^2-A+\sum_{j=1}^k|E_j^+|^2+k
\ge k. \tag{1.1}
\end{aligned}
\]
This is the piece of information erased by the usual convex-hull argument: LeBrun’s estimate retains only a radius at least \(\sqrt A\), whereas (1.1) retains the anti-self-dual energy defect \(k\).

### Precise estimate to seek

For every smooth metric \(g\), seek perturbed monopole solutions for the whole sign family and an averaged trace-free response tensor \(\mathbb T_g\) satisfying
\[
\left(4\pi^2\mathfrak D_g-\frac12P(g)\right)_+
 \le
\left|\int_M\langle {\rm Ric}^\circ,\mathbb T_g\rangle\,d\mu\right|,
\tag{1.2}
\]
together with
\[
\int_M|\mathbb T_g|^2\,d\mu
\le 8\pi^2A. \tag{1.3}
\]
Then (1.1)–(1.3) and Cauchy–Schwarz give
\[
4\pi^2(k-p)_+\le \sqrt{P}\sqrt{8\pi^2A},
\]
which is exactly (R). A robust variant
\[
\|\mathbb T_g\|_2^2\le C\pi^2(A+\mathcal E_Y)
\]
still yields \(d^2\le C'Ap\): whenever \(d>0\), one has
\(\mathcal E_Y<\mathcal R_W\le2A/3\).

The natural \(\mathbb T_g\) is the trace-free metric stress tensor of the completed-square Seiberg–Witten Weitzenböck identity, averaged over \(\varepsilon\). Before integration by parts it should contain calibrated combinations of
\[
F_{A_\varepsilon}^+\circ F_{A_\varepsilon}^-,
\qquad
\operatorname{Re}\langle\nabla_i\Phi_\varepsilon,
\nabla_j\Phi_\varepsilon\rangle^\circ,
\qquad
(\nabla^2|\Phi_\varepsilon|^2)^\circ .
\]
The commutator of spinor derivatives inserts the curvature operator on \(\Lambda^+\), so the local algebra sees
\[
\mathbf R^+=W^++\frac{s}{12}I
\]
rather than \(|W^+|\) alone. Averaging over signs cancels the terms linear in individual \(E_j\), while the quadratic sign average gives precisely (1.1).

### First decisive calculation

The metric variation of the completed-square identity should be carried out for one perturbed monopole solution, with every divergence retained, and then averaged over all signs. Two exact calibrations are decisive:

1. **Burns flux.** On the flat/Burns matched model, the flux of the resulting stress tensor against the insertion variation must equal
   \[
   -8\pi^2\,\mathbf R^+(\zeta,\zeta),
   \]
   reproducing Theorem 59.R. On a kernel direction, its quadratic response must recover the complementary splitting term \(-|T|^2\), with the same normalization as \(\Phi\).

2. **Kähler degeneration.** For an Arezzo–Pacard blow-up sequence, evaluate the averaged tensor using the Kähler monopole solutions. The left side of (1.2) is then largely absorbed by \(P/2\simeq4\pi^2k\), so the estimate must become nearly vacuous rather than impose a unit surgery cost.

A further disproof test is any Einstein four-manifold carrying an analogous full monopole hypercube with \(k>0\): (1.2) would exclude it. No such example is presently recorded in the supplied material.

### What this changes relative to the earlier SW route

The estimate \(C_+\ge2A/3\) selects one monopole class, applies pointwise norm inequalities, and discards both the anti-self-dual cohomological defect and the spinor-gradient stress. That is exactly where \(k\) disappears. The response-weighted version averages first, preserves \((\mathfrak a^+)^2-\mathfrak a^2\), and pairs the surviving stress with \({\rm Ric}^\circ\). The local \(\mathbf R^+\)-laws provide the missing normalization of this metric response.

---

## 2. A renormalized capacity matrix for all bubbles, with the common mode \(1/(4A)\)

The local Burns and Eguchi–Hanson formulas strongly suggest that a bubble tree should be described by a finite-dimensional effective quadratic form, not by a sum of independent cell energies. In dimension four the relevant point-source problem is critical: the self-energy has logarithmic behavior, exactly matching the \(\varepsilon^2\log(1/\varepsilon)\) term in Theorem 59.R, while the spatially constant mode has energy of order charge-squared divided by volume, hence \(k^2/A\).

Let \(B\) be a smooth Einstein or \(P\)-critical bulk in a selected noncollapsed minimizing sequence, and let
\[
\mathcal L_B=D{\rm Ric}^\circ_B+\text{Bianchi gauge terms}.
\]
Each attached core determines a distributional source \(\ell_j\), defined by the bilinear flux at its asymptotic end. Its local renormalized energy is supplied by the exact model:

- Burns: first response \(-8\pi^2\mathbf R^+(\zeta,\zeta)\), followed on the kernel by the \(-|T|^2\log\) response;
- Eguchi–Hanson:
  \[
  P=\pi^2a^4|\mathbf R^+\zeta|^2+o(a^4).
  \]

After subtracting these exact self-energies, let \(G_B\) be the Green or capacity matrix of the remaining sources.

### Precise estimate to seek

For every noncollapsed selected minimizing sequence with smooth bulk and separated cores, seek screening variables \(\sigma_j\), residual charges \(r_j\), and local energies \(e_j(\sigma_j)\ge0\) such that
\[
p(g_i)\ge
\sum_j e_j(\sigma_j)+r^{\!T}G_Br-o(1),
\qquad
\sum_j r_j=d(g_i)=k-p(g_i)+o(1).
\tag{2.1}
\]
The global capacity estimate is
\[
\mathbf 1^{T}G_B^{-1}\mathbf 1\le4A, \tag{2.2}
\]
or \(\le C A\) for a first theorem. By quadratic duality,
\[
r^{T}G_Br
\ge \frac{(\sum_jr_j)^2}
{\mathbf1^TG_B^{-1}\mathbf1}
\ge\frac{d(g_i)^2}{4A}. \tag{2.3}
\]
Equations (2.1)–(2.3) again give (R).

This formulation automatically permits the certified sub-unit cell: no diagonal entry of \(G_B\), and no local \(e_j\), is required to be at least one. The measured value \(0.9956627\) is simply admissible local screening. The lower estimate comes from the unscreened collective charge \(d=k-p\), not from a sum of unit costs.

### How the \(\mathbf R^+\) rigidity enters

The Euler equations of the effective functional are already visible in the local laws:

- varying a Burns scale or direction gives \(\mathbf R^+(\zeta,\zeta)\);
- when \(\mathbf R^+\le0\), a zero Rayleigh direction is a kernel direction;
- on that kernel, the logarithmic term measures the trace-free splitting \(T\) of the complementary \(2\times2\) block;
- for an Einstein bulk, a cheap stationary core therefore requires
  \[
  \mathbf R^+\zeta=0,\qquad T=0,
  \]
  up to the scale of the remaining defect;
- an EH core has the stronger leading response \(|\mathbf R^+\zeta|^2\).

Thus the bubble points sample the tensor
\[
\mathcal S_B=(\lambda_{\max}(\mathbf R^+),T)
\]
rather than merely \(|W^+|\). A capacity estimate for the elliptic equation obeyed by \(\mathbf R^+\) on an Einstein or \(P\)-critical bulk can convert these sampled values into (2.2). The critical four-dimensional capacity is also the natural origin of the Burns logarithm.

### First decisive calculation

On a compact complex-hyperbolic quotient, compute \(G_B\) spectrally for kernel-direction Burns sources:

1. form the exact source \(\ell_{p,\zeta}\) from the flux in Theorem 59.R;
2. invert the gauged linearized operator on the orthogonal complement of its kernel;
3. separate the constant canonical mode from the remaining spectrum;
4. evaluate
   \[
   \mathbf1^TG_B^{-1}\mathbf1
   \]
   for equidistributed points.

Since
\[
\int_Xs^2\,d\mu=32\pi^2A
\]
on the KE bulk, the common-mode computation should produce \(4A\) if the formal coefficient \(p\sim k^2/(4A)\) is correct. The remaining spectral sum must reproduce the sign and scale of the one-cell \(\varepsilon^2\log(1/\varepsilon)\) response.

Three essential tests are:

- **cell collision:** as points merge, the matrix must pass to a charge-\(m\) core rather than continue as \(m\) independent entries;
- **the spherical EH example:** the model must exhibit a zero-energy orbifold reservoir rather than incorrectly force \(k^2/A\);
- **fixed-complex Kähler degeneration:** complete local screening should cost asymptotically \(p=k\), leaving \(d\to0\).

### What this changes relative to the earlier gluing route

Theorem 59.R computes one cell, while the balanced multi-cell matching law and interactions were deferred. Theorem 61.EH gives a sharp estimate only inside weighted neighborhoods of a prescribed orbifold degeneration. The capacity matrix is the missing collective object: it treats diagonal polarizability, off-diagonal interaction, collision, and the spatially constant mode in one quadratic form. It also gives a concrete representation in which the formal \(k^2/A\) coefficient can actually be calculated.

A zero eigenvector of the renormalized form has geometric meaning rather than being discarded: it should correspond to a Ricci-flat ALE replacement of an Einstein orbifold. Such a vector leads to \(\alpha=0\) through Proposition 59.N. Orbifold and collapsed reservoirs require the third mechanism.

---

## 3. An APS–adiabatic response formula for orbifold absorption and collapse

The remaining way to evade both preceding mechanisms is to store the deficit \(d=A-C_+\) in orbifold interface terms or in a collapsed region. Ordinary local curvature integrals do not see this storage: Ricci-flat ALE pieces can carry topology with \(P=0\), and finite-isotropy collapse contributes spectral correction terms.

For a selected minimizing sequence, let \(\Omega_i\) denote the thick Einstein-like region, \(N_{i,b}\) the ALE pieces, and \(C_i\) the collapsed portion. Define the assembled chiral quantity
\[
\mathscr I_i
=
C_+(\Omega_i)
+\sum_b w_+(N_{i,b})
+\eta_{\rm ad}(C_i), \tag{3.1}
\]
where \(w_+\) is the ALE Chern–Weil weight and \(\eta_{\rm ad}\) is the combined adiabatic signature and spin\(^c\)-Dirac correction on the cutting interfaces. Exact Chern–Weil assembly should give
\[
A-\mathscr I_i=k-p(g_i)+o(1). \tag{3.2}
\]

### Precise estimate to seek

For every selected minimizing sequence, including finite isotropy and graph-type collapsed regions, seek
\[
\boxed{\quad
\big(A-\mathscr I_i\big)_+^2
\le C\,A\,p(g_i)+o(1).
\quad} \tag{3.3}
\]
The sharp common-mode value is \(C=4\).

Combining (3.2) and (3.3) gives a global \(k^2/A\) estimate. Indeed, if \(p\ge k/2\), then \(p\) is already much larger than \(k^2/A\) for \(k<A/3\). If \(p<k/2\), then
\[
\frac{k}{2}\le C^{1/2}\sqrt{Ap}+o(1),
\]
so
\[
p\ge\frac{k^2}{4CA}+o(1).
\]

The analytic source of (3.3) should again be the complete sign family \(\mathfrak a_\varepsilon\), now inserted into APS index formulas on each cut piece. The joint signature and Dirac spectral corrections retain the odd characteristic information carried by the exceptional lattice. Pairing the residual index density with \({\rm Ric}^\circ\), followed by Cauchy–Schwarz, gives the right square-root structure.

### First decisive calculation

The first calculation is entirely finite and arithmetic:

1. For a Seifert or spherical interface \(Y\), compute the joint quadratic refinement
   \[
   \eta_{\rm sign}(Y)+\eta_{\rm Dirac}(Y,\mathfrak a_\varepsilon|_Y)
   \]
   for all sign restrictions, and average over \(\varepsilon\).

2. Perform this explicitly for
   \[
   Y=L(n^2,nm-1)
   \]
   arising from Wahl pieces, and for \(Y=\mathbb{RP}^3\) arising from EH.

3. Determine whether the resulting discriminant form can absorb an odd generator of \(\langle-1\rangle^k\) while preserving the canonical characteristic class from \(X\).

4. Extend the computation to graph interfaces using the Dai/Bismut–Cheeger adiabatic decomposition and Mayer–Vietoris for the intersection lattice.

Three model tests fix the interpretation:

- A free circle-collapse region is spin and should contribute no odd exceptional generator.
- The resolution of \(S^4/\{\pm1\}\) by two EH spaces must show exact cancellation of the two odd generators; otherwise the formula is normalized incorrectly.
- The Wahl lens-space calculation must reproduce the existing arithmetic alternatives \(n\) odd or \(8\mid n\).

### Lower estimate versus a zero-gap construction

This calculation has a decisive two-way outcome.

If the combined eta quadratic refinement leaves a residual odd charge proportional to \(k\), then (3.3) converts it into \(P\ge c\,k^2/A\). This would fill precisely the finite-isotropy, graph-interface, and adiabatic pieces left unresolved in the Anderson analysis.

If instead there are null vectors carrying the full exceptional charge, they give a construction blueprint. One seeks Einstein orbifold or finite-volume Einstein cores \(\Omega_\ell\) and Ricci-flat ALE or bounded-curvature collapsed fillings \(C_\ell\) with
\[
Q_{\rm total}\cong Q_{X_\ell}\oplus\langle-1\rangle^{k_\ell},
\qquad
c_1^2(X_\ell)=A_\ell>3k_\ell,
\]
with matching canonical spin\(^c\) data and vanishing assembled response. ALE replacement then gives \(\alpha=0\) by Proposition 59.N; an adiabatic filling gives the analogous conclusion by the interpolation mechanism of Proposition 59.D. A family with \(k_\ell\to\infty\) would give \(P/k_\ell\to0\).

The necessary source families are explicit: APS signature and spin\(^c\)-Dirac eta formulas for lens and spherical space forms, Bismut–Cheeger and Dai adiabatic eta formulas for locally free circle fibrations, and discriminant-form gluing for four-manifold intersection lattices.

---

## Synthesis

These mechanisms address different parts of the same response law:

- The **SW stress identity** is the direct all-metric route to
  \[
  (A-C_+)^2\lesssim A\,P.
  \]
  Its new input is the full sign hypercube and the anti-self-dual defect \(\mathfrak D_g\ge k\).

- The **capacity matrix** gives the geometric meaning of the sharp coefficient \(1/(4A)\), incorporates the certified sub-unit cell, and turns the local \(\mathbf R^+\)-responses into a collective effective action.

- The **APS–adiabatic formula** determines whether orbifold and collapsed regions can absorb the exceptional charge at zero \(P\). It either supplies the missing global estimate or identifies precise gluing data for a family with \(P/k\to0\).

The central quantitative object common to all three is not a surgery cost but the unscreened response charge
\[
d=A-C_+=k-\frac{P}{8\pi^2}.
\]
The most informative single formula is therefore
\[
\boxed{\;
\left(A-\frac1{2\pi^2}\int|W^+|^2
-\frac1{96\pi^2}\int s^2\right)_+^2
\le
\frac{A}{2\pi^2}\int|{\rm Ric}^\circ|^2,
\;}
\]
with a universal constant multiplying the right side if the sharp coefficient is inaccessible. It simultaneously matches the formal common mode, permits the measured Burns cell, and identifies any zero-gap sequence as requiring an exact orbifold or adiabatic response reservoir.
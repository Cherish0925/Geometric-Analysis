# Step 74: ℓ-mode classification, structural impossibility of higher-obstruction necessity, and hardness propagation

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

This note records three connected structural results that reshape the noncollapsed positive-branch proof architecture for Yau–26. All three are clean mathematical statements with explicit sources; they supersede the Step-70 skeleton's "higher-obstruction necessity" module and the Step-73 plan's ℓ>2 extension.

---

## 1. The ℓ-mode classification: first obstruction is the unique log-critical mode

### Statement (dimension-general)

Let \(d\ge4\), \(\Gamma\subset O(d)\) act freely on \(S^{d-1}\), \(A=\{b<r<R\}/\Gamma\), \(L=\log(R/b)\).

For integer \(\ell\ge2\), let \(K_\ell\) be a nonzero smooth symmetric 2-tensor on \(\mathbb R^d\setminus\{0\}\) with Cartesian component homogeneity
\[
K_\ell(rx)=r^\ell K_\ell(x),
\]
and satisfying \(\Gamma\)-invariance,
\[
\operatorname{tr}K_\ell=0,\quad
\operatorname{div}K_\ell=0,\quad
\Delta K_\ell=0,\quad
K_\ell(x,\cdot)=0.
\]
Define the dual mode \(o_\ell=r^{-(d+2\ell-2)}K_\ell\). Then \(o_\ell\) inherits trace-free, divergence-free, harmonic, and radial-null properties (proof: Step 73 plan §2). For a smooth interpolant \(u\) from \(0\) to \(K_\ell\), gauge terms pair away against \(o_\ell\), and the Wronskian identity gives
\[
\int_A\langle D\operatorname{Ric}_e u,\,o_\ell\rangle
=-\frac{d+2\ell-2}{2}\,I_{K_\ell},
\qquad
I_{K_\ell}=\int_{S^{d-1}/\Gamma}|K_\ell|^2_{r=1}\,d\theta.
\]
At \(\ell=2\) this is the proved FND:flux (manuscript lines 891–907) with coefficient \(-(d+2)/2\).

**Key: the unweighted nuclear-norm mass.** The duality estimate requires bounding
\[
\int_A\|o_\ell\|_*\,dV
=J_{K_\ell}\int_b^R r^{1-\ell}\,dr
=J_{K_\ell}\cdot H_\ell(b,R),
\]
where
\[
H_\ell(b,R)=
\begin{cases}
\log(R/b)=L, & \ell=2,\\[1mm]
\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2}, & \ell>2.
\end{cases}
\]

The unweighted operator-norm lower bound is therefore
\[
\|D\operatorname{Ric}_e u\|_{op,\infty}
\ge \frac{(d+2\ell-2)\,I_{K_\ell}}{2\,J_{K_\ell}\,H_\ell(b,R)}.
\]

### Consequence: ℓ=2 is the unique unweighted log-critical mode

- **\(\ell=2\):** \(H_2=L\), giving the inverse-logarithmic lower bound
\[
\delta\ge \frac{(d+2)I_K}{2LJ_K}\sim \frac{c}{L}.
\]
This is the only polynomial mode producing a logarithmic denominator.

- **\(\ell>2\):** \(H_\ell\sim b^{2-\ell}/(\ell-2)\) for \(b\ll R\), giving
\[
\delta\ge c\,b^{\ell-2}\to0
\]
in the bubbling limit \(b\to0\). This is a power-scale lower bound, not a log-scale one. It cannot produce the relation \(\delta L\ge c\) needed for the exponential-neck dichotomy.

There is a weighted version: \(\sup_A r^{2-\ell}\|D\operatorname{Ric}_e u\|_{op}\ge c/L\) for all \(\ell\ge2\). But Yau–26 controls the unweighted operator norm, so only \(\ell=2\) is log-critical under the problem's hypothesis.

### Formal status

The \(\ell=2\) identity is proved in the manuscript (FND:flux) and checked in Step 69. The general \(\ell\) identity follows by the same integration-by-parts argument with the appropriate dual mode. The nuclear-norm mass is an elementary calculus of
\(\int r^{1-\ell}dr\). The TTCS verification (Step 73) confirmed the correct denominator scaling and explicitly rejected the earlier unweighted \(c/L\) claim for \(\ell>2\). Both TTCS branches agreed on this correction.

---

## 2. Structural impossibility of forcing higher obstructions from small δ

This is the central negative result. It explains why the Step-70 proof skeleton cannot close through a "higher-obstruction necessity" module.

**Caveat (from TTCS verification):** No concrete nonzero higher obstruction has been computed on the mixed rows. The argument proves the *inference mechanism* is impossible (no small-δ theorem can force higher obstructions to vanish), not that a nonzero higher obstruction actually exists. The mode identification (cone degree ℓ and Biquard–Ozuch obstruction order k) also needs a separate theorem; the ℓ-classification and the t-scaling hierarchy are independent inputs supporting the same conclusion from different angles.

### The two independent arguments

**Argument A: flux scaling.** The ℓ-classification (§1) shows that ℓ>2 modes give power-scale lower bounds vanishing in the bubbling limit. A sequence with δ→0 and ℓ=2 mode vanishing does not receive any logarithmic obstruction from ℓ>2 modes; the unweighted defect from these modes is compatible with δ→0 for any nonzero higher-mode amplitude.

**Argument B: Ozuch subcritical scaling.** Ozuch (arXiv:2012.13316, lines 142–147) establishes the exact scaling hierarchy for the Biquard obstruction tower at an \(A_1\) point:

- If \(R^\pm\) is invertible at the node: no desingularization up to \(o(t)\) error.
- If \(\dim\ker(R^\pm)=1\): no *transverse* desingularization up to \(o(t^2)\); a one-parameter family up to \(o(t)\).
- If \(\dim\ker(R^\pm)=2\) or \(3\): transverse desingularizations up to \(o(t^2)\) form a \(\dim\ker\)-parameter family.

The first obstruction creates \(O(t)\) error in the (0,2)-form on the ALE core metric. Since \(g_t\sim t\,g_{\mathrm{ALE}}\), raising an index gives \(O(t)\cdot t^{-1}=O(1)\) operator-norm defect. This is the order-one obstruction-amplitude principle from Steps 1–3, 32, 48–50.

The k-th obstruction creates \(O(t^k)\) in the (0,2)-form, hence \(O(t^{k-1})\) in operator norm. For \(k\ge2\), this is \(O(t)\) or smaller.

Meanwhile, the near-pinched construction FND:A1construction (manuscript lines 534–577) produces metrics with dominant defect
\[
\delta(g_a)\le C|\log a|^{-1}
\]
from the log-Weyl annulus, with inner core matching error \(O(a)\) and outer Taylor error \(O(R^2)\). Since the ALE scale parameter \(t\sim a^2\) (or any fixed power of \(a\)), the higher-obstruction contribution to the operator norm is
\[
O(t^{k-1})\le O(a^{2(k-1)})\ll O(|\log a|^{-1})
\]
for all \(k\ge2\).

**Therefore:** A configuration with vanishing first obstruction and nonvanishing second (or higher) obstruction still admits near-pinched families with \(\delta\to0\). The Ricci-endomorphism pinching hypothesis cannot distinguish between "all obstructions vanish" and "only the first obstruction vanishes." No theorem based on \(\delta\to0\) alone can force the higher obstruction tower to vanish.

### Consequence for the proof architecture

The Step-70 skeleton had the form:

1. ✓ Extract orbifold limit from noncollapsed near-pinched sequence
2. ✓ First obstruction either vanishes or gives exponential neck
3. **✗ Force higher obstructions to vanish from tight pinching** ← structurally impossible
4. Use Ozuch existence/transversality to recover Einstein metric

Step 3 is unachievable by any refinement of the flux/pinching mechanism. The proof must instead proceed through one of two honest routes (§4 below).

---

## 3. Specific product hardness propagation to n≥6 (not a universal reduction)

### Theorem

Let \((\mathcal O^4,g_\mathcal O)\) be a positive Einstein 4-orbifold with \(\operatorname{Ric}=\sigma g_\mathcal O\), \(\sigma>0\), and finitely many isolated \(A_1\) points. Let \(M^4\) be the smooth resolution carrying the near-pinched family \(g_a\) from FND:A1construction with \(\delta_\sigma(g_a)\le C|\log a|^{-1}\).

For \(n\ge6\), let \(N^{n-4}=S^{n-4}\) with the round metric scaled to \(\operatorname{Ric}_{g_N}=\sigma g_N\), i.e., \(g_N=\frac{n-5}{\sigma}g_{\mathrm{round}}\).

Then the product \(M^4\times N^{n-4}\) is a closed smooth connected \(n\)-manifold, and the product metric \(g_a\times g_N\) satisfies
\[
\|\operatorname{Ric}_{g_a\times g_N}-\sigma(g_a\times g_N)\|_{\mathrm{op}}
=\max\bigl(\|\operatorname{Ric}_{g_a}-\sigma g_a\|_{\mathrm{op}},\,0\bigr)
=\delta_\sigma(g_a)\le C|\log a|^{-1}.
\]

### Proof

The Ricci tensor of a product metric is block-diagonal:
\[
\operatorname{Ric}_{g_1\times g_2}\big|_{T_pM_1\oplus T_qM_2}
=\operatorname{Ric}_{g_1}\oplus\operatorname{Ric}_{g_2}.
\]
This is because the product connection has zero mixed Christoffel symbols, hence vanishing mixed Riemann and Ricci components. The Ricci endomorphism \((\operatorname{Ric}-\sigma g)^\sharp\) is also block-diagonal, with operator norm equal to the maximum of the block norms. Since \(\operatorname{Ric}_{g_N}=\sigma g_N\) exactly, the \(N\)-block contributes zero. ∎

### Coverage

| Total dim \(n\) | Factor \(N\) | \(\dim N\) | Ric = σg? | Status |
|---|---|---|---|---|
| 5 | \(S^1\) | 1 | \(\operatorname{Ric}=0\neq\sigma\) | **Fails** |
| 6 | \(S^2\) | 2 | ✓ | ✓ |
| 7 | \(S^3\) | 3 | ✓ | ✓ |
| ≥8 | \(S^{n-4}\) | ≥4 | ✓ | ✓ |

**Gap at \(n=5\):** A one-dimensional Einstein manifold has \(\operatorname{Ric}=0\), not \(\sigma>0\). The product construction does not cover dimension 5 for the positive branch.

### Consequences and precise scope (corrected after TTCS and A03 #512)

The product construction gives near-pinched families on **specific** product manifolds \(M^4\times S^{n-4}\). It does **NOT** prove \(P_4^+\Rightarrow P_n^+\) for all \(n\ge6\), because \(P_n^+\) quantifies over ALL closed \(n\)-manifolds, not just products. An Einstein metric on \(M^4\times S^{n-4}\) need not split as a product; even if \(M^4\) has no \(\sigma\)-Einstein metric, \(M^4\times S^{n-4}\) might still carry a non-product Einstein metric.

1. **Bottleneck, not reduction:** Any proof of \(P_n^+\) for \(n\ge6\) must in particular handle the special case of product manifolds \(M^4\times N^{n-4}\), and for those the four-dimensional factor is the source of difficulty. This makes the 4D problem a **necessary ingredient** for any all-dimensional proof, but does not reduce the higher-dimensional problem to the four-dimensional one.

2. **Specific family propagation:** If the four-dimensional mixed rows \emph{do} admit Einstein metrics with constant \(\sigma\), then the corresponding products \(M^4\times S^{n-4}\) also admit Einstein metrics (the product metric), and the near-pinched families have matching defects.

3. **n=5 requires a separate device**, such as a warped product, suspension, or join construction that produces positive Einstein 5-manifolds with near-pinched input, or a direct Ricci-flow/variational argument in dimension 5.

4. **Nonexistence does not propagate automatically:** If \(M^4\) admits no \(\sigma\)-Einstein metric, it does NOT follow that \(M^4\times S^{n-4}\) admits no Einstein metric. The product propagation is a one-way existence statement, not a two-way reduction.

---

## 4. The mixed-row Einstein question as the noncollapsed P₄⁺ crux

### Hardness reduction

The manuscript's FND:A1construction (lines 534–539) states that on any fixed \(A_1\)-resolution of a positive Einstein 4-orbifold, with EH insertion directions and markings specified pointwise, there exist smooth metrics with \(\delta\to0\). Step 68 proved that the reflection \(c(z,w)=(\bar z,w)\) exchanges chiralities while preserving the Einstein obstruction data at every order. Therefore:

**FND:A1construction covers all chirality patterns** — compatible, reversed, and mixed — since the insertion direction at each node can be independently chosen.

Combined with the obstruction-amplitude argument from §2:

> **Hardness reduction.** If \(P_4^+\) holds, then for the orbifold \((S^2\times S^2)/\mathbb Z_2\) (positive Einstein, 4 isolated \(A_1\) points, \(R_\pm=\operatorname{diag}(\Lambda,0,0)\), \(\ker(R_\pm)\) two-dimensional), every \(A_1\)-resolution in every chirality pattern \(r=0,1,2,3,4\) must carry an Einstein metric.

The known case is \(r=0\): the del Pezzo \(dP_4\) surface \(\mathbb{CP}^2\#5\overline{\mathbb{CP}}^2\), which carries a Kähler–Einstein metric (Tian–Yau). The case \(r=4\) follows by orientation reversal. The **minimal open instances** are:

| Pattern | Smooth type | Properties | Einstein status |
|---|---|---|---|
| \(r=1\) | \(2\mathbb{CP}^2\#4\overline{\mathbb{CP}}^2\) | s.c., PSC, strict HT, SW-void | **OPEN** |
| \(r=2\) (spin) | \(\#_3(S^2\times S^2)\) | s.c., PSC, strict HT, SW-void, spin | **OPEN** |
| \(r=2\) (nonspin) | \(3\mathbb{CP}^2\#3\overline{\mathbb{CP}}^2\) | s.c., PSC, strict HT, SW-void | **OPEN** |
| \(r=3\) | \(4\mathbb{CP}^2\#2\overline{\mathbb{CP}}^2\) | equivalent to \(r=1\) by reflection | **OPEN** |

### Both outcomes of the obstruction computation are consequential

Since the first obstruction vanishes automatically (\(\ker(R_\pm)\) is 2-dimensional), the question reduces to the higher obstruction tower.

**(A) All higher obstructions vanish, and transversality holds.** Then Ozuch's existence theorem (combined with Step 68's TT-kernel vanishing and the four non-TT scalar modes being sliced/projected) produces exact Einstein metrics on the mixed rows. This would be the **first construction of a positive Einstein metric on a simply connected, PSC, non-Kähler, SW-void four-manifold** — the first instance of the \(P_4^+\) existence machinery.

**(B) Some higher obstruction is nonzero.** Then the local desingularization route (nearby metrics converging to this orbifold) cannot produce Einstein metrics on these manifolds. They remain the sharpest positive-branch counterexample candidates in the record, since:
- All existing obstruction tools (LeBrun/Kotschick/Ishida–LeBrun/Bauer–Furuta/simplicial-volume/entropy) are silent on this class (Step 72 obstruction catalogue).
- Only "far" metrics — Einstein metrics not in any neighborhood of this orbifold degeneration — remain unexcluded.

In case (B), a proof of \(P_4^+\) would require a **global existence mechanism** (Ricci flow, variational, or other) that does not go through nearby orbifold limits.

### The computation to execute

The finite obstruction calculation for the mixed rows requires:

1. **Multipole-to-second-jet Green transport:** For the orbifold \((S^2\times S^2)/\mathbb Z_2\) with Einstein operator \(P=\frac12\nabla^*\nabla-\mathring R\), compute the map sending a TT quadrupole source \(H^4(\zeta_i)\) at node \(p_i\) to the second jet \(H_{ij,2}\) at node \(p_j\), with singular-part subtraction and kernel projection.

2. **Four non-TT scalar directions sliced:** The full gauged \(P\)-kernel has four quotient-invariant non-TT scalar directions (from \(\ell=1\) harmonics on each \(S^2\) factor). These must be projected away or included in the Ozuch \(v\)-parameter.

3. **Reflection bug-check:** The \(c(z,w)=(\bar z,w)\) reflection proves \(r=1\) and \(r=3\) have identical obstruction systems. Any computation giving different answers has a symmetry error.

4. **Concrete target:** Does the second-order obstruction vanish for all \(\zeta\in\ker(R_\pm)\) at every node, in every mixed pattern?

---

## 5. Two honest continuations for the noncollapsed branch

The structural impossibility (§2) means the noncollapsed \(P_4^+\) proof architecture has exactly two honest routes forward. Neither has been achieved; naming them prevents downstream overcommitment.

### Route A: Tower rigidity

**Conjecture.** For every compact positive Einstein 4-orbifold \((\mathcal O,g_\mathcal O)\) with \(A_1\) singularities satisfying the Kähler–Einstein curvature condition (4) of Ozuch Theorem 0.2 — i.e., with \(\dim\ker(R_\pm)\ge2\) at every node — vanishing of the first Biquard obstruction implies vanishing of all higher obstructions.

This is a strengthening of Ozuch's Question 0.8 (originally stated for Ricci-flat/hyperkähler). If true, it would mean that first-obstruction vanishing + Ozuch transversality close the full obstruction tower, recovering an Einstein metric on the resolution. Combined with the first-obstruction vanishing at product orbifolds (where \(R_\pm=\operatorname{diag}(\Lambda,0,0)\)), it would close the noncollapsed \(P_4^+\) branch.

**Testable on the mixed rows:** The minimal concrete computation is whether the second obstruction vanishes for \(\zeta\in\ker(R_\pm)\) on \((S^2\times S^2)/\mathbb Z_2\). A positive answer would be strong evidence for tower rigidity in the product geometry; a negative answer would disprove it in this case.

### Route B: Global existence

**Problem.** Find an Einstein metric on the resolution manifold by a method that does not go through orbifold degeneration or nearby-metric analysis.

Possible approaches:
- Ricci flow starting from the near-pinched metric (but long-time existence with surgery in dimension four is not established for positive Einstein).
- Variational methods on the Einstein–Hilbert functional (but compactness and regularity under only Ricci-pinching input are the central gaps).
- Discovery of a hidden algebraic or Kähler-like structure on the mixed rows (but adjunction and Taubes exclude Kähler/symplectic in both orientations).
- A new PSC-compatible Einstein-existence invariant (which would simultaneously refute the positive branch if it goes the other way).

No current technique produces positive Einstein metrics on these topologies.

---

## 6. Summary of architectural changes

| Component | Old status | New status |
|---|---|---|
| Higher-mode (ℓ>2) flux necessity | Planned as next theorem | **Structurally impossible** for unweighted C⁰ pinching |
| Step-70 skeleton step 3 | Open gap | **Unachievable premise** |
| Mixed-row obstruction | Bounded laboratory | **Crux of noncollapsed P₄⁺** |
| Product dimension propagation | Not considered | **specific near-pinched product families propagate to n≥6**; this is a bottleneck/family test, not a proof that \(P_4^+\Rightarrow P_n^+\) |
| n=5 | Uncovered | **Needs separate device** |
| Honest continuations | Multiple vague gaps | **Two named routes**: tower rigidity or global existence |

## 7. Files

- This note: `workspace/notes/step74_ell_classification_tower_impossibility_and_hardness_propagation.md`
- Propagation data: `workspace/data/step74_product_propagation.json`
- Propagation script: `workspace/scripts/step74_product_propagation.py`
- Source references: FND:flux (manuscript lines 891–907), FND:A1construction (lines 534–577), Ozuch arXiv:2012.13316 lines 100–154 and 340–370
- Step 68 reflection proof: `workspace/notes/step68_spectral_symmetry_and_multipole_gate.md`
- Step 73 ℓ-classification plan v2: `workspace/plans/step73_general_higher_flux_necessity_plan.md`
- TTCS scaling correction: `trace/ttcs/results/step73_ttcs01_verifier1_integration.md`

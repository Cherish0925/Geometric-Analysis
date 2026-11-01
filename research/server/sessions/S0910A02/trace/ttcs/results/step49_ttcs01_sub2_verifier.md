# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step49_positive_branch_wall_and_operator_norm.md",
    "Sessions/S0910A02/workspace/data/step49_operator_norm_and_enumeration.json",
    "Sessions/S0910A02/workspace/notes/step48_H4dual_and_biKahler_realizability.md",
    "Sessions/S0910A02/workspace/notes/step45_preceptor_review_biKahler_loophole.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md"
  ]
}
```

## Task

Verify the Step 49 correction for the Yau-26 positive noncollapsed route. Read the Step 49 note and supporting data/sources. Check: (i) whether the scaling from MV/Ozuch refined estimates really shows that after the first obstruction term t*lambda*o is killed, the glued approximate metrics have ||Ric-Lambda g||_op = O(t^{1/2}) on the four-dimensional EH/Calabi replacement, while second/higher obstruction residuals are invisible to C^0 operator pinching; (ii) whether the H4_dual compactness obstruction must be formulated as the normalized boundary flux B/t_i^2 with quantitative two-scale matching, not the unnormalized B; (iii) whether the finite product-quotient orientation enumeration and known-Einstein/mixed-row status are stated with correct caveats. Identify any mathematical errors, hidden assumptions, or needed repairs that would change the route allocation. Do not invent external facts; if a needed source is absent, say exactly what source should be retrieved.

## Output

## Verifier memo — Step 49 positive noncollapsed correction

I read the Step 49 note, the Step 48/45 notes it revises, the JSON arithmetic, and the three source papers (Morteza–Viaclovsky Calabi, Ozuch higher-order obstructions, LeBrun–Ozuch conformally-Kähler). Below is what holds, one computation that is the crux and should be stated explicitly because it is a natural place to go wrong, and the precise repairs and source retrievals needed.

---

### (i) Operator-norm scaling: after the first obstruction is killed, the explicit refined metric is O(t^{1/2})-pinched

**This is correct, and it is corroborated directly by an existing estimate rather than only by the MV scale structure.**

The index-raising factor is right: on the bubble region \(g_t\sim t\,g_{\rm cal}\), so for a \((0,2)\)-tensor \(T\),
\(\;\|g_t^{-1}T\|_{\rm op}=t^{-1}\|g_{\rm cal}^{-1}T\|_{\rm op}\). This is exactly the relation LeBrun–Ozuch use between the pointwise \(C^0\) norm and their weighted norm ("\(\|\cdot\|_{C^0(g_i)}\le C t_i^{-1}\|\cdot\|_{\varrho_D^{-2}C^\alpha}\) because \(\varrho_D^2>t_i\)"). So the \(t^{-1}\) amplification is a genuine feature of the geometry, not an artifact.

Consequences check out region by region: with the first obstruction removed the \(g_{\rm cal}\)-norm remainder is \(O(t^2\rho^2)\); its maximum over \(\rho\le 2t^{-1/4}\) is \(O(t^{3/2})\) at the damage-zone edge, giving operator norm \(O(t^{1/2})\); the orbifold exterior is exactly Einstein. A nonzero first-obstruction term \(t\lambda\chi_t o\) is \(O(t)\) in \(g_{\rm cal}\) on the core, hence \(O(1)\) in operator norm — it is the only order that survives. A \(q\)-th obstruction enters at coefficient \(t^q\), hence \(t^{q-1}\) in operator norm, vanishing for \(q>1\). All internally consistent.

**Independent corroboration.** Ozuch Proposition 2.19 (source lines ~772–797) gives
\(\|\pi_{\tilde{\mathbf O}^\perp}\Phi_{g^D}(g^A)\|_{\varrho_D^{-2}C^\alpha}\le C|\zeta|^{3/2-\beta/4}\).
Multiplying by the \(t^{-1}\) conversion yields \(C^0\) operator norm \(O(t^{1/2-\beta/4})\). This is Ozuch's own bound on the component orthogonal to the obstruction space, and it reproduces the Step 49 exponent. The remaining pieces of the full defect are the obstruction components: the bubble obstruction \(o_{j,k}\) with coefficient \(t^2\mu\) gives operator norm \(t^{-1}\cdot t^2=O(t)\); the orbifold obstruction \(\sum_l\nu_l v_l\) lives where \(g^A\sim g_o\) (no \(t^{-1}\) amplification) and \(\nu_l\propto|\zeta|^2\), so it contributes only \(O(t^2)\). Summing, the total \(\|\operatorname{Ric}_{g^A}-\Lambda g^A\|_{\rm op}\to0\) at rate \(t^{1/2-\beta/4}\).

**The one computation that must be stated, because it is where the argument looks paradoxical.** The manifold is built from Ricci-**flat** Eguchi–Hanson pieces glued to a **positive**-Einstein orbifold. A naive reading says: on the deep core \(g_t=t\,g_{\rm cal}\) is Ricci-flat, so \(\operatorname{Ric}_{g_t}-\Lambda g_t=-\Lambda g_t\), whose operator norm is \(\Lambda=O(1)\), and pinching is destroyed. The resolution is that the refined metric is \(g_t=t(g_{\rm cal}+t h)\), where \(h\) solves \(P_{g_{\rm cal}}h=\Lambda g_{\rm cal}+\lambda o\). By scale-invariance of Ricci, \(\operatorname{Ric}(g_t)=\operatorname{Ric}(h_t)=t\Lambda h_t+t\lambda o+O(t^2\rho^2)\), so
\[
\operatorname{Ric}(g_t)-\Lambda g_t = t\lambda o+O(t^2\rho^2),
\]
the \(t\Lambda h_t\) terms cancelling exactly. The linear correction \(th\) is precisely what supplies the positive Ricci curvature that the flat bubble lacks. This cancellation is the entire content of "explicit glued metrics are already near-Einstein," and it should be written into the Step 49 note, since without it the reader cannot see why a flat-bubble construction can be \(\Lambda\)-pinched.

**Two things to repair, neither changing the conclusion.**
1. *Source precision.* MV Lemma 4.1/4.2 (the lines 456–514 anchor) is the Calabi metric with \(\Gamma_n\subset SU(n)\), \(n\ge 3\). The four-dimensional \(A_1\)/Eguchi–Hanson object is \(n=2\), which is Biquard's case; MV explicitly note \(n=2\) differs (rotational parameters exist, the obstruction becomes vectorial, and the deformation space is 3-dimensional not 1-dimensional). The scale structure \(t^2\rho^{2-k}\) coincides, but the load-bearing estimate should be cited from the four-dimensional statement — Ozuch Prop 2.19 (present) or Biquard 2013 §14 (not in the supplied files) — not from the \(n\ge3\) Calabi lemma. This is a citation slip, not a mathematical error.
2. *Exponent.* The honest rate from Ozuch is \(O(t^{1/2-\beta/4})\), with \(\beta>0\) arbitrarily small. The clean "\(O(t^{1/2})\)" should carry the \(\beta\)-loss.

**One assumption to state.** The argument that "the first obstruction is the complete local \(C^0\) story" tacitly uses that the orbifold-deformation obstructions \(\nu_l\) do not threaten pinching. They do not, because \(\nu_l\propto|\zeta|^2\) and act in the un-rescaled region — but this is a separate fact from "killing \(\lambda\)," and should be recorded, together with whether \((S^2\times S^2)\) has any infinitesimal Einstein deformations \(\mathbf O(\mathbf g_o)\) at all (if it is rigid, the \(\nu_l\) issue is empty).

**Net for (i):** correct, unconditional (the construction does not use the unproved compactness lemma), and the produced sequence genuinely satisfies Yau–26's two-sided pinching for any fixed dimension-only \(c_4<1<C_4\).

---

### (ii) H4_dual must be the normalized flux \(t_i^{-2}\mathcal B_k\); the unnormalized version reads nothing

**The correction is right, and the reformulation is the correct one.**

In the bubble frame \(\tilde g_i=t_i^{-2}g_i=\mathbf{eh}+h_i\), the ambient quadratic signal is \(h_i\sim t_i^2H_2\): pulling back \(g_o=\mathbf e+H_2+\cdots\) under \(\phi_{\sqrt s}\) with \(s=t_i^2\) gives \(s^{-1}\phi^*g_o=g_{\rm euc}+sH_2+\cdots\), so \(h_i\sim t_i^2H_2\). Because \(\mathcal B_k\) is linear in \(h_i\), the unnormalized limit \(\lim_i\mathcal B_k(R,i)=0\) is forced by \(h_i\to0\) and carries no curvature. Step 48's chain ("\(\mathcal B_k(R,\infty)=0\), then equate to the Ozuch coefficient \(c\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\rangle\)") is therefore self-contradictory: it proves \(0=0\) and then identifies \(0\) with a generally nonzero curvature pairing. Step 49's replacement by \(t_i^{-2}\mathcal B_k\) removes the contradiction: the normalized flux has a finite nonzero limit set by \(H_2\), i.e. by \(R_\varepsilon(p)\).

The error accounting is consistent in the bubble frame. Ricci scale-invariance gives, for the defect \(E_i=\operatorname{Ric}(g_i)-\Lambda g_i\), \(|E_i|_{\tilde g}=t_i^2|E_i|_{g_i}\le t_i^2\delta_i\); with \(o_k\sim\rho^{-4}\) the flux is \(\tilde\Phi_k^i(R)=O(t_i^2\delta_i\ln R)\), so \(t_i^{-2}\tilde\Phi_k^i=O(\delta_i\ln R)\to0\) at fixed \(R\); the nonlinear term \(\|h_i\|^2\sim t_i^4\) normalizes to \(O(t_i^2)\). All consistent with Step 49 §5.

**The genuine open object is correctly identified.** What must be newly proved is that \(t_i^{-2}h_i\) converges, on fixed neck annuli \(\rho\sim R\), to the field driven by the limit orbifold's \(H_2\), so that \(\lim_R\lim_i t_i^{-2}\mathcal B_k=c\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\rangle\). Cheeger–Naber \(C^{1,\alpha}_{\rm loc}\) gives only \(h_i\to0\); it does not deliver the \(t_i^2R^2\)-scale expansion. Under exact Einstein this is Ozuch's weighted-Hölder approximation, which uses the elliptic equation \(\Phi=0\) essentially; the \(C^0\)-pinched analogue is not available in the supplied sources and is where the compactness direction stands or does not stand. Step 49 states this as an unproved lemma rather than asserting it — appropriately.

**Net for (ii):** correct, and the normalized-flux/two-scale formulation is the one that could in principle carry the vector condition \(R_\varepsilon(p)\zeta=0\). The compactness direction remains contingent on this lemma.

---

### (iii) Product-quotient enumeration and Einstein-existence status

**Arithmetic verified.** For the diagonal half-turn \((a,a)\) on \(S^2\times S^2\): each \(a\) has 2 fixed points, so 4 fixed points, and the differential at each is \(-I_4\), i.e. \(-I_2\in SU(2)\) on \(\mathbb C^2\), giving four \(A_1\) points — correct. Resolution: \(\chi=4+4\cdot1=8\); the invariant \(H^2\) is the hyperbolic \(H\) (both factor classes preserved by the orientation-preserving \(a\)), signature 0, so \(\tau=2r-4\), \(b_2=6\), \((b_+,b_-)=(1+r,5-r)\), \(2\chi+3\tau=4+6r\). These match the JSON exactly. The additive splitting of the intersection form is legitimate because the exceptional \((-2)\)-cycles are localized and orthogonal to the orbifold cycles.

**Del Pezzo identification correct.** \(r=0\) gives \((b_+,b_-)=(1,5)\), \(\chi=8\), \(\tau=-4\), \(c_1^2=2\chi+3\tau=4\) — this is \(\mathbb{CP}^2\#5\overline{\mathbb{CP}^2}\), the degree-4 del Pezzo, which does carry a Kähler–Einstein metric. So the smooth manifold admits a positive Einstein metric, and the row is harmless for Yau–26 regardless of the input metric. \(r=4\) is its orientation reversal, likewise harmless. The reasoning that only the smooth diffeotype's Einstein existence matters (output metric unrelated to input) is right.

**Reservations stated correctly.** Mixed rows \(r=1,2,3\) have \(b_+\ge2\), hence are not del Pezzo; by LeBrun–Ozuch Theorem 4.1 an admissible (all-ASD-bubble) Hermitian-limit sequence forces \(b_+=1\), so these mixed manifolds are not reachable by admissible sequences — consistent. The balanced \(r=2\) case is \(3H\) only if the form is even/spin, which is not established (the naive spin argument would make the nonzero-signature rows spin too, contradicting Rokhlin — this point in Step 45 §2.1 is right). Freedman gives homeomorphism, not diffeomorphism; exotic structures exist; the exact smooth type of mixed rows is unknown. Einstein existence on \(\#_3(S^2\times S^2)\) is genuinely open (strict Hitchin–Thorpe \(2\chi-3|\tau|=16>0\) holds, no known obstruction, no known metric). All stated as such.

**Two points to sharpen.**
1. The \(V_4\) six-\(A_1\) model is Step 49's own extension and is marked as needing validation — appropriate. Note also that LeBrun–Ozuch's "\(k\ne2,4\)" remark (source line ~130) concerns **cyclic** \(\mathbb Z_k\) diagonal rotation; the special \(k=4\) there is cyclic \(\mathbb Z_4\), not the Klein four \(V_4\) used in Step 49. The "only \(C_2\) and \(V_4\)" statement is Step 49's own \(m\mid2\) computation, consistent with but not identical to the cited remark, and its six-fixed-point count for \((\mathbb Z_2)^2\) is unverified in the supplied material.
2. The \(m\mid2\) endpoint-weight test as written ("both \((1,a)\) and \((1,-a)\) ADE") should be spelled out: an \(A\)-type \(\mathbb C^2/\mathbb Z_m\) needs \(1+a\equiv0\pmod m\); requiring the reversed-orientation weight \((1,-a)\) also to be \(SU(2)\)-type forces \(2\equiv0\pmod m\). The conclusion is sound; the framing "both orientations" deserves one explicit sentence so it is not read as a single-orientation condition.

---

### Effect on route allocation

Nothing found changes the allocation, and the allocation is sound. The decisive, reliable output is the **construction direction**, which is unconditional: at the bi-Kähler locus \(R_+=R_-=\operatorname{diag}(\Lambda,0,0)\) both chiralities have a 2-dimensional kernel, so for each orientation assignment there are EH parameters \(\zeta^\pm\in\ker R_\pm\) killing the vector first obstruction, and (i) then gives an explicit fixed-manifold sequence with \(\|\operatorname{Ric}-\Lambda g\|_{\rm op}=O(t^{1/2-})\to0\). This produces bona fide Yau–26 pinched-input families on definite smooth 4-manifolds, independent of the unproved compactness lemma. Because a single \(C^0\)-pinched metric with pinching approaching \([1,1]\) satisfies any fixed dimension-only interval, such a manifold refutes the \(n=4\) proposition **iff** it admits no Einstein metric of any sign. Hence the genuine unknown of this branch is Einstein existence/nonexistence on the mixed-chirality resolutions, exactly as Step 49 states; higher obstructions are not decisive for pinching, and the second-order vanishing \(\mu_1=0\) at the bi-Kähler locus (Step 48 §2.2, computed correctly: the residual \(2\times2\) block has eigenvalues \((\Lambda,0)\), determinant 0) is not load-bearing.

### Sources to retrieve to close the remaining unknowns

- **Four-dimensional pointwise estimate for (i):** Biquard, *Désingularisation de métriques d'Einstein I* (Invent. Math. 192, 2013), §14 — the \(n=2\)/EH analogue of MV Lemma 4.1/4.2, to replace the \(n\ge3\) Calabi citation with the correct-dimension statement. (The weighted-norm form is already present via Ozuch Prop 2.19.)
- **Feasibility of the two-scale flux lemma for (ii):** Ozuch, *Noncollapsed degeneration of Einstein 4-manifolds II* (Geom. Topol. 26, 2022) and the Ozuch thesis, for the exact weighted-Hölder approximation statement and whether it uses \(\Phi=0\) essentially; and Cheeger–Naber (Ann. Math. 182, 2015) for the precise \(C^{1,\alpha}\) statement, to confirm it does not supply the \(t_i^2R^2\)-scale rate. These pin down exactly what a \(C^0\)-pinched replacement must prove.
- **Einstein existence/nonexistence for the mixed rows:** literature on Einstein metrics and obstructions for simply-connected 4-manifolds with \(b_+\ge2\), specifically \(\#_k(S^2\times S^2)\) (LeBrun-type curvature obstructions, Gromov simplicial-volume bounds), to determine whether any mixed resolution is a decidable target.
- **Diffeotype of mixed rows and the \(V_4\) model:** an equivariant/toric resolution or Kirby-calculus computation for the \((S^2\times S^2)/\mathbb Z_2\) mixed resolutions and the \((\mathbb Z_2)^2\) action, plus spin/parity of the resulting form — no single source; this is a computation to be carried out.
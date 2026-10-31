# Route map (updated through Step 66)

Session: S0910A03. Phase: Explore.

## 1. Strategic picture

Yau 26 has been reduced to two independent single-sign questions. The negative
branch is the active front. Sectional-pinching counterexamples are closed
(Anderson 2003, flagged). The problem is irreducibly about Ricci-level pinching
with unbounded sectional/Weyl curvature—collapse.

## 2. Negative branch routes

| Route | Status | Blocking gap | Owner |
|-------|--------|--------------|-------|
| IL Seiberg–Witten (n=4) | 8/8 modules established | Per-datum existence (Step 56, regularization-uniform estimates to named parabolic theorem) | A01/A03 |
| Graph-manifold gap (n=4) | Model class CLOSED (Step 66) | Non-warped collars, general metrics, entropy/CSS stability | A03 |
| Higher-dim counterexample | Speculative | \(\mu_5\) open (monitored); first interesting KK case \(n=6\) | A03 |
| Orbifold desingularization | Weakened | Smooth resolution may admit unrelated Einstein | A02 |

## 3. Graph-manifold program status (Step 66 update)

The curved-slice collar fork is **closed negatively** in the model class:

- **Flat-slice barrier** (Step 63, PROVED): \(H^2 \ge 9 - 6\delta\) for
  \(g = dr^2 + G(r)\) with flat \(T^3\) slices. No collar with \(\delta < 3/2\).
- **Curved-slice obstruction** (Step 66, CONFIRMED numerically): when slices
  leave the flat class, \(E_{\tan} \sim 0\) forces
  \(\operatorname{Ric}_\gamma \sim -3\gamma\) where dynamic terms are small,
  impossible on \(T^3\) (Preissmann). Full 4D Ricci optimization confirms:
  the optimizer cannot activate the curved-slice channel without increasing
  the defect.
- **Two-pronged obstruction** closes doubly-warped collars on \(T^3 \times I\).
- **Lemma J gate lifted** (not needed for model-class Conjecture F).
- **Remaining open:** non-warped collars (twist, off-diagonal), general metrics,
  entropy/CSS quantitative stability.

## 4. The slice-defect cascade (corrected in Step 65)

- \(\mu_2=1\) (Gauss–Bonnet); \(\mu_3\ge2/3\) (Preissmann);
  \(\mu_4\ge3(\sqrt3-1)/2\approx1.098\) (Chern–Gauss–Bonnet).
- Open from \(m=5\); adjacent to negative-Einstein-on-tori. **Monitor, do not attack.**
- Cheap absolute gap class: \(2\chi \le 3|\tau|\) excluded from tight pinching
  of either sign.

## 5. KK rank analysis

First interesting KK case is \(n=6\); \(n=5\) candidates fail rank obstruction
or land on nil/solvmanifolds.

## 6. Positive branch

No counterexample known. A02's chi=8 balanced rows remain the active front.
A02's Einstein-DeTurck/variational search on \(\#_3(S^2 \times S^2)\) is the
right next arc. If the negative branch holds broadly (as Step 66 suggests),
the positive branch is the only viable counterexample territory in \(n=4\).

## 7. Immediate actions

1. **A01/A03 (IL module):** connect Step 56's regularization-uniform estimates
   to a named parabolic existence theorem for the doubly-regularized
   \((\varepsilon,\nu)\) system. This is the sole conditional input for the
   restricted gap theorem.
2. **A02:** continue Einstein-DeTurck/variational search on
   \(\#_3(S^2 \times S^2)\); solve the coupled Lichnerowicz ODE system
   (bolt regularity + ambient-H matching).
3. **A03:** assess whether non-warped collars (twist, off-diagonal \(G(r)\))
   can evade the two-pronged obstruction; if not, the graph-manifold gap
   theorem reduces to the entropy/CSS stability program.
4. **All:** verify Anderson's preprint status independently before
   load-bearing use.

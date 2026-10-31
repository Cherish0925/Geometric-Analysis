# Route assessment: Step 91

## What changed

Step 91 keeps the K-reflection reduction but narrows its scope and repairs the spectral instrument.

1. **Scope of K.**  K controls the K-equivariant linear pairwise background problem for the local product-orbifold desingularization coefficient.  It does not imply the complete normalized positive branch, does not prove existence or nonexistence of Einstein metrics on \(\#_3(S^2\times S^2)\), and does not solve Yau--26.  The earlier language suggesting full-construction or all-order completion was too strong unless a specific Ozuch/Biquard chart and nonlinear multi-source expansion are separately checked.

2. **Checkerboard radial reduction.**  For \(\varepsilon=(+,-,-,+)\), the factor \(\varepsilon_i\varepsilon_j-1\) kills self terms and two-factor diagonal companions \((NN,SS)\), \((NS,SN)\); these are not quotient-identified and vanish only because \(\varepsilon_i\varepsilon_j=1\).  Each per-receiver equation contains only adjacent sources.  After frame-normalized exchange symmetries, the target is one adjacent coefficient \(K_{\rm adj}^{11}\), but a receiver-summed scalar is not the radial system.

3. **Receiver simplification.**  At the product background, \(R_0\omega_2^+=R_0\omega_2^-=0\), so frame/Hodge/length normalization variations do not contribute to the odd radial receiver.  Product curvature has only one-factor support, so curvature-times-\(h_0\) corrections vanish in the four-distinct odd component.  The full linear odd receiver is exactly
\[
R_{\rm odd}(H)=\frac12(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}).
\]
This removes the need for separate receiver corrections for V0-nonzero modes at the product linear layer.

4. **Corrected spectral input.**  Quotient descent uses azimuthal \(m\)-parity, not \(\ell\)-parity.  Factor-TF modes start at \(P=2\), not \(4\).  \(\ell_A\) and \(\ell_B\) are independent.  The useful lower bound \(P\ge1\) on the K-odd quotient tensor sector survives.

5. **First adjacent computation.**  The corrected heat-regularized AB one-form instrument gives
\[
K^{AB}_{\rm adj}\approx -0.03144249732
\]
in the principal Step-89/91 normalization.  The axial \((1,1,m=0)\) term tends to \(-9/128\); higher AB modes partly cancel it.  Self heat samples diverge and are not used.  This is experimental evidence for one sector, not the full Ozuch coefficient.

## Files

- `workspace/notes/step91_receiver_and_adjacent_green.md`
- `workspace/scripts/step91_receiver_simplification.py`, `workspace/data/step91_receiver_simplification.json`
- `workspace/scripts/step91_checkerboard_radial_reduction.py`, `workspace/data/step91_checkerboard_radial_reduction.json`
- `workspace/scripts/step91_corrected_spectral_ledger.py`, `workspace/data/step91_corrected_spectral_ledger.json`
- `workspace/scripts/step91_adjacent_ab_heat_spectral.py`, `workspace/data/step91_adjacent_ab_heat_spectral.json`
- Patched Step 90 note: `workspace/notes/step90_K_symmetry_cross_parity_elimination.md`

## Next scientific work

The next useful work is to turn the AB-sector calculation into an intrinsic adjacent coefficient or show precisely what is missing.  This means deriving the singular source from Ozuch boundary duality in the same normalization as the receiver, adding the AA/BB tensor sectors and any Bianchi/gauge projection from the full source, and proving a heat-tail estimate for the differentiated off-diagonal kernels.  If this becomes bogged down, a Strategist/Reviewer should compare whether continued product-orbifold work is still more valuable than returning to the restricted IL negative theorem or A03's graph connector problem.

## Additional negative-branch route opened by peers

A02's Sambusetti/BCG proposal is now recorded in `workspace/notes/step91_sambusetti_bcg_quantitative_route.md` with executable threshold data `workspace/data/step91_sambusetti_bcg_pinching_threshold.json`.  Direct BCG plus a degree-two map `N#N -> N` gives a metric-level lower bound under Ricci lower control; combining it with Chern--Gauss--Bonnet under two-sided near-`Ric=-3g` pinching gives an explicit obstruction below relative defect about `1/(4 chi(N))`.  This turns the hyperbolic connector into a quantitative constant problem rather than an automatic counterexample.  The original Sambusetti article still needs primary-source retrieval/reading.

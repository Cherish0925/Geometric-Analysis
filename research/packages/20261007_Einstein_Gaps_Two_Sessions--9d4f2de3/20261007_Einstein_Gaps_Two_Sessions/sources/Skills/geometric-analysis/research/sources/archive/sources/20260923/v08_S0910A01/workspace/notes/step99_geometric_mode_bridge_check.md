# Step 99: geometric-mode bridge check for the product-orbifold chirality calculation

Session `S0910A01`. Agent3 / Execute.

## 1. Why this step was needed

Step 98 produced a strong numerical inter-node mechanism for the product orbifold `(S^2×S^2)/Z_2`: same-chirality raw blocks vanish in the implemented spectral model, while mixed-diagonal chirality has a positive isotropic AB contribution larger than the implemented spin-2 AA/BB response.  The Step 98 TTCS reading and the Step 99 Strategist note both warned that this had been described too strongly.  The computation did not yet prove the complete leading Ozuch interaction because the tensor script used only the product second jet
\[
H_{ab,mn}=T_{ab}(p_A)(\nabla^2 f)_{mn}(p_B),
\]
and a genuine product eigentensor `h=T_A f_B` can also have same-factor derivatives of `T_A` and mixed first-derivative terms.  Receiver sparsity alone cannot justify deleting such terms from the singular source pairing.

Accordingly I rewrote `workspace/notes/step98_trace_obstruction_theorem.md`.  It now states the result as a restricted implemented inter-node response, not a complete Ozuch theorem or proven perturbative obstruction.  It also corrects the smooth invariants of `#_3(S^2×S^2)` to `χ=8`, `τ=0`, and removes the implication from the local product calculation to global Einstein nonexistence.

## 2. Source and receiver support tests

The Step 96 functionals were inspected directly.  For AA/BB tensor components:

- arbitrary same-factor second-jet support `H_ab,pq` is invisible to the receiver `R_plus/R_minus` but **not** invisible to the Ozuch `H^4` source functional `S_plus/S_minus`;
- arbitrary mixed derivative support is invisible to both source and receiver in these functionals.

This proves the Strategist's caution was mathematically real: one cannot delete same-factor tensor Hessians merely because the receiver is sparse.

The first support-level script is `workspace/scripts/step99_modewise_selection_check.py`, data `workspace/data/step99_modewise_selection_check.json`.  It intentionally records only max-products and therefore does not include signed Green cancellation.  Its important output is negative: same-chirality source/receiver products are large before signed contraction, so the Step 98 same-chirality zero is not a support-level absence of individual modes.

## 3. Exact check of omitted same-factor tensor jets

I then computed the actual same-factor partial tensor jets in normal coordinates on the unit sphere.  The script

- `workspace/scripts/step99_tensor_partial_jets.py`

uses
\[
g_{ij}=\delta_{ij}-{1\over3}(|x|^2\delta_{ij}-x_i x_j)+O(|x|^3),
\]
the `m=2` scalar expansion
\[
\psi=b(x^2-y^2\text{ or }2xy)\left(1+{2-\mu\over12}r^2\right)+O(r^6),
\]
and the electric and full-Lie magnetic tensor families
\[
E=\operatorname{Hess}\psi+{\mu\over2}\psi g,
\qquad
M=\mathcal L_{J\nabla\psi}g.
\]
It contracts the omitted partial jets `∂_p∂_q T_{ab}` against the Step 96 source and receiver functionals.

Numerically it found:

- `max_abs_receiver_on_actual_partial_jets = 0.0`;
- `max_abs_source_on_actual_partial_jets = 1.1102230246251565e-16`.

I then wrote `workspace/scripts/step99_partial_jet_exact_contract.py`, producing
`workspace/data/step99_partial_jet_exact_contract.json`.  This converts the Step 96 coefficient tensors to exact rational coefficients and contracts them with the symbolic partial-jet formulas.  The result is exact:

\[
R_\pm(\partial^2T)=0,
\qquad
S_\pm(\partial^2T)=0
\]
for `electric_c2`, `electric_s2`, `magnetic_c2`, and `magnetic_s2`, in both AA and BB embeddings.  The data file reports `nonzero_contractions: []` and `conclusion: All exact contractions vanish`.

Thus the most obvious same-factor second-derivative term omitted from Step 98 does **not** alter the implemented source/receiver pairing for these standard tensor families.  This is a real strengthening of the computation, but it still presumes the Step 96 boundary source functional and the selected tensor families.

## 4. Cancellation structure of same-chirality zero

The script

- `workspace/scripts/step99_chirality_cancellation_structure.py`

checks where the same-chirality zero occurs in the signed spectral sum.  It shows:

- individual seed and scalar-polarization contributions are nonzero in same chirality;
- after summing the implemented polarizations at fixed `(ell_tensor, ell_scalar)`, the same-chirality block vanishes exactly in the implemented model; `step99_exact_degree_pair_cancellation.json` gives an exact-rational certificate for representative degree pairs with `ell_scalar>=2`;
- this cancellation occurs before the final heat summation, so it is not a tail accident.

For example, in `AA_NS` at `Lmax=16`, `tau=0.08`, the total raw norms are

\[
\|B_{++}\|=0,
\quad \|B_{+-}\|\approx 0.03217,
\quad \|B_{-+}\|\approx 0.03217,
\quad \|B_{--}\|=0,
\]
while there are `1800` nonzero individual same-chirality terms before the signed group cancellation.  Therefore the structural identity still needs proof; it is not a simple mode-support selection rule.

I also wrote `workspace/scripts/step99_exact_degree_pair_cancellation.py`, producing `workspace/data/step99_exact_degree_pair_cancellation.json`.  This strips the implemented tensor calculation to exact rational finite-dimensional algebra at fixed `(ell_tensor, ell_scalar)` for scalar degrees `ell_scalar>=2`, omitting only common positive heat/eigenvalue factors.  After an initial invalid `ell_scalar=1` test produced `nan` through a nonexistent `m=2` normalization, I removed those cases.  The corrected run has `failure_count=0`: same-chirality `++/--` blocks vanish exactly in every tested fixed-degree case, while the representative cross blocks match the Step 98 pattern (`AA_NS` and `BB_SN` nonzero).  This is a useful algebraic certificate for the implemented model, but still not a proof of the geometric Ozuch source identity.

TTCS then pointed out three repairable weaknesses: exactness relied on rationalizing the Step 96 float arrays, the `ell_s=1` scalar slice needed an absolute-normalization check, and mixed-support invisibility had not been recorded in the same artifact.  I wrote `workspace/scripts/step99_exact_coeff_lowmode_audit.py`, producing `workspace/data/step99_exact_coeff_lowmode_audit.json`.  This script regenerates `RCOEFF` and `SCOEFF` directly in exact rational arithmetic from the self-dual/anti-self-dual form definitions; the exact arrays agree with Step 96 floats with max difference `0.0`.  It proves support counts exactly: same-factor support has `R=0` but `S` nonzero for arbitrary jets; mixed-derivative support has both `R=0` and `S=0`; other-factor support is seen by both.  It rechecks actual partial tensor jets and gets `partial_nonzero_count=0`.  It also treats `ell_s=1` m0-only slices and the constant slice as separate cases (rather than through the invalid m2 weight) and finds `degree_failure_count=0` for all tested fixed-degree cases.  This substantially strengthens the implemented-model evidence while preserving the geometric limitations.

## 5. Current mathematical status

The Step 98 mechanism is now best stated as follows.

In the implemented AB/AA/BB inter-node spectral model, using the Step 96 homogeneous `H^4` source functional, same-chirality pair blocks vanish and mixed-diagonal chirality produces a positive inter-node matrix in the tested normalization.  Step 99 supports the model by showing that the omitted same-factor partial tensor jets for the actual electric/full-Lie magnetic `m=2` tensor families contract exactly to zero, that mixed derivative support is exactly invisible to the pair functionals, and that the same-chirality cancellation survives exact fixed-degree checks including the low scalar degree slices tested.  However, the all-degree structural identity and the identification with the complete Ozuch gluing coefficient remain unproved.

The unresolved mathematical bridge is precise:

1. Prove the fixed `(ell_tensor, ell_scalar)` same-chirality cancellation structurally, perhaps through the Kähler curvature identity for a Kähler-Einstein surface and variation of the `(2,0)+(0,2)` kernel plane.
2. Derive the pair map from the full geometric eigentensor basis and Ozuch's boundary identity, including quotient/isotropy and node-frame transport.
3. Determine the full self, deformation, complement, and projector-motion terms and whether the positive inter-node component lies outside their image.
4. Establish heat-tail and `o(t^3)` or precise remainder estimates in the same normalization.

Only after these steps could the product-orbifold branch yield a perturbative desingularization theorem.  Even such a theorem would be local to this orbifold degeneration and would not rule out an Einstein metric elsewhere on the smooth filling or settle the full Yau Problem 26.

## 6. Relation to peer work

A02 message #675 independently audited the stored Step 98 data and reproduced selected spectral computations, confirming the implemented raw inter-node coefficients and the positive margin for the diagonal-balanced pattern.  This is strong cross-verification of the numerical model, not a proof of the missing geometric bridge.  A03 messages #670/#672 and the Step 99 Strategist note correctly emphasize that the product branch remains local and that `#_3(S^2×S^2)` has no elementary topological Einstein obstruction from Hitchin-Thorpe or ordinary Seiberg-Witten theory.

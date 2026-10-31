# Step 98/99 corrected record: implemented inter-node chirality response, not a complete Ozuch theorem

Session `S0910A01`. Product-orbifold branch for Yau Problem 26.

This file supersedes the first Step 98 wording.  The computations in Step 98 are useful and reproducible, but they do **not** establish the complete leading-order Ozuch interaction and do **not** establish a perturbative obstruction theorem.  They compute the inter-node response in the spectral model actually implemented by the scripts, using the Step 96 boundary source functional and the specific AB one-form and AA/BB tensor-scalar families.  The remaining bridge to the geometric gluing problem is mathematical, not editorial.

Key files:

- `workspace/scripts/step98_full_chirality_tensor_maps.py`
- `workspace/data/step98_full_chirality_tensor_maps.json`
- `workspace/data/step96_kernel_plane_ab_map.json`
- `workspace/data/step97_tensor_odd_physical_map.json`
- Step 98 TTCS reading: `trace/ttcs/results/step98_ttcs01_verifier1_integration.md`
- Step 99 bridge checks: `workspace/data/step99_tensor_partial_jets.json`, `workspace/data/step99_partial_jet_exact_contract.json`, `workspace/data/step99_modewise_selection_check.json`, `workspace/data/step99_chirality_cancellation_structure.json`, `workspace/data/step99_exact_degree_pair_cancellation.json`, `workspace/data/step99_exact_coeff_lowmode_audit.json`

## 1. What Step 98 actually computed

The Step 98 script reconstructed raw chirality maps
\[
B_{++},\ B_{+-},\ B_{-+},\ B_{--}
\]
for the implemented AA/BB tensor-scalar heat sums.  Together with the Step 96 AB one-form data, it gives a coherent finite spectral-model response for distinct node pairs of
\[
\mathcal O=(S^2\times S^2)/\mathbb Z_2.
\]

The implemented tensor-scalar Hessian has the restricted product form
\[
H_{ab,mn}=T_{ab}(p_A)\, (\nabla^2 f)_{mn}(p_B)
\]
for AA, and the factor-exchanged form for BB.  It did not by itself derive the complete second jet of every geometric eigentensor nor prove that the Ozuch singular source equals this distributional functional for all components.  Step 99 began checking exactly this missing bridge.

## 2. Numerical structure retained from Step 98

Within the implemented model, same-chirality inter-node blocks vanish to machine precision for the tested heat ladders:
\[
B_{++}=B_{--}=0.
\]
The tensor sectors have nonzero cross-chirality spin-2 channels, while the AB sector contributes an isotropic trace channel.

Using the stored normalizations, the cross-chirality pair response at receiver `NN` has the following structure.

| Pair | Sector | trace channel | holomorphic spin-2 | anti-holomorphic spin-2 |
|------|--------|---------------|--------------------|-------------------------|
| NN←NS | AB | positive, `c0=4a≈0.12577` | 0 | 0 |
| NN←NS | AA | 0 | 0 | `≈0.00800` |
| NN←NS | BB | 0 | 0 | 0 |
| NN←SN | AB | positive, `c0=4a≈0.12577` | 0 | 0 |
| NN←SN | AA | 0 | 0 | 0 |
| NN←SN | BB | 0 | `≈0.00800` | 0 |
| NN←SS | AB | negative, `≈-0.07091` | 0 | 0 |
| NN←SS | AA/BB | 0 | 0 | 0 |

Here `a≈0.03144249732` is the AB adjacent coefficient inherited from Step 91/92/96, so a single adjacent cross-chirality physical rank-one source contributes the matrix
\[
2a\,t_j^2 I_K
\]
to the receiver block in the current convention.

For the mixed diagonal chirality pattern `(+,-,-,+)`, the two adjacent cross-chirality sources at receiver `NN` give
\[
\operatorname{tr} A^{\rm inter}_{NN}=4a(t_{NS}^2+t_{SN}^2),
\]
which at equal scales is
\[
8a\,t^2\approx 0.25154\,t^2.
\]
The earlier value `0.503 t^2` double-counted the matrix trace.

The spin-2 terms are much smaller in the implemented model.  At equal adjacent scales they are bounded by about `0.008 t^2` per adjacent source, while the isotropic eigenvalue is `2a t^2≈0.062885 t^2` per adjacent source.  Hence the **implemented inter-node relative matrix** is positive on every physical receiver direction.  This is a strong numerical mechanism, but it is not yet the full gluing equation.

## 3. Same-chirality zero is an observed cancellation, not yet a theorem

Step 99 shows that the zero is not merely support-level vanishing of individual modes.  The support-level file `workspace/data/step99_modewise_selection_check.json` records large nonzero same-chirality receiver/source products if one ignores the signed Green contraction.  The signed grouped-sum file
`workspace/data/step99_chirality_cancellation_structure.json` shows the real pattern:

- individual tensor seed and scalar-polarization contributions can be nonzero in same chirality;
- after summing the complete implemented polarizations at fixed `(ell_tensor, ell_scalar)`, the same-chirality block is exactly zero in the implemented model; `step99_exact_degree_pair_cancellation.json` gives an exact-rational certificate for representative degree pairs with `ell_scalar>=2`, and `step99_exact_coeff_lowmode_audit.json` regenerates the Step 96 coefficient arrays directly from exact form algebra and includes tested `ell_scalar=1` and constant-slice cases without the invalid m2 normalization;
- the cancellation occurs before the final heat sum, so it is more structured than numerical tail cancellation;
- no full representation-theoretic or Kähler-geometric proof has yet been written.

A promising structural explanation is the Kähler curvature identity.  On a Kähler-Einstein surface in its complex orientation, the self-dual curvature block has rank one and its kernel is the real `(2,0)+(0,2)` plane.  Along a genuine Kähler-Einstein deformation, differentiating this identity gives zero kernel-to-kernel curvature variation; movement of the kernel plane contributes nothing because the background block annihilates the plane.  If the same-chirality singular field belongs to this linearized Kähler sector, allowing the complex structure and kernel plane to move, this would explain the zero at the operator level.  Membership of the Ozuch singular field in that sector is not yet proved.

## 4. Step 99 bridge check for omitted eigentensor jets

The Step 98 tensor script used only the component `T(p) Hess(f)`.  A genuine product eigentensor `h=T_A f_B` also has possible same-factor second derivative terms `partial^2 T_A * f_B(p)` and mixed first derivative terms.  Step 99 checked these at the second-jet functional level.

The file `workspace/data/step99_tensor_partial_jets.json` records:

1. Arbitrary same-factor tensor support `H_ab,pq` is invisible to the receiver but not invisible to the Step 96 source functional.  Therefore receiver sparsity alone cannot justify deletion.
2. For the actual electric and full-Lie magnetic `m=2` tensor families on `S^2`, the same-factor partial tensor jets have zero Step 96 source and zero receiver contraction.  The numerical file records max source contraction `1.1e-16`; `workspace/data/step99_partial_jet_exact_contract.json` verifies the contractions are exactly zero as symbolic expressions in the degree parameter and pole amplitude; and `workspace/data/step99_exact_coeff_lowmode_audit.json` removes the rational-reconstruction weakness by regenerating the Step 96 coefficients exactly from the form definitions.
3. Arbitrary mixed derivative support for AA/BB components is annihilated exactly by both Step 96 source and receiver functionals, so the obvious mixed first-derivative product terms are invisible to this pairing.  The same audit records this with exact support counts.

This supports the implemented AA/BB map for the standard tensor families, but it does not prove all missing geometry is gone.  It still assumes the Step 96 H4 boundary functional, the tensor-family normalization, the quotient factors, node-frame transport, and the distributional Green identity.

## 5. Why the implemented positivity is not an Ozuch obstruction yet

The complete projected equation has more terms than the inter-node response:
\[
F_i^\varepsilon
=F_i^{\rm self}+F_i^{\rm deform,\varepsilon}
+\sum_{j\ne i}B_{ij}^{\varepsilon_i\varepsilon_j}(M_j)
+F_i^{\rm complement}+R_i.
\]
Even if the same-chirality inter-node part vanishes, known Kähler-Einstein existence in the all-same smoothing does not imply that the self term is zero or separately removable.  It only says that the complete all-same projected equation is solved along some actual gluing/deformation path, if that path is matched to this orbifold chart and normalization.

Thus the next mathematical target is not another declaration of obstruction.  It is to determine whether the positive inter-node component survives after projecting away all allowed adjustment directions.  In concrete terms, one needs:

- a structural identity for the same-chirality cancellation;
- a derivation from complete geometric eigentensors and the singular Green pairing;
- explicit node-frame transport and quotient normalization;
- self, deformation, complement, and projector-motion contributions;
- a proof that the positive direction is outside their image, or a computation showing how they can balance it;
- heat-tail and Ozuch/Biquard remainder estimates in the same normalization.

Only after this work could one state a perturbative desingularization theorem.  Even that would remain local to this product-orbifold branch and would not prove the smooth filling has no Einstein metric elsewhere in moduli space.

## 6. Relation to the full Yau-26 goal

For the mixed filling `#_3(S^2×S^2)`, the correct smooth invariants are
\[
\chi=8,\qquad \tau=0,
\]
so Hitchin-Thorpe gives no obstruction.  The manifold admits positive scalar curvature, so ordinary Seiberg-Witten invariants are not a direct positive-Einstein exclusion.  A local obstruction to this orbifold desingularization would not exclude a non-perturbative Einstein metric on the same smooth manifold.  The output Einstein constant in Yau Problem 26 is unrestricted, so the product-orbifold positive branch cannot by itself settle the original interval proposition.

The product calculation remains valuable because it exposes a sharp local mechanism and a set of testable identities.  The broader Yau-26 work still separately requires the restricted IL negative-pinching proof to be audited, the hyperbolic/graph connector question to be resolved, and a mechanism for dimensions at least five or a dimension-uniform positive theorem.

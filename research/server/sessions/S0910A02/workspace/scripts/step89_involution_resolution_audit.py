#!/usr/bin/env python3
"""
Step 89 audit helpers for the Yau-26 negative hyperbolic-orbifold route.
This is not a proof of existence of the required hyperbolic involution.  It
records elementary local-linear and topological bookkeeping used in the note.
"""
import json
from pathlib import Path
from math import sqrt

OUT = Path('Sessions/S0910A02/workspace/data/step89_involution_resolution_audit.json')
OUT.parent.mkdir(parents=True, exist_ok=True)

# Orientation-preserving order-2 linear isotropy in SO(4): eigenvalues +/-1;
# det=1 => number of -1 eigenvalues is even.  Fixed stratum dimension is the
# +1 eigenspace dimension in the tangent representation, and the corresponding
# hyperbolic fixed set is H^{plus_dim} for an elliptic isometry fixing a point.
so4_order2_types = []
for minus_dim in [0, 2, 4]:
    plus_dim = 4 - minus_dim
    if minus_dim == 0:
        kind = 'identity, not a singular stabilizer'
    elif minus_dim == 2:
        kind = 'codimension-2 fixed surface (local model R^2 x (R^2/Z2))'
    else:
        kind = 'isolated A1 point (local model R^4/{±1})'
    so4_order2_types.append({
        'minus_eigenspace_dimension': minus_dim,
        'plus_eigenspace_dimension': plus_dim,
        'determinant': (-1) ** minus_dim,
        'fixed_stratum_dimension': plus_dim,
        'kind': kind,
    })

# Quotient/resolution Euler bookkeeping for a closed hyperbolic 4-manifold N
# with orientation-preserving involution sigma and k isolated fixed points.
# chi(|N/sigma|)=(chi(N)+k)/2; orbifold chi=chi(N)/2; resolving an A1 point
# replaces a contractible cone ball by a disk bundle over S^2, increasing chi by 1.
# Equivalently chi(M)=chi_orb + 3k/2.
examples = []
for chi_N, k in [(4, 1), (100, 1), (100, 10), (72, 36)]:
    chi_underlying = (chi_N + k) / 2
    chi_orb = chi_N / 2
    chi_resolution = chi_underlying + k
    examples.append({
        'chi_N': chi_N,
        'isolated_fixed_points_k': k,
        'chi_underlying_quotient': chi_underlying,
        'chi_orbifold': chi_orb,
        'chi_resolution': chi_resolution,
        'chi_resolution_alt': chi_orb + 1.5 * k,
    })

# For N#N threshold recorded in Step 88, retain formula to compare with the
# entirely different hyperbolic-orbifold route.  It is additive in chi(N).
threshold_samples = []
for chi in [2, 10, 100, 1000]:
    eps = (1 - sqrt(1 - 1/chi)) / (1 + sqrt(1 - 1/chi))
    threshold_samples.append({
        'chi_N': chi,
        'relative_eps_threshold': eps,
        'operator_delta_threshold': 3*eps,
        'leading_operator_delta': 3/(4*chi),
    })

# Logical group quotient template for a quotient N/sigma with lift t normalizing Gamma0.
# Orbifold group is Gamma0 semidirect <t>.  Resolving a fixed point whose stabilizer
# is represented by gamma_j t kills that element.  If t itself is killed, the
# semidirect relation turns into gamma = sigma_*(gamma) (coinvariants).  Other
# fixed points impose extra gamma_j=1 relations in the coinvariant quotient.
group_template = {
    'orbifold_group': 'Gamma = Gamma0 ⋊_<sigma_*> <t | t^2=1>',
    'resolution_pi1': 'Gamma / normal_closure{ gamma_j t : gamma_j t has isolated fixed point giving a resolved A1 point }',
    'one_fixed_point_represented_by_t': 'Gamma0 / normal_closure{ gamma sigma_*(gamma)^(-1) for gamma in Gamma0 } (coinvariants)',
    'many_fixed_points_after_killing_t': 'coinvariants further quotiented by normal_closure{ gamma_j : j>1 }, where gamma_j t are the other point stabilizers',
    'rational_H1_coinvariant_dimension': 'dim H1(M;Q)=dim H1(N;Q)^{sigma_*} only before any extra gamma_j relations are considered; with many nodes these relations can kill H1 entirely',
    'negative_mirror_status': 'Step57 van Kampen proves all 36-node sign-pattern fillings are simply connected; the Step88 infinite-pi1 coinvariant-only conclusion was false.'
}

result = {
    'so4_orientation_preserving_order2_types': so4_order2_types,
    'quotient_resolution_euler_examples': examples,
    'connected_sum_bcg_threshold_samples': threshold_samples,
    'group_quotient_template': group_template,
    'route_cautions': [
        'Positive b1 of the resolution is not enough for entropy obstruction; T^4 has b1>0 but zero simplicial volume.',
        'Positive simplicial volume is still weaker than the Sambusetti/BCG certificate used here, which requires a nonzero-degree map to a closed real-hyperbolic 4-manifold with the sharp inequality violation.',
        'Amenable-boundary additivity for simplicial volume cannot be applied across compressible RP3 A1 seams without compatibility/pi1-injectivity; the outside piece may have positive relative volume while the filled resolution has zero absolute simplicial volume.',
        'The sharp existence question is a closed hyperbolic 4-manifold with an orientation-preserving isometric involution whose fixed set is nonempty finite and has no 2-dimensional components, followed by a separate degree-map/Sambusetti analysis for its A1 resolution.'
    ]
}

OUT.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(f'Saved {OUT}')
print('SO(4) order-2 types:', so4_order2_types)
print('Corrected group template:', group_template['resolution_pi1'])

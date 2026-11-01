#!/usr/bin/env python3
"""
Step 87: node-to-node partial Green response from the axial Killing-Killing
lambda=1 mode.

This uses the reliable V0=0 mode h=(*dZ_A)⊙(*dZ_B).  At all four fixed nodes
N/S on each factor this mode vanishes to first order as a one-form on each
factor, so its quadratic jet is the whole local contribution relevant to the
flat receiver curvature calculation.  Other lambda=1 coexact modes involving
*dX or *dY have nonzero constant jets at the nodes and require additional
frame/background curvature corrections before they can be added.

The output is a partial spectral contribution, not the complete Ozuch
coefficient.
"""
import json, math, os
from fractions import Fraction

nodes = {
    'NN': (+1, +1),
    'NS': (+1, -1),
    'SN': (-1, +1),
    'SS': (-1, -1),
}

# In orientation-preserving geodesic frames on each unit sphere:
# *dZ at N has the NN model sign +1; at S it has sign -1.
node_sign = {name: sA*sB for name, (sA, sB) in nodes.items()}

# From step87_missed_killing_mode_boundary.py at NN:
# B_+ - B_- = pi^2 for the unnormalized h.
source_diff_over_pi2_NN = Fraction(1, 1)

# From step87_missed_killing_mode_receiver.py at NN:
# L^+ = 1 for the unnormalized h in the script Riemann convention.
receiver_L_plus_NN = Fraction(1, 1)

# P eigenvalue and L2 norm on the quotient orbifold.
lambda_P = Fraction(1, 1)
# ||(*dZ_A)⊙(*dZ_B)||^2 over (S^2xS^2)/Z2:
# cover integral = 2*(int |dZ|^2)^2 = 2*(8pi/3)^2 = 128pi^2/9;
# quotient halves it.
norm_sq_over_pi2 = Fraction(64, 9)

matrix = {}
for recv in nodes:
    matrix[recv] = {}
    for src in nodes:
        sign = node_sign[recv] * node_sign[src]
        # coefficient difference divided by pi^2 cancels with norm pi^2.
        coeff = Fraction(sign, 1) * receiver_L_plus_NN * source_diff_over_pi2_NN / lambda_P / norm_sq_over_pi2
        matrix[recv][src] = {
            'node_sign_product': sign,
            'normalized_axial_lambda1_partial_difference': f'{coeff.numerator}/{coeff.denominator}',
            'float': float(coeff),
        }

results = {
    'scope': 'partial source-to-plus-receiver spectral response from the one-dimensional axial coexact lambda=1 channel h=(*dZ_A)⊙(*dZ_B)',
    'not_complete_coefficient': 'does not include the rest of the lambda=1 eigenspace, higher eigenspaces, negative/zero modes, gauge projection, or Ozuch normalization of radial variables',
    'node_frame_convention': 'orientation-preserving geodesic frames on each S^2 factor; *dZ sign is + at N and - at S, so h sign is product of the two factor signs',
    'node_signs': node_sign,
    'local_inputs': {
        'source_difference_at_NN': 'B_plus-B_minus = pi^2 for unnormalized h',
        'plus_receiver_at_NN': 'L_plus(h)=1 in the Step87 receiver Riemann convention',
        'lambda_P': '1',
        'norm_sq_on_quotient': '64*pi^2/9',
    },
    'partial_matrix': matrix,
    'interpretation': [
        'The axial V0=0 channel alone gives a nonzero basis-independent one-dimensional contribution: +9/64 for same node-sign pairs and -9/64 for opposite node-sign pairs, in the present provisional normalization.',
        'This demonstrates that the low-lying product resolvent contains chirality-sensitive propagation channels; cancellations, if present, must involve additional eigenspace components or the exact Ozuch receiver/source normalization rather than Step86 index matching.',
        'The node signs are a convention-sensitive transport ledger; a complete calculation must transform source multipoles, receiver zeta directions, and local frames consistently.'
    ]
}

outpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'step87_axial_killing_lambda1_partial.json')
os.makedirs(os.path.dirname(outpath), exist_ok=True)
with open(outpath, 'w') as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
print(f'Wrote {outpath}')

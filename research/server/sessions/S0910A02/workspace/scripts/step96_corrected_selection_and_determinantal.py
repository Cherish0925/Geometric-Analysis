"""
Step 96: Corrected T^2 selection rules with node-dependent sigma,
determinantal response framework, and pattern comparison.

Fixes the Step 95 error: weights are node-dependent through pole signs.
The anisotropy condition is sigma_i = sigma_j where sigma_j = eps_j * s_A^j * s_B^j.

The response map on K_j ≅ C is:
    xi_j ↦ P_j * xi_j + Q_j * conj(xi_j)
where P_j (isotropic) comes from |xi_i|^2 xi_j terms (all pairs),
and Q_j (anisotropic) comes from xi_i^2 conj(xi_j) terms (only sigma_i = sigma_j pairs).

Kernel condition: det(P*Id + Q*conj) = |P|^2 - |Q|^2 = 0, i.e. |P| = |Q|.
"""

import json
import numpy as np
from itertools import product as cartprod

# Node labels and pole signs
nodes = ['NN', 'NS', 'SN', 'SS']
pole_signs = {
    'NN': (+1, +1),
    'NS': (+1, -1),
    'SN': (-1, +1),
    'SS': (-1, -1),
}

# Chirality patterns
patterns = {
    'all_compatible': {'NN': +1, 'NS': +1, 'SN': +1, 'SS': +1},
    'diagonal_balanced': {'NN': +1, 'SS': +1, 'NS': -1, 'SN': -1},
    'adjacent_balanced_AB': {'NN': +1, 'NS': +1, 'SN': -1, 'SS': -1},  # share A-north
    'all_reversed': {'NN': -1, 'NS': -1, 'SN': -1, 'SS': -1},  # equiv to all_compatible
}

def compute_sigma(node, eps):
    """sigma_j = eps_j * s_A^j * s_B^j"""
    sA, sB = pole_signs[node]
    return eps * sA * sB

def compute_theta_str(node, eps):
    """theta_j = s_A * alpha + eps * s_B * beta as string"""
    sA, sB = pole_signs[node]
    a_coeff = sA
    b_coeff = eps * sB
    parts = []
    if a_coeff == 1: parts.append('α')
    elif a_coeff == -1: parts.append('-α')
    if b_coeff == 1: parts.append('+β')
    elif b_coeff == -1: parts.append('-β')
    return ''.join(parts)

results = {}

for pname, pdata in patterns.items():
    pat = {}
    sigma_vals = {}
    for n in nodes:
        eps = pdata[n]
        sig = compute_sigma(n, eps)
        theta = compute_theta_str(n, eps)
        sigma_vals[n] = sig
        pat[n] = {'chirality': '+' if eps > 0 else '-', 'sigma': sig, 'theta': theta}
    
    # Compute anisotropic pairs
    aniso_pairs = []
    iso_only_pairs = []
    for i, ni in enumerate(nodes):
        for j, nj in enumerate(nodes):
            if i >= j: continue
            if sigma_vals[ni] == sigma_vals[nj]:
                aniso_pairs.append(f"{ni}-{nj}")
            else:
                iso_only_pairs.append(f"{ni}-{nj}")
    
    # Per-node anisotropic neighbor count
    aniso_neighbors = {}
    for ni in nodes:
        count = sum(1 for nj in nodes if nj != ni and sigma_vals[ni] == sigma_vals[nj])
        partners = [nj for nj in nodes if nj != ni and sigma_vals[ni] == sigma_vals[nj]]
        aniso_neighbors[ni] = {'count': count, 'partners': partners}
    
    # Adjacency structure: nodes sharing exactly one pole are adjacent
    def are_adjacent(n1, n2):
        return sum(abs(a-b) for a,b in zip(pole_signs[n1], pole_signs[n2])) == 2
    
    def are_diagonal(n1, n2):
        return sum(abs(a-b) for a,b in zip(pole_signs[n1], pole_signs[n2])) == 4
    
    # Classify anisotropic pairs as adjacent or diagonal
    aniso_adj = []
    aniso_diag = []
    for pair_str in aniso_pairs:
        n1, n2 = pair_str.split('-')
        if are_adjacent(n1, n2):
            aniso_adj.append(pair_str)
        elif are_diagonal(n1, n2):
            aniso_diag.append(pair_str)
    
    pat['anisotropic_pairs'] = aniso_pairs
    pat['isotropic_only_pairs'] = iso_only_pairs
    pat['aniso_neighbor_counts'] = aniso_neighbors
    pat['aniso_adjacent'] = aniso_adj
    pat['aniso_diagonal'] = aniso_diag
    pat['total_aniso'] = len(aniso_pairs)
    pat['total_iso_only'] = len(iso_only_pairs)
    
    results[pname] = pat

# Compare all-compatible vs diagonal balanced
ac = results['all_compatible']
db = results['diagonal_balanced']
ab = results['adjacent_balanced_AB']

comparison = {
    'all_compatible_total_aniso': ac['total_aniso'],
    'diagonal_balanced_total_aniso': db['total_aniso'],
    'adjacent_balanced_total_aniso': ab['total_aniso'],
    'all_compatible_aniso_adjacent': len(ac['aniso_adjacent']),
    'all_compatible_aniso_diagonal': len(ac['aniso_diagonal']),
    'diagonal_balanced_aniso_adjacent': len(db['aniso_adjacent']),
    'diagonal_balanced_aniso_diagonal': len(db['aniso_diagonal']),
    'adjacent_balanced_aniso_adjacent': len(ab['aniso_adjacent']),
    'adjacent_balanced_aniso_diagonal': len(ab['aniso_diagonal']),
}

# Determinantal framework
determinantal = {
    'response_map': 'xi_j ↦ P_j * xi_j + Q_j * conj(xi_j)',
    'P_definition': 'P_j = sum_i c_{ji} |xi_i|^2 (isotropic, all pairs)',
    'Q_definition': 'Q_j = sum_{i: sigma_i=sigma_j} q_{ji} xi_i^2 (anisotropic, sigma-matched only)',
    'kernel_condition': 'det(P*Id + Q*conj) = |P|^2 - |Q|^2 = 0',
    'equivalent_condition': '|P| = |Q|',
    'scale_invariance': 'With equal scales t and unit norms, t cancels. The equation is scale-free at leading order.',
    'why_no_critical_scale': 'Both P and Q are homogeneous degree 2 in source norms. At equal scales the t^2 cancels from both, leaving a scale-free equation. This is the representation-theoretic reason the Step 92 critical-scale story was impossible.',
}

# r=0 calibration
r0_calibration = {
    'pattern': 'all_compatible',
    'sigma_values': {n: compute_sigma(n, patterns['all_compatible'][n]) for n in nodes},
    'anisotropic_pairs': ac['aniso_pairs'] if 'aniso_pairs' in ac else ac['anisotropic_pairs'],
    'calibration_test': 'On the r=0 KE curve, det(response) = 0 must hold: |sum_i c_{ji}| = |sum_{i: sigma_i=sigma_j} q_{ji}|. This is a sharp check on normalization and transport before any mixed number is believed.',
    'degeneracy_not_vanishing': 'The r=0 equation gives degeneracy of the response map (kernel direction exists), NOT vanishing of the response coefficients. Linear subtraction F(mixed) - F(compatible) is therefore invalid; the correct comparison is determinantal.',
    'source_grounding': 'OSS (doi:10.4310/jdg/1452002879) places the 4-A1 surface (P1xP1)/Z2 as a boundary point of the compactified KE moduli of degree-4 del Pezzo. Smooth KE metrics with bubble scale t_i → 0 exist along a GH-convergent sequence. Step 67 identifies the all-compatible chirality. At a limiting direction, the all-compatible response is degenerate. No local deformation coordinates or Spotti hypothesis needed for this calibration.',
}

# Diagonal balanced comparison
db_comparison = {
    'sigma_values': {n: compute_sigma(n, patterns['diagonal_balanced'][n]) for n in nodes},
    'key_fact': 'All sigma_j = +1 in diagonal balanced. Every pair contributes anisotropy.',
    'consequence': 'Diagonal balanced has strictly MORE anisotropic freedom (6 aniso pairs) than all-compatible (2 aniso pairs). This tilts toward solvability rather than obstruction, contrary to the tacit assumption that mixed patterns are harder.',
    'P_formula': 'P_j = c_adj1 + c_adj2 + c_diag (three neighbor terms)',
    'Q_formula': 'Q_j = q_adj1 + q_adj2 + q_diag (all three, since all sigma match)',
    'r0_comparison': {
        'P_r0': 'P_j^(r0) = c_adj1 + c_adj2 + c_diag (same terms, different pattern may give different coefficients)',
        'Q_r0': 'Q_j^(r0) = q_diag (only diagonal sigma matches in all-compatible)',
        'additional_aniso_in_mixed': 'Adjacent Q terms q_adj1, q_adj2 are present in diagonal balanced but absent in all-compatible.',
    }
}

output = {
    'purpose': 'Corrected T^2 selection rules with node-dependent sigma and determinantal response framework.',
    'correction': 'Step 95 used uniform weight w_i=(1,eps_i) for all nodes. Correct: theta_j = s_A^j alpha + eps_j s_B^j beta, so sigma_j = eps_j s_A^j s_B^j. Anisotropy condition: sigma_i = sigma_j.',
    'gate1_unaffected': 'The beta=0 subcircle gives |theta_j|=1 on every K_j regardless of pole signs. Gate 1 (no quadratic equivariant K→K map) is unchanged.',
    'patterns': results,
    'pattern_comparison': comparison,
    'determinantal_framework': determinantal,
    'r0_calibration': r0_calibration,
    'diagonal_balanced_comparison': db_comparison,
}

outpath = 'Sessions/S0910A02/workspace/data/step96_corrected_selection_determinantal.json'
with open(outpath, 'w') as f:
    json.dump(output, f, indent=2, default=str)

print(f"Saved {outpath}")
print()
print("=== PATTERN SIGMA VALUES ===")
for pname in ['all_compatible', 'diagonal_balanced', 'adjacent_balanced_AB']:
    sigmas = {n: results[pname][n]['sigma'] for n in nodes}
    aniso = results[pname]['total_aniso']
    print(f"{pname}: sigma = {sigmas}, total aniso pairs = {aniso}")
    print(f"  aniso adjacent: {results[pname]['aniso_adjacent']}")
    print(f"  aniso diagonal: {results[pname]['aniso_diagonal']}")

print()
print("=== COMPARISON ===")
for k, v in comparison.items():
    print(f"  {k}: {v}")

print()
print("=== DETERMINANTAL ===")
print(f"  Response map: {determinantal['response_map']}")
print(f"  Kernel condition: {determinantal['kernel_condition']}")
print(f"  Scale invariance: {determinantal['scale_invariance']}")

print()
print("=== r=0 CALIBRATION ===")
print(f"  Sigma: {r0_calibration['sigma_values']}")
print(f"  Aniso pairs: {r0_calibration['anisotropic_pairs']}")
print(f"  Test: {r0_calibration['calibration_test']}")

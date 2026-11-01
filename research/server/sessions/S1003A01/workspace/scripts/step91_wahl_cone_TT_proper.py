"""Step 91: Wahl cone deformation modes — proper linear algebra.

For the Ricci-flat Kahler cone C^2/Z_{n^2}(1,n-1), count anti-Hermitian
(non-Kahler) TT symmetric 2-tensor modes at each indicial root nu.

Method: enumerate Z_{n^2}-invariant harmonic (2,0)-tensor polynomials of
degree d=nu, compute the divergence operator as a matrix, find its kernel.
The kernel dimension is the number of independent TT modes.

Key formula for divergence of h = p e_{ij} (anti-Hermitian symmetric tensor
on flat C^2):
  (delta h)_1 = -2[dp/dzbar_1 if ij=11] - 2[dp/dzbar_2 if ij=12]
  (delta h)_2 = -2[dp/dzbar_1 if ij=12] - 2[dp/dzbar_2 if ij=22]

The output is a (1,0)-form, expanded in degree-(d-1) monomials.
"""

import numpy as np
from itertools import product
import json, os

def get_invariant_harmonic_basis(n, deg):
    """Get Z_{n^2}-invariant harmonic degree-d (2,0)-tensor monomials.
    
    Returns list of (a,b,c,d_exp,ttype) where monomial is z1^a zb1^b z2^c zb2^d_exp
    and ttype in {0:'dz1^2', 1:'dz1 dz2', 2:'dz2^2'}.
    """
    p = n * n
    tensor_weights = [2, n, 2*(n-1)]  # for dz1^2, dz1 dz2, dz2^2
    basis = []
    for a, b, c, d_exp in product(range(deg+1), repeat=4):
        if a + b + c + d_exp != deg:
            continue
        # Harmonic: a*b == 0 and c*d_exp == 0
        if a * b != 0 or c * d_exp != 0:
            continue
        mono_weight = (a - b + (n-1)*(c - d_exp)) % p
        for ttype in range(3):
            total = (mono_weight + tensor_weights[ttype]) % p
            if total == 0:
                basis.append((a, b, c, d_exp, ttype))
    return basis

def compute_divergence_matrix(basis, n):
    """Compute the divergence matrix for the given basis.
    
    The divergence maps degree-d tensors to degree-(d-1) (1,0)-covectors.
    Output basis: all degree-(d-1) monomials z1^a' zb1^b' z2^c' zb2^d' times
    {dz1, dz2}.
    
    Returns (matrix, output_labels).
    """
    if not basis:
        return np.zeros((0, 0)), []
    
    deg = basis[0][0] + basis[0][1] + basis[0][2] + basis[0][3]
    
    # Build output basis: degree-(deg-1) monomials times {component 1, component 2}
    # Only monomials that actually appear in the divergence
    output_monomials = set()
    for a, b, c, d_exp, ttype in basis:
        # Divergence involves d/dzbar_1 and d/dzbar_2
        if ttype == 0:  # e_{11}: delta_1 = -2 dp/dzbar_1
            if b > 0:
                output_monomials.add((a, b-1, c, d_exp, 0))  # component 1
        elif ttype == 1:  # e_{12}: delta_1 = -2 dp/dzbar_2, delta_2 = -2 dp/dzbar_1
            if d_exp > 0:
                output_monomials.add((a, b, c, d_exp-1, 0))  # component 1
            if b > 0:
                output_monomials.add((a, b-1, c, d_exp, 1))  # component 2
        elif ttype == 2:  # e_{22}: delta_2 = -2 dp/dzbar_2
            if d_exp > 0:
                output_monomials.add((a, b, c, d_exp-1, 1))  # component 2
    
    output_list = sorted(output_monomials)
    if not output_list:
        return np.zeros((0, len(basis))), []
    
    out_idx = {m: i for i, m in enumerate(output_list)}
    M = np.zeros((len(output_list), len(basis)))
    
    for j, (a, b, c, d_exp, ttype) in enumerate(basis):
        if ttype == 0:  # delta_1 = -2 dp/dzbar_1
            if b > 0:
                key = (a, b-1, c, d_exp, 0)
                if key in out_idx:
                    M[out_idx[key], j] = -2 * b
        elif ttype == 1:  # delta_1 = -2 dp/dzbar_2, delta_2 = -2 dp/dzbar_1
            if d_exp > 0:
                key = (a, b, c, d_exp-1, 0)
                if key in out_idx:
                    M[out_idx[key], j] = -2 * d_exp
            if b > 0:
                key = (a, b-1, c, d_exp, 1)
                if key in out_idx:
                    M[out_idx[key], j] = -2 * b
        elif ttype == 2:  # delta_2 = -2 dp/dzbar_2
            if d_exp > 0:
                key = (a, b, c, d_exp-1, 1)
                if key in out_idx:
                    M[out_idx[key], j] = -2 * d_exp
    
    return M, output_list

def kernel_dim(M):
    """Dimension of kernel of M."""
    if M.size == 0:
        return M.shape[1] if len(M.shape) > 1 else 0
    s = np.linalg.svd(M, compute_uv=False)
    rank = np.sum(s > 1e-10)
    return M.shape[1] - rank

def kernel_vectors(M):
    """Get kernel basis."""
    if M.size == 0 or M.shape[0] == 0:
        return np.eye(M.shape[1])
    U, s, Vh = np.linalg.svd(M, full_matrices=True)
    rank = np.sum(s > 1e-10)
    return Vh[rank:].T  # columns are kernel vectors

results = {}
ttype_names = ['dz1^2', 'dz1 dz2', 'dz2^2']

for n in range(2, 16):
    p = n * n
    res_n = {'n': n, 'singularity': f'1/{p}(1,{n-1})'}
    
    for nu in range(5):
        basis = get_invariant_harmonic_basis(n, nu)
        if not basis:
            res_n[f'nu{nu}'] = {'basis_dim': 0, 'TT_dim': 0}
            continue
        
        M, out_labels = compute_divergence_matrix(basis, n)
        kdim = kernel_dim(M) if M.size > 0 else len(basis)
        
        res_n[f'nu{nu}'] = {
            'basis_dim': len(basis),
            'div_matrix_shape': list(M.shape) if M.size > 0 else [0, len(basis)],
            'div_rank': len(basis) - kdim,
            'TT_dim': kdim
        }
        
        # Get kernel vectors for important cases
        if kdim > 0 and nu in [0, 1, 2]:
            kvecs = kernel_vectors(M) if M.size > 0 else np.eye(len(basis))
            modes = []
            for k in range(kvecs.shape[1]):
                v = kvecs[:, k]
                terms = []
                for i, (a, b, c, d_exp, tt) in enumerate(basis):
                    if abs(v[i]) > 1e-10:
                        terms.append({
                            'coeff': round(v[i], 6),
                            'monomial': f'z1^{a} zb1^{b} z2^{c} zb2^{d_exp}',
                            'tensor': ttype_names[tt]
                        })
                modes.append(terms)
            res_n[f'nu{nu}']['modes'] = modes
    
    results[n] = res_n
    
    print(f"\nn={n}, singularity 1/{p}(1,{n-1}):")
    for nu in range(5):
        r = res_n[f'nu{nu}']
        star = ' ***' if r['TT_dim'] > 0 and nu <= 2 else ''
        print(f"  nu={nu}: basis {r['basis_dim']}, TT dim = {r['TT_dim']}{star}")

print("\n\nSUMMARY: anti-Hermitian TT dimension at each indicial root")
print(f"{'n':>3} {'1/n^2':>8} {'nu=0':>6} {'nu=1':>6} {'nu=2':>6} {'nu=3':>6} {'nu=4':>6}")
for n in range(2, 16):
    r = results[n]
    vals = [r[f'nu{nu}']['TT_dim'] for nu in range(5)]
    print(f"{n:3d} {f'1/{n*n}':>8} {vals[0]:6d} {vals[1]:6d} {vals[2]:6d} {vals[3]:6d} {vals[4]:6d}")

# Check the universal mode
print("\n\nVerification: the mode h = (zb1 dz1 - zb2 dz2)^2")
print("This tensor has weight 0 under Z_{n^2}(1,n-1) for all n")
print("since zb1*dz1 and zb2*dz2 each have weight 0.")
print("It is harmonic (each monomial satisfies a*b=0, c*d=0).")
print("Divergence check:")
print("  h = zb1^2 dz1^2 - 2 zb1*zb2 dz1*dz2 + zb2^2 dz2^2")
print("  delta_1 = -2*d(zb1^2)/dzb1 - 2*d(-2*zb1*zb2)/dzb2")
print("          = -4 zb1 + 4 zb1 = 0  ✓")
print("  delta_2 = -2*d(-2*zb1*zb2)/dzb1 - 2*d(zb2^2)/dzb2")
print("          = 4 zb2 - 4 zb2 = 0  ✓")
print("TT confirmed analytically.")

here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step91')
os.makedirs(od, exist_ok=True)

# Serialize
def serialize(obj):
    if isinstance(obj, np.integer): return int(obj)
    if isinstance(obj, np.floating): return float(obj)
    if isinstance(obj, np.ndarray): return obj.tolist()
    return obj

json_out = json.loads(json.dumps(results, default=serialize))
with open(os.path.join(od, 'wahl_cone_TT_proper.json'), 'w') as f:
    json.dump(json_out, f, indent=1)
print(f"\nSaved to data/step91/wahl_cone_TT_proper.json")

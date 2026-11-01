#!/usr/bin/env python3
"""Step 38: Direct exact computation of Weyl period coefficients.

For equal-length alternating rods [0,1],[1,2],...,[m-1,m] with labels
alternating 1,2,1,2,..., compute exp(4*ell_k) for each rod using the
EXACT pairwise formula for nu on the axis, combined with the regular
part of U_i.

The ell_k coefficient combines:
  1. nu from all rod pairs (computed as a product)
  2. The geometric factor 4(z-a)(b-z) from the singular rod
  3. The regular contribution of other same-label rods

Key: adjacent rod endpoints give 0/0 in the pairwise formula, but
they cancel in the combined ell expression. We compute exp(4*ell) as
a single rational product that avoids the cancellation issue.
"""
import json, os
from fractions import Fraction

def compute_exp_4ell(m, target, L=1):
    """Compute exp(4*ell) for rod 'target' in a chain of m equal rods.
    
    Rod k spans [k*L, (k+1)*L], label = (k%2)+1.
    z = midpoint of target rod = (target + 1/2) * L.
    
    ell_target = nu(0,z) + (1/2)log(4(z-a)(b-z)) - sum_{j!=target,same_label} u_j(0,z)
    
    exp(4*ell) = exp(4*nu) * [4(z-a)(b-z)]^2 * prod_{j,same} [(z-a_j)/(z-b_j)]^{-2}
    
    where the nu product and the u_j evaluations are all rational for integer-
    spaced rods evaluated at the midpoint.
    """
    rods = [(Fraction(k), Fraction(k+1), (k%2)+1) for k in range(m)]
    a_t, b_t, label_t = rods[target]
    z = a_t + Fraction(1, 2)  # midpoint
    
    # STEP 1: Compute exp(4*nu_pairwise) for all NONADJACENT pairs.
    # For ADJACENT pairs (sharing an endpoint), the pairwise formula diverges.
    # But we compute ell = nu + geometric + other, and the divergences cancel.
    # 
    # Strategy: compute exp(4*ell) = product of all rational factors directly.
    # 
    # exp(4*nu) = prod_{i<j} (|a_i-a_j|*|b_i-b_j| / (|a_i-b_j|*|b_i-a_j|))^{eps_{ij}}
    # where eps=+1 same label, -1 different.
    #
    # exp(4*geometric) = [4*(z-a_t)*(b_t-z)]^2 = [4*(1/2)*(1/2)]^2 = 1
    #
    # exp(4*other) = prod_{j!=target, same label} [(z-a_j)/(z-b_j)]^{-2} or [(b_j-z)/(a_j-z)]^{-2}
    
    # Geometric factor for the target rod at its midpoint:
    geom = Fraction(4) * (z - a_t) * (b_t - z)  # = 4 * 1/2 * 1/2 = 1
    P_geom = geom ** 2  # = 1
    
    # Other same-label rods:
    P_other = Fraction(1)
    for j in range(m):
        if j == target: continue
        aj, bj, lj = rods[j]
        if lj != label_t: continue
        if z > bj:
            # u_j(0,z) = (1/2)log((z-bj)/(z-aj))
            # exp(-4*u_j) = ((z-aj)/(z-bj))^2
            P_other *= (z - aj) ** 2 / (z - bj) ** 2
        elif z < aj:
            # u_j(0,z) = (1/2)log((aj-z)/(bj-z))
            # exp(-4*u_j) = ((bj-z)/(aj-z))^2
            P_other *= (bj - z) ** 2 / (aj - z) ** 2
    
    # Nu pairwise product:
    # exp(4*nu) = prod_{i<j} factor^{eps}
    # where factor = |a_i-a_j|*|b_i-b_j| / (|a_i-b_j|*|b_i-a_j|)
    # 
    # Problem: for adjacent rods (b_i = a_{i+1}), |b_i - a_{i+1}| = 0.
    # Solution: the 0 factor in the denominator of one pair is cancelled by
    # a 0 factor in the numerator of another pair when combined with
    # P_other and P_geom. Let's compute the COMBINED product.
    #
    # Actually, let's be more careful. The formula for nu is:
    # nu = sum_{i<j} eps_{ij} * (1/4) * log(N_{ij}/D_{ij})
    # where N_{ij} = |a_i-a_j|*|b_i-b_j|, D_{ij} = |a_i-b_j|*|b_i-a_j|.
    #
    # For adjacent rods i, i+1: b_i = a_{i+1}, so |b_i - a_{i+1}| = 0 in D.
    # This gives log(0) in the denominator, i.e., nu = +infty contribution.
    #
    # But ell = nu + stuff, and the stuff also has log contributions that
    # cancel the infinity. We need to compute ell directly.
    #
    # Let me use a REGULARIZATION: replace the shared endpoint b_i = a_{i+1}
    # with b_i = a_{i+1} - epsilon, and take epsilon -> 0. The divergent
    # terms should cancel in ell.
    #
    # Actually, for the product formula, the zeros appear as:
    # 1. In nu: |b_i - a_{i+1}| = 0 for adjacent rods.
    # 2. In P_other: the distances (z - b_j) or (a_j - z) are nonzero for
    #    j != target with the same label.
    # 3. In P_geom: no zeros (it's just 1 at the midpoint).
    #
    # The cancellation happens because some numerator zeros match denominator zeros.
    #
    # Let me just enumerate all factors and cancel explicitly.
    
    # Collect all factors as (numerator_piece, denominator_piece) pairs
    # and cancel common factors.
    
    num_factors = []  # list of absolute-valued integers appearing in numerator
    den_factors = []  # list of absolute-valued integers appearing in denominator
    
    # From exp(4*nu):
    for i in range(m):
        for j in range(i+1, m):
            ai, bi, li = rods[i]
            aj, bj, lj = rods[j]
            eps = 1 if li == lj else -1
            # factor = N/D = |ai-aj|*|bi-bj| / (|ai-bj|*|bi-aj|)
            N1 = abs(ai - aj)
            N2 = abs(bi - bj)
            D1 = abs(ai - bj)
            D2 = abs(bi - aj)
            if eps == 1:
                num_factors.extend([N1, N2])
                den_factors.extend([D1, D2])
            else:
                num_factors.extend([D1, D2])
                den_factors.extend([N1, N2])
    
    # From exp(2*log(geom)):
    # geom = 4*(z-a_t)*(b_t-z) = 4*(1/2)*(1/2) = 1
    # geom^2 = 1, contributes nothing.
    
    # From exp(-4*sum u_j):
    for j in range(m):
        if j == target: continue
        aj, bj, lj = rods[j]
        if lj != label_t: continue
        if z > bj:
            # exp(-4*u_j) = ((z-aj)/(z-bj))^2
            num_factors.extend([abs(z - aj)] * 2)
            den_factors.extend([abs(z - bj)] * 2)
        elif z < aj:
            # exp(-4*u_j) = ((bj-z)/(aj-z))^2
            num_factors.extend([abs(bj - z)] * 2)
            den_factors.extend([abs(aj - z)] * 2)
    
    # Now compute the product, cancelling zeros
    # Convert everything to Fraction and compute
    product = Fraction(1)
    for n_f in num_factors:
        product *= Fraction(n_f)
    for d_f in den_factors:
        if d_f == 0:
            return None  # Still has uncancelled zero — need regularization
        product /= Fraction(d_f)
    
    return product

def main():
    results = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace = os.path.dirname(script_dir)
    
    for m in [4, 6, 8, 10]:
        label_1_rods = [k for k in range(m) if k % 2 == 0]
        vals = {}
        has_none = False
        for k in label_1_rods:
            v = compute_exp_4ell(m, k)
            if v is None:
                has_none = True
                vals[k] = "DIVERGENT (adjacent endpoint)"
            else:
                vals[k] = str(v)
        
        if not has_none and len(label_1_rods) >= 2:
            frac_vals = [compute_exp_4ell(m, k) for k in label_1_rods]
            ratio = max(frac_vals) / min(frac_vals)
            # exp(4*(ell_max - ell_min)) = ratio
            # exp(ell_max - ell_min) = ratio^(1/4)
            results[str(m)] = {
                "exp_4ell": vals,
                "exp_4ell_max_over_min": str(ratio),
                "exp_4ell_max_over_min_float": float(ratio),
                "note": "exp_range = ratio^(1/4)"
            }
        else:
            results[str(m)] = {
                "exp_4ell": vals,
                "status": "has divergent terms from adjacent endpoints"
            }
    
    path = os.path.join(workspace, "data", "step38_exact_ell_product.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Saved to {path}")
    for m_str, v in results.items():
        print(f"\nm={m_str}:")
        if "exp_4ell_max_over_min" in v:
            print(f"  exp(4*ell) max/min = {v['exp_4ell_max_over_min']}")
            ratio_f = v['exp_4ell_max_over_min_float']
            import math
            print(f"  exp_range = ratio^(1/4) = {ratio_f**(1/4):.10f}")
        for k, vv in v.get('exp_4ell', {}).items():
            print(f"  rod {k}: {vv}")

if __name__ == '__main__':
    main()

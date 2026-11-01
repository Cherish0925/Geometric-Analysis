# STEP 89 WARNING: superseded for normalization/interpretation. The flat identity is real, but with
# corrected convention S_odd(V2)=(pi^2/2)R_odd(H), not pi^2 R_odd. The positivity conclusion is invalid
# without full geometric source/receiver matching, negative-mode treatment, and singular self-term subtraction.
# Use step89_identity_and_spectral_support.py and step89_identity_sparse_components.py.
#!/usr/bin/env python3
"""
Step 88: Test source-receiver proportionality for RANDOM TT quadratic jets.

If the proportionality κ = π² holds for ALL TT tensors (not just specific
eigenmodes), it would be an algebraic identity rather than a spectral accident.

We generate random V₂ tensors satisfying:
  1. Symmetric in (i,j): V[i,j,p,q] = V[j,i,p,q]
  2. Symmetric in (p,q): V[i,j,p,q] = V[i,j,q,p]
  3. Trace-free: Σ_i V[i,i,p,q] = 0 for all p,q
  4. Divergence-free: Σ_j V[i,j,p,j] = 0 for all i,p
  (These are the V₀=V₁=0 TT conditions at a point.)

Then compute S_odd and R_odd and check the ratio.
"""
import numpy as np
import json, pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"

def e2f(i, j, n=4):
    M = np.zeros((n, n)); M[i,j]=1; M[j,i]=-1; return M

wp = [(e2f(0,1)+e2f(2,3))/np.sqrt(2),
      (e2f(0,2)-e2f(1,3))/np.sqrt(2),
      (e2f(0,3)+e2f(1,2))/np.sqrt(2)]
wm = [(e2f(0,1)-e2f(2,3))/np.sqrt(2),
      (e2f(0,2)+e2f(1,3))/np.sqrt(2),
      (e2f(0,3)-e2f(1,2))/np.sqrt(2)]

C = np.zeros((3,3,4,4))
for a in range(3):
    for b in range(3):
        prod = wp[a] @ wm[b]
        C[a,b] = prod + prod.T

D = np.zeros((4,4,4,4))
for k in range(3):
    D += np.einsum('ij,pq->ijpq', C[1,k], C[1,k]) - np.einsum('ij,pq->ijpq', C[k,1], C[k,1])

pi2 = np.pi**2

def compute_source_odd(V2):
    """S_odd from V₂ using D tensor."""
    return -(pi2/16) * np.einsum('ijpq,ijpq->', D, V2)

def compute_receiver_odd(V2):
    """R_odd = (δR⁺₂₂ - δR⁻₂₂)/2 from linearized Riemann."""
    # δR_{abcd} = (V_{ad,bc} + V_{bc,ad} - V_{ac,bd} - V_{bd,ac})/2
    dR = np.zeros((4,4,4,4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    dR[a,b,c,d] = 0.5*(V2[a,d,b,c]+V2[b,c,a,d]-V2[a,c,b,d]-V2[b,d,a,c])
    
    # SD/ASD blocks
    Rp22 = 0.0; Rm22 = 0.0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    Rp22 += wp[1][i,j]*dR[i,j,k,l]*wp[1][k,l]
                    Rm22 += wm[1][i,j]*dR[i,j,k,l]*wm[1][k,l]
    Rp22 /= 4; Rm22 /= 4
    return (Rp22 - Rm22) / 2

def make_random_TT_V2(rng):
    """Generate a random V₂ satisfying TT conditions at the origin with V₀=V₁=0."""
    # Start with random tensor, then project to TT
    V = rng.standard_normal((4,4,4,4))
    
    # Symmetrize in (i,j) and (p,q)
    V = (V + V.transpose(1,0,2,3)) / 2
    V = (V + V.transpose(0,1,3,2)) / 2
    
    # Project trace-free: V[i,i,p,q] = 0
    for p in range(4):
        for q in range(4):
            tr = sum(V[i,i,p,q] for i in range(4))
            for i in range(4):
                V[i,i,p,q] -= tr / 4
    
    # Re-symmetrize after trace projection
    V = (V + V.transpose(1,0,2,3)) / 2
    
    # Project divergence-free: Σ_j V[i,j,p,j] = 0 for all i,p
    # This is harder. Use iterative projection.
    for _ in range(20):
        for i in range(4):
            for p in range(4):
                div_ip = sum(V[i,j,p,j] for j in range(4))
                for j in range(4):
                    V[i,j,p,j] -= div_ip / 4
                    V[j,i,p,j] -= div_ip / 4  # maintain (i,j) symmetry
                    V[i,j,j,p] -= div_ip / 4  # maintain (p,q) symmetry
                    V[j,i,j,p] -= div_ip / 4
                V[i,i,p,i] += 3*div_ip / 4  # overcorrection fix for diagonal
        
        # Re-symmetrize
        V = (V + V.transpose(1,0,2,3)) / 2
        V = (V + V.transpose(0,1,3,2)) / 2
        
        # Re-project trace-free
        for p in range(4):
            for q in range(4):
                tr = sum(V[i,i,p,q] for i in range(4))
                for i in range(4):
                    V[i,i,p,q] -= tr / 4
        V = (V + V.transpose(1,0,2,3)) / 2
    
    return V

# Actually, the iterative projection is messy. Let me use a cleaner approach:
# directly parameterize TT tensors.

def make_TT_from_AB_oneform(alpha_A, beta_B):
    """Construct a V₂ tensor from one-form coefficients.
    
    alpha_A: 2-vector (components along directions 0,1)
    beta_B: 2-vector (components along directions 2,3)
    
    h_{ij} = alpha_i * beta_j + alpha_j * beta_i (AB mixed one-form product)
    V₂: second jet at origin where alpha = a_p x_p + ..., beta = b_q x_q + ...
    """
    V2 = np.zeros((4,4,4,4))
    # alpha_i = Σ_p a_{i,p} x_p for i=0,1 (linear terms)
    # beta_j = Σ_q b_{j,q} x_q for j=2,3 (linear terms)
    # h_{ij} = alpha_i beta_j + alpha_j beta_i
    # V₂_{ij,pq} = a_{i,p} b_{j,q} + a_{j,p} b_{i,q} (symmetric in ij)
    # But alpha only has i∈{0,1} and beta only has j∈{2,3}
    
    # a[i,p]: alpha component i, derivative direction p (i=0,1; p=0,1 only for axial)
    # But for general rotation, p can be 0,1 (A-directions)
    # b[j,q]: beta component j, derivative direction q (j=2,3; q=2,3 only for axial)
    
    # Actually, for a one-form on factor A: alpha has components in A-directions 0,1
    # and its Taylor expansion at the pole has derivative indices also in 0,1 directions.
    # For a one-form on factor B: similarly in 2,3 directions.
    # 
    # So V₂_{ij,pq} has i or j ∈ {0,1} paired with j or i ∈ {2,3}
    # and p ∈ {0,1} (from alpha derivative), q ∈ {2,3} (from beta derivative)
    
    for i in range(2):       # A tensor index
        for j in range(2,4): # B tensor index
            for p in range(2):       # A derivative index
                for q in range(2,4): # B derivative index
                    val = alpha_A[i,p] * beta_B[j-2,q-2]
                    V2[i,j,p,q] += val
                    V2[j,i,p,q] += val  # symmetrize tensor
                    V2[i,j,q,p] += val  # symmetrize derivative
                    V2[j,i,q,p] += val
    return V2

# Test with various one-form coefficients
rng = np.random.default_rng(42)

print("="*70)
print("PROPORTIONALITY TEST: random AB one-form product V₂ jets")
print("="*70)
print(f"{'Trial':>6} {'S_odd/π²':>12} {'R_odd':>12} {'ratio/π²':>12}")
print("-"*70)

ratios = []
for trial in range(20):
    # Random 2×2 coefficient matrices for the one-form linear jets
    alpha_A = rng.standard_normal((2, 2))  # component × derivative
    beta_B = rng.standard_normal((2, 2))
    
    V2 = make_TT_from_AB_oneform(alpha_A, beta_B)
    
    S = compute_source_odd(V2)
    R = compute_receiver_odd(V2)
    
    if abs(R) > 1e-12:
        ratio = S / R
        ratios.append(ratio)
        print(f"{trial:>6d} {S/pi2:>12.6f} {R:>12.6f} {ratio/pi2:>12.6f}")
    else:
        print(f"{trial:>6d} {S/pi2:>12.6f} {R:>12.6f} {'N/A':>12}")

if ratios:
    mean_r = np.mean(ratios)
    std_r = np.std(ratios)
    print(f"\nRatios: mean = {mean_r:.6f} = {mean_r/pi2:.6f} π²")
    print(f"         std  = {std_r:.2e}")
    print(f"  Expected: π² = {pi2:.6f}")
    print(f"  Match: {'YES' if std_r < 1e-10 else 'NO'} (std < 1e-10)")

# Also test with AA/BB trace tensors (these should have S_odd = R_odd = 0)
print("\n" + "="*70)
print("PROPORTIONALITY TEST: AA trace V₂ jets (expect both zero)")
print("="*70)
for trial in range(5):
    # AA trace: h = f · g_A where f is a quadratic function
    # V₂_{00,pq} = f_{pq}, V₂_{11,pq} = f_{pq}, rest zero
    f_pq = rng.standard_normal((4, 4))
    f_pq = (f_pq + f_pq.T) / 2  # symmetric
    
    V2 = np.zeros((4,4,4,4))
    for ii in range(2):  # tensor indices in A
        for p in range(4):
            for q in range(4):
                V2[ii, ii, p, q] = f_pq[p, q]
    
    S = compute_source_odd(V2)
    R = compute_receiver_odd(V2)
    print(f"  AA trace trial {trial}: S_odd/π² = {S/pi2:.2e}, R_odd = {R:.2e}")

# Test with general random symmetric tensors (not necessarily TT)
print("\n" + "="*70)
print("PROPORTIONALITY TEST: random GENERAL V₂ (NOT TT)")
print("="*70)
print(f"{'Trial':>6} {'S_odd/π²':>12} {'R_odd':>12} {'ratio/π²':>12}")
print("-"*70)
gen_ratios = []
for trial in range(20):
    V2 = rng.standard_normal((4,4,4,4))
    V2 = (V2 + V2.transpose(1,0,2,3)) / 2
    V2 = (V2 + V2.transpose(0,1,3,2)) / 2
    
    S = compute_source_odd(V2)
    R = compute_receiver_odd(V2)
    if abs(R) > 1e-12:
        ratio = S / R
        gen_ratios.append(ratio)
        print(f"{trial:>6d} {S/pi2:>12.6f} {R:>12.6f} {ratio/pi2:>12.6f}")
    else:
        print(f"{trial:>6d} {S/pi2:>12.6f} {R:>12.6f} {'N/A':>12}")

if gen_ratios:
    mean_r = np.mean(gen_ratios)
    std_r = np.std(gen_ratios)
    print(f"\nGeneral ratios: mean = {mean_r:.6f} = {mean_r/pi2:.6f} π²")
    print(f"                std  = {std_r:.2e}")
    print(f"  Universal? {'YES' if std_r < 1e-10 else 'NO - not universal for non-TT'}")

results = {
    'AB_oneform_ratios_over_pi2': [r/pi2 for r in ratios],
    'general_ratios_over_pi2': [r/pi2 for r in gen_ratios],
    'AB_oneform_std': float(np.std(ratios)) if ratios else None,
    'general_std': float(np.std(gen_ratios)) if gen_ratios else None,
}
outpath = DATA_DIR / "step88_proportionality_random_test.json"
with open(outpath, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nWrote {outpath}")

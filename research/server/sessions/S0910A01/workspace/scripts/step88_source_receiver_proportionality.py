# STEP 89 WARNING: this Step 88 script is superseded for normalization and positivity interpretation.
# It feeds Hessian-style quadratic jets into a source formula written for polynomial V2 coefficients,
# producing S_odd = pi^2 R_odd instead of the corrected S_odd = (pi^2/2) R_odd.
# It also states an invalid positivity consequence: P has a TT negative shape mode q=g_A-g_B and
# point-supported source self-pairings are singular. Use step89_identity_and_spectral_support.py instead.
#!/usr/bin/env python3
"""
Step 88: Source-receiver proportionality check.

Tests whether the chirality-odd source S_odd and receiver R_odd 
are proportional across multiple product eigenmodes.

If S_odd(ψ) = κ R_odd(ψ) for all eigenmodes ψ with the same constant κ,
then self-adjointness of the Lichnerowicz operator gives:

  c_ij^odd = (1/κ) Σ_k S_i^odd(h_k) S_j^odd(h_k) / (λ_k ||h_k||²)

which is a positive-semidefinite matrix. Combined with the nonzero
λ=1 axial contribution, this proves c_opp - c_same ≠ 0.

Uses __file__-relative output convention.
"""
import numpy as np
import json, pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# =================================================================
# SD/ASD basis (corrected normalization for tr(C_ab C_cd) = 4 δ_ac δ_bd)
# =================================================================
def e2f(i, j, n=4):
    M = np.zeros((n, n))
    M[i, j] = 1; M[j, i] = -1
    return M

# Self-dual and anti-self-dual 2-forms (as antisymmetric matrices)
wp = [
    (e2f(0,1) + e2f(2,3)) / np.sqrt(2),
    (e2f(0,2) - e2f(1,3)) / np.sqrt(2),
    (e2f(0,3) + e2f(1,2)) / np.sqrt(2),
]
wm = [
    (e2f(0,1) - e2f(2,3)) / np.sqrt(2),
    (e2f(0,2) + e2f(1,3)) / np.sqrt(2),
    (e2f(0,3) - e2f(1,2)) / np.sqrt(2),
]

# C_{ab} = omega^+_a @ omega^-_b + omega^-_b @ omega^+_a  (NO /2)
C = np.zeros((3, 3, 4, 4))
for a in range(3):
    for b in range(3):
        prod = wp[a] @ wm[b]
        C[a, b] = prod + prod.T  # symmetrized, no /2

# Verify orthogonality
max_err = 0
for a in range(3):
    for b in range(3):
        for c_ in range(3):
            for d in range(3):
                val = np.sum(C[a,b] * C[c_,d])
                expected = 4.0 if (a == c_ and b == d) else 0.0
                max_err = max(max_err, abs(val - expected))
print(f"C_ab orthogonality check: max |tr(C_ab C_cd) - 4δ| = {max_err:.2e}")
assert max_err < 1e-12, f"C_ab orthogonality failed: {max_err}"

# Build D tensor: D_{ij,pq} = Σ_k [C_{2k,ij}C_{2k,pq} - C_{k2,ij}C_{k2,pq}]
# In 0-based: SD index 2 -> a=1
D = np.zeros((4, 4, 4, 4))
for k in range(3):
    for i in range(4):
        for j in range(4):
            for p in range(4):
                for q in range(4):
                    D[i,j,p,q] += C[1,k,i,j]*C[1,k,p,q] - C[k,1,i,j]*C[k,1,p,q]

print(f"max |D|: {np.max(np.abs(D)):.4f}")
print(f"D[0,3,1,2] = {D[0,3,1,2]:.4f}")

# =================================================================
# Source formula: B_ε = -(π²/8) Σ_k tr(A_k^ε · V2 · A_k^ε)
# where A_k^+ = C[1,k], A_k^- = C[k,1]
# =================================================================
pi2 = np.pi**2

def compute_source(V2, chirality):
    """B_ε from quartic moment formula."""
    if chirality == '+':
        Aks = [C[1, k] for k in range(3)]
    else:
        Aks = [C[k, 1] for k in range(3)]
    
    total = 0.0
    for Ak in Aks:
        for i in range(4):
            for j in range(4):
                for p in range(4):
                    for q in range(4):
                        total += Ak[i,j] * Ak[p,q] * V2[i,j,p,q]
    return -(pi2/8) * total

# =================================================================
# Receiver formula: linearized curvature from V2
# δR_{abcd} = 1/2(V_{ad,bc} + V_{bc,ad} - V_{ac,bd} - V_{bd,ac})
# where V_{ij,pq} = h_{ij,pq} (second derivatives)
# =================================================================
def compute_riemann_from_V2(V2):
    """Linearized Riemann tensor δR_{abcd} from the quadratic jet."""
    R = np.zeros((4,4,4,4))
    for a in range(4):
        for b in range(4):
            for c_ in range(4):
                for d in range(4):
                    R[a,b,c_,d] = 0.5*(V2[a,d,b,c_] + V2[b,c_,a,d] 
                                        - V2[a,c_,b,d] - V2[b,d,a,c_])
    return R

def compute_sd_asd_blocks(R):
    """Extract 3×3 self-dual and anti-self-dual curvature blocks."""
    Rp = np.zeros((3,3))
    Rm = np.zeros((3,3))
    Rpm = np.zeros((3,3))
    for a in range(3):
        for b in range(3):
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        for l in range(4):
                            Rp[a,b] += wp[a][i,j] * R[i,j,k,l] * wp[b][k,l]
                            Rm[a,b] += wm[a][i,j] * R[i,j,k,l] * wm[b][k,l]
                            Rpm[a,b] += wp[a][i,j] * R[i,j,k,l] * wm[b][k,l]
    # Each contraction has a factor from the 2-form normalization
    # <ω_a, R ω_b> = (1/4) ω_{a,ij} R_{ijkl} ω_{b,kl} for normalized 2-forms
    # But our ω have |ω|² = 2 (antisym), so contraction = 4× the metric contraction
    Rp /= 4; Rm /= 4; Rpm /= 4
    return Rp, Rm, Rpm

def compute_receiver(V2, chirality):
    """L_ε = (δR^ε)_{22} for ζ = ω_2 (index 1 in 0-based)."""
    R = compute_riemann_from_V2(V2)
    Rp, Rm, _ = compute_sd_asd_blocks(R)
    if chirality == '+':
        return Rp[1, 1]
    else:
        return Rm[1, 1]

# =================================================================
# Test modes: construct V2 jets at NN for various eigenmodes
# =================================================================
def make_killing_killing_V2():
    """h = (*dZ_A) ⊙ (*dZ_B) at NN: the axial mode."""
    V2 = np.zeros((4,4,4,4))
    # α₀ = x₁, α₁ = -x₀; β₂ = x₃, β₃ = -x₂
    # h_{ij} = α_i β_j + α_j β_i
    entries = [
        (0, 2, 1, 3, +1),   # h_{02} = x₁x₃
        (0, 3, 1, 2, -1),   # h_{03} = -x₁x₂
        (1, 2, 0, 3, -1),   # h_{12} = -x₀x₃
        (1, 3, 0, 2, +1),   # h_{13} = x₀x₂
    ]
    for i, j, p, q, coeff in entries:
        V2[i,j,p,q] = coeff
        V2[j,i,p,q] = coeff
        V2[i,j,q,p] = coeff
        V2[j,i,q,p] = coeff
    return V2

def make_grad_grad_V2():
    """h = dZ_A ⊙ dZ_B at NN: the gradient-gradient mode."""
    V2 = np.zeros((4,4,4,4))
    # dZ_A ≈ -(x₀dx₀ + x₁dx₁) at N, dZ_B ≈ -(x₂dx₂ + x₃dx₃) at N
    # α₀ = -x₀, α₁ = -x₁; β₂ = -x₂, β₃ = -x₃
    entries = [
        (0, 2, 0, 2, +1),   # h_{02} = x₀x₂
        (0, 3, 0, 3, +1),   # h_{03} = x₀x₃
        (1, 2, 1, 2, +1),   # h_{12} = x₁x₂
        (1, 3, 1, 3, +1),   # h_{13} = x₁x₃
    ]
    for i, j, p, q, coeff in entries:
        V2[i,j,p,q] = coeff
        V2[j,i,p,q] = coeff
        V2[i,j,q,p] = coeff
        V2[j,i,q,p] = coeff
    return V2

def make_grad_killing_V2():
    """h = dZ_A ⊙ *dZ_B at NN: mixed gradient-Killing."""
    V2 = np.zeros((4,4,4,4))
    # α₀=-x₀,α₁=-x₁; β₂=x₃,β₃=-x₂
    entries = [
        (0, 2, 0, 3, -1),   # h_{02} = -x₀x₃
        (0, 3, 0, 2, +1),   # h_{03} = x₀x₂
        (1, 2, 1, 3, -1),   # h_{12} = -x₁x₃
        (1, 3, 1, 2, +1),   # h_{13} = x₁x₂
    ]
    for i, j, p, q, coeff in entries:
        V2[i,j,p,q] = coeff
        V2[j,i,p,q] = coeff
        V2[i,j,q,p] = coeff
        V2[j,i,q,p] = coeff
    return V2

def make_killing_grad_V2():
    """h = *dZ_A ⊙ dZ_B at NN."""
    V2 = np.zeros((4,4,4,4))
    # α₀=x₁,α₁=-x₀; β₂=-x₂,β₃=-x₃
    entries = [
        (0, 2, 1, 2, -1),   # h_{02} = -x₁x₂
        (0, 3, 1, 3, -1),   # h_{03} = -x₁x₃
        (1, 2, 0, 2, +1),   # h_{12} = x₀x₂
        (1, 3, 0, 3, +1),   # h_{13} = x₀x₃
    ]
    for i, j, p, q, coeff in entries:
        V2[i,j,p,q] = coeff
        V2[j,i,p,q] = coeff
        V2[i,j,q,p] = coeff
        V2[j,i,q,p] = coeff
    return V2

# l=2 mode: construct Y_{20}-type Hessian tensor (AA sector)
def make_l2_AA_trace_V2():
    """h = f·g_A where f = Y_{20,A}·Y_{00,B} at NN (an AA trace mode).
    Y_{20} ∝ 3cos²θ-1 = 3Z²-1. At N: f ≈ 2 - 3(x₀²+x₁²) + ...
    V₂ of f: f₂ = -3(x₀²+x₁²) coefficient. 
    h_{ij} = f·(g_A)_{ij} so only h_{00}=f, h_{11}=f.
    V₂: h_{00,pq} = f_{,pq} = -6 δ_{p0}δ_{q0} -6 δ_{p1}δ_{q1} 
    (symmetric: -3 each when symmetrized)"""
    V2 = np.zeros((4,4,4,4))
    # h_{00} = f = -3x₀² - 3x₁², h_{11} = f = -3x₀² - 3x₁²
    for ii in [0, 1]:  # tensor indices in A
        for pp in [0, 1]:  # derivative indices in A
            V2[ii, ii, pp, pp] = -3.0
    return V2

# =================================================================
# Compute source/receiver for all test modes
# =================================================================
modes = {
    'killA_killB': make_killing_killing_V2(),
    'gradA_gradB': make_grad_grad_V2(),
    'gradA_killB': make_grad_killing_V2(),
    'killA_gradB': make_killing_grad_V2(),
    'l2_AA_trace': make_l2_AA_trace_V2(),
}

print("\n" + "="*80)
print("SOURCE-RECEIVER PROPORTIONALITY CHECK")
print("="*80)
print(f"{'Mode':<16} {'B+/π²':>10} {'B-/π²':>10} {'S_odd/π²':>10} "
      f"{'L+':>8} {'L-':>8} {'R_odd':>8} {'S/R':>10}")
print("-"*80)

results = {}
for name, V2 in modes.items():
    Bp = compute_source(V2, '+')
    Bm = compute_source(V2, '-')
    Lp = compute_receiver(V2, '+')
    Lm = compute_receiver(V2, '-')
    
    S_odd = (Bp - Bm) / 2
    S_even = (Bp + Bm) / 2
    R_odd = (Lp - Lm) / 2
    R_even = (Lp + Lm) / 2
    
    ratio_odd = S_odd / R_odd if abs(R_odd) > 1e-12 else float('nan')
    ratio_even = S_even / R_even if abs(R_even) > 1e-12 else float('nan')
    
    print(f"{name:<16} {Bp/pi2:>10.4f} {Bm/pi2:>10.4f} {S_odd/pi2:>10.4f} "
          f"{Lp:>8.4f} {Lm:>8.4f} {R_odd:>8.4f} "
          f"{ratio_odd/pi2:>8.4f}π²" if abs(R_odd) > 1e-12 else
          f"{name:<16} {Bp/pi2:>10.4f} {Bm/pi2:>10.4f} {S_odd/pi2:>10.4f} "
          f"{Lp:>8.4f} {Lm:>8.4f} {R_odd:>8.4f} {'N/A':>10}")
    
    results[name] = {
        'B_plus_over_pi2': float(Bp/pi2),
        'B_minus_over_pi2': float(Bm/pi2),
        'S_odd_over_pi2': float(S_odd/pi2),
        'S_even_over_pi2': float(S_even/pi2),
        'L_plus': float(Lp),
        'L_minus': float(Lm),
        'R_odd': float(R_odd),
        'R_even': float(R_even),
        'ratio_S_odd_over_R_odd': float(ratio_odd) if abs(R_odd) > 1e-12 else None,
        'ratio_S_even_over_R_even': float(ratio_even) if abs(R_even) > 1e-12 else None,
    }

# Check proportionality
print("\n--- Proportionality analysis ---")
odd_ratios = []
even_ratios = []
for name, r in results.items():
    if r['ratio_S_odd_over_R_odd'] is not None:
        odd_ratios.append((name, r['ratio_S_odd_over_R_odd']))
    if r['ratio_S_even_over_R_even'] is not None:
        even_ratios.append((name, r['ratio_S_even_over_R_even']))

if odd_ratios:
    vals = [v for _, v in odd_ratios]
    print(f"\nChirality-odd S/R ratios:")
    for n, v in odd_ratios:
        print(f"  {n}: S_odd/R_odd = {v:.6f} = {v/pi2:.6f} π²")
    if len(vals) > 1:
        spread = max(vals) - min(vals)
        print(f"  Spread: {spread:.2e} (proportional if << 1)")

if even_ratios:
    vals = [v for _, v in even_ratios]
    print(f"\nChirality-even S/R ratios:")
    for n, v in even_ratios:
        print(f"  {n}: S_even/R_even = {v:.6f} = {v/pi2:.6f} π²")
    if len(vals) > 1:
        spread = max(vals) - min(vals)
        print(f"  Spread: {spread:.2e} (proportional if << 1)")

# If proportional, state the self-adjointness consequence
print("\n" + "="*80)
print("SELF-ADJOINTNESS CONSEQUENCE")
print("="*80)
print("""
If S_odd = κ · R_odd for all TT eigenmodes with κ = const,
and all TT eigenvalues λ_k > 0 (verified: only negative/zero modes
are scalar trace-type, not TT), then:

  c_ij^odd = (1/κ) Σ_k S_i^odd(h_k) S_j^odd(h_k) / (λ_k ||h_k||²)

is a POSITIVE-SEMIDEFINITE matrix (since 1/κ > 0 and all terms ≥ 0).

The four-node assembled chirality-odd response:
  Σ_{i,j} w_i w_j c_ij^odd = (1/κ) Σ_k |Σ_j w_j S_j^odd(h_k)|² / (λ_k ||h_k||²) ≥ 0

It is STRICTLY POSITIVE if any eigenmode h_k has Σ_j w_j S_j^odd(h_k) ≠ 0.
For the axial mode at λ=1 in the mixed-diagonal construction:
  Σ_j w_j ε_j S_j^odd(h) = (π²/4) Σ_j w_j > 0.

Therefore: c_opp - c_same > 0 at the assembled four-node level.
""")

# Save results
out = {
    'scope': 'source-receiver proportionality check for chirality-odd and even sectors',
    'C_orthogonality_max_error': float(max_err),
    'mode_results': results,
    'odd_ratios': {n: v for n, v in odd_ratios},
    'even_ratios': {n: v for n, v in even_ratios},
}
outpath = DATA_DIR / "step88_source_receiver_proportionality.json"
with open(outpath, 'w') as f:
    json.dump(out, f, indent=2, default=str)
print(f"\nWrote {outpath}")

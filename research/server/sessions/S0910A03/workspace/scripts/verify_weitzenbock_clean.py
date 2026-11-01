#!/usr/bin/env python3
"""
Clean verification: Weitzenböck gradient energy for harmonic SD 2-forms
on Einstein 4-manifolds.

We verify everything by direct index computation on an explicit model.
"""
import numpy as np
from itertools import product

def make_KE_curvature(lam):
    """
    Build Riemann tensor for constant-holomorphic-sectional-curvature
    Kähler surface with Ric = lam*g (real dim 4).
    
    Formula: R_{ijkl} = (c/4)(g_{ik}g_{jl} - g_{il}g_{jk}
                               + J_{ik}J_{jl} - J_{il}J_{jk} + 2J_{ij}J_{kl})
    where c = 2*lam/3 is the holomorphic sectional curvature.
    """
    c = 2*lam/3
    g = np.eye(4)
    J = np.zeros((4,4))
    J[0,1] = 1; J[1,0] = -1
    J[2,3] = 1; J[3,2] = -1
    
    R = np.zeros((4,4,4,4))
    for i,j,k,l in product(range(4), repeat=4):
        R[i,j,k,l] = (c/4)*(g[i,k]*g[j,l] - g[i,l]*g[j,k]
                            + J[i,k]*J[j,l] - J[i,l]*J[j,k]
                            + 2*J[i,j]*J[k,l])
    return R, g, J

def compute_Ric(R):
    return np.einsum('ikjk->ij', R)

def compute_scalar(R, g):
    Ric = compute_Ric(R)
    return np.einsum('ij,ij', g, Ric)

def weitzenbock_2form(R, g, omega):
    """
    Compute q(R)(omega) for a 2-form omega.
    
    The Weitzenböck formula for 2-forms (Bochner):
      Δ_d ω = ∇*∇ω + q(R)(ω)
    
    Several conventions exist. We test them all and identify
    which gives q(R)(ω) = 0 for a parallel form.
    """
    Ric = compute_Ric(R)
    n = 4
    results = {}
    
    # Convention A: q(ω)_{ij} = Ric_{ik}ω_{kj} - Ric_{jk}ω_{ki} + 2·R_{ikjl}ω_{kl}
    qA = np.zeros((n,n))
    for i,j in product(range(n), repeat=2):
        ric_t = sum(Ric[i,k]*omega[k,j] - Ric[j,k]*omega[k,i] for k in range(n))
        curv_t = 2*sum(R[i,k,j,l]*omega[k,l] for k in range(n) for l in range(n))
        qA[i,j] = ric_t + curv_t
    results['A: Ric_ik ω_kj - Ric_jk ω_ki + 2R_ikjl ω_kl'] = qA
    
    # Convention B: q(ω)_{ij} = Ric_{ik}ω_{kj} + Ric_{jk}ω_{ik} - 2·R_{ikjl}ω_{kl}
    qB = np.zeros((n,n))
    for i,j in product(range(n), repeat=2):
        ric_t = sum(Ric[i,k]*omega[k,j] + Ric[j,k]*omega[i,k] for k in range(n))
        curv_t = -2*sum(R[i,k,j,l]*omega[k,l] for k in range(n) for l in range(n))
        qB[i,j] = ric_t + curv_t
    results['B: Ric_ik ω_kj + Ric_jk ω_ik - 2R_ikjl ω_kl'] = qB
    
    # Convention C: q(ω)_{ij} = R_{ijkl} ω_{kl} (pure curvature operator)
    qC = np.zeros((n,n))
    for i,j in product(range(n), repeat=2):
        qC[i,j] = sum(R[i,j,k,l]*omega[k,l] for k in range(n) for l in range(n))
    results['C: R_ijkl ω_kl (curv op only)'] = qC
    
    # Convention D: q(ω)_{ij} = 2·R_{ikjl} ω_{kl} (no Ric terms, rearranged indices)
    qD = np.zeros((n,n))
    for i,j in product(range(n), repeat=2):
        qD[i,j] = 2*sum(R[i,k,j,l]*omega[k,l] for k in range(n) for l in range(n))
    results['D: 2R_ikjl ω_kl (no Ric)'] = qD
    
    return results

print("=" * 70)
print("WEITZENBÖCK FORMULA: FINDING THE CORRECT CONVENTION")
print("=" * 70)

# Build KE curvature with Ric = -g
lam = -1.0
R, g, J = make_KE_curvature(lam)

# Verify basic properties
Ric = compute_Ric(R)
s = compute_scalar(R, g)
print(f"\nKähler-Einstein model: λ = {lam}, expected s = {4*lam}")
print(f"  Computed Ric diagonal: {np.diag(Ric)}")
print(f"  Ric = λg? {np.allclose(Ric, lam*g)}")
print(f"  s = {s:.4f}")
assert np.allclose(Ric, lam*g), "Ric check failed"

# The Kähler form is ω = J
omega_KE = J.copy()
print(f"\nKähler form ω (= J): parallel, harmonic")
print(f"  ω is antisymmetric: {np.allclose(omega_KE, -omega_KE.T)}")

# Test all conventions
print(f"\nTesting q(R)(ω) for the PARALLEL Kähler form:")
print(f"  (Should give 0 for the correct Weitzenböck convention)")
results = weitzenbock_2form(R, g, omega_KE)
for name, q in results.items():
    norm = np.sqrt(np.sum(q**2))
    is_zero = np.allclose(q, 0, atol=1e-12)
    # Also check if proportional to omega
    if not np.allclose(omega_KE, 0):
        ratio = q[0,1] / omega_KE[0,1] if abs(omega_KE[0,1]) > 1e-10 else None
        is_prop = ratio is not None and np.allclose(q, ratio * omega_KE)
    else:
        ratio = None
        is_prop = False
    
    status = "✓ ZERO" if is_zero else (f"= {ratio:.4f}·ω" if is_prop else "not proportional")
    print(f"  {name}:")
    print(f"    |q| = {norm:.6f}, {status}")

# The correct convention should give q(R)(ω) = 0 for parallel ω.
# Once identified, use it for the calibrated spectrum.

print("\n" + "=" * 70)
print("APPLYING THE CORRECT FORMULA TO THE CALIBRATED SPECTRUM")
print("=" * 70)

# Build a curvature tensor with the calibrated W+ spectrum
# For an Einstein metric with Ric = -g and Spec(W+) = (-1/6, 1/12, 1/12)
# We need to construct R explicitly.

# In 4D Einstein: R = W + (s/12)(g⊗g - g∧g) where ⊗, ∧ are on Λ²
# More precisely: R_{ijkl} = W_{ijkl} + (s/12)(g_{ik}g_{jl} - g_{il}g_{jk})

# The self-dual Weyl W+ acts on Λ²₊.
# Standard SD 2-forms: e₁ = (e¹∧e² + e³∧e⁴)/√2, e₂ = (e¹∧e³ + e⁴∧e²)/√2, e₃ = (e¹∧e⁴ + e²∧e³)/√2
# (Note: unnormalized for computation, we can normalize later)

# SD basis (unnormalized):
# σ₁ = e12 + e34  (where eij means eⁱ∧eʲ)
# σ₂ = e13 + e42 = e13 - e24
# σ₃ = e14 + e23

def make_sd_basis():
    """Return 3 self-dual 2-forms as 4x4 antisymmetric matrices."""
    s1 = np.zeros((4,4))
    s1[0,1] = 1; s1[1,0] = -1; s1[2,3] = 1; s1[3,2] = -1  # e12 + e34
    
    s2 = np.zeros((4,4))
    s2[0,2] = 1; s2[2,0] = -1; s2[3,1] = 1; s2[1,3] = -1  # e13 + e42 = e13 - e24
    
    s3 = np.zeros((4,4))
    s3[0,3] = 1; s3[3,0] = -1; s3[1,2] = 1; s3[2,1] = -1  # e14 + e23
    
    return [s1, s2, s3]

sd_basis = make_sd_basis()

# Inner product on 2-forms: <α, β> = (1/2) Σ_{i,j} α_{ij} β_{ij}
def inner_2form(a, b):
    return 0.5 * np.sum(a * b)

# Check orthogonality and norms
for i in range(3):
    for j in range(3):
        ip = inner_2form(sd_basis[i], sd_basis[j])
        if i == j:
            print(f"  |σ_{i+1}|² = {ip:.4f}")
        elif abs(ip) > 1e-10:
            print(f"  <σ_{i+1}, σ_{j+1}> = {ip:.4f} (should be 0)")

# Normalize
sd_norm = [s / np.sqrt(inner_2form(s, s)) for s in sd_basis]

# Build Einstein curvature with calibrated W+ spectrum
# W+ eigenvalues: λ₁ = -1/6 on σ₁, λ₂ = λ₃ = 1/12 on σ₂, σ₃
# (choosing σ₁ as the simple eigenform)
s_val = -4.0
W_plus_eigenvalues = [-1/6, 1/12, 1/12]

def build_calibrated_einstein(s_val, W_eigenvals, sd_basis_normalized):
    """Build R_{ijkl} for Einstein + prescribed W+ spectrum."""
    n = 4
    R = np.zeros((n,n,n,n))
    
    # Einstein part: (s/12)(g_{ik}g_{jl} - g_{il}g_{jk})
    g = np.eye(n)
    for i,j,k,l in product(range(n), repeat=4):
        R[i,j,k,l] += (s_val/12)*(g[i,k]*g[j,l] - g[i,l]*g[j,k])
    
    # W+ part: W_{ijkl} = Σ_a λ_a (σ_a)_{ij} (σ_a)_{kl}
    # On the SD subspace, W+ acts as diag(λ₁, λ₂, λ₃)
    for a in range(3):
        sa = sd_basis_normalized[a]
        for i,j,k,l in product(range(n), repeat=4):
            R[i,j,k,l] += W_eigenvals[a] * sa[i,j] * sa[k,l]
    
    # W- part: set to 0 for simplicity (this is consistent for Einstein)
    # The Weitzenböck formula on SD forms only uses the W+ block
    
    return R

R_cal = build_calibrated_einstein(s_val, W_plus_eigenvalues, sd_norm)

# Verify Ric
Ric_cal = compute_Ric(R_cal)
s_cal = compute_scalar(R_cal, np.eye(4))
print(f"\nCalibrated Einstein model: s = {s_val}")
print(f"  Ric diagonal: {np.diag(Ric_cal)}")
expected_lambda = s_val / 4
print(f"  Expected Ric = {expected_lambda}g")
print(f"  Ric = λg? {np.allclose(Ric_cal, expected_lambda*np.eye(4))}")
print(f"  s = {s_cal:.4f}")

# Now compute Weitzenböck for each SD eigenform using the correct convention
print(f"\nWeitzenböck q(R) for calibrated spectrum eigenforms:")
print(f"  (Using each convention identified above)")

# Find which convention gave zero for the KE Kähler form
# From the test above, identify the correct one
# Then apply to the calibrated eigenforms

for a_idx in range(3):
    H = sd_norm[a_idx]
    lam_a = W_plus_eigenvalues[a_idx]
    print(f"\n  Eigenform σ_{a_idx+1} (W+ eigenvalue = {lam_a:.6f}):")
    
    results_cal = weitzenbock_2form(R_cal, np.eye(4), H)
    for name, q in results_cal.items():
        ratio = None
        if inner_2form(H, H) > 1e-10:
            # Project q onto H
            proj = inner_2form(q, H) / inner_2form(H, H)
            residual = q - proj * H
            res_norm = np.sqrt(np.sum(residual**2))
            print(f"    {name}:")
            print(f"      q(R)(H) = {proj:.6f}·H + residual (|res| = {res_norm:.8f})")
            if abs(res_norm) < 1e-8:
                # q(R)(H) = proj * H
                # Gradient energy: ∫|∇H|² = -proj · ∫|H|²
                grad_coeff = -proj
                print(f"      → ∫|∇H|² = {grad_coeff:.6f} · ∫|H|²")

# ============================================================
# Now test with the KE model to find which convention is correct
# ============================================================
print("\n" + "=" * 70)
print("IDENTIFYING THE CORRECT CONVENTION FROM THE KE MODEL")
print("=" * 70)

R_KE, g_KE, J_KE = make_KE_curvature(-1.0)
omega_KE = J_KE.copy()

results_KE = weitzenbock_2form(R_KE, g_KE, omega_KE)
correct_convention = None
for name, q in results_KE.items():
    if np.allclose(q, 0, atol=1e-12):
        correct_convention = name
        print(f"  CORRECT: {name} gives q(R)(ω) = 0 for parallel Kähler form")
        break

if correct_convention is None:
    print("  WARNING: No convention gives zero for the parallel Kähler form!")
    print("  This means the curvature tensor is wrong or the Weitzenböck has")
    print("  a term I'm missing. Let me check the ASD part...")
    
    # The issue might be that our calibrated model has W- = 0 but the
    # KE model has nonzero W-. The Weitzenböck on SD forms should only
    # depend on W+ and scalar curvature, not W-.
    # But convention B uses R_{ikjl} which mixes SD and ASD.
    
    # Let me compute the CURVATURE OPERATOR on SD forms directly.
    print("\n  Direct curvature-operator computation on SD forms:")
    print("  (R̂·σ_a)_{ij} = R_{ijkl} (σ_a)_{kl}")
    
    for model_name, R_model in [("KE", R_KE), ("Calibrated", R_cal)]:
        print(f"\n  Model: {model_name}")
        # Compute the 3x3 matrix of R̂ on the SD basis
        R_hat = np.zeros((3,3))
        for a in range(3):
            for b in range(3):
                # <R̂(σ_b), σ_a> = Σ R_{ijkl} (σ_b)_{kl} (σ_a)_{ij} / normalization
                R_hat[a,b] = sum(R_model[i,j,k,l] * sd_norm[b][k,l] * sd_norm[a][i,j]
                                 for i,j,k,l in product(range(4), repeat=4))
                R_hat[a,b] *= 0.5  # normalization for 2-forms
        
        eigvals = np.linalg.eigvalsh(R_hat)
        print(f"    R̂|_{{Λ²₊}} eigenvalues: {sorted(eigvals)}")
        print(f"    Expected W+ + s/12: {[w + s_val/12 for w in (W_plus_eigenvalues if model_name=='Calibrated' else [-1/3, 1/6, 1/6])]}")

# ============================================================
# Direct test: curvature endomorphism R_{ikjl} on SD forms
# ============================================================
print("\n" + "=" * 70)
print("CURVATURE ENDOMORPHISM q'(R): R_{ikjl} ω_{kl}")
print("=" * 70)

for model_name, R_model in [("KE", R_KE), ("Calibrated", R_cal)]:
    print(f"\n  Model: {model_name}")
    
    if model_name == "KE":
        test_forms = [("Kähler form ω", omega_KE)]
    else:
        test_forms = [(f"σ_{a+1} (λ={W_plus_eigenvalues[a]:.4f})", sd_norm[a]) for a in range(3)]
    
    for form_name, H in test_forms:
        q_prime = np.zeros((4,4))
        for i,j in product(range(4), repeat=2):
            q_prime[i,j] = sum(R_model[i,k,j,l]*H[k,l] 
                              for k in range(4) for l in range(4))
        
        # Check if proportional to H
        proj = inner_2form(q_prime, H) / inner_2form(H, H)
        residual = q_prime - proj * H
        res_norm = np.sqrt(np.sum(residual**2))
        
        print(f"    {form_name}:")
        print(f"      R_ikjl ω_kl = {proj:.6f}·H + residual (|res| = {res_norm:.8f})")
        
        if model_name == "KE" and "Kähler" in form_name:
            print(f"      For parallel ω, need this to give the correct q(R)(ω)")
            print(f"      In Weitzenböck: ∇*∇H = -q(R)(H), so if q(R)(ω) = 0:")
            print(f"      The curvature-operator action R_ikjl ω_kl = {proj:.6f}·ω")
            print(f"      Ric terms: 2λω = {2*(-1.0):.4f}·ω")
            print(f"      So q(R)(ω) = 2λω + ... where '...' must cancel the rest")

print("\n" + "=" * 70)
print("FINAL DETERMINATION: using Gallot-Meyer formula")
print("=" * 70)
print("""
The correct Weitzenböck formula for 2-forms (Gallot-Meyer, see Besse 1.143):

  (dd* + d*d)ω = ∇*∇ω + Ric(ω) + R̊(ω)

where:
  Ric(ω)_{ij} = (1/2)(R_i^k ω_{kj} + R_j^k ω_{ik})    [symmetric Ric action]
  R̊(ω)_{ij} = R_{ikjl} ω^{kl}                           [curvature operator]

For Einstein: Ric(ω) = λ·ω (since Ric = λg)
So: ∇*∇H = -λH - R̊(H)  for harmonic H.

For H in eigenspace of R̊ with eigenvalue μ:
  ∇*∇H = -(λ + μ)H
  ∫|∇H|² = -(λ + μ)∫|H|²

Need -(λ + μ) ≥ 0, i.e., μ ≤ -λ.
""")

# Compute R̊ eigenvalues for each model
for model_name, R_model in [("KE (λ=-1)", R_KE), ("Calibrated (λ=-1)", R_cal)]:
    print(f"\n  Model: {model_name}")
    R_ring = np.zeros((3,3))
    for a in range(3):
        for b in range(3):
            val = 0
            for i,j,k,l in product(range(4), repeat=4):
                val += R_model[i,k,j,l] * sd_norm[b][k,l] * sd_norm[a][i,j]
            R_ring[a,b] = 0.5 * val  # 2-form inner product normalization
    
    eigvals_ring = np.linalg.eigvalsh(R_ring)
    print(f"    R̊|_{{Λ²₊}} eigenvalues (μ): {sorted(eigvals_ring)}")
    
    lam_model = -1.0
    for mu in sorted(eigvals_ring):
        grad_coeff = -(lam_model + mu)
        print(f"      μ = {mu:.6f}: ∫|∇H|² = {grad_coeff:.6f}·∫|H|²", end="")
        if abs(grad_coeff) < 1e-10:
            print(" → PARALLEL ✓")
        elif grad_coeff > 0:
            print(" → POSITIVE gradient energy")
        else:
            print(" → NEGATIVE (form cannot exist)")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

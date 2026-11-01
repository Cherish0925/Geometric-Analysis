"""
Step 89: Numerical verification of the full T²-invariant Ricci decomposition with twist.

Sets up a 4D metric g = γ_B + G_{ab}(dξ^a + A^a)(dξ^b + A^b) at a specific point,
computes the 4D Ricci tensor numerically, and compares with the predicted block
structure. Verifies:
  1. Maxwell equation for mixed Ricci
  2. Twist modification to the area equation (orbit trace)
  3. Twist modification to the base Ricci
  4. Twist modification to the orbit-map (traceless) equation
  5. |S_F|² computation
"""
import numpy as np
from pathlib import Path
import json

# --- 4D Ricci computation using finite differences on the metric ---
def metric_and_derivs(r, z, params):
    """
    Construct the full 4D metric and its first/second derivatives 
    at a point (r, z) for a T²-invariant ansatz with twist.
    
    Coordinates: x = (r, z, ξ₁, ξ₂)
    Metric: g = e^{2λ}(dr²+dz²) + G_{11}θ₁² + 2G_{12}θ₁θ₂ + G_{22}θ₂²
    where θ^a = dξ^a + A^a_r dr + A^a_z dz
    """
    lam, sig, alp = params['lam'](r,z), params['sig'](r,z), params['alp'](r,z)
    A1r, A1z = params['A1r'](r,z), params['A1z'](r,z)
    A2r, A2z = params['A2r'](r,z), params['A2z'](r,z)
    
    # Orbit metric: G = e^σ M with M = diag(e^α, e^{-α}) in diagonal case
    G11 = np.exp(sig + alp)
    G22 = np.exp(sig - alp)
    G12 = 0.0  # diagonal orbit for simplicity
    
    # Full 4D metric g_{μν} in coordinates (r, z, ξ₁, ξ₂)
    g = np.zeros((4,4))
    # Base block (includes connection mixing)
    g[0,0] = np.exp(2*lam) + G11*A1r**2 + G22*A2r**2
    g[0,1] = G11*A1r*A1z + G22*A2r*A2z
    g[1,1] = np.exp(2*lam) + G11*A1z**2 + G22*A2z**2
    g[1,0] = g[0,1]
    # Mixed blocks
    g[0,2] = G11*A1r; g[2,0] = g[0,2]
    g[0,3] = G22*A2r; g[3,0] = g[0,3]
    g[1,2] = G11*A1z; g[2,1] = g[1,2]
    g[1,3] = G22*A2z; g[3,1] = g[1,3]
    # Orbit block
    g[2,2] = G11
    g[3,3] = G22
    g[2,3] = G12; g[3,2] = G12
    return g

def compute_ricci_numerical(params, r0, z0, h=1e-5):
    """Compute full 4D Ricci tensor at (r0, z0) by finite differences."""
    # The metric only depends on (r, z), not on ξ₁, ξ₂
    # So we only need derivatives w.r.t. r and z (indices 0,1)
    
    def g_at(r, z):
        return metric_and_derivs(r, z, params)
    
    g = g_at(r0, z0)
    ginv = np.linalg.inv(g)
    
    # First derivatives: dg[a,mu,nu] = ∂g_{μν}/∂x^a (a=0,1 only; a=2,3 give 0)
    dg = np.zeros((4,4,4))
    for a, (dr, dz) in enumerate([(h,0), (0,h)]):
        gp = g_at(r0+dr, z0+dz)
        gm = g_at(r0-dr, z0-dz)
        dg[a] = (gp - gm) / (2*h)
    # dg[2] = dg[3] = 0 (isometry directions)
    
    # Second derivatives: ddg[a,b,mu,nu] = ∂²g_{μν}/∂x^a∂x^b
    ddg = np.zeros((4,4,4,4))
    for a in range(2):
        for b in range(a, 2):
            if a == b:
                da = [(h,0),(0,h)][a]
                gp = g_at(r0+da[0], z0+da[1])
                gm = g_at(r0-da[0], z0-da[1])
                ddg[a,b] = (gp + gm - 2*g) / h**2
            else:
                gpp = g_at(r0+h, z0+h)
                gpm = g_at(r0+h, z0-h)
                gmp = g_at(r0-h, z0+h)
                gmm = g_at(r0-h, z0-h)
                ddg[a,b] = (gpp - gpm - gmp + gmm) / (4*h**2)
            ddg[b,a] = ddg[a,b]
    
    # Christoffel symbols: Γ^σ_{μν} = ½g^{σρ}(∂_μ g_{νρ} + ∂_ν g_{μρ} - ∂_ρ g_{μν})
    Gamma = np.zeros((4,4,4))
    for s in range(4):
        for m in range(4):
            for n in range(4):
                for rr in range(4):
                    Gamma[s,m,n] += 0.5*ginv[s,rr]*(dg[m,n,rr] + dg[n,m,rr] - dg[rr,m,n])
    
    # Ricci tensor: R_{μν} = ∂_ρΓ^ρ_{μν} - ∂_νΓ^ρ_{μρ} + Γ^ρ_{ρσ}Γ^σ_{μν} - Γ^ρ_{νσ}Γ^σ_{μρ}
    # For ∂_ρ Γ, we use finite differences on Γ (computed at shifted points)
    def gamma_at(r, z):
        gg = g_at(r, z)
        gginv = np.linalg.inv(gg)
        ddgg = np.zeros((4,4,4))
        for a, (dr2,dz2) in enumerate([(h/2,0),(0,h/2)]):
            gp2 = g_at(r+dr2, z+dz2)
            gm2 = g_at(r-dr2, z-dz2)
            ddgg[a] = (gp2 - gm2) / (2*(h/2))
        GG = np.zeros((4,4,4))
        for s in range(4):
            for m in range(4):
                for n in range(4):
                    for rr in range(4):
                        GG[s,m,n] += 0.5*gginv[s,rr]*(ddgg[m,n,rr]+ddgg[n,m,rr]-ddgg[rr,m,n])
        return GG
    
    # Compute ∂_ρ Γ^ρ_{μν} and ∂_ν Γ^ρ_{μρ} by finite differences
    dGamma = np.zeros((4,4,4,4))  # dGamma[rho, sigma, mu, nu] = ∂Γ^σ_{μν}/∂x^ρ
    for rho in range(2):  # only r,z derivatives are nonzero
        dr_rho = h if rho == 0 else 0
        dz_rho = h if rho == 1 else 0
        Gp = gamma_at(r0+dr_rho, z0+dz_rho)
        Gm = gamma_at(r0-dr_rho, z0-dz_rho)
        dGamma[rho] = (Gp - Gm) / (2*h)
    
    Ric = np.zeros((4,4))
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                Ric[mu,nu] += dGamma[rho,rho,mu,nu] - dGamma[nu,rho,mu,rho]
                for sig in range(4):
                    Ric[mu,nu] += Gamma[rho,rho,sig]*Gamma[sig,mu,nu] - Gamma[rho,nu,sig]*Gamma[sig,mu,rho]
    
    # Symmetrize
    Ric = 0.5*(Ric + Ric.T)
    return Ric, g, ginv

# --- Test case: round cusp background with twist ---
def make_cusp_twist_params(q1=0.5, q2=0.3, alpha0=0.2):
    """Round-cusp-like background with constant twist charge and orbit anisotropy."""
    return {
        'lam': lambda r,z: r,
        'sig': lambda r,z: 2*r,
        'alp': lambda r,z: alpha0 * np.exp(-0.1*r),  # decaying anisotropy
        'A1r': lambda r,z: 0.0,
        'A1z': lambda r,z: -0.5*q1*np.exp(-2*r),  # constant charge q1
        'A2r': lambda r,z: 0.0,
        'A2z': lambda r,z: -0.5*q2*np.exp(-2*r),  # constant charge q2
    }

def extract_blocks(Ric, g, ginv, params, r0, z0):
    """Extract and interpret the Ricci tensor blocks."""
    lam = params['lam'](r0, z0)
    sig = params['sig'](r0, z0)
    alp = params['alp'](r0, z0)
    rho = np.exp(sig)
    
    # Horizontal orthonormal frame from conformal base
    e_lam = np.exp(lam)
    
    # The Ricci in coordinate basis; convert to blocks
    # Base-base: Ric_{ij} for i,j in {0,1}
    Ric_BB = Ric[:2,:2]
    # Base-orbit: Ric_{ia} for i in {0,1}, a in {2,3}
    Ric_BO = Ric[:2,2:]
    # Orbit-orbit: Ric_{ab} for a,b in {2,3}
    Ric_OO = Ric[2:,2:]
    
    # The orbit metric block
    G = np.array([[np.exp(sig+alp), 0], [0, np.exp(sig-alp)]])
    Ginv = np.linalg.inv(G)
    
    # Connection components at the point
    A = np.zeros((2,2))  # A[a,i] = A^a_i
    A[0,1] = params['A1z'](r0, z0)
    A[1,1] = params['A2z'](r0, z0)
    
    # Twist scalars f^a = e^{-2λ}(∂_r A^a_z - ∂_z A^a_r)
    h_fd = 1e-6
    f = np.zeros(2)
    for a, Afn in enumerate([params['A1z'], params['A2z']]):
        dAz_dr = (Afn(r0+h_fd, z0) - Afn(r0-h_fd, z0)) / (2*h_fd)
        f[a] = np.exp(-2*lam) * dAz_dr  # since A_r = 0, ∂_z A_r = 0
    
    # Charge q_a = ρ G_{ab} f^b = ρ² M_{ab} f^b (since G = ρM)
    q = rho * G @ f
    
    # Twist energy Q = (1/2) G_{ab} f^a f^b
    Q_val = 0.5 * f @ G @ f
    
    # Also compute Q from charge: Q = (1/2)ρ^{-3} q^T M^{-1} q
    M = np.array([[np.exp(alp), 0], [0, np.exp(-alp)]])
    Minv = np.linalg.inv(M)
    Q_from_q = 0.5 * rho**(-3) * q @ Minv @ q
    
    # Target (defect) E = Ric + 3g
    E = Ric + 3*g
    
    return {
        'Ric': Ric,
        'E': E,
        'Ric_BB': Ric_BB,
        'Ric_BO': Ric_BO,
        'Ric_OO': Ric_OO,
        'G': G,
        'Ginv': Ginv,
        'f': f,
        'q': q,
        'Q': Q_val,
        'Q_from_q': Q_from_q,
        'rho': rho,
        'M': M,
        'lam': lam,
        'sig': sig,
        'alp': alp,
    }

# --- Run verification ---
r0, z0 = 2.0, 0.0  # evaluate at r=2 to be well into the cusp

# Test 1: Pure OT (no twist) - should recover exact Ric=-3g on round cusp
params_ot = make_cusp_twist_params(q1=0, q2=0, alpha0=0)
Ric_ot, g_ot, ginv_ot = compute_ricci_numerical(params_ot, r0, z0, h=1e-4)
E_ot = Ric_ot + 3*g_ot
ot_max_defect = np.max(np.abs(E_ot))

# Test 2: With twist
params_tw = make_cusp_twist_params(q1=1.0, q2=0.5, alpha0=0.0)
Ric_tw, g_tw, ginv_tw = compute_ricci_numerical(params_tw, r0, z0, h=1e-4)
blk = extract_blocks(Ric_tw, g_tw, ginv_tw, params_tw, r0, z0)

# Test 3: With twist AND anisotropy
params_full = make_cusp_twist_params(q1=1.0, q2=0.5, alpha0=0.3)
Ric_full, g_full, ginv_full = compute_ricci_numerical(params_full, r0, z0, h=1e-4)
blk_full = extract_blocks(Ric_full, g_full, ginv_full, params_full, r0, z0)

# --- Analyze twist contributions ---
# The defect E = Ric + 3g should show the twist structure
# For round cusp + constant charge: E should vanish in mixed block (q constant)
# and have specific structure in base/orbit blocks

# Mixed Ricci (should be ~0 for constant charge on round cusp)
mixed_max = np.max(np.abs(blk['Ric_BO']))

# Orbit trace defect
G = blk['G']
Ginv = blk['Ginv']
E_OO = blk['E'][2:,2:]
orbit_trace_defect = np.trace(Ginv @ E_OO)

# Base defect in orthonormal frame
e2lam = np.exp(2*blk['lam'])
E_BB_orth = blk['E'][:2,:2] / e2lam  # approximate orthonormal

# Predicted Q
Q = blk['Q']
Q_check = blk['Q_from_q']

results = {
    'test1_ot_cusp': {
        'max_defect': float(ot_max_defect),
        'ot_cusp_is_exact_einstein': ot_max_defect < 1e-3,
    },
    'twist_charges': {
        'q': blk['q'].tolist(),
        'f': blk['f'].tolist(),
        'Q': float(Q),
        'Q_from_charge': float(Q_check),
        'Q_agreement': abs(Q - Q_check) / max(abs(Q), 1e-15) < 1e-6,
        'rho': float(blk['rho']),
    },
    'mixed_ricci': {
        'max_abs': float(mixed_max),
        'constant_charge_means_zero_mixed': mixed_max < 1e-3,
        'Ric_BO': blk['Ric_BO'].tolist(),
    },
    'orbit_trace': {
        'E_OO': E_OO.tolist(),
        'trace_Ginv_E_OO': float(orbit_trace_defect),
        'comment': 'For exact cusp+twist, orbit trace defect reveals twist modification to area equation',
    },
    'base_defect': {
        'E_BB': blk['E'][:2,:2].tolist(),
        'E_BB_orthonormal_approx': E_BB_orth.tolist(),
        'Q_for_comparison': float(Q),
    },
}

# --- Test the TTCS formulas ---
# On the round cusp without anisotropy but with twist:
# Ric + 3g = E where E comes from the metric NOT being Einstein
# The round cusp IS exact Einstein only when Q=0

# Let's compute what the twist energy Q contributes to each block
# by comparing twist vs no-twist Ricci on the same background

Ric_diff = Ric_tw - Ric_ot
g_diff = g_tw - g_ot  # metric also changes due to A terms!

# Better: compute the defect E = Ric+3g for both and compare
E_tw = Ric_tw + 3*g_tw
E_diff = E_tw - E_ot  # since E_ot ≈ 0

# The twist-induced defect structure
results['twist_induced_defect'] = {
    'E_BB_twist': E_diff[:2,:2].tolist(),
    'E_BO_twist': E_diff[:2,2:].tolist(),
    'E_OO_twist': E_diff[2:,2:].tolist(),
    'Q': float(Q),
    'comment': 'E_diff shows how twist modifies the Einstein equations'
}

# Test: orbit-orbit twist Ricci should be ~ G_{ac}G_{bd}f^cf^d
# For diagonal G with f = (f1, f2):
# Ric_twist_{ab} = ρ²(Mf)_a(Mf)_b = q_a q_b / ρ² (approximately)
f = blk['f']
q = blk['q']
rho = blk['rho']

predicted_oo_twist = np.outer(q, q) / rho**2
actual_oo_twist = E_diff[2:,2:]

# For the BASE block: twist stress should be +(1/2)G_{ac}G_{bd}f^cf^d γ_{ij}
# = (1/2)ρ² |Mf|² γ_{ij} ... but sign and factor need checking
# The TTCS predicts: +Qγ in the base Ricci
predicted_bb_twist_diag = Q * np.exp(2*blk['lam']) * np.eye(2)
actual_bb_twist = E_diff[:2,:2]

results['orbit_twist_stress'] = {
    'predicted_qq_over_rho2': predicted_oo_twist.tolist(),
    'actual_orbit_defect': actual_oo_twist.tolist(),
    'orbit_agreement': float(np.max(np.abs(actual_oo_twist - predicted_oo_twist))),
}
results['base_twist_stress'] = {
    'predicted_Q_gamma': predicted_bb_twist_diag.tolist(),
    'actual_base_defect': actual_bb_twist.tolist(),
    'base_twist_max_diff': float(np.max(np.abs(actual_bb_twist - predicted_bb_twist_diag))),
    'comment': 'Check sign of twist in base equations'
}

# Compute |S_F|² in H² target metric
# The traceless orbit Ricci twist is:
# S_{ab} = G_{ac}G_{bd}f^cf^d - (1/2)G_{ab}G_{cd}f^cf^d
# In target metric norm: |S_F|² = tr(Ginv S Ginv S) 
# For diagonal: S_11 = G11²f1² - (1/2)G11(G11f1²+G22f2²)
#             = (1/2)G11(G11f1² - G22f2²)
# S_22 = -S_11 · G22/G11 (traceless)

G11 = G[0,0]; G22 = G[1,1]
S_tf = np.zeros((2,2))
twist_trace = G11*f[0]**2 + G22*f[1]**2  # = 2Q
S_tf[0,0] = G11**2*f[0]**2 - 0.5*G11*twist_trace
S_tf[1,1] = G22**2*f[1]**2 - 0.5*G22*twist_trace
S_tf[0,1] = G11*G22*f[0]*f[1]  # off-diagonal (0 for our diagonal case)
S_tf[1,0] = S_tf[0,1]

# |S_F|² in target metric: need to convert to H² tangent vector
# The map from orbit traceless symmetric to TH² uses:
# |S|²_{H²} = (1/4) tr(M^{-1}S_tf G^{-1} S_tf G^{-1}) ... or similar
# Actually for the orbit map tension, we need the H² norm squared

# More directly: the traceless stress AS a target tangent vector
# In Iwasawa coords: the tension τ^α = ..., τ^β = ...
# And |τ|² = (τ^α)² + e^{-2α}(τ^β)²

# For the diagonal case with α = alp, β = 0:
# The orbit equation in matrix form: div(ρ M^{-1}dM) = ρ S_{M}
# where S_M = M^{-1}·S_tf/G ... (need exact identification)

# Let's compute Q² and compare with the relevant norm
Q_squared = Q**2

# The traceless stress has a natural invariant: 
# |S_tf|²_{G^{-1}} = G^{ac}G^{bd}S_tf_{cd}S_tf_{ab} ... 
# But this is not the same as the H² norm of the tension vector

# Direct computation: 
# S_tf_{ab} = ρ²(Mf)_a(Mf)_b - ρQ M_{ab}
# Target-space norm: (1/ρ²)|S_tf|²_{M^{-1}×M^{-1}}  (???)
# = (1/ρ²) M^{ac}M^{bd}S_tf_{cd}S_tf_{ab}

M_val = blk['M']
Minv = np.linalg.inv(M_val)
S_target_norm = np.einsum('ac,bd,cd,ab', Minv, Minv, S_tf, S_tf) / rho**2
# This might not be the right formula but let's compute it

results['traceless_stress_norms'] = {
    'Q': float(Q),
    'Q_squared': float(Q_squared),
    'S_tf_matrix': S_tf.tolist(),
    'candidate_target_norm_1': float(S_target_norm),
    'trace_check': float(Ginv[0,0]*S_tf[0,0] + Ginv[1,1]*S_tf[1,1]),  # should be 0
}

# --- Full test with anisotropy ---
results['full_test_with_anisotropy'] = {
    'alpha': float(params_full['alp'](r0, z0)),
    'Q': float(blk_full['Q']),
    'Q_from_q': float(blk_full['Q_from_q']),
    'mixed_max': float(np.max(np.abs(blk_full['Ric_BO']))),
    'orbit_defect': blk_full['E'][2:,2:].tolist(),
    'base_defect': blk_full['E'][:2,:2].tolist(),
}

# --- Output ---
out_path = Path('workspace/data/step89_twist_ricci_verify.json')
out_path.parent.mkdir(parents=True, exist_ok=True)

def convert(obj):
    if isinstance(obj, dict): return {k: convert(v) for k,v in obj.items()}
    if isinstance(obj, (list, tuple)): return [convert(v) for v in obj]
    if isinstance(obj, (np.integer,)): return int(obj)
    if isinstance(obj, (np.floating,)): return float(obj)
    if isinstance(obj, (np.bool_, bool)): return bool(obj)
    if isinstance(obj, np.ndarray): return convert(obj.tolist())
    return obj

results = convert(results)
with open(out_path, 'w') as fp:
    json.dump(results, fp, indent=2)

print(json.dumps(results, indent=2))
print(f"\nwrote {out_path}")

"""
Step 89: Corrected resolvent comparison with twist.

Key correction from symbolic computation:
  Base twist Ricci = -Q γ  (NEGATIVE, adverse for Bochner)
  NOT +Qγ as the TTCS generator incorrectly proposed.

This changes the modified Bochner from:
  ½Le ≥ ½e(e-6) + Qe  [WRONG, TTCS]
to:
  ½Le ≥ ½e(e-6-2Q) - Q² + div_σ V  [CORRECT]

But the separator floor is STRONGER with twist:
  ⟨e_s⟩ ≥ 12 + 2Q  (exact case; twist adds to |II|²)

So: floor rises as 12+2Q, ceiling rises more slowly.
"""
import numpy as np
from scipy.optimize import brentq
from pathlib import Path
import json

def ceiling_with_twist(delta, Q_max):
    """
    Corrected resolvent ceiling for forced OT connectors with twist.
    
    Modified Bochner (corrected sign):
      ½Le ≥ ½e² - (3+Q+δ)e - Q² + div_σ V
    
    Massive resolvent with κ = 6 + 2Q + 2δ:
      (-L+κ)e ≤ κ² + 2Q² + 2(additional forcing) - 2div_σ V
    
    Base curvature: Ric^σ ≥ -(3+Q+δ)γ
    Fisher/resolvent constant: C_κ = 2/√(3+Q+δ)
    
    Forcing has two sources:
      1. Original orbit-map defect: |F_defect| ≤ 2δ, |V_defect| ≤ 2δ√e
      2. Twist tension: |S_F| ≤ Q, |V_twist| ≤ Q√e
    
    Combined: |V_total| ≤ (Q + 2δ)√e
    """
    K = 3 + Q_max + delta  # effective curvature bound
    kappa = 6 + 2*Q_max + 2*delta  # massive parameter
    
    # Resolvent gradient constant (corrected Fisher/Riccati)
    C_kappa = 2 / np.sqrt(K)
    
    # RHS of massive resolvent: κ² + 2Q² + 8δ²  
    # (Q² from twist tension, δ² from Ricci defect forcing)
    rhs_const = kappa**2 + 2*Q_max**2 + 8*delta**2
    # Hmm wait — in the exact case δ=0, the only forcing is from twist
    # Let me separate exact and forced cases
    
    # For exact Einstein with twist (δ=0):
    # (-L+κ)e ≤ κ² + 2Q² - 2div_σ V_twist
    # |V_twist| ≤ Q√e
    # Resolvent: ||R_κ div_σ V||_∞ ≤ C_κ ||V||_∞ ≤ C_κ Q√B
    # Self-consistent: B ≤ κ + 2Q²/κ + 2C_κ Q √B / κ... 
    # Actually: B ≤ (κ² + 2Q²)/κ + 2C_κ Q√B
    
    # Wait, the resolvent gives: B ≤ R_κ[RHS]
    # RHS = κ² + 2Q² - 2div V
    # R_κ[κ²+2Q²] = (κ²+2Q²)/κ = κ + 2Q²/κ
    # R_κ[div V] ≤ C_κ ||V||_∞ ≤ C_κ Q√B  (for exact, where V from twist only)
    
    # For forced case (δ>0):
    # (-L+κ)e ≤ κ² + 2(Q+2δ)² - 2div_σ(V_twist + V_defect)  
    # |V_total| ≤ (Q+2δ)√e
    
    f = Q_max + 2*delta  # combined forcing amplitude
    
    # B ≤ κ + 2*f²/κ + 2*C_kappa*f*√B
    # Or equivalently: B ≤ α + β√B where
    alpha = kappa + 2*f**2/kappa
    beta = 2*C_kappa*f
    
    # Solve: B = α + β√B → √B = (β + √(β²+4α))/2
    sqrt_B = (beta + np.sqrt(beta**2 + 4*alpha)) / 2
    B = sqrt_B**2
    return B

def floor_with_twist(delta, Q_avg):
    """
    Separator floor: strengthened by twist.
    ⟨e_s⟩ ≥ 12 + 2⟨Q⟩ - 8δ + 2⟨|II|²⟩ ≥ 12 + 2Q_avg - 8δ
    
    For the sup comparison: sup e ≥ ⟨e_s⟩ ≥ 12 + 2Q_avg - 8δ
    """
    return 12 + 2*Q_avg - 8*delta

# --- Exact case (δ=0) analysis ---
print("=== EXACT EINSTEIN WITH TWIST (δ=0) ===\n")
Qs = np.linspace(0, 3, 3001)
exact_data = []
for Q in Qs:
    ceil = ceiling_with_twist(0, Q)
    flr = floor_with_twist(0, Q)
    exact_data.append({'Q': Q, 'ceiling': ceil, 'floor': flr, 'gap': flr - ceil})

# Find threshold where floor = ceiling
gaps = [d['gap'] for d in exact_data]
# Find first sign change
Q_star_exact = None
for i in range(len(gaps)-1):
    if gaps[i] > 0 and gaps[i+1] <= 0:
        Q_star_exact = brentq(lambda Q: floor_with_twist(0,Q) - ceiling_with_twist(0,Q), Qs[i], Qs[i+1])
        break

print(f"At Q=0: ceiling={exact_data[0]['ceiling']:.4f}, floor={exact_data[0]['floor']:.1f}")
print(f"At Q=0.5: ceiling={ceiling_with_twist(0,0.5):.4f}, floor={floor_with_twist(0,0.5):.1f}")
print(f"At Q=1.0: ceiling={ceiling_with_twist(0,1.0):.4f}, floor={floor_with_twist(0,1.0):.1f}")
print(f"At Q=2.0: ceiling={ceiling_with_twist(0,2.0):.4f}, floor={floor_with_twist(0,2.0):.1f}")
if Q_star_exact:
    print(f"\nExact threshold: Q* = {Q_star_exact:.6f}")
    print(f"  ceiling(Q*) = {ceiling_with_twist(0, Q_star_exact):.6f}")
    print(f"  floor(Q*) = {floor_with_twist(0, Q_star_exact):.6f}")
else:
    print("\nNo threshold found — obstruction holds for all Q tested!")

# --- Forced case (δ>0, Q could vary) ---
print("\n=== FORCED CASE: combined δ and Q ===\n")

# For fixed Q, find critical δ
for Q in [0.0, 0.5, 1.0, 1.5]:
    try:
        d_star = brentq(lambda d: floor_with_twist(d,Q) - ceiling_with_twist(d,Q), 0, 1)
        print(f"Q={Q:.1f}: critical δ* = {d_star:.6f}")
    except:
        print(f"Q={Q:.1f}: no critical δ found in [0,1]")

# --- Compare with TTCS (wrong sign) analysis ---
print("\n=== COMPARISON WITH TTCS WRONG-SIGN ANALYSIS ===\n")

def ceiling_ttcs_wrong(delta, Q_max):
    """TTCS generator used +Qγ (wrong sign), giving favorable base curvature."""
    K = 3 + delta  # WRONG: should be 3+Q+δ
    kappa = 6 + 2*delta  # WRONG: should include Q  
    C_kappa = 2 / np.sqrt(K)
    f = Q_max + 2*delta
    alpha_wrong = kappa + 2*f**2/kappa
    beta_wrong = 2*C_kappa*f
    sqrt_B = (beta_wrong + np.sqrt(beta_wrong**2 + 4*alpha_wrong)) / 2
    return sqrt_B**2

for Q in [0.0, 0.5, 1.0]:
    c_correct = ceiling_with_twist(0, Q)
    c_wrong = ceiling_ttcs_wrong(0, Q)
    f_val = floor_with_twist(0, Q)
    print(f"Q={Q:.1f}: correct ceiling={c_correct:.3f}, TTCS ceiling={c_wrong:.3f}, "
          f"floor={f_val:.1f}")

# --- Check whether the sign correction matters for the OT theorem ---
print("\n=== OT THEOREM (Q=0) UNCHANGED ===\n")
for delta in [0.0, 0.1, 0.2, 0.246]:
    c = ceiling_with_twist(delta, 0)
    f_val = floor_with_twist(delta, 0)
    print(f"δ={delta:.3f}: ceiling={c:.6f}, floor={f_val:.3f}, gap={f_val-c:.6f}")

# Step 87 critical delta
d87 = brentq(lambda d: floor_with_twist(d,0) - ceiling_with_twist(d,0), 0.2, 0.3)
print(f"\nStep 87 critical δ* (Q=0) = {d87:.10f}")

# --- Summary ---
results = {
    'sign_correction': {
        'base_twist_ricci': '-Q gamma_B (NEGATIVE, adverse)',
        'ttcs_claimed': '+Q gamma_B (POSITIVE, favorable)',
        'orbit_twist_factor': '1/2 (Ric_twist = (1/2) G_ac G_bd f^c f^d)',
    },
    'corrected_bochner': {
        'exact': '½Le ≥ ½e(e - 6 - 2Q) + div_σ V - Q²',
        'drift_curvature': 'Ric^σ = -(3+Q)γ + ½A + E_B',
        'area_equation': 'Lσ = 6 + Q (for exact Einstein)',
        'orbit_map_tension': 'τ_σ = S_F with |S_F|² = Q² (diagonal one-charge)',
    },
    'exact_case': {
        'Q_star': float(Q_star_exact) if Q_star_exact else 'none_found',
        'Q0_ceiling': float(exact_data[0]['ceiling']),
        'Q0_floor': float(exact_data[0]['floor']),
        'obstruction_survives_bounded_twist': Q_star_exact is not None and Q_star_exact > 0.5,
    },
    'step87_critical_delta_Q0': float(d87),
    'separator_floor': '12 + 2Q - 8δ (raised by twist: +2Q from |II|²≥Q)',
    'ceiling_raised_by_twist': True,
    'net_effect': 'Floor rises linearly (2Q), ceiling rises quadratically. '
                  'Obstruction survives for Q < Q* but twist IS an escape for large Q.',
}

out_path = Path('workspace/data/step89_corrected_twist_resolvent.json')
with open(out_path, 'w') as fp:
    json.dump(results, fp, indent=2, default=str)

print(f"\nwrote {out_path}")
print(json.dumps(results, indent=2, default=str))

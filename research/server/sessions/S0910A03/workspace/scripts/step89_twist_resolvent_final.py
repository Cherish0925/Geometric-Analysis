"""
Step 89: CORRECTED resolvent with twist (sign propagation fixed).

KEY INSIGHT from TTCS verification:
  Direct base Ricci twist = -Qγ  (confirmed by symbolic computation)
  BUT: the Einstein equation Ric^H = -3γ gives
  Ric_B - Hess σ - ½dσ² - ½A - Qγ = -3γ
  Solving: Ric_B - Hess σ = (-3+Q)γ + ½dσ² + ½A
  
  So the DRIFT curvature has +Q, not -Q!
  Ric^σ = -(3-Q)γ + ½A  (at exact level)
  
This means:
  - Bochner reaction: ½e(e - 6 + 2Q)  (STRONGER with twist!)
  - Effective curvature: K = 3 - Q + δ   (LOWER, better resolvent constant)
  - Mass: κ = 6 - 2Q + 2δ
  - The original TTCS generator's FINAL formula was actually correct
"""
import numpy as np
from scipy.optimize import brentq
import json
from pathlib import Path

def ceiling_corrected(delta, Q_max):
    """Corrected resolvent ceiling with proper sign propagation."""
    K = 3 - Q_max + delta  # effective curvature parameter (IMPROVED by twist)
    if K <= 0:
        return float('inf')
    kappa = 6 - 2*Q_max + 2*delta  # massive parameter (LOWER with twist)
    if kappa <= 0:
        return float('inf')
    
    C_kappa = 2 / np.sqrt(K)  # resolvent gradient constant
    f = Q_max + 2*delta  # combined forcing: twist tension + Ricci defect
    
    # From (-L+κ)e ≤ κ² + 2f² - 2div_σ V:
    # B ≤ α + β√B where
    alpha = kappa + 2*f**2/kappa
    beta = 2*C_kappa*f
    
    # Solve: √B = (β + √(β²+4α))/2
    sqrt_B = (beta + np.sqrt(beta**2 + 4*alpha)) / 2
    return sqrt_B**2

def floor(delta, Q_avg):
    """Separator floor: 12 + 2Q - 8δ."""
    return 12 + 2*Q_avg - 8*delta

# --- Exact case (δ=0) ---
print("=== EXACT EINSTEIN WITH CONSTANT TWIST Q (δ=0) ===\n")
print(f"{'Q':>6} {'ceiling':>10} {'floor':>8} {'gap':>8} {'blocked':>8}")
for Q in [0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 1.0, 1.5, 2.0]:
    c = ceiling_corrected(0, Q)
    f_val = floor(0, Q)
    gap = f_val - c
    blocked = c < f_val
    print(f"{Q:6.2f} {c:10.4f} {f_val:8.1f} {gap:8.4f} {'YES' if blocked else 'NO':>8}")

# Find exact threshold
try:
    Q_star = brentq(lambda Q: floor(0,Q) - ceiling_corrected(0,Q), 0.01, 2.5)
    print(f"\nExact threshold Q* = {Q_star:.10f}")
    print(f"  ceiling(Q*) = {ceiling_corrected(0, Q_star):.6f}")
    print(f"  floor(Q*) = {floor(0, Q_star):.6f}")
except:
    Q_star = None
    print("\nNo threshold found")

# --- TTCS formula check ---
print("\n=== TTCS VERIFIER FORMULA CHECK ===")
def ceiling_ttcs_verifier(q):
    """From the TTCS verifier: B ≤ [2q/√(3-q) + √(2(3-q)+5q²/(3-q))]²"""
    K = 3 - q
    if K <= 0: return float('inf')
    inner = 2*K + 5*q**2/K
    return (2*q/np.sqrt(K) + np.sqrt(inner))**2

for q in [0, 0.5, 0.8, 0.9, 0.8986, 0.95]:
    c_mine = ceiling_corrected(0, q)
    c_ttcs = ceiling_ttcs_verifier(q)
    f_val = floor(0, q)
    print(f"q={q:.4f}: my={c_mine:.4f}, TTCS={c_ttcs:.4f}, floor={f_val:.1f}, "
          f"agree={abs(c_mine-c_ttcs)<0.01}")

# --- OT theorem (Q=0) recovery ---
print("\n=== OT THEOREM (Q=0) ===")
d87 = brentq(lambda d: floor(d,0) - ceiling_corrected(d,0), 0.2, 0.3)
print(f"Step 87 critical δ* = {d87:.10f}")
for d in [0, 0.1, 0.2, 0.246]:
    c = ceiling_corrected(d, 0)
    f_val = floor(d, 0)
    print(f"  δ={d:.3f}: ceiling={c:.4f}, floor={f_val:.1f}, gap={f_val-c:.4f}")

# --- Combined (Q,δ) threshold curve ---
print("\n=== COMBINED (Q, δ) THRESHOLD ===")
for Q in [0, 0.2, 0.4, 0.6, 0.8, 0.9]:
    try:
        d_star = brentq(lambda d: floor(d,Q) - ceiling_corrected(d,Q), 0.001, 0.5)
        print(f"Q={Q:.1f}: critical δ* = {d_star:.6f}")
    except:
        print(f"Q={Q:.1f}: no critical δ in [0,0.5]")

# --- Key structural result about exact twist ---
print("\n=== STRUCTURAL CONSTRAINT ON EXACT TWIST ===")
print("For exact Einstein with exact OT open ends (F=0 on an open set):")
print("  Maxwell conservation => q = 0 globally => F ≡ 0")
print("  So exact twist is INCOMPATIBLE with exact cusp-open-set extensions.")
print("  The Q* threshold applies to approximately OT or non-exact-cusp settings.")

# --- Save results ---
results = {
    'sign_correction_applied': {
        'direct_base_twist': '-Qγ (confirmed)',
        'drift_curvature': '(-3+Q)γ + ½dσ² + ½A (FAVORABLE: +Q from solving Einstein eq)',
        'bochner_reaction': 'e - 6 + 2Q (FAVORABLE with twist)',
        'resolvent_mass': 'κ = 6 - 2Q + 2δ (LOWER = better)',
        'effective_K': '3 - Q + δ (BETTER curvature bound with twist)',
        'my_original_error': 'Failed to flip sign when moving -Qγ to other side of Einstein eq',
    },
    'corrected_formulas': {
        'area': 'Lσ = 6 + Q',
        'base': 'Ric_B - Hessσ = (-3+Q)γ + ½dσ² + ½A + E_B',
        'orbit_tension': '|S_F|² = Q² (diagonal one-charge)',
        'bochner': '½Le ≥ ½e(e-6+2Q) + div_σV - Q²',
        'resolvent': '(-L+κ)e ≤ κ²+2f²-2div_σV, κ=6-2Q+2δ, f=Q+2δ',
    },
    'exact_threshold': {
        'Q_star': float(Q_star) if Q_star else None,
        'Q0_ceiling': 6.0,
        'Q0_floor': 12.0,
        'interpretation': 'Twist STRENGTHENS the obstruction for Q < Q*',
    },
    'step87_Q0': float(d87),
    'structural': 'Exact OT open ends force q=0 hence F≡0; twist requires approximate or asymptotic ends',
    'ttcs_generator_retrospective': 'The TTCS Step88 generator final formula was CORRECT despite sloppy intermediate sign reasoning; the drift curvature IS +Qγ',
}

out_path = Path('workspace/data/step89_corrected_twist_resolvent.json')
with open(out_path, 'w') as fp:
    json.dump(results, fp, indent=2, default=str)

print(f"\nwrote {out_path}")

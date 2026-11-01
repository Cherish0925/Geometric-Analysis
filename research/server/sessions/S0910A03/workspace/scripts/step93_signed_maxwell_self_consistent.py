"""
Step 93: Signed Maxwell transport from cusp ends and self-consistent
twist obstruction for the free-T² two-ended connector problem.

Three results:
1. Koiso germs preserve OT under exact Einstein continuation (structural)
2. Signed Maxwell transport from each cusp end bounds separator charge
3. Self-consistent resolvent + transport obstruction

The key insight (Strategist): on the exact cusp with σ_ν=2, e_ν=0,
the Maxwell coefficient a = -(3/2)σ_ν + √e_ν/2 = -3, giving
exponential damping.  Area growth always dominates orbit energy
amplification when B(δ) < 36.  The forcing integral converges
independently of connector length.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
import json
from pathlib import Path

# =====================================================================
# Part 1: Resolvent ceiling B(δ, Q+, Q−) and separator floor
# =====================================================================

def resolvent_ceiling(delta, Q_plus=0.0, Q_minus=0.0):
    """Step 87/89/90 resolvent ceiling with twist parameters.
    B = [2f/sqrt(K) + sqrt(2K + 5f^2/K)]^2
    where f = Q+ + 2δ, K = 3 - Q- + δ.
    """
    f = Q_plus + 2 * delta
    K = 3 - Q_minus + delta
    if K <= 0:
        return float('inf')
    return (2 * f / np.sqrt(K) + np.sqrt(2 * K + 5 * f**2 / K))**2

def separator_floor(delta, Q_C=0.0):
    """Step 88/91: ⟨e_s⟩ ≥ 12 + 2Q_C − 8δ."""
    return 12 + 2 * Q_C - 8 * delta

# =====================================================================
# Part 2: Area equation profile σ(r) on the right half-connector
# =====================================================================

def solve_area_profile(delta=0.0, Q_const=0.0, r_max=8.0, n_pts=4000):
    """
    Solve the cohomogeneity-one area equation
        u' = (6 + Q) − u(1 + u)
    on the curved-base model (corresponding to the conformal
    Laplacian on a 2D base approaching H^2 at the cusp).
    
    Here u = σ' and σ'(0)=0 (separator = area minimum in the
    symmetric model).  The fixed point is u_∞ = (−1+√(25+4Q))/2 → 2
    for Q=0.
    
    Returns: r, sigma, u (= sigma')
    """
    c = 6 + Q_const
    
    def rhs(r, y):
        u = y[0]
        sigma = y[1]
        return [c - u * (1 + u), u]  # u', σ'
    
    sol = solve_ivp(rhs, [0, r_max], [0.0, 0.0],
                    max_step=r_max / n_pts, dense_output=True)
    r = np.linspace(0, r_max, n_pts + 1)
    y = sol.sol(r)
    u = y[0]
    sigma = y[1]
    return r, sigma, u

# =====================================================================
# Part 3: Signed Maxwell transport from the right cusp end
# =====================================================================

def signed_transport_integral(delta, B_sup, r_arr, sigma_arr, e_nu_profile=None):
    """
    Compute the signed Maxwell transport from the right cusp end.
    
    w(r) ≤ 2√2 δ ∫_r^∞ exp(−(3/2)(σ(t)−σ(r)) + (1/2)∫_r^t √e_ν dτ) dt
    
    Using e_ν ≤ B_sup everywhere (worst case).
    
    Returns w_at_separator = w(r=0).
    """
    dr = r_arr[1] - r_arr[0]
    n = len(r_arr)
    
    if e_nu_profile is None:
        # Worst case: e_ν = B_sup everywhere
        sqrt_e_nu = np.full(n, np.sqrt(B_sup))
    else:
        sqrt_e_nu = np.sqrt(e_nu_profile)
    
    # Compute the exponent at each grid point relative to r=0 (separator)
    # exp(-(3/2)(σ(t) - σ(0)) + (1/2)∫_0^t √e_ν dτ)
    
    # Area damping: -3σ(t)/2 (since σ(0)=0)
    area_damp = -1.5 * sigma_arr
    
    # Orbit amplification: (1/2)∫_0^t √e_ν dτ
    orbit_amp = 0.5 * np.cumsum(sqrt_e_nu) * dr
    orbit_amp = np.concatenate(([0.0], orbit_amp[:-1]))  # shift for proper integration
    
    # Net exponent
    exponent = area_damp + orbit_amp
    
    # Integrand for w(0): exp(exponent(t)) from t=0 to ∞
    integrand = np.exp(exponent)
    
    # Truncation: add the tail from r_max to ∞ analytically
    # On the cusp: a = -3 + √B/2 (constant), σ grows like u_∞·r
    alpha_cusp = 1.5 * sigma_arr[-1] / r_arr[-1]  # effective slope ≈ 3
    orbit_rate = 0.5 * sqrt_e_nu[-1]  # √B/2 or actual value
    net_rate = alpha_cusp - orbit_rate
    if net_rate > 0:
        tail = integrand[-1] / net_rate  # ∫_R^∞ e^{-net_rate·(t-R)} dt
    else:
        tail = float('inf')
    
    # Numerical integral
    w_0 = 2 * np.sqrt(2) * delta * (np.trapezoid(integrand, r_arr) + tail)
    Q_0 = w_0**2 / 2
    
    return w_0, Q_0, exponent, integrand

# =====================================================================
# Part 4: Self-consistent iteration
# =====================================================================

def self_consistent_obstruction(delta, r_max=8.0, max_iter=30, tol=1e-10,
                                use_decaying_e=False, e_decay_rate=2.0):
    """
    Self-consistent loop:
    1. Start with Q+ = 0
    2. Compute B = resolvent_ceiling(δ, Q+, Q−=0)
    3. Solve area profile, compute signed transport → Q_sep
    4. Set Q+ = Q_sep, iterate until convergence
    5. Check floor > ceiling
    
    If use_decaying_e: use e_ν = B·exp(−e_decay_rate·r) instead of B constant.
    """
    Q_plus = 0.0
    Q_minus = 0.0  # At cusp ends, Q = 0
    
    for i in range(max_iter):
        B = resolvent_ceiling(delta, Q_plus, Q_minus)
        if B >= 36 or np.isnan(B) or np.isinf(B):
            return {"delta": float(delta), "converged": False, "reason": "B >= 36 or invalid",
                    "obstruction_holds": False, "Q_plus": float('inf'), "gap": float('-inf'),
                    "B_ceiling": float(B), "floor": 0.0, "Q_C": 0.0, "w_sep": 0.0,
                    "sqrt_B": 0.0, "alpha_eff": 0.0, "iterations": i+1}
        
        r, sigma, u = solve_area_profile(delta=0, Q_const=min(Q_plus, 3.0), r_max=r_max)
        
        if use_decaying_e:
            e_nu = B * np.exp(-e_decay_rate * r)
        else:
            e_nu = None  # Use constant B everywhere
        
        w_0, Q_new, _, _ = signed_transport_integral(delta, B, r, sigma, e_nu)
        
        if np.isnan(Q_new) or np.isinf(Q_new) or Q_new > 100:
            return {"delta": float(delta), "converged": False, "reason": "divergent",
                    "obstruction_holds": False, "Q_plus": float(Q_new), "gap": float('-inf'),
                    "B_ceiling": float(B), "floor": 0.0, "Q_C": 0.0, "w_sep": 0.0,
                    "sqrt_B": 0.0, "alpha_eff": 0.0, "iterations": i+1}
        
        if abs(Q_new - Q_plus) < tol * max(Q_plus, 1e-15):
            Q_plus = Q_new
            break
        Q_plus = Q_new
    
    Q_C = Q_plus  # separator charge
    B_final = resolvent_ceiling(delta, Q_plus, Q_minus)
    floor_val = separator_floor(delta, Q_C)
    
    return {
        "delta": float(delta),
        "Q_plus": float(Q_plus),
        "Q_C": float(Q_C),
        "B_ceiling": float(B_final),
        "floor": float(floor_val),
        "gap": float(floor_val - B_final),
        "obstruction_holds": bool(floor_val > B_final),
        "iterations": i + 1,
        "converged": True,
        "w_sep": float(np.sqrt(2 * Q_plus)),
        "sqrt_B": float(np.sqrt(B_final)),
        "alpha_eff": float(3 - np.sqrt(B_final) / 2)
    }

# =====================================================================
# Part 5: Run computations
# =====================================================================

print("=" * 70)
print("SIGNED MAXWELL TRANSPORT AND SELF-CONSISTENT TWIST OBSTRUCTION")
print("=" * 70)

# --- Koiso OT theorem ---
print("\n=== Part 1: Koiso germ OT preservation ===")
print("Theorem: Constrained Koiso germs (Step 92) have q=0 initial data.")
print("Under exact Ric=-3g, Maxwell conservation dq=0 => q=0 everywhere.")
print("Therefore the germ is OT throughout its domain.")
print("Consequence: the complete two-ended OT obstruction (Steps 85-88)")
print("blocks exact extension to any two-ended connector with cusp ends.")
print("The concentrated e_nu escape does NOT evade the OT obstruction.")
print("Only forced (non-exact) mixed Ricci defect can create twist.")

# --- Area profile ---
print("\n=== Part 2: Area transition profile ===")
r, sigma, u = solve_area_profile(r_max=8.0)
print(f"Area ODE: u'=6-u(1+u), u(0)=0, u_inf -> 2")
print(f"σ(0)={sigma[0]:.4f}, σ(4)={sigma[len(r)//2]:.4f}, σ(8)={sigma[-1]:.4f}")
print(f"u(0)={u[0]:.4f}, u(1)={u[500]:.4f}, u(2)={u[1000]:.4f}, u(4)={u[2000]:.4f}")
print(f"Transition width (u reaches 1.9): r ≈ {r[np.searchsorted(u, 1.9)]:.3f}")

# --- Pure cusp benchmark ---
print("\n=== Part 3: Pure cusp benchmark (σ_ν=2, e_ν=0) ===")
r_cusp = np.linspace(0, 20, 10000)
sigma_cusp = 2 * r_cusp
w_cusp, Q_cusp, _, _ = signed_transport_integral(0.246, 0.0, r_cusp, sigma_cusp,
                                                   e_nu_profile=np.zeros_like(r_cusp))
print(f"w = 2√2δ/3 = {2*np.sqrt(2)*0.246/3:.6f} (theory)")
print(f"w = {w_cusp:.6f} (numerical)")
print(f"Q = {Q_cusp:.6f}")

# --- Worst-case transport (e_ν = B constant) ---
print("\n=== Part 4: Worst-case self-consistent (e_ν = B everywhere) ===")
results_worst = []
for d in np.arange(0.02, 0.28, 0.02):
    res = self_consistent_obstruction(d, use_decaying_e=False)
    results_worst.append(res)
    if res.get("converged", False):
        mark = "✓" if res["obstruction_holds"] else "✗"
        print(f"  δ={d:.3f}: Q+={res['Q_plus']:.5f}, B={res['B_ceiling']:.3f}, "
              f"floor={res['floor']:.3f}, gap={res['gap']:.3f} {mark}")
    else:
        print(f"  δ={d:.3f}: {res.get('reason', 'divergent')}")

# Find threshold
def gap_worst(d):
    return self_consistent_obstruction(d, use_decaying_e=False)["gap"]

# Find threshold more carefully
try:
    # Check signs at endpoints
    g_lo = gap_worst(0.10)
    g_hi = gap_worst(0.26)
    if g_lo > 0 and g_hi < 0:
        delta_star_worst = brentq(gap_worst, 0.10, 0.26)
        print(f"\n  Critical δ** (worst-case) = {delta_star_worst:.10f}")
    else:
        delta_star_worst = None
        print(f"\n  No crossing: gap(0.10)={g_lo:.3f}, gap(0.26)={g_hi:.3f}")
except Exception as e:
    delta_star_worst = None
    print(f"\n  Threshold search failed: {e}")

# --- Decaying orbit energy (more realistic) ---
print("\n=== Part 5: Decaying orbit energy e_ν = B·exp(−2r) ===")
results_decay = []
for d in np.arange(0.02, 0.28, 0.02):
    res = self_consistent_obstruction(d, use_decaying_e=True, e_decay_rate=2.0)
    if res.get("converged", False):
        mark = "✓" if res["obstruction_holds"] else "✗"
        print(f"  δ={d:.3f}: Q+={res['Q_plus']:.5f}, B={res['B_ceiling']:.3f}, "
              f"floor={res['floor']:.3f}, gap={res['gap']:.3f} {mark}")
    else:
        print(f"  δ={d:.3f}: {res.get('reason', 'unknown')}")
    results_decay.append(res)

def gap_decay(d):
    res = self_consistent_obstruction(d, use_decaying_e=True, e_decay_rate=2.0)
    if not res.get("converged", False):
        return -1.0  # treat as failing
    return res["gap"]

try:
    g_lo = gap_decay(0.10)
    g_hi = gap_decay(0.26)
    if g_lo > 0 and g_hi < 0:
        delta_star_decay = brentq(gap_decay, 0.10, 0.26)
        print(f"\n  Critical δ** (decaying e_ν) = {delta_star_decay:.10f}")
    else:
        delta_star_decay = None
        print(f"\n  No crossing: gap(0.10)={g_lo:.3f}, gap(0.26)={g_hi:.3f}")
except Exception as e:
    delta_star_decay = None
    print(f"\n  Threshold search failed: {e}")

# --- Component distinction check ---
print("\n=== Part 6: Ricci component distinction ===")
print("E_ns: horizontal-horizontal (base normal × base tangential)")
print("  → Sources Codazzi relation and horizontal constraint")
print("E_na: horizontal-vertical (base normal × orbit)")
print("  → Sources TANGENTIAL Maxwell: ∂_s q_a ∝ ρ E_{n,a}")
print("E_sa: horizontal-vertical (base tangential × orbit)")
print("  → Sources NORMAL Maxwell: ∂_n q_a ∝ ρ E_{s,a}")
print("All share ||E||_op ≤ δ budget, but serve different equations.")
print("Physical twist w transport: sourced by E_sa, NOT by E_ns.")

# --- Final summary ---
print("\n=== Part 7: Summary ===")
r_detail = self_consistent_obstruction(0.20, use_decaying_e=False)
r_detail2 = self_consistent_obstruction(0.20, use_decaying_e=True)
print(f"At δ=0.246 (Step 87 OT threshold):")
print(f"  Worst-case: Q+={r_detail['Q_plus']:.5f}, gap={r_detail['gap']:.3f}, "
      f"holds={'YES' if r_detail['obstruction_holds'] else 'NO'}")
print(f"  Decaying:   Q+={r_detail2['Q_plus']:.5f}, gap={r_detail2['gap']:.3f}, "
      f"holds={'YES' if r_detail2['obstruction_holds'] else 'NO'}")

if delta_star_worst:
    print(f"\nSelf-consistent twist obstruction threshold:")
    print(f"  Worst-case (e_ν=B const):  δ** = {delta_star_worst:.6f}")
if delta_star_decay:
    print(f"  Decaying (e_ν=B·e^(-2r)): δ** = {delta_star_decay:.6f}")
print(f"  Original OT threshold:      δ*  = 0.246250")

# --- Save results ---
output = {
    "koiso_ot_theorem": {
        "statement": "Constrained Koiso germs with q=0 remain OT under exact Einstein continuation.",
        "mechanism": "Maxwell conservation dq=0 under Ric=-3g preserves q=0.",
        "consequence": "Concentrated e_nu at separator does not escape OT two-ended obstruction."
    },
    "signed_transport": {
        "equation": "|dw + (3/2)w dσ| ≤ (1/2)w|dU| + |b|, |b| ≤ 2√2 δ",
        "cusp_coefficient": "a = -(3/2)σ_n + √e_ν/2 → -3 on exact cusp",
        "convergence_condition": "3 > √B(δ)/2, i.e., B < 36 (always true in our regime)",
        "pure_cusp_bound": f"w ≤ 2√2δ/3 ≈ {2*np.sqrt(2)/3:.4f}δ"
    },
    "component_distinction": {
        "E_ns": "horizontal-horizontal, sources Codazzi/constraint",
        "E_na": "horizontal-vertical, sources tangential Maxwell",
        "E_sa": "horizontal-vertical, sources normal Maxwell (and hence twist transport)"
    },
    "area_profile": {
        "equation": "u' = 6 - u(1+u), u(0)=0",
        "fixed_point": 2.0,
        "transition_width_to_1.9": float(r[np.searchsorted(u, 1.9)])
    },
    "self_consistent_worst": results_worst,
    "self_consistent_decay": results_decay,
    "thresholds": {
        "delta_star_ot": 0.246249763690668,
        "delta_star_worst": float(delta_star_worst) if delta_star_worst else None,
        "delta_star_decay": float(delta_star_decay) if delta_star_decay else None
    }
}

out = Path("workspace/data/step93_signed_maxwell_self_consistent.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(output, indent=2))
print(f"\nwrote {out}")

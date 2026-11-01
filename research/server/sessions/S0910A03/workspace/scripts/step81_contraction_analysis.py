#!/usr/bin/env python3
"""
Corrected angular-slip energy preservation and contraction analysis.

Bug fix: use analytical derivatives of d(z) and θ(z), not periodic finite
differences, because θ=k₀z is NOT 2π-periodic (it winds k₀ times).
"""
import numpy as np
import json
from pathlib import Path

def main():
    results = {}
    
    Nz = 1024
    z = np.linspace(0, 2*np.pi, Nz, endpoint=False)
    
    k0 = 2  # loop winding number
    sd = np.sqrt(12.0 / k0**2)  # sinh(d*)
    d_star = np.arcsinh(sd)
    cd = np.cosh(d_star)
    cothd = cd / sd
    
    print(f"k₀={k0}, d*={d_star:.4f}, sinh={sd:.4f}, cosh={cd:.4f}, coth={cothd:.4f}")
    
    # ===== Part 1: Angular slip at various k̃ and ε =====
    print("\n=== Angular slip energy preservation (analytical derivatives) ===")
    
    for kt in [1, 2, 3]:
        for eps in [0.01, 0.1, 0.3, 0.5, 1.0]:
            A0 = eps
            B0 = -(k0/kt) * cothd * A0  # angular slip relation
            
            # Center loop: d(z), θ(z)
            d_val = d_star + A0 * np.cos(kt*z)
            theta = k0*z + B0*np.sin(kt*z)
            
            # Analytical derivatives
            d_z = -A0*kt*np.sin(kt*z)
            theta_z = k0 + B0*kt*np.cos(kt*z)
            
            # H² speed² = d_z² + sinh²(d)*θ_z²
            speed_sq = d_z**2 + np.sinh(d_val)**2 * theta_z**2
            
            # orbit energy |A|² = speed²/2 (for constant area)
            Asq = speed_sq / 2
            
            # u'(0,z) = 3 - |A|²(z)
            u_prime = 3.0 - Asq
            
            # First-order variation: speed² = 12 + ε * δ₁ + ε² * δ₂
            # The angular-slip condition cancels δ₁:
            speed_deviation = speed_sq - 12.0
            
            if kt == 1 and eps <= 0.3:
                print(f"k̃={kt}, ε={eps:.2f}: speed²=[{speed_sq.min():.4f},{speed_sq.max():.4f}], "
                      f"dev from 12: max|δ|={np.max(np.abs(speed_deviation)):.4f}, "
                      f"δ/ε²={np.max(np.abs(speed_deviation))/eps**2:.3f}")
                print(f"  u' range: [{u_prime.min():.4f},{u_prime.max():.4f}], "
                      f"mean={u_prime.mean():.6f}")
            
            if kt == 1:
                results[f"slip_kt{kt}_eps{eps}"] = {
                    "speed_sq_range": [float(speed_sq.min()), float(speed_sq.max())],
                    "max_dev": float(np.max(np.abs(speed_deviation))),
                    "dev_over_eps2": float(np.max(np.abs(speed_deviation))/max(eps**2, 1e-15)),
                    "u_prime_range": [float(u_prime.min()), float(u_prime.max())],
                    "u_prime_mean": float(u_prime.mean()),
                }
    
    # Show the O(ε²) scaling explicitly
    print("\n=== O(ε²) scaling verification (k̃=1) ===")
    devs = []
    for eps in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]:
        A0 = eps
        B0 = -(k0/1) * cothd * A0
        d_val = d_star + A0*np.cos(z)
        d_z = -A0*np.sin(z)
        theta_z = k0 + B0*np.cos(z)
        speed_sq = d_z**2 + np.sinh(d_val)**2 * theta_z**2
        dev = np.max(np.abs(speed_sq - 12.0))
        devs.append((eps, dev))
        print(f"ε={eps:.3f}: max|speed²-12| = {dev:.6f}, ratio/ε² = {dev/eps**2:.3f}")
    
    # The ratio should be approximately constant (proving O(ε²) cancellation)
    results["eps2_scaling"] = [(e, d, d/e**2) for e, d in devs]
    
    # ===== Part 2: Isometry control at k̃=k₀ =====
    print("\n=== Isometry control (k̃=k₀=2) ===")
    for eps in [0.1, 0.5, 1.0]:
        A0 = eps
        B0 = -(k0/k0)*cothd*A0  # = -cothd * A0
        d_val = d_star + A0*np.cos(k0*z)
        d_z = -A0*k0*np.sin(k0*z)
        theta_z = k0 + B0*k0*np.cos(k0*z)
        speed_sq = d_z**2 + np.sinh(d_val)**2 * theta_z**2
        dev = np.max(np.abs(speed_sq - 12.0))
        # For the isometry at k̃=k₀: this should also be O(ε²)
        # because the finite isometry preserves the H² metric exactly,
        # but the linearized B₀ only cancels to first order.
        print(f"ε={eps}: max|speed²-12| = {dev:.4f}, ratio/ε² = {dev/eps**2:.3f}")
    
    # ===== Part 3: Non-constant-speed centers =====
    print("\n=== Non-constant-speed centers (variable θ_z, fixed d) ===")
    for c in [0.5, 1.0, 1.5, 1.9]:
        theta_z = k0 + c*np.cos(z)  # variable angular speed
        d_z = np.zeros(Nz)
        d_val = d_star * np.ones(Nz)
        
        speed_sq = d_z**2 + np.sinh(d_val)**2 * theta_z**2
        Asq = speed_sq / 2
        u_prime = 3.0 - Asq
        
        frac_pos = np.mean(u_prime > 0)
        print(f"c={c}: speed²=[{speed_sq.min():.2f},{speed_sq.max():.2f}], "
              f"u' range=[{u_prime.min():.2f},{u_prime.max():.2f}], "
              f"mean u'={u_prime.mean():.4f}, frac(u'>0)={frac_pos:.3f}")
        
        results[f"nonconst_c{c}"] = {
            "speed_sq_range": [float(speed_sq.min()), float(speed_sq.max())],
            "u_prime_range": [float(u_prime.min()), float(u_prime.max())],
            "u_prime_mean": float(u_prime.mean()),
            "frac_positive": float(frac_pos),
        }
    
    # ===== Part 4: Universal contraction theorem (corrected) =====
    print("\n=== Universal contraction theorem ===")
    print("For constant-area (h=0) and R(q₀)=-6:")
    print("  ⟨|A|²⟩_z = 6 (exact, from scalar curvature)")
    print("  ⟨u'(0)⟩_z = 3 - 6 = -3 (universal)")
    print("  This is independent of loop shape/speed distribution")
    print("")
    print("Angular slip (k̃<k₀) cancels first-order energy variation:")
    print("  speed² = 12 + O(ε²)  [verified numerically]")
    print("  u'(0,z) = -3 + O(ε²) everywhere [not just on average]")
    print("")
    print("For non-constant-area (h≠0):")
    print("  R = -2h' - |A|² - h² (for flat T² orbits)")
    print("  ⟨R⟩ = -⟨|A|²⟩ - ⟨h²⟩ = -6")
    print("  ⟨|A|²⟩ = 6 - ⟨h²⟩")
    print("  ⟨u'(0)⟩ = 3 - ⟨|A|²⟩ = -3 + ⟨h²⟩")
    print("  Expansion requires ⟨h²⟩ > 3, i.e., h_rms > √3 ≈ 1.73")
    
    # ===== Part 5: VII₀ collapse summary =====
    print("\n=== VII₀ collapse summary ===")
    print("For all tested k (2,3,4,6,8):")
    print("  Exact Einstein evolution collapses at r_c ≈ 0.24-0.36")
    print("  a → 0 (z-circle), d → ∞ (orbit anisotropy), K → ∞")
    print("  The cascade: K>3 → u'<0 → a↓ → K↑ → catastrophic feedback")
    print("")
    print("  Defect δ=3 makes u'(0)=0 (neutral), not enough to reverse cascade")
    print("  Step 78 barrier: for δ≤3/5, protected region (u<0, d'>0, K>K₀)")
    print("")
    print("Key conclusion:")
    print("  The graph construction needs defect O(1) at the center to prevent collapse.")
    print("  But ||E||_∞ → 0 requires the defect to vanish everywhere.")
    print("  Unless the center can be bypassed or the 2-variable case is fundamentally different,")
    print("  the graph-manifold route cannot produce vanishing Ricci defect.")
    
    results["conclusion"] = {
        "angular_slip_cancellation": "O(eps^2) verified",
        "u_prime_universal": "-3 for all constant-area R=-6 centers",
        "expansion_from_area": "requires h_rms > sqrt(3)",
        "vii0_collapse_radius": "0.24-0.36 for all k",
        "defect_for_neutral": 3.0,
        "step78_barrier": "delta <= 3/5",
        "graph_route_status": "blocked at center unless z-dependent escape exists",
    }
    
    out = Path(__file__).resolve().parents[1] / 'data' / 'step81_contraction_analysis.json'
    out.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f"\nwrote {out}")

if __name__ == '__main__':
    main()

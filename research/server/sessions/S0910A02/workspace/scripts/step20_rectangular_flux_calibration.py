"""
Step 20: Rectangular (m=4) flux calibration — seed vs. actual minimum.

For the RECTANGLE (flat base, separated solution), the Einstein system
forces a minimum flux that can be computed exactly.
Compare with the formal seed flux to demonstrate the gap.

This calibration shows that the GLOBAL system is far more constraining
than the LOCAL rod/corner data alone.
"""
import numpy as np
import json, os

# =============================================
# PART A: Exact rectangular minimum
# =============================================
# p = (L_x/pi) sin(pi x/L_x), q = (L_y/pi) sin(pi y/L_y)
# Eigenvalue constraint: pi^2/L_x^2 + pi^2/L_y^2 = 2
# 
# w = pq, int w = 4 L_x^2 L_y^2 / pi^4
# Total flux = 2 int w = 8 L_x^2 L_y^2 / pi^4
# 
# Minimize flux subject to constraint:
# Let a = L_x^2, b = L_y^2. Then 1/a + 1/b = 2/pi^2.
# Flux = 8ab/pi^4.
# By AM-GM on 1/a, 1/b: (1/a)(1/b) <= (1/a + 1/b)^2/4 = 1/pi^4
# So ab >= pi^4, with equality iff a = b = pi^2 (L_x = L_y = pi).
# Min flux = 8 pi^4 / pi^4 = 8.

# Rod flux decomposition for the square L_x = L_y = pi:
# On a p-rod (x=0): -d_nu w = q sin(pi y / pi) = q sin y.
# q(y) = sin y. Rod flux = int_0^pi sin y dy = 2.
# 4 rods * 2 = 8. ✓

Lx_sq = np.pi
flux_min_rectangle = 8.0  # exactly 8 for the square
vol_min_rectangle = 4 * np.pi**2 * 4  # 4 pi^2 * int_w = 4 pi^2 * 4 = 16 pi^2
int_w_min = 4.0  # int_Omega w = total_flux/2 = 4

# Aspect ratio scan:
aspect_ratios = np.linspace(0.3, 3.0, 100)
fluxes = []
for alpha in aspect_ratios:
    # L_x^2 = alpha * L_y^2, constraint: 1/(alpha L_y^2) + 1/L_y^2 = 2/pi^2
    # L_y^2 = pi^2 (1 + 1/alpha) / 2
    Ly2 = np.pi**2 * (1 + 1/alpha) / 2
    Lx2 = alpha * Ly2
    flux = 8 * Lx2 * Ly2 / np.pi**4
    fluxes.append(flux)

print("=== RECTANGULAR (m=4) FLUX ===")
print(f"Minimum flux = {flux_min_rectangle} (at square L_x = L_y = pi)")
print(f"Minimum int_w = {int_w_min}")
print(f"Minimum Vol_4 = {vol_min_rectangle:.4f} = 16 pi^2 = {16*np.pi**2:.4f}")
print(f"Rod flux at minimum = 2 per rod (4 rods)")
print(f"Flux at aspect 2:1 = {fluxes[np.argmin(np.abs(aspect_ratios - 2))]:.4f}")
print(f"Flux at aspect 3:1 = {fluxes[np.argmin(np.abs(aspect_ratios - 3))]:.4f}")

# =============================================
# PART B: Seed formal flux for m = 4, 6, 8, 10
# =============================================
print("\n=== SEED vs. ACTUAL (m=4) ===")
for m in [4, 6, 8, 10, 20, 50, 100]:
    A = m**2
    omega = np.sqrt(1 + 2*A)
    flux_per_rod = 2 / (1 + 2*A)
    total_flux_seed = m * flux_per_rod
    int_w_seed = total_flux_seed / 2
    vol_seed = 4 * np.pi**2 * int_w_seed
    
    # For m=4: compare with actual minimum
    if m == 4:
        ratio = flux_min_rectangle / total_flux_seed
        print(f"m={m}: seed total flux = {total_flux_seed:.6f}, "
              f"actual min = {flux_min_rectangle:.1f}, "
              f"ratio = {ratio:.1f}x")
        print(f"  seed int_w = {int_w_seed:.6f}, actual min int_w = {int_w_min:.1f}")
        print(f"  seed vol = {vol_seed:.4f}, actual min vol = {vol_min_rectangle:.2f}")
    else:
        print(f"m={m:>3}: seed total flux = {total_flux_seed:.6f}, "
              f"seed int_w = {int_w_seed:.6f}, "
              f"seed vol = {vol_seed:.6f}")

# =============================================
# PART C: What the m=4 gap means
# =============================================
print("\n=== SCIENTIFIC INTERPRETATION ===")
print("For m=4 (S^2 x S^2):")
print("  The seed with A=16, K_B|edge=-16 gives total flux 0.242")
print("  The actual Einstein system forces flux >= 8 (the flat square)")
print("  Gap factor: 33x")
print()
print("This demonstrates that the global system is FAR more constraining")
print("than the local rod/corner data. The local seed passes all rod ODE,")
print("corner smoothness, and low-order Ricci matching tests, yet the")
print("actual minimum flux is 33 times larger.")
print()
print("The mechanism: the eigenvalue equation -Delta_B w = 2w on the")
print("polygon, combined with the v-equation div(w nabla v) = 0 and")
print("the traceless horizontal equation, forces the base to be")
print("nearly flat for m=4, making the rods long and the flux large.")
print()
print("KEY QUESTION: Does this gap persist for m >= 6?")
print("  If I_m := min flux >= c > 0 uniformly in m, that is the")
print("  chi-uniform volume gap (BUILD).")
print("  If I_m -> 0, BREAK survives but does not refute Yau-26")
print("  because Einstein existence on #_k(S^2 x S^2) is unknown.")

# =============================================
# PART D: Conservation law / energy identity
# =============================================
print("\n=== FLUX-ENERGY IDENTITY ===")
print("For separated rectangles: flux = 8 L_x^2 L_y^2 / pi^4")
print("Under pi^2/L_x^2 + pi^2/L_y^2 = 2:")
print("  By AM-GM: L_x^2 L_y^2 >= pi^4 (equality at square)")
print("  So flux >= 8 (chi-uniform for the rectangular sub-class)")
print()
print("For general m-gons, an analogous identity would need:")
print("  (a) An energy representation of total flux in terms of w, v, g_B")
print("  (b) A lower bound using the eigenvalue, Gauss-Bonnet, and unit closure")
print("  (c) Handling of the v-equation's singular boundary behavior")

# Save
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "step20_rectangular_flux_calibration.json")
report = {
    "title": "Step 20 rectangular flux calibration",
    "m4_rectangle": {
        "min_flux": 8,
        "min_int_w": 4,
        "min_vol4": float(16 * np.pi**2),
        "at_square_Lx_eq_Ly_eq_pi": True,
        "rod_flux_at_minimum": 2,
        "proof": "AM-GM on ab >= pi^4 under 1/a+1/b = 2/pi^2"
    },
    "m4_seed": {
        "A": 16,
        "omega": float(np.sqrt(33)),
        "flux_per_rod": 2/33,
        "total_flux": 8/33,
        "int_w": 4/33,
        "vol4": float(4 * np.pi**2 * 4/33)
    },
    "gap_ratio_m4": float(8 / (8/33)),
    "scientific_conclusion": "The m=4 actual minimum flux is 33x the seed flux. "
        "The global reduced Einstein system is far more constraining than "
        "local rod/corner matching alone. The BUILD/BREAK fork for m >= 6 "
        "hinges on whether this rigidity persists as m grows."
}
with open(OUT, 'w') as f:
    json.dump(report, f, indent=2)
print(f"\nSaved {OUT}")

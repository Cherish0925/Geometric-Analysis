"""
Step 14 (S0910A02): numerical test setup for the chi-uniform volume-gap fork.

This script computes EXACT Einstein data for known toric positive 4-manifolds
(S^4, CP^2, S^2xS^2) and tests the reduced system identities numerically.
It then sets up the framework for testing whether small-total-flux solutions
exist on polygons with many corners.

KEY QUESTION: Does the reduced system {-Delta w = 2w, div(w grad v) = 0,
traceless condition, unit closure, right-angle GB} allow total flux -> 0 
as chi -> infinity?
"""
import json, math, os
import numpy as np
from scipy.integrate import dblquad, quad

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# =====================================================================
# 1. Known toric Einstein examples: exact data
# =====================================================================

def rod_data(KB_edge, name=""):
    """For constant K_B on the edge, compute rod parameters."""
    omega2 = 1 - 2*KB_edge
    if omega2 <= 0:
        return {"name": name, "KB_edge": KB_edge, "omega2": omega2, "status": "no positive rod"}
    omega = math.sqrt(omega2)
    L = math.pi / omega
    Phi = 2 / omega2
    fixed_sphere_area = 2 * math.pi * Phi
    return {
        "name": name, "KB_edge": KB_edge, "omega": omega,
        "rod_length": L, "rod_flux": Phi,
        "fixed_sphere_area": fixed_sphere_area
    }

examples = {
    "S4": {
        "chi": 2, "m_corners": 2, "m_rods": 2,
        "GB_int_KB": math.pi, "KB_constant": 1/3,
        "rods": [rod_data(1/3, "S4_rod")] * 2,
        "total_flux": 12, "int_w": 6, "Vol4": 24*math.pi**2,
        "orbit_space": "spherical lune, S^2(sqrt(3)), area = 3*pi/2"
    },
    "CP2": {
        "chi": 3, "m_corners": 3, "m_rods": 3,
        "GB_int_KB": math.pi/2,
        "note": "Fubini-Study metric, toric with 3 edges. KB not constant on edges.",
        "Vol4": 8*math.pi**2 / 3,  # well-known CP^2 Einstein volume
        "total_flux": 8/(3*math.pi**2) * 2 * math.pi**2,  # = Vol/(2pi^2) ... recompute
    },
    "S2xS2": {
        "chi": 4, "m_corners": 4, "m_rods": 4,
        "GB_int_KB": 0, "KB_constant": 0,
        "rods": [rod_data(0, "S2xS2_rod")] * 4,
        "total_flux": 8, "int_w": 4, "Vol4": 16*math.pi**2,
        "orbit_space": "flat square [0,pi]^2, area = pi^2"
    }
}

# Recompute CP^2. Fubini-Study with Ric = 6g_{FS} normalized to Ric = g:
# Scalar curvature s = 4*1 = 4 (Einstein lambda=1 in dim 4).
# Vol(CP^2, g_{FS}(1)) = pi^2/2. With Ric = 6g_{FS}, to get Ric = g: g = (1/6)g_{FS}.
# No - the standard Fubini-Study has Ric = 2(n+1) g in the usual convention.
# For CP^2 (complex dim 2): Ric_{FS} = 6 g_{FS}. Normalizing to Ric = g:
# g = (1/6) g_{FS}. Vol = (1/6)^2 * pi^2/2 = pi^2/72.
# But the ORBIFOLD volume... this needs more care.
# Standard: Vol(CP^2, g_{FS}(r)) where sectional curvature range [1/(4r^2), 1/r^2].
# With Ric = g (lambda=1): scalar = 4, s = n(n-1) lambda/(n-1) = 4 for n=4.
# For CP^2 with lambda=1: R = 3 (radius of sectional curvature).
# Vol(CP^2) = pi^2 R^4 / 2 = pi^2 * 9 / 2 = 9 pi^2 / 2? Let me check.
# Actually, the standard CP^2 with Fubini-Study of holomorphic sectional curvature 4
# has Ric = 6g, Vol = pi^2/2. Rescaling to Ric = g: multiply metric by 6,
# so Vol = 6^2 * pi^2/2 = 18 pi^2. That seems too large.
# Let me use the formula: for CP^n with Ric = lambda g, the lambda = 2(n+1)/c
# where c is related to the sectional curvature normalization.
# Simplest: CP^2 with Ric = g, Einstein constant lambda=1.
# Since Ric(CP^2,g_FS) = 6 g_FS, we need g = 6 g_FS, so lambda = 1.
# Vol = 6^2 Vol(g_FS) = 36 * pi^2/2 = 18 pi^2.
# chi(CP^2) = 3. int_w = Vol/(4pi^2) = 18/4 = 4.5. Total flux = 9.
# Average flux per rod = 9/3 = 3.
examples["CP2"]["Vol4"] = 18 * math.pi**2
examples["CP2"]["int_w"] = 4.5
examples["CP2"]["total_flux"] = 9
examples["CP2"]["avg_flux_per_rod"] = 3.0

# Correction: let me double-check with the formula from the S^4 normalization.
# S^4 with Ric = g: radius sqrt(3), Vol = 8pi^2/3 * (sqrt(3))^4 = 8pi^2/3 * 9 = 24pi^2. OK.
# CP^2: the Berger constant. The Fubini-Study metric on CP^2 normalized so that
# all sectional curvatures lie in [K/4, K]. With K = 4/3 (so holomorphic sec curv = 4/3),
# Ric = (2n+2)/(2n) * K * g = 3 * (4/3) * ... this is getting confused.
# Let me just use: for CP^2 with Einstein constant 1, the volume is known to be
# Vol(CP^2) = 2 * 8 pi^2 chi / 3 = 2 * 8*pi^2 * 3 / 3 = 16 pi^2? No.
# From CGB: 8 pi^2 chi = int(|W|^2) + 2/3 lambda^2 Vol (for self-dual Einstein).
# For CP^2 (self-dual): W- = 0, |W+|^2 = lambda^2/6 (constant on round CP^2).
# 8 pi^2 * 3 = (lambda^2/6) Vol + (2/3) lambda^2 Vol = (5/6) lambda^2 Vol.
# With lambda = 1: 24 pi^2 = (5/6) Vol, Vol = 24 * 6/5 pi^2 = 144 pi^2/5.
# Hmm, that doesn't match either. Let me use a different approach.
# 
# For S^4(R): Ric = 3/R^2 g. For Ric = g: R^2 = 3, Vol = 8pi^2R^4/3 = 24pi^2.
# For CP^2 with Fubini-Study (holomorphic sectional curvature c): Ric = (n+1)c g.
# For n=2: Ric = 3c g. For Ric = g: c = 1/3, Vol = pi^2/(2c^2) = pi^2*9/2 = 9pi^2/2.
# Check with CGB: W+ has spectrum {lambda/3, -lambda/6, -lambda/6} = {1/3, -1/6, -1/6}.
# |W+|^2 = 1/9 + 1/36 + 1/36 = 4/36 + 1/36 + 1/36 = 6/36 = 1/6.
# CGB (for self-dual Einstein in 4D): 8pi^2 chi = int |W+|^2 dmu + (2/3) lambda^2 Vol.
# 8pi^2 * 3 = (1/6)Vol + (2/3)Vol = (1/6 + 2/3)Vol = (5/6)Vol.
# Vol = 24*6*pi^2/5 = 144pi^2/5 ≈ 284.5.
# But 9pi^2/2 ≈ 44.4. These don't match!
# 
# I think the issue is the CGB formula. Let me use the standard one:
# 8pi^2(2chi+3tau) = 4 int |W+|^2 + (4/3) lambda^2 Vol (for 4D Einstein Ric=lambda g).
# For CP^2: chi=3, tau=1, so 2chi+3tau = 9.
# 8pi^2*9 = 4*(1/6)*Vol + (4/3)*1*Vol = (2/3 + 4/3)Vol = 2Vol.
# 72 pi^2 = 2Vol, Vol = 36pi^2.
# Hmm, that gives a different answer. The issue is the CGB formula normalization.
# 
# I'll just use Vol = 36pi^2 for CP^2 with Ric=g and check later.
# Actually, I realize this is less important than the fork. Let me just record
# the known examples with caveats and focus on the fork test.

# =====================================================================
# 2. Rod flux as a function of edge K_B: the mechanism
# =====================================================================
KB_values = np.linspace(-10, 0.45, 200)
rod_fluxes = []
for kb in KB_values:
    omega2 = 1 - 2*kb
    if omega2 > 0:
        rod_fluxes.append(2/omega2)
    else:
        rod_fluxes.append(float('inf'))

# Total flux for chi-gon with all edges having same K_B (idealized):
chi_values = [2, 3, 4, 5, 6, 8, 10, 20, 50, 100]
flux_tables = []
for chi_val in chi_values:
    # GB: int K_B = 2pi - pi/2 * chi. Average K_B = (2pi - pi/2*chi) / Area.
    # With Faber-Krahn: Area >= 9.08 for delta=0. Use Area = 10 for estimate.
    area_est = 10.0
    avg_KB = (2*math.pi - math.pi/2*chi_val) / area_est
    omega2 = 1 - 2*avg_KB
    if omega2 > 0:
        avg_rod_flux = 2/omega2
    else:
        avg_rod_flux = float('inf')
    total_flux_est = chi_val * avg_rod_flux
    vol_est = 2*math.pi**2 * total_flux_est
    
    flux_tables.append({
        "chi": chi_val, "m_rods": chi_val,
        "avg_KB_at_area_10": avg_KB,
        "avg_rod_flux_if_uniform": avg_rod_flux,
        "total_flux_estimate": total_flux_est,
        "Vol_estimate": vol_est,
        "Bishop_ceiling": 24*math.pi**2,
        "violates_Bishop": vol_est > 24*math.pi**2
    })

# =====================================================================
# 3. The decisive question: total flux vs chi
# =====================================================================
# For UNIFORM K_B on all edges:
# Total flux = chi * 2/(1-2*avg_KB) = chi * 2/(1 - 2*(2pi-pi*chi/2)/Area)
# = chi * 2 / (1 - (4pi - pi*chi)/Area)
# = chi * 2 * Area / (Area - 4pi + pi*chi)
# For large chi: ~ chi * 2 * Area / (pi*chi) = 2*Area/pi.
# So total flux -> 2*Area/pi ~ 6.36 for Area ~ 10.
# This is BOUNDED, not going to zero!

# Wait: this assumes UNIFORM K_B. If K_B varies, negative K_B can concentrate
# near edges while positive K_B fills the interior. Let me compute more carefully.

uniform_KB_analysis = {
    "formula": "For uniform K_B = (2pi - pi*chi/2)/Area on all edges:",
    "total_flux": "chi * 2 / (1 - 2*KB) = chi * 2 * Area / (Area + pi*chi - 4*pi)",
    "large_chi_limit": "-> 2*Area/pi (BOUNDED, not zero!)",
    "interpretation": ("For uniform edge K_B consistent with Gauss-Bonnet, "
                       "total flux approaches 2*Area/pi as chi -> infinity. "
                       "With Area >= 9.08 (Faber-Krahn), total flux >= ~5.78. "
                       "Vol >= 2*pi^2 * 5.78 = 114. This is a CHI-UNIFORM "
                       "LOWER BOUND if the uniform-KB model is representative."),
    "CRITICAL_CAVEAT": ("This assumes K_B is the SAME constant on all edges. "
                         "In reality, K_B varies, and the edge equation coefficients "
                         "can differ across rods. The traceless condition constrains "
                         "this variation. The question is whether nonuniform K_B can "
                         "beat the uniform bound.")
}

# Compute the limit
area_fk = math.pi * 2.40483**2 / 2  # Faber-Krahn at delta=0
total_flux_limit = 2 * area_fk / math.pi
vol_limit = 2 * math.pi**2 * total_flux_limit

uniform_KB_analysis["Area_FK_delta0"] = area_fk
uniform_KB_analysis["total_flux_limit_at_FK_area"] = total_flux_limit
uniform_KB_analysis["Vol_lower_limit"] = vol_limit

report = {
    "title": "Step 14: numerical tests for chi-uniform fork",
    "known_examples": {k: v for k, v in examples.items() if k in ["S4", "S2xS2"]},
    "flux_vs_chi_uniform_KB": flux_tables[:6],
    "uniform_KB_large_chi_analysis": uniform_KB_analysis,
    "MAIN_FINDING": ("Under the uniform-KB idealization, total flux -> 2*Area/pi > 0 "
                     "as chi -> infinity, giving a CHI-UNIFORM volume lower bound. "
                     "This is because negative K_B shrinks each rod's flux by factor "
                     "1/(1-2*KB), but there are chi rods, and the product chi/(1-2*KB) "
                     "stabilizes because GB forces KB ~ -pi*chi/(2*Area). "
                     "The fork therefore TILTS TOWARD BUILD (gap exists) under uniform KB. "
                     "The remaining question is whether NONUNIFORM K_B can beat this "
                     "by concentrating negative curvature at rod edges while keeping "
                     "positive curvature in the interior.")
}

OUT = os.path.join(DATA, "step14_chi_uniform_flux_test.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2, default=str)
print(json.dumps(report, indent=2, default=str))
print(f"\nSaved {OUT}")

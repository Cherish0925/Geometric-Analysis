"""
Step 13 (S0910A02): consistency anchors for the T^2 determinant/spectral route.

This script does not prove the toric volume gap.  It records exact elementary
checks that are hard to reconcile with a sign/factor error:
  * S^4 with Ric=g, radius sqrt(3), T^2 rotations: orbit space is the spherical
    lune r1>=0,r2>=0 in S^2(sqrt(3)); w=r1 r2 has -Delta w=2w;
    int_Omega w=6 and Vol_4=24 pi^2.
  * Gauss--Bonnet corner formula for a disk orbit space with right-angle corners:
    int K_B = 2*pi - (pi/2)*m.
  * C^0-pinched vertical-trace Rayleigh consequence in dimension 4:
    if |Ric-g|_op<=delta, lambda_1^Dir(Omega)<=2(1+delta).
"""
import json, math, os
from fractions import Fraction

SESSION = "Sessions/S0910A02"
OUT = os.path.join(SESSION, "workspace/data/step13_toric_spectral_anchors.json")

R2 = 3.0  # S^4 normalized Ric=g has radius^2 = n-1 = 3
R = math.sqrt(R2)
# Spherical lune 0<=phi<=pi/2, 0<=psi<=pi.  r1=R sin psi cos phi, r2=R sin psi sin phi.
int_sin3_0_pi = Fraction(4, 3)
int_cosphi_sinphi_0_pi2 = Fraction(1, 2)
int_w_exact = Fraction(2, 3) * Fraction(9, 1)  # R^4 * 4/3 * 1/2, R^4=9
vol4_exact_pi2_coeff = 4 * int_w_exact  # Vol=(2pi)^2 int w = 4 pi^2 int w
edge_flux_each = 2 * R2  # integral y ds on one meridian = 2R^2
edge_flux_total = 2 * edge_flux_each
fixed_sphere_area_each_pi_coeff = 4 * R2  # 4*pi*R^2 = 12*pi
fixed_sphere_area_total_pi_coeff = 2 * fixed_sphere_area_each_pi_coeff

# Gauss-Bonnet corner identity samples: m=number of right-angle corners.
gb_samples = []
for name, m in [("S4", 2), ("CP2", 3), ("S2xS2", 4), ("CP2#CPbar2_or_Page_topology", 4), ("CP2#2CPbar2_or_CLW_topology", 5)]:
    gb_samples.append({
        "example": name,
        "corners_chi_fixed_points_m": m,
        "int_K_B_over_pi": 2 - m/2,
        "comment": "For disk orbit space with geodesic edges and right-angle corners. Negative values are allowed; they must be accommodated by edge/rod curvature."
    })

rayleigh_statement = {
    "exact_Einstein": "For T^2-invariant Ric=lambda*g and degeneration boundary, w>0 Dirichlet satisfies (-Delta_B + |F|_h^2/2)w = 2*lambda*w, hence lambda_1^Dir(-Delta_B) <= 2*lambda.",
    "positive_C0_pinched": "If |Ric-g|_op <= delta, then tr_h Ric^V <= 2*(1+delta) and Rayleigh with w gives lambda_1^Dir(-Delta_B) <= 2*(1+delta).",
    "sign_test": "Because lambda_1^Dir(-Delta_B+nonnegative potential)>0, a compact Einstein metric with a T^2 degeneration boundary cannot have lambda<=0. This matches Bochner/no-zero Killing fields."
}

report = {
    "S4_anchor": {
        "ambient_radius_squared_for_Ric_equals_g": R2,
        "orbit_space": "spherical lune in S^2(sqrt(3)) with two right-angle corners",
        "w": "r1*r2 = degree-2 spherical harmonic restricted to lune",
        "laplacian_eigenvalue": "l(l+1)/R^2 = 6/3 = 2, so Delta w = -2w",
        "int_Omega_w_exact": str(int_w_exact),
        "int_Omega_w_float": float(int_w_exact),
        "Vol4_pi2_coefficient": str(vol4_exact_pi2_coeff),
        "Vol4": "24*pi^2",
        "edge_flux_each": edge_flux_each,
        "edge_flux_total": edge_flux_total,
        "check_2_int_w_equals_flux_total": float(2*int_w_exact) == edge_flux_total,
        "fixed_sphere_area_each": "12*pi",
        "fixed_sphere_area_total": "24*pi",
        "flux_times_2pi_equals_total_fixed_sphere_area": f"{edge_flux_total}*2*pi = {fixed_sphere_area_total_pi_coeff}*pi"
    },
    "GB_corner_identity_samples": gb_samples,
    "rayleigh_consequence": rayleigh_statement,
    "caveats": [
        "GB formula assumes orbit space is a disk, edges are geodesic in quotient metric, and all corners have interior angle pi/2; these are local metric facts plus a torus-action topological input requiring source-scoped hypotheses.",
        "The rayleigh inequality is an invariant-class result, not yet the simply connected volume gap required by Proposition A and not yet a general-collapse reduction."
    ]
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(report, f, indent=2)
print(json.dumps(report, indent=2))
print(f"Saved {OUT}")

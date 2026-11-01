"""
Step 20: Global flux-energy identity for the reduced toric system.

Derive integral identities relating total flux to interior energies.
These identities capture why the global system is more constraining
than local rod/corner data.
"""
import sympy as sp
import json, os

# SETUP: exact Einstein reduced system (twist-free diagonal)
# -Delta_B p = (K_B - 1) p,  p = 0 on p-rods, |grad p| = 1
# -Delta_B q = (K_B - 1) q,  q = 0 on q-rods, |grad q| = 1
# <grad p, grad q> = -K_B pq
# w = pq,  v = log(p/q)

# IDENTITY 1: From -Delta p = (K_B - 1)p, multiply by q and integrate
# Using Green: int grad_p . grad_q + int (Delta p) q = int_bdry q (d_nu p)
# So: int grad_p.grad_q - int(K_B - 1)pq = int_bdry q (d_nu p)
# Use <grad p, grad q> = -K_B pq:
# -int K_B pq - int(K_B - 1)pq = int_bdry q (d_nu p)
# -int(2K_B - 1)w = int_bdry q (d_nu p) = -sum Phi_i^p  (flux through p-rods)

# IDENTITY 2: Similarly from -Delta q multiply by p:
# -int(2K_B - 1)w = -sum Phi_j^q

# So: sum Phi_i^p = sum Phi_j^q = int(2K_B - 1)w

# Adding: total_flux = 2 int(2K_B - 1)w

# But also total_flux = 2 int w (from eigenvalue eq).
# Consistency: 2 int(2K_B - 1)w = 2 int w => int K_B w = int w.

# This is a TAUTOLOGY following from the system. But the PARTITION is useful:
# Flux through p-rods = int(2K_B - 1)w dA
# Flux through q-rods = int(2K_B - 1)w dA

# Since the total is 2∫w and each half is ∫(2K_B - 1)w:
# This means: ∫(2K_B - 1)w = ∫w.
# Rearranging: 2∫K_B w = 2∫w, so ∫K_B w = ∫w. ✓

# NEW IDENTITY: From |grad(pq)|^2 = q^2|grad p|^2 + p^2|grad q|^2 + 2pq<grad p, grad q>
# = q^2|grad p|^2 + p^2|grad q|^2 - 2K_B (pq)^2

# Integrate: int|grad w|^2 = int q^2|grad p|^2 + int p^2|grad q|^2 - 2 int K_B w^2

# Also: int|grad w|^2 = 2 int w^2 (Rayleigh quotient with lambda = 2).

# So: 2 int w^2 = int q^2|grad p|^2 + int p^2|grad q|^2 - 2 int K_B w^2  ...(*)

# BOUNDARY DATA: On a p-rod, |grad p| = 1, p = 0, q = Q(s):
# int_p-rods q^2 |grad p|^2 ds = int_p-rods Q^2 ds = sum of "squared rod fluxes"

# Let S_p = int q^2|grad p|^2 dA = INTERIOR part + p-rod boundary part
# The interior contribution of q^2|grad p|^2 involves the INTERIOR values.

# This is getting complicated. Let me use a different approach.

# APPROACH: Pohozaev identity for the eigenvalue equation.
# For -Delta_B w = lambda w on Omega, w = 0 on bdry, use vector field X:
#
# int_bdry (X . nu) (d_nu w)^2 ds 
#   = 2 lambda int w (X . grad w) + int |grad w|^2 div X - 2 int (grad w)^T (DX) (grad w)
#
# For X = position vector on a FLAT domain: div X = 2, DX = I.
# int_bdry (x . nu)(d_nu w)^2 = 2 lambda int w (x . grad w) + 2 int|grad w|^2 - 2 int|grad w|^2
# = 2 lambda int w (x . grad w)
# Integration by parts: int w (x . grad w) = -(1/2) int |grad w|^2 ... no, 
# int (x . grad w) w = -int w div(xw) = -int w (2w + x.grad w) ... circular.

# Let me use the standard Pohozaev directly.
# For -Delta w = lambda w, w = 0 on bdry, in 2D:
# (lambda/2) int (2xw_x + 2yw_y + 2w) w dxdy... 
# Actually the 2D Pohozaev for Dirichlet eigenfunctions on a flat domain is:
# lambda int |x|^2 w^2 = int_bdry (x.nu)(d_nu w)^2 + lambda int w^2  ... (approximately)

# This doesn't give a clean lower bound either.

# CLEANEST APPROACH: Use the INDIVIDUAL p and q equations more carefully.
# p satisfies -Delta p = (K_B - 1) p. Think of this as an eigenvalue problem:
# -Delta p + p = K_B p, i.e., (-Delta + 1) p = K_B p.
# But K_B is not constant, so this is not a standard eigenvalue problem.

# KEY INSIGHT from the v-equation:
# div(w grad v) = 0, with v -> -infty on p-rods, +infty on q-rods.
# Multiply by a test function chi and integrate:
# int w grad v . grad chi = int_bdry chi w (d_nu v) ds
# On the boundary, w = 0, so boundary term = 0 (modulo corner terms).
# So: int w grad v . grad chi = 0 for all chi in C^infty_0(Omega).
# This means: w grad v is divergence-free in the interior.

# The 1-form alpha = w * dv is closed and co-closed: d(*alpha) = 0, d alpha = 0.
# Wait, d(w dv) = dw wedge dv + w d(dv) = dw wedge dv (since d^2v = 0 in 2D).
# And *d*(w dv) = div(w grad v) = 0.
# So w dv is co-closed. It's NOT necessarily closed unless dw wedge dv = 0.

# The dual 1-form: * (w dv) is closed (since div(w grad v) = d*(w dv) = 0).
# So *(w dv) = d psi for some function psi on the simply connected Omega.
# psi is the "stream function" of the weighted flow w grad v.

# The level sets of psi are the integral curves of w grad v.
# Since v -> -infty on p-rods and +infty on q-rods, the flow goes from
# p-rods to q-rods. The stream function psi is constant on each rod.

# The total flux of w grad v from all p-rods to all q-rods equals:
# Psi_total = sum of psi jumps around the polygon.

# From Stokes: integral of *(w dv) over any curve from rod i to rod i+1
# equals psi(rod_{i+1}) - psi(rod_i).

# This gives a quantitative connection between the v-flow and the rod geometry.
# But I need to compute the actual flux of w grad v, not just assert it exists.

# COMPUTATION for the rectangle (S^2 x S^2):
# w = sin x sin y, v = log(sin x / sin y).
# grad v = (cos x / sin x, -cos y / sin y) = (cot x, -cot y).
# w grad v = sin x sin y * (cot x, -cot y) = (cos x sin y, -sin x cos y).
# This is a vector field. Its divergence:
# d/dx(cos x sin y) + d/dy(-sin x cos y) = -sin x sin y - (-sin x sin y) = 0. ✓

# The magnitude |w grad v| = sqrt(cos^2 x sin^2 y + sin^2 x cos^2 y).
# This is bounded and smooth in the interior.

# The total "v-flux" from all p-rods to all q-rods:
# Flux of (cos x sin y, -sin x cos y) across the line x = pi/2:
# int_0^pi cos(pi/2) sin y dy = 0. Hmm.

# Actually the v-flux through the interior should be measured differently.
# On a p-rod (x = 0): w grad v . nu = sin0 siny * (cot0, -coty) . (-1,0)
# = lim_{x->0} sin x sin y cot x * (-1) = -sin y. 
# So the outward v-flux on the x=0 rod = -int sin y dy = -2.
# On a q-rod (y = 0): w grad v . nu = sinx sin0 * (cotx, -cot0) . (0,-1) 
# = lim_{y->0} sinx siny (-coty)(-1) = sinx. 
# Outward v-flux on y=0 rod = int sinx dx = 2.

# Total v-outflux through q-rods = 2+2 = 4, through p-rods = -2-2 = -4. 
# Conservation: net = 0. ✓

# The v-flux through each rod = ±(rod area of SURVIVING fiber)!
# Because on a p-rod: w d_nu v = pq d_nu(log p - log q) = pq (d_nu p/p - d_nu q/q)
# As p -> 0: = q d_nu p - p d_nu q ~ q * 1 = q (the surviving fiber).
# So: v-flux through p-rod = int q ds = Phi_rod. ✓ They're the SAME as the w-flux!

# This means: total flux = total v-flux through rods.
# And the stream function psi of the v-flow has jumps that sum to total flux.

print("=== GLOBAL ENERGY IDENTITY ===")
print("From the v-equation div(w grad v) = 0:")
print("  *(w dv) = d psi (stream function on simply connected Omega)")
print("  v-flux through each rod = rod flux Phi_i")
print("  Total v-flux = total flux = 2 int w")
print()

# The KEY identity: for the stream function psi,
# int |grad psi|^2 dA = int w^2 |grad v|^2 dA
# (This is the Dirichlet energy of psi = energy of w*dv.)

# From K_B = (1/4)(|grad v|^2 - |grad u|^2):
# |grad v|^2 = |grad u|^2 + 4 K_B
# w^2 |grad v|^2 = w^2 |grad u|^2 + 4 K_B w^2

# And int K_B w^2 = int K_B pq pq dA. This involves the WEIGHTED curvature.

# From the Gauss-Bonnet integral: int K_B dA = 2pi - pi*m/2.
# But int K_B w^2 is different: it depends on where w is large vs where K_B is negative.

# For the rectangle: K_B = 0 everywhere. So w^2|grad v|^2 = w^2|grad u|^2.
# int w^2|grad v|^2 = int|grad w|^2/w * w^2 ... hmm, w^2|grad u|^2 = |grad w|^2.
# So int w^2|grad v|^2 = int|grad w|^2 = 2 int w^2. (For K_B = 0.)

# For general K_B: int w^2|grad v|^2 = int|grad w|^2 + 4 int K_B w^2.
# = 2 int w^2 + 4 int K_B w^2.

# And int|grad psi|^2 = int w^2|grad v|^2 = 2 int w^2 + 4 int K_B w^2.

# Now, int|grad psi|^2 >= lambda_1^D(Omega) int psi^2  (Rayleigh quotient of psi).
# But psi has different boundary conditions than w (it's constant on rods, not zero).

# Actually, psi is multi-valued: it increases by Phi_i at each rod.
# On the polygon, psi is a well-defined function with constant values on each rod,
# increasing monotonically around the boundary.

# This is related to the CAPACITY or modulus of the polygon.
# The total oscillation of psi around the boundary is the total flux.

# For a conformal modulus argument: the total flux is related to the conformal
# extremal length of the family of curves from p-rods to q-rods.

print("=== CONFORMAL MODULUS CONNECTION ===")
print("The stream function psi has boundary values:")
print("  psi = 0 on first p-rod, psi = Phi_1 on first q-rod, etc.")
print("  Total oscillation = total flux")
print()
print("The Dirichlet energy of psi: int |grad psi|^2 = int w^2 |grad v|^2")
print("  = 2 int w^2 + 4 int K_B w^2")
print()
print("For the RECTANGLE (K_B = 0): int|grad psi|^2 = 2 int w^2")
print("  = 2 * (4 L_x^2 L_y^2 / pi^4) * (pi^2 / (2*2)) = ... ")
print("  Actually: int w^2 = (L_x L_y / pi^2)^2 * (L_x * L_y) * (1/2)^2")

# int sin^2(pi x/L_x) dx from 0 to L_x = L_x/2
# int sin^4(pi x/L_x) dx from 0 to L_x = 3L_x/8
# int w^2 = (L_x L_y / pi^2)^2 * (L_x/2)(L_y/2) = L_x^3 L_y^3 / (4 pi^4)

# So int|grad psi|^2 = 2 L_x^3 L_y^3 / (4 pi^4) = L_x^3 L_y^3 / (2 pi^4)

# And the total flux = 8 L_x^2 L_y^2 / pi^4.

# Ratio: int|grad psi|^2 / (total_flux)^2 = [L_x^3 L_y^3 / (2 pi^4)] / [64 L_x^4 L_y^4 / pi^8]
# = pi^4 / (128 L_x L_y)

# For L_x = L_y = pi: = pi^4 / (128 pi^2) = pi^2/128 ≈ 0.077.
# So int|grad psi|^2 ≈ 0.077 * 64 = 4.93 for the square.

# The conformal modulus of the rectangle (alternating Dirichlet BCs) is:
# M = int|grad psi|^2 / (delta psi)^2 where delta psi = total flux / 2 (half-oscillation).
# This relates the Dirichlet energy to the oscillation.

# For an annulus of modulus M: M = (1/2pi) log(R_outer/R_inner).
# The modulus bounds the capacity and hence the flux.

# KEY LOWER BOUND IDEA:
# If the conformal modulus of the polygon (with alternating rod BCs) is bounded
# below independently of m, then total_flux >= c * int|grad psi|^2 >= c * 2 int w^2.
# And from Cauchy-Schwarz: (int w)^2 <= Area * int w^2.
# So: total_flux^2 = 4(int w)^2 <= 4 Area * int w^2 <= 4 Area * total_flux / (2c).
# Hence total_flux >= 8c / Area... but if Area is bounded above (which it is, by Bishop),
# then total_flux >= 8c / A_max.

# But this doesn't work directly because the relationship between int|grad psi|^2
# and total_flux depends on the modulus, which varies with geometry.

print("\nFor the rectangle with L_x = L_y = pi:")
Lx, Ly = sp.pi, sp.pi
int_w_sq = Lx**3 * Ly**3 / (4 * sp.pi**4)
int_grad_psi_sq = 2 * int_w_sq
total_flux_rect = 8 * Lx**2 * Ly**2 / sp.pi**4
print(f"  int w^2 = {float(int_w_sq):.4f}")
print(f"  int|grad psi|^2 = {float(int_grad_psi_sq):.4f}")
print(f"  total flux = {float(total_flux_rect):.4f}")
ratio = float(int_grad_psi_sq / total_flux_rect**2)
print(f"  int|grad psi|^2 / flux^2 = {ratio:.6f}")

# Save
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "step20_global_energy_identity.json")
report = {
    "title": "Step 20 global flux-energy identity",
    "identities": {
        "v_flux_equals_rod_flux": "On each rod, the outward flux of w*grad v equals the rod flux Phi_i",
        "stream_function": "psi defined by d(psi) = *(w dv); psi constant on rods with jumps = Phi_i",
        "energy_of_psi": "int |grad psi|^2 = int w^2 |grad v|^2 = 2 int w^2 + 4 int K_B w^2",
        "K_B_identity": "int K_B w = int w (from the eigenvalue equation)",
    },
    "rectangle_square_check": {
        "int_w2": float(int_w_sq),
        "int_grad_psi2": float(int_grad_psi_sq),
        "total_flux": float(total_flux_rect),
        "energy_to_flux2_ratio": ratio
    },
    "modulus_path": "A conformal modulus lower bound for the alternating-rod polygon "
                    "would give a rigorous BUILD theorem: if the modulus is bounded below "
                    "uniformly in m, then total flux >= c > 0.",
    "open": "The conformal modulus of the m-gon with alternating Dirichlet BCs "
            "as m -> infinity must be computed or estimated."
}
with open(OUT, 'w') as f:
    json.dump(report, f, indent=2)
print(f"\nSaved {OUT}")

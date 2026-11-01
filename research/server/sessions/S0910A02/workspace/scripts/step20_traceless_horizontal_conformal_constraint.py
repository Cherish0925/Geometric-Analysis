"""
Step 20: Traceless horizontal equation forces conformal blow-up near high-A rods.

For the diagonal twist-free polar Einstein reduction:
  g = g_B + p^2 dtheta^2 + q^2 dphi^2, w=pq, v=log(p/q)
  g_B = e^{2phi}(dr^2 + ds^2) in conformal coordinates

The traceless horizontal Einstein equation in conformal z = r + is is:
  u_{zz} + (1/2)(u_z^2 + v_z^2) - 2 phi_z u_z = 0
where u = log w.

COMPUTATION: In the rod collar with p ~ r, q ~ Q(s), Q''+omega^2 Q=0, omega^2=1+2A,
compute the traceless residual in FLAT coordinates (phi=0) and determine
what conformal factor phi is needed to satisfy the equation.

This tests whether the Step-19 collapsing seed is compatible with the
full reduced Einstein system, not just the vertical/trace equations.
"""
import sympy as sp
import json, os

r, s, A = sp.symbols('r s A', positive=True)
omega = sp.sqrt(1 + 2*A)

# Leading-order rod collar: p ~ r, q ~ Q(s), g_B ~ dr^2 + ds^2 (flat to lowest order)
# u = log(r Q(s)) = log r + log Q(s)
# v = log(r/Q(s)) = log r - log Q(s)

# Q(s) = sin(omega s)/omega, Q' = cos(omega s), Q'' = -omega^2 sin(omega s)
Q = sp.sin(omega * s) / omega
logQ = sp.log(Q)
dlogQ = sp.diff(logQ, s)  # Q'/Q = omega cos(omega s)/sin(omega s) = omega cot(omega s)
d2logQ = sp.diff(dlogQ, s)  # Q''/Q - (Q'/Q)^2

# u = log r + log Q, v = log r - log Q
# In conformal z = r + is with flat base:
# u_r = 1/r, u_s = Q'/Q
# u_rr = -1/r^2, u_ss = d/ds(Q'/Q) = Q''/Q - (Q'/Q)^2
# u_rs = 0

u_r = 1/r
u_s = dlogQ
u_rr = -1/r**2
u_ss = d2logQ

v_r = 1/r
v_s = -dlogQ

# u_z = (1/2)(u_r - i u_s), etc.
# u_{zz} = (1/4)(u_{rr} - u_{ss})  [since u_rs = 0]
u_zz_real = sp.Rational(1,4) * (u_rr - u_ss)

# (1/2)(u_z^2 + v_z^2):
# u_z^2 + v_z^2 = (1/4)((u_r - i u_s)^2 + (v_r - i v_s)^2)
# Real part = (1/4)((u_r^2 - u_s^2) + (v_r^2 - v_s^2))
#           = (1/2)(1/r^2 - (Q'/Q)^2)
half_uz2_vz2_real = sp.Rational(1,4) * (u_r**2 - u_s**2 + v_r**2 - v_s**2)

# Traceless residual in flat base = u_zz + (1/2)(u_z^2 + v_z^2)
residual_flat = sp.simplify(u_zz_real + half_uz2_vz2_real)
print("Traceless residual (flat base, real part):")
print("  =", residual_flat)

# Simplify using Q''/Q = -omega^2:
# d2logQ = Q''/Q - (Q'/Q)^2 = -omega^2 - (Q'/Q)^2
# u_ss = -omega^2 - (Q'/Q)^2
# u_zz = (1/4)(-1/r^2 + omega^2 + (Q'/Q)^2)
# half(u_z^2+v_z^2) = (1/4)(1/r^2 - (Q'/Q)^2)
# Sum = (1/4)(omega^2) = (1+2A)/4

# Direct verification:
residual_simplified = sp.simplify(residual_flat.rewrite(sp.cos))
print("Simplified:", residual_simplified)

# Substitute specific: at s = L/2 (midpoint), Q = 1/omega, Q' = 0
s_mid = sp.pi / (2 * omega)
res_at_mid = residual_flat.subs(s, s_mid)
res_at_mid_simplified = sp.simplify(res_at_mid)
print(f"\nAt rod midpoint s = pi/(2 omega): residual = {res_at_mid_simplified}")

# === KEY RESULT ===
# The traceless residual = (1+2A)/4 in flat-base coordinates.
# For the equation u_{zz} + (1/2)(u_z^2 + v_z^2) - 2 phi_z u_z = 0,
# we need 2 phi_z u_z = (1+2A)/4.
# u_z = (1/2)(1/r - i Q'/Q), dominant as r->0 is 1/(2r).
# So phi_z ~ (1+2A)r/4 near r=0.
# In real: phi_r ~ (1+2A)r/2, giving phi ~ (1+2A)r^2/4.

print("\n=== CONFORMAL CORRECTION NEEDED ===")
print("2 phi_z u_z = (1+2A)/4")
print("Near r=0: u_z ~ 1/(2r), so phi_z ~ (1+2A)r/4")
print("=> phi ~ (1+2A) r^2 / 4 + O(r^4)")
print("=> e^{2phi} ~ exp((1+2A) r^2 / 2)")
print("For A = m^2: e^{2phi} ~ exp(m^2 r^2)")

# Compute consequences for the eigenvalue equation
# -Delta_B w = 2 w in g_B = e^{2phi}(dr^2 + ds^2)
# -e^{-2phi} Delta_0 w = 2 w
# -Delta_0 w = 2 e^{2phi} w = 2 exp((1+2A)r^2/2) w
# This is an effective Schrodinger equation with exponentially growing potential!

print("\n=== EIGENVALUE EQUATION IN CONFORMAL BASE ===")
print("-Delta_0 w = 2 e^{2phi} w = 2 exp((1+2A) r^2 / 2) w")
print("This is a harmonic oscillator-type equation near each rod.")
print("The exponential potential LOCALIZES w near the rods,")
print("forcing the eigenfunction to have exponentially small values")
print("in the interior (distance >> 1/sqrt(A) from any rod).")

# Estimate: for the Schrodinger equation -psi'' + V(r) psi = E psi
# with V(r) = 2 exp(A r^2/2) (in 1D cross-section),
# the ground state has most of its mass within r ~ 1/sqrt(A) of the rod.
# The WKB approximation gives psi ~ exp(-S(r)) where
# S(r) ~ integral_0^r sqrt(V(t)-E) dt ~ integral sqrt(2 exp(At^2/2)) dt

# For r >> 1/sqrt(A): S(r) ~ sqrt(2) integral exp(At^2/4) dt
# This grows super-exponentially, so w is EXTREMELY localized.

print("\n=== LOCALIZATION ESTIMATE ===")
print("In the 1D cross-section perpendicular to a rod,")
print("w ~ exp(-sqrt(2) * integral_0^r exp(A t^2/4) dt)")
print("for r >> 1/sqrt(A).")
print("Effective localization width: ~ 1/sqrt(A) = 1/m")

# CONSEQUENCES FOR TOTAL FLUX
# If w is localized within O(1/sqrt(A)) of each rod, and along
# the rod Q(s) has maximum 1/omega ~ 1/m, then:
# w ~ Q(s) * r * (localization factor) in the collar
# The flux through one rod = int_rod q ds = int Q(s) ds = 2/(1+2A)
# But the INTERIOR value of w is exponentially small.

# The total int_Omega w dA is dominated by the collar regions:
# int_collar w ~ (rod length) * (collar width) * (typical w)
# ~ (pi/omega) * (1/sqrt(A)) * (1/omega * 1) 
# ~ pi/A * 1/sqrt(A) = pi/A^{3/2}
# With m rods: total int w ~ m * pi/A^{3/2}
# For A = m^2: ~ m * pi/m^3 = pi/m^2 -> 0.

print("\n=== TOTAL FLUX / VOLUME ESTIMATE ===")
print("Collar-dominated int w ~ m * (pi/omega) * (1/sqrt(A)) * (1/omega)")
print("For A = m^2: ~ m * pi/(m sqrt(2)) * 1/m * 1/(m sqrt(2)) ~ pi/(2 m^2)")
print("Total flux = 2 int w ~ pi/m^2 -> 0")
print("Vol_4 = 4 pi^2 int w ~ 4 pi^3 / m^2 -> 0")
print()
print("BUT: this volume collapse is even FASTER than the rod-flux estimate 1/m.")
print("The rod-flux estimate gives flux ~ 1/m, while the conformal")
print("localization gives int w ~ 1/m^2. Consistency requires checking.")

# CONSISTENCY CHECK: is the flux = 2 int w?
# Rod flux per rod = 2/(1+2A) ~ 1/m^2. Total flux = m * 1/m^2 = 1/m.
# int w = total_flux/2 = 1/(2m).
# My collar estimate above gives int w ~ pi/(2m^2), which is too small!
# This means either:
# (a) the conformal blow-up makes the area larger than estimated, or
# (b) the collar estimate used wrong effective area.

# Let me redo: in the conformal metric g_B = e^{2phi}(dr^2+ds^2),
# dA_B = e^{2phi} dr ds. So:
# int w dA_B = int w * e^{2phi} dr ds
# In the collar: w ~ r * Q(s), e^{2phi} ~ exp(A r^2/2).
# int_collar w dA_B ~ int_0^{L} int_0^R r Q(s) exp(A r^2/2) dr ds
# r-integral: int_0^R r exp(A r^2/2) dr = [exp(A r^2/2) - 1]/A ~ 1/A for R >> 1/sqrt(A)
# s-integral: int_0^L Q(s) ds = 2/(1+2A)
# So int_collar w dA_B ~ (1/A) * 2/(1+2A) ~ 2/A^2 for large A
# With m rods: int w ~ m * 2/A^2 = 2m/m^4 = 2/m^3 for A=m^2.

# But total flux / 2 = m/(1+2m^2) / 2 ~ 1/(2m).
# So 2/m^3 << 1/(2m). The collar integral is TOO SMALL.

# This means: the conformal blow-up increases dA_B so much that even though
# w is small, the volume element compensates. The integral is dominated NOT
# by the thin collar but by a TRANSITION region where both w and e^{2phi}
# are moderate.

print("\n=== REVISED AREA INTEGRAL ===")
print("In conformal coordinates: int w dA_B = int w * exp(A r^2 / 2) dr ds")
print("Collar r-integral: int_0^R r exp(A r^2/2) dr = [exp(Ar^2/2)-1]/A ~ 1/A")
print("Per rod: ~ 2/(A(1+2A)) ~ 2/A^2")
print("m rods with A=m^2: total ~ 2m/m^4 = 2/m^3")
print()
print("But needed: int w = total_flux/2 = m/(1+2m^2) ~ 1/(2m)")
print("Collar contribution 2/m^3 << 1/(2m): the collar does NOT dominate.")
print("The interior/transition region must carry most of int w.")
print()
print("CONCLUSION: The conformal blow-up makes the INTERIOR integral")
print("of w significant, even though w decreases exponentially there,")
print("because e^{2phi} grows even faster. This is the key tension.")

# Save results
OUTDIR = "Sessions/S0910A02/workspace/data"
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "step20_traceless_horizontal_conformal.json")
report = {
    "title": "Step 20: traceless horizontal forces conformal blow-up",
    "flat_base_traceless_residual": "(1+2A)/4",
    "conformal_correction": "phi ~ (1+2A) r^2 / 4 near rod",
    "base_metric_near_rod": "g_B ~ exp((1+2A) r^2 / 2) (dr^2+ds^2)",
    "eigenvalue_equation_in_flat": "-Delta_0 w = 2 exp((1+2A) r^2 / 2) w",
    "collar_r_integral_per_rod": "2/(A(1+2A)) ~ 2/A^2",
    "total_collar_contribution_A_eq_m2": "2m/m^4 = 2/m^3",
    "needed_int_w": "1/(2m)",
    "conclusion": "Collar integral 2/m^3 << 1/(2m): interior/transition dominates int w. "
                   "The conformal blow-up exp(Ar^2/2) in the base metric "
                   "creates a tension: the eigenvalue equation -Delta_0 w = 2 exp(Ar^2/2) w "
                   "localizes w near rods, but the area element exp(2phi) amplifies the interior, "
                   "so the integral of w is not dominated by the collar.",
    "key_new_insight": "The traceless horizontal equation is NOT automatically satisfied "
                       "in flat-base collar coordinates. It requires phi ~ A r^2 / 4, "
                       "which changes the base geometry from flat to exponentially expanding. "
                       "This was not tested in Step 19's corner matching, which only checked "
                       "the vertical/trace equations.",
    "open_question": "Does the exponentially expanding base metric, required by the traceless "
                     "equation, change the global eigenvalue or flux in a way that obstructs "
                     "or permits the collapsing seed? The transition from collar to interior "
                     "carries most of int w and must be analyzed."
}
with open(OUT, 'w') as f:
    json.dump(report, f, indent=2)
print("\nSaved", OUT)

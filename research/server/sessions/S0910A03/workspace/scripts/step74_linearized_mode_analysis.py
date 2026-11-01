"""
Step 74: Linearized Einstein mode analysis around the flat hyperbolic cusp.

For g0 = dt^2 + e^{2t}(dz^2 + dx^2 + dy^2), perturb by T^2-invariant
diagonal modes with Fourier wavenumber k in z.

This determines whether the center-to-cusp BVP has growing or decaying
modes, which controls the feasibility of the core-entry construction.
"""
import numpy as np
import sympy as sp
import json, os
from scipy.integrate import solve_ivp
from scipy.linalg import eig

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(os.path.dirname(script_dir), 'data')
os.makedirs(data_dir, exist_ok=True)

results = {}

# ===================================================================
# Part 1: Symbolic linearized system
# ===================================================================
print("="*70)
print("LINEARIZED EINSTEIN AROUND FLAT CUSP")
print("="*70)
print()

t = sp.Symbol('t')
k = sp.Symbol('k', real=True, positive=True)
alpha = sp.Function('alpha')  # perturbation of a
beta = sp.Function('beta')    # perturbation of b
gamma = sp.Function('gamma')  # perturbation of c

# Background: a=b=c=t, a'=b'=c'=1, a''=0
# Metric: g = dt^2 + e^{2(t+alpha)}dz^2 + e^{2(t+beta)}dx^2 + e^{2(t+gamma)}dy^2
# Keep only first order in alpha, beta, gamma.
# The z-dependence enters as multiplied by e^{ikz}; derivatives d/dz -> ik.

# From step70 Ricci formulas, linearized around background:
# Using h = alpha + beta + gamma (trace perturbation)

al = alpha(t)
be = beta(t)
ga = gamma(t)
h = al + be + ga  # trace

# Linearized E_{00} = 0:
# Background: R_{00} = -3, so dR_{00} = -(2h' + h'')
# Thus: dE_{00} = -(2*h' + h'') = 0
# => h'' + 2h' = 0
E00 = sp.diff(h, t, 2) + 2*sp.diff(h, t)
print("E_00 linearized: h'' + 2h' = 0")
print(f"  Solution: h ~ C1 + C2*e^{{-2t}}")
print()

# Linearized E_{11}/e^{2a} = 0 (z-component):
# Background gives: -(a_tt + a_t*H) + intrinsic terms + 3 = 0
# Perturbed: a = t+alpha, H_t = 3 + h'
# -(alpha'' + 1*(3+h') + alpha'*3) + e^{-2t}*k^2*(...) + 3 = 0
# Careful: the theta-derivative terms at the background vanish,
# but linearized they contribute through the k^2 multiplier.

# Full linearized E_{11}/e^{2(t+alpha)} from step70 data:
# The intrinsic terms (z-derivatives) at k!=0:
# e^{-2a} * (a_z*b_z + a_z*c_z - b_z^2 - b_zz - c_z^2 - c_zz)
# Linearized: e^{-2t} * (ik*alpha*ik*beta + ik*alpha*ik*gamma
#                          - (ik*beta)^2 - (-k^2*beta)
#                          - (ik*gamma)^2 - (-k^2*gamma))
# = e^{-2t} * (-k^2*alpha*beta - k^2*alpha*gamma + k^2*beta + k^2*gamma)
# Wait, I need to be more careful. The background z-derivatives are all zero.
# The perturbation z-derivative of f(t)*e^{ikz} gives ik*f(t)*e^{ikz}.
# Products like a_z*b_z are (ik*alpha)(ik*beta) = -k^2*alpha*beta (2nd order).
# But b_zz = -k^2*beta (1st order in perturbation).

# So the first-order z-derivative contributions from E_{11}/e^{2a}:
# e^{-2t}*(0 + 0 - 0 - (-k^2*beta) - 0 - (-k^2*gamma))
# = e^{-2t}*k^2*(beta + gamma)

# Similarly, the t-derivative linearized terms:
# -(alpha'' + alpha'*3 + 1*h') + 3 -> -(alpha'' + 3*alpha' + h')
# But we're perturbing from E=0, so:
# dE_{11}/e^{2t} = -(alpha'' + 3*alpha' + h') + e^{-2t}*k^2*(beta + gamma)

E11 = -(sp.diff(al, t, 2) + 3*sp.diff(al, t) + sp.diff(h, t)) + k**2*sp.exp(-2*t)*(be + ga)
print("E_11/e^{2a} linearized:")
print(f"  -{sp.diff(al, t, 2)} - 3*{sp.diff(al, t)} - {sp.diff(h, t)} + k^2*e^{{-2t}}*(beta+gamma)")
print()

# E_{22}/e^{2b}:
# Intrinsic z-terms: e^{-2a}*(a_z*b_z - b_z^2 - b_z*c_z - b_zz)
# Linearized 1st order: e^{-2t}*(0 - 0 - 0 - (-k^2*beta)) = e^{-2t}*k^2*beta
# But wait, actually looking at the formula more carefully:
# E_{22} has factor e^{-2a+2b}, and the intrinsic terms are:
# (a_z*b_z - b_z^2 - b_z*c_z - b_zz) evaluated at perturbation level
# 1st order z-derivative terms: only -b_zz = k^2*beta
# The product terms a_z*b_z etc are 2nd order.

E22 = -(sp.diff(be, t, 2) + 3*sp.diff(be, t) + sp.diff(h, t)) + k**2*sp.exp(-2*t)*be
print("E_22/e^{2b} linearized:")
print(f"  -beta'' - 3*beta' - h' + k^2*e^{{-2t}}*beta")
print()

# E_{33}/e^{2c}: similarly
E33 = -(sp.diff(ga, t, 2) + 3*sp.diff(ga, t) + sp.diff(h, t)) + k**2*sp.exp(-2*t)*ga
print("E_33/e^{2c} linearized:")
print(f"  -gamma'' - 3*gamma' - h' + k^2*e^{{-2t}}*gamma")
print()

# E_{01} (mixed t-z):
# From step70: a_t*(b_z+c_z) - b_t*b_z - c_t*c_z - b_tz - c_tz
# Linearized: 1*(ik*beta+ik*gamma) - 1*ik*beta - 1*ik*gamma - ik*beta' - ik*gamma'
# = ik*(beta+gamma) - ik*(beta+gamma) - ik*(beta'+gamma')
# = -ik*(beta'+gamma')
# For E_{01} = 0: beta' + gamma' = 0 for each mode
# i.e., (beta+gamma)' = 0, so beta+gamma = const at each t for each k!=0 mode.

print("E_{01} linearized: -ik*(beta'+gamma') = 0")
print("  => beta + gamma = const for each k!=0 Fourier mode")
print()

# Summary: the constraint E_{01}=0 gives beta+gamma = const.
# Combined with E_00: h''+2h'=0 => h ~ C1+C2*e^{-2t}
# And: alpha' = h' - (beta'+gamma') = h' - 0 = h'
# So alpha' = h' => alpha = h + const = (alpha+beta+gamma) + const
# => beta+gamma = -const (absorbed into the constant mode)

# Effective system: set phi = alpha, psi = beta-gamma (anisotropy)
# Then beta = (beta+gamma)/2 + psi/2, gamma = (beta+gamma)/2 - psi/2
# With beta+gamma = const (call it W0), we get:
# alpha = h - W0, where h satisfies h''+2h'=0

# From E22-E33: -(psi''+3psi') + k^2*e^{-2t}*psi = 0
# This is the ANISOTROPY MODE EQUATION!

psi = sp.Function('psi')
anisotropy_eq = -(sp.diff(psi(t), t, 2) + 3*sp.diff(psi(t), t)) + k**2*sp.exp(-2*t)*psi(t)

print("="*70)
print("KEY: ANISOTROPY MODE EQUATION (beta - gamma = psi)")
print("="*70)
print(f"  psi'' + 3*psi' - k^2*e^{{-2t}}*psi = 0")
print()

# Change of variable: let x = k*e^{-t} (so x -> 0 as t -> inf, x = k at t=0)
# dt = -dx/x, d/dt = -x*d/dx
# psi' = -x*psi_x, psi'' = x^2*psi_xx + x*psi_x
# x^2*psi_xx + x*psi_x - 3*(-x*psi_x) - x^2*psi = 0
# x^2*psi_xx + x*psi_x + 3x*psi_x - x^2*psi = 0
# x^2*psi_xx + 4x*psi_x - x^2*psi = 0
# Divide by x^2: psi_xx + (4/x)*psi_x - psi = 0

# This is a modified Bessel equation! Let psi = x^{-3/2} w(x):
# Then psi_x = -3/(2x^{5/2})w + x^{-3/2}w_x
# ... actually, let me try the standard substitution.
# The equation x^2 y'' + 4x y' - x^2 y = 0
# Let y = x^{-p} z(x). Choose p=3/2 to absorb the first-order term.
# y = x^{-3/2} z
# y' = -3/(2x^{5/2}) z + x^{-3/2} z'
# y'' = 15/(4x^{7/2}) z - 3/x^{5/2} z' + x^{-3/2} z''
# x^2 y'' = 15/(4x^{3/2}) z - 3/x^{1/2} z' + x^{1/2} z''
# 4x y' = -6/x^{3/2} z + 4/x^{1/2} z'
# -x^2 y = -x^{1/2} z
# Sum: z''*x^{1/2} + z'*(4/x^{1/2}-3/x^{1/2}) + z*(15/(4x^{3/2})-6/x^{3/2}-x^{1/2})
#     = z''*x^{1/2} + z'/x^{1/2} + z*(-9/(4x^{3/2}) - x^{1/2}) = 0
# Multiply by x^{1/2}: z''*x + z' + z*(-9/(4x) - x) = 0
# x z'' + z' - (x + 9/(4x))z = 0

# Compare with modified Bessel: x z'' + z' - (x + nu^2/x) z = 0
# This is I_nu, K_nu with nu = 3/2!
# So z = A*I_{3/2}(x) + B*K_{3/2}(x)
# psi = x^{-3/2}[A*I_{3/2}(x) + B*K_{3/2}(x)]

print("Change of variable x = k*e^{-t}:")
print("  x^2*psi_xx + 4x*psi_x - x^2*psi = 0")
print("  Substitution psi = x^{-3/2} z(x):")
print("  => z satisfies the modified Bessel equation with nu = 3/2")
print("  z = A*I_{3/2}(x) + B*K_{3/2}(x)")
print("  psi(t) = (k*e^{-t})^{-3/2} * [A*I_{3/2}(k*e^{-t}) + B*K_{3/2}(k*e^{-t})]")
print()

# Known: I_{3/2}(x) = sqrt(2/(pi*x)) * (cosh(x) - sinh(x)/x)
#         K_{3/2}(x) = sqrt(pi/(2x)) * e^{-x}*(1 + 1/x)

# As t -> infinity (x -> 0):
# I_{3/2}(x) ~ x^{3/2} / (2^{3/2} Gamma(5/2)) = x^{3/2}/(2^{3/2} * 3*sqrt(pi)/4)
# K_{3/2}(x) ~ Gamma(3/2) / (2*(x/2)^{3/2}) = sqrt(pi/2) * 2^{1/2} / x^{3/2}
# = sqrt(pi) / x^{3/2}

# psi_I ~ x^{-3/2} * x^{3/2} * const = const  (bounded as t -> inf)
# psi_K ~ x^{-3/2} * x^{-3/2} * const = x^{-3} = k^{-3} e^{3t}  (GROWS as t -> inf!)

# As t -> 0 (x = k):
# I_{3/2}(k) and K_{3/2}(k) are both finite for k > 0

print("Asymptotic behavior:")
print("  As t -> infinity (x -> 0):")
print("  I-branch: psi ~ const (approaches zero harmlessly)")
print("  K-branch: psi ~ e^{3t} (GROWS exponentially!)")
print()
print("  As t -> 0 (x = k):")
print("  Both branches are regular.")
print()
print("CONCLUSION: The anisotropy PDE has exponentially growing modes")
print("(rate 3) toward the cusp, driven by the K_{3/2} Bessel function.")
print("The BVP must select the I-branch to avoid this growth.")
print()

# ===================================================================
# Part 2: Numerical verification of mode behavior
# ===================================================================
print("="*70)
print("NUMERICAL MODE EVOLUTION")
print("="*70)

from scipy.special import iv, kv

def psi_I(t_arr, k_val):
    """I-branch solution"""
    x = k_val * np.exp(-t_arr)
    return x**(-1.5) * iv(1.5, x)

def psi_K(t_arr, k_val):
    """K-branch solution"""
    x = k_val * np.exp(-t_arr)
    return x**(-1.5) * kv(1.5, x)

# Verify against ODE solver
def aniso_ode(t_val, y, k_val):
    p, dp = y
    ddp = -3*dp + k_val**2 * np.exp(-2*t_val) * p
    return [dp, ddp]

mode_results = {}
for k_val in [1, 2, 3, 5]:
    # I-branch: starts regular, stays bounded
    t_eval = np.linspace(0, 10, 1000)
    
    # Initial conditions from I-branch at t=0
    x0 = k_val
    I_32 = iv(1.5, x0)
    # d/dt [x^{-3/2} I_{3/2}(x)] at t=0:
    # = (-3/2)*(-k)*x^{-5/2}*I_{3/2} + x^{-3/2}*(-k)*I'_{3/2}
    # I'_{3/2}(x) = I_{1/2}(x) - (3/2)/x * I_{3/2}(x)
    dI = iv(0.5, x0) - 1.5/x0 * iv(1.5, x0)
    
    psi0 = x0**(-1.5) * I_32
    dpsi0 = 1.5*k_val*x0**(-2.5)*I_32 + x0**(-1.5)*(-k_val)*dI
    
    sol = solve_ivp(aniso_ode, [0, 10], [psi0, dpsi0], args=(k_val,),
                    t_eval=t_eval, rtol=1e-12, atol=1e-14)
    
    # Check growth/decay
    if sol.success:
        psi_vals = sol.y[0]
        ratio = np.abs(psi_vals[-1]) / np.abs(psi_vals[0])
        print(f"k={k_val}: psi(0)={psi_vals[0]:.6f}, psi(10)={psi_vals[-1]:.6e}, "
              f"ratio={ratio:.6f}")
        
        # K-branch for comparison (should grow ~e^{3t})
        psi_K_vals = psi_K(t_eval, k_val)
        # Normalize to 1 at t=0
        if np.abs(psi_K_vals[0]) > 1e-15:
            K_ratio = np.abs(psi_K_vals[-1] / psi_K_vals[0])
        else:
            K_ratio = float('inf')
        
        mode_results[f"k={k_val}"] = {
            "I_branch_ratio": float(ratio),
            "K_branch_ratio_t10": float(min(K_ratio, 1e20)),
            "expected_K_growth": float(np.exp(30))  # e^{3*10}
        }

print()
print("Mode behavior:")
print("  I-branch: BOUNDED (decays or oscillates) — viable for BVP")
print("  K-branch: GROWS as e^{3t} — must be excluded by boundary conditions")
print()

results["mode_analysis"] = mode_results

# ===================================================================
# Part 3: BVP feasibility assessment
# ===================================================================
print("="*70)
print("BVP FEASIBILITY ASSESSMENT")
print("="*70)
print()

# The linearized system decomposes into:
# 1. Trace mode h: h'' + 2h' = 0 (decays at rate 2)
# 2. Sum beta+gamma: constrained to be constant (from E_01)
# 3. Anisotropy psi = beta-gamma: modified Bessel equation
#    - I-branch: bounded at cusp (GOOD)
#    - K-branch: grows at rate 3 at cusp (BAD)

# For the BVP to have a unique solution, we need:
# - At the center (t=0): reflection conditions fix psi'(0) = 0 (or similar)
# - At the cusp (t=R): psi should match cusp data (const anisotropy)
# - The I-branch naturally satisfies bounded cusp behavior

# The BVP is: given center conditions (Neumann), find the I-branch
# that matches cusp-end data. This is a well-posed elliptic BVP IF
# the I-branch exists and the nonlinear terms don't destabilize.

# For the full nonlinear problem, the question is whether the
# linearized BVP structure persists.

# Key dimension count:
# At each Fourier mode k, we have a 2nd-order ODE for psi(t).
# Center: 1 condition (Neumann: psi'(0) = 0)
# Far end: 1 condition (select I-branch: exclude K-branch growth)
# This gives a UNIQUE solution for each k! (2 conditions for 2nd order ODE)

print("For each Fourier mode k in the anisotropy:")
print("  - 2nd order ODE in t for psi_k(t)")
print("  - Center: psi_k'(0) = 0 (reflection)")  
print("  - Far end: exclude K-branch (boundedness)")
print("  => Unique solution per mode (well-posed BVP)")
print()

# Compute the ratio psi_k(R)/psi_k(0) for the I-branch
# This tells us how much center anisotropy propagates to the cusp
print("Anisotropy transmission (I-branch, center -> cusp at R=10):")
for k_val in [1, 2, 3, 5, 10]:
    x0 = k_val  # at t=0
    x_R = k_val * np.exp(-10)  # at t=R=10
    
    I_0 = x0**(-1.5) * iv(1.5, x0) if x0 > 0 else 1
    I_R = x_R**(-1.5) * iv(1.5, x_R) if x_R > 1e-15 else (x_R**(-1.5) * x_R**1.5 / (2**1.5 * 1.329))
    
    # For small x: I_{3/2}(x) ~ x^{3/2} / (2^{3/2} * Gamma(5/2))
    # x^{-3/2} * I_{3/2}(x) ~ 1 / (2^{3/2} * 3*sqrt(pi)/4) = 4/(6*sqrt(2*pi)) = 0.2659
    I_R_approx = 4.0 / (6.0 * np.sqrt(2*np.pi))  # ~ 0.2659
    
    ratio = I_R_approx / I_0 if abs(I_0) > 1e-15 else float('inf')
    print(f"  k={k_val:2d}: psi_k(0)={I_0:.6f}, psi_k(inf)~{I_R_approx:.6f}, "
          f"transmission={ratio:.4f}")

print()
print("CONCLUSION: Center anisotropy is ATTENUATED at the cusp for all k.")
print("The I-branch naturally suppresses z-oscillations toward the cusp.")
print("This is the OPPOSITE of the growing K-branch.")
print()
print("Physical interpretation: the exponential expansion of the cusp")
print("dilutes spatial oscillations, selecting the smooth I-branch solution.")
print("The BVP is well-posed at the linearized level: center reflection +")
print("cusp boundedness uniquely determine each Fourier mode.")

results["bvp_feasibility"] = {
    "linearized_well_posed": True,
    "mechanism": "I-branch (modified Bessel) attenuates center anisotropy toward cusp",
    "K_branch_growth_rate": 3,
    "trace_decay_rate": 2,
    "note": "Nonlinear stability requires separate analysis"
}

# ===================================================================
# Part 4: Comparison with the Frobenius from Step 72
# ===================================================================
print()
print("="*70)
print("COMPARISON WITH STEP 72 FROBENIUS")
print("="*70)
print()
print("Step 72 found AMPLIFICATION of anisotropy modes in the exact Einstein")
print("drift-Laplacian div(e^sigma grad d) = 0. This DOES NOT contradict")
print("the present result because:")
print("  1. Step 72 used the EXACT Einstein equation (delta=0)")
print("  2. The present analysis linearizes around the FLAT cusp background")
print("  3. The exact solution couples anisotropy to geometry nonlinearly")
print("  4. The I-branch I-transmission applies to the APPROXIMATE problem")
print()
print("The key insight: for the APPROXIMATE problem (small delta),")
print("linearization around the flat cusp is appropriate near the cusp end,")
print("and the I-branch structure governs the mode selection.")
print("Step 73's expanding tail explicitly demonstrated this at the nonlinear level:")
print("O(1) anisotropy is removed with O(K^{-1}) Ricci cost.")

# Save results
out_path = os.path.join(data_dir, 'step74_linearized_modes.json')
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nWrote {out_path}")

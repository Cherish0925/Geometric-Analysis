# STEP 75 SCOPE CORRECTION: although both displayed basis solutions are bounded as t->infinity for each fixed k, the reflection-normalized solution psi(0)=1, psi'(0)=0 has limit sinh(k)/k.  Thus there is exponential amplification in frequency.  Fixed-mode Neumann--Dirichlet uniqueness is not frequency-uniform stability and does not establish the nonlinear Einstein boundary map.
"""
Step 74 CORRECTED: Linearized anisotropy mode analysis.

TTCS verification found a chain-rule sign error in the Bessel reduction.
The correct equation in x = k*e^{-t} is:
  x^2 psi_xx - 2x psi_x - x^2 psi = 0
NOT x^2 psi_xx + 4x psi_x - x^2 psi = 0.

Correct solution: psi = x^{3/2}[A*I_{3/2}(x) + B*K_{3/2}(x)]
NOT psi = x^{-3/2}[...].

BOTH branches are bounded as t -> infinity:
  I-branch: psi ~ x^3 ~ e^{-3t} (decays to zero)
  K-branch: psi ~ const (approaches nonzero constant)
NO exponentially growing modes exist.
"""
import numpy as np
import json, os
from scipy.integrate import solve_ivp
from scipy.special import iv, kv

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(os.path.dirname(script_dir), 'data')
os.makedirs(data_dir, exist_ok=True)

results = {"correction": "Step74 Bessel prefactor x^{3/2} not x^{-3/2}"}

# ===================================================================
# Verify the corrected Bessel solutions against the ODE
# ===================================================================
print("="*70)
print("CORRECTED ANISOTROPY MODE ANALYSIS")
print("="*70)
print()
print("Anisotropy ODE: psi'' + 3*psi' - k^2*e^{-2t}*psi = 0")
print("Variable change x = k*e^{-t}:")
print("  psi_t = -x*psi_x,  psi_tt = x^2*psi_xx + x*psi_x")
print("  => x^2*psi_xx - 2x*psi_x - x^2*psi = 0  (CORRECTED)")
print()
print("Substitution psi = x^{3/2}*z:")
print("  => x^2*z'' + x*z' - (x^2 + 9/4)*z = 0")
print("  Modified Bessel equation with nu = 3/2")
print()
print("Solution: psi = x^{3/2}*[A*I_{3/2}(x) + B*K_{3/2}(x)]")
print()

# Verify: direct ODE integration vs Bessel formula
def aniso_ode(t_val, y, k_val):
    p, dp = y
    ddp = -3*dp + k_val**2 * np.exp(-2*t_val) * p
    return [dp, ddp]

def psi_I_correct(t_arr, k_val):
    """I-branch: x^{3/2} * I_{3/2}(x) where x = k*e^{-t}"""
    x = k_val * np.exp(-t_arr)
    return x**1.5 * iv(1.5, x)

def psi_K_correct(t_arr, k_val):
    """K-branch: x^{3/2} * K_{3/2}(x) where x = k*e^{-t}"""
    x = k_val * np.exp(-t_arr)
    return x**1.5 * kv(1.5, x)

print("Verification: Bessel solutions vs ODE integration")
print("-"*60)

mode_data = {}
for k_val in [1, 2, 3, 5]:
    # I-branch initial data at t=0
    x0 = float(k_val)
    psi0_I = x0**1.5 * iv(1.5, x0)
    
    # Derivative: d/dt[x^{3/2} I_{3/2}(x)] = (-x)[3/2 x^{1/2} I_{3/2} + x^{3/2} I'_{3/2}]
    # I'_{3/2}(x) = I_{1/2}(x) - (3/2)/x * I_{3/2}(x)
    dI = iv(0.5, x0) - 1.5/x0 * iv(1.5, x0)
    dpsi0_I = (-x0) * (1.5 * x0**0.5 * iv(1.5, x0) + x0**1.5 * dI)
    
    # K-branch initial data at t=0
    psi0_K = x0**1.5 * kv(1.5, x0)
    dK = -kv(0.5, x0) - 1.5/x0 * kv(1.5, x0)  # K'_{3/2}
    dpsi0_K = (-x0) * (1.5 * x0**0.5 * kv(1.5, x0) + x0**1.5 * dK)
    
    # Integrate ODE from t=0 to t=15 for each branch
    t_eval = np.linspace(0, 15, 3000)
    
    sol_I = solve_ivp(aniso_ode, [0, 15], [psi0_I, dpsi0_I], args=(k_val,),
                      t_eval=t_eval, rtol=1e-13, atol=1e-15)
    sol_K = solve_ivp(aniso_ode, [0, 15], [psi0_K, dpsi0_K], args=(k_val,),
                      t_eval=t_eval, rtol=1e-13, atol=1e-15)
    
    # Compare with analytic formula
    psi_I_analytic = psi_I_correct(t_eval, k_val)
    psi_K_analytic = psi_K_correct(t_eval, k_val)
    
    if sol_I.success and sol_K.success:
        err_I = np.max(np.abs(sol_I.y[0] - psi_I_analytic))
        err_K = np.max(np.abs(sol_K.y[0] - psi_K_analytic))
        
        # Asymptotic values
        psi_I_far = sol_I.y[0][-1]
        psi_K_far = sol_K.y[0][-1]
        
        # Expected: I-branch -> 0, K-branch -> sqrt(pi/2)
        K_asymp = np.sqrt(np.pi/2)  # K_{3/2}(x) -> sqrt(pi/(2x)) * e^{-x}(1+1/x) -> sqrt(pi/2)/x^{3/2} * ...
        # Actually: x^{3/2}*K_{3/2}(x) -> Gamma(3/2)/(2*(1/2)^{3/2}) = sqrt(pi)/2 * 2^{3/2} = sqrt(2*pi)
        # More precisely: K_{3/2}(x) ~ Gamma(3/2)/(2*(x/2)^{3/2}) = sqrt(pi)/(2*(x/2)^{3/2})
        # = sqrt(pi)*2^{1/2}/x^{3/2}
        # x^{3/2}*K_{3/2}(x) -> sqrt(pi)*2^{1/2} = sqrt(2*pi) ~ 2.5066
        K_limit = np.sqrt(2*np.pi)
        
        print(f"k={k_val}: I-branch: psi(0)={psi0_I:.6f}, psi(15)={psi_I_far:.4e} "
              f"(analytic match err={err_I:.2e})")
        print(f"       K-branch: psi(0)={psi0_K:.6f}, psi(15)={psi_K_far:.6f} "
              f"(analytic match err={err_K:.2e})")
        print(f"       K-branch asymptotic: {psi_K_far:.4f} vs sqrt(2pi)={K_limit:.4f}")
        
        mode_data[f"k={k_val}"] = {
            "I_psi0": float(psi0_I), "I_psi15": float(psi_I_far),
            "K_psi0": float(psi0_K), "K_psi15": float(psi_K_far),
            "I_err": float(err_I), "K_err": float(err_K)
        }

print()
print("="*70)
print("ASYMPTOTICS (CORRECTED)")
print("="*70)
print()
print("As t -> infinity (x = k*e^{-t} -> 0):")
print("  I-branch: psi = x^{3/2}*I_{3/2}(x) ~ C*x^3 = C*k^3*e^{-3t} -> 0")
print("  K-branch: psi = x^{3/2}*K_{3/2}(x) -> sqrt(2*pi) ~ 2.507  (CONSTANT)")
print()
print("BOTH branches are bounded. No exponentially growing modes exist.")
print("This is consistent with the large-t limit psi''+3psi'=0,")
print("whose solutions are const and e^{-3t}.")

# ===================================================================
# BVP structure (corrected)
# ===================================================================
print()
print("="*70)
print("BVP STRUCTURE (CORRECTED)")
print("="*70)
print()
print("Since both solutions are bounded, 'Neumann + boundedness' gives")
print("only ONE effective condition for a 2nd-order ODE => NOT unique.")
print()
print("Correct BVP conditions:")
print("  Option A: Neumann at center + Dirichlet at far end => UNIQUE")
print("  Option B: Neumann at center + decay (psi -> 0) => B=0, then")
print("            psi'(0)=0 forces A=0 for homogeneous; non-homogeneous")
print("            problem has unique solution.")
print()
print("Energy argument for uniqueness on [0,R]:")
print("  Write (e^{3t}*psi')' - k^2*e^t*psi = 0")
print("  Multiply by psi and integrate: e^{3t}*psi*psi'|_0^R")
print("    - integral(e^{3t}*(psi')^2 + k^2*e^t*psi^2) = 0")
print("  With Neumann at 0 and Dirichlet at R: boundary term = 0")
print("  => psi' = 0 and psi = 0 everywhere. QED.")
print()

# Verify the energy form
t_sym = np.linspace(0, 10, 1000)
for k_val in [1, 3]:
    # Verify (e^{3t}psi')' - k^2 e^t psi = 0 for I-branch
    dt = t_sym[1] - t_sym[0]
    psi_vals = psi_I_correct(t_sym, k_val)
    psi_prime = np.gradient(psi_vals, dt)
    e3t_psi_prime = np.exp(3*t_sym) * psi_prime
    lhs = np.gradient(e3t_psi_prime, dt) - k_val**2 * np.exp(t_sym) * psi_vals
    print(f"  Energy form residual (k={k_val}): max|res| = {np.max(np.abs(lhs)):.2e}")

# ===================================================================
# k=0 mode structure
# ===================================================================
print()
print("="*70)
print("k=0 MODE STRUCTURE")
print("="*70)
print()
print("At k=0, the anisotropy ODE is psi'' + 3*psi' = 0")
print("  => psi = C + D*e^{-3t}")
print("  Neumann: D = 0, constant C survives (cusp cross-section modulus)")
print("  This reflects the T^3 shape parameter, not an obstruction.")

# ===================================================================
# Coupling relation from E_{zz}
# ===================================================================
print()
print("="*70)
print("COUPLING RELATION (from TTCS)")
print("="*70)
print()
print("E_{zz} = 0 gives an additional relation:")
print("  4D + k^2*W = 0,  where D = decaying trace coefficient,")
print("  W = constant sum (beta+gamma)")
print("  Equivalently: h' = (k^2/2)*W*e^{-2t}")
print("This couples the trace and sum modes.")

results["mode_analysis_corrected"] = mode_data
results["bessel_correct"] = {
    "equation_x": "x^2*psi_xx - 2x*psi_x - x^2*psi = 0",
    "substitution": "psi = x^{3/2} * z",
    "bessel_nu": 1.5,
    "I_asymptotic": "e^{-3t} (decays)",
    "K_asymptotic": "sqrt(2*pi) ~ 2.507 (constant)"
}
results["bvp_corrected"] = {
    "uniqueness": "Neumann at center + Dirichlet at far end gives unique solution",
    "energy_form": "(e^{3t}*psi')' - k^2*e^t*psi = 0",
    "k0_mode": "constant anisotropy survives (cusp shape modulus)"
}

print()
print("="*70)
print("CONCLUSIONS (CORRECTED)")
print("="*70)
print()
print("1. Both Bessel branches bounded: NO growing modes (correcting Step 72)")
print("2. I-branch decays at rate 3, K-branch -> constant")
print("3. BVP is well-posed (Neumann + Dirichlet), unique by energy")
print("4. k=0 mode: constant cusp shape parameter (not an obstruction)")
print("5. Trace/sum coupling 4D + k^2*W = 0 must be maintained")
print("6. Full constraint propagation requires all 5 Einstein equations")
print()
print("The absence of growing modes is FAVORABLE for the core construction:")
print("center anisotropy does not amplify toward the cusp.")

out_path = os.path.join(data_dir, 'step74_corrected_modes.json')
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nWrote {out_path}")

#!/usr/bin/env python3
"""Step 65: Derive the coupled linearized-Ricci ODEs on EH SYMBOLICALLY.

The failure of the numerical extraction was due to finite-difference noise.
Here we compute the linearized Ricci operator on the diagonal ansatz
    h = diag(f1*g00, f2*g11, f2*g11, f3*g33)   (coordinate basis, theta=pi/2)
directly from the closed-form Christoffels and curvature, with NO finite differences.

Approach:
  The linearized Ricci for a metric perturbation h on a background g (Ricci-flat):
    (dRic)_ij[h] = (1/2)*g^{kl}( -nabla_k nabla_l h_ij - nabla_i nabla_j h_kl
                                 + nabla_k nabla_j h_il + nabla_k nabla_i h_jl )
  This is the standard Lichnerowicz form (equivalent to the trace/divergence form).
  
  We compute this for the perturbed metric g_s = g_EH + s*h, extracting the
  coefficient of s^1 in the Ricci tensor, all symbolically.

  Since the metric is diagonal and depends only on r, and h is diagonal depending
  only on r, the computation is tractable. We work at theta=pi/2 where the EH
  metric is diagonal.

Output: the 3 ODEs (D Ric)_ii[h] = Lambda*g_ii for i=0,1,3 as sympy expressions
in f1(r), f2(r), f3(r) and their derivatives, then solve with solve_bvp.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
import numpy as np
from scipy.integrate import solve_bvp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step65_symbolic_lichnerowicz_odes.json"

print("=== Symbolic linearized Ricci ODEs on EH ===")

r, a, Lam, s = sp.symbols('r a Lambda s', positive=True)
W = 1 - a**4/r**4

# Background EH (diagonal at theta=pi/2)
g00 = 1/W
g11 = r**2/4
g22 = r**2/4
g33 = r**2*W/4

# Perturbation functions
f1, f2, f3 = sp.symbols('f1 f2 f3', cls=sp.Function)

# Perturbed metric: g_s = g + s*h, h = diag(f1*g00, f2*g11, f2*g11, f3*g33)
# So (g_s)_ii = g_ii*(1 + s*f_i)
gs00 = g00*(1 + s*f1(r))
gs11 = g11*(1 + s*f2(r))
gs22 = g22*(1 + s*f2(r))
gs33 = g33*(1 + s*f3(r))
gs_diag = [gs00, gs11, gs22, gs33]

# We compute the Ricci tensor of g_s to first order in s.
# For a diagonal metric depending only on r:
# Christoffel (nonzero at theta=pi/2):
#   G^0_00 = (1/2) g^{00} d_r g_00
#   G^0_ii = -(1/2) g^{00} d_r g_ii   (i=1,2,3)
#   G^i_i0 = G^i_0i = (1/2) g^{ii} d_r g_ii
# Ricci (diagonal):
#   Ric_00 = -sum_i d_r(G^i_i0) + G^0_00 * sum_i G^i_i0 - sum_i (G^i_i0)^2
#   Ric_jj = d_r(G^0_jj) + (G^0_00 + sum_i G^i_i0)*G^0_jj - 2*G^0_jj*G^j_j0   (j=1,2,3)
# (these were verified in the previous scripts)

def christoffels(gd):
    """Return (G000, [Gi0 for i=1,2,3], [G0ii for i=1,2,3]) for diagonal metric gd."""
    G000 = sp.diff(gd[0], r)/(2*gd[0])
    Gi0 = [sp.diff(gd[i], r)/(2*gd[i]) for i in [1,2,3]]
    G0ii = [-sp.diff(gd[i], r)/(2*gd[0]) for i in [1,2,3]]
    return G000, Gi0, G0ii

def ricci_diagonal(gd):
    """Return [Ric_00, Ric_11, Ric_22, Ric_33] for diagonal r-dependent metric."""
    G000, Gi0, G0ii = christoffels(gd)
    Ric00 = -sum(sp.diff(Gi0[i], r) for i in range(3)) + G000*sum(Gi0) - sum(G**2 for G in Gi0)
    Rics = [sp.simplify(Ric00)]
    for j in range(3):
        Ricjj = sp.diff(G0ii[j], r) + (G000 + sum(Gi0))*G0ii[j] - 2*G0ii[j]*Gi0[j]
        Rics.append(sp.simplify(Ricjj))
    return Rics

# Compute Ricci of g_s
print("Computing Ricci of perturbed metric symbolically...")
Ric_s = ricci_diagonal(gs_diag)

# Verify zeroth order is zero (EH Ricci-flat)
Ric0 = [sp.simplify(R.subs(s, 0)) for R in Ric_s]
print(f"Zeroth-order Ricci (should be 0): {[sp.simplify(x) for x in Ric0]}")

# Extract first-order coefficient = linearized Ricci applied to h
print("Extracting first-order (linearized Ricci)...")
dRic = [sp.simplify(sp.diff(R, s).subs(s, 0)) for R in Ric_s]

# The linearized Ricci in coordinate basis. Divide by g_ii for frame components.
# But for the ODE we want (dRic)_ii[h] = Lambda*g_ii, i.e., dRic_ii = Lambda*g_ii.

# Substitute a=1 for numerical work
a_val = 1.0
subs_a = {a: a_val}

print("\nLinearized Ricci components (coordinate basis, a=1):")
labels = ['(0,0)', '(1,1)', '(2,2)', '(3,3)']
for i in range(4):
    expr = sp.simplify(dRic[i].subs(subs_a))
    print(f"  dRic{labels[i]} = {expr}")

# The three independent ODEs: dRic_00 = Lam*g00, dRic_11 = Lam*g11, dRic_33 = Lam*g33
eq00 = sp.Eq(dRic[0].subs(subs_a), Lam*g00.subs(subs_a))
eq11 = sp.Eq(dRic[1].subs(subs_a), Lam*g11.subs(subs_a))
eq33 = sp.Eq(dRic[3].subs(subs_a), Lam*g33.subs(subs_a))

# Solve for f1'', f2'', f3''
f1pp = sp.Derivative(f1(r), (r, 2))
f2pp = sp.Derivative(f2(r), (r, 2))
f3pp = sp.Derivative(f3(r), (r, 2))

print("\nSolving for second derivatives...")
try:
    sols = sp.solve([eq00, eq11, eq33], [f1pp, f2pp, f3pp], dict=True)
    if sols:
        sol = sols[0]
        e1 = sp.simplify(sol[f1pp])
        e2 = sp.simplify(sol[f2pp])
        e3 = sp.simplify(sol[f3pp])
        print("Decoupled system obtained.")
        decoupled = True
    else:
        print("Could not decouple.")
        decoupled = False
        e1 = e2 = e3 = None
except Exception as ex:
    print(f"Solve failed: {ex}")
    decoupled = False
    e1 = e2 = e3 = None

if decoupled:
    # Lambdify for solve_bvp
    args = [r, f1(r), sp.Derivative(f1(r), r), f2(r), sp.Derivative(f2(r), r), f3(r), sp.Derivative(f3(r), r), Lam]
    E1 = sp.lambdify(args, e1.subs(subs_a), 'numpy')
    E2 = sp.lambdify(args, e2.subs(subs_a), 'numpy')
    E3 = sp.lambdify(args, e3.subs(subs_a), 'numpy')
    
    Lam_val = 1.0
    def ode_sys(rr, y):
        f1v, f1pv, f2v, f2pv, f3v, f3pv = y
        return np.vstack([
            f1pv, E1(rr, f1v, f1pv, f2v, f2pv, f3v, f3pv, Lam_val),
            f2pv, E2(rr, f1v, f1pv, f2v, f2pv, f3v, f3pv, Lam_val),
            f3pv, E3(rr, f1v, f1pv, f2v, f2pv, f3v, f3pv, Lam_val),
        ])
    
    # Boundary conditions:
    # At bolt r_min ~ 1.05: regularity. For the diagonal ansatz on EH,
    # smoothness at the bolt requires h to be a smooth tensor. 
    # The natural BC: f_i'(r_min) = 0 (radial derivative vanishes).
    # At infinity r_max: h should match the ambient quadratic H.
    # For the flat ambient with curvature Lambda, the matching is to a
    # specific quadratic form. We use f_i(r_max) = c_i * r_max^2 with
    # c_i determined by requiring the solution to be a "growing" mode.
    # For a first solve, use the homogeneous-growing BC f_i(r_max)/r_max^2 -> const.
    # Simplest: f_i(r_max) = K*r_max^2 with K a free constant we scan.
    
    r_min = 1.05
    r_max = 50.0
    
    # Scan over the matching constant K
    best = None
    for K in [0.0, 0.01, 0.05, 0.1, 0.125, 0.25]:
        def bc(ya, yb, K=K):
            return np.array([
                ya[1], ya[3], ya[5],  # Neumann at bolt
                yb[0] - K*r_max**2, yb[2] - K*r_max**2, yb[4] - K*r_max**2,
            ])
        r_mesh = np.linspace(r_min, r_max, 150)
        y_g = np.zeros((6, r_mesh.size))
        y_g[0] = K*r_mesh**2; y_g[1] = 2*K*r_mesh
        y_g[2] = K*r_mesh**2; y_g[3] = 2*K*r_mesh
        y_g[4] = K*r_mesh**2; y_g[5] = 2*K*r_mesh
        try:
            sol_bvp = solve_bvp(ode_sys, bc, r_mesh, y_g, tol=1e-5, max_nodes=8000)
            ok = bool(sol_bvp.success)
            maxres = float(np.max(np.abs(sol_bvp.rms_residuals))) if hasattr(sol_bvp, 'rms_residuals') else None
            print(f"  K={K}: success={ok}, max_res={maxres}")
            if ok and (best is None):
                best = (K, sol_bvp)
        except Exception as ex:
            print(f"  K={K}: FAILED {ex}")
    
    if best is not None:
        K_best, sol_best = best
        print(f"\nBest solution: K={K_best}")
        # Evaluate the solution
        r_eval = np.linspace(r_min, r_max, 20)
        Y = sol_best.sol(r_eval)
        print("  f1(r):", np.array2string(Y[0][:8], precision=4))
        print("  f2(r):", np.array2string(Y[2][:8], precision=4))
        print("  f3(r):", np.array2string(Y[4][:8], precision=4))
        
        # Check growth rate at large r
        growth = Y[0][-1]/r_eval[-1]**2, Y[2][-1]/r_eval[-1]**2, Y[4][-1]/r_eval[-1]**2
        print(f"  f_i/r^2 at r_max: {growth}")
        
        sol_data = {
            "K": K_best,
            "r_eval": r_eval.tolist(),
            "f1": Y[0].tolist(),
            "f2": Y[2].tolist(),
            "f3": Y[4].tolist(),
        }
    else:
        print("\nNo BVP solution found for any K.")
        sol_data = None
else:
    sol_data = None

# Save
data = {
    "status": "ok" if sol_data else "ode_derived_bvp_unsolved",
    "zeroth_order_ricci_zero": all(x == 0 for x in Ric0),
    "linearized_ricci_coordinate": {labels[i]: str(sp.simplify(dRic[i].subs(subs_a))) for i in range(4)},
    "ode_decoupled": decoupled,
    "solution": sol_data,
}
OUT.write_text(json.dumps(data, indent=2))
print(f"\nOutput: {OUT}")

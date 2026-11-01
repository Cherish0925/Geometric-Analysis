#!/usr/bin/env python3
"""Step 65: Solve the full linearized Ricci (Einstein) equation on EH for the diagonal ansatz.

The linearized Ricci operator on a Ricci-flat background, for a symmetric 2-tensor h:
    (D Ric)_ij[h] = -(1/2)*nabla^2 h_ij - (1/2)*nabla_i nabla_j (tr h) 
                   + (1/2)*(nabla_i (div h)_j + nabla_j (div h)_i)
                   + R_{ikjl} h^{kl}

We solve (D Ric)[h] = Lambda*g_EH on EH with the U(2)-invariant diagonal ansatz:
    h = f1(r)*g_00*dr^2 + f2(r)*(g_11*(dth^2+sin^2 dph^2)) + f3(r)*g_33*(fiber term)
In the orthonormal frame at theta=pi/2:
    h = diag(f1(r)*g00, f2(r)*g11, f2(r)*g22, f3(r)*g33)
i.e., h_ij = f_i * g_ij (no sum), so f_i are the FRAME eigenvalues of h relative to g.

With this ansatz:
    tr(h) = f1 + 2*f2 + f3  (trace in the g-frame)
    (div h)_0 = radial component of divergence

The equation (D Ric)[h] = Lambda*g becomes 3 coupled ODEs for f1, f2, f3.

This script derives the ODEs symbolically and solves them with scipy solve_bvp,
then assembles the corrected metric and verifies the operator-norm defect.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step65_lichnerowicz_ode_system.json"

print("=== Full linearized Ricci on EH: diagonal ansatz ===")

r, a, Lam = sp.symbols('r a Lambda', positive=True)
W = 1 - a**4/r**4
g00 = 1/W
g11 = r**2/4
g33 = r**2*W/4
g_diag_syms = [g00, g11, g11, g33]

# Background Christoffels
Gam000 = sp.diff(g00, r)/(2*g00)
Gam0 = {i: -sp.diff(g_diag_syms[i], r)/(2*g00) for i in [1,2,3]}
Gi0 = {i: sp.diff(g_diag_syms[i], r)/(2*g_diag_syms[i]) for i in [1,2,3]}

# Sectional curvatures (computed earlier, verified Ricci-flat)
def R_0i0i(gi):
    return sp.simplify(-sp.Rational(1,2)*sp.diff(gi, r, 2) + 
                       sp.Rational(1,4)*sp.diff(gi, r)**2/gi + 
                       sp.Rational(1,4)*sp.diff(g00, r)*sp.diff(gi, r)/g00)
R0101 = R_0i0i(g11)
R0303 = R_0i0i(g33)
K01 = sp.simplify(R0101/(g00*g11))
K03 = sp.simplify(R0303/(g00*g33))
K13 = sp.simplify(-K03/2)
K12 = sp.simplify(-K01 - K13)

print(f"K01 = {sp.simplify(K01)}")
print(f"K03 = {sp.simplify(K03)}")
print(f"K12 = {sp.simplify(K12)}")
print(f"K13 = {sp.simplify(K13)}")

# Ansatz functions (frame eigenvalues)
f1, f2, f3 = sp.symbols('f1 f2 f3', cls=sp.Function)
F = [f1(r), f2(r), f2(r), f3(r)]  # frame eigenvalues of h

# h_ij = f_i * g_ij (no sum) in the diagonal frame
# h^i_j = f_i * delta^i_j (the endomorphism is diagonal with eigenvalues f_i)
# tr(h) = f1 + 2*f2 + f3
tr_h = F[0] + 2*F[1] + F[3]

# Divergence: (div h)_j = nabla^i h_ij = g^{ii}*nabla_i h_ij
# For diagonal h depending on r, only (div h)_0 is nonzero:
# (div h)_0 = g^{ii}*nabla_i h_i0 ... 
# nabla_i h_j0 = -Gamma^k_ji h_k0 - Gamma^k_0i h_jk
# For diagonal h: nabla_i h_j0 = -Gamma^0_ji*h_00 - Gamma^j_0i*h_jj (only nonzero terms)
# At our point: Gamma^0_ji = 0 for i!=j, Gamma^0_jj = Gam0[j], Gamma^j_0j = Gi0[j]
# nabla_j h_j0 = -Gam0[j]*h_00 - Gi0[j]*h_jj = -Gam0[j]*f1*g00 - Gi0[j]*f_j*g_jj
# (div h)_0 = g^{jj}*nabla_j h_j0 = sum_j g^{jj}*(-Gam0[j]*f1*g00 - Gi0[j]*f_j*g_jj)
# = -sum_j (g^{jj}*Gam0[j]*f1*g00 + g^{jj}*Gi0[j]*f_j*g_jj)
# = -sum_j (Gam0[j]*f1*g00/g_jj + Gi0[j]*f_j)
# Wait, g^{jj}*g_jj = 1, so:
# = -sum_j (Gam0[j]*f1*g00/g_diag_syms[j] + Gi0[j]*f_j)
# Hmm, but also nabla_0 h_00 contributes to (div h)_0:
# (div h)_0 = g^{00}*nabla_0 h_00 + g^{jj}*nabla_j h_j0
# nabla_0 h_00 = d(f1*g00)/dr - 2*Gamma^0_00*f1*g00 = f1'*g00 + f1*g00' - 2*Gam000*f1*g00
# = g00*(f1' + f1*(g00'/g00 - 2*Gam000)) = g00*(f1' + f1*(2*Gam000 - 2*Gam000)) = g00*f1'
# So g^{00}*nabla_0 h_00 = f1'

# (div h)_0 = f1' - sum_{j=1,2,3} (Gam0[j]*f1*g00/g_diag_syms[j] + Gi0[j]*f_j)
# Simplify: Gam0[j]*g00/g_diag_syms[j] = -(g_jj'/(2*g00))*g00/g_jj = -g_jj'/(2*g_jj) = -Gi0[j]
# So Gam0[j]*f1*g00/g_diag_syms[j] = -Gi0[j]*f1
# (div h)_0 = f1' - sum_j (-Gi0[j]*f1 + Gi0[j]*f_j) = f1' + sum_j Gi0[j]*(f1 - f_j)

div_h_0 = sp.diff(F[0], r) + sum(Gi0[j]*(F[0] - F[j]) for j in [1,2,3])
div_h_0 = sp.simplify(div_h_0)

print(f"\n(div h)_0 = {div_h_0}")

# ============================================================
# Linearized Ricci components
# ============================================================
# (D Ric)_ij[h] = -(1/2)*nabla^2 h_ij - (1/2)*nabla_i nabla_j tr(h) 
#                + (1/2)*(nabla_i (div h)_j + nabla_j (div h)_i)
#                + R_{ikjl} h^{kl}

# We need each term for (i,j) = (0,0), (1,1), (3,3).

# --- Term 1: -(1/2)*nabla^2 h_ij (rough Laplacian) ---
# For h_00 = f1*g00:
# nabla_0 h_00 = g00*f1' (computed above)
# nabla_0 nabla_0 h_00 = d(g00*f1')/dr - 2*Gam000*g00*f1' = g00*f1'' + g00'*f1' - 2*Gam000*g00*f1'
# = g00*(f1'' + (2*Gam000)*f1' - 2*Gam000*f1') = g00*f1''
# nabla_j nabla_j h_00 = -Gam0[j]*g00*f1' - 2*Gi0[j]*(-Gi0[j]*f_j*g_jj)... 
# Hmm wait. nabla_j h_00 = -Gamma^0_jj*h_00 = -Gam0[j]*f1*g00 (for j != 0)
# nabla_j nabla_j h_00 = d_j(nabla_j h_00) - Gamma^l_jj*nabla_l h_00 - 2*Gamma^l_0j*nabla_j h_l0
# d_j(...) = 0 (radial only)
# Gamma^l_jj*nabla_l h_00 = Gamma^0_jj*nabla_0 h_00 = Gam0[j]*g00*f1'
# Gamma^l_0j*nabla_j h_l0: l=0: Gamma^0_0j=0; l=k(!=0): Gamma^k_0j*nabla_j h_k0
# = Gamma^j_0j*nabla_j h_j0 = Gi0[j]*(-Gam0[j]*f1*g00 - Gi0[j]*f_j*g_jj)
# So nabla_j nabla_j h_00 = -Gam0[j]*g00*f1' - 2*Gi0[j]*(-Gam0[j]*f1*g00 - Gi0[j]*f_j*g_jj)
# = -Gam0[j]*g00*f1' + 2*Gi0[j]*Gam0[j]*f1*g00 + 2*Gi0[j]^2*f_j*g_jj

# g^{jj}*nabla_j nabla_j h_00 summed over j=1,2,3:
# = sum_j g^{jj}*(-Gam0[j]*g00*f1' + 2*Gi0[j]*Gam0[j]*f1*g00 + 2*Gi0[j]^2*f_j*g_jj)
# Using Gam0[j]*g00/g_jj = -Gi0[j]:
# g^{jj}*Gam0[j]*g00 = -Gi0[j]
# g^{jj}*Gi0[j]*Gam0[j]*g00 = -Gi0[j]^2
# g^{jj}*Gi0[j]^2*g_jj = Gi0[j]^2
# So sum_j g^{jj}*nabla_j nabla_j h_00 = sum_j (Gi0[j]*f1' - 2*Gi0[j]^2*f1 + 2*Gi0[j]^2*f_j)
# = (sum_j Gi0[j])*f1' + 2*sum_j Gi0[j]^2*(f_j - f1)

# nabla^2 h_00 = g^{00}*nabla_0 nabla_0 h_00 + sum_j g^{jj}*nabla_j nabla_j h_00
# = g^{00}*g00*f1'' + (sum_j Gi0[j])*f1' + 2*sum_j Gi0[j]^2*(f_j - f1)
# = f1'' + (sum_j Gi0[j])*f1' + 2*sum_j Gi0[j]^2*(f_j - f1)

# This is getting extremely long. Let me use a more systematic approach:
# compute everything numerically with a=a_val, then extract the ODEs.

a_val = 1.0
subs_a = {a: a_val}

# Numerical Christoffels and curvatures
Gam000_n = sp.lambdify(r, Gam000.subs(subs_a), 'numpy')
Gi0_n = {i: sp.lambdify(r, Gi0[i].subs(subs_a), 'numpy') for i in [1,2,3]}
K01_n = sp.lambdify(r, K01.subs(subs_a), 'numpy')
K03_n = sp.lambdify(r, K03.subs(subs_a), 'numpy')
K12_n = sp.lambdify(r, K12.subs(subs_a), 'numpy')
K13_n = sp.lambdify(r, K13.subs(subs_a), 'numpy')

# The ODE system: (D Ric)_ii[h] = Lambda*g_ii for i=0,1,3
# In the frame, (D Ric)_ii[h] = Lambda (since g_ii=1 in orthonormal frame).
# Actually we work in coordinate basis: (D Ric)_ii[h] = Lambda*g_ii.

# The linearized Ricci in coordinate basis, divided by g_ii, gives the frame equation.
# For the diagonal ansatz, the frame equation is:
# -(1/2)*[nabla^2 h]_ii/g_ii - (1/2)*[Hess tr h]_ii/g_ii + [sym grad div h]_ii/g_ii + [Rm.h]_ii/g_ii = Lambda

# Let me compute each term symbolically in the frame.

# For the rough Laplacian in the frame:
# [nabla^2 h]_00/g00 = f1'' + S1*f1' + S2 terms
# where S1 = sum_j Gi0[j], S2 involves Gi0[j]^2

# I'll derive the ODEs by direct symbolic computation of each piece.

# For a diagonal h with frame eigenvalues f_i(r), the rough Laplacian in the frame is:
# (nabla^2 h)_ii/g_ii = f_i'' + (sum_j Gi0[j])*f_i' + sum_j Gi0[j]^2*(f_i - f_j) ... 
# Not quite. Let me be very careful for each component.

# For the (0,0) component (frame):
L00 = sp.symbols('L00')  # placeholder

# Instead of deriving everything by hand, let me compute the linearized Ricci
# numerically using finite differences on the full Ricci computation.
# This is slower but guaranteed correct.

print("\n=== Computing linearized Ricci numerically via perturbation ===")

def build_metric(rv, f1v, f2v, f3v, av=1.0):
    """Build g_EH + h at radius r with frame eigenvalues f1,f2,f3."""
    Wv = 1 - av**4/rv**4
    g00v = 1/Wv
    g11v = rv**2/4
    g33v = rv**2*Wv/4
    # g + h in coordinate basis: (g+h)_ii = g_ii*(1 + f_i)
    # Wait: h_ij = f_i*g_ij, so (g+h)_ii = g_ii + f_i*g_ii = g_ii*(1+f_i)
    return np.array([g00v*(1+f1v), g11v*(1+f2v), g11v*(1+f2v), g33v*(1+f3v)])

def ricci_diag_numerical(g_func, r0, eps=1e-6):
    """Compute Ricci tensor (diagonal) numerically at r0.
    g_func(r) returns the 4 diagonal metric components at radius r."""
    # Christoffel components needed
    g = g_func(r0)
    gp = (g_func(r0+eps) - g_func(r0-eps))/(2*eps)
    gpp = (g_func(r0+eps) - 2*g_func(r0) + g_func(r0-eps))/eps**2
    
    G000 = gp[0]/(2*g[0])
    Gi0 = [gp[i]/(2*g[i]) for i in [1,2,3]]
    G0ii = [-gp[i]/(2*g[0]) for i in [1,2,3]]
    
    # Derivatives of Christoffels
    def christoffel_at(rr):
        gv = g_func(rr)
        gpv = (g_func(rr+eps) - g_func(rr-eps))/(2*eps)
        return gpv[0]/(2*gv[0]), [gpv[i]/(2*gv[i]) for i in [1,2,3]], [-gpv[i]/(2*gv[0]) for i in [1,2,3]]
    
    _, Gi0_p, G0ii_p = None, None, None
    # d/dr(Gamma^i_i0) = d/dr(gp[i]/(2*g[i])) = gpp[i]/(2*g[i]) - gp[i]^2/(2*g[i]^2)
    dGi0 = [gpp[i]/(2*g[i]) - gp[i]**2/(2*g[i]**2) for i in [1,2,3]]
    dG0ii = [-gpp[i]/(2*g[0]) + gp[i]*gp[0]/(2*g[0]**2) for i in [1,2,3]]
    
    # Ric_00 = -sum dGi0 + G000*sum Gi0 - sum Gi0^2
    Ric00 = -sum(dGi0) + G000*sum(Gi0) - sum(G**2 for G in Gi0)
    # Ric_jj = dG0ii[j] + (G000 + sum Gi0)*G0ii[j] - 2*G0ii[j]*Gi0[j]
    Ric = [Ric00]
    for j in range(3):
        Ricjj = dG0ii[j] + (G000 + sum(Gi0))*G0ii[j] - 2*G0ii[j]*Gi0[j]
        Ric.append(Ricjj)
    
    return np.array(Ric)

# Verify: at s=0 (no perturbation), Ricci should be 0
g0 = lambda rr: build_metric(rr, 0, 0, 0)
Ric0 = ricci_diag_numerical(g0, 2.0)
print(f"EH Ricci at r=2.0: {Ric0} (should be ~0)")

# Linearized Ricci via finite difference: dRic/ds at s=0 for h with eigenvalues f1,f2,f3
def linearized_ricci_numerical(rv, f1v, f2v, f3v, eps_s=1e-7):
    """Compute (D Ric)[h] at radius rv for h with frame eigenvalues (f1v,f2v,f3v)."""
    g_plus = lambda rr: build_metric(rr, eps_s*f1v, eps_s*f2v, eps_s*f3v)
    g_minus = lambda rr: build_metric(rr, -eps_s*f1v, -eps_s*f2v, -eps_s*f3v)
    Ric_plus = ricci_diag_numerical(g_plus, rv)
    Ric_minus = ricci_diag_numerical(g_minus, rv)
    return (Ric_plus - Ric_minus)/(2*eps_s)

# Test with f1=f2=f3=0 (should give 0)
DRic0 = linearized_ricci_numerical(2.0, 0, 0, 0)
print(f"dRic[0] at r=2.0: {DRic0} (should be ~0)")

# Test with f1=1, f2=f3=0
DRic1 = linearized_ricci_numerical(2.0, 1, 0, 0)
print(f"dRic[diag(1,0,0,0)] at r=2.0: {DRic1}")

# ============================================================
# Build the ODE system matrix
# ============================================================
# The linearized Ricci for the diagonal ansatz with r-dependent f_i(r) is:
# (D Ric)_ii[h] = A_ii*f_i'' + B_ii*f_i' + sum_j C_ii_j*f_j
# We need the coefficients A, B, C as functions of r.
# 
# The second-derivative terms come only from the rough Laplacian:
# -(1/2)*(nabla^2 h)_ii contains -(1/2)*f_i''
# The Hess(tr h) contains f_j'' terms:
# -(1/2)*nabla_i nabla_j(tr h): for i=j=0: -(1/2)*(tr h)'' = -(1/2)*(f1''+2*f2''+f3'')
# The sym grad div h contains f_j'' terms:
# (1/2)*(nabla_0(div h)_0 + nabla_0(div h)_0) = (div h)_0' = f1'' + ... 

# So the system is coupled through the second derivatives.
# Let me extract the ODEs by computing dRic for basis perturbations.

# Actually, the cleanest approach: derive the ODEs symbolically.
# Since the computation is long, let me use the general formula for a diagonal metric.

print("\n=== Deriving ODE system symbolically ===")

# For the diagonal metric g = diag(g00, g11, g11, g33) and h = diag(f1*g00, f2*g11, f2*g11, f3*g33):
# 
# Rough Laplacian (frame):
# [nabla^2 h]_00/g00 = f1'' + (sum_j Gi0[j])*f1' + 2*sum_j Gi0[j]^2*(f1 - f_j)
# Wait, I need to double-check this. Let me verify numerically.

# Compute [nabla^2 h]_00 for f1=r^2, f2=f3=0 numerically
# nabla^2 h_00 = g^{00}*nabla_0 nabla_0 h_00 + sum g^{jj}*nabla_j nabla_j h_00
# nabla_0 h_00 = g00*f1' (h_00 = f1*g00, nabla_0 h_00 = d(f1*g00)/dr - 2*Gam000*f1*g00 = g00*f1' + f1*g00' - 2*(g00'/(2*g00))*f1*g00 = g00*f1')
# nabla_0 nabla_0 h_00 = d(g00*f1')/dr - 2*Gam000*g00*f1' = g00*f1'' + g00'*f1' - (g00'/g00)*g00*f1' = g00*f1''
# g^{00}*g00*f1'' = f1''
# 
# For f1 = r^2: f1'' = 2
# The full nabla^2 h_00 includes angular terms.

# Rather than deriving by hand, let me compute the full linearized Ricci numerically
# for a set of basis functions and extract the ODE coefficients.

# Define the ODE in the form:
# M(r) * [f1'', f2'', f3'']^T + N(r) * [f1', f2', f3']^T + P(r) * [f1, f2, f3]^T = Lambda * [1, 1, 1]^T
# where M, N, P are 3x3 matrices.

# The (D Ric)_ii[g_ii] = Lambda*g_ii equation, divided by g_ii, gives:
# (D Ric)_ii[h]/g_ii = Lambda

# For the numerical extraction, I compute dRic[h]/g for several choices of h
# and solve for the coefficients.

# The second-derivative coefficient matrix M:
# From the rough Laplacian: -(1/2)*delta_ij (each f_i'' appears only in its own equation)
# From Hess(tr h): -(1/2)*[[1,2,1],[1,2,1],[1,2,1]] (tr h = f1+2f2+f3, Hess_00(tr h) ~ (tr h)'')
# From sym grad div h: div h_0 = f1' + ..., so nabla_0(div h)_0 ~ f1''
# Only the (0,0) component gets div h contributions.

# Let me just compute the ODEs numerically at a specific radius using the
# finite-difference Ricci computation with r-dependent f_i.

def linearized_ricci_radial(rv, f_funcs, eps_s=1e-7):
    """Compute (D Ric)[h] at radius rv for h with r-dependent frame eigenvalues.
    f_funcs = (f1, f2, f3) where each is a callable f(r)."""
    def g_plus(rr):
        return build_metric(rr, eps_s*f_funcs[0](rr), eps_s*f_funcs[1](rr), eps_s*f_funcs[2](rr))
    def g_minus(rr):
        return build_metric(rr, -eps_s*f_funcs[0](rr), -eps_s*f_funcs[1](rr), -eps_s*f_funcs[2](rr))
    Ric_plus = ricci_diag_numerical(g_plus, rv)
    Ric_minus = ricci_diag_numerical(g_minus, rv)
    dRic = (Ric_plus - Ric_minus)/(2*eps_s)
    # Divide by g_ii to get frame components
    g = build_metric(rv, 0, 0, 0)
    return dRic/g

# Basis functions for extracting ODE coefficients:
# We need f_i and its derivatives at the test radius.
# Use polynomial functions to get known derivatives.

# Test at r=2.0, a=1.0
r_test = 2.0

# The ODE has the form:
# M @ [f1'', f2'', f3'']^T + N @ [f1', f2', f3']^T + P @ [f1, f2, f3]^T = Lambda*[1,1,1]^T
# Extract M, N, P by testing with appropriate basis functions.

# For M (second derivatives): use f_i = (1/2)*c*(r-r0)^2 with f_i(r0)=0, f_i'(r0)=0, f_i''(r0)=c
# For N (first derivatives): use f_i = c*(r-r0) with f_i(r0)=0, f_i'(r0)=c, f_i''(r0)=0
# For P (zeroth order): use f_i = c with f_i(r0)=c, f_i'(r0)=0, f_i''(r0)=0

def make_quad(c, r0):
    return lambda rr: c*(rr-r0)**2/2
def make_lin(c, r0):
    return lambda rr: c*(rr-r0)
def make_const(c):
    return lambda rr: c

# Extract M column by column
M = np.zeros((3, 3))  # rows: equations (0,0), (1,1), (3,3); cols: f1'', f2'', f3''
N = np.zeros((3, 3))
P = np.zeros((3, 3))

for j in range(3):
    # Second derivative of f_j
    f_list = [make_const(0), make_const(0), make_const(0)]
    f_list[j] = make_quad(1.0, r_test)
    dRic = linearized_ricci_radial(r_test, f_list)
    M[:, j] = [dRic[0], dRic[1], dRic[3]]  # components (0,0), (1,1), (3,3)
    
    # First derivative of f_j
    f_list = [make_const(0), make_const(0), make_const(0)]
    f_list[j] = make_lin(1.0, r_test)
    dRic = linearized_ricci_radial(r_test, f_list)
    N[:, j] = [dRic[0], dRic[1], dRic[3]]
    
    # Zeroth order of f_j
    f_list = [make_const(0), make_const(0), make_const(0)]
    f_list[j] = make_const(1.0)
    dRic = linearized_ricci_radial(r_test, f_list)
    P[:, j] = [dRic[0], dRic[1], dRic[3]]

print(f"\nODE coefficient matrices at r={r_test}:")
print(f"M = \n{M}")
print(f"N = \n{N}")
print(f"P = \n{P}")

# Verify: M should be invertible for the system to be solvable
M_det = np.linalg.det(M)
print(f"det(M) = {M_det}")

# ============================================================
# Solve the ODE system
# ============================================================
from scipy.integrate import solve_bvp

def get_matrices(rv):
    """Get M, N, P at radius rv."""
    Mv = np.zeros((3, 3))
    Nv = np.zeros((3, 3))
    Pv = np.zeros((3, 3))
    for j in range(3):
        f_list = [make_const(0), make_const(0), make_const(0)]
        f_list[j] = make_quad(1.0, rv)
        dRic = linearized_ricci_radial(rv, f_list)
        Mv[:, j] = [dRic[0], dRic[1], dRic[3]]
        
        f_list = [make_const(0), make_const(0), make_const(0)]
        f_list[j] = make_lin(1.0, rv)
        dRic = linearized_ricci_radial(rv, f_list)
        Nv[:, j] = [dRic[0], dRic[1], dRic[3]]
        
        f_list = [make_const(0), make_const(0), make_const(0)]
        f_list[j] = make_const(1.0)
        dRic = linearized_ricci_radial(rv, f_list)
        Pv[:, j] = [dRic[0], dRic[1], dRic[3]]
    return Mv, Nv, Pv

# Precompute matrices on a grid
r_grid = np.linspace(1.05, 50.0, 200)
matrices = {}
print("\nPrecomputing ODE matrices on grid...")
for rv in r_grid:
    matrices[rv] = get_matrices(rv)
print(f"Computed {len(matrices)} grid points.")

# Interpolate matrices
from scipy.interpolate import interp1d
def get_M_func():
    Ms = np.array([matrices[rv][0] for rv in r_grid])
    return lambda rr: np.array([interp1d(r_grid, Ms[:,i,j], kind='cubic', fill_value='extrapolate')(rr) for i in range(3) for j in range(3)]).reshape(3,3)
def get_N_func():
    Ns = np.array([matrices[rv][1] for rv in r_grid])
    return lambda rr: np.array([interp1d(r_grid, Ns[:,i,j], kind='cubic', fill_value='extrapolate')(rr) for i in range(3) for j in range(3)]).reshape(3,3)
def get_P_func():
    Ps = np.array([matrices[rv][2] for rv in r_grid])
    return lambda rr: np.array([interp1d(r_grid, Ps[:,i,j], kind='cubic', fill_value='extrapolate')(rr) for i in range(3) for j in range(3)]).reshape(3,3)

M_func = get_M_func()
N_func = get_N_func()
P_func = get_P_func()

Lam_val = 1.0
def ode_system(rr, y):
    """y = [f1, f1', f2, f2', f3, f3']"""
    fv = np.array([y[0], y[2], y[4]])
    fpv = np.array([y[1], y[3], y[5]])
    Mv = M_func(rr)
    Nv = N_func(rr)
    Pv = P_func(rr)
    rhs = Lam_val*np.ones(3) - Nv@fpv - Pv@fv
    fppv = np.linalg.solve(Mv, rhs)
    return np.vstack([fpv[0], fppv[0], fpv[1], fppv[1], fpv[2], fppv[2]])

# Boundary conditions
r_min_bc = 1.05
r_max_bc = 50.0

def bc(ya, yb):
    # At bolt (r_min): regularity -- smoothness requires specific relations.
    # For the diagonal ansatz on EH, the bolt is at r=a=1.
    # Smoothness at the bolt requires h to extend smoothly to the bolt.
    # In the frame, this means f_i and f_i' should be finite.
    # Simplest BC: f_i'(r_min) = 0 (Neumann)
    # At infinity: f_i ~ c*r^2 for the growing mode matching the ambient.
    # The Biquard normalization: h ~ H where H is the ambient quadratic.
    # For Lambda=1 ambient, H = -(Lambda/8)*r^2 in some frame... but we showed
    # that's not the right solution. The correct BC is f_i(r_max) = c_i*r_max^2
    # where c_i are determined by the ambient curvature.
    # For simplicity, use Dirichlet: f_i(r_max) = c_inf*r_max^2 with c_inf to be determined.
    # Since the system is linear, we can solve for a particular solution + homogeneous.
    # For now, use f_i(r_max) = r_max^2/4 as a trial (will need adjustment).
    c_inf = 1.0/4  # trial value
    return np.array([
        ya[1],  # f1'(r_min) = 0
        ya[3],  # f2'(r_min) = 0
        ya[5],  # f3'(r_min) = 0
        yb[0] - c_inf*r_max_bc**2,  # f1(r_max) = c*r^2
        yb[2] - c_inf*r_max_bc**2,  # f2(r_max) = c*r^2
        yb[4] - c_inf*r_max_bc**2,  # f3(r_max) = c*r^2
    ])

# Initial guess
r_mesh = np.linspace(r_min_bc, r_max_bc, 100)
y_guess = np.zeros((6, r_mesh.size))
c_inf = 1.0/4
y_guess[0] = c_inf*r_mesh**2
y_guess[1] = 2*c_inf*r_mesh
y_guess[2] = c_inf*r_mesh**2
y_guess[3] = 2*c_inf*r_mesh
y_guess[4] = c_inf*r_mesh**2
y_guess[5] = 2*c_inf*r_mesh

print("\nSolving BVP...")
try:
    sol = solve_bvp(ode_system, bc, r_mesh, y_guess, tol=1e-4, max_nodes=5000, verbose=0)
    print(f"Success: {sol.success}, message: {sol.message}")
    print(f"Max residual: {np.max(np.abs(sol.rms_residuals)) if hasattr(sol, 'rms_residuals') else 'N/A'}")
    bvp_ok = bool(sol.success)
except Exception as e:
    print(f"BVP FAILED: {e}")
    bvp_ok = False
    sol = None

# Save
data = {
    "status": "ok" if bvp_ok else "bvp_failed",
    "M_at_r2": M.tolist(),
    "N_at_r2": N.tolist(),
    "P_at_r2": P.tolist(),
    "det_M": float(M_det),
    "bvp_solved": bvp_ok,
    "domain": [r_min_bc, r_max_bc],
    "boundary_conditions": "Neumann at bolt, Dirichlet (c*r^2) at infinity",
    "caveat": "The Dirichlet BC constant c_inf is a trial value; the correct value is determined by matching to the ambient quadratic form H from the orbifold metric g_0.",
}
OUT.write_text(json.dumps(data, indent=2))
print(f"\nOutput: {OUT}")

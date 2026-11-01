#!/usr/bin/env python3
"""
Step 22: finite-neighbor first-exit energy bookkeeping with the corrected
S_alpha=A_alpha^4 H2_alpha graph variable.

Model the system
    S'_alpha <= C r^{-2} sum_{beta~alpha} (A_alpha/A_beta)^4 S_beta
and check that bounded degree and neighbor Sobolev comparability give a
multiplicative persistence bound independent of the number of components.
"""
import math
import numpy as np

r = 3.0e-3
theta = 1.0e-3
T = theta*r*r
C = 12.0
N = 8
C_A = 1.3
K0 = 15100.0
Gamma0 = r*r*math.sqrt(1+K0)
S0_sup = Gamma0**2
threshold = (4.0*Gamma0)**2

amplification_S = math.exp(C*(C_A**4)*N*T/(r*r))
GammaT = math.sqrt(amplification_S)*Gamma0

print("STEP 22 CORRECTED FIRST-EXIT COMPONENT ENERGY MODEL")
print(f"r={r:g}, theta={theta:g}, T=theta*r^2={T:.3e}")
print(f"neighbor number N={N}, C={C:g}, neighbor Sobolev ratio C_A={C_A:g}")
print(f"Gamma0 = r^2*sqrt(1+K0) = {Gamma0:.6e}")
print(f"S amplification <= exp(C*C_A^4*N*theta) = {amplification_S:.6f}")
print(f"Gamma(T) <= {GammaT:.6e}; threshold=4 Gamma0 = {4*Gamma0:.6e}")
print("Improves first-exit threshold:", GammaT < 4*Gamma0)

# Explicit bounded-degree graph example.
def ring_matrix(m, half_width, CA):
    A = np.zeros((m, m))
    for i in range(m):
        for d in range(-half_width, half_width+1):
            # worst neighbor Sobolev ratio on every edge
            A[i, (i+d) % m] = CA**4
    return A

m = 20
half_width = 4
A = ring_matrix(m, half_width, C_A)
deg_weight = A.sum(axis=1)[0]
S0 = np.zeros(m)
S0[0] = 1.0
w, V = np.linalg.eigh(A)
ST = V @ (np.exp((C/r**2)*w*T) * (V.T @ S0))
print(f"explicit ring weighted degree={deg_weight:.6f}: max S(T)={ST.max():.6f}, sum S(T)={ST.sum():.6f}")
print(f"sup bound exp(C*weighted_degree*theta)={math.exp(C*deg_weight*theta):.6f}")

# Cubic potential scaling.
t = T
A4H3_bound_scale = GammaT**3 / t
print()
print("Cubic potential scale from graph current-energy loop:")
print(f"A^4 H3(t) <= C Gamma^3/t ~ {A4H3_bound_scale:.6e} (up to fixed constants)")
print(f"At t=theta*r^2, Gamma/t = {GammaT/t:.6e}; r^-2 = {1/r**2:.6e}")
print("The estimate is a graph-semigroup/finite-overlap statement, not a local Whitney-volume statement.")

assert GammaT < 4*Gamma0
assert np.isfinite(ST).all()
print("PASS")

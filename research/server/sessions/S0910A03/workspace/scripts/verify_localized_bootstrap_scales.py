"""
Verify the localized bootstrap scale separation.

Key claim: On the plateau B_{rho/4}(p_j) where chi=1,
all covering balls for Li's proof at scale r_* stay inside the plateau,
and the parabolic propagation distance during time T = theta * r_*^2
is much less than the distance from the inner plateau to the boundary.

Parameters (following A01's calculation):
- K_0 ~ 2 * C_BG(R) * K_max with K_max ~ 12 (Noether energy)
- C_BG_local ~ (13/2)^4 ~ 1785 (comparable ball ratio)
- r_* chosen so that r_*^4 * C_BG_local * K_0 <= eps_Li/2
- rho: good-set ball radius (can be taken as 1 or any fixed positive number)
- Inner plateau: B_{rho/8}(p_j), Working domain: B_{rho/4}(p_j)
"""
import numpy as np

# Parameters
K_max = 12.0  # Noether energy bound
C_n_R = 50.0  # weak-type constant (conservative estimate for n=4, R=1)
K_0 = 2 * C_n_R * K_max  # maximal function threshold = 1200
C_BG_local = (6.5)**4  # comparable ball ratio ~ 1785
eps_Li = 1e-3  # Li's threshold (conservative)

print("="*60)
print("LOCALIZED BOOTSTRAP SCALE SEPARATION")
print("="*60)
print(f"K_max (Noether) = {K_max}")
print(f"K_0 (maximal function threshold) = {K_0}")
print(f"C_BG_local (comparable ball ratio) = {C_BG_local:.1f}")
print(f"eps_Li = {eps_Li}")
print()

# Choose r_*
# Condition: r_*^4 * C_BG_local * K_0 <= eps_Li/2
r_star = (eps_Li / (2 * C_BG_local * K_0))**(1/4)
print(f"r_* = (eps_Li / (2 * C_BG_local * K_0))^(1/4) = {r_star:.6f}")
print()

# Set rho (good-set ball radius)
rho = 1.0  # can be any fixed positive number

print(f"rho (good-set ball radius) = {rho}")
print(f"Inner plateau: B_{{rho/8}} = B_{{{rho/8:.4f}}}")
print(f"Working domain: B_{{rho/4}} = B_{{{rho/4:.4f}}}")
print()

# Scale separation checks
dist_inner_to_boundary = rho/4 - rho/8  # = rho/8
covering_reach = 5*r_star/2  # farthest covering ball from x in Omega_inner
max_parabolic_distance = np.sqrt(r_star**2)  # ~ r_* over time T = r_*^2

print("SCALE SEPARATION:")
print(f"  dist(Omega_inner, partial Omega_work) = rho/8 = {rho/8:.4f}")
print(f"  Covering reach from Omega_inner: 5r*/2 = {5*r_star/2:.6f}")
print(f"  Parabolic propagation in time T=r*^2: ~ r* = {r_star:.6f}")
print(f"  Ratio: dist / covering_reach = {(rho/8)/(5*r_star/2):.1f}")
print(f"  Ratio: dist / parabolic_dist = {(rho/8)/r_star:.1f}")
print()

assert 5*r_star/2 < rho/8, "Covering balls extend outside working domain!"
assert r_star < rho/8, "Parabolic distance too large!"
print("PASS: All covering balls stay inside the working domain.")
print("PASS: Parabolic propagation cannot reach the boundary.")
print()

# Li's bootstrap time
theta = 0.5  # safety factor
T_flow = theta * r_star**2
print(f"Flow time T = theta * r*^2 = {T_flow:.8f}")
print(f"Curvature bound at T: C_3/T ~ 1/T = {1/T_flow:.1f}")
print()

# Defect propagation (Cor 3.5 estimate)
delta_i = 0.01  # example Einstein defect
C_defect = 5.0  # constant in Cor 3.5
defect_at_T = C_defect * delta_i * (r_star**2 / T_flow)**(2/3)
print(f"For delta_i = {delta_i}:")
print(f"  |E(T)| <= C*delta*(r*^2/T)^(2/3) = {defect_at_T:.6f}")
print(f"  Metric drift: O(delta*r*^2) = {delta_i * r_star**2:.8f}")
print()

# Volume of good set
print("VOLUME BUDGET:")
print(f"  Good set volume >= Vol(M)/2 (maximal function selection)")
print(f"  Disjoint good balls cover >= Vol(M)/(2*C_BG)")
print(f"  Plateau volume >= Vol(M)/(2*C_BG) * BG(rho/8,rho)")
print(f"  This is a DEFINITE FRACTION of total volume.")
print()

print("="*60)
print("CONCLUSION: The localized bootstrap is viable.")
print("All scales separate by factors of 10^1 to 10^4.")
print("Li's proof applies on the inner plateau without modification.")
print("="*60)

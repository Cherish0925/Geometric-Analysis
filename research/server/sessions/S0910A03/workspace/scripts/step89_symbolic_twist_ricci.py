"""
Step 89: Symbolic Ricci computation for T²-invariant metric with twist.

Computes the full 4D Ricci tensor for:
  g = e^{2λ}(dr²+dz²) + e^{σ+α}(dξ₁+P dz)² + e^{σ-α}dξ₂²
  
where λ,σ,α,P depend on (r,z). This has one twist component F₁ = P_r dr∧dz.

Extracts the twist modifications to:
  - Orbit trace (area equation)
  - Orbit traceless (orbit-map equation)  
  - Base Ricci
  - Mixed Ricci (Maxwell law)
"""
import sympy as sp
from sympy import symbols, exp, Function, simplify, Matrix, Rational, sqrt
from sympy import diff, trigsimp
import json
from pathlib import Path

# Coordinates
r, z = symbols('r z')

# Functions of (r,z)
lam = Function('lambda')(r, z)
sig = Function('sigma')(r, z)
alp = Function('alpha')(r, z)
P = Function('P')(r, z)  # connection: θ₁ = dξ₁ + P dz

# Build the 4D metric in coordinates (r, z, ξ₁, ξ₂)
# g_{00} = e^{2λ}, g_{01} = 0, g_{02} = 0, g_{03} = 0
# g_{11} = e^{2λ} + e^{σ+α}P², g_{12} = e^{σ+α}P, g_{13} = 0  
# g_{22} = e^{σ+α}, g_{23} = 0
# g_{33} = e^{σ-α}

G = sp.zeros(4, 4)
e2l = exp(2*lam)
G11 = exp(sig + alp)
G22 = exp(sig - alp)

G[0,0] = e2l
G[1,1] = e2l + G11*P**2
G[1,2] = G11*P
G[2,1] = G11*P
G[2,2] = G11
G[3,3] = G22

print("Metric matrix:")
sp.pprint(G)

# Inverse metric
Ginv = G.inv()
print("\nInverse metric computed.")

# Christoffel symbols Γ^σ_{μν}
coords = [r, z, sp.Symbol('xi1'), sp.Symbol('xi2')]
n = 4

# Metric derivatives: dG[a][mu][nu] = ∂g_{μν}/∂x^a
# Only r and z derivatives are nonzero
dG = [[[sp.S(0)]*n for _ in range(n)] for _ in range(n)]
for mu in range(n):
    for nu in range(n):
        dG[0][mu][nu] = diff(G[mu,nu], r)
        dG[1][mu][nu] = diff(G[mu,nu], z)

# Christoffel symbols
Gamma = [[[sp.S(0)]*n for _ in range(n)] for _ in range(n)]
for s in range(n):
    for mu in range(n):
        for nu in range(n):
            val = sp.S(0)
            for rho in range(n):
                val += Rational(1,2)*Ginv[s,rho]*(dG[mu][nu][rho] + dG[nu][mu][rho] - dG[rho][mu][nu])
            Gamma[s][mu][nu] = val

print("Christoffel symbols computed.")

# Ricci tensor R_{μν}
# R_{μν} = ∂_ρ Γ^ρ_{μν} - ∂_ν Γ^ρ_{μρ} + Γ^ρ_{ρσ}Γ^σ_{μν} - Γ^ρ_{νσ}Γ^σ_{μρ}
Ric = sp.zeros(n, n)

for mu in range(n):
    for nu in range(mu, n):
        val = sp.S(0)
        for rho in range(n):
            # ∂_ρ Γ^ρ_{μν} (only r,z derivatives contribute)
            if rho <= 1:
                val += diff(Gamma[rho][mu][nu], coords[rho])
            # -∂_ν Γ^ρ_{μρ}
            if nu <= 1:
                val -= diff(Gamma[rho][mu][rho], coords[nu])
            for s in range(n):
                val += Gamma[rho][rho][s]*Gamma[s][mu][nu]
                val -= Gamma[rho][nu][s]*Gamma[s][mu][rho]
        Ric[mu,nu] = val
        Ric[nu,mu] = val

print("Ricci tensor computed. Simplifying key blocks...")

# Extract and simplify each block
# Mixed block: Ric(base, orbit) - the Maxwell equation
R_02 = simplify(Ric[0,2])  # Ric(r, ξ₁) 
R_12 = simplify(Ric[1,2])  # Ric(z, ξ₁)
R_03 = simplify(Ric[0,3])  # Ric(r, ξ₂)
R_13 = simplify(Ric[1,3])  # Ric(z, ξ₂)

print("\n=== MIXED RICCI (Maxwell law) ===")
print(f"Ric(r,ξ₁) = {R_02}")
print(f"Ric(z,ξ₁) = {R_12}")
print(f"Ric(r,ξ₂) = {R_03}")
print(f"Ric(z,ξ₂) = {R_13}")

# Orbit-orbit block
R_22 = simplify(Ric[2,2])
R_33 = simplify(Ric[3,3])
R_23 = simplify(Ric[2,3])

print("\n=== ORBIT RICCI ===")
print(f"Ric(ξ₁,ξ₁) = {R_22}")
print(f"Ric(ξ₂,ξ₂) = {R_33}")
print(f"Ric(ξ₁,ξ₂) = {R_23}")

# Now identify twist terms: set P=0 to get OT part, subtract
# Define substitution P=0
ot_sub = {P: 0, P.diff(r): 0, P.diff(z): 0, 
           P.diff(r,r): 0, P.diff(r,z): 0, P.diff(z,z): 0}

R_22_ot = R_22.subs(ot_sub)
R_33_ot = R_33.subs(ot_sub)
R_22_twist = simplify(R_22 - R_22_ot)
R_33_twist = simplify(R_33 - R_33_ot)

print("\n=== ORBIT TWIST CONTRIBUTIONS ===")
print(f"Ric_twist(ξ₁,ξ₁) = {R_22_twist}")
print(f"Ric_twist(ξ₂,ξ₂) = {R_33_twist}")

# Base-base block  
R_00 = simplify(Ric[0,0])
R_11 = simplify(Ric[1,1])
R_01 = simplify(Ric[0,1])

R_00_ot = R_00.subs(ot_sub)
R_11_ot = R_11.subs(ot_sub)
R_00_twist = simplify(R_00 - R_00_ot)
R_11_twist = simplify(R_11 - R_11_ot)

print("\n=== BASE TWIST CONTRIBUTIONS ===")
print(f"Ric_twist(r,r) = {R_00_twist}")
print(f"Ric_twist(z,z) = {R_11_twist}")

# Define the twist scalar: f = e^{-2λ} P_r (since F₁ = P_r dr∧dz, *F₁ = e^{-2λ}P_r)
Pr = P.diff(r)
f1 = exp(-2*lam) * Pr  # twist scalar for direction 1
f1_sq = f1**2

# Express Q = (1/2)G₁₁ f₁² = (1/2)e^{σ+α}(e^{-2λ}P_r)²
Q_expr = Rational(1,2) * exp(sig+alp) * exp(-4*lam) * Pr**2

# Charge q₁ = ρ G₁₁ f₁ = e^σ · e^{σ+α} · e^{-2λ}P_r = e^{2σ+α-2λ}P_r
q1_expr = exp(2*sig+alp-2*lam) * Pr

print(f"\n=== INVARIANTS ===")
print(f"f₁ = e^(-2λ) P_r")
print(f"Q = {Q_expr}")
print(f"q₁ = {q1_expr}")

# Check: does orbit twist Ricci = (1/2) q₁²/ρ² predicted? Or something else?
# predicted: Ric^twist_{11} = (G11)^2 f1^2 = e^{2(σ+α)} e^{-4λ} P_r²
pred_orbit_twist_11 = exp(2*(sig+alp)) * exp(-4*lam) * Pr**2

# Check 
ratio_11 = simplify(R_22_twist / pred_orbit_twist_11)
print(f"\nRic_twist(ξ₁,ξ₁) / (G11² f₁²) = {ratio_11}")

# For 33 component: predicted = G11*G22*f1² · δ_{if not diagonal}
# Since f₂=0, G11*G22*f1*f2 = 0 for the 33 component
# But there IS a trace contribution: -(1/2)G_{22}·2Q term... 
# Actually, the standard formula says Ric^twist_{33} should be 0 when f₂=0
# because the twist only acts in direction 1

check_33_zero = simplify(R_33_twist)
print(f"Ric_twist(ξ₂,ξ₂) [should be 0 for f₂=0] = {check_33_zero}")

# Base twist: predicted +Q γ_{ij} or -Q γ_{ij}?  
# Check the sign of the rr component
base_ratio_rr = simplify(R_00_twist / (exp(2*lam) * Q_expr))
print(f"\nRic_twist(r,r) / (e^(2λ) Q) = {base_ratio_rr}")

base_ratio_zz = simplify(R_11_twist / (exp(2*lam) * Q_expr)) 
print(f"Ric_twist(z,z) / (e^(2λ) Q) = {base_ratio_zz}")

# The mixed Ricci as Maxwell law
# Ric(r,ξ₁) should be proportional to ∂_z(q₁) or similar
print(f"\nRic(r,ξ₁) = {R_02}")

# For constant charge on round cusp (σ=2r, λ=r, α=0, P=-q₁e^{-2r}/2):
# Check if mixed Ricci vanishes
round_cusp_sub = {
    lam: r, 
    sig: 2*r, 
    alp: sp.S(0),
    lam.diff(r): sp.S(1), lam.diff(z): sp.S(0),
    sig.diff(r): sp.S(2), sig.diff(z): sp.S(0),
    alp.diff(r): sp.S(0), alp.diff(z): sp.S(0),
}
# Add second derivatives
for fn, val_r, val_z, val_rr, val_rz, val_zz in [
    (lam, 1, 0, 0, 0, 0), (sig, 2, 0, 0, 0, 0), (alp, 0, 0, 0, 0, 0)]:
    pass  # handled by explicit substitution below

# Use symbols for derivatives for cleaner substitution
lr, lz, sr, sz, ar, az = symbols('lr lz sr sz ar az')
lrr, lrz, lzz = symbols('lrr lrz lzz')
srr, srz, szz = symbols('srr srz szz')
arr, arz, azz = symbols('arr arz azz')
Prv, Pzv = symbols('Pr Pz')
Prrv, Przv, Pzzv = symbols('Prr Prz Pzz')

# Create a manageable substitution: replace function derivatives with symbols
deriv_sub = {
    lam.diff(r): lr, lam.diff(z): lz,
    sig.diff(r): sr, sig.diff(z): sz,
    alp.diff(r): ar, alp.diff(z): az,
    P.diff(r): Prv, P.diff(z): Pzv,
    lam.diff(r,r): lrr, lam.diff(r,z): lrz, lam.diff(z,z): lzz,
    sig.diff(r,r): srr, sig.diff(r,z): srz, sig.diff(z,z): szz,
    alp.diff(r,r): arr, alp.diff(r,z): arz, alp.diff(z,z): azz,
    P.diff(r,r): Prrv, P.diff(r,z): Przv, P.diff(z,z): Pzzv,
}

# Substitute and simplify key quantities
R_02_s = R_02.subs(deriv_sub)
R_22_twist_s = R_22_twist.subs(deriv_sub)
R_00_twist_s = R_00_twist.subs(deriv_sub)
R_11_twist_s = R_11_twist.subs(deriv_sub)

print(f"\n=== SIMPLIFIED FORMULAS ===")
print(f"Ric(r,ξ₁) = {simplify(R_02_s)}")
print(f"Orbit twist 22 = {simplify(R_22_twist_s)}")
print(f"Base twist 00 = {simplify(R_00_twist_s)}")
print(f"Base twist 11 = {simplify(R_11_twist_s)}")

# Save key results
out = {
    'mixed_ricci_r_xi1': str(simplify(R_02_s)),
    'orbit_twist_22': str(simplify(R_22_twist_s)),
    'orbit_twist_33': str(check_33_zero),
    'base_twist_00': str(simplify(R_00_twist_s)),
    'base_twist_11': str(simplify(R_11_twist_s)),
    'ratio_orbit_to_G11sq_f1sq': str(ratio_11),
    'base_ratio_rr': str(base_ratio_rr) if base_ratio_rr is not sp.nan else 'N/A',
}
out_path = Path('workspace/data/step89_symbolic_twist_ricci.json')
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w') as fp:
    json.dump(out, fp, indent=2)
print(f"\nwrote {out_path}")

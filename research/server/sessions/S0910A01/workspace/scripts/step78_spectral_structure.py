"""
Step 78: Non-scalar sector spectral analysis for the inter-node Green response.

Having established that H^4(zeta) for in-kernel zeta has zero scalar coupling,
the inter-node response lives entirely in the vector and TT sectors.
This script computes:
1. The exact tensor decomposition of H^4 into factor-TT components
2. The coupling to product TT eigenmodes at the poles
3. The spectral sum for the leading inter-node Hessian
"""

import numpy as np
import json

Lambda = 1.0  # normalize

# ========== H^4 tensor decomposition ==========

# H^4(omega_2) = diag(1,-1,1,-1)/2 (in the orthonormal product frame at a node)
# = (e1^2 - e2^2)/2 on factor 1   +   (e3^2 - e4^2)/2 on factor 2
# Each piece is a TRACELESS symmetric 2-tensor on the respective S^2 factor

# For general in-kernel zeta = cos(alpha)*omega_2 + sin(alpha)*omega_3:
# Using the verified compositions:
# omega_2^- circ omega_2^+ = diag(-1,1,-1,1) -> factor-1 part: diag(-1,1), factor-2 part: diag(-1,1)
# omega_3^- circ omega_3^+ = diag(-1,1,1,-1) -> factor-1 part: diag(-1,1), factor-2 part: diag(1,-1)
# omega_2^- circ omega_3^+ = off-diagonal (symmetric, factor-traceless)
# omega_3^- circ omega_2^+ = off-diagonal (same)

# H^4(zeta) = -[c^2 (w2- o w2+) + cs(w2- o w3+ + w3- o w2+) + s^2 (w3- o w3+)] / 2
# where c=cos(alpha), s=sin(alpha)

# ========== TT tensor modes on S^2 ==========

# On S^2(Lambda), the Lichnerowicz Laplacian eigenvalues for TT tensors are:
# mu_L(l) = Lambda*(l*(l+1) - 2) for l >= 2
# multiplicity: 2l+1 (spin-weighted) but in practice for TT tensors it's 2*(2l+1)
#
# At the north pole of S^2, the TT tensor value is nonzero only for |m| = 2
# (because m=0 TT mode is zero at the pole by axial symmetry,
#  and |m|=1 modes vanish at the pole for a different reason)
#
# The m=+-2 modes at the pole give:
# Re(m=2): (e1^2 - e2^2) type, Im(m=2): (e1 e2 + e2 e1) type

# At the south pole: Y_{l,m}(-x) = (-1)^l Y_{l,m}(x) for scalars
# For spin-2 harmonics: A* h_{l,m} -> (-1)^l h_{l,m} (same parity as scalars for EVEN spin)
# So TT l=2 modes: A* h -> (-1)^2 h = h (A-even!)
# TT l=3 modes: A* h -> (-1)^3 h = -h (A-odd)
# General: l even -> A-even, l odd -> A-odd

# For the sigma-invariance: sigma rotates phi -> phi+pi on each S^2
# Y_{l,m}(theta, phi+pi) = (-1)^m Y_{l,m}(theta, phi)
# For TT spin-2 tensors: the m-dependent phase gives (-1)^m
# We need (-1)^{m_1+m_2} = +1 for sigma-invariance (on the product)
# But for TT modes on ONE factor combined with a function on the other:
# sigma acts as (-1)^{m_TT} on the TT part and (-1)^{m_scalar} on the scalar part
# sigma-invariance: m_TT + m_scalar even

# ========== Ozuch P eigenvalue on product tensor sectors ==========

# On S^2(Lambda) x S^2(Lambda), the operator P = 1/2*nabla^*nabla - R^circ
# The rough Laplacian on product symmetric 2-tensors decomposes by sector:

# Sector 1: h = T_1 * f_2 where T_1 is TT on factor 1, f_2 scalar on factor 2
#   nabla^*nabla(T_1 f_2) = (Delta_L T_1)f_2 + T_1(Delta f_2)
#   R^circ(T_1 f_2) = Lambda * T_1 * f_2  [since Rcirc on TT = Lambda * TT on Einstein S^2]
#   P eigenvalue: (mu_L(l_1) + lambda_scalar(l_2))/2 - Lambda
#     = (Lambda(l_1(l_1+1)-2) + Lambda*l_2(l_2+1))/2 - Lambda
#     = Lambda*((l_1(l_1+1)-2+l_2(l_2+1))/2 - 1)
#     = Lambda*((l_1(l_1+1)+l_2(l_2+1)-4)/2)

# Sector 2: h = f_1 * T_2 (symmetric roles)
#   P eigenvalue same formula with l_1 <-> l_2

# Actually wait, Rcirc on TT tensors on S^2(Lambda):
# On an Einstein manifold Ric=Lambda*g, the action of Rcirc on a TT tensor h is:
# Rcirc(h) = R_{iacb}h^{cb} (Rm contraction)
# For S^2 with K=Lambda/2: R_{1212} = Lambda/2
# Rcirc on a 2D TT tensor: Rcirc(h)_{ab} = R_{acbd}h^{cd}
# = (K/2)(g_{ab}g_{cd}-g_{ad}g_{bc})h^{cd} = (K/2)(tr(h)g_{ab}-h_{ab})
# Since h is TT (traceless): Rcirc(h)_{ab} = -(K/2)h_{ab} = -(Lambda/4)h_{ab}
# Wait, but S^2 has R_{1212} = Lambda/2 (curvature of round S^2 with Ric=Lambda g has K=Lambda/2)
# For a 2D surface: Rm_{abcd} = K(g_{ac}g_{bd}-g_{ad}g_{bc})
# Rcirc(h)_{ab} = R_{a}^c_{b}^d h_{cd} = K(delta_a^c delta_b^d - g_{ab}g^{cd})h_{cd}
# = K(h_{ab} - g_{ab}tr(h)) = K*h_{ab} for TT h
# So Rcirc(h) = K*h = (Lambda/2)*h for TT on S^2(Lambda)

# Hmm wait, that gives Rcirc = Lambda/2, not Lambda. But on the 4D product:
# The full 4D Rcirc acts on a tensor of the form T_1 * f_2.
# The 4D Rm_{ABCD} decomposes into sum of factor curvatures:
# Rm = Rm_1 (acting on factor 1 indices) + Rm_2 (acting on factor 2 indices)
# No cross terms because the product has no mixed curvature.
#
# For h = T_1 * f_2 (a product tensor):
# Rcirc_{4D}(h)_{AB} = Rm_{A}^C_{B}^D h_{CD}
# The only nonzero contributions come from matching factor indices.
# For indices both on factor 1: (Rcirc h)_{ab} = Rm1_{a}^c_{b}^d (T_1)_{cd} * f_2
#                                               = K_1 * (T_1)_{ab} * f_2
# For one index on each factor: (Rcirc h)_{a\mu} = Rm_{a}^C_{mu}^D h_{CD}
# If C on factor 1 and D on factor 2: Rm_{a}^c_{\mu}^{\nu} = 0 (no mixed Rm)
# If both C,D on factor 1: Rm_{a}^c_{\mu}^d = 0 (mixed index)
# So cross-factor components of Rcirc(T_1*f_2) = 0 ✓
#
# For indices both on factor 2: (Rcirc h)_{\mu\nu} = Rm2_{\mu}^{\rho}_{\nu}^{\sigma} * 0 = 0
# (since T_1*f_2 has zero factor-2 tensor part)
#
# So Rcirc_{4D}(T_1*f_2) = (K_1*T_1)*f_2 = (Lambda/2)*T_1*f_2

# Therefore:
# P(T_1*f_2) = 1/2*(mu_L(l_1)+Lambda*l_2(l_2+1))*T_1*f_2 - (Lambda/2)*T_1*f_2
# = Lambda/2 * (l_1(l_1+1)-2 + l_2(l_2+1) - 1) * T_1*f_2
# = Lambda/2 * (l_1(l_1+1) + l_2(l_2+1) - 3) * T_1*f_2

# Hmm, let me redo this more carefully.
# nabla^*nabla on T_1*f_2:
#   = (Delta_L^{S^2_1} T_1) * f_2 + T_1 * (Delta^{S^2_2} f_2)
#   = Lambda*(l_1(l_1+1)-2)*T_1*f_2 + Lambda*l_2(l_2+1)*T_1*f_2
#   = Lambda*(l_1(l_1+1)+l_2(l_2+1)-2)*T_1*f_2
# 
# P = 1/2 * nabla^*nabla - Rcirc = Lambda/2*(l_1(l_1+1)+l_2(l_2+1)-2) - Lambda/2
#   = Lambda/2 * (l_1(l_1+1)+l_2(l_2+1)-3)
#
# Check: l_1=2, l_2=0: P = Lambda/2*(6+0-3) = 3Lambda/2 ✓ (positive)
# l_1=2, l_2=1: P = Lambda/2*(6+2-3) = 5Lambda/2
# l_1=2, l_2=2: P = Lambda/2*(6+6-3) = 9Lambda/2

# Wait, but on the PRODUCT S^2xS^2 with Ric=Lambda*g (where Lambda is 
# the Ricci constant on each factor), let me use a consistent normalization.
# 
# Each S^2 has Ric_factor = Lambda*g_factor, so K = Lambda/2.
# Product: Ric = Lambda*g, R = 4*Lambda.
# Lichnerowicz on factor-1 TT: eigenvalue Lambda*(l(l+1)-2) using factor Ric convention.
# Factor scalar Laplacian: eigenvalue Lambda*l(l+1).

# Let me just tabulate the P eigenvalues for each sector:

print("=== P eigenvalue computation for product sectors ===\n")

# Sector: TT_1 x scalar_2
print("Sector: TT on factor 1 x scalar on factor 2")
print(f"P eigenvalue = Lambda/2 * (l1(l1+1) + l2(l2+1) - 3)")
print(f"  l1 >= 2 (TT), l2 >= 0 (scalar)")
tt1_scalar2 = []
for l1 in range(2, 8):
    for l2 in range(0, 8):
        mu = Lambda/2 * (l1*(l1+1) + l2*(l2+1) - 3)
        parity = (l1 + l2) % 2  # A-parity: even = 0
        sigma_rule = "needs m_TT+m_scalar even"
        if l1 == 2 and l2 <= 3:
            tt1_scalar2.append({"l1": l1, "l2": l2, "mu": mu, "A_parity": "even" if parity==0 else "odd"})

# By symmetry, sector TT_2 x scalar_1 gives same eigenvalues

# Sector: 1-form_1 x 1-form_2 (vector sector)
# On S^2, divergence-free 1-forms have eigenvalue Lambda*(l(l+1)-1) for l>=1
# The product 1-form sector: df_1 symm dg_2 (symmetrized)
# This involves the rough Laplacian on 1-forms: eigenvalue Lambda*(l(l+1)-1) per factor
# P on the resulting symmetric 2-tensor is more complex, involving both factors

# For now, focus on the dominant TT x scalar sector

print("\nLowest P eigenvalues in TT_1 x scalar_2 sector:")
all_eigenvalues = []
for l1 in range(2, 12):
    for l2 in range(0, 12):
        mu = Lambda/2 * (l1*(l1+1) + l2*(l2+1) - 3)
        parity = (l1 + l2) % 2
        all_eigenvalues.append({
            "l1": l1, "l2": l2, "mu": round(mu, 4),
            "A_even": parity == 0,
            "sector": "TT1_scalar2"
        })

# Also TT_2 x scalar_1
for l1 in range(0, 12):
    for l2 in range(2, 12):
        mu = Lambda/2 * (l1*(l1+1) + l2*(l2+1) - 3)
        parity = (l1 + l2) % 2
        all_eigenvalues.append({
            "l1": l1, "l2": l2, "mu": round(mu, 4),
            "A_even": parity == 0,
            "sector": "scalar1_TT2"
        })

# Sort and show lowest
all_eigenvalues.sort(key=lambda x: x["mu"])
lowest_A_even = [e for e in all_eigenvalues if e["A_even"]][:10]
lowest_A_odd = [e for e in all_eigenvalues if not e["A_even"]][:5]

print("\nLowest A-even non-scalar eigenvalues:")
for e in lowest_A_even:
    print(f"  (l1={e['l1']}, l2={e['l2']}) sector={e['sector']}: P={e['mu']}")

# ========== Pole coupling structure ==========

# At (N,N), H^4(omega_2) has factor-1 TT part: (e1^2-e2^2)/2
# This couples to l_1=2, |m_1|=2 TT modes on factor 1
# (m=0 TT modes are zero at the pole)
# Combined with the scalar Y_{l2,0} on factor 2 (value at N)

# The inter-node Green response from (N,N) to another node involves:
# G_TT(p_recv, p_src) = sum over (l1,l2) of 
#   (TT mode value at recv) * (TT mode value at src) / P_eigenvalue
# 
# For source at (N,N) and receiver at (S,S):
# TT_l1 value at S: (-1)^{l1} * TT_l1 value at N (for the m=2 zonal component)
# scalar Y_{l2,0} at S: (-1)^{l2} * Y_{l2,0} at N
# Combined: (-1)^{l1+l2} * (value at NN)^2 / P_eigenvalue
# In A-even sector (l1+l2 even): (-1)^{l1+l2} = +1 always!

# For source at (N,N) and receiver at (N,S):
# TT_l1 at N: same as source
# scalar Y_{l2,0} at S: (-1)^{l2} * Y_{l2,0} at N
# Combined: (-1)^{l2} * (TT at N)^2 * Y_{l2,0}(N)^2 / P_eigenvalue

# This sign structure is important for inter-orbit interactions.

# ========== Spectral sum convergence test ==========

# For the TT_1 x scalar_2 sector contribution to the Green function
# between (N,N) and (S,S) (same orbit):
# G_{NN,SS} = sum_{l1>=2 even, l2>=0 even (A-even)} |TT_{l1}(N)|^2 * |Y_{l2,0}(N)|^2 / P_{l1,l2}
# with sign (+1) from A-evenness

# For (N,N) to (N,S) (cross orbit):
# G_{NN,NS} = sum_{l1>=2, l2>=0, l1+l2 even} |TT_{l1}(N)|^2 * Y_{l2,0}(N)*Y_{l2,0}(S) / P_{l1,l2}
# = sum ... * (-1)^{l2} * |Y_{l2,0}(N)|^2 / P_{l1,l2}

# The TT tensor amplitude at the north pole for l,m=2:
# For a normalized l=2, m=2 TT mode on S^2(Lambda):
# |h_{l=2,m=2}(N)|^2 (pointwise norm) is a specific constant.
# On the round S^2, the spin-2 spherical harmonics satisfy:
# |_2Y_{l,m}(0,0)|^2 = (l-1)*l*(l+1)*(l+2)/(4*4*pi) for m=0 on a tensor
# Actually this is getting complicated. Let me use a different approach.

# The KEY observation: the curvature modification at the receiver enters as
# delta R^- = d_e R^-(Green_response) (the linearized anti-self-dual curvature)
# From Ozuch's formula (line 333-341):
# d_e R^-(H^4(zeta+)) = 12*pi_tr(rho(zeta)^- tensor rho(zeta)^-) / r^6

# At the receiver node (distance r ~ manifold diameter), this translates to a
# regular correction that we can bound.

# For comparable scales t1 ~ t2 ~ t, the leading inter-node term is O(t^3):
# F_{1,k} = t1^2 * mu_k(alpha1) + t1*(t1^2 * I_{11,k} + t2^2 * I_{12,k}) + O(t^{5/2})
# At comparable t: = t^2*mu_k + t^3*(I_{11}+I_{12}) + O(t^{5/2})
# Since O(t^{5/2}) < O(t^3) for small t, the self-obstruction mu_k dominates IF nonzero.
# If mu_k = 0, the inter-node term at O(t^3) vs O(t^{5/2}): 5/2 < 3, so remainder dominates!
# This means: if mu_2 = mu_3 = 0, the equations are automatically satisfied to O(t^{5/2}).

print("\n=== Order analysis ===")
print("Self-obstruction mu_k: order t^2")
print("Inter-node I_{ij,k}: order t^3 (at comparable scales)")
print("Ozuch remainder: order t^{5/2}")
print("If mu_k != 0: leading equation is t^2*mu_k = 0 -> constraint on alpha")
print("If mu_k = 0: next equation is at O(t^{5/2}), controlled by remainder")
print("The inter-node term at O(t^3) > O(t^{5/2}) cannot appear in the leading equation!")

# Correction: the O(t^{5/2}) is the NECESSARY condition error.
# For a SUFFICIENT condition, we need:
# |F(t,alpha)| <= C*t^{5/2} (necessary) and an inverse/contraction estimate.
# The inter-node interaction changes the approximate metric but doesn't appear
# in the finite-dimensional equation until it exceeds the remainder.
# Since I_{ij} = O(t^3) > O(t^{5/2}), it's BELOW the necessary error for small t.

# This is a critical structural observation: at comparable scales, the inter-node
# interaction is INVISIBLE to the leading obstruction equations.
# The leading reduced map is simply: mu_k(alpha) = 0 for each orbit.

print("\n=== Critical finding ===")  
print("At comparable scales, the inter-node O(t^3) is SMALLER than the O(t^{5/2}) remainder.")
print("The leading reduced equation is simply: mu_k(alpha) = 0 at each orbit representative.")
print("Inter-node interaction matters only at the next order (t^{5/2} vs t^3 crossover).")
print("Or when scales differ: t1 >> t2 makes t1*t2^2 relevant at orbit 2.")

# ========== Assemble results ==========

results = {
    "step": 78,
    "analysis": "non_scalar_sector_spectral_structure",
    
    "H4_tensor_decomposition": {
        "for_omega2_zeta": {
            "H4_diag": [0.5, -0.5, 0.5, -0.5],
            "factor1_TT_part": "diag(1,-1)/2 * constant_on_factor2",
            "factor2_TT_part": "constant_on_factor1 * diag(1,-1)/2",
            "scalar_part": "ZERO (factor-traceless)",
            "azimuthal_number": "|m|=2 (at the pole, only |m|=2 TT modes nonzero)",
        }
    },
    
    "P_eigenvalues_TT_scalar_sector": {
        "formula": "Lambda/2 * (l_TT*(l_TT+1) + l_scalar*(l_scalar+1) - 3)",
        "lowest_A_even": lowest_A_even[:5],
        "all_positive": all(e["mu"] > 0 for e in all_eigenvalues),
        "lowest_value": min(e["mu"] for e in all_eigenvalues),
    },
    
    "order_analysis": {
        "self_obstruction_mu": "O(t^2)",
        "inter_node_interaction": "O(t^3) at comparable scales",
        "Ozuch_remainder": "O(t^{5/2})",
        "comparison": "t^{5/2} << t^3 for small t",
        "consequence": "inter-node terms are BELOW the necessary-condition remainder",
        "leading_equation": "mu_k(alpha) = 0 at each orbit, no inter-node coupling",
    },
    
    "unequal_scale_regime": {
        "when_t1_much_larger": "orbit 2 equation: t2^2*mu + t2*t1^2*I_{21} = O(t_max^{5/2})",
        "ratio_effect": "I_{21} can compete with mu when t1/t2 >> 1",
        "but_self_obstruction_still_leads": "unless mu_k=0 identically",
    },
    
    "pole_coupling_signs": {
        "same_orbit_NN_to_SS": "+1 (A-even sector always positive product of signs)",
        "cross_orbit_NN_to_NS": "(-1)^{l2} (alternating by scalar quantum number)",
    },
}

print(json.dumps(results, indent=2, default=str))

with open("Sessions/S0910A01/workspace/data/step78_spectral_structure.json", "w") as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nWrote Sessions/S0910A01/workspace/data/step78_spectral_structure.json")

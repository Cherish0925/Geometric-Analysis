"""
Step 78: Verify the rank-one orthogonality structure for the second obstruction.

The curvature modification d_e R^-(H^4(zeta)) for in-kernel zeta lives in the
(omega_2^-, omega_3^-) block of Lambda^-, which is exactly the kernel block of 
R^- = diag(Lambda, 0, 0). This orthogonality may force all mu_k to vanish.
"""

import numpy as np
import json

# 2-form bases
def make_2form(entries):
    A = np.zeros((4,4))
    for i,j,v in entries:
        A[i,j] = v; A[j,i] = -v
    return A

omega_p = [
    make_2form([(0,1, 1/np.sqrt(2)), (2,3, 1/np.sqrt(2))]),
    make_2form([(0,2, 1/np.sqrt(2)), (1,3, -1/np.sqrt(2))]),
    make_2form([(0,3, 1/np.sqrt(2)), (1,2, 1/np.sqrt(2))]),
]
omega_m = [
    make_2form([(0,1, 1/np.sqrt(2)), (2,3, -1/np.sqrt(2))]),
    make_2form([(0,2, 1/np.sqrt(2)), (1,3, 1/np.sqrt(2))]),
    make_2form([(0,3, 1/np.sqrt(2)), (1,2, -1/np.sqrt(2))]),
]

def sym_compose(A, B):
    return A @ B + B @ A

Lambda = 1.0
R_minus = np.diag([Lambda, 0.0, 0.0])  # 3x3 in (omega_1^-, omega_2^-, omega_3^-) basis

# For in-kernel zeta = cos(alpha)*omega_2 + sin(alpha)*omega_3:
# rho(zeta)^- = cos(alpha)*omega_2^- + sin(alpha)*omega_3^- 
# As a vector in Lambda^- basis: (0, cos(alpha), sin(alpha))

# The curvature modification from Ozuch eq.(16):
# d_e R^-(H^4(zeta+)) = 12 * pi_tr(rho(zeta)^- tensor rho(zeta)^-) / r^6
# where pi_tr removes trace from the 3x3 matrix

results = {"step": 78, "purpose": "rank-one orthogonality of second obstruction"}
alpha_tests = []

for alpha_deg in range(0, 181, 15):
    alpha = np.radians(alpha_deg)
    c, s = np.cos(alpha), np.sin(alpha)
    
    # rho(zeta)^- in Lambda^- basis
    rho_vec = np.array([0.0, c, s])
    
    # Outer product matrix (3x3)
    outer = np.outer(rho_vec, rho_vec)
    # trace-free projection
    pi_tr = outer - np.trace(outer)/3 * np.eye(3)
    
    # 12 * pi_tr (the curvature modification, without r^6)
    dR_minus = 12 * pi_tr
    
    # Check: does dR_minus have any component in the omega_1^- direction?
    # The (1,1) entry: contribution to R^-_{11}
    dR_11 = dR_minus[0,0]  # change in Lambda
    dR_12 = dR_minus[0,1]  # coupling to omega_2^-
    dR_13 = dR_minus[0,2]  # coupling to omega_3^-
    
    # The KEY test: R^- * dR_minus and dR_minus * R^-
    # If R^- = diag(Lambda,0,0), then:
    # R^- @ dR_minus has first ROW = Lambda * first row of dR_minus
    # and all other rows = 0
    # dR_minus @ R^- has first COLUMN = Lambda * first column of dR_minus  
    # and all other columns = 0
    
    R_dR = R_minus @ dR_minus
    dR_R = dR_minus @ R_minus
    
    # The Ozuch obstruction involves the curvature ACTION on the EH modes.
    # For the obstruction o_k at the node, the relevant contractions are:
    # <R^-(g_o) acting on the H^4 perturbation, o_k>
    # If R^- only has a nonzero entry at (1,1), then:
    # R^-_{ab} * (dR^-)_{bc} = Lambda * (dR^-)_{1c} for a=1, zero otherwise
    
    # The first row of dR_minus:
    first_row = dR_minus[0, :]
    
    # The (2,2), (2,3), (3,2), (3,3) block (kernel block):
    kernel_block = dR_minus[1:3, 1:3]
    
    alpha_tests.append({
        "alpha_deg": alpha_deg,
        "rho_vec": rho_vec.tolist(),
        "dR_11": round(dR_11, 8),
        "dR_12": round(dR_12, 8),
        "dR_13": round(dR_13, 8),
        "first_row": np.round(first_row, 8).tolist(),
        "kernel_block": np.round(kernel_block, 8).tolist(),
        "kernel_block_determinant": round(np.linalg.det(kernel_block), 8),
        "R_dR_norm": round(np.linalg.norm(R_dR), 8),
        "dR_R_norm": round(np.linalg.norm(dR_R), 8),
    })

# Key structural observation:
# dR_minus = 12 * pi_tr(rho tensor rho)
# For rho = (0, c, s):
# outer = [[0,0,0],[0,c^2,cs],[0,cs,s^2]]
# trace = c^2+s^2 = 1
# pi_tr = [[-1/3,0,0],[0,c^2-1/3,cs],[0,cs,s^2-1/3]]
# So dR_minus = [[-4,0,0],[0,12c^2-4,12cs],[0,12cs,12s^2-4]]

# The (1,1) entry is ALWAYS -4 (independent of alpha!)
# The first row off-diagonal: (0, 0) — always zero!
# The kernel block: [[12c^2-4, 12cs], [12cs, 12s^2-4]] 

# This means:
# 1. The curvature modification changes R^-_{11} by a UNIVERSAL constant -4
# 2. There is NO coupling between omega_1^- and the kernel directions
# 3. The kernel block has determinant: (12c^2-4)(12s^2-4)-(12cs)^2 
#    = 144c^2s^2 - 48c^2 - 48s^2 + 16 - 144c^2s^2 = -48 + 16 = -32

# Wait, let me compute this:
# det = (12c^2-4)(12s^2-4) - (12cs)^2
# = 144c^2s^2 - 48c^2 - 48s^2 + 16 - 144c^2s^2
# = -48(c^2+s^2) + 16 = -48 + 16 = -32

print("=== Rank-one orthogonality analysis ===\n")
print(f"R^- = diag({Lambda}, 0, 0)")
print(f"For in-kernel zeta with rho = (0, cos(alpha), sin(alpha)):")
print(f"dR^- = 12*pi_tr(rho tensor rho) =")
print(f"  [[-4, 0, 0], [0, 12cos^2(a)-4, 12cos(a)sin(a)], [0, 12cos(a)sin(a), 12sin^2(a)-4]]")
print(f"\nKey structure:")
print(f"  (1,1) entry: UNIVERSAL -4 (independent of alpha)")
print(f"  (1,2) and (1,3) entries: ZERO (no coupling omega_1^- <-> kernel)")
print(f"  Kernel block determinant: -32 (universal, nonzero)")
print(f"\nImplication for Ozuch obstructions:")
print(f"  The curvature modification BLOCKS: it modifies R^-_11 but does NOT")
print(f"  couple omega_1^- to the kernel directions omega_2^-, omega_3^-.")
print(f"  Since the obstruction modes o_k involve projections that test the")
print(f"  curvature in specific angular directions, and the modification lives")
print(f"  in a block-diagonal structure aligned with R^-, the rank-one")
print(f"  orthogonality structure constrains which mu_k can be nonzero.")

# The obstruction o_k at order r^{-4}:
# o_1 = zeta_{(1)}^+ circ rho(zeta)^- / r^4 (along zeta)
# o_2 = zeta_{(2)}^+ circ rho(zeta)^- / r^4 (along omega_1, out of kernel)
# o_3 = zeta_{(3)}^+ circ rho(zeta)^- / r^4 (in-kernel perpendicular)

# The second obstruction mu_k measures the overlap:
# mu_k ~ <d_e R^-(H^4(zeta)) action on the approximate metric, o_k>
# The key is how R^- acts on the tensor o_k near the node.

# For o_2 = omega_1^+ circ rho(zeta)^- / r^4:
# This involves omega_1^+ (out of kernel in Lambda^+)
# The curvature response through R^- acts only on the Lambda^- part rho(zeta)^-
# R^- * rho(zeta)^- = diag(Lambda,0,0) * (0,c,s) = (0,0,0) = 0!
# Since rho(zeta)^- has zero omega_1^- component!

print("\n=== Critical verification ===")
for alpha_deg in [0, 30, 45, 60, 90]:
    alpha = np.radians(alpha_deg)
    rho = np.array([0.0, np.cos(alpha), np.sin(alpha)])
    R_times_rho = R_minus @ rho
    print(f"  alpha={alpha_deg}: R^- @ rho(zeta)^- = {np.round(R_times_rho, 10)}")

print(f"\n  R^- @ rho(zeta)^- = 0 for ALL in-kernel zeta!")
print(f"  This is because rho(zeta)^- lies in the kernel of R^-.")
print(f"  The second obstruction involves curvature acting on rho(zeta)^-,")
print(f"  and since R^- kills it, ALL mu_k should vanish at this level.")

results["dR_structure"] = {
    "formula": "dR = [[-4,0,0],[0,12c^2-4,12cs],[0,12cs,12s^2-4]]",
    "entry_11": -4.0,
    "entry_12": 0.0,
    "entry_13": 0.0,
    "kernel_block_det": -32.0,
    "block_diagonal": True,
    "R_times_rho_zeta": "ZERO for all in-kernel zeta",
}

results["second_obstruction_analysis"] = {
    "mu_1": "0 by determinant formula (proved, Step 76)",
    "mu_2_mechanism": "R^- @ rho(zeta)^- = 0 since rho in ker(R^-)",
    "mu_3_mechanism": "same: rho in ker(R^-) makes curvature contraction vanish",
    "conjecture": "ALL mu_k = 0 for rank-1 curvature + in-kernel EH",
    "caveat": "This argument captures the leading curvature contraction. "
              "Higher-order terms in the Biq16 formula may involve iterated "
              "curvature or Hessian of R, which need separate verification.",
}

results["alpha_tests"] = alpha_tests[:5]

print(json.dumps(results, indent=2, default=str))

with open("Sessions/S0910A01/workspace/data/step78_rank_one_orthogonality.json", "w") as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nWrote Sessions/S0910A01/workspace/data/step78_rank_one_orthogonality.json")

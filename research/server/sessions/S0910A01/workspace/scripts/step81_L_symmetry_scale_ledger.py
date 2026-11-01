"""
Step 81: verify the single-factor antipodal orbit-exchange symmetry L for the
A+J symmetric mixed-row product-orbifold desingularization, and keep the
correct scale ledger for the surviving radial equations.

Mathematical purpose:
- L(x,y)=(-x,y) exchanges the two A-orbits of A1 nodes of
  (S^2 x S^2)/<sigma>, where sigma=(r_pi,r_pi).
- L reverses four-dimensional orientation, so it swaps Lambda^+ and Lambda^-.
  For the diagonal mixed chirality assignment, this is exactly compatible:
  L maps positive-chirality diagonal nodes to negative-chirality off-diagonal
  nodes and conversely.
- In a local oriented product frame, a representative derivative of L is
  diag(1,-1,1,1).  It sends omega_2^+ to omega_2^- with + sign, so the radial
  EH mode can be normalized L-even.  Hence the reduced equations satisfy
  F_2(t1,t2)=F_1(t2,t1) after L-transported radial normalization.
- The candidate cubic response must be recorded as
      F_i(t1,t2) = t_i * sum_j B_ij t_j^2 + R_i,
  not sum_j B_ij t_j^3.  L symmetry then constrains B=[[a,b],[b,a]].
"""
import json
import numpy as np

# ---------- linear algebra on a local oriented frame ----------

def form_matrix(pairs):
    M = np.zeros((4, 4), dtype=float)
    for i, j, v in pairs:
        M[i, j] = v
        M[j, i] = -v
    return M

# Standard product-oriented basis (e1,e2 | e3,e4)
omega1p = form_matrix([(0,1,1),(2,3,1)])
omega2p = form_matrix([(0,2,1),(1,3,-1)])
omega3p = form_matrix([(0,3,1),(1,2,1)])
omega1m = form_matrix([(0,1,1),(2,3,-1)])
omega2m = form_matrix([(0,2,1),(1,3,1)])
omega3m = form_matrix([(0,3,1),(1,2,-1)])
SD = [omega1p, omega2p, omega3p]
ASD = [omega1m, omega2m, omega3m]

# In compatible oriented frames at source/target nodes, the first-factor
# antipodal is represented by an orientation-reversing reflection on the first
# two tangent directions and identity on the second factor.
L = np.diag([1., -1., 1., 1.])
J = np.diag([1., -1., 1., -1.])
sigma = -np.eye(4)
# A is not a fixed-node tangent map, but relative to compatible frames it can be
# represented by orientation reversal on both factors.
A_local = np.diag([1., -1., 1., -1.])


def pull(M, T):
    return T.T @ M @ T


def coeff_against_basis(M, basis):
    # The basis forms have equal squared Frobenius norm.  Use Frobenius pairing;
    # only one coefficient should be nonzero in these exact sign checks.
    den = [float(np.sum(B * B)) for B in basis]
    return [float(np.sum(M * B) / d) for B, d in zip(basis, den)]


def classify_image(M, target_basis, target_names):
    coeff = coeff_against_basis(M, target_basis)
    nz = [(target_names[i], coeff[i]) for i in range(3) if abs(coeff[i]) > 1e-12]
    return {"coefficients": coeff, "nonzero_terms": nz}

names = ["omega1", "omega2", "omega3"]
L_SD_to_ASD = {}
L_ASD_to_SD = {}
for idx, M in enumerate(SD):
    L_SD_to_ASD[f"{names[idx]}+"] = classify_image(pull(M, L), ASD, [n+"-" for n in names])
for idx, M in enumerate(ASD):
    L_ASD_to_SD[f"{names[idx]}-"] = classify_image(pull(M, L), SD, [n+"+" for n in names])

# J commutation in the local representative.  Global commutation with A and
# sigma is also direct because all maps are factorwise sign/reflection maps.
commutation = {
    "det_L": float(np.linalg.det(L)),
    "L_squared_is_I": bool(np.allclose(L @ L, np.eye(4))),
    "L_sigma_commute_local": bool(np.allclose(L @ sigma, sigma @ L)),
    "L_J_commute_local": bool(np.allclose(L @ J, J @ L)),
    "L_A_commute_local_representatives": bool(np.allclose(L @ A_local, A_local @ L)),
}

# Curvature block compatibility: R^+=diag(1,0,0) maps to R^-=diag(1,0,0)
# because L sends omega1+ -> -omega1-, omega2+ -> omega2-, omega3+ -> omega3-.
Rplus = np.diag([1., 0., 0.])
# The induced signed basis-change from SD to ASD under L.
S_pm = np.zeros((3,3))
for i, M in enumerate(SD):
    S_pm[:, i] = coeff_against_basis(pull(M, L), ASD)
Rplus_to_minus = S_pm @ Rplus @ S_pm.T

# The radial adapted direction is phi1=omega2.  L sends omega2+ -> +omega2-.
radial_sign = S_pm[1, 1]
transverse_signs = {"omega1": S_pm[0, 0], "omega3": S_pm[2, 2]}

# ---------- node/chirality/orbit bookkeeping ----------
# Represent N=+1, S=-1.  Diagonal chirality assignment epsilon=s1*s2:
# + on (N,N),(S,S), - on (N,S),(S,N).
nodes = [(1,1), (1,-1), (-1,1), (-1,-1)]
def node_name(n):
    return ("N" if n[0] == 1 else "S") + ("N" if n[1] == 1 else "S")
def A_node(n):
    return (-n[0], -n[1])
def L_node(n):
    return (-n[0], n[1])
def J_node(n):
    return n
def chirality(n):
    return n[0] * n[1]
def orbit(n):
    return 1 if chirality(n) == 1 else 2

node_table = []
for n in nodes:
    node_table.append({
        "node": node_name(n),
        "chirality_plus1_diag_minus1_offdiag": chirality(n),
        "A_node": node_name(A_node(n)),
        "L_node": node_name(L_node(n)),
        "J_node": node_name(J_node(n)),
        "A_preserves_chirality": chirality(A_node(n)) == chirality(n),
        "L_reverses_chirality": chirality(L_node(n)) == -chirality(n),
        "orbit": orbit(n),
        "L_orbit": orbit(L_node(n)),
    })

# ---------- reduced equation constraints ----------
# Let candidate effective cubic radial term be F_i = t_i * sum_j B_ij t_j^2.
# L gives F2(t1,t2)=F1(t2,t1) in L-transported radial normalization.
# This forces B22=B11 and B21=B12.
B_constraints = {
    "candidate_form": "F_i(t1,t2)=t_i*(B_i1*t1^2 + B_i2*t2^2) + R_i",
    "not_candidate_form": "sum_j B_ij*t_j^3 (missing receiver factor t_i)",
    "L_relation_normalized": "F_2(t1,t2)=F_1(t2,t1)",
    "B_form_under_L": "[[a,b],[b,a]]",
    "positive_scale_leading_equation": "B*(t1^2,t2^2)^T=0 after dividing by t_i>0",
    "positive_kernel_condition_exchange_symmetric": "a+b=0 with t1^2=t2^2, unless a=b=0 gives a fully zero candidate matrix",
    "if_a_plus_b_nonzero": "no L-symmetric positive kernel at this candidate order",
    "if_a_plus_b_zero": "equal-scale branch survives this order; next radial equation along t1=t2 is decisive",
    "normalization_caveat": "If radial basis at the negative-chirality orbit is not L-transported, the relation includes a fixed sign/norm factor; with omega2+ -> +omega2- the natural tensor normalization has factor +1."
}

# Remainder target needed to make the candidate response a real leading equation.
remainder_target = {
    "current_Ozuch_estimate": "t_i*lambda_i + t_i^2*mu_i = O(t_max^(5/2)); at comparable scales this is larger than degree-3 response",
    "needed_projected_expansion": "After A+J+det lower-order cancellations, derive F_i=t_i*sum_j B_ij*t_j^2 + o(t_i*(t1^2+t2^2)) on the positive scale cone, or a multi-scale analogue with explicit powers/logs.",
    "possible_terms_to_track": [
        "local self-response t_i^3",
        "regular inter-node response t_i*t_j^2",
        "even shape-mode response (g1-g2), contributing effectively to B",
        "even scalar/nonkernel corrections not killed by A or J",
        "Bianchi/DeTurck correction terms",
        "cutoff/matching terms, including possible logarithmic factors"
    ]
}

results = {
    "step": 81,
    "purpose": "verify L orbit-exchange symmetry and correct surviving radial scale ledger",
    "local_linear_model": {
        "L_matrix": L.tolist(),
        "J_matrix": J.tolist(),
        "sigma_matrix": sigma.tolist(),
        "orientation": "det L = -1, hence L swaps Lambda^+ and Lambda^-",
    },
    "commutation": commutation,
    "L_action_SD_to_ASD": L_SD_to_ASD,
    "L_action_ASD_to_SD": L_ASD_to_SD,
    "basis_change_SD_to_ASD_matrix_columns_are_images": S_pm.tolist(),
    "curvature_block_transport": {
        "Rplus_diag_100_to_minus": Rplus_to_minus.tolist(),
        "matches_Rminus_diag_100": bool(np.allclose(Rplus_to_minus, np.diag([1.,0.,0.])))
    },
    "radial_mode_transport": {
        "omega2_plus_to_omega2_minus_sign": float(radial_sign),
        "transverse_signs_plus_to_minus": transverse_signs,
        "radial_projection_relation_sign_with_L_transported_basis": float(radial_sign)
    },
    "node_chirality_table": node_table,
    "B_constraints": B_constraints,
    "remainder_target": remainder_target,
    "interpretation": "L is compatible with the diagonal mixed chirality assignment and relates the two A-orbit radial equations, reducing the candidate effective matrix to self/cross coefficients a,b. It does not by itself impose t1=t2 or force a+b=0."
}

print(json.dumps(results, indent=2))
outpath = "Sessions/S0910A01/workspace/data/step81_L_symmetry_scale_ledger.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nWrote {outpath}")

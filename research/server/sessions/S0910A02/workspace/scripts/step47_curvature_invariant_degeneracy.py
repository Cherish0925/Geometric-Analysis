"""
Step 47: Curvature-block invariance at an orbifold singularity.

If a 4D Einstein orbifold has local group Gamma acting on one chiral
2-form block by a finite subgroup G < SO(3), then the traceless Weyl block
W in Sym^2_0(R^3) must be G-invariant.  This is the SAME spin-2
representation tabulated in Step 46 for the l=2 modes.  The calculation below
computes invariant dimensions from generator matrices and records the resulting
finite-dimensional determinant equations.

This is a review/diagnostic script, not a proof of the analytic bridge.
"""

import json
import math
import numpy as np

OUT = "Sessions/S0910A02/workspace/data/step47_curvature_invariant_degeneracy.json"


def rot_axis(axis, theta):
    axis = np.array(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    x, y, z = axis
    K = np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]], dtype=float)
    I = np.eye(3)
    return I + math.sin(theta) * K + (1 - math.cos(theta)) * (K @ K)


def invariant_dim(gens, tol=1e-9):
    # Basis for traceless symmetric matrices.
    basis = [
        np.array([[1, 0, 0], [0, 0, 0], [0, 0, -1]], dtype=float),
        np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]], dtype=float),
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=float),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=float),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=float),
    ]
    if not gens:
        return 5, []
    rows = []
    for R in gens:
        for B in basis:
            C = R @ B @ R.T - B
            rows.append(C.reshape(-1))
    # Constraint matrix columns are basis coefficients: for each matrix entry, each basis image.
    rows = []
    for R in gens:
        # For each generator produce 9 equations in the 5 coefficients.
        cols = []
        for B in basis:
            cols.append((R @ B @ R.T - B).reshape(-1))
        A = np.stack(cols, axis=1)  # 9 x 5
        rows.append(A)
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    rank = int(np.sum(s > tol))
    return 5 - rank, [float(x) for x in s]


def cyclic_case(binary_p):
    image_order = binary_p // math.gcd(binary_p, 2)
    gens = [] if image_order == 1 else [rot_axis([0, 0, 1], 2 * math.pi / image_order)]
    dim, sv = invariant_dim(gens)
    return {
        "ADE": f"A_{binary_p-1}",
        "binary_group": f"Z_{binary_p}",
        "SO3_image_order": image_order,
        "spin2_invariant_dim_numeric": dim,
        "expected_form": (
            "arbitrary traceless symmetric 3x3 W" if image_order == 1 else
            "W=[[x,y,0],[y,z,0],[0,0,-x-z]] (Z2 case)" if image_order == 2 else
            "W=diag(-u/2,-u/2,u) in an adapted axis frame"
        ),
        "det_R_equation_for_a=Lambda_over_3": (
            "det(aI+W)=0, one cubic equation in five variables" if image_order == 1 else
            "det([[a+x,y,0],[y,a+z,0],[0,0,a-x-z]])=0" if image_order == 2 else
            "(a-u/2)^2*(a+u)=0"
        ),
        "singularity_review": (
            "A1 is the only cyclic type with no isotropy restriction on this block" if image_order == 1 else
            "A3 has a 3-dimensional restricted block" if image_order == 2 else
            "one scalar invariant u controls the traceless Weyl block"
        ),
    }


def dihedral_case(ade_D):
    # ADE D_k corresponds to binary dihedral D*_{k-2}; SO(3) image is ordinary D_{k-2}.
    n = ade_D - 2
    gens = [rot_axis([0, 0, 1], 2 * math.pi / n), rot_axis([1, 0, 0], math.pi)]
    dim, sv = invariant_dim(gens)
    return {
        "ADE": f"D_{ade_D}",
        "SO3_image": f"D_{n}",
        "spin2_invariant_dim_numeric": dim,
        "expected_form": (
            "W=diag(x,y,-x-y) in the three half-turn axes" if n == 2 else
            "W=diag(-u/2,-u/2,u) in the dihedral axis frame"
        ),
        "det_R_equation_for_a=Lambda_over_3": (
            "(a+x)*(a+y)*(a-x-y)=0" if n == 2 else
            "(a-u/2)^2*(a+u)=0"
        ),
    }


def exceptional_case(name, gens):
    dim, sv = invariant_dim(gens)
    return {
        "type": name,
        "spin2_invariant_dim_numeric": dim,
        "singular_values_of_constraint_matrix": [round(x, 10) for x in sv],
        "curvature_consequence": "W=0 on the chiral block where the isotropy acts by the nontrivial SO(3) group",
        "det_R_for_positive_Lambda": "det((Lambda/3)I)=Lambda^3/27 > 0; no kernel in that block",
    }


phi = (1 + 5 ** 0.5) / 2
# Generators for tetrahedral and octahedral rotation groups.
T_gens = [rot_axis([1, 0, 0], math.pi), rot_axis([1, 1, 1], 2 * math.pi / 3)]
O_gens = [rot_axis([0, 0, 1], math.pi / 2), rot_axis([1, 1, 1], 2 * math.pi / 3)]
# Icosahedral: 5-fold around a vertex and 3-fold around an adjacent face center.
v1 = np.array([0, 1, phi], dtype=float)
v2 = np.array([-1, phi, 0], dtype=float)
v3 = np.array([1, phi, 0], dtype=float)
I_gens = [rot_axis(v1, 2 * math.pi / 5), rot_axis(v1 + v2 + v3, 2 * math.pi / 3)]

results = {
    "purpose": "Review Step 46 by adding the missing curvature-block invariance calculation.",
    "main_principle": "At an orbifold fixed point, the Einstein curvature blocks R^± commute with the local isotropy action. Therefore the traceless Weyl block W^± lies in Sym^2_0(R^3)^G for the chiral block on which Gamma acts through G=Gamma/{±1}<SO(3). This is the same spin-2 invariant representation as the l=2 harmonic computation.",
    "cyclic_selected": [cyclic_case(p) for p in [2, 3, 4, 5, 6, 8]],
    "dihedral_selected": [dihedral_case(k) for k in [4, 5, 6, 8]],
    "exceptional": [
        exceptional_case("E6 / tetrahedral T", T_gens),
        exceptional_case("E7 / octahedral O", O_gens),
        exceptional_case("E8 / icosahedral I", I_gens),
    ],
    "kähler_orientation_caution": {
        "standard_complex_Kleinian_convention": "For a local complex/ADE quotient Gamma<SU(2) preserving the hyperkähler triple, Gamma acts trivially on the Kähler self-dual block and by the adjoint action on the opposite block. If a note uses the opposite SU(2)_L/R naming, plus/minus labels must be swapped.",
        "positive_KE_pinned_block": "In complex orientation, R_+ = diag(Lambda,0,0). This nonzero traceless Weyl block can occur only in the chiral block on which the isotropy action is trivial or at least has the needed invariant direction.",
        "E_type_review": "For E6/E7/E8, the nontrivial isotropy block has W=0 and R=(Lambda/3)I, hence is invertible for Lambda>0. Thus E-type is not an extra double-degeneracy loophole for reversed bubbles in a positive KE limit; depending on convention it either obstructs the opposite block or would make the claimed KE orientation impossible.",
    },
    "review_conclusion": [
        "The word 'generic' should be removed from Step 46. The sequence supplies a fixed orbifold limit; the honest statement is a finite set of degeneracy alternatives at its singular points and gluing directions.",
        "For A1, Gamma/{±1} is trivial and both chiral blocks are unconstrained by isotropy; this is the main double-degeneracy locus exemplified by the bi-Kähler product quotient.",
        "For A_k (k>=2) and D_k the degeneracy condition lives in a 1-, 2-, or 3-dimensional invariant curvature space and becomes explicit scalar equations in adapted coordinates.",
        "For E-types the nontrivial block is scalar positive and cannot have a kernel for Lambda>0. Step 46's 'E-type compatible bubble locus' is therefore at least misframed and is not a KE loophole of the same kind as A1 double degeneracy."
    ]
}

with open(OUT, "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps({
    "output": OUT,
    "exceptional_dims": [(e["type"], e["spin2_invariant_dim_numeric"]) for e in results["exceptional"]],
    "A1_dim": results["cyclic_selected"][0]["spin2_invariant_dim_numeric"],
    "A3_dim": results["cyclic_selected"][2]["spin2_invariant_dim_numeric"],
    "review": results["review_conclusion"][-1]
}, indent=2))

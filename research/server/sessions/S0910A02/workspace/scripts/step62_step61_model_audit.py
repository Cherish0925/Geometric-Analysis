#!/usr/bin/env python3
"""Step 62 audit of the Step-61 toric-cone drift model.

This is a finite algebra/check ledger for Agent4.  It checks three
load-bearing points from the Strategist correction:

1. The Step-61 T^2-invariant quadratic warped mode is not an Einstein-compatible
   2-jet: its linear Ricci tensor is not a scalar multiple of the Euclidean
   metric, so using it to make R_pm degenerate imports O(1) Ricci defect.
2. The same ansatz is not smooth along the toric axes unless v vanishes on both
   axes; the only T^2-invariant degree-2 harmonic is r1^2-r2^2 and it does not
   vanish on either axis.
3. In contrast, the full normal-coordinate algebraic curvature/2-jet space has
   a 10-dimensional Ricci-flat tangent space, i.e. the two Weyl blocks can be
   varied freely while preserving Einstein Ricci to first order.

The script is not a proof of the analytic flux theorem; it is a reproducible
local algebra audit.
"""

from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

OUT = Path("Sessions/S0910A02/workspace/data/step62_step61_model_audit.json")
OUT.parent.mkdir(parents=True, exist_ok=True)


def audit_step61_warped_ricci():
    A, eps, Lam = sp.symbols("A eps Lam", nonzero=True)
    r1 = r2 = sp.Integer(1)
    # From step61_weyl_eigenvalues.json, in orthonormal frame, linear in eps.
    Ric = sp.Matrix([
        [-4*A, 2*A*(r1**2+r2**2)/(r1*r2), 0, 0],
        [ 2*A*(r1**2+r2**2)/(r1*r2), -4*A, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]) * eps
    Ric_at = sp.simplify(Ric)
    eig = Ric_at.eigenvals()
    scal = sp.trace(Ric_at)
    # Step-61 reachability made the negative Weyl eigenvalue -16 eps A/3 cancel Lambda/3.
    reach_sub = {eps*A: Lam/16}
    # Compute eigenvalues after eps A=Lambda/16.  Since A,eps occur only as product,
    # substitute eps*A by q via a placeholder q.
    q = sp.symbols("q")
    Ric_q = Ric_at.subs(eps*A, q)
    Ric_reach = sp.simplify(Ric_q.subs(q, Lam/16))
    # Compare with Lambda times identity and also with any scalar multiple: scalar part is trace/4.
    defect_from_Lambda_Id = sp.simplify(Ric_reach - Lam*sp.eye(4))
    scalar_part = sp.simplify(sp.trace(Ric_reach)/4)
    traceless_part = sp.simplify(Ric_reach - scalar_part*sp.eye(4))
    return {
        "Ric_ON_linear_at_r1_eq_r2_eq_1": [[str(Ric_at[i,j]) for j in range(4)] for i in range(4)],
        "Ric_eigenvalues_linear": [{"eigenvalue": str(k), "multiplicity": int(v)} for k,v in eig.items()],
        "scalar_linear": str(scal),
        "reachability_choice_epsA": "Lambda/16",
        "Ric_at_reachability_choice": [[str(Ric_reach[i,j]) for j in range(4)] for i in range(4)],
        "scalar_part_at_reach": str(scalar_part),
        "traceless_Ric_at_reach": [[str(traceless_part[i,j]) for j in range(4)] for i in range(4)],
        "defect_from_Lambda_Id_at_reach": [[str(defect_from_Lambda_Id[i,j]) for j in range(4)] for i in range(4)],
        "verdict": "The mode is not Ricci-neutral or Einstein-compatible. At the Weyl degeneracy value eps*A=Lambda/16 it has O(Lambda) trace/traceless Ricci defect, so Step61 reachability is not reachability under ||Ric-Lambda g|| -> 0."
    }


def audit_axis_smoothness():
    a, b = sp.symbols("a b")
    # T^2-invariant homogeneous quadratics are a r1^2 + b r2^2.
    # D = d_r1^2 + d_r2^2 + (1/r1)d_r1 + (1/r2)d_r2.
    D = 4*a + 4*b
    harmonic_condition = sp.Eq(a+b, 0)
    # Vanish on r1=0 forces b=0; vanish on r2=0 forces a=0.
    solutions_raw = sp.solve([a+b, a, b], [a,b], dict=True)
    solutions = [{str(k): str(v) for k, v in sol.items()} for sol in solutions_raw]
    return {
        "T2_invariant_quadratic": "a*r1^2 + b*r2^2",
        "D_of_quadratic": str(D),
        "harmonic_condition": "a+b=0, hence span{r1^2-r2^2}",
        "axis_smoothness_for_metric_dr1^2+r1^2e^{2v}dphi^2+dr2^2+r2^2e^{-2v}dpsi^2": {
            "phi_axis_r1=0": "v(0,r2)=0 for all r2, otherwise the phi cone angle is multiplied by e^{v(0,r2)}",
            "psi_axis_r2=0": "v(r1,0)=0 for all r1, otherwise the psi cone angle is multiplied by e^{-v(r1,0)}"
        },
        "only_harmonic_satisfying_both_axis_conditions": solutions,
        "step61_mode_axis_values": {
            "v=r1^2-r2^2_on_r1=0": "-r2^2",
            "v=r1^2-r2^2_on_r2=0": "r1^2"
        },
        "verdict": "No nonzero T^2-invariant homogeneous degree-2 harmonic can be both harmonic and smooth-axis compatible inside this toric ansatz. Angular cutoffs would add second angular derivatives to Dv."
    }


# Algebraic curvature tensor audit.
# Use a symmetric curvature operator on Lambda^2 with the first Bianchi identity.
pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
pair_to_idx = {p:i for i,p in enumerate(pairs)}

def pair_sign(i,j):
    if i == j:
        return None, 0
    if i < j:
        return pair_to_idx[(i,j)], 1
    return pair_to_idx[(j,i)], -1


def curvature_component(M, i,j,k,l):
    p, s1 = pair_sign(i,j)
    q, s2 = pair_sign(k,l)
    if p is None or q is None:
        return 0
    return s1*s2*M[p,q]


def audit_curvature_space():
    # Variables for symmetric 6x6 curvature operator.
    vars_ = []
    M = [[None]*6 for _ in range(6)]
    for i in range(6):
        for j in range(i,6):
            x = sp.symbols(f"m{i}{j}")
            vars_.append(x)
            M[i][j] = M[j][i] = x
    M = sp.Matrix(M)

    # First Bianchi in 4D: R0123 + R0231 + R0312 = 0.
    bianchi = sp.expand(curvature_component(M,0,1,2,3) + curvature_component(M,0,2,3,1) + curvature_component(M,0,3,1,2))

    # Ricci_{jl} = sum_i R_{i j i l}; sign convention immaterial for rank/kernel dimensions.
    Ric = sp.Matrix(4,4, lambda j,l: sp.expand(sum(curvature_component(M,i,j,i,l) for i in range(4))))
    scalar = sp.expand(sum(Ric[i,i] for i in range(4)))

    # Linear map from 21 curvature-operator variables to (Bianchi, Ricci components).
    ric_comps = []
    for i in range(4):
        for j in range(i,4):
            ric_comps.append(Ric[i,j])
    equations_ricci_zero = [bianchi] + ric_comps
    mat_ric0, _ = sp.linear_eq_to_matrix(equations_ricci_zero, vars_)
    rank_bianchi_ric0 = mat_ric0.rank()

    mat_bianchi, _ = sp.linear_eq_to_matrix([bianchi], vars_)
    rank_bianchi = mat_bianchi.rank()
    algebraic_dim = len(vars_) - rank_bianchi
    ricci_zero_dim = len(vars_) - rank_bianchi_ric0

    # Map to Ricci components after imposing Bianchi: rank Ricci should be 10.
    mat_b_ric, _ = sp.linear_eq_to_matrix([bianchi] + ric_comps, vars_)
    ricci_rank_on_algebraic = rank_bianchi_ric0 - rank_bianchi

    # Einstein Ric=Lambda*g is affine nonempty: constant sectional curvature K=Lambda/3 works.
    # In 4D, curvature operator K*Id has Ric = -? 3K depending sign convention. Record sign not used.
    K = sp.symbols("K")
    M_const = sp.diag(*([K]*6))
    Ric_const = sp.Matrix(4,4, lambda j,l: sp.expand(sum(curvature_component(M_const,i,j,i,l) for i in range(4))))

    return {
        "curvature_operator_variables_symmetric_6x6": len(vars_),
        "first_bianchi_equation": str(bianchi),
        "algebraic_curvature_dimension": int(algebraic_dim),
        "ricci_map_rank_on_algebraic_curvatures": int(ricci_rank_on_algebraic),
        "ricci_zero_kernel_dimension": int(ricci_zero_dim),
        "expected_weyl_dimension": 10,
        "constant_curvature_Ricci_check_sign_convention": [[str(Ric_const[i,j]) for j in range(4)] for i in range(4)],
        "verdict": "Algebraic 4D curvature decomposes as Ricci data (rank 10) plus a 10-dimensional Ricci-flat/Weyl kernel. Hence Einstein-compatible normal-coordinate 2-jets form an affine space, and its tangent changes (W+,W-) freely while preserving Ricci to first order."
    }


def main():
    data = {
        "status": "ok",
        "audit_target": "Step61 toric-cone T^2-invariant warped drift model and its replacement by full Einstein-compatible 2-jets",
        "step61_warped_ricci_audit": audit_step61_warped_ricci(),
        "axis_smoothness_audit": audit_axis_smoothness(),
        "full_quadratic_jet_curvature_space_audit": audit_curvature_space(),
        "research_conclusion": [
            "Step61's specific toric warped ansatz must not be used as a near-pinched realizability construction: its Weyl reachability imports O(1) Ricci defect and violates toric-axis smoothness.",
            "The failure is not a failure of the exponential drift mechanism. In full normal-coordinate Einstein-compatible 2-jets, Ricci is fixed while the 10 Weyl degrees of freedom vary freely; these jets are smooth and Z2-even for A1.",
            "The rate-limited flux theorem should therefore be stated as a sharp conditional obstruction with an exponential escape channel, plus a finite Gamma-invariant reachability refinement for non-A1 ADE types."
        ]
    }
    OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps({
        "status": "ok",
        "output": str(OUT),
        "ricci_verdict": data["step61_warped_ricci_audit"]["verdict"],
        "axis_verdict": data["axis_smoothness_audit"]["verdict"],
        "weyl_kernel_dimension": data["full_quadratic_jet_curvature_space_audit"]["ricci_zero_kernel_dimension"]
    }, indent=2))

if __name__ == "__main__":
    main()

"""
Step 29 execution checks for the positive-collapse Bochner route.

This script does two independent things:

1. Dimension-four nilpotent allocation.  If a four-dimensional collapse has
   nilpotent fibre dimension <=3, every nilpotent Lie algebra is either abelian
   or H_3; hence every bracket lands in the center.  The Step-28 Bochner center
   bound therefore controls all fibre brackets in the crux dimension without a
   quotient induction or a horizontal-twist pointwise estimate.

2. A local Kaluza--Klein jet/spike test showing why a pointwise horizontal
   twist bound should not be expected from C^0 Ricci pinching alone.  In a
   circle bundle over a 3-base, a large connection curvature F at a point can be
   canceled in the total Ricci tensor by the Hessian of a small dilaton u=log f
   and by the base Ricci 2-jet.  The computation constructs an explicit local
   4D metric jet
       g = e^{2 psi}(dx^2+dy^2+dz^2) + e^{2u}(dtheta+A)^2
   with A=(-B y/2)dx+(B x/2)dy, u=(H/2)(x^2+y^2+z^2),
   psi=(pa/2)(x^2+y^2)+(pc/2)z^2, and solves the exact symbolic Ricci equations
   at the origin for Ric_g = Lambda g while B^2 is arbitrarily large.

The second check is a point-jet/local-formal obstruction to any attempted
pointwise |F| bound from Ricci pinching.  It is not a global closed metric and
not a Yau-26 counterexample.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


def dim4_nilpotent_allocation():
    # Classification-level algebra in dimensions <=3.
    # dim 1,2 nilpotent Lie algebras over R are abelian.  In dim 3, either
    # abelian or Heisenberg H3 with [e1,e2]=b e3 and e3 central.
    b, K = sp.symbols('b K', positive=True)
    # For H3 center z=e3, J_z on span(e1,e2) has matrix [[0,b],[-b,0]].
    J = sp.Matrix([[0, b], [-b, 0]])
    J_hs_sq = sp.simplify(sum(J[i, j] ** 2 for i in range(2) for j in range(2)))
    # General center-gradient formula from TTCS: |nabla^F Z|^2=(|Z|^2/4)||J_z||_HS^2.
    fiber_grad_coeff = sp.simplify(J_hs_sq / 4)
    # In the single-bracket convention this equals b^2/2.
    center_bound_implies = sp.solve_univariate_inequality(b**2 <= 2*K, b)
    return {
        "dimension_four_collapse_fibre_dimension": "<= 3",
        "nilpotent_lie_algebras_dim_le_3": [
            "dim 1: abelian",
            "dim 2: abelian",
            "dim 3: abelian or Heisenberg H3 with [e1,e2]=b e3, e3 central",
        ],
        "derived_algebra_subset_center": True,
        "consequence": "In dimension four, Step-28's center Bochner bound controls every nilpotent fibre bracket; no central-quotient induction or quotient pointwise Ricci bound is needed for the fibre-bracket part.",
        "H3_Jz_matrix": str(J),
        "Jz_HS_squared": str(J_hs_sq),
        "fiber_gradient_coefficient_for_unit_center": str(fiber_grad_coeff),
        "bochner_bound_symbolic": "if <b^2>_{|Z|^2} <= 2K then all H3 brackets are L2-bounded by 2K",
        "positive_K_solution_shape": str(center_bound_implies),
        "limitation": "This is weighted L2 control for exact/almost central Killing fields; it is not pointwise control and it does not by itself construct an Einstein metric."
    }


def compute_twist_jet_expressions():
    # Coordinates and parameters.
    x, y, z, th = sp.symbols('x y z th')
    pa, pc, H, B, Lam = sp.symbols('pa pc H B Lam')
    coords = (x, y, z, th)
    n = 4

    psi = sp.Rational(1, 2) * pa * (x**2 + y**2) + sp.Rational(1, 2) * pc * z**2
    u = sp.Rational(1, 2) * H * (x**2 + y**2 + z**2)
    s = sp.exp(2 * psi)
    f2 = sp.exp(2 * u)
    A = [-B*y/2, B*x/2, sp.Integer(0)]

    g = sp.zeros(4)
    for i in range(3):
        g[i, i] = s
    for i in range(3):
        for j in range(3):
            g[i, j] += f2 * A[i] * A[j]
        g[i, 3] = f2 * A[i]
        g[3, i] = f2 * A[i]
    g[3, 3] = f2

    ginv = sp.simplify(g.inv())

    # Christoffel symbols.
    Gamma = [[ [sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for bidx in range(n):
            for cidx in range(n):
                expr = sp.Integer(0)
                for d in range(n):
                    expr += ginv[a, d] * (sp.diff(g[d, cidx], coords[bidx]) + sp.diff(g[d, bidx], coords[cidx]) - sp.diff(g[bidx, cidx], coords[d]))
                Gamma[a][bidx][cidx] = sp.simplify(expr / 2)

    # Ricci_{bd} = R^a_{bad} = d_a Gamma^a_{bd} - d_d Gamma^a_{ba} + Gamma^a_{ae}Gamma^e_{bd} - Gamma^a_{de}Gamma^e_{ba}
    Ric = sp.zeros(n)
    for bidx in range(n):
        for didx in range(n):
            expr = sp.Integer(0)
            for a in range(n):
                expr += sp.diff(Gamma[a][bidx][didx], coords[a]) - sp.diff(Gamma[a][bidx][a], coords[didx])
                for e in range(n):
                    expr += Gamma[a][a][e] * Gamma[e][bidx][didx] - Gamma[a][didx][e] * Gamma[e][bidx][a]
            Ric[bidx, didx] = sp.simplify(expr)

    origin = {x:0, y:0, z:0, th:0}
    Ric0 = sp.Matrix([[sp.simplify(Ric[i, j].subs(origin)) for j in range(n)] for i in range(n)])
    g0 = sp.Matrix([[sp.simplify(g[i, j].subs(origin)) for j in range(n)] for i in range(n)])

    # Due to xy symmetry, solve Ric_xx=Ric_yy=Lam, Ric_zz=Lam, Ric_tt=Lam.
    # Use S=B^2 to display the arbitrary-twist family.
    S = sp.symbols('S')
    Ric0S = Ric0.subs(B**2, S)
    equations = [sp.Eq(Ric0S[0,0], Lam), sp.Eq(Ric0S[2,2], Lam), sp.Eq(Ric0S[3,3], Lam)]
    sol = sp.solve(equations, (pa, pc, H), dict=True, simplify=True)
    # There should be a one-parameter family in S and Lam.
    solved = sol[0] if sol else {}
    Ric_solved = sp.simplify(Ric0S.subs(solved)) if solved else Ric0S

    # Build sample values with arbitrarily large S: choose Lambda=1, S=2N+2 so H=N/3? Actually the solve returns H=S/2-Lam.
    # The vertical formula from the direct Ricci computation is Ric_tt=S/2-3H, so H=S/6-Lam/3.
    samples = []
    for Nval in [10, 100, 1000, 10_000]:
        # Choose S=2(N+Lam) with Lam=1.  Then H should be N/3 and u C1-small on radius r=N^-2.
        subsN = {Lam: sp.Integer(1), S: sp.Integer(2)*(sp.Integer(Nval)+1)}
        vals = {str(k): str(sp.simplify(v.subs(subsN))) for k, v in solved.items()}
        # Radius scaling for compact bump version: u amplitude ~ H r^2/2, gradient ~ H r, Hessian ~ H.
        r = Nval ** -2
        Hval = float(sp.N(solved[H].subs(subsN))) if H in solved else float('nan')
        samples.append({
            "N": Nval,
            "Lambda": 1,
            "twist_norm_squared_S_B2": int(2*(Nval+1)),
            "solved_pa_pc_H": vals,
            "bump_radius_r=N^-2": r,
            "dilaton_C0_scale_H*r^2": Hval*r*r,
            "dilaton_C1_scale_H*r": Hval*r,
            "dilaton_Hessian_scale_H": Hval,
            "pointwise_twist_scale_sqrt_S": float((2*(Nval+1))**0.5),
        })

    # Noncentral almost-Killing check in H3: L_X g(Y,Z) = -< [X,Y],Z> - <Y,[X,Z]>.
    # For X=e1 in orthonormal H3 with [e1,e2]=beta e3, the only nonzero symmetric entries are (2,3),(3,2)=-beta.
    beta = sp.symbols('beta', positive=True)
    L = sp.zeros(3)
    # indices 0,1,2 for e1,e2,e3; X=e1.  L_X g(e2,e3)=-beta and symmetric.
    L[1,2] = -beta
    L[2,1] = -beta
    L_norm_sq = sp.simplify(sum(L[i,j]**2 for i in range(3) for j in range(3)))

    return {
        "metric_ansatz": "g=e^{2psi}(dx^2+dy^2+dz^2)+e^{2u}(dtheta+A)^2, A=(-B y/2)dx+(B x/2)dy",
        "u": "(H/2)(x^2+y^2+z^2)",
        "psi": "(pa/2)(x^2+y^2)+(pc/2)z^2",
        "Ricci_at_origin_before_solving": [[str(sp.factor(Ric0S[i,j])) for j in range(n)] for i in range(n)],
        "g_at_origin": [[str(g0[i,j]) for j in range(n)] for i in range(n)],
        "solution_for_Ric_equals_Lambda_at_origin_with_arbitrary_S_equals_B2": {str(k): str(sp.factor(v)) for k, v in solved.items()},
        "Ricci_at_origin_after_solving": [[str(sp.factor(Ric_solved[i,j])) for j in range(n)] for i in range(n)],
        "interpretation_of_solution": {
            "vertical_equation": "Ric_theta_theta(0)=B^2/2-3H, so choose H=(B^2/2-Lambda)/3.",
            "base_2jet": "pa,pc are O(B^2) and make the base Ricci absorb the horizontal twist/Hessian spike.",
            "arbitrary_twist": "B^2=S is a free parameter; total Ric_g(0)=Lambda g(0) for all S once the base/dilaton 2-jets are chosen.",
            "small_dilaton_spike_scaling": "On a ball of radius r<<1/S, a bump with Hessian H=O(S) has ||u||_C0=O(S r^2) and ||du||_C0=O(S r), both tending to 0 while |F|^2=S tends to infinity.",
            "consequence": "Pointwise |phi|^2 cannot be forced by the algebraic KK Ricci equations or by a naive Moser argument that lacks full-curvature/Sobolev control; the accessible quantity should be integrated Bochner/scale comparability."
        },
        "scaling_samples_Lambda1": samples,
        "noncentral_left_invariant_field_H3": {
            "Lie_derivative_matrix_for_X=e1": str(L),
            "Frobenius_norm_squared": str(L_norm_sq),
            "consequence": "Noncentral directions have |L_X g|~|b| at unit length, so the almost-Killing correction is the same order as the bracket term; they cannot replace the central Killing direction in the Bochner argument."
        }
    }


def main():
    out = {
        "title": "Step 29 dimension-four allocation and twist-spike audits",
        "scope": "Execution checks for the positive-collapse Bochner route; not a proof/refutation of Yau-26.",
        "dim4_nilpotent_allocation": dim4_nilpotent_allocation(),
        "local_twist_spike_pointwise_bound_test": compute_twist_jet_expressions(),
        "research_conclusion": [
            "In dimension four, nilpotent collapse fibres have dimension at most 3 and are 2-step, so the Step-28 center bound controls all fibre brackets in weighted L2 once a central Killing/almost-Killing field exists.",
            "The quotient-induction horizontal-twist pointwise problem is therefore not the crux for the four-dimensional positive branch; it first matters for higher-dimensional multi-step fibres.",
            "A direct symbolic KK jet computation exhibits arbitrarily large pointwise connection curvature with total Ricci exactly Lambda at a point after adjusting a small-dilaton Hessian and base Ricci 2-jet. This supports abandoning pointwise |phi|^2 as a target and focusing on integrated Bochner estimates plus collapse-scale comparability/oscillation.",
            "The main positive-branch bridge remains producing central (almost-)Killing fields with scale-correct Lie derivative bounds from C0 Ricci pinching alone; bounded-curvature CFG machinery cannot be assumed because of the Step-11 CZ spike."
        ]
    }
    path = Path(__file__).resolve().parents[1] / "data" / "step29_dim4_allocation_and_twist_spike.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    print(f"\nSaved to {path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Step 83: local smoothing constants for a diagonal degree-4 del Pezzo family
near the four-A1 product quotient X_4^T.

Purpose
-------
Construct an explicit 1-parameter family of intersections of two quadrics
whose central fibre has two double eigenvalues (hence four A1 nodes) and whose
nearby fibres are smooth.  Compute the leading local A1 smoothing parameter at
each node.  This is a first matched-control calculation: if the KE smooth degree
4 del Pezzo metrics degenerate along such a path, the local EH scales are equal
when the two eigenvalue splittings have equal magnitude.

The script does not compute any Biquard-Ozuch Green coefficient.  It only fixes
a concrete algebraic smoothing path and the local scale ratios that any matched
KE control lemma would have to use.
"""

import json
from pathlib import Path
import sympy as sp

I = sp.I
eps, kappa, c = sp.symbols('eps kappa c')

# Projective complete intersection in P^4:
#   Q0 = sum x_i^2 = 0,
#   Q1_eps = eps*x0^2 - eps*x1^2 + (1+kappa eps)*x2^2
#            + (1-kappa eps)*x3^2 + c*x4^2 = 0.
# At eps=0 the eigenvalue multiplicities are (0,0),(1,1),(c), hence two double
# roots of the binary quintic and four ordinary double points.

results = {
    "family": {
        "Q0": "x0^2+x1^2+x2^2+x3^2+x4^2",
        "Q1_eps": "eps*x0^2-eps*x1^2+(1+kappa*eps)*x2^2+(1-kappa*eps)*x3^2+c*x4^2",
        "central_eigenvalues": ["0 (multiplicity 2)", "1 (multiplicity 2)", "c (multiplicity 1)"],
        "smooth_for_small_eps_if": "eps != 0, kappa*eps != 0, and the five eigenvalues eps,-eps,1+kappa eps,1-kappa eps,c are distinct",
    },
    "nodes": [],
}

# Utility: retain constant and quadratic terms in local variables for the
# equation G=Q1-lambda_node Q0 after using Q0 only to remove the redundant
# normal direction to leading order.  Since G has no linear term at eps=0, its
# constant term and quadratic form in transverse variables give the A1 smoothing
# model up to an invertible linear change.

def analyze_A(sign):
    # Node in first eigenvalue pair: [1 : sign*i : 0 : 0 : 0].
    # Chart x0=1, x1=sign*i + y, x2=u, x3=v, x4=w.
    y, u, v, w = sp.symbols(f'y_A{sign} u_A{sign} v_A{sign} w_A{sign}')
    x0 = 1
    x1 = sign*I + y
    x2 = u
    x3 = v
    x4 = w
    Q0 = x0**2 + x1**2 + x2**2 + x3**2 + x4**2
    Q1 = eps*x0**2 - eps*x1**2 + (1+kappa*eps)*x2**2 + (1-kappa*eps)*x3**2 + c*x4**2
    G = sp.expand(Q1)  # lambda_node=0, so Q1 - 0*Q0
    # constant and eps=0 quadratic transverse part in (u,v,w); y is eliminated by Q0.
    const = sp.expand(G.subs({y:0,u:0,v:0,w:0}))
    quad0 = sp.expand(G.subs(eps,0).subs(y,0))
    return {
        "node": f"A_{'plus' if sign==1 else 'minus'}",
        "projective_point": f"[1:{'i' if sign==1 else '-i'}:0:0:0]",
        "eigenvalue_pair": "0-pair (x0,x1)",
        "redundant_equation": "Q0 = 2 sign*i*y + O(2) solves for y",
        "local_G": "Q1_eps - 0*Q0",
        "smoothing_constant_leading": str(sp.series(const, eps, 0, 2).removeO()),
        "central_quadratic_form_after_eliminating_y": str(quad0),
        "nondegenerate_if": "c != 0",
    }


def analyze_B(sign):
    # Node in second eigenvalue pair: [0 : 0 : 1 : sign*i : 0].
    # Chart x2=1, x3=sign*i + y, x0=p, x1=q, x4=w.
    y, p, q, w = sp.symbols(f'y_B{sign} p_B{sign} q_B{sign} w_B{sign}')
    x0 = p
    x1 = q
    x2 = 1
    x3 = sign*I + y
    x4 = w
    Q0 = x0**2 + x1**2 + x2**2 + x3**2 + x4**2
    Q1 = eps*x0**2 - eps*x1**2 + (1+kappa*eps)*x2**2 + (1-kappa*eps)*x3**2 + c*x4**2
    G = sp.expand(Q1 - Q0)  # lambda_node=1, so cancel the central linear gradient
    const = sp.expand(G.subs({y:0,p:0,q:0,w:0}))
    quad0 = sp.expand(G.subs(eps,0).subs(y,0))
    return {
        "node": f"B_{'plus' if sign==1 else 'minus'}",
        "projective_point": f"[0:0:1:{'i' if sign==1 else '-i'}:0]",
        "eigenvalue_pair": "1-pair (x2,x3)",
        "redundant_equation": "Q0 = 2 sign*i*y + O(2) solves for y",
        "local_G": "Q1_eps - 1*Q0",
        "smoothing_constant_leading": str(sp.series(const, eps, 0, 2).removeO()),
        "central_quadratic_form_after_eliminating_y": str(quad0),
        "nondegenerate_if": "c != 1",
    }

for sgn in [1, -1]:
    results["nodes"].append(analyze_A(sgn))
for sgn in [1, -1]:
    results["nodes"].append(analyze_B(sgn))

results["scale_consequences"] = {
    "local_smoothing_parameters_up_to_units": {
        "0-pair_nodes": "2*eps + O(eps^2)",
        "1-pair_nodes": "2*kappa*eps + O(eps^2)",
    },
    "equal_magnitude_condition": "|kappa|=1 gives equal leading |s_j| at all four A1 nodes; kappa=1 gives the simplest real equal-scale path",
    "spotti_scale_relation": "For local equation z1^2+z2^2+z3^2=s, Spotti uses delta^2=sqrt(|s|), hence equal |s_j| gives equal EH diameters/scales up to common constants in matched coordinates.",
    "matched_control_use": "If this path is identified with the all-same-chirality KE degeneration in the Biquard-Ozuch chart, its radial equation gives s_self + d_same_diag + 2*c_same_adj = 0 at each coefficient layer visible in the matched expansion. This is a conditional coefficient relation, not an automatic conclusion for mixed chirality.",
}

out = Path("Sessions/S0910A01/workspace/data/step83_diagonal_delpezzo_local_smoothing.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(results, indent=2), encoding="utf-8")
print(json.dumps(results, indent=2))
print(f"\nWrote {out}")

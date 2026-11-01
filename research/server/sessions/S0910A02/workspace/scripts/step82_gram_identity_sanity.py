#!/usr/bin/env python3
"""
Symbolic/algebraic sanity checks for the Step82 Gram determinant route.

We check the matrix calculus identities behind the local formula for
G_ab=<omega_a,omega_b>, where each harmonic SD form satisfies
  ∇*∇ omega = B omega,  B=2W^+ - s/3 I
under the convention that ∇*∇ is the nonnegative connection Laplacian and
Delta = d*d is the nonnegative scalar Laplacian.  Pointwise on the open set
where Ω:R^b -> Λ^+ has full rank b=rank(Λ^+)=3, G=Ω^T Ω is invertible and Ω is
a square isomorphism.

This script does not use coordinates on a manifold; it verifies the exact
linear-algebra traces and records the sign-convention dependence.
"""
import json
from pathlib import Path

# We encode the identities as strings plus test them on a random numerical matrix.
import numpy as np
rng = np.random.default_rng(82082)

Omega = rng.normal(size=(3,3))
while abs(np.linalg.det(Omega)) < 0.1:
    Omega = rng.normal(size=(3,3))
B = rng.normal(size=(3,3))
B = 0.5*(B+B.T)
B = B - np.trace(B)/3*np.eye(3) - 4*np.eye(3)  # arbitrary symmetric with trace -12
G = Omega.T @ Omega
lhs = np.trace(np.linalg.inv(G) @ (Omega.T @ B @ Omega))
rhs = np.trace(B)
trace_pullback_ok = abs(lhs-rhs) < 1e-10

# For one derivative direction A=dΩ, dG = A^TΩ+Ω^TA, K=A^T A.
A = rng.normal(size=(3,3))
dG = A.T @ Omega + Omega.T @ A
K = A.T @ A
# identity: d^2 logdet includes tr(G^{-1} d2G) - tr(G^{-1}dG G^{-1}dG).  If
# positive scalar Laplacian Δ=-sum ∂ii and connection Laplacian ∇*∇=-sum ∂ii,
# the local PDE gives (1/2)ΔG = Ω^T B Ω - K. Hence
# (1/2)Δ log det G = tr(G^{-1}(Ω^T B Ω - K)) + (1/2)tr(G^{-1} dG G^{-1} dG) summed over i.
# We check only the pullback trace equality; derivative terms do not reduce to a sign.
derivative_quadratic = 0.5*np.trace(np.linalg.inv(G) @ dG @ np.linalg.inv(G) @ dG)
Kterm = np.trace(np.linalg.inv(G) @ K)

# Check normalized determinant is scale invariant and <=1 by AM-GM.
eigs = np.linalg.eigvalsh(G)
delta_norm = 3*(np.linalg.det(G)**(1/3))/np.trace(G)
amgm_ok = 0 <= delta_norm <= 1+1e-12

data = {
    "purpose": "Sanity-check local Gram determinant identities before using them as an alignment/positive-Einstein obstruction route.",
    "convention": {
        "form_Weitzenbock": "For harmonic SD forms on Ric=3g: ∇*∇ω = Bω, B=2W^+ - 4I under nonnegative ∇*∇ convention.",
        "scalar_laplacian": "Using nonnegative Δ=d*d=-trace Hessian, (1/2)ΔG = Ω^*BΩ - K, K_ab=<∇ω_a,∇ω_b>.",
        "warning": "If Δ is the analyst positive/negative opposite convention, all displayed Δ signs reverse. Integral identities on punctured domains must preserve this convention.",
    },
    "local_full_rank_formula": {
        "G": "Ω^*Ω, square because b_+=rank Λ^+=3 only in the balanced τ=0 row with chosen orientation.",
        "trace_pullback_identity": "tr(G^{-1} Ω^* B Ω)=tr(B)=-12 on {detΩ≠0}; this fails if Ω has rank<3 or for b_+<3 rectangular Ω.",
        "formula": "(1/2)Δ log det G = tr(B) - tr(G^{-1}K) + (1/2)Σ_i tr(G^{-1}(∇_iG)G^{-1}(∇_iG)) on detG>0.",
        "normalized_delta": "δ_G=3(detG)^(1/3)/trG ∈ [0,1] by AM-GM; δ_G=1 iff G scalar.",
    },
    "numeric_sanity": {
        "trace_pullback_lhs": float(lhs),
        "trace_B_rhs": float(rhs),
        "trace_pullback_ok": trace_pullback_ok,
        "sample_K_term": float(Kterm),
        "sample_positive_derivative_quadratic_term": float(derivative_quadratic),
        "normalized_delta_sample": float(delta_norm),
        "amgm_ok": amgm_ok,
    },
    "obstruction_attempt_analysis": {
        "topological_input": "If detΩ>0 everywhere, the three harmonic SD forms trivialize Λ^+, forcing p1(Λ^+)=0. For χ=8,τ=0, p1(Λ^+)=16, so detΩ vanishes for every harmonic basis. Non-symplecticity is stronger directionwise: every nonzero class has some zero.",
        "boundary_term": "Integrating Δ log detG over M minus a tubular neighborhood of Z={detG=0} gives only a boundary flux around Z. Without a quantitative lower bound on this flux in terms of p1 or local vanishing order, no Weyl-energy inequality follows.",
        "singularity_problem": "Zeros of detΩ need not be isolated; individual near-symplectic forms have circle zero sets generically, but det rank-drop sets for a 3-frame can be surfaces/curves with complicated stratification. log detG can have nonintegrable-looking negative singularities and boundary flux depends on vanishing model.",
        "sign_problem": "The derivative terms have competing signs: -tr(G^{-1}K) and +1/2|∇G|_G^2. Cauchy-Schwarz gives neither a clean nonpositive nor nonnegative remainder in general. Thus the local PDE is theorem-shaped but not an immediate integrated inequality.",
        "stop_condition_result": "Bounded attempt stalls at the missing quantitative transgression/vanishing-order theorem. This is a precise new target, not a closed obstruction.",
    },
}

out = Path("Sessions/S0910A02/workspace/data/step82_gram_identity_sanity.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({"output": str(out), "trace_pullback_ok": trace_pullback_ok, "amgm_ok": amgm_ok, "stop": "missing quantitative transgression/zero-set theorem"}, indent=2))

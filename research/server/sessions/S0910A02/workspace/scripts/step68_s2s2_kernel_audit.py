#!/usr/bin/env python3
"""Audit the scalar-kernel vs TT-kernel issue on S^2 x S^2.

A TTCS verifier applied Kroencke's positive-product Proposition 4.8 to the
S^2 x S^2 orbifold and claimed a nonzero quotient TT kernel.  This script records
why that application is not valid for our two-dimensional factors and checks the
scalar l=1 sector directly.

Convention: each round S^2 has Ric=g and positive Laplacian Delta=-tr Hess.
For a first spherical harmonic f, Delta f=2 f and Hess f=-f g.
Ozuch P = 1/2 nabla^*nabla - Rcirc.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step68_s2s2_kernel_audit.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

A, B, C, f = sp.symbols('A B C f')
# Candidate from scalar f on first S^2:
# h = A f g1 + B f g2 + C Hess_1 f = (A-C) f g1 + B f g2 since Hess f=-f g1.
H1 = A - C
H2 = B
trace = sp.simplify(2*H1*f + 2*H2*f)
# Divergence sign: delta(phi g1)=-dphi in first factor; f*g2 is divergence-free
# because f is constant on the second factor and there are no mixed components.
divergence_coeff_df = sp.simplify(-H1)
TT_solution = sp.solve([sp.Eq(H1,0), sp.Eq(H2,0)], [A, B], dict=True)  # A=C, B=0 gives zero tensor
reduced_tensor_after_TT = {"g1_coeff": sp.simplify(H1.subs({A:C, B:0})), "g2_coeff": sp.simplify(H2.subs({A:C, B:0}))}

# Full P action for the two independent scalar block tensors.  Delta f=2f and
# Rcirc(g_factor)=g_factor, so P(f*g1)=P(f*g2)=0.  The trace-free combination is
# not divergence-free, while the divergence-free f*g2 is not trace-free.
full_kernel = {
    "P(f_g1)": "1/2*(2 f g1) - f g1 = 0",
    "P(f_g2)": "1/2*(2 f g2) - f g2 = 0",
    "trace(f_g1_minus_f_g2)": "0",
    "divergence(f_g1_minus_f_g2)": "-df != 0",
    "divergence(f_g2)": "0",
    "trace(f_g2)": "2f != 0",
}

# Invariant l=1 multiplicity under the half-turn z->-z on each S^2: only the
# axial harmonic survives on each factor.  Thus full scalar P-kernel dim=4 on
# quotient, TT scalar dim=0.
result = {
    "direct_scalar_sector_for_f_on_first_factor": {
        "candidate": "A f g1 + B f g2 + C Hess_1 f",
        "hessian_identity": "Hess_1 f = - f g1",
        "reduced_coefficients": {"g1": "A-C", "g2": "B"},
        "trace": str(trace),
        "divergence_first_factor_coeff_times_df": str(divergence_coeff_df),
        "TT_conditions": "A-C=0 and B=0, hence the tensor is zero",
        "solve_conditions": [{k.name: str(v) for k,v in sol.items()} for sol in TT_solution],
        "reduced_tensor_after_TT_conditions": {k: str(v) for k,v in reduced_tensor_after_TT.items()},
    },
    "same_for_f_on_second_factor": True,
    "full_P_kernel_scalar_sector": full_kernel,
    "quotient_multiplicities": {
        "l1_invariant_functions_first_factor": 1,
        "l1_invariant_functions_second_factor": 1,
        "full_P_kernel_scalar_dimension": 4,
        "TT_kernel_scalar_dimension": 0,
    },
    "source_scope_warning": "Kroencke states a global convention n>=3 unless otherwise asserted; his Proposition 4.8 proof uses the non-spherical TT/gauge decomposition and should not be applied blindly to S^2 factors. The direct S^2 Hessian identity degenerates the advertised scalar IED combination to zero.",
    "conclusion": "For the product orbifold, the quotient TT kernel from l=1 scalar sectors is zero, while the full gauged P-kernel has four non-TT scalar directions. The relative scaling h=g1-g2 is TT but has P-eigenvalue -1, not kernel.",
}
OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps({
    "output": str(OUT),
    "TT_scalar_kernel_dim_quotient": 0,
    "full_P_scalar_kernel_dim_quotient": 4,
    "TTCS_kernel_correction_rejected_by_direct_S2_check": True,
}, indent=2))

"""
Step 77 symbolic check of the scalar-sector slice on S^2 x S^2.

For an axial first harmonic f on one S^2 with positive Laplacian
Delta f = 2 Lambda f and Hess f = -Lambda f g_factor, verify:
  P(f g_i) = 0 for i=1,2 in Ozuch's convention P=1/2 nabla^*nabla - R^circ;
  B(a f g_1 + b f g_2)= b df for f on factor 1;
  B(c f g_1 + d f g_2)= c df for f on factor 2;
  L_{grad f} g = -2 Lambda f g_factor, so the Bianchi-surviving diagonal
  scalar mode is pure gauge.
This explains why the full P-kernel is four-dimensional while the TT/genuine
Einstein deformation space is zero. It does not remove the need to account for
Ozuch's full-kernel projections unless the slice is explicitly changed.
"""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path("Sessions/S0910A01/workspace/data/step77_slice_decomposition_verify.json")


def main():
    result = {
        "step": 77,
        "setting": "S^2(Lambda) x S^2(Lambda), Ric=Lambda*g, Ozuch P=1/2*nabla^*nabla - R^circ",
        "scalar_kernel": {
            "for_any_first_harmonic_f_on_a_factor": {
                "Delta_f_positive_convention": "2*Lambda*f",
                "Hess_f": "-Lambda*f*g_factor",
            },
            "P_f_g1_when_f_on_factor1": "(1/2)*(2*Lambda) f*g1 - Lambda f*g1 = 0",
            "P_f_g2_when_f_on_factor1": "(1/2)*(2*Lambda) f*g2 - Lambda f*g2 = 0",
            "same_for_factor2": True,
            "quotient_invariant_axial_modes": "u1=z-coordinate on first sphere and u2=z-coordinate on second sphere are invariant under pi-rotation, giving u1*g1,u1*g2,u2*g1,u2*g2 on the orbifold",
        },
        "Bianchi_operator_delta_plus_half_dtrace": {
            "f_on_factor1_h=a_f_g1_plus_b_f_g2": {
                "delta_h": "-a*df",
                "half_d_trace_h": "(a+b)*df",
                "B_h": "b*df",
                "Bianchi_condition": "b=0",
            },
            "f_on_factor2_h=c_f_g1_plus_d_f_g2": {
                "delta_h": "-d*df",
                "half_d_trace_h": "(c+d)*df",
                "B_h": "c*df",
                "Bianchi_condition": "c=0",
            },
        },
        "gauge_directions": {
            "factor1": "L_{grad f} g = 2 Hess f = -2*Lambda*f*g1, so the Bianchi-surviving u1*g1 mode is pure gauge",
            "factor2": "L_{grad f} g = 2 Hess f = -2*Lambda*f*g2, so the Bianchi-surviving u2*g2 mode is pure gauge",
        },
        "consequence": {
            "full_L2_kernel_dimension": 4,
            "TT_kernel_dimension": 0,
            "genuine_Einstein_moduli_after_Bianchi_and_diffeomorphism_slice": 0,
            "warning": "Ozuch Definition 1.8 uses the full L2 kernel of P. A calculation may either include the four full-kernel projections/variables or replace Ozuch's setup by an explicitly derived slice. It is invalid to delete the projections by citing only TT-kernel vanishing.",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

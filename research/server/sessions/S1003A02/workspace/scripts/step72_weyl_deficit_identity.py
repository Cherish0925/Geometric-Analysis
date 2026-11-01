#!/usr/bin/env python3
"""Step 72: exact symbolic checks for the orientation-free Weyl-deficit law.

Conventions:
  8*pi^2 chi = W + S/24 - P/2,
  R = P + S/4,
  L = S - T^2/V,
  E = (4P+L)/R.
The script eliminates P,S and checks the unit-wall and Yamabe formulas.
"""
import json
import sympy as sp
from pathlib import Path

pi = sp.pi
W, S, P, R, L, T, V, chi, Y = sp.symbols(
    "W S P R L T V chi Y", real=True
)

# Algebraic defining equations, used by direct substitution.
P_gb = 2*W + S/sp.Integer(12) - 16*pi**2*chi
R_gb = sp.expand(P_gb + S/sp.Integer(4))
E_minus_1 = sp.factor((4*P_gb + L - R_gb)/R_gb)
orient_num = sp.factor(4*P_gb + L - R_gb)
expected_num = 6*(W - 8*pi**2*chi) + L

# At a Yamabe representative: S=Y^2, L=0.
R_yam = sp.factor(R_gb.subs(S, Y**2))
E_yam = sp.factor((4*P_gb/R_gb).subs(S, Y**2))
D = sp.symbols("D", real=True)
E_yam_D = sp.factor(E_yam.subs(W, 8*pi**2*chi-D))
ratio_D = sp.factor(1 - 6*D/R_yam.subs(W, 8*pi**2*chi-D))

# Connected-sum deficit: chi(M#N)=chiM+chiN-2 and W_inf subadditive.
chiM, chiN, WM, WN = sp.symbols("chiM chiN WM WN", real=True)
dM = 8*pi**2*chiM-WM
dN = 8*pi**2*chiN-WN
d_connected_lower = sp.factor(8*pi**2*(chiM+chiN-2) - (WM+WN))
connected_residual = sp.factor(d_connected_lower - (dM+dN-16*pi**2))

# Model checks: constant-curvature Einstein and cylinder R x S^3.
def model(name, chi_value, W_value, P_value, S_value, R_value, L_value=0):
    e = sp.factor((4*P_value+L_value)/R_value)
    rhs = sp.factor(1+(6*(W_value-8*pi**2*chi_value)+L_value)/R_value)
    return {"name": name, "E": str(e), "weyl_deficit_form": str(rhs), "residual": str(sp.factor(e-rhs))}

models = [
    model("round_S4", 2, 0, 0, 384*pi**2, 96*pi**2),
    # per length L=1 for R x S^3(1): vol=2*pi^2, P density=3, R density=12
    model("cylinder_RxS3_per_unit_length", 0, 0, 6*pi**2, 72*pi**2, 24*pi**2),
]

out = {
    "gauss_bonnet_eliminations": {
        "P": str(P_gb),
        "R": str(R_gb),
        "orientation_free_numerator": str(orient_num),
        "expected_numerator": str(expected_num),
        "identity_residual": str(sp.factor(orient_num-expected_num)),
        "E_minus_1": str(E_minus_1),
    },
    "yamabe_representative": {
        "R": str(R_yam),
        "E": str(E_yam),
        "E_in_deficit_D": str(E_yam_D),
        "ratio_form": str(ratio_D),
        "residual": str(sp.factor(E_yam_D-ratio_D)),
    },
    "connected_sum": {
        "lower_deficit_from_subadditivity": str(d_connected_lower),
        "expected": str(dM+dN-16*pi**2),
        "residual": str(connected_residual),
    },
    "models": models,
}

out_path = Path(__file__).resolve().parents[1] / "data" / "step72_weyl_deficit_identity.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))

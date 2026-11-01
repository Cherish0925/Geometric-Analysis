#!/usr/bin/env python3
"""Symbolic bookkeeping for Step 76 center-energy and flux identities.

This checks only algebraic reductions.  It does not prove existence of a core.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

# Center scalar identity in orbit arclength s.
rho, h, hp, A0sq, e = sp.symbols("rho h hp A0sq e", real=True)
# |A|^2 = |A0|^2 + h^2/2 in orbit dimension two.
R = sp.expand(-2 * hp - A0sq - sp.Rational(3, 2) * h**2)
# After multiplying by rho and integrating periodically,
# int rho*h' = -int rho*h^2 because rho'=rho*h.
integrated_rhs_density = sp.expand(
    (-2 * hp - A0sq - sp.Rational(3, 2) * h**2).subs(hp, -h**2)
)
# R=-6+e therefore gives int rho A0^2 = 6V + 1/2 int rho h^2 - int rho e.
A0_integrated_density = sp.solve(
    sp.Eq(-6 + e, integrated_rhs_density), A0sq
)[0]

# Diagonal orbit block: A=diag(b_s,c_s), d=b-c.
ds = sp.symbols("d_s", real=True)
A0_diag_sq = sp.simplify(2 * (ds / 2) ** 2)
diag_energy_density = sp.simplify(2 * A0_integrated_density)

# Sharp approximate reflected-center cancellation.
delta = sp.symbols("delta", nonnegative=True, real=True)
Evv, E11, E22, Enn = sp.symbols("Evv E11 E22 Enn", real=True)
e_components = Evv + E11 + E22 - Enn
# At a downward zero: K >= 3-e/2, so (Ric_q+3)(v,v) <= e-3.
# S'vv=(Ric_q+3)(v,v)-Evv.
Sprime_bound_components = sp.expand(e_components - 3 - Evv)
Sprime_worst_box = Sprime_bound_components.subs({E11: delta, E22: delta, Enn: -delta})

# Gaussian anisotropy divergence bookkeeping.
r = sp.symbols("r", real=True)
w = sp.Function("w")(r)  # slice-volume density e^(a+sigma)
D = sp.Function("D")(r)  # one Fourier-free placeholder for d
J = sp.Function("J")(r)  # tangential energy placeholder
# If (w D')' plus tangential divergence =0, multiplying by D and integrating
# tangentially gives F' = radial energy + tangential energy.
Fprime_formal = "F'(r)=N(r)+Z(r), F=integral (d-c) rho d_n dmu, N,Z>=0"

out = {
    "center_scalar": {
        "pointwise_R_formula": str(R),
        "periodic_integrated_rhs_after_int_rho_hprime_eq_minus_int_rho_h2": str(integrated_rhs_density),
        "A0_energy_density_identity": str(A0_integrated_density),
        "meaning": "int rho |A0|^2 = 6 int rho + (1/2) int rho h^2 - int rho e",
    },
    "diagonal_center": {
        "A0_sq": str(A0_diag_sq),
        "d_energy_density_identity": str(diag_energy_density),
        "meaning": "int rho |d_s|^2 = 12 int rho + int rho h^2 - 2 int rho e",
        "exact_floor": "normalized center anisotropy energy >= 12 when e=0",
        "ambient_defect_floor": "if |Ric_4+3g|_op<=delta at reflection center, |e|<=4delta, so normalized energy >=12-8delta",
    },
    "sharp_center_acceleration": {
        "e_components": str(e_components),
        "Sprime_selected_direction_bound": str(Sprime_bound_components),
        "box_worst_case": str(Sprime_worst_box),
        "result": "lambda_min S'(0) <= -3+3 delta",
    },
    "exact_core_flux": {
        "net_signed_flux": "Q(r)=integral rho d_n dmu is constant and Q(0)=0, hence Q(R)=0",
        "boundary_pairing": "F(R)=integral_outer (d-c) rho d_n dmu = integral_core rho |grad d|^2 dmu",
        "radial_derivative": Fprime_formal,
        "center_slope": "F'(0)=Z(0)>=12 Vol(center quotient) in the exact diagonal scalar-minus-six center",
        "scope": "A center-slope floor gives no geometry-uniform positive thickness without coefficient/regularity control",
    },
}

path = Path(__file__).resolve().parents[1] / "data" / "step76_center_energy_flux.json"
path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out, indent=2))
print("wrote", path)

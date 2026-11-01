#!/usr/bin/env python3
"""Step 69: audit the log-Weyl flux constants in 20260912.tex.

This is not a proof assistant formalization.  It records the algebraic core used
by FND:flux for the four-dimensional A1 annulus and the sharp constants in the
spherical model from lines 956--989 of the manuscript.

Assumptions being audited:
  * K is homogeneous quadratic and satisfies tr K = div K = Delta K = 0 and
    K(x,.) = 0.
  * o = r^{-6} K in n=4.
  * u = eta(log r) K, with eta=0 near the inner boundary and eta=1 near the
    outer boundary.
  * Step68 verified on a sample Weyl sector that
        D Ric_e(eta K)=-(eta_tt+6 eta_t)K/(2 r^2).

Then |K(r theta)|^2 = r^4 |K(theta)|^2 and dV=r^3 dr dtheta, so
  <D Ric u,o>dV = -1/2 (eta_tt+6 eta_t) |K(theta)|^2 d(log r)dtheta.
Integrating in t=log r gives -3 I_K in dimension four, i.e.
-(n+2)/2 I_K.  The lower bound follows from operator/nuclear norm duality and
int_A ||o||_* = L J_K.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step69_flux_identity_constants.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

# Formal one-dimensional integral in t=log r.  eta' has total jump 1 and eta''
# integrates to 0 because eta' vanishes at the constant end collars.
eta_t_integral = sp.Integer(1)
eta_tt_integral = sp.Integer(0)
n = sp.Integer(4)
flux_coefficient_4d = -sp.Rational(1, 2) * (eta_tt_integral + 6 * eta_t_integral)
general_expected = -sp.Rational(n + 2, 2)

# Spherical model constants from manuscript lines 956--989.
v = sp.symbols('v_Gamma', positive=True)
I_K = v / sp.Integer(216)
J_K = v / sp.Integer(9)
linear_lower_constant = sp.simplify((sp.Rational(4+2, 2) * I_K) / J_K)  # coefficient of 1/L

# Constant-scalar version: numerator v/72, denominator v/12 times L.
const_scalar_constant = sp.simplify((v / sp.Integer(72)) / (v / sp.Integer(12)))

# Eigenvalue/nuclear-norm check for Q spectrum (0,-sigma/18,sigma/36,sigma/36):
# Hilbert-Schmidt square = 1/324 + 2/1296 = 1/216 per unit volume; nuclear norm
# = 1/18 + 2/36 = 1/9 per unit volume.
sigma = sp.symbols('sigma', nonzero=True)
eigs_abs = [sp.Integer(0), sp.Rational(1,18), sp.Rational(1,36), sp.Rational(1,36)]
HS_square = sp.simplify(sum(e**2 for e in eigs_abs))
nuclear = sp.simplify(sum(eigs_abs))

result = {
    "flux_identity_4d": {
        "assumed_operator_identity": "D Ric_e(eta(log r) K)=-(eta_tt+6 eta_t)K/(2 r^2)",
        "o": "r^{-6} K",
        "volume_scaling": "|K(r theta)|^2=r^4|K(theta)|^2, dV=r^3 dr dtheta, so r-powers reduce to d(log r)",
        "eta_tt_integral": str(eta_tt_integral),
        "eta_t_integral": str(eta_t_integral),
        "flux_coefficient_times_IK": str(flux_coefficient_4d),
        "matches_minus_(n+2)/2_for_n=4": bool(sp.simplify(flux_coefficient_4d - general_expected) == 0),
    },
    "duality_lower_bound": {
        "integral_norm_o": "L J_K",
        "bound": "||D Ric u||_{op,infty} >= 3 I_K/(L J_K) in n=4",
    },
    "spherical_model_constants": {
        "Q_spectrum_abs_values": [str(e) for e in eigs_abs],
        "HS_square_per_unit_volume": str(HS_square),
        "nuclear_norm_per_unit_volume": str(nuclear),
        "I_K": "v_Gamma/216",
        "J_K": "v_Gamma/9",
        "linear_unconstrained_constant": str(linear_lower_constant),
        "linear_unconstrained_constant_statement": "1/(8 L)",
        "constant_scalar_constant": str(const_scalar_constant),
        "constant_scalar_constant_statement": "1/(6 L)",
    },
    "scope": "This audits the clean annulus constant algebra used by FND:flux and the sharp spherical-model constants.  It does not prove the nonlinear estimates or the applicability to arbitrary bubbling sequences; those require the manuscript's hypotheses and ambient tower/gauge localization.",
}
OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps({
    "output": str(OUT),
    "flux_coefficient_times_IK": str(flux_coefficient_4d),
    "unconstrained_constant": str(linear_lower_constant),
    "constant_scalar_constant": str(const_scalar_constant),
}, indent=2))

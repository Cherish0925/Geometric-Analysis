#!/usr/bin/env python3
"""Step 68: verify the 20260912 explicit Eguchi-Hanson Einstein core.

The new cumulative manuscript gives a two-axis Bianchi IX family q_Lambda with
Ric(q_Lambda)=Lambda q_Lambda, smooth on the O(-2) disk bundle for small Lambda,
and a gauge-corrected derivative h_tilde at Lambda=0 satisfying
D Ric_EH(h_tilde)=g_EH with a prescribed quadratic far-field H_*.

This script checks the algebraic derivative and the Lie-gauge correction against
lines 472-529 of Skills/qiushi-yau26/references/research/20260912.tex.  The
Einstein equation itself follows by differentiating Ric(q_Lambda)=Lambda q_Lambda
once the q_Lambda ODE is accepted/verified, but here we verify the concrete
coefficients that must match our Step-65/66 Bianchi-IX conventions.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step68_qLambda_core_verify.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

r = sp.symbols('r', positive=True)
Lam = sp.symbols('Lam')

# c_Lambda and first variation at Lambda=0
c = (1 - Lam/4)**2 - 1
cdot0 = sp.diff(c, Lam).subs(Lam, 0)
W = 1 - r**-4

# Differentiate the defining integral explicitly at Lambda=0.
s = sp.symbols('s', positive=True)
A = s**3 * (4 - Lam*s**2) / (1 + c*s**2)**sp.Rational(3,2)
Adot0 = sp.simplify(sp.diff(A, Lam).subs(Lam, 0))
Idot0 = sp.integrate(Adot0, (s, 1, r))
I0 = r**4 - 1
pref_dot0 = sp.simplify(sp.diff(sp.sqrt(1+c*r**2)/r**4, Lam).subs(Lam, 0))
Gdot = sp.simplify(pref_dot0 * I0 + Idot0 / r**4)
Fdot = sp.simplify(cdot0*r**2*W + Gdot)

# Raw derivative of q_Lambda at Lambda=0 in coframe dr^2, sigma1^2+sigma2^2, sigma3^2.
h_raw_rr = sp.simplify(-Fdot / W**2)
h_raw_12 = sp.Integer(0)
h_raw_3 = sp.simplify(r**2/4 * Gdot)

# Lie derivative of EH metric along V=v(r) d/dr, v=5/72(r^3-r^-1).
v = sp.Rational(5,72)*(r**3 - r**-1)
g_rr = 1/W
g_12 = r**2/4
g_3 = r**2*W/4
Lie_rr = sp.simplify(v*sp.diff(g_rr,r) + 2*g_rr*sp.diff(v,r))
Lie_12 = sp.simplify(v*sp.diff(g_12,r))
Lie_3 = sp.simplify(v*sp.diff(g_3,r))

h_tilde_rr = sp.factor(sp.simplify(h_raw_rr - Lie_rr))
h_tilde_12 = sp.factor(sp.simplify(h_raw_12 - Lie_12))
h_tilde_3 = sp.factor(sp.simplify(h_raw_3 - Lie_3))

# Manuscript formulas.
ms_rr = -r**2*(7*r**2-5)/(36*(r**2-1)*(r**2+1)**2)
ms_12 = -5*(r**4-1)/sp.Integer(144)
ms_3 = -r**4/sp.Integer(72) + sp.Rational(1,16) - r**-2/sp.Integer(12) + 5*r**-4/sp.Integer(144)

checks = {
    "Adot0": str(sp.factor(Adot0)),
    "Idot0": str(sp.factor(Idot0)),
    "Gdot0": str(sp.factor(Gdot)),
    "Fdot0": str(sp.factor(Fdot)),
    "h_raw_coefficients": {
        "dr2": str(sp.factor(h_raw_rr)),
        "sigma12": str(h_raw_12),
        "sigma3": str(sp.factor(h_raw_3)),
    },
    "Lie_V_coefficients": {
        "V": "5/72*(r^3-r^-1) d/dr",
        "dr2": str(sp.factor(Lie_rr)),
        "sigma12": str(sp.factor(Lie_12)),
        "sigma3": str(sp.factor(Lie_3)),
    },
    "h_tilde_coefficients": {
        "dr2": str(h_tilde_rr),
        "sigma12": str(h_tilde_12),
        "sigma3": str(h_tilde_3),
    },
    "matches_manuscript": {
        "dr2": bool(sp.simplify(h_tilde_rr-ms_rr)==0),
        "sigma12": bool(sp.simplify(h_tilde_12-ms_12)==0),
        "sigma3": bool(sp.simplify(h_tilde_3-ms_3)==0),
    },
    "asymptotic_leading": {
        "dr2": str(sp.series(h_tilde_rr, r, sp.oo, 3)),
        "sigma12": str(sp.series(h_tilde_12, r, sp.oo, 2)),
        "sigma3": str(sp.series(h_tilde_3, r, sp.oo, 2)),
    },
    "logical_consequence": "Since q_Lambda is an exact Einstein family in the same Bianchi-IX convention, differentiating Ric(q_Lambda)=Lambda*q_Lambda at Lambda=0 gives D Ric_EH(h_raw)=g_EH; subtracting Lie_V g_EH preserves this because Ric_EH=0. Thus h_tilde is an explicit smooth linear correction, unlike the Step66 scalar/radial guesses.",
}

OUT.write_text(json.dumps(checks, indent=2, ensure_ascii=False))
print(json.dumps({
    "output": str(OUT),
    "matches_manuscript": checks["matches_manuscript"],
    "Gdot0": checks["Gdot0"],
    "h_tilde_sigma3": checks["h_tilde_coefficients"]["sigma3"],
}, indent=2))

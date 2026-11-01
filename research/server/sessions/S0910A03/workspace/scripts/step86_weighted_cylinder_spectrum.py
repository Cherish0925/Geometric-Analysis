#!/usr/bin/env python3
"""Step 86: exact drift spectrum on the round-cusp weighted cylinder.

The model base is gamma=dr^2+exp(2r) dz^2, sigma=2r, z periodic of
coordinate period Lz.  For L=Delta_gamma+<grad sigma,grad>,

    L = d_rr + 3 d_r + exp(-2r) d_zz.

For the symmetric Dirichlet energy of a scalar test function on [-R,R]xS1,
the radial Rayleigh quotient after conjugating by exp(3r/2) has potential
9/4.  Thus the lowest radial Dirichlet eigenvalue of -L is
9/4 + (pi/(2R))^2.  The angular term is nonnegative.  This supplies an
exact benchmark for any proposed massive-resolvent estimate, but is not a
general coupled-connector theorem.
"""
from __future__ import annotations

import json
from pathlib import Path
import math

rows=[]
for R in [0.5,1.0,2.0,4.0,8.0,16.0,32.0]:
    lam = 9.0/4.0 + (math.pi/(2*R))**2
    rows.append({"R":R,"lambda1_radial_dirichlet":lam,"inverse":1/lam})

out={
  "model":"gamma=dr^2+e^(2r)dz^2, sigma=2r, dmu=e^(3r)dr dz",
  "drift_operator":"L=d_rr+3d_r+e^(-2r)d_zz",
  "conjugation":"phi=e^(-3r/2) y gives integral e^(3r)|phi_r|^2 = integral(|y_r|^2+9|y|^2/4) for Dirichlet y",
  "radial_lambda1":"9/4+(pi/(2R))^2",
  "rows":rows,
  "limiting_gap_as_R_to_infinity":9.0/4.0,
  "interpretation":"The exact cusp has a length-independent radial spectral gap. CD(K,4) alone does not encode this; a general OT proof would need to recover an analogous global consequence from the coupled area equation and boundary data."
}
path=Path(__file__).resolve().parents[1]/"data"/"step86_weighted_cylinder_spectrum.json"
path.write_text(json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps(out,indent=2));print(f"wrote {path}")

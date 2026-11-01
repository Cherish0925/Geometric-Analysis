#!/usr/bin/env python3
"""Exact checks for Step 103: isotropy angles/invariant symmetric blocks and Wahl-orbifold signatures.

For gamma=diag(zeta,zeta^(n-1)), zeta^(n^2)=1, the effective rotation exponents on
Lambda^+ and Lambda^- are n and n-2 modulo n^2.  A nontrivial planar rotation not equal
to pi forces every commuting real symmetric 3x3 matrix to have a scalar planar block.
The script checks the angle exclusions and enumerates exact ball-quotient signature
values for the first realized one-point family.
"""
from fractions import Fraction
import json
from pathlib import Path

rows=[]
for n in range(2,65):
    N=n*n
    eplus=n % N
    eminus=(n-2) % N
    plus_nontrivial = eplus not in (0, N//2) if N % 2 == 0 else eplus != 0
    minus_nontrivial = eminus not in (0, N//2) if N % 2 == 0 else eminus != 0
    rows.append({
        "n":n,"N":N,"lambda_plus_rotation_exponent":eplus,
        "lambda_minus_rotation_exponent":eminus,
        "plus_angle_not_0_or_pi":plus_nontrivial,
        "minus_angle_not_0_or_pi":minus_nontrivial,
    })
assert rows[0]["plus_angle_not_0_or_pi"] is False   # n=2: angle pi
assert rows[0]["minus_angle_not_0_or_pi"] is False  # n=2: angle zero
assert all(r["plus_angle_not_0_or_pi"] for r in rows[1:])
assert all(r["minus_angle_not_0_or_pi"] for r in rows[1:])

sig=[]
for A in (18,27,36,45,54):
    for n in (3,5,7,15):
        tau=Fraction(A,9)-4+Fraction(2,3)*(1-Fraction(1,n*n))
        sig.append({"A":A,"k":4,"n":n,"tau_num":tau.numerator,"tau_den":tau.denominator,
                    "tau_sign":(tau>0)-(tau<0)})
assert all(x["tau_sign"]<0 for x in sig if x["A"] in (18,27))
assert all(x["tau_sign"]>0 for x in sig if x["A"]>=36)

out={"isotropy":rows,"one_point_ball_quotient_signatures":sig,
     "all_isotropy_assertions":True,"signature_assertions":True}
path=Path(__file__).resolve().parents[1]/"data"/"step103"/"wahl_isotropy_and_signature.json"
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2))
print(f"wrote {path}; n=3..64 two-block isotropy checks pass (n=2 exceptional); {len(sig)} signatures pass")

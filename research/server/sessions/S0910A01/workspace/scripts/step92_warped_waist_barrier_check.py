#!/usr/bin/env python3
"""Step 92 independent algebra check of A02's warped-product waist barrier.

For g=dr^2+f(r)^2 g_F in dimension 4 with Ric_F=2k g_F, at a waist
f'=0, f''>=0.  Put alpha=f''/f>=0, beta=2k/f^2>=0.  Ricci endomorphism
eigenvalues are lambda_r=-3 alpha and lambda_F=beta-alpha.  Defect from the
negative Einstein value -3 is max(3|1-alpha|, |3-alpha+beta|).

The script verifies the exact minimizer for beta>=0 and samples the landscape.
"""
from __future__ import annotations

import json, math, pathlib

DATA_DIR = pathlib.Path("Sessions/S0910A01/workspace/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def defect(alpha, beta):
    return max(3*abs(1-alpha), abs(3 - alpha + beta))


def minimizer(beta):
    # Equalize 3(alpha-1)=3+beta-alpha in the relevant interval alpha>=1.
    alpha = (6 + beta)/4
    value = 3*(beta+2)/4
    return alpha, value

samples=[]
for beta in [0, 0.01, 0.1, 0.5, 1, 2, 10]:
    a, val = minimizer(beta)
    # crude grid confirmation around the predicted minimizer
    grid_min = min((defect(x/1000, beta), x/1000) for x in range(0, int(max(5, a+2)*1000)+1))
    samples.append({
        "beta": beta,
        "alpha_min_exact": a,
        "delta_min_exact": val,
        "grid_min_delta": grid_min[0],
        "grid_min_alpha": grid_min[1],
        "matches_grid_to_1e-3": abs(grid_min[0]-val) < 1e-3,
    })

results={
    "step":92,
    "scope":"warped product waist barrier for negative pinching connector",
    "formula":"delta(alpha,beta)=max(3|1-alpha|, |3-alpha+beta|), alpha=f''/f>=0, beta=2k/f^2>=0",
    "minimum_beta_ge_0":"delta_min(beta)=3/2+3 beta/4, attained at alpha=(6+beta)/4",
    "consequence":"for k>=0 every warped waist has delta>=3/2; for round S^3 beta=2/f0^2 so delta_min=3/2+3/(2 f0^2); for flat T^3 beta=0 equality delta=3/2 is possible only at alpha=3/2",
    "negative_fiber_check":"hyperbolic fiber beta<0 can have zero defect, e.g. beta=-2, alpha=1 gives H^4 equidistant waist",
    "samples":samples,
    "interpretation":"This independently confirms A02 #614 in the warped-product class. It is pointwise and cannot be averaged away, but it is not a general non-warped waist theorem.",
}

out=DATA_DIR/"step92_warped_waist_barrier_check.json"
with open(out,"w") as f:
    json.dump(results,f,indent=2)
print(json.dumps(results,indent=2))
print(f"Wrote {out}")

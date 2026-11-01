#!/usr/bin/env python3
"""Step 60 explicit schedules for the resonant neck-drift channel.

This complements step60_resonant_flux_neck_alf.py.  It computes concrete
families with t=exp(-a/delta), the number of dyadic scales in the ALE neck,
and the l=2 Wronskian coefficient drift in the scalar model.  It also records
when nonresonant beta<2 weighted estimates eventually exceed the O(t) target.
"""
from __future__ import annotations

import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step60_neck_drift_schedules.json"

# In the normalized l=2 radial ODE L f = S with S=t*delta in the metric-scale
# convention, the coefficient drift over [1,t^-1/2] is approximately
# (t*delta/12) log(1/t).  Relative to the signal t*kappa, drift/kappa =
# delta log(1/t)/12.

def exp_channel_rows():
    rows=[]
    for a in [1, 3, 6, 12, 24]:
        for delta in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
            log_1_t = a/delta
            log10_1_t = log_1_t / math.log(10)
            dyadic_scales = log_1_t/(2*math.log(2))
            rel_drift = delta*log_1_t/12.0
            rows.append({
                "a_in_t_equals_exp_minus_a_over_delta": a,
                "delta": delta,
                "log_1_over_t": log_1_t,
                "log10_1_over_t": log10_1_t,
                "dyadic_scales_between_1_and_t_minus_half": dyadic_scales,
                "relative_l2_flux_drift_scalar_constant_source": rel_drift,
                "interpretation": "constant O(1) drift as delta->0 when t=exp(-a/delta)"
            })
    return rows


def beta_threshold_rows():
    rows=[]
    # For delta=1/log^2(1/t), factor over target for beta<2 is
    # F(L)=exp((1-beta/2)L)/L^2.  Solve roughly when F=1.
    for beta in [0.5, 1.0, 1.5, 1.8, 1.9, 1.95, 1.99]:
        c = 1 - beta/2
        # find first L on a grid where c L - 2 log L > 0
        threshold = None
        for L in [i*10 for i in range(1, 20001)]:
            if c*L - 2*math.log(L) > 0:
                threshold = L
                break
        rows.append({
            "beta": beta,
            "c=1-beta/2": c,
            "approx_first_L_with_exp(cL)/L^2_gt_1": threshold,
            "approx_log10_1_over_t_threshold": None if threshold is None else threshold/math.log(10),
            "asymptotic": "for every fixed beta<2, exp((1-beta/2)L)/L^2 -> infinity; beta=2 is endpoint/resonant"
        })
    return rows


def main():
    data={
        "status":"ok",
        "convention":"t is metric bubble scale; outer ALE radius is t^{-1/2}; l=2 source amplitude in the divided equation is delta; coefficient drift is delta log(1/t)/12 in the scalar constant-source model.",
        "exponential_neck_channel": exp_channel_rows(),
        "beta_less_than_2_asymptotic_thresholds": beta_threshold_rows(),
        "summary": {
            "delta_log_theorem_regime":"If delta_i log(1/t_i)->0, the resonant Wronskian drift is negligible and the first Ozuch vector obstruction is necessary, assuming the standard annular gauge/projection hypotheses.",
            "failure_channel":"If t_i=exp(-a/delta_i), C^0 Ricci pinching allows constant relative l=2 block drift a/12; this is the precise long-neck channel to realize or rule out.",
            "weighted_estimate_correction":"Nonresonant beta<2 estimates cannot reach the O(t) matching target asymptotically; beta=2 is an indicial root and produces exactly the logarithm measured by flux."
        }
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(json.dumps({"status":"ok","output":str(OUT),"sample":data["exponential_neck_channel"][10],"beta_1_9_threshold": [r for r in data["beta_less_than_2_asymptotic_thresholds"] if r["beta"]==1.9][0]}, indent=2))

if __name__=='__main__': main()

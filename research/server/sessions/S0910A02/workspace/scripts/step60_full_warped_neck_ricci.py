#!/usr/bin/env python3
"""Exact Ricci-size check for the corrected Step-60 long-neck warping model.

Metric on a local flat base annulus times T^2:
    g = dr^2 + r^2 dtheta^2 + exp(2u) dphi^2 + exp(-2u) dpsi^2
with
    u = t r^2 A(log r) cos(2 theta).
For this exact doubly-warped metric (flat base, 1D flat fibers),
    Ric_base = -2 du ⊗ du,
    Ric_phi/|dphi|^2 = -Delta u,
    Ric_psi/|dpsi|^2 = +Delta u.

This script checks the corrected exponential neck scale recommended by TTCS:
    eta^2 = delta, R = eta/sqrt(t) = exp(L), L=a/delta,
    hence t = delta exp(-2a/delta).
Then |Delta u| = O(t delta) and |du|^2 = O(t delta), so the exact Ricci tensor
of this LOCAL flat model is O(t delta) in the ALE frame while the H2 coefficient
A(log r) drifts by O(1).

This is still not a closed Yau-26 metric: it ignores background Einstein terms,
EH matching, gauge, end caps, and topology.  It addresses the specific TTCS
objection that the earlier eta=1 schedule had quadratic gradient terms too large.
"""
from __future__ import annotations

import json, math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step60_full_warped_neck_ricci.json"

# Use smootherstep profile q(z)=6z^5-15z^4+10z^3: q'=q''=0 at endpoints,
# enough for C^2 cap estimates.  A true C^infty profile with comparable bounds
# can replace it without changing scale.
def q(z): return 6*z**5 - 15*z**4 + 10*z**3
def qp(z): return 30*z**2*(1-z)**2
def qpp(z): return 60*z*(1-z)*(1-2*z)

def profile_constants(samples=200001):
    z=np.linspace(0.0,1.0,samples)
    qv=q(z); qpv=qp(z); qppv=qpp(z)
    return {
        "profile":"smootherstep q(z)=6z^5-15z^4+10z^3",
        "max_abs_q": float(np.max(np.abs(qv))),
        "max_abs_q_prime": float(np.max(np.abs(qpv))),
        "max_abs_q_double_prime": float(np.max(np.abs(qppv))),
        "q_endpoint_values":"q(0)=0,q(1)=1,q'(0)=q'(1)=q''(0)=q''(1)=0",
    }

def schedule(delta, a, drift=1.0, A0=0.0, samples=40001):
    L=a/delta
    eta=math.sqrt(delta)
    # Store logs to avoid underflow; compute t if representable.
    log_t=math.log(delta)-2*L
    t = math.exp(log_t) if log_t > -740 else 0.0
    z=np.linspace(0.0,1.0,samples)
    A=A0+drift*q(z)
    Ap=drift*qp(z)/L
    App=drift*qpp(z)/(L*L)
    # Delta u = t (A''+4A') cos2theta.
    max_lap_coeff=float(np.max(np.abs(App+4*Ap)))
    # |du|^2 = t^2 r^2 [ (2A+A')^2 cos^2 + 4 A^2 sin^2 ].
    # t^2 r^2 is largest at r=R=e^L, equal to t^2 e^{2L}=t*delta.
    grad_factor=np.maximum((2*A+Ap)**2, 4*A**2)  # sup over theta bounded by max of components; sum bound below too.
    grad_factor_sum=(2*A+Ap)**2+4*A**2
    max_grad_factor=float(np.max(grad_factor_sum))
    # Exact orthonormal Ricci components: base operator norm <=2|du|^2, fiber <=|Delta u|.
    ric_over_tdelta_bound=2*max_grad_factor + max_lap_coeff/delta
    return {
        "delta":delta,
        "a_in_L=a/delta":a,
        "drift_DeltaA":drift,
        "outer_orbifold_radius_eta=sqrt(delta)":eta,
        "log_neck_length_L":L,
        "log10_outer_ALE_radius_R":L/math.log(10),
        "log10_1_over_metric_scale_t":-log_t/math.log(10),
        "t_underflowed_in_float": t==0.0,
        "metric_scale_t_float_if_available":t,
        "H2_coefficient_change_t_times_DeltaA_relative_to_t":drift,
        "max_abs_Delta_u_divided_by_t":max_lap_coeff,
        "max_abs_Delta_u_divided_by_t_delta":max_lap_coeff/delta,
        "max_gradient_square_divided_by_t_delta_factor_bound":max_grad_factor,
        "exact_Ricci_operator_bound_divided_by_t_delta":ric_over_tdelta_bound,
        "scale_success_for_local_model":"yes: exact Ricci components are <= C(a,drift,A0) t delta while H2 coefficient drifts by drift*t",
    }

def fixed_eta_bad_schedule(delta, a=1.0, drift=1.0, samples=40001):
    # Compare old eta=1 schedule L=a/delta, R=e^L=t^-1/2 -> t=e^-2L.
    L=a/delta
    z=np.linspace(0.0,1.0,samples)
    A=drift*q(z); Ap=drift*qp(z)/L
    App=drift*qpp(z)/(L*L)
    max_lap_coeff=float(np.max(np.abs(App+4*Ap)))
    max_grad_factor=float(np.max((2*A+Ap)**2+4*A**2))
    # t^2 R^2=t, so |du|^2/(t delta)=factor/delta, too large.
    return {
        "delta":delta,
        "old_eta":1.0,
        "log_neck_length_L":L,
        "max_abs_Delta_u_divided_by_t_delta":max_lap_coeff/delta,
        "max_gradient_square_divided_by_t_delta_factor_bound":max_grad_factor/delta,
        "why_bad":"with eta fixed, |du|^2~t, exceeding the t*delta Ricci allowance by factor ~1/delta",
    }

def main():
    pc=profile_constants()
    rows=[]
    bad=[]
    for delta in [0.2,0.1,0.05,0.02,0.01,0.005]:
        for a in [1.0,2.0,4.0,8.0]:
            rows.append(schedule(delta,a,drift=1.0,A0=0.0))
        bad.append(fixed_eta_bad_schedule(delta,a=2.0,drift=1.0))
    data={
        "status":"ok",
        "exact_ricci_formula":"For g=base + e^{2u}dphi^2 + e^{-2u}dpsi^2 over flat 2D base: Ric_base=-2 du⊗du, Ric_phi=-Delta u, Ric_psi=+Delta u in orthonormal fiber components.",
        "profile_constants":pc,
        "corrected_eta_sqrt_delta_schedules":rows,
        "old_fixed_eta_failure_schedules":bad,
        "interpretation":{
            "what_is_verified":"After correcting the outer orbifold radius to eta^2~delta, the full exact Ricci tensor of the local doubly-warped flat model, including quadratic gradient terms, is O(t delta) across an exponentially long neck while the l=2/H2 coefficient changes by O(t).",
            "why_this_matters":"This removes the main TTCS objection to the linear neck-drift schedule and shows the exponential delta log(1/t) failure channel survives at the exact local doubly-warped Ricci level.",
            "limitations":"The model is local, Ricci-flat/flat-background rather than positive Einstein, and on a T^2-warped annulus rather than an S^3/Z2 EH neck. It still needs cap smoothness, nonlinear matching to ambient H2/H4, EH projection nonzero, and a closed smooth topology."
        }
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(json.dumps({
        "status":"ok",
        "output":str(OUT),
        "profile":pc,
        "corrected_sample":rows[6],
        "old_bad_sample":bad[2],
        "interpretation":data["interpretation"]
    },indent=2))

if __name__=='__main__': main()

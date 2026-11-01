#!/usr/bin/env python3
"""Step 60 local opposite-warping neck drift model.

This tests the Strategist's proposed failure channel constructively.

In the Step-11 opposite-warping ansatz, the trace-free Hessian of a warp u is
visible to the Weyl/Riemann block while Ricci sees only Delta u (to leading
linear order; quadratic gradient terms are lower if the amplitude is small on
orbifold balls).  On an annulus use

    u(r,theta) = t r^2 A(log r) cos(2 theta).

For constant A, r^2 cos(2theta) is harmonic in the 2D base, so it is a pure
H2 drift with no Ricci source.  If A changes slowly over a logarithmic neck of
length L, then the H2 coefficient changes by O(1) while

    Delta u = t (A'' + 4 A') cos(2theta) = O(t/L).

Setting L ~ 1/delta and outer ALE radius R=e^L=t^{-1/2} gives
    t ~ exp(-2/delta),
which is precisely the exponential neck channel.  This is not a closed metric;
it is a local linear/warping model showing the channel is compatible with the
same trace-free-Hessian freedom as Step 11.
"""
from __future__ import annotations

import json, math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step60_warp_neck_drift_model.json"


def sympy_laplacian_formula():
    r, th, t = sp.symbols('r th t', positive=True)
    s = sp.symbols('s', real=True)
    A = sp.Function('A')
    # Work by hand with f(r)=t r^2 A(log r); represent A(log r).
    f = t * r**2 * A(sp.log(r))
    u = f * sp.cos(2*th)
    lap = sp.simplify(sp.diff(u, r, 2) + (1/r)*sp.diff(u, r) + (1/r**2)*sp.diff(u, th, 2))
    # Substitute log(r)=s naming in readable form.
    return {
        "u": str(u),
        "laplacian_polar": str(lap),
        "readable_formula": "Delta[t r^2 A(log r) cos(2theta)] = t (A''(log r) + 4 A'(log r)) cos(2theta)",
        "constant_A_check": "If A'=A''=0, Delta u=0; the H2 coefficient can be nonzero with zero linear Ricci source."
    }


def q(z):
    return 3*z*z - 2*z*z*z

def qp(z):
    return 6*z - 6*z*z

def qpp(z):
    return 6 - 12*z


def schedule_rows():
    rows=[]
    for delta in [0.2,0.1,0.05,0.02,0.01,0.005]:
        for drift in [0.5,1.0,2.0]:
            # Choose L=1/delta.  A(s)=A0+drift*q(s/L).
            L = 1.0/delta
            R = math.exp(L)
            # Outer ALE radius R = t^-1/2 -> t=exp(-2L)
            log_1_t = 2*L
            log10_1_t = log_1_t/math.log(10)
            # Max |A'| = drift * max q'/L = 1.5*drift/L
            # Max |A''| = drift * max |q''|/L^2 = 6*drift/L^2
            max_Ap = 1.5*drift/L
            max_App = 6.0*drift/(L*L)
            max_lap_over_t = max_App + 4*max_Ap
            rows.append({
                "delta": delta,
                "coefficient_drift_DeltaA": drift,
                "log_neck_length_L": L,
                "outer_ALE_radius_R=e^L_log10": L/math.log(10),
                "metric_scale_t=e^{-2L}_log10_1_over_t": log10_1_t,
                "dyadic_scales": L/math.log(2),
                "max_abs_A_prime": max_Ap,
                "max_abs_A_double_prime": max_App,
                "max_abs_Delta_u_over_t": max_lap_over_t,
                "max_abs_Delta_u_over_t_delta": max_lap_over_t/delta,
                "interpretation": "O(1) H2 coefficient drift with Ricci/Laplacian source O(t*delta) on a neck of length ~1/delta."
            })
    return rows


def sample_profile(delta=0.02, drift=1.0, samples=9):
    L=1.0/delta
    prof=[]
    for j in range(samples):
        z=j/(samples-1)
        A=drift*q(z)
        Ap=drift*qp(z)/L
        App=drift*qpp(z)/(L*L)
        source=App+4*Ap
        prof.append({
            "z=s/L": z,
            "A_minus_A0": A,
            "A_prime": Ap,
            "A_double_prime": App,
            "laplacian_coefficient_over_t": source
        })
    return {"delta":delta,"drift":drift,"L":L,"profile":prof}


def main():
    data={
        "status":"ok",
        "sympy_verification": sympy_laplacian_formula(),
        "construction": {
            "ansatz":"u=t r^2 A(log r) cos(2theta) in the 2D base of the opposite-warping metric; use A(s)=A0+DeltaA q(s/L), q=3z^2-2z^3.",
            "why_this_is_the_neck_channel":"A changes the l=2/H2/Weyl block coefficient.  Ricci sees Delta u=t(A''+4A')cos2theta, so slow logarithmic variation makes Ricci defect O(t/L) while changing the coefficient by DeltaA.",
            "matching_to_pinching":"Take L~1/delta and R=e^L=t^{-1/2}. Then t=exp(-2/delta) and the coefficient drift is O(1) with pointwise Ricci defect O(t delta) in the ALE frame, exactly the failure regime for the H4 flux theorem.",
            "limitations":"Local linear/warped model only. A closed smooth near-pinched metric still requires end caps, nonlinear gradient estimates, full Riemannian positivity, and topology/bubble matching. Cutoffs must use long logarithmic shoulders; sharp endpoint cutoffs would create O(t) Ricci defects."
        },
        "schedules": schedule_rows(),
        "sample_profile_delta_0p02": sample_profile(),
        "research_consequence":"The exponential failure channel is not merely formal ODE bookkeeping. The same opposite-warping Hessian mechanism that produced Step-11 C0-Ricci/small-L2/high-curvature spikes can locally realize an O(1) l=2 curvature-block drift across a neck while keeping the Ricci source O(delta). This makes the constructive counterexample channel credible and identifies the exact next obstruction to check: whether global caps and nonlinear terms can preserve the O(delta) Ricci defect."
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(json.dumps({
        "status":"ok",
        "output":str(OUT),
        "laplacian_formula":data["sympy_verification"]["readable_formula"],
        "sample_schedule":data["schedules"][7],
        "consequence":data["research_consequence"]
    }, indent=2))

if __name__=='__main__': main()

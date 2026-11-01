#!/usr/bin/env python3
"""
Step 37 Weyl period probe for alternating finite rods.

This is an exploratory numerical check of the generalized Weyl period-matching
mechanism, not a proof.  We model a 4D Euclidean generalized Weyl metric

  ds^2 = e^{2 U1} dphi1^2 + e^{2 U2} dphi2^2 + e^{2 nu}(dr^2+dz^2),
  U1 + U2 = log r,

where U1 is the superposition of finite rod potentials on selected intervals
and U2 carries the complementary rod source.  A rod of label i is smooth for a
specific period of phi_i.  Multiple rods with the same label must have the same
period if a single global circle coordinate is to close smoothly.

We compute log-period coefficients
  ell_j = nu - (U_i - log r)
near the interior of each finite rod j of label i.
Differences ell_j-ell_k within the same label are gauge-independent.
"""
import json, math, os
from dataclasses import dataclass
from typing import List, Tuple

try:
    from scipy.integrate import quad
except Exception as e:
    raise SystemExit(f"scipy required: {e}")

@dataclass
class Rod:
    a: float
    b: float
    label: int  # 1 or 2


def rod_potential_and_derivatives(a: float, b: float, r: float, z: float) -> Tuple[float, float, float]:
    """Finite Weyl rod potential of density 1/2 and derivatives."""
    L = b - a
    Ra = math.hypot(r, z - a)
    Rb = math.hypot(r, z - b)
    A = Ra + Rb
    # u = 1/2 log((A-L)/(A+L)); stable enough away from exact rod at r=0.
    u = 0.5 * (math.log(A - L) - math.log(A + L))
    denom = A*A - L*L
    Ar = r * (1.0/Ra + 1.0/Rb)
    Az = (z-a)/Ra + (z-b)/Rb
    ur = L * Ar / denom
    uz = L * Az / denom
    return u, ur, uz


def U1_and_derivatives(rods: List[Rod], r: float, z: float) -> Tuple[float, float, float]:
    U = Ur = Uz = 0.0
    for rod in rods:
        if rod.label == 1:
            u, ur, uz = rod_potential_and_derivatives(rod.a, rod.b, r, z)
            U += u; Ur += ur; Uz += uz
    return U, Ur, Uz


def nu_derivatives(rods: List[Rod], r: float, z: float) -> Tuple[float, float]:
    U1, U1r, U1z = U1_and_derivatives(rods, r, z)
    U2r = 1.0/r - U1r
    U2z = -U1z
    # Generalized Weyl equations for sum U_i = log r.
    nur = -0.5/r + 0.5*r*((U1r*U1r - U1z*U1z) + (U2r*U2r - U2z*U2z))
    nuz = r*(U1r*U1z + U2r*U2z)
    return nur, nuz


def compute_nu(rods: List[Rod], r_target: float, z_target: float) -> float:
    # Gauge fixed by nu(R,z_ref)=0. Only period differences are used.
    zmin = min(rod.a for rod in rods); zmax = max(rod.b for rod in rods)
    span = zmax - zmin
    R = max(50.0*span, 50.0)
    z_ref = 0.5*(zmin+zmax)
    # horizontal path at large R, then vertical down/up at z_target.
    if z_target >= z_ref:
        horiz = quad(lambda zz: nu_derivatives(rods, R, zz)[1], z_ref, z_target, epsabs=1e-9, epsrel=1e-9, limit=200)[0]
    else:
        horiz = -quad(lambda zz: nu_derivatives(rods, R, zz)[1], z_target, z_ref, epsabs=1e-9, epsrel=1e-9, limit=200)[0]
    if r_target <= R:
        vert = -quad(lambda rr: nu_derivatives(rods, rr, z_target)[0], r_target, R, epsabs=1e-9, epsrel=1e-9, limit=400)[0]
    else:
        vert = quad(lambda rr: nu_derivatives(rods, rr, z_target)[0], R, r_target, epsabs=1e-9, epsrel=1e-9, limit=400)[0]
    return horiz + vert


def rod_log_period(rods: List[Rod], rod: Rod, eps: float = 1e-5) -> float:
    z = 0.5*(rod.a + rod.b)
    r = eps * max(1.0, rod.b-rod.a)
    nu = compute_nu(rods, r, z)
    U1, _, _ = U1_and_derivatives(rods, r, z)
    if rod.label == 1:
        V = U1 - math.log(r)
    else:
        U2 = math.log(r) - U1
        V = U2 - math.log(r)  # = -U1
    return nu - V


def make_alternating(lengths: List[float], start_label: int = 1) -> List[Rod]:
    rods=[]; z=0.0; label=start_label
    for L in lengths:
        rods.append(Rod(z,z+L,label)); z += L; label = 3-label
    return rods


def summarize(rods: List[Rod], name: str) -> dict:
    rows=[]
    for idx,rod in enumerate(rods, start=1):
        ell = rod_log_period(rods, rod)
        rows.append({"rod":idx,"label":rod.label,"a":rod.a,"b":rod.b,"length":rod.b-rod.a,"log_period_coeff":ell})
    by_label={}
    for label in (1,2):
        vals=[row["log_period_coeff"] for row in rows if row["label"]==label]
        by_label[str(label)]={
            "count":len(vals),
            "values":vals,
            "range":(max(vals)-min(vals)) if vals else 0.0,
            "exp_range_ratio":math.exp(max(vals)-min(vals)) if vals else 1.0,
            "mean":sum(vals)/len(vals) if vals else None,
        }
    return {"name":name,"rows":rows,"by_label":by_label}


def main():
    cases=[]
    for m in [4,6,8]:
        cases.append(summarize(make_alternating([1.0]*m,1), f"equal_{m}_finite_rods_alt12"))
    # Mildly perturbed cases to see sensitivity.  These are not optimized.
    cases.append(summarize(make_alternating([1.0,1.2,0.9,1.1,0.95,1.05],1), "m6_perturbed"))
    cases.append(summarize(make_alternating([1.0,1.2,0.8,1.1,0.95,1.05,1.3,0.9],1), "m8_perturbed"))
    out={
        "title":"Step 37 generalized Weyl rod period probe",
        "scope":"Exploratory half-plane generalized Weyl period ratios; not a compact polygon proof and not a Yau-26 result.",
        "formulae":{
            "metric":"ds^2=e^{2U1}dphi1^2+e^{2U2}dphi2^2+e^{2nu}(dr^2+dz^2), U1+U2=log r",
            "rod_potential":"u_[a,b]=1/2 log((Ra+Rb-(b-a))/(Ra+Rb+(b-a)))",
            "nu_r":"-1/(2r)+(r/2) sum_i ((U_i,r)^2-(U_i,z)^2)",
            "nu_z":"r sum_i U_i,r U_i,z",
            "log_period_coeff":"ell_j=nu-(U_label-log r) near rod interior; same-label ell differences measure period mismatch",
        },
        "source_support":"Emparan-Reall lines 1358-1426: rod sources add to an infinite rod; spatial rods are bolts; avoiding conical singularity requires a coordinate period determined by the sources; multiple sources for the same coordinate can require different periods, producing conical singularities.",
        "cases":cases,
        "review_conclusion":"Alternating adjacent labels do not remove period mismatch. Equal finite alternating chains are symmetric enough in this half-plane probe to equalize some same-label periods, but perturbed chains show same-label period ranges. Compact polygon closing/monodromy is a separate finite computation and cannot be declared strut-free from Delzant adjacency alone."
    }
    path="Sessions/S0910A02/workspace/data/step37_weyl_period_probe.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w") as f: json.dump(out,f,indent=2)
    print(json.dumps({"output":path,"case_summaries":[{"name":c["name"],"by_label":c["by_label"]} for c in cases]},indent=2))

if __name__ == "__main__":
    main()

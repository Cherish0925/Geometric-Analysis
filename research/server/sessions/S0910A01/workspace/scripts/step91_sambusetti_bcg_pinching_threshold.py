#!/usr/bin/env python3
"""Step 91: quantitative BCG/Sambusetti threshold for N#N.

Let N be a closed real-hyperbolic 4-manifold with sectional curvature -1,
Vol(N)=4*pi^2*chi(N)/3.  Let M=N#N.  There is a degree-two map M->N by mapping
both punctured summands with degree one and collapsing the neck.

For any metric g on M with Ric_g >= -3(1+eps) g, Bishop gives h(g)<=3*sqrt(1+eps).
BCG applied to the degree-two map gives Vol(g)>=2 Vol(N)/(1+eps)^2.

If in addition all Ricci eigenvalues lie in [-3(1+eps), -3(1-eps)] and
eps<=1/3, then the Ricci part of Chern--Gauss--Bonnet satisfies
s^2/24-|E|^2/2 = s^2/6-|Ric|^2/2 >= 6(1-eps)^2.
The proof writes r_i=-3 x_i, x_i in [1-eps,1+eps]; the resulting quadratic is
(3/2)[(sum x_i)^2 - 3 sum x_i^2], concave in each x_i, so its minimum on the box
is at a vertex, and for eps<=1/3 the minimum vertex is x_i=1-eps for all i. Since
8*pi^2 chi(M)=int(|W|^2+s^2/24-|E|^2/2), this gives
Vol(g)<=2 Vol(N)*(1-1/chi(N))/(1-eps)^2.

The two inequalities are incompatible when ((1-eps)/(1+eps))^2 > 1-1/chi(N).
"""
import json, math, pathlib

DATA_DIR = pathlib.Path("Sessions/S0910A01/workspace/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def eps_threshold(chi):
    a = math.sqrt(1.0 - 1.0/chi)
    return (1.0 - a)/(1.0 + a)

rows=[]
for chi in [2,3,4,5,10,25,50,100,500,1000]:
    eps=eps_threshold(chi)
    rows.append({
        "chi_N": chi,
        "epsilon_relative_threshold": eps,
        "absolute_delta_threshold_for_|Ric+3g|": 3*eps,
        "asymptotic_chi_times_epsilon": chi*eps,
        "asymptotic_chi_times_delta": 3*chi*eps,
    })

results={
    "step":91,
    "scope":"BCG plus Chern-Gauss-Bonnet quantitative obstruction for near-negative pinching on M=N#N",
    "assumptions":{
        "N":"closed oriented real-hyperbolic 4-manifold, sec=-1, Ric=-3g0",
        "M":"connected sum N#N with degree-two map to N",
        "pinching":"-3(1+eps) g <= Ric_g <= -3(1-eps) g with 0<eps<=1/3 (the final threshold is always in this range for chi_N>=2)",
    },
    "topology":{
        "Vol_N":"4*pi^2*chi_N/3",
        "chi_M":"2*chi_N-2",
        "tau_M":0,
    },
    "BCG_lower_volume":"Vol_g >= 2 Vol_N/(1+eps)^2",
    "CGB_upper_volume":"Vol_g <= 2 Vol_N*(1-1/chi_N)/(1-eps)^2, using s^2/24-|E|^2/2=s^2/6-|Ric|^2/2 >= 6(1-eps)^2 for eps<=1/3",
    "incompatibility_condition":"((1-eps)/(1+eps))^2 > 1 - 1/chi_N",
    "epsilon_threshold_exact":"eps < (1-sqrt(1-1/chi_N))/(1+sqrt(1-1/chi_N)) = 1/(4 chi_N)+O(chi_N^-2)",
    "threshold_table":rows,
    "interpretation":[
        "The entropy lower bound used here applies to every metric through BCG and the degree-two map, while the CGB upper volume uses two-sided near-negative Ricci pinching plus eps<=1/3, not the Einstein equation.",
        "Therefore any construction of metrics on N#N with |Ric+3g|_op <= 3 eps and eps=o(1/chi_N) is impossible; along a varying counterexample sequence the defect may still tend to zero, but for each N it must stay above the displayed ~3/(4 chi_N) lower margin.",
        "This gives a quantitative obstruction to the proposed N#N near-negative branch, not a positive construction, not evidence for the exact optimal rate, and not a full Yau-26 refutation."
    ]
}

out=DATA_DIR/"step91_sambusetti_bcg_pinching_threshold.json"
with open(out,"w") as f:
    json.dump(results,f,indent=2)
print(json.dumps(results,indent=2))
print(f"Wrote {out}")

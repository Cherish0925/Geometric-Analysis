"""Sampled Hamilton--Jacobi probe for the non-round opening problem.

This does NOT certify a state-space inequality.  It derives the exact control-
minimized Hamiltonian for V=b_+ + phi(q,eta), evaluates the charge slack m
and coefficient K on selected cap -1 optimizer trajectories, and solves finite
sample convex programs for low-degree phi.  The purpose is to locate a region
that resists a q/eta-only certificate before interval work.

Run from workspace:
  PYTHONDONTWRITEBYTECODE=1 python scripts/hj_qeta_probe.py
Output: data/saturation_control/hj_qeta_probe.json
"""
from __future__ import annotations

import json
from pathlib import Path

import casadi as ca
import numpy as np

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
OUT = WORK / "data" / "saturation_control" / "hj_qeta_probe.json"
FILES = [
    WORK / "data/saturation_control/eps0p0625_N60_ch_bpmax_m1.json",
    WORK / "data/saturation_control/eps0p03125_N80_ch_bpmax_m1_e32.json",
    WORK / "data/saturation_control/eps0p015625_N80_ch_bpmax_m1_e64.json",
]

# Import the exact session transcription without executing its CLI.
import sys
sys.path.insert(0, str(HERE))
import saturation_optimal_control as sat


def build_functions():
    X = ca.MX.sym("X", 5)
    U0 = ca.MX.zeros(3, 1)
    b = sat.bplus_ca(X)
    f0 = sat.f_rhs(X, U0)
    gb = ca.gradient(b, X)
    h0 = ca.dot(gb, f0)
    # Supremum over controls of db/dtau - L.
    bp, bc, be = gb[2], gb[3], gb[4]
    h0 = h0 + bp**2/3 + 1.5*bc**2 + 2*(bc/2-be)**2
    m = -h0
    Aeta = f0[4]
    K = Aeta - 2*bc + 4*be
    q = -3*ca.log(X[1])
    return ca.Function("hj_fields", [X], [q, m, K, b, gb, f0])


def records(fun):
    rows = []
    by_file = []
    for path in FILES:
        rec = json.loads(path.read_text())
        xs = np.asarray(rec["X"], dtype=float)
        one = []
        for i, x in enumerate(xs):
            q, m, K, b, gb, f0 = fun(x)
            r = {
                "file": path.name,
                "index": i,
                "q": float(q),
                "eta": float(x[4]),
                "x": float(x[0]),
                "z": float(x[1]),
                "p": float(x[2]),
                "chi": float(x[3]),
                "m": float(m),
                "K": float(K),
                "bplus": float(b),
            }
            one.append(r); rows.append(r)
        desc = [r for r in one if r["eta"] < -1e-8]
        ratios = [r["m"]/(-r["eta"]) for r in desc]
        j = int(np.argmin(ratios)) if ratios else -1
        by_file.append({
            "file": path.name,
            "entry_q": one[0]["q"],
            "entry_eta": one[0]["eta"],
            "min_m": min(r["m"] for r in one),
            "min_q_slope_capacity": ratios[j] if ratios else None,
            "resisting_row": desc[j] if ratios else None,
        })
    return rows, by_file


def sampled_convex_program(rows, endpoint_pairs, objective="phi_gain"):
    try:
        import cvxpy as cp
    except Exception as exc:  # pragma: no cover
        return {"status": "cvxpy unavailable", "error": str(exc)}

    # phi=-a q+b q^2+c q eta+d eta^2.  phi(0,0)=0 automatically.
    th = cp.Variable(4)
    a, b, c, d = th[0], th[1], th[2], th[3]
    delta = cp.Variable()
    cons = [cp.norm(th, 2) <= 10]
    # Tiny negative m may occur from floating cancellation; require the exact
    # inequality against max(m,0) only for this sampled route probe.
    for r in rows:
        q, eta, K, m = r["q"], r["eta"], r["K"], max(r["m"], 0.0)
        phiq = -a + 2*b*q + c*eta
        phie = c*q + 2*d*eta
        cons.append(eta*phiq + K*phie + 2*cp.square(phie) <= m + 1e-10)
    def phi(r):
        q,e=r["q"],r["eta"]
        return -a*q+b*q*q+c*q*e+d*e*e
    for start, stop in endpoint_pairs:
        fixed = (stop["bplus"]-start["bplus"]) if objective == "total_bound" else 0.0
        cons.append(fixed + phi(stop) - phi(start) >= delta)
    prob = cp.Problem(cp.Maximize(delta), cons)
    attempts = []
    for solver in ["CLARABEL", "SCS"]:
        try:
            prob.solve(solver=solver, verbose=False)
            attempts.append({"solver": solver, "status": prob.status, "value": prob.value})
            if prob.status in ("optimal", "optimal_inaccurate"):
                break
        except Exception as exc:
            attempts.append({"solver": solver, "status": "error", "error": str(exc)})
    out = {"attempts": attempts, "status": prob.status, "delta": prob.value}
    if th.value is not None:
        out["coefficients_a_b_c_d"] = np.asarray(th.value).tolist()
        # Evaluate the actual sampled residual without clipping m.
        vals=[]
        aa,bb,cc,dd=np.asarray(th.value,dtype=float)
        for r in rows:
            q,e,K,m=r["q"],r["eta"],r["K"],r["m"]
            pq=-aa+2*bb*q+cc*e; pe=cc*q+2*dd*e
            vals.append(e*pq+K*pe+2*pe*pe-m)
        out["max_true_sample_residual"] = max(vals)
    return out


def main():
    fun = build_functions()
    rows, by_file = records(fun)
    # For each trajectory, challenge the certificate only on the descending
    # swap segment from q maximum to the first later node where q <= .70.
    # This avoids demanding a b_+-based certificate through the exact-CH
    # terminal region where b_+ becomes very negative and a different channel
    # should be used.
    endpoint_pairs=[]; swap_rows=[]
    for f in FILES:
        one=[r for r in rows if r["file"] == f.name]
        imax=max(range(len(one)), key=lambda i: one[i]["q"])
        istop=next((i for i in range(imax,len(one)) if one[i]["q"] <= .70), len(one)-1)
        endpoint_pairs.append((one[imax], one[istop]))
        swap_rows.extend(one[imax:istop+1])

    descending = [r for r in rows if r["eta"] < -1e-8]
    j = int(np.argmin([r["m"]/(-r["eta"]) for r in descending]))
    rr = descending[j]
    amax = rr["m"]/(-rr["eta"])
    affine_gains = [{"file": r["file"], "gain_at_common_amax": amax*r["entry_q"]}
                    for r in by_file]

    # Bin the sampled q-only slope envelope.  This is only a sampled upper
    # capacity, not a state-space bound, and empty bins are omitted.
    qmax = max(r["q"] for r in rows)
    edges = np.linspace(0, qmax, 25)
    bins=[]
    for lo,hi in zip(edges[:-1],edges[1:]):
        rs=[r for r in descending if lo <= r["q"] < hi]
        if rs:
            vals=[r["m"]/(-r["eta"]) for r in rs]
            k=int(np.argmin(vals))
            bins.append({"q_range":[float(lo),float(hi)],"sample_capacity":float(vals[k]),
                         "resisting_row":rs[k]})

    out = {
        "meaning": "finite-sample route probe only; no interval/state-space certificate",
        "exact_HJ": "eta*phi_q + K*phi_eta + 2*phi_eta^2 <= m, with m=-sup_U(dbplus/dtau-L), K=Aeta-2*b_chi+4*b_eta",
        "by_file": by_file,
        "global_affine_q": {"a_max_on_samples": amax, "resisting_row": rr,
                            "entry_gains": affine_gains},
        "sampled_q_capacity_bins": bins,
        "swap_endpoint_pairs": endpoint_pairs,
        "quadratic_q_eta_phi_gain_on_swap": sampled_convex_program(swap_rows, endpoint_pairs, "phi_gain"),
        "quadratic_q_eta_total_bound_on_swap": sampled_convex_program(swap_rows, endpoint_pairs, "total_bound"),
        "m_range": [min(r["m"] for r in rows), max(r["m"] for r in rows)],
        "K_range": [min(r["K"] for r in rows), max(r["K"] for r in rows)],
    }
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))
    print("output", OUT)


if __name__ == "__main__":
    main()

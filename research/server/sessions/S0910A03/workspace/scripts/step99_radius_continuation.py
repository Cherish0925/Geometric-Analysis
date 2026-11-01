"""Step 99: Radius continuation with Raychaudhuri cost decomposition.

For each R, build the best quintic jet-preserving baseline, compute the full 
Ricci residual with all ten blocks, and decompose costs:

  Normal:     E_rr (constrained by Raychaudhuri identity)
  Mixed:      E_ri (Codazzi block)  
  Tangential: E_T  (orbit-shape + area + charge)

Also compute the exact normal projection integral:
  ∫₀ᴿ cosh²r(-E_rr)dr = 3cosh²R(1-tanh R) + ∫₀ᴿ cosh²r[|W°|²+u²/3]dr

This separates the compulsory length-dependent normal cost from the
tangential/mixed costs that may decrease with R.
"""
from __future__ import annotations
import importlib.util, json, math, sys
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

SESSION = Path(__file__).resolve().parents[2]

# Import the Step 98 full-matrix evaluator
spec = importlib.util.spec_from_file_location(
    "step98_eval", SESSION / "workspace/scripts/step98_full_matrix_joint_transition.py")
fmat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fmat)


def raychaudhuri_floor(R: float) -> float:
    """Minimum δ for H: [0,0]→[R,3] under H'≤3+δ-H²/3."""
    def f(k): return k * math.tanh(k * R) - 1.0
    if f(1.0) >= 0: return 0.0
    k_max = max(2.0, 2.0 / R)
    while f(k_max) < 0: k_max *= 2
    k_sol = brentq(f, 1.0, k_max, xtol=1e-14)
    return 3.0 * (k_sol**2 - 1.0)


def normal_projection_integral(r, H_avg, W2_avg, Err_avg, R):
    """Evaluate the exact Raychaudhuri integral identity on s-averaged quantities.
    
    Uses the minimal center form: H(0)=0.
    All inputs are 1D arrays indexed by r.
    """
    u = H_avg - 3.0 * np.tanh(r)
    Wcirc_sq = W2_avg - H_avg**2 / 3.0
    cosh2 = np.cosh(r)**2
    
    # Trapezoidal integration
    dr = np.diff(r)
    def trap(f):
        return np.sum(0.5 * (f[:-1] + f[1:]) * dr)
    
    lhs = trap(cosh2 * (-Err_avg))
    shear = trap(cosh2 * np.maximum(Wcirc_sq, 0))
    mismatch = trap(cosh2 * u**2 / 3.0)
    endpoint = 3.0 * math.cosh(R)**2 * (1.0 - math.tanh(R))
    
    return {
        "weighted_neg_Err": float(lhs),
        "endpoint_cost": float(endpoint),
        "shear_integral": float(shear),
        "mismatch_integral": float(mismatch),
        "rhs_total": float(endpoint + shear + mismatch),
        "identity_residual": float(abs(lhs - endpoint - shear - mismatch)),
    }


def run_one_R(R, ns, nr, wind, S, Qmax, sign=+1):
    """Build baseline quintic trial at given R, compute full residual decomposition."""
    geom = fmat.center_geometry(ns, wind, S, Qmax)
    
    # Build quintic baseline (theta=0)
    fields, _ = fmat.matrix_basis(geom["s"], wind, richer=False)
    p = len(fields) * 1  # radial_count=1
    theta = np.zeros(p)
    
    r, Dr, D2r, q, names = fmat.build_half(geom, R, nr, sign, theta, 1, False)
    
    # Override endpoint jets for accuracy
    qn, qnn = fmat.normal_derivatives(q, Dr, D2r)
    qn[0] = 2.0 * sign * geom["k0"]
    qnn[0] = 2.0 * (geom["ric0"] + 3.0 * geom["q0"] + 2.0 * np.einsum(
        "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
    qn[-1] = 2.0 * q[-1]
    qnn[-1] = 4.0 * q[-1]
    
    # Full residual
    res = fmat.full_residual(q, Dr, D2r, qn_override=qn, qnn_override=qnn)
    
    # Extract block decomposition
    op = res["op"]  # (nr, ns)
    Enn = res["Enn"]  # (nr, ns)
    mom = res["mom"]  # (nr, ns, 3) -- Codazzi
    ET = res["ET"]    # (nr, ns, 3, 3) -- tangential
    H = res["H"]      # (nr, ns) -- mean curvature
    W2 = res["W2"]    # (nr, ns) -- tr(W^2)
    
    # Compute tangential operator norm at each point
    ET_op = np.zeros((nr, ns))
    for a in range(nr):
        for b in range(ns):
            qi_local = np.linalg.inv(q[a, b])
            # E_T^sharp = q^{-1} E_T
            ET_sharp = qi_local @ ET[a, b]
            # eigenvalues of the symmetric part
            ET_sym = 0.5 * (ET_sharp + ET_sharp.T)
            ET_op[a, b] = np.max(np.abs(np.linalg.eigvalsh(ET_sym)))
    
    # Codazzi/mixed norm: ||mom||_q = sqrt(g^{ij} mom_i mom_j) but in our
    # orthonormal frame it's the Euclidean norm of E_{0i} with q-metric
    mom_op = np.zeros((nr, ns))
    for a in range(nr):
        for b in range(ns):
            qi_local = np.linalg.inv(q[a, b])
            mom_op[a, b] = np.sqrt(mom[a, b] @ qi_local @ mom[a, b])
    
    # s-averaged quantities for the Raychaudhuri projection
    r_1d = r[:, 0] if r.ndim > 1 else (R * fmat.chebyshev_lobatto_01(nr)[0])
    # r is shape (nr,) from the Lobatto grid
    H_avg = np.mean(H, axis=1)
    W2_avg = np.mean(W2, axis=1)
    Err_avg = np.mean(Enn, axis=1)
    
    npi = normal_projection_integral(r_1d, H_avg, W2_avg, Err_avg, R)
    
    # Collect results
    result = {
        "R": R,
        "nr": nr,
        "ns": ns,
        "delta_min": raychaudhuri_floor(R),
        "total_operator_sup": float(np.max(op)),
        "total_operator_sup_location": {
            "r_index": int(np.unravel_index(np.argmax(op), op.shape)[0]),
            "s_index": int(np.unravel_index(np.argmax(op), op.shape)[1]),
            "r_value": float(r_1d[np.unravel_index(np.argmax(op), op.shape)[0]]),
        },
        "block_decomposition": {
            "Enn_sup": float(np.max(np.abs(Enn))),
            "Enn_center": float(np.max(np.abs(Enn[0]))),
            "Enn_end": float(np.max(np.abs(Enn[-1]))),
            "mom_sup": float(np.max(mom_op)),
            "mom_center": float(np.max(mom_op[0])),
            "mom_end": float(np.max(mom_op[-1])),
            "ET_op_sup": float(np.max(ET_op)),
            "ET_op_center": float(np.max(ET_op[0])),
            "ET_op_end": float(np.max(ET_op[-1])),
        },
        "normal_projection": npi,
        "H_center": float(np.mean(H[0])),
        "H_end": float(np.mean(H[-1])),
        "H_center_range": [float(np.min(H[0])), float(np.max(H[0]))],
        "H_end_range": [float(np.min(H[-1])), float(np.max(H[-1]))],
        "W2_center_avg": float(np.mean(W2[0])),
        "minimum_q_eigenvalue": float(np.min(res["mineig_q"])),
        # Ratio of actual to floor
        "ratio_actual_to_floor": float(np.max(op)) / max(raychaudhuri_floor(R), 1e-20),
        # End residual from exterior attachment
        "end_residual": float(np.max(op[-1])),
    }
    
    # Radial profile of s-averaged operator norm
    profile = []
    for a in range(nr):
        profile.append({
            "r": float(r_1d[a]),
            "op_avg": float(np.mean(op[a])),
            "op_max": float(np.max(op[a])),
            "Enn_avg": float(np.mean(np.abs(Enn[a]))),
            "mom_avg": float(np.mean(mom_op[a])),
            "ET_avg": float(np.mean(ET_op[a])),
            "H_avg": float(np.mean(H[a])),
        })
    result["radial_profile"] = profile
    
    return result


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ns", type=int, default=64)
    ap.add_argument("--nr", type=int, default=35)
    ap.add_argument("--wind", type=int, default=2)
    ap.add_argument("--S", type=float, default=1.0)
    ap.add_argument("--Qmax", type=float, default=0.5)
    args = ap.parse_args()
    
    Rs = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]
    all_results = []
    
    print(f"{'R':>5} {'delta_min':>10} {'op_sup':>10} {'ratio':>8} "
          f"{'Enn_sup':>10} {'mom_sup':>10} {'ET_sup':>10} {'endpt':>10} {'posdef':>8}")
    
    for R in Rs:
        # Scale nr with R to maintain physical resolution
        nr = max(args.nr, int(15 * R) + 5)
        try:
            res = run_one_R(R, args.ns, nr, args.wind, args.S, args.Qmax)
            all_results.append(res)
            bd = res["block_decomposition"]
            print(f"{R:5.1f} {res['delta_min']:10.6f} {res['total_operator_sup']:10.4f} "
                  f"{res['ratio_actual_to_floor']:8.1f} "
                  f"{bd['Enn_sup']:10.4f} {bd['mom_sup']:10.4f} "
                  f"{bd['ET_op_sup']:10.4f} {res['end_residual']:10.6f} "
                  f"{res['minimum_q_eigenvalue']:8.4f}")
        except Exception as e:
            print(f"{R:5.1f} FAILED: {e}")
            all_results.append({"R": R, "error": str(e)})
    
    # Summary table
    print("\n=== Normal Projection Integral ===")
    print(f"{'R':>5} {'wt(-Err)':>10} {'endpt_cost':>12} {'shear':>10} {'mismatch':>10} {'id_res':>10}")
    for res in all_results:
        if "error" in res:
            continue
        npi = res["normal_projection"]
        print(f"{res['R']:5.1f} {npi['weighted_neg_Err']:10.4f} "
              f"{npi['endpoint_cost']:12.4f} {npi['shear_integral']:10.4f} "
              f"{npi['mismatch_integral']:10.4f} {npi['identity_residual']:10.2e}")
    
    out = {"parameters": vars(args), "results": all_results}
    path = SESSION / "workspace/data/step99_radius_continuation.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

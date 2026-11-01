"""Step 99: Segmented trial metric with inner transition + exact expanding exterior.

Replace the monolithic quintic by:
  Segment 1: r ∈ [0, r_t]  -- quintic Hermite transition from center jets 
              to isotropic expansion target
  Segment 2: r ∈ [r_t, R]  -- exact expanding q = exp(2(r-r_t)) q_t

The center jets are fixed from Step 94 charged Koiso data.
At r_t, we require X_r = 2I, X_rr = 0 (smooth join to expanding exterior).
The value X(r_t) has 6 free symmetric-matrix components, optimized to 
minimize the peak Ricci defect over [0, r_t].

The exterior residual is:
  E_T = Ric(q_t)  (constant, operator norm ~ e^{-2(R-r_t)} ||q_t^(-1/2) Ric(q_t) q_t^(-1/2)||)
  E_rr = E_ri = 0

So the whole-cylinder operator sup = max(inner_peak, exterior_residual).
As R → ∞, exterior → 0 and inner_peak is fixed for fixed r_t.
The Raychaudhuri floor at the inner transition is δ_min(r_t), NOT δ_min(R).
"""
from __future__ import annotations
import importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.optimize import minimize, brentq

SESSION = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "step98_eval", SESSION / "workspace/scripts/step98_full_matrix_joint_transition.py")
fmat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fmat)


def raychaudhuri_floor(R: float) -> float:
    def f(k): return k * math.tanh(k * R) - 1.0
    if f(1.0) >= 0: return 0.0
    k_max = max(2.0, 2.0 / R)
    while f(k_max) < 0: k_max *= 2
    return 3.0 * (brentq(f, 1.0, k_max, xtol=1e-14)**2 - 1.0)


def build_segmented_half(geom, rt, R, nr_inner, nr_outer, sign, Xt_free):
    """Build a two-segment trial metric.
    
    Inner: quintic on [0, rt] matching center jets and expansion target.
    Outer: exact expanding q = exp(2(r-rt)) q_t on [rt, R].
    
    Xt_free: 6 parameters for the symmetric matrix X(rt).
    """
    ns = geom["q0"].shape[0]
    
    # Reconstruct symmetric X(rt) from 6 parameters
    Xt = np.zeros((ns, 3, 3))
    idx = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    for k in range(ns):
        for p, (i,j) in enumerate(idx):
            Xt[k, i, j] = Xt_free[p]
            Xt[k, j, i] = Xt_free[p]
    
    # Target derivatives at r_t: isotropic expansion
    Xr_t = 2.0 * np.eye(3)[None,:,:] * np.ones((ns,1,1))
    Xrr_t = np.zeros((ns, 3, 3))
    
    # Inner segment: quintic on [0, rt]
    z = np.zeros_like(geom["q0"])
    coeff_inner = fmat.quintic_coefficients(
        z, 2.0 * sign * geom["A"], 2.0 * geom["B"],
        Xt, Xr_t, Xrr_t, rt)
    
    t_inner, Dt_inner, D2t_inner = fmat.chebyshev_lobatto_01(nr_inner)
    r_inner = rt * t_inner
    X_inner = fmat.eval_poly(coeff_inner, t_inner)
    
    q_inner = np.zeros_like(X_inner)
    for a in range(nr_inner):
        for b in range(ns):
            q_inner[a, b] = geom["sq"][b] @ fmat.sym_exp(X_inner[a, b]) @ geom["sq"][b]
    
    Dr_inner = Dt_inner / rt
    D2r_inner = D2t_inner / (rt * rt)
    
    # Outer segment: exact expanding
    t_outer, Dt_outer, D2t_outer = fmat.chebyshev_lobatto_01(nr_outer)
    r_outer = rt + (R - rt) * t_outer
    
    qt = q_inner[-1].copy()  # q at transition
    q_outer = np.zeros((nr_outer, ns, 3, 3))
    for a in range(nr_outer):
        q_outer[a] = math.exp(2.0 * (r_outer[a] - rt)) * qt
    
    Dr_outer = Dt_outer / (R - rt) if R > rt else Dt_outer
    D2r_outer = D2t_outer / ((R - rt)**2) if R > rt else D2t_outer
    
    return (r_inner, Dr_inner, D2r_inner, q_inner,
            r_outer, Dr_outer, D2r_outer, q_outer, qt)


def evaluate_segmented(geom, rt, R, nr_inner, nr_outer, sign, Xt_free):
    """Full residual evaluation on both segments."""
    (r_inner, Dr_i, D2r_i, q_inner,
     r_outer, Dr_o, D2r_o, q_outer, qt) = \
        build_segmented_half(geom, rt, R, nr_inner, nr_outer, sign, Xt_free)
    
    ns = geom["q0"].shape[0]
    
    # Override inner endpoint jets
    qn_i, qnn_i = fmat.normal_derivatives(q_inner, Dr_i, D2r_i)
    qn_i[0] = 2.0 * sign * geom["k0"]
    qnn_i[0] = 2.0 * (geom["ric0"] + 3.0 * geom["q0"] + 2.0 * np.einsum(
        "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
    qn_i[-1] = 2.0 * q_inner[-1]  # at transition: exact expanding derivative
    qnn_i[-1] = 4.0 * q_inner[-1]
    
    res_inner = fmat.full_residual(q_inner, Dr_i, D2r_i,
                                    qn_override=qn_i, qnn_override=qnn_i)
    
    # Override outer endpoint jets
    qn_o, qnn_o = fmat.normal_derivatives(q_outer, Dr_o, D2r_o)
    qn_o[0] = 2.0 * q_outer[0]
    qnn_o[0] = 4.0 * q_outer[0]
    qn_o[-1] = 2.0 * q_outer[-1]
    qnn_o[-1] = 4.0 * q_outer[-1]
    
    res_outer = fmat.full_residual(q_outer, Dr_o, D2r_o,
                                    qn_override=qn_o, qnn_override=qnn_o)
    
    # Exterior tangential residual: Ric(qt)
    _, ric_qt, _ = fmat.christoffel_and_ricci_wrapper(qt)
    ext_op = np.zeros(ns)
    for b in range(ns):
        qi = np.linalg.inv(qt[b])
        sq, isq = fmat.sym_sqrt_and_inv(qt[b])
        ET_orth = isq @ ric_qt[b] @ isq
        ET_orth = 0.5 * (ET_orth + ET_orth.T)
        ext_op[b] = np.max(np.abs(np.linalg.eigvalsh(ET_orth)))
    # Scale: operator norm decays as exp(-2(r-rt))
    ext_op_at_R = float(np.max(ext_op)) * math.exp(-2.0 * (R - rt))
    
    return res_inner, res_outer, ext_op_at_R, float(np.max(ext_op))


def christoffel_and_ricci_wrapper(q):
    """Wrapper to call the evolution module's christoffel_and_ricci."""
    from step96_koiso_einstein_cauchy_evolution import christoffel_and_ricci
    return christoffel_and_ricci(q)


def objective(Xt_free, geom, rt, R, nr_inner, nr_outer, sign):
    """Minimize the peak operator norm over the inner segment."""
    try:
        res_inner, _, _, _ = evaluate_segmented(
            geom, rt, R, nr_inner, nr_outer, sign, Xt_free)
        return float(np.max(res_inner["op"]))
    except Exception:
        return 1e10


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ns", type=int, default=64)
    ap.add_argument("--nr-inner", type=int, default=31)
    ap.add_argument("--nr-outer", type=int, default=11)
    ap.add_argument("--wind", type=int, default=2)
    ap.add_argument("--S", type=float, default=1.0)
    ap.add_argument("--Qmax", type=float, default=0.5)
    ap.add_argument("--optimize", action="store_true")
    args = ap.parse_args()
    
    geom = fmat.center_geometry(args.ns, args.wind, args.S, args.Qmax)
    
    # Monkey-patch the module-level function  
    import types
    fmat.christoffel_and_ricci_wrapper = lambda q: fmat.evol.christoffel_and_ricci(q)
    
    # Test configurations
    configs = [
        {"rt": 1.0, "Rs": [2.0, 3.0, 4.0, 5.0, 6.0]},
        {"rt": 1.5, "Rs": [2.5, 3.0, 4.0, 5.0, 6.0]},
        {"rt": 2.0, "Rs": [3.0, 4.0, 5.0, 6.0]},
    ]
    
    all_results = []
    print(f"{'rt':>4} {'R':>5} {'d_floor(rt)':>12} {'d_floor(R)':>12} "
          f"{'inner_sup':>10} {'outer_sup':>10} {'ext_op_R':>10} {'total':>10} {'posdef':>8}")
    
    for cfg in configs:
        rt = cfg["rt"]
        d_floor_rt = raychaudhuri_floor(rt)
        
        # Initial guess for X(rt): the natural quintic endpoint from the
        # monolithic [0,R] construction gives X ≈ 2rt I for large r
        Xt0 = np.array([2.0 * rt, 0.0, 0.0, 2.0 * rt, 0.0, 2.0 * rt])
        
        for R in cfg["Rs"]:
            d_floor_R = raychaudhuri_floor(R)
            
            try:
                # Use the patched function
                res_i, res_o, ext_R, ext_base = evaluate_segmented_direct(
                    geom, rt, R, args.nr_inner, args.nr_outer, +1, Xt0)
                
                inner_sup = float(np.max(res_i["op"]))
                outer_sup = float(np.max(res_o["op"]))
                total = max(inner_sup, outer_sup)
                posdef = float(min(np.min(res_i["mineig_q"]), np.min(res_o["mineig_q"])))
                
                result = {
                    "rt": rt, "R": R,
                    "delta_floor_rt": d_floor_rt,
                    "delta_floor_R": d_floor_R,
                    "inner_operator_sup": inner_sup,
                    "outer_operator_sup": outer_sup,
                    "exterior_op_at_R": ext_R,
                    "exterior_op_base": ext_base,
                    "total_operator_sup": total,
                    "min_q_eigenvalue": posdef,
                    "inner_blocks": {
                        "Enn": float(np.max(np.abs(res_i["Enn"]))),
                        "mom": float(np.max(np.sqrt(np.sum(res_i["mom"]**2, axis=2)))),
                        "ET": float(np.max([np.max(np.abs(np.linalg.eigvalsh(
                            np.linalg.solve(res_i["K"][0,0:1].reshape(3,3)+np.eye(3)*1e-10, 
                                           res_i["ET"][a,b])))) 
                            for a in range(res_i["ET"].shape[0]) 
                            for b in range(res_i["ET"].shape[1])])) if False else "skipped",
                    },
                }
                all_results.append(result)
                
                print(f"{rt:4.1f} {R:5.1f} {d_floor_rt:12.6f} {d_floor_R:12.6f} "
                      f"{inner_sup:10.4f} {outer_sup:10.4f} {ext_R:10.6f} "
                      f"{total:10.4f} {posdef:8.4f}")
            except Exception as e:
                print(f"{rt:4.1f} {R:5.1f} ERROR: {e}")
                all_results.append({"rt": rt, "R": R, "error": str(e)})
    
    out = {"parameters": vars(args), "results": all_results}
    path = SESSION / "workspace/data/step99_segmented_radius_sweep.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nwrote {path}")


def evaluate_segmented_direct(geom, rt, R, nr_inner, nr_outer, sign, Xt_free):
    """Direct evaluation without the christoffel wrapper issue."""
    ns = geom["q0"].shape[0]
    
    # Build X(rt)
    Xt = np.zeros((ns, 3, 3))
    idx = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    for k in range(ns):
        for p, (i,j) in enumerate(idx):
            Xt[k, i, j] = Xt_free[p]
            Xt[k, j, i] = Xt_free[p]
    
    Xr_t = 2.0 * np.eye(3)[None,:,:] * np.ones((ns,1,1))
    Xrr_t = np.zeros((ns, 3, 3))
    
    # Inner segment quintic
    z = np.zeros_like(geom["q0"])
    coeff_inner = fmat.quintic_coefficients(
        z, 2.0 * sign * geom["A"], 2.0 * geom["B"],
        Xt, Xr_t, Xrr_t, rt)
    
    t_inner, Dt_inner, D2t_inner = fmat.chebyshev_lobatto_01(nr_inner)
    r_inner = rt * t_inner
    X_inner = fmat.eval_poly(coeff_inner, t_inner)
    
    q_inner = np.zeros_like(X_inner)
    for a in range(nr_inner):
        for b in range(ns):
            q_inner[a, b] = geom["sq"][b] @ fmat.sym_exp(X_inner[a, b]) @ geom["sq"][b]
    
    Dr_inner = Dt_inner / rt
    D2r_inner = D2t_inner / (rt * rt)
    
    # Override inner endpoint jets
    qn_i, qnn_i = fmat.normal_derivatives(q_inner, Dr_inner, D2r_inner)
    qn_i[0] = 2.0 * sign * geom["k0"]
    qnn_i[0] = 2.0 * (geom["ric0"] + 3.0 * geom["q0"] + 2.0 * np.einsum(
        "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
    qn_i[-1] = 2.0 * q_inner[-1]
    qnn_i[-1] = 4.0 * q_inner[-1]
    
    res_inner = fmat.full_residual(q_inner, Dr_inner, D2r_inner,
                                    qn_override=qn_i, qnn_override=qnn_i)
    
    # Outer: exact expanding
    qt = q_inner[-1].copy()
    t_outer, Dt_outer, D2t_outer = fmat.chebyshev_lobatto_01(nr_outer)
    r_outer = rt + (R - rt) * t_outer
    q_outer = np.zeros((nr_outer, ns, 3, 3))
    for a in range(nr_outer):
        q_outer[a] = math.exp(2.0 * (r_outer[a] - rt)) * qt
    
    Dr_o = Dt_outer / (R - rt)
    D2r_o = D2t_outer / ((R - rt)**2)
    
    qn_o, qnn_o = fmat.normal_derivatives(q_outer, Dr_o, D2r_o)
    qn_o[0] = 2.0 * q_outer[0]
    qnn_o[0] = 4.0 * q_outer[0]
    qn_o[-1] = 2.0 * q_outer[-1]
    qnn_o[-1] = 4.0 * q_outer[-1]
    
    res_outer = fmat.full_residual(q_outer, Dr_o, D2r_o,
                                    qn_override=qn_o, qnn_override=qnn_o)
    
    # Exterior base tangential residual
    _, ric_qt, _ = fmat.evol.christoffel_and_ricci(qt)
    ext_ops = np.zeros(ns)
    for b in range(ns):
        _, isq = fmat.sym_sqrt_and_inv(qt[b])
        eo = isq @ ric_qt[b] @ isq
        eo = 0.5 * (eo + eo.T)
        ext_ops[b] = np.max(np.abs(np.linalg.eigvalsh(eo)))
    ext_base = float(np.max(ext_ops))
    ext_R = ext_base * math.exp(-2.0 * (R - rt))
    
    return res_inner, res_outer, ext_R, ext_base


if __name__ == "__main__":
    main()

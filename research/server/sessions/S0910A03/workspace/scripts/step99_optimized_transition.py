"""Step 99: Optimized segmented transition with block decomposition.

Diagnose which Ricci block dominates the inner transition, then optimize 
X(r_t) and additional radial modes to reduce the peak operator norm.

Key insight from the Raychaudhuri floor: for a given r_t, the floor is
δ_min(r_t), and the exterior adds negligible cost for large R. So the 
matching problem reduces to: minimize the peak operator-norm defect over 
the inner transition [0, r_t] while preserving the center jets and smooth
join to the expanding exterior.
"""
from __future__ import annotations
import importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.optimize import minimize, brentq, differential_evolution

SESSION = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "step98_eval", SESSION / "workspace/scripts/step98_full_matrix_joint_transition.py")
fmat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fmat)


def raychaudhuri_floor(R):
    def f(k): return k * math.tanh(k * R) - 1.0
    if f(1.0) >= 0: return 0.0
    k_max = max(2.0, 2.0 / R)
    while f(k_max) < 0: k_max *= 2
    return 3.0 * (brentq(f, 1.0, k_max, xtol=1e-14)**2 - 1.0)


def build_inner_with_modes(geom, rt, nr, sign, Xt_free, mode_coeffs, n_radial_modes):
    """Build inner segment with X(rt) optimization + radial perturbation modes."""
    ns = geom["q0"].shape[0]
    
    # Reconstruct X(rt) from 6 params
    Xt = np.zeros((ns, 3, 3))
    idx = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    for k in range(ns):
        for p, (i,j) in enumerate(idx):
            Xt[k, i, j] = Xt_free[p]
            Xt[k, j, i] = Xt_free[p]
    
    # Target at rt: isotropic expansion
    Xr_t = 2.0 * np.eye(3)[None,:,:] * np.ones((ns,1,1))
    Xrr_t = np.zeros((ns, 3, 3))
    
    z = np.zeros_like(geom["q0"])
    coeff = fmat.quintic_coefficients(
        z, 2.0 * sign * geom["A"], 2.0 * geom["B"],
        Xt, Xr_t, Xrr_t, rt)
    
    t, Dt, D2t = fmat.chebyshev_lobatto_01(nr)
    r = rt * t
    X = fmat.eval_poly(coeff, t)
    
    # Add radial perturbation modes (vanish to 3rd order at both ends)
    if n_radial_modes > 0 and len(mode_coeffs) > 0:
        # Basis: t^3(1-t)^3, t^3(1-t)^3(2t-1), etc.
        shapes = fmat.normalized_radial_shapes(t, n_radial_modes)
        fields, _ = fmat.matrix_basis(geom["s"], int(geom["meta"]["wind"]), richer=False)
        n_per_mode = len(fields)
        p = 0
        for ir, sh in enumerate(shapes):
            for f in fields:
                if p < len(mode_coeffs):
                    X += mode_coeffs[p] * sh[:, None, None, None] * f[None, :, :, :]
                p += 1
    
    q = np.zeros_like(X)
    for a in range(nr):
        for b in range(ns):
            q[a, b] = geom["sq"][b] @ fmat.sym_exp(X[a, b]) @ geom["sq"][b]
    
    Dr = Dt / rt
    D2r = D2t / (rt * rt)
    
    # Override endpoint jets
    qn, qnn = fmat.normal_derivatives(q, Dr, D2r)
    qn[0] = 2.0 * sign * geom["k0"]
    qnn[0] = 2.0 * (geom["ric0"] + 3.0 * geom["q0"] + 2.0 * np.einsum(
        "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
    qn[-1] = 2.0 * q[-1]
    qnn[-1] = 4.0 * q[-1]
    
    res = fmat.full_residual(q, Dr, D2r, qn_override=qn, qnn_override=qnn)
    return r, q, res


def block_analysis(res, q):
    """Decompose the residual into normal, mixed, and tangential blocks."""
    nr, ns = res["op"].shape
    
    ET_op = np.zeros((nr, ns))
    for a in range(nr):
        for b in range(ns):
            qi = np.linalg.inv(q[a, b])
            ET_sharp = qi @ res["ET"][a, b]
            ET_sym = 0.5 * (ET_sharp + ET_sharp.T)
            ET_op[a, b] = np.max(np.abs(np.linalg.eigvalsh(ET_sym)))
    
    mom_norm = np.zeros((nr, ns))
    for a in range(nr):
        for b in range(ns):
            qi = np.linalg.inv(q[a, b])
            mom_norm[a, b] = np.sqrt(res["mom"][a, b] @ qi @ res["mom"][a, b])
    
    return {
        "Enn_sup": float(np.max(np.abs(res["Enn"]))),
        "ET_op_sup": float(np.max(ET_op)),
        "mom_sup": float(np.max(mom_norm)),
        "total_op_sup": float(np.max(res["op"])),
        # Peak locations
        "Enn_peak_r_frac": float(np.unravel_index(np.argmax(np.abs(res["Enn"])), res["Enn"].shape)[0] / max(nr-1,1)),
        "ET_peak_r_frac": float(np.unravel_index(np.argmax(ET_op), ET_op.shape)[0] / max(nr-1,1)),
        # s-averaged radial profiles
        "Enn_profile": [float(np.max(np.abs(res["Enn"][a]))) for a in range(nr)],
        "ET_profile": [float(np.max(ET_op[a])) for a in range(nr)],
        "H_profile": [float(np.mean(res["H"][a])) for a in range(nr)],
    }


def optimize_transition(geom, rt, nr, ns, sign, n_radial_modes, max_evals):
    """Optimize X(rt) and optional radial modes to minimize peak op norm."""
    
    # Parameters: 6 for X(rt) + n_radial_modes * n_fields for modes
    fields, _ = fmat.matrix_basis(geom["s"], int(geom["meta"]["wind"]), richer=False)
    n_fields = len(fields)
    n_mode_params = n_radial_modes * n_fields
    n_total = 6 + n_mode_params
    
    eval_count = [0]
    best_val = [1e20]
    best_x = [None]
    
    def obj(x):
        eval_count[0] += 1
        Xt_free = x[:6]
        mode_coeffs = x[6:] if n_mode_params > 0 else np.array([])
        try:
            _, q, res = build_inner_with_modes(
                geom, rt, nr, sign, Xt_free, mode_coeffs, n_radial_modes)
            val = float(np.max(res["op"]))
            if val < best_val[0]:
                best_val[0] = val
                best_x[0] = x.copy()
            return val
        except Exception:
            return 1e10
    
    # Initial guess
    x0 = np.zeros(n_total)
    x0[:6] = [2*rt, 0, 0, 2*rt, 0, 2*rt]  # isotropic X(rt) = 2rt I
    
    baseline = obj(x0)
    
    # Try Nelder-Mead for the 6 X(rt) parameters first
    if n_total <= 6:
        result = minimize(obj, x0, method='Nelder-Mead',
                         options={'maxfev': max_evals, 'xatol': 0.01, 'fatol': 0.1})
    else:
        result = minimize(obj, x0, method='Nelder-Mead',
                         options={'maxfev': max_evals, 'xatol': 0.01, 'fatol': 0.1})
    
    x_opt = best_x[0] if best_x[0] is not None else x0
    _, q_opt, res_opt = build_inner_with_modes(
        geom, rt, nr, sign, x_opt[:6], x_opt[6:] if n_mode_params > 0 else np.array([]),
        n_radial_modes)
    blocks = block_analysis(res_opt, q_opt)
    
    return {
        "baseline_op_sup": baseline,
        "optimized_op_sup": float(np.max(res_opt["op"])),
        "improvement_factor": baseline / max(float(np.max(res_opt["op"])), 1e-20),
        "evaluations": eval_count[0],
        "Xt_optimized": x_opt[:6].tolist(),
        "mode_coeffs_norm": float(np.linalg.norm(x_opt[6:])) if n_mode_params > 0 else 0.0,
        "blocks": blocks,
        "min_q_eigenvalue": float(np.min(res_opt["mineig_q"])),
    }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ns", type=int, default=64)
    ap.add_argument("--nr", type=int, default=35)
    ap.add_argument("--wind", type=int, default=2)
    ap.add_argument("--S", type=float, default=1.0)
    ap.add_argument("--Qmax", type=float, default=0.5)
    ap.add_argument("--max-evals", type=int, default=500)
    args = ap.parse_args()
    
    geom = fmat.center_geometry(args.ns, args.wind, args.S, args.Qmax)
    
    # First: diagnostic at rt=1.0 without optimization
    print("=== DIAGNOSTIC: Block decomposition at rt=1.0, baseline quintic ===")
    Xt0 = np.array([2.0, 0, 0, 2.0, 0, 2.0])
    r, q, res = build_inner_with_modes(geom, 1.0, args.nr, +1, Xt0, np.array([]), 0)
    blocks = block_analysis(res, q)
    print(f"  Total op sup: {blocks['total_op_sup']:.4f}")
    print(f"  Enn sup:      {blocks['Enn_sup']:.4f} (peak at r_frac={blocks['Enn_peak_r_frac']:.2f})")
    print(f"  ET op sup:    {blocks['ET_op_sup']:.4f} (peak at r_frac={blocks['ET_peak_r_frac']:.2f})")
    print(f"  mom sup:      {blocks['mom_sup']:.4f}")
    print(f"  Raychaudhuri floor: {raychaudhuri_floor(1.0):.4f}")
    print(f"  H(0)={blocks['H_profile'][0]:.4f}, H(end)={blocks['H_profile'][-1]:.4f}")
    
    # Radial profile of max block norms
    print("\n  r_frac     Enn_max    ET_max     H_avg")
    for i in range(0, len(blocks['Enn_profile']), max(1, len(blocks['Enn_profile'])//10)):
        rf = i / max(len(blocks['Enn_profile'])-1, 1)
        print(f"  {rf:.3f}    {blocks['Enn_profile'][i]:10.4f}  {blocks['ET_profile'][i]:10.4f}  "
              f"{blocks['H_profile'][i]:8.4f}")
    
    # Optimize at different transition lengths
    print("\n=== OPTIMIZATION SWEEP ===")
    rts = [0.6, 0.8, 1.0, 1.2, 1.5]
    results = []
    
    print(f"{'rt':>5} {'floor':>8} {'baseline':>10} {'optimized':>10} {'improve':>8} "
          f"{'Enn':>8} {'ET':>8} {'mom':>8} {'posdef':>8} {'evals':>6}")
    
    for rt in rts:
        floor = raychaudhuri_floor(rt)
        opt = optimize_transition(geom, rt, args.nr, args.ns, +1, 0, args.max_evals)
        opt["rt"] = rt
        opt["floor"] = floor
        results.append(opt)
        b = opt["blocks"]
        print(f"{rt:5.1f} {floor:8.4f} {opt['baseline_op_sup']:10.4f} "
              f"{opt['optimized_op_sup']:10.4f} {opt['improvement_factor']:8.2f} "
              f"{b['Enn_sup']:8.4f} {b['ET_op_sup']:8.4f} {b['mom_sup']:8.4f} "
              f"{opt['min_q_eigenvalue']:8.4f} {opt['evaluations']:6d}")
    
    # Now with radial modes at best rt
    print("\n=== WITH RADIAL PERTURBATION MODES ===")
    best_rt = min(rts, key=lambda rt: next(
        (r["optimized_op_sup"] for r in results if r["rt"] == rt), 1e20))
    
    for n_modes in [1, 2]:
        opt_m = optimize_transition(geom, best_rt, args.nr, args.ns, +1,
                                    n_modes, args.max_evals)
        opt_m["rt"] = best_rt
        opt_m["n_modes"] = n_modes
        results.append(opt_m)
        b = opt_m["blocks"]
        print(f"rt={best_rt}, modes={n_modes}: baseline={opt_m['baseline_op_sup']:.4f} "
              f"optimized={opt_m['optimized_op_sup']:.4f} "
              f"Enn={b['Enn_sup']:.4f} ET={b['ET_op_sup']:.4f} "
              f"posdef={opt_m['min_q_eigenvalue']:.4f}")
    
    out = {"parameters": vars(args), "results": results}
    path = SESSION / "workspace/data/step99_optimized_transition.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

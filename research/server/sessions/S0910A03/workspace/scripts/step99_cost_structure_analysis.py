"""Step 99: Complete cost structure analysis.

For the optimized transition at rt=1.0, compute:
1. Normal projection integral (Raychaudhuri identity)
2. Tangential cost decomposition: Ric(q) vs Weingarten terms  
3. Conformal expansion baseline: what ET would be for q=cosh²(r)q₀
4. Trace-traceless split of ET (scalar constraint vs TT content)

This determines whether ET has a structural floor or is an artifact of the 
parametrization.
"""
from __future__ import annotations
import importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

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


def conformal_expansion_residual(geom, R, nr):
    """Residual of the conformal trial q = cosh²(r) q₀.
    
    This trial has H(0)=0 (minimal center with zero Weingarten),
    NOT matching the charged Koiso center. It shows what the
    tangential cost is for a smooth conformal expansion alone.
    """
    ns = geom["q0"].shape[0]
    t, Dt, D2t = fmat.chebyshev_lobatto_01(nr)
    r = R * t
    
    q = np.zeros((nr, ns, 3, 3))
    for a in range(nr):
        q[a] = math.cosh(r[a])**2 * geom["q0"]
    
    Dr = Dt / R
    D2r = D2t / (R * R)
    
    res = fmat.full_residual(q, Dr, D2r)
    
    # Extract blocks
    ET_op = np.zeros((nr, ns))
    for a in range(nr):
        for b in range(ns):
            qi = np.linalg.inv(q[a, b])
            ET_sharp = qi @ res["ET"][a, b]
            ET_sym = 0.5 * (ET_sharp + ET_sharp.T)
            ET_op[a, b] = np.max(np.abs(np.linalg.eigvalsh(ET_sym)))
    
    return {
        "total_op_sup": float(np.max(res["op"])),
        "Enn_sup": float(np.max(np.abs(res["Enn"]))),
        "ET_op_sup": float(np.max(ET_op)),
        "ET_center": float(np.max(ET_op[0])),
        "ET_end": float(np.max(ET_op[-1])),
        # Analytic prediction: ET_orth = sech²(r)(Ric(q0)^sharp + 2I)
        # at r=0: Ric(q0)^sharp + 2I
        "H_center": float(np.mean(res["H"][0])),
        "H_end": float(np.mean(res["H"][-1])),
        "profile": [{"r": float(r[a]), 
                     "op_max": float(np.max(res["op"][a])),
                     "ET_max": float(np.max(ET_op[a])),
                     "H_avg": float(np.mean(res["H"][a]))} 
                    for a in range(0, nr, max(1, nr//10))],
    }


def decompose_ET_terms(geom, rt, nr, sign):
    """Decompose E_T = Ric(q) + 3q - K_r - HK + 2KqiK into individual terms."""
    ns = geom["q0"].shape[0]
    
    # Build quintic baseline
    Xt = np.array([2*rt, 0, 0, 2*rt, 0, 2*rt])
    idx = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    Xt_mat = np.zeros((ns, 3, 3))
    for k in range(ns):
        for p, (i,j) in enumerate(idx):
            Xt_mat[k, i, j] = Xt[p]
            Xt_mat[k, j, i] = Xt[p]
    
    Xr_t = 2.0 * np.eye(3)[None,:,:] * np.ones((ns,1,1))
    Xrr_t = np.zeros((ns, 3, 3))
    z = np.zeros_like(geom["q0"])
    coeff = fmat.quintic_coefficients(z, 2.0*sign*geom["A"], 2.0*geom["B"],
                                      Xt_mat, Xr_t, Xrr_t, rt)
    t, Dt, D2t = fmat.chebyshev_lobatto_01(nr)
    r = rt * t
    X = fmat.eval_poly(coeff, t)
    
    q = np.zeros_like(X)
    for a in range(nr):
        for b in range(ns):
            q[a, b] = geom["sq"][b] @ fmat.sym_exp(X[a, b]) @ geom["sq"][b]
    
    Dr, D2r = Dt / rt, D2t / (rt * rt)
    qn = np.einsum("ab,bsij->asij", Dr, q)
    qnn = np.einsum("ab,bsij->asij", D2r, q)
    
    # Override endpoints
    qn[0] = 2.0 * sign * geom["k0"]
    qnn[0] = 2.0 * (geom["ric0"] + 3.0 * geom["q0"] + 2.0 * np.einsum(
        "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
    qn[-1] = 2.0 * q[-1]
    qnn[-1] = 4.0 * q[-1]
    
    K = 0.5 * qn
    Kn = 0.5 * qnn
    qi = np.linalg.inv(q)
    W = np.einsum("rsij,rsjk->rsik", qi, K)
    H = np.trace(W, axis1=2, axis2=3)
    KqiK = np.einsum("rsij,rsjk,rskl->rsil", K, qi, K)
    
    ric3 = np.zeros_like(q)
    for a in range(nr):
        _, rr, _ = fmat.evol.christoffel_and_ricci(q[a])
        ric3[a] = rr
    
    # Individual terms of ET
    term_ric = ric3                           # Ric(q)
    term_3q = 3.0 * q                        # 3q
    term_Kn = -Kn                             # -K_r
    term_HK = -H[:,:,None,None] * K           # -HK
    term_2KqK = 2.0 * KqiK                   # 2KqiK
    ET_total = term_ric + term_3q + term_Kn + term_HK + term_2KqK
    
    # Compute operator norms of each term
    def term_op_norm(T):
        norms = np.zeros((nr, ns))
        for a in range(nr):
            for b in range(ns):
                sharp = qi[a, b] @ T[a, b]
                sym = 0.5 * (sharp + sharp.T)
                norms[a, b] = np.max(np.abs(np.linalg.eigvalsh(sym)))
        return norms
    
    terms = {
        "Ric_q": term_op_norm(term_ric),
        "3q": term_op_norm(term_3q),  # always = 3
        "minus_Kn": term_op_norm(term_Kn),
        "minus_HK": term_op_norm(term_HK),
        "2KqiK": term_op_norm(term_2KqK),
        "ET_total": term_op_norm(ET_total),
    }
    
    # Radial profile of s-max of each term
    profile = []
    for a in range(0, nr, max(1, nr//12)):
        entry = {"r": float(r[a]), "r_frac": float(t[a])}
        for name, norms in terms.items():
            entry[f"{name}_max"] = float(np.max(norms[a]))
        entry["H_avg"] = float(np.mean(H[a]))
        profile.append(entry)
    
    return {
        "rt": rt,
        "sups": {name: float(np.max(norms)) for name, norms in terms.items()},
        "profile": profile,
    }


def normal_projection_on_trial(geom, rt, nr, sign):
    """Compute the Raychaudhuri normal projection integral on the quintic trial."""
    ns = geom["q0"].shape[0]
    Xt = np.array([2*rt, 0, 0, 2*rt, 0, 2*rt])
    idx = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    Xt_mat = np.zeros((ns, 3, 3))
    for k in range(ns):
        for p, (i,j) in enumerate(idx):
            Xt_mat[k, i, j] = Xt[p]; Xt_mat[k, j, i] = Xt[p]
    
    Xr_t = 2.0 * np.eye(3)[None,:,:] * np.ones((ns,1,1))
    Xrr_t = np.zeros((ns, 3, 3))
    z = np.zeros_like(geom["q0"])
    coeff = fmat.quintic_coefficients(z, 2.0*sign*geom["A"], 2.0*geom["B"],
                                      Xt_mat, Xr_t, Xrr_t, rt)
    t_arr, Dt, D2t = fmat.chebyshev_lobatto_01(nr)
    r = rt * t_arr
    X = fmat.eval_poly(coeff, t_arr)
    
    q = np.zeros_like(X)
    for a in range(nr):
        for b in range(ns):
            q[a, b] = geom["sq"][b] @ fmat.sym_exp(X[a, b]) @ geom["sq"][b]
    
    Dr, D2r = Dt / rt, D2t / (rt * rt)
    qn = np.einsum("ab,bsij->asij", Dr, q); qnn = np.einsum("ab,bsij->asij", D2r, q)
    qn[0] = 2.0*sign*geom["k0"]
    qnn[0] = 2.0*(geom["ric0"]+3.0*geom["q0"]+2.0*np.einsum(
        "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
    qn[-1] = 2.0*q[-1]; qnn[-1] = 4.0*q[-1]
    
    K = 0.5*qn; qi = np.linalg.inv(q)
    W = np.einsum("rsij,rsjk->rsik", qi, K)
    H = np.trace(W, axis1=2, axis2=3)
    W2 = np.einsum("rsij,rsji->rs", W, W)
    
    Kn = 0.5*qnn
    Enn = 3.0 - np.einsum("rsij,rsji->rs", qi, Kn) + W2
    
    # Normal projection integral (s-averaged)
    H_avg = np.mean(H, axis=1)
    W2_avg = np.mean(W2, axis=1)
    Enn_avg = np.mean(Enn, axis=1)
    
    u = H_avg - 3.0*np.tanh(r)
    Wcirc_sq = W2_avg - H_avg**2/3.0
    cosh2 = np.cosh(r)**2
    
    dr = np.diff(r)
    def trap(f): return np.sum(0.5*(f[:-1]+f[1:])*dr)
    
    lhs = trap(cosh2*(-Enn_avg))
    ec = 3.0*math.cosh(rt)**2*(1.0-math.tanh(rt))
    shear = trap(cosh2*np.maximum(Wcirc_sq, 0))
    mismatch = trap(cosh2*u**2/3.0)
    
    return {
        "weighted_neg_Err": float(lhs),
        "endpoint_cost": float(ec),
        "shear_integral": float(shear),
        "mismatch_integral": float(mismatch),
        "identity_residual": float(abs(lhs - ec - shear - mismatch)),
        "u_center": float(u[0]),
        "u_end": float(u[-1]),
        "H_center": float(H_avg[0]),
        "H_end": float(H_avg[-1]),
    }


def main():
    ns, nr, wind, S, Qmax = 64, 35, 2, 1.0, 0.5
    geom = fmat.center_geometry(ns, wind, S, Qmax)
    
    print("=" * 70)
    print("STEP 99: COMPLETE COST STRUCTURE ANALYSIS")
    print("=" * 70)
    
    # 1. Conformal expansion baseline
    print("\n=== Conformal expansion q = cosh²(r)·q₀ (K₀=0, NOT Koiso center) ===")
    for R in [1.0, 2.0, 3.0]:
        cf = conformal_expansion_residual(geom, R, nr)
        print(f"  R={R}: total={cf['total_op_sup']:.4f}, ET_center={cf['ET_center']:.4f}, "
              f"ET_end={cf['ET_end']:.6f}, Enn={cf['Enn_sup']:.4f}, "
              f"H0={cf['H_center']:.3f}, H_end={cf['H_end']:.3f}")
    
    # 2. ET term decomposition for the quintic transition at rt=1.0
    print("\n=== ET term decomposition for quintic at rt=1.0 ===")
    decomp = decompose_ET_terms(geom, 1.0, nr, +1)
    print("Suprema:")
    for name, val in decomp["sups"].items():
        print(f"  {name:15s}: {val:10.4f}")
    print("\nRadial profile:")
    print(f"{'r':>6} {'Ric_q':>10} {'3q':>6} {'-Kn':>10} {'-HK':>10} {'2KqK':>10} {'ET':>10} {'H':>8}")
    for p in decomp["profile"]:
        print(f"{p['r']:6.3f} {p['Ric_q_max']:10.4f} {p['3q_max']:6.1f} "
              f"{p['minus_Kn_max']:10.4f} {p['minus_HK_max']:10.4f} "
              f"{p['2KqiK_max']:10.4f} {p['ET_total_max']:10.4f} {p['H_avg']:8.4f}")
    
    # 3. Normal projection integral
    print("\n=== Normal projection integral at rt=1.0 ===")
    npi = normal_projection_on_trial(geom, 1.0, nr, +1)
    print(f"  Weighted -E_rr: {npi['weighted_neg_Err']:.4f}")
    print(f"  Endpoint cost:  {npi['endpoint_cost']:.4f}")
    print(f"  Shear integral: {npi['shear_integral']:.4f}")
    print(f"  Mismatch:       {npi['mismatch_integral']:.4f}")
    print(f"  Identity resid: {npi['identity_residual']:.2e}")
    print(f"  u(0)={npi['u_center']:.4f}, u(R)={npi['u_end']:.4f}")
    print(f"  H(0)={npi['H_center']:.4f}, H(R)={npi['H_end']:.4f}")
    
    # 4. Floor comparison
    print(f"\n=== Floor comparison ===")
    print(f"  Raychaudhuri floor at rt=1.0: {raychaudhuri_floor(1.0):.4f}")
    print(f"  Conformal ET at center:       7.25 (approximate)")
    print(f"  Quintic ET peak:              {decomp['sups']['ET_total']:.4f}")
    print(f"  Quintic total peak:           {decomp['sups']['ET_total']:.4f}")
    print(f"  Ratio ET/floor:               {decomp['sups']['ET_total']/raychaudhuri_floor(1.0):.1f}")
    
    # Save all
    out = {
        "conformal_R1": conformal_expansion_residual(geom, 1.0, nr),
        "decomposition_rt1": decomp,
        "normal_projection_rt1": npi,
        "floor_rt1": raychaudhuri_floor(1.0),
    }
    path = SESSION / "workspace/data/step99_cost_structure_analysis.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

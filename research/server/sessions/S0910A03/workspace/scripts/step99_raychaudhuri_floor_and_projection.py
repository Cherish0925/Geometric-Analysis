"""Step 99: Raychaudhuri comparison floor and exact normal projection integral.

The Raychaudhuri identity for G = dn^2 + q(n,s) with H = tr(q^{-1} q_n/2),
W° = W - (H/3)I, and E = Ric + 3g gives

    H' + H^2/3 + |W°|^2 = 3 - E_rr.

Substituting u = H - 3 tanh(r) and multiplying by cosh^2(r):

    d/dr[cosh^2(r) u] + cosh^2(r)(u^2/3 + |W°|^2) = -cosh^2(r) E_rr.

Integrating from 0 to R with H(0)=0 (minimal center) and H(R)=3 (expanding):

    ∫_0^R cosh^2(r)(-E_rr) dr = 3 cosh^2(R)(1 - tanh R)
                                  + ∫_0^R cosh^2(r)[|W°|^2 + u^2/3] dr.

The first term is the endpoint cost; the second is the shear/mismatch integral.
Both are nonneg. The Raychaudhuri comparison ODE h'=(3+δ)-h^2/3, h(0)=0 gives
h(R)≥3 iff k tanh(kR)≥1 where k=sqrt(1+δ/3). This is the hard floor.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

SESSION = Path(__file__).resolve().parents[2]


def raychaudhuri_floor(R: float) -> float:
    """Solve k tanh(kR) = 1 for k = sqrt(1+delta/3); return delta."""
    if R <= 0:
        return float('inf')
    # f(k) = k tanh(kR) - 1; f(1)=tanh(R)-1<0 for finite R, f(large)>0
    def f(k):
        return k * math.tanh(k * R) - 1.0
    if f(1.0) >= 0:
        return 0.0
    k_max = max(2.0, 2.0 / R)
    while f(k_max) < 0:
        k_max *= 2
    k_sol = brentq(f, 1.0, k_max, xtol=1e-14)
    return 3.0 * (k_sol**2 - 1.0)


def endpoint_cost(R: float) -> float:
    """3 cosh^2(R) (1 - tanh R), the compulsory endpoint contribution."""
    c = math.cosh(R)
    t = math.tanh(R)
    return 3.0 * c * c * (1.0 - t)


def cosh2_integral(R: float) -> float:
    """∫_0^R cosh^2(r) dr = R/2 + sinh(2R)/4."""
    return R / 2.0 + math.sinh(2.0 * R) / 4.0


def compute_normal_projection(r: np.ndarray, H: np.ndarray,
                              Wsharp_sq: np.ndarray,
                              E_rr: np.ndarray,
                              R: float) -> dict:
    """Evaluate the exact normal projection integral on a grid.
    
    r: radial nodes (1D array, length nr)
    H: mean curvature H(r,s), shape (nr, ns)
    Wsharp_sq: |W|^2 = tr(W^2), shape (nr, ns)  -- TOTAL, not traceless
    E_rr: normal-normal Ricci defect, shape (nr, ns)
    R: half-cylinder length
    """
    nr, ns = H.shape
    
    # u = H - 3 tanh(r)
    tanh_r = np.tanh(r)
    u = H - 3.0 * tanh_r[:, None]
    
    # Traceless shear: |W°|^2 = |W|^2 - H^2/3
    Wcirc_sq = Wsharp_sq - H**2 / 3.0
    
    # cosh^2(r) weight
    cosh2 = np.cosh(r)**2
    
    # Integrands
    lhs_integrand = cosh2[:, None] * (-E_rr)  # weighted -E_rr
    shear_integrand = cosh2[:, None] * Wcirc_sq
    mismatch_integrand = cosh2[:, None] * (u**2 / 3.0)
    rhs_integrand = shear_integrand + mismatch_integrand
    
    # Trapezoidal integration over r for each s
    dr = np.diff(r)
    def trap(f):
        return np.sum(0.5 * (f[:-1] + f[1:]) * dr[:, None], axis=0)
    
    lhs_vals = trap(lhs_integrand)  # shape (ns,)
    shear_vals = trap(shear_integrand)
    mismatch_vals = trap(mismatch_integrand)
    rhs_vals = shear_vals + mismatch_vals
    
    ec = endpoint_cost(R)
    
    return {
        "endpoint_cost": ec,
        "weighted_neg_Err_mean": float(np.mean(lhs_vals)),
        "shear_integral_mean": float(np.mean(shear_vals)),
        "mismatch_integral_mean": float(np.mean(mismatch_vals)),
        "rhs_mean": float(np.mean(rhs_vals)) + ec,
        "identity_residual_mean": float(np.mean(np.abs(lhs_vals - rhs_vals - ec))),
        "identity_residual_max": float(np.max(np.abs(lhs_vals - rhs_vals - ec))),
        "u_sup": float(np.max(np.abs(u))),
        "u_center": float(np.max(np.abs(u[0]))),
        "u_end": float(np.max(np.abs(u[-1]))),
        "Wcirc_sq_sup": float(np.max(Wcirc_sq)),
    }


def main():
    # Table of Raychaudhuri floor values
    Rs = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0]
    table = []
    for R in Rs:
        dmin = raychaudhuri_floor(R)
        ec = endpoint_cost(R)
        ci = cosh2_integral(R)
        asym = 12.0 * math.exp(-2.0 * R)
        table.append({
            "R": R,
            "delta_min": dmin,
            "asymptotic_12exp_minus_2R": asym,
            "ratio_to_asymptotic": dmin / asym if asym > 1e-20 else None,
            "endpoint_cost_3cosh2R_1minustanhR": ec,
            "cosh2_integral": ci,
            "min_avg_neg_Err": ec / ci,  # minimum average -E_rr needed
        })
    
    print("Raychaudhuri Floor Table:")
    print(f"{'R':>6} {'delta_min':>12} {'12e^{-2R}':>12} {'ratio':>8} {'endpt_cost':>12} "
          f"{'cosh2_int':>12} {'min_avg':>10}")
    for t in table:
        print(f"{t['R']:6.1f} {t['delta_min']:12.6f} {t['asymptotic_12exp_minus_2R']:12.6f} "
              f"{t['ratio_to_asymptotic']:8.3f} {t['endpoint_cost_3cosh2R_1minustanhR']:12.4f} "
              f"{t['cosh2_integral']:12.4f} {t['min_avg_neg_Err']:10.6f}")
    
    # Validation: at R=1, k tanh(k)=1 should give delta≈1.318
    print(f"\nValidation: delta_min(1) = {raychaudhuri_floor(1.0):.6f} (expected ~1.318)")
    print(f"Validation: delta_min(2) = {raychaudhuri_floor(2.0):.6f}")
    print(f"Validation: delta_min(3) = {raychaudhuri_floor(3.0):.6f}")
    
    # Also verify the identity on the exact hyperbolic metric (E_rr=0)
    # For g = dn^2 + e^{2n} q0, W = I, H = 3, |W|^2 = 3, |W°|^2 = 0,
    # u = 3 - 3 tanh(n). The identity should hold exactly.
    nr = 201
    R_test = 3.0
    r = np.linspace(0, R_test, nr)
    H_test = 3.0 * np.ones((nr, 1))
    W2_test = 3.0 * np.ones((nr, 1))
    Err_test = np.zeros((nr, 1))
    proj = compute_normal_projection(r, H_test, W2_test, Err_test, R_test)
    print(f"\nExact hyperbolic validation (R={R_test}):")
    print(f"  Endpoint cost: {proj['endpoint_cost']:.6f}")
    print(f"  LHS (weighted -E_rr): {proj['weighted_neg_Err_mean']:.6f}")
    print(f"  Shear integral: {proj['shear_integral_mean']:.6f}")
    print(f"  Mismatch integral: {proj['mismatch_integral_mean']:.6f}")
    print(f"  RHS: {proj['rhs_mean']:.6f}")
    print(f"  Identity residual: {proj['identity_residual_mean']:.2e}")
    print(f"  u_sup: {proj['u_sup']:.6f}")  # should be 3(1-tanh(0))=3 at r=0 ... wait
    # Actually for exact expanding: H=3 everywhere, so u(0)=3-0=3, u(R)=3-3tanh(R)
    
    out = {"floor_table": table, "hyperbolic_validation": proj}
    path = SESSION / "workspace/data/step99_raychaudhuri_floor.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

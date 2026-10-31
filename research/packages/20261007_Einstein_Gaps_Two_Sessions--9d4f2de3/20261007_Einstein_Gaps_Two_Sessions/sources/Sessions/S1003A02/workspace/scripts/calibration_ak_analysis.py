"""INVALID (Step 35): ignores the r-scaling of scale-free variables (integrated |Ric0|^2 ~351
vs stored cost 6.48) and wrongly applies Phat=1+int L_AK to connectors starting at a collapsed
entry.  Kept only as a record; do not use its output.  See notes/step35_calibration_theorem_and_branch_classification.md §5.

Evaluate the AK Lagrangian and B-corrected calibration on optimizer trajectories.

For a smooth diagonal perpendicular exact-CH cell:
  Phat = 1 + int L_AK
  B = b+ - 3F - 9 Pm^2 - 6 W u u'
with B_bolt = 1, B_CH = 2.

This script evaluates these on the non-round and round optimizer trajectories
to identify the mechanism driving the large non-round cost.

In the scale-free system with r = 1:
  af = exp(2x/3)/z,  ag = 1/(exp(x/3)*z),  ah = z^2/exp(x/3)
  W = af*ag*ah = 1,   u = af  (conformal factor)
  q = -3 log z,  beta = x + q/2
"""
import json, sys, math
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parents[1] / 'data' / 'saturation_control'
OUT.mkdir(parents=True, exist_ok=True)

def shape_from_state(x, z):
    """Return (af, ag, ah) with af*ag*ah = 1 at r=1."""
    ex3 = math.exp(x / 3)
    af = ex3**2 / z
    ag = 1.0 / (ex3 * z)
    ah = z**2 / ex3
    return af, ag, ah

def full_jets(X, U, T):
    """Compute metric variables, curvature, and AK quantities along trajectory.
    
    X[i] = (x, z, p, chi, eta) at node i
    U[i] = (Hbar, Ebar, Dbar) at node i
    T = total tau duration
    """
    N = len(X) - 1
    dtau = T / N
    n = len(X)
    
    # State variables
    xs, zs, ps, chis, etas = X.T
    
    # Shape variables 
    qs = -3 * np.log(zs)
    betas = xs + qs / 2
    xis = chis + etas / 2
    
    ex3 = np.exp(xs / 3)
    afs = ex3**2 / zs
    ags = 1.0 / (ex3 * zs)
    ahs = zs**2 / ex3
    
    # u = af in scale-free
    us = afs
    
    # First jets (d log a_i / dtau)
    yf = 2 * chis / 3 + etas / 3
    yg = -chis / 3 + etas / 3
    yh = -chis / 3 - 2 * etas / 3
    
    # Physical first jets a_i' = a_i * (p + y_i) in original dt = r*dtau
    # But at r=1, dt = dtau, so a_i' = d(a_i)/dtau = a_i * y_i 
    # (since a_i = r * shape_i and dr/dtau = r*p for scale-free time)
    # Actually d(a_i)/dtau includes the r evolution.
    # d(af)/dtau = af * (p + yf) ... no. af = exp(2beta/3)/z doesn't depend on r.
    # In scale-free: d(af)/dtau = af * yf (shape evolution only)
    # d(ag)/dtau = ag * yg
    # d(ah)/dtau = ah * yh
    # These are the shape velocities at unit scale.
    
    # The gamma curvature quantities
    gf = (ags**2 + ahs**2 - afs**2) / (ags * ahs)
    gg = (ahs**2 + afs**2 - ags**2) / (ahs * afs)
    gh = (afs**2 + ags**2 - ahs**2) / (afs * ags)
    
    # b+ calculation
    # pf, pg, ph are the 'physical first jets' used in bplus
    # From the original code: pf = af*(p + 2*xi/3) etc.
    pf = afs * (ps + 2 * xis / 3)
    pg = ags * (ps - xis / 3 + etas / 2)
    ph = ahs * (ps - xis / 3 - etas / 2)
    uf = pf - gf
    ug = pg - gg
    uh = ph - gh
    bplus = 2 - (uf**2 + ug**2 + uh**2) - uf * ug * uh
    
    # Scalar curvature from Bianchi-IX
    # In diagonal metric ds^2 = dt^2 + af^2 sf^2 + ..., Gauss formula gives
    # s = -2(y_i' + Sum y_i^2) + 2 Sum P_i
    # where P_i = 2(a_i^4 - (a_j^2 - a_k^2)^2)/W^2 on round spheres
    # At r = 1, W = 1.
    # Actually this formula uses d/dt derivatives, and at r=1, dt = dtau.
    # So y_i are d(log a_i)/dtau and we need dy_i/dtau for curvature.
    
    # Second jets: use finite differences 
    dyf = np.gradient(yf, dtau, edge_order=2)
    dyg = np.gradient(yg, dtau, edge_order=2)
    dyh = np.gradient(yh, dtau, edge_order=2)
    
    S = yf + yg + yh  # Should be 0 (volume preserving)
    
    # Orbital curvatures
    Pf = 2 * (afs**4 - (ags**2 - ahs**2)**2)  # W=1
    Pg = 2 * (ags**4 - (ahs**2 - afs**2)**2)
    Ph = 2 * (ahs**4 - (afs**2 - ags**2)**2)
    
    # Individual Ric_{ii}: -y_i' - S * y_i + P_i (in dt gauge at r=1)
    Rff = -dyf - S * yf + Pf
    Rgg = -dyg - S * yg + Pg
    Rhh = -dyh - S * yh + Ph
    R00 = -(dyf + dyg + dyh + yf**2 + yg**2 + yh**2)  # -d(S)/dt - sum y_i^2
    sc = R00 + Rff + Rgg + Rhh  # scalar curvature
    
    # Ric tracefree components
    sbar = sc / 4
    ric0sq = (R00 - sbar)**2 + (Rff - sbar)**2 + (Rgg - sbar)**2 + (Rhh - sbar)**2
    
    # Controls and cost
    Hbar, Ebar, Dbar = U.T
    cost_density = 3 * Hbar**2 / 16 + Ebar**2 / 6 + Dbar**2 / 8
    
    # AK variables (at scale r = 1)
    # u = af, du/dtau = af * yf
    uprime = afs * yf  # du/dtau = du/dt at r=1
    
    # Nijenhuis scalar: nu = -(q_T + 4 sinh q / A_f) / (2u)
    # where T is AK time with dT = u dt = u dtau (r=1)
    # q_T = dq/dT = eta / (af)  since dq/dtau = eta and dtau = dT/u = dT/af
    qT = etas / afs
    sinhq = np.sinh(qs)
    coshq = np.cosh(qs)
    # A_f is the AK metric coefficient = u * a_f = af^2 (at r=1)
    Af_ak = afs * afs  # u * af = af^2
    nu = -(qT + 4 * sinhq / Af_ak) / (2 * us)
    
    # W3 eigenvalue lambda from Weyl
    # R+ eigenvalues: from the diagonal Bianchi-IX Weyl tensor
    # Self-dual Weyl W+:
    # W+_f = Rff/2 - (Rgg+Rhh)/4 - R00/4 + Pf/2 - (Pg+Ph)/4
    # Actually, the conformal AK W3 eigenvalue is:
    # lambda = (W+_g - W+_h) / (2u^2)
    # where W+ are the eigenvalues of the self-dual Weyl operator
    
    # Self-dual Weyl in orthonormal frame:
    # W+_1 = (1/2)(R_fgfg - R_fhfh) + R_ghgh - s/12
    # More precisely for Bianchi-IX:
    # w_f = -y_f'/2 + (-y_f - y_g*y_h/2)/(ag*ah) ... no wait
    
    # Use the proven formula: W+_i = -(Ric_jj - Ric_kk)/(2) + ...
    # Actually from the Cartan module: 
    # R+_i = -v_i'/(2*a_i) + (-v_i - v_j*v_k/2)/(a_j*a_k)
    # where v_i = a_i' - gamma_i
    # With v_i = pf - gf etc. (already computed as uf, ug, uh)
    
    # Need v_i' = d(v_i)/dtau
    dvf = np.gradient(uf, dtau, edge_order=2)
    dvg = np.gradient(ug, dtau, edge_order=2)
    dvh = np.gradient(uh, dtau, edge_order=2)
    
    Rpf = -dvf / (2 * afs) + (-uf - ug * uh / 2) / (ags * ahs)
    Rpg = -dvg / (2 * ags) + (-ug - uh * uf / 2) / (ahs * afs)
    Rph = -dvh / (2 * ahs) + (-uh - uf * ug / 2) / (afs * ags)
    
    # lambda = (Rp_g - Rp_h) / (2 * u^2)
    # but this is the R+ eigenvalue difference. The AK W3 eigenvalue 
    # from Theorem A: lambda is defined via W_3 of the AK metric.
    # In the peer's convention: lambda = (W+_g - W+_h)/(2u^2)
    # where W+_i = R+_i - s/12
    Wpg = Rpg - sc / 12
    Wph = Rph - sc / 12
    lam = (Wpg - Wph) / (2 * us**2)
    
    # delta: diagonal Weyl parameter delta = W+_f/u^2 + 4
    Wpf = Rpf - sc / 12
    delta = Wpf / us**2 + 4
    
    # AK volume density: dVhat = u^4 * W * dt = af^4 * 1 * dtau
    dVhat = afs**4  # per unit dtau
    
    # AK Lagrangian density (per dtau)
    # L_AK = 12 W (u^2 + s/24)^2 + 6 W u'^2 + 1.5 delta^2 dVhat + 2 lambda^2 dVhat - 6 nu^2 dVhat
    # At r=1, W=1
    term_H = 12 * (us**2 + sc / 24)**2  # * W * dt/dtau = 1
    term_G = 6 * uprime**2
    term_Qd = 1.5 * delta**2 * dVhat
    term_QA = 2 * lam**2 * dVhat  # = 0.5 * 4*lam^2 * dVhat
    term_N = -6 * nu**2 * dVhat
    
    LAK = term_H + term_G + term_Qd + term_QA + term_N
    
    # Also compute Sigma (scalar correction, zero if s = -24)
    term_Sigma = (sc + 24) * (us**2 - 1) * 1 + (sc + 24)**2 / 48  # Approximate
    
    return {
        'tau': np.arange(n) * dtau,
        'af': afs, 'ag': ags, 'ah': ahs,
        'q': qs, 'beta': betas, 'u': us,
        'yf': yf, 'yg': yg, 'yh': yh,
        'bplus': bplus, 'sc': sc,
        'nu': nu, 'lam': lam, 'delta': delta,
        'uprime': uprime, 'dVhat': dVhat,
        'cost_density': cost_density,
        'LAK': LAK,
        'term_H': term_H, 'term_G': term_G,
        'term_Qd': term_Qd, 'term_QA': term_QA,
        'term_N': term_N,
        'ric0sq': ric0sq, 'Phat_density': ric0sq / 4,
        'dtau': dtau,
    }


def analyze_trajectory(fname):
    d = json.load(open(fname))
    X = np.array(d['X']); U = np.array(d['U'])
    T = d['T']; cost = d['cost']
    eps = d.get('eps', '?')
    
    jets = full_jets(X, U, T)
    dtau = jets['dtau']
    n = len(X)
    
    # Integrate using trapezoidal rule
    def trap(arr):
        return np.trapz(arr, dx=dtau)
    
    int_LAK = trap(jets['LAK'])
    int_H = trap(jets['term_H'])
    int_G = trap(jets['term_G'])
    int_Qd = trap(jets['term_Qd'])
    int_QA = trap(jets['term_QA'])
    int_N = trap(jets['term_N'])
    int_cost = trap(jets['cost_density'])
    int_Phat = trap(jets['Phat_density'])
    
    # Predicted Phat from B formula: Phat = 1 + int L_AK
    Phat_pred = 1.0 + int_LAK
    
    result = {
        'file': str(fname),
        'eps': eps,
        'cost_stored': cost,
        'cost_integrated': float(int_cost),
        'Phat_integrated': float(int_Phat),
        'int_LAK': float(int_LAK),
        'Phat_from_B': float(Phat_pred),
        'terms': {
            '12H': float(int_H),
            '6G': float(int_G),
            '1.5Qd': float(int_Qd),
            '0.5QA (=2*int lam^2)': float(int_QA),
            '-1.5N (=-6*int nu^2)': float(int_N),
            'sum_AK': float(int_H + int_G + int_Qd + int_QA + int_N),
        },
        'bplus_range': [float(jets['bplus'].min()), float(jets['bplus'].max())],
        'q_range': [float(jets['q'].min()), float(jets['q'].max())],
        'u_range': [float(jets['u'].min()), float(jets['u'].max())],
        's_range': [float(jets['sc'].min()), float(jets['sc'].max())],
        'nu_range': [float(jets['nu'].min()), float(jets['nu'].max())],
    }
    
    return result, jets


def main():
    files_nonround = [
        'eps0p0625_N60_ch_bpmax_m1.json',
    ]
    files_round = [
        'chain_N80_c80.json',  # may contain round reopening 
    ]
    
    # Try to find available trajectory files
    all_results = []
    
    for fn in files_nonround:
        fp = OUT / fn
        if fp.exists():
            print(f"\n=== Non-round: {fn} ===")
            r, j = analyze_trajectory(fp)
            all_results.append(r)
            print(json.dumps(r, indent=2))
    
    # Also check the eps=1/32 case
    fn32 = 'eps0p03125_N80_ch_bpmax_m1_e32.json'
    fp32 = OUT / fn32
    if fp32.exists():
        print(f"\n=== Non-round eps=1/32: {fn32} ===")
        r, j = analyze_trajectory(fp32)
        all_results.append(r)
        print(json.dumps(r, indent=2))
    
    # Try a round-reopening case for comparison
    fn_round = 'chain_N80_c80.json'
    fp_round = OUT / fn_round
    if fp_round.exists():
        try:
            d = json.load(open(fp_round))
            # chain files may have different structure
            print(f"\n=== Round chain: {fn_round} - checking structure ===")
            print(f"Keys: {list(d.keys())[:10]}")
        except:
            pass
    
    # Save
    outf = OUT / 'calibration_ak_analysis.json'
    outf.write_text(json.dumps(all_results, indent=1) + '\n')
    print(f"\nSaved to {outf}")


if __name__ == '__main__':
    main()

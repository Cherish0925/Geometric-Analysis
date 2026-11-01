"""T^2-invariant Einstein BVP solver (Fourier-Galerkin, vectorized).

scipy.solve_bvp calls fun(x,y) with x shape (m,) and y shape (N,m).
We process each column separately.
"""
import json, traceback
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp

TWOPI = 2*np.pi

def build_koiso_center(A=1.0, npts=512):
    from scipy.integrate import solve_bvp as sbvp
    th = np.linspace(0, TWOPI, npts, endpoint=False)
    f_val = A*np.sin(th)
    def ode(x, y):
        u, up = y
        return np.vstack((up, 0.75*u**5 - 0.25*(A*np.cos(x))**2*u))
    def bc(ya, yb):
        return np.array([ya[0]-yb[0], ya[1]-yb[1]])
    x = np.linspace(0, TWOPI, 801)
    u0 = (np.mean((A*np.cos(x))**2)/3)**0.25
    guess = np.vstack((u0*(1+0.02*np.cos(2*x)), -0.04*u0*np.sin(2*x)))
    sol = sbvp(ode, bc, x, guess, tol=1e-11, max_nodes=40000)
    assert sol.success, sol.message
    u = sol.sol(th)[0]
    a0 = 2*np.log(u)
    b0 = 2*np.log(u) + f_val
    c0 = 2*np.log(u) - f_val
    return th, a0, b0, c0

def spec_deriv(v, order=1):
    """Spectral derivative of 1D periodic signal."""
    n = len(v)
    k = np.fft.rfftfreq(n, d=1.0/n) * TWOPI / n  # angular freq: k*2pi/n -> just use fftfreq properly
    # Correct: angular frequencies for period 2pi
    k_ang = np.arange(n//2+1)  # integer wave numbers
    vc = np.fft.rfft(v)
    return np.fft.irfft((1j*k_ang)**order * vc, n=n)

def spec_project(v, M):
    n = len(v)
    vc = np.fft.rfft(v)
    vc[M+1:] = 0
    return np.fft.irfft(vc, n=n)

def einstein_accel_1col(a, b, c, da, db, dc, M):
    """Compute (a_tt, b_tt, c_tt) for one theta-profile."""
    n = len(a)
    H = da + db + dc
    alpha = np.exp(-2*a)
    ap = spec_deriv(a); bp = spec_deriv(b); cp = spec_deriv(c)
    bpp = spec_deriv(b, 2); cpp = spec_deriv(c, 2)
    
    rhs_a = 3 - da*H + alpha*(ap*bp + ap*cp - bp**2 - bpp - cp**2 - cpp)
    rhs_b = 3 - db*H + alpha*(ap*bp - bp**2 - bp*cp - bpp)
    rhs_c = 3 - dc*H + alpha*(ap*cp - bp*cp - cp**2 - cpp)
    
    return spec_project(rhs_a, M), spec_project(rhs_b, M), spec_project(rhs_c, M)

def run_bvp_test(A_koiso, M, n_phys, R, target_type='round_cusp', nt_mesh=31):
    _, a0_raw, b0_raw, c0_raw = build_koiso_center(A_koiso, n_phys)
    a0 = spec_project(a0_raw, M)
    b0 = spec_project(b0_raw, M)
    c0 = spec_project(c0_raw, M)
    
    if target_type == 'round_cusp':
        aR = np.full(n_phys, R); bR = np.full(n_phys, R); cR = np.full(n_phys, R)
    elif target_type == 'aniso_expand':
        aR = np.full(n_phys, np.mean(a0))
        bR = np.full(n_phys, np.mean(b0) + R)
        cR = np.full(n_phys, np.mean(c0) + R)
    else:
        raise ValueError(target_type)
    
    N = 6 * n_phys
    
    def fun(x_arr, y_arr):
        """Vectorized: x_arr shape (m,), y_arr shape (N, m). Return (N, m)."""
        m = y_arr.shape[1] if y_arr.ndim > 1 else 1
        if y_arr.ndim == 1:
            y_arr = y_arr[:, None]
        out = np.zeros_like(y_arr)
        for j in range(m):
            yj = y_arr[:, j]
            a  = spec_project(yj[0*n_phys:1*n_phys], M)
            b  = spec_project(yj[1*n_phys:2*n_phys], M)
            c  = spec_project(yj[2*n_phys:3*n_phys], M)
            da = spec_project(yj[3*n_phys:4*n_phys], M)
            db = spec_project(yj[4*n_phys:5*n_phys], M)
            dc = spec_project(yj[5*n_phys:6*n_phys], M)
            ra, rb, rc = einstein_accel_1col(a, b, c, da, db, dc, M)
            out[0*n_phys:1*n_phys, j] = da
            out[1*n_phys:2*n_phys, j] = db
            out[2*n_phys:3*n_phys, j] = dc
            out[3*n_phys:4*n_phys, j] = ra
            out[4*n_phys:5*n_phys, j] = rb
            out[5*n_phys:6*n_phys, j] = rc
        return out
    
    def bc(ya, yb):
        res = np.empty(N)
        res[0*n_phys:1*n_phys] = ya[0*n_phys:1*n_phys] - a0
        res[1*n_phys:2*n_phys] = ya[1*n_phys:2*n_phys] - b0
        res[2*n_phys:3*n_phys] = ya[2*n_phys:3*n_phys] - c0
        res[3*n_phys:4*n_phys] = yb[0*n_phys:1*n_phys] - aR
        res[4*n_phys:5*n_phys] = yb[1*n_phys:2*n_phys] - bR
        res[5*n_phys:6*n_phys] = yb[2*n_phys:3*n_phys] - cR
        return res
    
    t_mesh = np.linspace(0, R, nt_mesh)
    y_guess = np.zeros((N, nt_mesh))
    for j in range(nt_mesh):
        s = t_mesh[j] / R
        y_guess[0*n_phys:1*n_phys, j] = (1-s)*a0 + s*aR
        y_guess[1*n_phys:2*n_phys, j] = (1-s)*b0 + s*bR
        y_guess[2*n_phys:3*n_phys, j] = (1-s)*c0 + s*cR
        y_guess[3*n_phys:4*n_phys, j] = (aR - a0)/R
        y_guess[4*n_phys:5*n_phys, j] = (bR - b0)/R
        y_guess[5*n_phys:6*n_phys, j] = (cR - c0)/R
    
    print(f"  BVP: N={N}, mesh={nt_mesh}, R={R}...", flush=True)
    sol = solve_bvp(fun, bc, t_mesh, y_guess, tol=1e-4, max_nodes=500, verbose=0)
    print(f"  done: success={sol.success}, nodes={len(sol.x)}, rms_res={sol.rms_residuals.max():.2e}")
    
    # Extract shape operator at t=0
    y0 = sol.y[:, 0]
    da0 = y0[3*n_phys:4*n_phys]
    db0 = y0[4*n_phys:5*n_phys]
    dc0 = y0[5*n_phys:6*n_phys]
    H0 = da0 + db0 + dc0
    
    # Constraint check at selected points
    e00_vals = []
    for j in range(0, len(sol.x), max(1, len(sol.x)//8)):
        yj = sol.y[:, j]
        a  = spec_project(yj[0*n_phys:1*n_phys], M)
        b  = spec_project(yj[1*n_phys:2*n_phys], M)
        c  = spec_project(yj[2*n_phys:3*n_phys], M)
        da = spec_project(yj[3*n_phys:4*n_phys], M)
        db = spec_project(yj[4*n_phys:5*n_phys], M)
        dc = spec_project(yj[5*n_phys:6*n_phys], M)
        ra, rb, rc = einstein_accel_1col(a, b, c, da, db, dc, M)
        E00 = 3 - (ra + rb + rc) - (da**2 + db**2 + dc**2)
        H = da + db + dc
        e00_vals.append({
            't': round(float(sol.x[j]), 4),
            'H_range': [round(float(H.min()), 4), round(float(H.max()), 4)],
            'E00_sup': round(float(np.abs(E00).max()), 6),
        })
    
    return {
        'params': {'A': A_koiso, 'M': M, 'n': n_phys, 'R': R, 'target': target_type},
        'success': bool(sol.success),
        'message': str(sol.message),
        'nodes': int(len(sol.x)),
        'rms_res_max': round(float(sol.rms_residuals.max()), 6),
        'shape_at_0': {
            'H_mean': round(float(np.mean(H0)), 6),
            'H_range': [round(float(H0.min()), 4), round(float(H0.max()), 4)],
            'S_sup': round(float(max(np.abs(da0).max(), np.abs(db0).max(), np.abs(dc0).max())), 4),
        },
        'constraint_check': e00_vals,
    }

def main():
    results = []
    configs = [
        (0.3, 'round_cusp'), (0.5, 'round_cusp'), (1.0, 'round_cusp'),
        (0.5, 'aniso_expand'), (1.0, 'aniso_expand'),
    ]
    for R, target in configs:
        print(f"\n--- R={R}, target={target} ---")
        try:
            res = run_bvp_test(A_koiso=1.0, M=2, n_phys=16, R=R,
                               target_type=target, nt_mesh=25)
            results.append(res)
            so = res['shape_at_0']
            print(f"  S_sup(0)={so['S_sup']:.4f}, H_mean(0)={so['H_mean']:.4f}")
            print(f"  E00: {[v['E00_sup'] for v in res['constraint_check']]}")
        except Exception as e:
            traceback.print_exc()
            results.append({'R': R, 'target': target, 'error': str(e)})
    
    path = Path(__file__).resolve().parents[1]/'data'/'step70_bvp_results.json'
    path.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f"\nWrote {path}")

if __name__ == '__main__':
    main()

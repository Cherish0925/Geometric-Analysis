"""Step 50c: test the closed-form corrector k0^W = (3/2) sym(h_W kB) - (1/4) tr(h_W kB) delta
in the independent Step-49 trace-free-Ricci (Laurent) quadratic form on H2xH2 and CH.
Expected: F_H2H2(Ch.5 c* ansatz + k0^W) = -18 (= F_CH(c*)), F_CH unchanged (h_W absent).
Usage: python step50_check_corrector_ric0.py
"""
import os, sys, json, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import step50_wminus_compatibility as W

D49 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "step49")

def k0W(x, scale=1.0):
    h = W.hW(x); k = W.kB(x)
    return scale*(0.75*(h@k + k@h) - 0.25*jnp.trace(h@k)*jnp.eye(4))

def coeffs_in_step49_basis(fun):
    rng = np.random.default_rng(0)
    pts = rng.normal(size=(400, 4))
    idx4 = list(itertools.combinations_with_replacement(range(4), 4))
    M = np.array([[np.prod(p[list(i)])/(p@p)**2 for i in idx4] for p in pts])
    vals = np.array([np.array(fun(jnp.array(p))) for p in pts])      # (400,4,4)
    ab = [(a, b) for a in range(4) for b in range(a, 4)]
    C = np.zeros((35, 10)); maxres = 0
    for e, (a, b) in enumerate(ab):
        c, *_ = np.linalg.lstsq(M, vals[:, a, b], rcond=None)
        maxres = max(maxres, np.abs(M@c - vals[:, a, b]).max())
        C[:, e] = c
    vec = np.zeros(465)
    vec[5 + 10*(1+10):] = C.reshape(-1)       # d=4 block: index 5 + 10*(m) + e with m offset 11
    return vec, maxres

def main():
    vecW, fitres = coeffs_in_step49_basis(k0W)
    out = {"fit_residual": float(fitres)}
    cst = np.zeros(465); cst[0] = 1; cst[1] = 1; cst[2:5] = [9/4, 3/4, 1/2]
    for bg in ["H2H2", "CH"]:
        Q = np.load(os.path.join(D49, f"quadform_{bg}_NS12_NXI20_M24_R0.3_A4_K0.npz"))["Q"]
        F = Q/(8*np.pi**2)
        r = {"F_cstar": float(cst@F@cst)}
        for sc in [0.5, 1.0, 1.5]:
            v = cst + sc*vecW
            r[f"F_cstar_plus_{sc}k0W"] = float(v@F@v)
        r["cross_cstar_k0W"] = float(cst@F@vecW)
        r["quad_k0W"] = float(vecW@F@vecW)
        out[bg] = r
    print(json.dumps(out, indent=1))
    json.dump(out, open(os.path.join(W.OUT, "corrector_check_ric0form.json"), "w"), indent=1)

if __name__ == "__main__":
    main()

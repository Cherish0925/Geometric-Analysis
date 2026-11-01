"""Step 66: test A02's shared jet at D=6 and D=8 to confirm or reject order-6 obstruction.

A02's parametrization: f(z) = c z + B zbar, B = S + A, where
  c = 1, S = [[2, 1], [1, 1+i]], A = [[0, a], [-a, 0]] with a = 2+2i, lam = -1.
  ||S||^2 = 8, ||A||^2 = 16 = 8|c|^2 + ||S||^2 (on cone), det_R Df = 110.

Dictionary: F = Df (real Jacobian of f) = Fp + Fm, where
  Fp = c_r I (for c real) is the J-commuting part,
  Fm is the J-anticommuting part from B.
  Mmat = F^T (transposed = nabla_k a_l), Nphi = 2 Mmat, Mvec = [Nphi.ravel(), 0^16].
  
My D corresponds to A02's ordering:
  D=6 -> Ric through degree 4 (their order 4)   -> should converge
  D=8 -> Ric through degree 6 (their order 6)   -> predicted to STAGNATE if Phi6 > 0
"""
import os, sys, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from step62_zero_prolong import setup, Mvec, lm, TRI, PAIRS, W0, JM

def build_F_from_cSA(c, S, A):
    """Build real 4x4 Jacobian F = Df from complex (c, S, A)."""
    B = S + A  # 2x2 complex
    # Fp: complex-linear part c*Id
    cr, ci = c.real, c.imag
    Fp = np.array([[cr, -ci, 0, 0],
                    [ci,  cr, 0, 0],
                    [0,  0,  cr, -ci],
                    [0,  0,  ci,  cr]])
    # Fm: antilinear part z -> B zbar
    # Row ordering: (Re f1, Im f1, Re f2, Im f2)
    # Col ordering: (x0, x1, x2, x3) with z1=x0+ix1, z2=x2+ix3
    Fm = np.zeros((4, 4))
    for row_idx, (i_out, re_im) in enumerate([(0, 'r'), (0, 'i'), (1, 'r'), (1, 'i')]):
        for col_idx, j_in in enumerate(range(4)):
            # z_bar_k = x_{2k} - i x_{2k+1}
            # (B zbar)_i = sum_k B[i,k] zbar_k
            # x_j contributes to zbar_{j//2} with coefficient +1 if j even, -i if j odd
            k = j_in // 2; sgn_im = -1 if (j_in % 2 == 1) else 0; sgn_re = 1 if (j_in % 2 == 0) else 0
            # zbar_k coefficient of x_j: delta_{j,2k} - i delta_{j,2k+1}
            # So B[i,k]*(re coeff) and B[i,k]*(im coeff)
            bij = B[i_out, k]
            if j_in % 2 == 0:
                # x_{2k}: zbar_k has coeff 1
                contrib = bij  # complex
            else:
                # x_{2k+1}: zbar_k has coeff -i
                contrib = -1j * bij
            if re_im == 'r':
                Fm[row_idx, col_idx] = contrib.real
            else:
                Fm[row_idx, col_idx] = contrib.imag
    F = Fp + Fm
    return F, Fp, Fm

def make_mvec(c, S, A):
    """Construct the 32-dim Mvec from (c, S, A)."""
    F, _, _ = build_F_from_cSA(c, S, A)
    Mmat = F.T  # nabla_k a_l
    Nphi = 2.0 * Mmat
    Npsi = np.zeros((4, 4))
    return np.concatenate([Nphi.ravel(), Npsi.ravel()])

def check_cone(c, S, A):
    """Verify ||A||^2 = 8|c|^2 + ||S||^2."""
    normA2 = 2*np.sum(np.abs(A)**2)  # Frobenius of antisymmetric
    normS2 = 2*np.sum(np.abs(S)**2)  # Frobenius of symmetric
    normC2 = np.abs(c)**2
    # actual Frobenius: for 2x2 complex matrix M, ||M||^2 = sum |M_ij|^2
    normA2 = np.sum(np.abs(A)**2)
    normS2 = np.sum(np.abs(S)**2)
    return {"||A||^2": normA2, "||S||^2": normS2, "|c|^2": normC2,
            "cone_lhs": normA2, "cone_rhs": 8*normC2 + normS2,
            "on_cone": abs(normA2 - 8*normC2 - normS2) < 1e-10}

def run_test(D, lam, mvec_target, label, nsteps=15, iters=80):
    """Run continuation from Kahler germ to target at degree D."""
    S = setup(D); nvar = S["nvar"]; keep = jnp.array(S["keep"])
    mt = jnp.array(mvec_target)
    
    def F_eq(z, t):
        return jnp.concatenate([S["system"](z, lam)[keep], Mvec(S, z) - t*mt])
    Fj = jax.jit(F_eq); Jj = jax.jit(jax.jacfwd(F_eq))
    
    z = np.random.default_rng(42).standard_normal(nvar)*0.05
    path = []
    t0 = time.time()
    ts = np.concatenate([[0.0], np.linspace(1.0/nsteps, 1.0, nsteps)])
    for t in ts:
        z, f, hist, gn, Jm, r = lm(lambda zz: Fj(zz, t), lambda zz: Jj(zz, t), z, iters)
        sys_r = np.asarray(S["system"](jnp.array(z), lam))[S["keep"]]
        # residual by equation type and degree
        bydeg = {}
        for k_, ri in zip(S["keep"], sys_r):
            key = f"E{S['rowtype'][k_]}_d{S['rowdeg'][k_]}"; bydeg[key] = bydeg.get(key, 0.0) + float(ri**2)
        cv = S["curvature"](jnp.array(z)); mz = np.asarray(Mvec(S, jnp.array(z)))
        mdet = float(np.linalg.det(mz[:16].reshape(4,4)))
        rec = {"t": float(t), "res2": f, "grad": gn, "Merr": float(np.linalg.norm(mz - t*mvec_target)),
               "det": mdet, "s": float(cv["s"]), "|W-|": float(np.linalg.norm(np.asarray(cv["Wm"]))),
               "worst": dict(sorted(bydeg.items(), key=lambda kv: -kv[1])[:4]),
               "time": time.time()-t0}
        path.append(rec)
        print(f"  t={t:.3f}  res2={f:.4e}  grad={gn:.2e}  Merr={rec['Merr']:.2e}  det={mdet:.4f}", flush=True)
    
    result = {"label": label, "D": D, "lam": lam, "nvar": nvar, "neq": int(len(S["keep"])+32),
              "target_det": float(np.linalg.det(mvec_target[:16].reshape(4,4)/2)),
              "path": path}
    return result, z

def main():
    # A02's test jet
    c = complex(1, 0)
    S = np.array([[2, 1], [1, 1+1j]], dtype=complex)
    A = np.array([[0, 2+2j], [-(2+2j), 0]], dtype=complex)
    lam = -1.0
    
    # Verify cone
    cone = check_cone(c, S, A)
    print("Cone check:", json.dumps(cone, default=str))
    
    # Build F and check det
    F, Fp, Fm = build_F_from_cSA(c, S, A)
    det_F = np.linalg.det(F)
    print(f"F =\n{F}")
    print(f"det(F) = {det_F:.6f}  (A02 says 110)")
    
    # Verify J decomposition: Fp should commute with J, Fm anticommute
    J = np.array(JM)
    comm_p = np.linalg.norm(Fp @ J - J @ Fp)
    anti_m = np.linalg.norm(Fm @ J + J @ Fm)
    print(f"[Fp,J] = {comm_p:.2e}, {{Fm,J}} = {anti_m:.2e}")
    
    # Build admissible target in L whose Nphi block equals F^T (Mm = F^T convention of step62 linear_analysis);
    # the Npsi block is then determined by L (it is a J-rotation of Nphi, not zero).
    linpath = os.path.join(HERE, "..", "data", "step62", "linear.npz")
    lin = np.load(linpath); Lb = lin["Lb"]
    coef, *_ = np.linalg.lstsq(Lb[:16], F.T.ravel(), rcond=None)
    mvec = Lb @ coef
    fit_err = float(np.linalg.norm(Lb[:16] @ coef - F.T.ravel())/np.linalg.norm(F))
    print(f"fit error of Nphi block inside L: {fit_err:.3e}")
    # sector norms in the step62 bases (cone: |m_A|^2 = 4|m_c|^2 + |m_S|^2)
    def comp(B):
        x, *_ = np.linalg.lstsq(B, mvec, rcond=None); return B @ x
    mc, mA, mS = comp(lin["Llin"]), comp(lin["A"]), comp(lin["S"])
    dec_err = float(np.linalg.norm(mvec - mc - mA - mS))
    nc, nA, nS = [float(np.linalg.norm(v)**2) for v in (mc, mA, mS)]
    print(f"sector |m_c|^2={nc:.6f} |m_A|^2={nA:.6f} |m_S|^2={nS:.6f} dec_err={dec_err:.2e}")
    print(f"cone residual |m_A|^2-4|m_c|^2-|m_S|^2 = {nA-4*nc-nS:.3e}  (relative {(nA-4*nc-nS)/nA:.3e})")
    print(f"det(Mm) = {np.linalg.det(mvec[:16].reshape(4,4)):.6f}")
    if fit_err > 1e-8 or abs(nA-4*nc-nS) > 1e-8*nA:
        print("DICTIONARY MISMATCH"); 
        if os.environ.get("DIAG_ONLY"): return
    if os.environ.get("DIAG_ONLY"): return
    
    OUTDIR = os.path.join(HERE, "..", "data", "step66"); os.makedirs(OUTDIR, exist_ok=True)
    
    # Run D=6 (should converge)
    print(f"\n=== D=6, lam={lam} ===")
    res6, z6 = run_test(6, lam, mvec, "A02_shared_D6")
    json.dump(res6, open(os.path.join(OUTDIR, "A02_shared_D6.json"), "w"), indent=1, default=float)
    
    # Run D=8 (critical test)
    print(f"\n=== D=8, lam={lam} ===")
    res8, z8 = run_test(8, lam, mvec, "A02_shared_D8", nsteps=20, iters=100)
    json.dump(res8, open(os.path.join(OUTDIR, "A02_shared_D8.json"), "w"), indent=1, default=float)
    
    # Summary
    best6 = min(p["res2"] for p in res6["path"] if p["t"] > 0.9)
    best8 = min(p["res2"] for p in res8["path"] if p["t"] > 0.9)
    print(f"\n=== SUMMARY ===")
    print(f"D=6: best res2 at t~1 = {best6:.4e}")
    print(f"D=8: best res2 at t~1 = {best8:.4e}")
    print(f"A02 prediction: D=6 converges, D=8 stagnates (Phi6=1121.5)")
    if best6 < 1e-20 and best8 > 1e-5:
        print("CONFIRMED: order-6 obstruction at this jet")
    elif best6 < 1e-20 and best8 < 1e-20:
        print("REJECTED: D=8 converges, pipeline disagreement")
    else:
        print(f"INCONCLUSIVE: D=6={best6:.2e}, D=8={best8:.2e}")

if __name__ == "__main__":
    main()

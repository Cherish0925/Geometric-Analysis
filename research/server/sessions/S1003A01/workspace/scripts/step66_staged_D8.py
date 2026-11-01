"""Step 66: staged D=8 test for the order-6 obstruction at a prescribed nondegenerate cone jet.

Strategy:
  1. Solve the full system at D=6 (Ric through degree 4) with continuation -> z6.
  2. Embed z6 into D=8 (degree 7,8 coefficients = 0).
  3. Compute the NEW equations (E3 degrees 5,6; E1 degrees 7,8; E2 degrees 6,7)
     and their Jacobian w.r.t. the NEW unknowns (degree 7,8 coefficients).
  4. Attempt a least-squares solve: if the cokernel residual is nonzero, the obstruction is confirmed.

Memory: only the incremental Jacobian (~5000 x 4500) is needed, not the full D=8 system.
"""
import os, sys, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import step62_zero_prolong as Z
from step66_A02_test_jet import build_F_from_cSA

OUT = os.path.join(HERE, "..", "data", "step66"); os.makedirs(OUT, exist_ok=True)
Lb = np.load(os.path.join(HERE, "..", "data", "step62", "linear.npz"))["Lb"]

def a02_mvec():
    c = 1+0j; S = np.array([[2, 1], [1, 1+1j]]); A = np.array([[0, 2+2j], [-(2+2j), 0]])
    F, _, _ = build_F_from_cSA(c, S, A)
    coef, *_ = np.linalg.lstsq(Lb[:16], F.T.ravel(), rcond=None)
    return Lb @ coef

def solve_D6(lam, mt, seed=7, nsteps=15, iters=60):
    """Solve the D=6 system with continuation."""
    S6 = Z.setup(6); nv = S6["nvar"]; keep = jnp.array(S6["keep"])
    mtj = jnp.array(mt)
    F6 = lambda z, t: jnp.concatenate([S6["system"](z, lam)[keep], Z.Mvec(S6, z) - t*mtj])
    Fj = jax.jit(F6); Jj = jax.jit(jax.jacfwd(F6))
    z = np.random.default_rng(seed).standard_normal(nv)*0.05
    for t in np.linspace(0, 1, nsteps+1):
        z, f, *_ = Z.lm(lambda zz: Fj(zz, t), lambda zz: Jj(zz, t), z, iters)
    r = float(np.sum(np.asarray(S6["system"](jnp.array(z), lam))[S6["keep"]]**2)
              + np.sum(np.asarray(Z.Mvec(S6, jnp.array(z)) - mt)**2))
    return z, r, S6

def embed_D6_to_D8(z6, S6, S8):
    """Embed D=6 solution into D=8 variable space (new coefficients = 0)."""
    P6, P8 = S6["P"], S8["P"]
    idx6 = np.where(P6.deg >= 2)[0]; idx8 = np.where(P8.deg >= 2)[0]
    pos8 = {tuple(P8.L[c]): k for k, c in enumerate(idx8)}
    z6_arr = np.asarray(z6).reshape(16, len(idx6))
    z8 = np.zeros((16, len(idx8)))
    for k, c in enumerate(idx6):
        mon = tuple(P6.L[c])
        if mon in pos8:
            z8[:, pos8[mon]] = z6_arr[:, k]
    return z8.ravel()

def staged_test(lam, mt, seed=7):
    """Main staged test: solve D=6 then check D=8 solvability."""
    t0 = time.time()
    
    # Stage 1: solve D=6
    print("=== Stage 1: D=6 solve ===", flush=True)
    z6, r6, S6 = solve_D6(lam, mt, seed)
    print(f"D6 res2 = {r6:.4e}  ({time.time()-t0:.1f}s)", flush=True)
    
    # Stage 2: embed into D=8
    print("=== Stage 2: embed and compute incremental system ===", flush=True)
    S8 = Z.setup(8)
    P8 = S8["P"]; idx8 = np.where(P8.deg >= 2)[0]; coldeg8 = np.tile(P8.deg[idx8], 16)
    keep8 = S8["keep"]; rt8 = S8["rowtype"][keep8]; rd8 = S8["rowdeg"][keep8]
    level8 = np.where(rt8 == 1, rd8, np.where(rt8 == 2, rd8 + 1, rd8 + 2))
    
    z8_base = embed_D6_to_D8(z6, S6, S8)
    
    # New unknowns: degree 7 and 8 coefficients
    hi_cols = np.where((coldeg8 == 7) | (coldeg8 == 8))[0]
    # New equations: those at levels 5,6,7,8 that are NOT already in D=6
    # D=6 covers: E1 deg<=6, E2 deg<=5, E3 deg<=4  -> levels <= 6
    # D=8 adds: E3 deg 5,6; E1 deg 7,8; E2 deg 6,7 -> levels 7,8 for E1/E2 and levels 5,6 for E3 (new)
    # More precisely: a "level" = degree in which the equation's highest jet enters
    # E3 at degree d has "level" d+2; E1 at degree d has level d; E2 at degree d has level d+1
    # D=6 solves levels 2..6 (E3 deg 0-4, E1 deg 2-6, E2 deg 1-5, plus Mvec)
    # D=8 adds: levels 7 (E3 deg5, E1 deg7, E2 deg6) and 8 (E3 deg6, E1 deg8, E2 deg7)
    new_rows = np.where((level8 == 7) | (level8 == 8))[0]
    
    print(f"  D8: nvar={S8['nvar']}, new_unknowns={len(hi_cols)}, new_equations={len(new_rows)}", flush=True)
    
    # Compute residual at the embedded D=6 solution
    sysf = jax.jit(lambda z: S8["system"](z, lam)[jnp.array(keep8)])
    z8j = jnp.array(z8_base)
    r_full = np.asarray(sysf(z8j))
    r_new = r_full[new_rows]
    r_old = np.delete(r_full, new_rows)
    mvec_r = np.asarray(Z.Mvec(S8, z8j) - mt)
    
    print(f"  old-level residual: {np.sum(r_old**2):.4e}", flush=True)
    print(f"  new-level residual: {np.sum(r_new**2):.4e}", flush=True)
    print(f"  Mvec residual: {np.sum(mvec_r**2):.4e}", flush=True)
    
    # Jacobian of new equations w.r.t. new unknowns (affine system)
    print("  computing incremental Jacobian...", flush=True)
    def F_new(y):
        z = jnp.array(z8_base).at[jnp.array(hi_cols)].add(y)
        return sysf(z)[jnp.array(new_rows)]
    J_new = np.asarray(jax.jacfwd(F_new)(jnp.zeros(len(hi_cols))))
    b = r_new  # constant term (residual at y=0)
    print(f"  J_new shape: {J_new.shape}  ({time.time()-t0:.1f}s)", flush=True)
    
    # SVD of J_new
    U, s, Vt = np.linalg.svd(J_new, full_matrices=True)
    rank = int((s > 1e-9 * s[0]).sum())
    print(f"  rank(J_new) = {rank} out of {min(J_new.shape)}", flush=True)
    
    # Solvability: decompose b into range and cokernel
    b_range = U[:, :rank] @ (U[:, :rank].T @ b)
    b_coker = b - b_range
    coker_norm = float(np.linalg.norm(b_coker))
    range_norm = float(np.linalg.norm(b_range))
    
    print(f"  ||b_range|| = {range_norm:.6e}", flush=True)
    print(f"  ||b_coker|| = {coker_norm:.6e}  <-- THIS IS THE OBSTRUCTION", flush=True)
    
    # Least-squares solve (find best z_hi)
    y_opt = -Vt[:rank].T @ ((s[:rank]**(-1)) * (U[:, :rank].T @ b))
    z8_opt = z8_base.copy(); z8_opt[hi_cols] += y_opt
    r_opt = np.asarray(F_new(jnp.array(y_opt)))
    
    print(f"  after LS: ||r_new||^2 = {np.sum(r_opt**2):.6e}", flush=True)
    
    # Also try LM from the LS solution to see if nonlinearity helps
    print("  LM refinement from LS...", flush=True)
    Fj = jax.jit(F_new); Jfj = jax.jit(jax.jacfwd(F_new))
    y_lm, f_lm, hist_lm, gn_lm, _, _ = Z.lm(Fj, Jfj, jnp.array(y_opt), 60)
    print(f"  LM res2 = {f_lm:.6e}  grad = {gn_lm:.2e}", flush=True)
    
    # Additional LM from random starts
    rng = np.random.default_rng(42); best_random = []
    for k in range(5):
        y0 = rng.standard_normal(len(hi_cols)) * 0.1
        y_r, f_r, *_ = Z.lm(Fj, Jfj, jnp.array(y0), 60)
        best_random.append(float(f_r))
    print(f"  random LM best res2: {min(best_random):.6e}", flush=True)
    
    # Cokernel analysis: how many independent cokernel conditions?
    coker_dim = len(new_rows) - rank
    Pc = U[:, rank:]  # cokernel basis
    coker_b = Pc.T @ b  # projection of constant term onto cokernel
    coker_sv = np.sort(np.abs(coker_b))[::-1][:min(20, coker_dim)]
    
    result = {
        "lam": lam, "D6_res2": float(r6), "D8_nvar": S8["nvar"],
        "new_unknowns": int(len(hi_cols)), "new_equations": int(len(new_rows)),
        "rank_J_new": rank, "cokernel_dim": coker_dim,
        "old_level_res2": float(np.sum(r_old**2)), "mvec_res2": float(np.sum(mvec_r**2)),
        "new_level_res2_at_embed": float(np.sum(r_new**2)),
        "b_range_norm": range_norm, "b_coker_norm": coker_norm,
        "LS_res2": float(np.sum(r_opt**2)), "LM_res2": float(f_lm), "LM_grad": float(gn_lm),
        "random_LM_res2": sorted(best_random)[:5],
        "coker_b_top": coker_sv.tolist(),
        "J_new_sv_top": s[:10].tolist(), "J_new_sv_tail": s[max(0, rank-5):rank].tolist(),
        "conclusion": "OBSTRUCTION" if coker_norm > 1e-6 else "COMPATIBLE",
        "time": time.time() - t0
    }
    print(f"\n=== RESULT: {result['conclusion']} ===")
    print(f"cokernel norm = {coker_norm:.6e}, LS residual = {result['LS_res2']:.6e}")
    return result

def main():
    mt = a02_mvec()
    lam = -1.0
    
    result = staged_test(lam, mt)
    fn = os.path.join(OUT, "staged_D8_a02_lam-1.json")
    json.dump(result, open(fn, "w"), indent=1, default=float)
    print(f"\nSaved to {fn}")
    
    # Also test Kahler control (zero jet): should be fully solvable
    print("\n\n=== CONTROL: Kahler jet (should be fully solvable) ===")
    result_k = staged_test(lam, np.zeros(32), seed=3)
    fn_k = os.path.join(OUT, "staged_D8_kahler_lam-1.json")
    json.dump(result_k, open(fn_k, "w"), indent=1, default=float)

if __name__ == "__main__":
    main()

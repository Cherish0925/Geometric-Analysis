"""Step 66: lightweight staged D=8 obstruction test.

1. Solve D=6 using step62_zero_prolong cont mode (known to work).
2. Embed into D=8, compute residual and incremental Jacobian via finite differences.
   This avoids jax.jacfwd at D=8 entirely.
"""
import os, sys, json, time, gc
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "..", "data", "step66"); os.makedirs(OUT, exist_ok=True)

# ---- Phase 1: solve D=6 ----
print("Phase 1: D=6 solve", flush=True); t0 = time.time()
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
import step62_zero_prolong as Z
from step66_A02_test_jet import build_F_from_cSA

Lb = np.load(os.path.join(HERE, "..", "data", "step62", "linear.npz"))["Lb"]
c = 1+0j; S = np.array([[2,1],[1,1+1j]]); A = np.array([[0,2+2j],[-(2+2j),0]])
F, _, _ = build_F_from_cSA(c, S, A)
coef, *_ = np.linalg.lstsq(Lb[:16], F.T.ravel(), rcond=None)
mt = Lb @ coef
lam = -1.0
print(f"  target det={np.linalg.det(mt[:16].reshape(4,4)):.4f}", flush=True)

S6 = Z.setup(6); nv6 = S6["nvar"]; keep6 = jnp.array(S6["keep"])
mtj = jnp.array(mt)
def F6t(z, t): return jnp.concatenate([S6["system"](z, lam)[keep6], Z.Mvec(S6, z) - t*mtj])
Fj6 = jax.jit(F6t); Jj6 = jax.jit(jax.jacfwd(F6t))
rng = np.random.default_rng(7)
z6 = rng.standard_normal(nv6)*0.05
for t in np.linspace(0, 1, 16):
    z6, f6, *_ = Z.lm(lambda zz: Fj6(zz, t), lambda zz: Jj6(zz, t), z6, 60)
    if t in (0, 0.5, 1.0): print(f"  t={t:.2f} res2={f6:.3e}", flush=True)
# verify
sys6 = np.asarray(S6["system"](jnp.array(z6), lam))[S6["keep"]]
mv6 = np.asarray(Z.Mvec(S6, jnp.array(z6)))
r6_sys = float(np.sum(sys6**2)); r6_mv = float(np.sum((mv6-mt)**2))
print(f"  D6 final: sys_res2={r6_sys:.3e}, Mvec_err2={r6_mv:.3e} ({time.time()-t0:.1f}s)", flush=True)
np.save(os.path.join(OUT, "z6_a02.npy"), np.asarray(z6))

# ---- Phase 2: embed into D=8 and compute incremental system ----
print("\nPhase 2: D=8 incremental", flush=True)
# Free JAX memory from D=6
del Fj6, Jj6; gc.collect()

S8 = Z.setup(8); P8 = S8["P"]; nv8 = S8["nvar"]
idx8 = np.where(P8.deg >= 2)[0]; coldeg8 = np.tile(P8.deg[idx8], 16)
keep8 = S8["keep"]; rt8 = S8["rowtype"][keep8]; rd8 = S8["rowdeg"][keep8]
level8 = np.where(rt8 == 1, rd8, np.where(rt8 == 2, rd8 + 1, rd8 + 2))
print(f"  D8: nvar={nv8}, neq_kept={len(keep8)}", flush=True)

# Embed z6 into D=8
P6 = S6["P"]; idx6 = np.where(P6.deg >= 2)[0]
pos8 = {tuple(P8.L[c_]): k for k, c_ in enumerate(idx8)}
z6_arr = np.asarray(z6).reshape(16, len(idx6))
z8 = np.zeros((16, len(idx8)))
for k, c_ in enumerate(idx6):
    mon = tuple(P6.L[c_])
    if mon in pos8: z8[:, pos8[mon]] = z6_arr[:, k]
z8_base = z8.ravel()

# Identify new unknowns (degree 7,8) and new equations (level 7,8)
hi_cols = np.where((coldeg8 >= 7))[0]
new_rows = np.where(level8 >= 7)[0]
# also equations that involve high-degree unknowns but at lower levels
# (E3 deg 5 involves g through degree 7, so level 7; already captured)
print(f"  new unknowns (deg7+8): {len(hi_cols)}", flush=True)
print(f"  new equations (lev7+8): {len(new_rows)}", flush=True)

# Compile only the system function (no Jacobian yet)
sysf8 = jax.jit(lambda z: S8["system"](z, lam)[jnp.array(keep8)])
mvf8 = jax.jit(lambda z: Z.Mvec(S8, z))
print("  compiling D=8 system...", flush=True)
z8j = jnp.array(z8_base)
r_full = np.asarray(sysf8(z8j))
mv8 = np.asarray(mvf8(z8j))
r_old = r_full[np.where(level8 < 7)[0]]
r_new = r_full[new_rows]
print(f"  old-level res2={np.sum(r_old**2):.3e}, new-level res2={np.sum(r_new**2):.3e}, Mvec_err={np.linalg.norm(mv8-mt):.3e}", flush=True)
print(f"  compile+eval ({time.time()-t0:.1f}s)", flush=True)

# Compute incremental Jacobian by finite differences (column by column, batched)
print(f"  computing incremental Jacobian ({len(new_rows)} x {len(hi_cols)}) by finite diff...", flush=True)
eps = 1e-7
J_inc = np.zeros((len(new_rows), len(hi_cols)))
batch = 50; done = 0
for i0 in range(0, len(hi_cols), batch):
    ib = min(batch, len(hi_cols) - i0)
    for jj in range(ib):
        col = i0 + jj
        z_p = z8_base.copy(); z_p[hi_cols[col]] += eps
        r_p = np.asarray(sysf8(jnp.array(z_p)))[new_rows]
        J_inc[:, col] = (r_p - r_new) / eps
    done += ib
    if done % 200 == 0 or done == len(hi_cols):
        print(f"    {done}/{len(hi_cols)} ({time.time()-t0:.1f}s)", flush=True)

# SVD of incremental Jacobian
print("  SVD...", flush=True)
U, s, Vt = np.linalg.svd(J_inc, full_matrices=True)
rank = int((s > 1e-8 * s[0]).sum())
coker_dim = len(new_rows) - rank
print(f"  rank={rank}, cokernel_dim={coker_dim}", flush=True)

# Project residual onto range and cokernel
b = r_new
b_range = U[:, :rank] @ (U[:, :rank].T @ b)
b_coker = b - b_range
print(f"  ||b_range||={np.linalg.norm(b_range):.6e}", flush=True)
print(f"  ||b_coker||={np.linalg.norm(b_coker):.6e}  <-- OBSTRUCTION", flush=True)

# Least-squares solve
y_ls = -Vt[:rank].T @ ((1.0/s[:rank]) * (U[:, :rank].T @ b))
z8_ls = z8_base.copy(); z8_ls[hi_cols] += y_ls
r_ls = np.asarray(sysf8(jnp.array(z8_ls)))[new_rows]
ls_res2 = float(np.sum(r_ls**2))
print(f"  LS residual (new eqs): {ls_res2:.6e}", flush=True)

# Full residual after LS
r_full_ls = np.asarray(sysf8(jnp.array(z8_ls)))
r_old_ls = r_full_ls[np.where(level8 < 7)[0]]
print(f"  old-level after LS: {np.sum(r_old_ls**2):.6e}", flush=True)

# Residual breakdown by equation type and degree
bydeg = {}
for k_, ri in zip(keep8, r_full_ls):
    key = f"E{rt8[np.searchsorted(keep8, k_)]}_d{rd8[np.searchsorted(keep8, k_)]}"
    bydeg[key] = bydeg.get(key, 0.0) + float(ri**2)
top_blocks = dict(sorted(bydeg.items(), key=lambda kv: -kv[1])[:8])
print(f"  worst blocks after LS: {top_blocks}", flush=True)

result = {
    "target": "A02 shared (c=1,S=[[2,1],[1,1+i]],a=2+2i)", "lam": lam,
    "D6_sys_res2": r6_sys, "D6_Mvec_err2": r6_mv,
    "D8_nvar": nv8, "D8_neq": len(keep8),
    "new_unknowns": int(len(hi_cols)), "new_equations": int(len(new_rows)),
    "embed_old_res2": float(np.sum(r_old**2)), "embed_new_res2": float(np.sum(r_new**2)),
    "J_inc_rank": rank, "J_inc_coker_dim": coker_dim,
    "b_range_norm": float(np.linalg.norm(b_range)),
    "b_coker_norm": float(np.linalg.norm(b_coker)),
    "LS_new_res2": ls_res2, "LS_old_res2": float(np.sum(r_old_ls**2)),
    "top_blocks_after_LS": top_blocks,
    "sv_top10": s[:10].tolist(), "sv_at_rank": float(s[rank-1]) if rank > 0 else 0,
    "sv_below_rank": float(s[rank]) if rank < len(s) else 0,
    "conclusion": "OBSTRUCTION" if float(np.linalg.norm(b_coker)) > 1e-4 else "COMPATIBLE",
    "time": time.time() - t0
}
print(f"\n=== RESULT: {result['conclusion']} ===")
print(f"cokernel norm = {result['b_coker_norm']:.6e}")
json.dump(result, open(os.path.join(OUT, "staged_D8_a02.json"), "w"), indent=1, default=float)
print(f"\nDone ({time.time()-t0:.1f}s)")

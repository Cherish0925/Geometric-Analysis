"""Step 66b: D=8 (Ricci through degree 6) solve at a prescribed first torsion jet.

Usage: python step66_D8_solve.py TARGET LAM NSTART ITERS [WARM]
  TARGET in {a02, gh, kahler}; a02 = A02 shared cone jet (c=1,S=[[2,1],[1,1+i]],a=2+2i),
  gh = Gibbons-Hawking first jet (lam must be 0; existence control), kahler = zero torsion jet (KE control).
  WARM=1: first start is a warm start from the D=6 solution embedded into D=8 monomials.
Output: data/step66/D8_<TARGET>_l<LAM>.json
"""
import os, sys, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from step62_zero_prolong import setup, Mvec, lm, gh_jets
from step66_A02_test_jet import build_F_from_cSA

OUT = os.path.join(HERE, "..", "data", "step66"); os.makedirs(OUT, exist_ok=True)
lin = np.load(os.path.join(HERE, "..", "data", "step62", "linear.npz")); Lb = lin["Lb"]

def a02_target():
    c = 1+0j; S = np.array([[2, 1], [1, 1+1j]]); A = np.array([[0, 2+2j], [-(2+2j), 0]])
    F, _, _ = build_F_from_cSA(c, S, A)
    coef, *_ = np.linalg.lstsq(Lb[:16], F.T.ravel(), rcond=None)
    return Lb @ coef

def embed(z_lo, S_lo, S_hi):
    """Embed a degree-D_lo jet vector into the degree-D_hi variable layout (higher coefficients zero)."""
    P_lo, P_hi = S_lo["P"], S_hi["P"]
    idx_lo = np.where(P_lo.deg >= 2)[0]; idx_hi = np.where(P_hi.deg >= 2)[0]
    pos_hi = {tuple(P_hi.L[c]): k for k, c in enumerate(idx_hi)}
    zl = z_lo.reshape(16, len(idx_lo)); zh = np.zeros((16, len(idx_hi)))
    for k, c in enumerate(idx_lo): zh[:, pos_hi[tuple(P_lo.L[c])]] = zl[:, k]
    return zh.ravel()

def residual_fn(S, lam, mt):
    keep = jnp.array(S["keep"]); mtj = jnp.array(mt)
    F = lambda z: jnp.concatenate([S["system"](z, lam)[keep], Mvec(S, z) - mtj])
    return jax.jit(F), jax.jit(jax.jacfwd(F))

def blocks(S, z, lam):
    sysr = np.asarray(S["system"](jnp.array(z), lam))[S["keep"]]; b = {}
    for k_, ri in zip(S["keep"], sysr):
        key = f"E{S['rowtype'][k_]}_d{S['rowdeg'][k_]}"; b[key] = b.get(key, 0.0) + float(ri**2)
    return {k: v for k, v in sorted(b.items(), key=lambda kv: -kv[1])[:6]}

def main():
    tgt, lam, nstart, iters = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    warm = len(sys.argv) > 5 and sys.argv[5] == "1"
    t0 = time.time()
    if tgt == "a02": mt = a02_target()
    elif tgt == "gh":
        _, zg = gh_jets(6, 0.5); mt = np.asarray(Mvec(setup(6), jnp.array(zg)))
    elif tgt == "kahler": mt = np.zeros(32)
    else: raise ValueError(tgt)
    out = {"target": tgt, "lam": lam, "target_det": float(np.linalg.det(mt[:16].reshape(4, 4))), "runs": []}
    S8 = setup(8); R8, J8 = residual_fn(S8, lam, mt)
    out["nvar"] = S8["nvar"]; out["neq"] = int(len(S8["keep"]) + 32)
    print("setup D8", out["nvar"], out["neq"], time.time()-t0, flush=True)
    starts = []
    if warm:
        S6 = setup(6); R6, J6 = residual_fn(S6, lam, mt)
        z6 = np.random.default_rng(7).standard_normal(S6["nvar"])*0.05
        # continuation at D=6 to reach the target (the D=6 system is known to be solvable on the cone)
        def F6t(z, t): return jnp.concatenate([S6["system"](z, lam)[jnp.array(S6["keep"])], Mvec(S6, z) - t*jnp.array(mt)])
        F6j = jax.jit(F6t); J6j = jax.jit(jax.jacfwd(F6t))
        for t in np.linspace(0, 1, 11):
            z6, f6, *_ = lm(lambda zz: F6j(zz, t), lambda zz: J6j(zz, t), z6, 60)
        out["D6_res2"] = f6; print("D6 warm res2", f6, time.time()-t0, flush=True)
        np.save(os.path.join(OUT, f"D6_{tgt}_l{lam}_z.npy"), z6)
        starts.append(("warm_D6", embed(z6, S6, S8)))
    rng = np.random.default_rng(11)
    for k in range(nstart): starts.append((f"rand{k}", rng.standard_normal(S8["nvar"])*0.1))
    for name, z in starts:
        z, f, hist, gn, Jm, r = lm(R8, J8, z, iters)
        sv = np.linalg.svd(Jm, compute_uv=False)
        run = {"start": name, "res2": f, "iters": len(hist)-1, "grad_norm": gn, "hist": hist[::max(1, len(hist)//12)] + [hist[-1]],
               "Merr": float(np.linalg.norm(np.asarray(Mvec(S8, jnp.array(z))) - mt)),
               "jac_rank": int((sv > 1e-10*sv[0]).sum()), "blocks": blocks(S8, z, lam), "time": time.time()-t0}
        out["runs"].append(run); print(json.dumps(run), flush=True)
        if f < 1e-24: np.save(os.path.join(OUT, f"D8_{tgt}_l{lam}_{name}_z.npy"), z)
        json.dump(out, open(os.path.join(OUT, f"D8_{tgt}_l{lam}.json"), "w"), indent=1)

if __name__ == "__main__":
    main()

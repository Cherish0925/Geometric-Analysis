"""Step 54: fixed-lower-jet prolongation for the almost-Kahler Einstein system.

This corrects the interpretation of the degree ladder in step53_ak_einstein_jets.py.
Given a solved degree-D jet z_D, hold every coefficient through degree D fixed and
write the new degree-(D+1) equations as

    A_D u_top + b_D(j_low) = 0.

Here u_top consists only of the degree-(D+1) coefficients of g and omega.  The
new equations are compatibility E1 in degree D+1, closure E2 in degree D, and
Einstein E3 in degree D-1.  Since the PDE has order two, these equations are
affine-linear in u_top.  The orthogonal projection of b_D to coker(A_D),
represented by the least-squares residual, is the actual numerical extension
test for this specified lower jet.  A rank count alone is not interpreted as
an obstruction.

Usage:
  python step54_ak_prolong.py TAG D0 DMAX [run_index]

Reads data/step53_jets/akjets_<TAG>_z<run_index>.npy, extends sequentially, and
writes data/step54_prolong/prolong_<TAG>_z<run_index>_to_D<DMAX>.json plus each
extended jet.  DMAX is intentionally modest: finite formal compatibility is
not local analytic existence.
"""
import os, sys, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
from step53_ak_einstein_jets import setup

HERE = os.path.dirname(os.path.abspath(__file__))
DATA53 = os.path.join(HERE, "..", "data", "step53_jets")
OUT = os.path.join(HERE, "..", "data", "step54_prolong")
os.makedirs(OUT, exist_ok=True)


def unpack_vector_layout(z, D):
    """Return component coefficient arrays for the unknown parts at degree <=D."""
    P, unpack, residual, nvar, ng, nw = setup(D)
    gmask = np.asarray(P.deg >= 2)
    wmask = np.asarray(P.deg >= 1)
    gz = np.asarray(z[:10*ng]).reshape(10, ng)
    wz = np.asarray(z[10*ng:]).reshape(6, nw)
    return P, gz, wz


def embed_lower(zold, Dold, Dnew):
    """Embed a degree-Dold unknown vector into degree-Dnew, zero in new degrees."""
    assert Dnew == Dold + 1
    Po, go, wo = unpack_vector_layout(zold, Dold)
    Pn, unpack, residual, nvar, ng, nw = setup(Dnew)
    gn = np.zeros((10, ng)); wn = np.zeros((6, nw))
    # Monomial lists are nested degree by degree. Copy compressed component
    # positions by exponent for robustness.
    old_g_mons = [a for a in Po.L if sum(a) >= 2]
    old_w_mons = [a for a in Po.L if sum(a) >= 1]
    new_g_pos = {a: i for i, a in enumerate([a for a in Pn.L if sum(a) >= 2])}
    new_w_pos = {a: i for i, a in enumerate([a for a in Pn.L if sum(a) >= 1])}
    for i, a in enumerate(old_g_mons): gn[:, new_g_pos[a]] = go[:, i]
    for i, a in enumerate(old_w_mons): wn[:, new_w_pos[a]] = wo[:, i]
    return Pn, residual, np.concatenate([gn.ravel(), wn.ravel()]), ng, nw


def prolong_once(zold, Dold, lam, q0, rtol=1e-11):
    N = Dold + 1
    P, residual, zbase, ng, nw = embed_lower(zold, Dold, N)
    deg = np.asarray(P.deg)
    g_unknown_mons = [a for a in P.L if sum(a) >= 2]
    w_unknown_mons = [a for a in P.L if sum(a) >= 1]
    gpos = {a: i for i, a in enumerate(g_unknown_mons)}
    wpos = {a: i for i, a in enumerate(w_unknown_mons)}
    top = [a for a in P.L if sum(a) == N]
    nt = len(top)
    n_top = 16*nt

    # Positions in the full unknown vector occupied by top-degree coefficients.
    topvar = []
    for c in range(10):
        topvar += [c*ng + gpos[a] for a in top]
    offw = 10*ng
    for c in range(6):
        topvar += [offw + c*nw + wpos[a] for a in top]
    topvar = np.asarray(topvar, dtype=int)

    # Positions in flattened residual carrying the newly imposed exact degrees.
    M = P.M
    idx1 = np.where(deg == N)[0]       # E1 degree N
    idx2 = np.where(deg == N-1)[0]     # E2 degree N-1
    idx3 = np.where(deg == N-2)[0]     # E3 degree N-2
    eqpos = []
    sector_slices = {}
    a0 = 0
    for c in range(10): eqpos += (c*M + idx1).tolist()
    sector_slices["E1_compat"] = [a0, len(eqpos)]; a0 = len(eqpos)
    off2 = 10*M
    for c in range(4): eqpos += (off2 + c*M + idx2).tolist()
    sector_slices["E2_closed"] = [a0, len(eqpos)]; a0 = len(eqpos)
    off3 = 14*M
    for c in range(10): eqpos += (off3 + c*M + idx3).tolist()
    sector_slices["E3_Einstein"] = [a0, len(eqpos)]
    eqpos = np.asarray(eqpos, dtype=int)

    zbase_j = jnp.array(zbase)
    topvar_j = jnp.array(topvar)
    eqpos_j = jnp.array(eqpos)
    def Rtop(u):
        z = zbase_j.at[topvar_j].set(u)
        return residual(z, lam, q0, 1.0)[eqpos_j]
    Rj = jax.jit(Rtop)
    Jj = jax.jit(jax.jacfwd(Rtop))
    u0 = jnp.zeros(n_top)
    b = np.asarray(Rj(u0)); A = np.asarray(Jj(u0))

    t0 = time.time()
    # gelsd returns the singular spectrum and a minimum-norm solution.
    u, _, rank, sval = np.linalg.lstsq(A, -b, rcond=rtol)
    proj = A @ u + b
    aff_err = np.asarray(Rj(jnp.array(u))) - proj
    znew = zbase.copy(); znew[topvar] = u

    sec = {}
    for name, (i, j) in sector_slices.items():
        sec[name] = {"source_norm": float(np.linalg.norm(b[i:j])),
                     "cokernel_projection_norm": float(np.linalg.norm(proj[i:j]))}
    return znew, {
        "from_D": Dold, "to_D": N, "lam": lam, "q0": q0,
        "n_top_unknown": int(n_top), "n_new_equations": int(len(eqpos)),
        "symbol_rank": int(rank), "symbol_cokernel_dim": int(len(eqpos)-rank),
        "symbol_kernel_dim": int(n_top-rank),
        "source_norm": float(np.linalg.norm(b)),
        "cokernel_projection_norm": float(np.linalg.norm(proj)),
        "relative_projection": float(np.linalg.norm(proj)/max(np.linalg.norm(b), 1e-300)),
        "affine_linearity_error": float(np.linalg.norm(aff_err)),
        "largest_singular": float(sval[0]) if len(sval) else None,
        "smallest_retained_singular": float(sval[rank-1]) if rank else None,
        "sector_norms": sec, "lstsq_seconds": time.time()-t0,
        "interpretation": "Extension of this fixed lower jet succeeds numerically only if the cokernel projection is at roundoff scale; rank by itself is not an obstruction."
    }


def main():
    tag = sys.argv[1]; D0 = int(sys.argv[2]); Dmax = int(sys.argv[3]); iz = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    meta = json.load(open(os.path.join(DATA53, f"akjets_{tag}.json")))
    lam, q0 = float(meta["lam"]), float(meta["q0"])
    src = os.path.join(DATA53, f"akjets_{tag}_z{iz}.npy")
    z = np.load(src)
    out = {"tag": tag, "source": src, "D0": D0, "Dmax": Dmax, "lam": lam, "q0": q0,
           "q_over_abs_lambda": None if lam == 0 else q0/abs(lam), "steps": []}
    for D in range(D0, Dmax):
        z, rec = prolong_once(z, D, lam, q0)
        out["steps"].append(rec)
        np.save(os.path.join(OUT, f"prolong_{tag}_z{iz}_D{D+1}.npy"), z)
        print(json.dumps(rec), flush=True)
    dst = os.path.join(OUT, f"prolong_{tag}_z{iz}_to_D{Dmax}.json")
    json.dump(out, open(dst, "w"), indent=1)
    print(dst, flush=True)

if __name__ == "__main__":
    main()

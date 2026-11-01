"""Step 50b: find a closed-form W^- corrector k0^W in a basis of natural tensors.

Builds natural degree-0 symmetric tensors linear in A = h_W/|x|^2 from x, the projectors
Pr = xx^T/u, K = (v0v0^T+v1v1^T)/u (Burns-enlarged plane), P3 = v2v2^T/u (Burns fibre), and the
complex structures J_m, then solves (Lw,Ls)(k0) = -(S_W, sigma_W) pointwise in least squares,
reports the residual and a sparse rational representative.
Usage: python step50_natural_corrector.py
"""
import os, sys, json, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import step50_wminus_compatibility as W

OUT = W.OUT
Jm = W.Jm_j

def natural(x):
    u = x@x; v = W.vvec(x)
    A = W.hW(x)/u
    Pr = jnp.outer(x, x)/u
    K = (jnp.outer(v[0], v[0]) + jnp.outer(v[1], v[1]))/u
    P3 = jnp.outer(v[2], v[2])/u
    I = jnp.eye(4)
    mats = {"I": I, "K": K, "P3": P3, "J0": Jm[0], "J1": Jm[1], "J2": Jm[2]}
    out, names = [], []
    keys = list(mats)
    for i, a in enumerate(keys):
        for b in keys[i:]:
            X = mats[a] @ A @ mats[b].T
            out.append(0.5*(X + X.T)); names.append(f"sym({a} A {b}^T)")
    # scalar contractions times projectors / mixed tensors
    sc = {"trP3A": jnp.trace(P3@A), "v0Av1": v[0]@A@v[1]/u, "v0Av0-v1Av1": (v[0]@A@v[0]-v[1]@A@v[1])/u,
          "v0Av2": v[0]@A@v[2]/u, "v1Av2": v[1]@A@v[2]/u}
    tens = {"I": I, "Pr": Pr, "K": K, "P3": P3}
    for m in range(3):
        for n in range(m, 3):
            tens[f"v{m}v{n}"] = 0.5*(jnp.outer(v[m], v[n]) + jnp.outer(v[n], v[m]))/u
        tens[f"xv{m}"] = 0.5*(jnp.outer(x, v[m]) + jnp.outer(v[m], x))/u
    for sn, s in sc.items():
        for tn, t in tens.items():
            out.append(s*t); names.append(f"{sn}*{tn}")
    return jnp.stack(out), names

_, NAMES = natural(jnp.array([0.3, 0.1, 0.5, 0.2]))

def main():
    NS, NXI = 14, 24
    def per_point(x):
        S, *_ = W.source_point(x, W.hW)
        f = lambda y: natural(y)[0]
        K = f(x); dK = jax.jacfwd(f)(x); ddK = jax.jacfwd(jax.jacfwd(f))(x)
        L = jax.vmap(W.lin_flat)(K, dK, ddK)
        return S, L
    pp = jax.jit(jax.vmap(per_point))
    sn, sw = np.polynomial.legendre.leggauss(NS); sn = 0.5*(sn+1); sw = 0.5*sw
    xi = 2*np.pi*np.arange(NXI)/NXI; xw = 2*np.pi/NXI
    pts, wts = [], []
    for s_, w in zip(sn, sw):
        for a in xi:
            for b in xi:
                pts.append([np.sqrt(1-s_)*np.cos(a), np.sqrt(1-s_)*np.sin(a), np.sqrt(s_)*np.cos(b), np.sqrt(s_)*np.sin(b)])
                wts.append(0.5*w*xw*xw)
    pts = np.array(pts); wts = np.array(wts)
    outs = [pp(jnp.array(pts[i:i+256])) for i in range(0, len(pts), 256)]
    S = np.concatenate([np.array(o[0]) for o in outs]); L = np.concatenate([np.array(o[1]) for o in outs])
    nb = L.shape[1]
    wvec = np.concatenate([4*np.ones(9), [1/12]])
    sq = np.sqrt(wts)[:, None]*np.sqrt(wvec)[None, :]
    A = (sq[:, None, :]*L[:, :, :10]).transpose(0, 2, 1).reshape(-1, nb)
    b = (sq*S[:, :10]).reshape(-1)
    sol, *_ = np.linalg.lstsq(A, -b, rcond=1e-12)
    r = A@sol + b
    res = {"nnat": nb, "kappa_natural": float(r@r)/(8*np.pi**2), "S2": float(b@b)/(8*np.pi**2)}
    # greedy sparse search: smallest subsets giving zero residual
    G = A.T@A; g = A.T@b; bb = b@b
    colnorm = np.sqrt(np.diag(G))
    good = [i for i in range(nb) if colnorm[i] > 1e-8]
    best = None
    for size in range(1, 5):
        for sub in itertools.combinations(good, size):
            sub = list(sub)
            Gs = G[np.ix_(sub, sub)]
            try:
                c = -np.linalg.solve(Gs, g[sub])
            except np.linalg.LinAlgError:
                continue
            rr = bb + g[sub]@c
            if rr < 1e-18*bb:
                best = (sub, c); break
        if best: break
        print("no exact subset of size", size, flush=True)
    if best:
        res["sparse"] = {NAMES[i]: float(ci) for i, ci in zip(best[0], best[1])}
    print(json.dumps(res, indent=1))
    json.dump(res, open(os.path.join(OUT, "natural_corrector.json"), "w"), indent=1)
    np.savez(os.path.join(OUT, "natural_corrector.npz"), A=A, b=b, names=np.array(NAMES))

if __name__ == "__main__":
    main()

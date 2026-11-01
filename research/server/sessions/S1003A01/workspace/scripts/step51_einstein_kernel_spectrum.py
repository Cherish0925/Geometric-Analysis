"""Step 51: Verify the general Einstein log coefficient Φ on the kernel locus.

Einstein background with W+ eigenvalues (w, -2-w, 2) in (J1,J2,J3) basis, ζ=J3 in ker R+.
Uses quadratic normal-coordinate jet: g = δ + h2(x;w), exact for the log coefficient.

h2(x; w) = c1(w)*v1v1^T + c2(w)*v2v2^T + c3*v3v3^T
  c1 = 2/3 - w/6,  c2 = 1 + w/6,  c3 = 1/3

A02's formula: Φ = -μ1(μ1-μ2-μ3)/2 - (μ2-μ3)^2/2,  μ_i = W+_i + s/12 (R+ eigenvalues).
On the kernel locus μ3=0:  Φ = -(μ1-μ2)^2/2 = -2(w+1)^2.

Sweep w ∈ {-4, -3, -2, -1, 0, 1, 2} to verify the quadratic law.
"""
import sys, os, json, time, math, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step51")
os.makedirs(OUT, exist_ok=True)

# ---------- quaternion left-invariant coframe
def qmul(p, q):
    a1,b1,c1,d1 = p; a2,b2,c2,d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
def conj(q): return np.array([q[0],-q[1],-q[2],-q[3]])
E4 = np.eye(4)
Jm = np.zeros((3,4,4))
for c in range(4):
    for b in range(4):
        prod = qmul(conj(E4[c]), E4[b])
        for m in range(3):
            Jm[m,b,c] = prod[m+1]
Jm_j = jnp.array(Jm)
def vvec(x): return jnp.einsum('mbc,c->mb', Jm_j, x)

Esym = []
for a in range(4):
    for b in range(a,4):
        E = np.zeros((4,4)); E[a,b] = E[b,a] = 1.0
        Esym.append(E)
Esym = jnp.array(Esym)  # (10,4,4)

def monomials(x, deg):
    u = x@x
    if deg == 0:
        return jnp.ones((1,), dtype=x.dtype)
    idx = list(itertools.combinations_with_replacement(range(4), deg))
    return jnp.stack([jnp.prod(x[jnp.array(i)]) for i in idx]) / u**(deg//2)

# ---------- Background metric: Einstein with W+ eigenvalues (w, -2-w, 2) in J-basis
def gb_einstein(x, w):
    """Quadratic normal-coordinate jet for Einstein, s=-24, W-=0."""
    v = vvec(x)
    c1 = 2.0/3.0 - w/6.0
    c2 = 1.0 + w/6.0
    c3 = 1.0/3.0
    return jnp.eye(4, dtype=x.dtype) + c1*jnp.outer(v[0],v[0]) + c2*jnp.outer(v[1],v[1]) + c3*jnp.outer(v[2],v[2])

# ---------- Ricci from metric jets (same as step49)
def ric0_alg(g, dg, ddg):
    gi = jnp.linalg.inv(g)
    Gl = 0.5*(dg.transpose(0,2,1) + dg - jnp.einsum('bcd->dbc', dg))
    G = jnp.einsum('ad,dbc->abc', gi, Gl)
    dGl = 0.5*(ddg.transpose(0,2,1,3) + ddg - jnp.einsum('bcde->dbce', ddg))
    dgi = -jnp.einsum('am,mne,nd->ade', gi, dg, gi)
    dG = jnp.einsum('ade,dbc->abce', dgi, Gl) + jnp.einsum('ad,dbce->abce', gi, dGl)
    R = (jnp.einsum('abca->bc', dG) - jnp.einsum('aabc->bc', dG)
         + jnp.einsum('aad,dbc->bc', G, G) - jnp.einsum('acd,dab->bc', G, G))
    s = jnp.einsum('ij,ij->', gi, R)
    return R - 0.25*s*g

# ---------- Build corrector+Burns basis
ANG = 4  # angular degree of correctors
def kstack(x):
    u = x@x; v = vvec(x)
    named = jnp.stack([
        (jnp.outer(v[0],v[0]) + jnp.outer(v[1],v[1]))/u**2,  # Burns kB
    ])
    mons = jnp.concatenate([monomials(x, d) for d in range(0, ANG+1, 2)])
    gen = jnp.einsum('m,eij->meij', mons, Esym).reshape(-1, 4, 4)
    return jnp.concatenate([named, gen])

NB_TEST = kstack(jnp.array([0.3, 0.2, 0.1, 0.5])).shape[0]
print(f"Corrector basis dimension: {NB_TEST}", flush=True)

# ---------- Per-point evaluation: background depends on w
def per_point(xw):
    """xw = (x[0..3], w) complex."""
    x = xw[:4]; w = xw[4]
    gb_fn = lambda xx: gb_einstein(xx, w)
    g = gb_fn(x)
    dg = jax.jacfwd(gb_fn, holomorphic=True)(x)
    ddg = jax.jacfwd(jax.jacfwd(gb_fn, holomorphic=True), holomorphic=True)(x)
    K = kstack(x)
    dK = jax.jacfwd(kstack, holomorphic=True)(x)
    ddK = jax.jacfwd(jax.jacfwd(kstack, holomorphic=True), holomorphic=True)(x)
    lin = lambda k, dk, ddk: jax.jvp(ric0_alg, (g, dg, ddg), (k, dk, ddk))[1]
    Rs = jax.vmap(lin)(K, dK, ddK)  # (nb,4,4)
    gi = jnp.linalg.inv(g); sd = jnp.sqrt(jnp.linalg.det(g))
    Rup = jnp.einsum('ik,akl,lj->aij', gi, Rs, gi)  # raised indices
    Gm = jnp.einsum('aij,bij->ab', Rup, Rs) * sd     # quadratic form
    Rb = ric0_alg(g, dg, ddg) + 6.0*g  # Ric + 6g (should be ~ Ric0 for Einstein bg)
    resid = jnp.max(jnp.abs(Rb))
    return Gm, resid

pp_jit = jax.jit(jax.vmap(per_point))

# ---------- S^3 quadrature and Cauchy extraction
NS, NXI, M, RHO = 12, 20, 24, 0.3

sn, sw = np.polynomial.legendre.leggauss(NS); sn = 0.5*(sn+1); sw = 0.5*sw
xi = 2*np.pi*np.arange(NXI)/NXI; xw = 2*np.pi/NXI
pts, wts = [], []
for s_, w_ in zip(sn, sw):
    for a in xi:
        for b in xi:
            pts.append([math.sqrt(1-s_)*math.cos(a), math.sqrt(1-s_)*math.sin(a),
                        math.sqrt(s_)*math.cos(b), math.sqrt(s_)*math.sin(b)])
            wts.append(0.5*w_*xw*xw)
pts = np.array(pts); wts = np.array(wts)
lam = RHO * np.exp(2j*np.pi*(np.arange(M)+0.5)/M)
print(f"S^3 volume check: {wts.sum():.6f} (should be {2*np.pi**2:.6f})", flush=True)
print(f"Quadrature: {NS}×{NXI}²={len(pts)} S³ pts, {M} Cauchy pts", flush=True)

def compute_F(w_val):
    """Compute the optimized log coefficient F for Einstein bg with parameter w."""
    nb = NB_TEST
    Q = np.zeros((nb, nb), dtype=np.complex128)
    maxres = 0.0
    allx = (lam[None,:,None]*pts[:,None,:]).reshape(-1, 4)
    allw_arr = np.full(allx.shape[0], w_val, dtype=np.complex128)
    allxw = np.concatenate([allx, allw_arr[:,None]], axis=1)
    allwt = (wts[:,None]*lam[None,:]**4/M).reshape(-1)
    CH = 64
    for i in range(0, allxw.shape[0], CH):
        batch = jnp.array(allxw[i:i+CH])
        Gm, res = pp_jit(batch)
        Gm = np.array(Gm); n = Gm.shape[0]
        for j in range(n):
            Q += allwt[i+j] * Gm[j]
        maxres = max(maxres, float(np.max(np.abs(np.array(res)))))
    Qr = Q.real
    F = Qr / (8*np.pi**2)
    # Optimize: minimize e^T F e subject to e[0]=1 (Burns coefficient)
    # F_opt = F[0,0] + min_{c} 2*F[0,1:]*c + c^T*F[1:,1:]*c
    A = F[1:, 1:]
    b = F[0, 1:]
    w_eig, V = np.linalg.eigh(A)
    keep = w_eig > 1e-9 * max(1, abs(w_eig).max())
    Ainv = (V[:, keep] / w_eig[keep]) @ V[:, keep].T
    sol = -Ainv @ b
    F_opt = F[0,0] + b @ sol
    F_burns = float(F[0,0])
    return dict(w=w_val, F_opt=float(F_opt), F_burns_only=F_burns,
                null_modes=int(np.sum(~keep)), max_bg_residual=maxres,
                max_imag=float(np.max(np.abs(Q.imag))))

# ---------- Sweep
w_values = [-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0]
results = []
t0 = time.time()
for w_val in w_values:
    print(f"\n--- w = {w_val} ---", flush=True)
    tw = time.time()
    r = compute_F(w_val)
    r['time'] = time.time() - tw
    # A02 prediction: Phi = -2*(w+1)^2
    r['A02_prediction'] = -2.0*(w_val+1)**2
    r['difference'] = r['F_opt'] - r['A02_prediction']
    results.append(r)
    print(json.dumps(r, indent=1), flush=True)

print(f"\nTotal time: {time.time()-t0:.1f} s", flush=True)
print("\n=== Summary ===")
print(f"{'w':>6} {'F_opt':>12} {'Φ=-2(w+1)²':>12} {'diff':>12}")
for r in results:
    print(f"{r['w']:6.1f} {r['F_opt']:12.6f} {r['A02_prediction']:12.6f} {r['difference']:12.2e}")

json.dump(results, open(os.path.join(OUT, "kernel_spectrum_sweep.json"), "w"), indent=1)
print(f"\nSaved to {OUT}/kernel_spectrum_sweep.json")
